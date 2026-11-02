# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 287. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_destiny_hardening.py::module::root::Module

Source: `infra/tests/test_destiny_hardening.py:1`; AST `6318a03b008502a451530e7b6cfd154edc0b31b4d8c4cd92706ff4c50b01de02`.

Rust module: `infra::tests::test_destiny_hardening`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: DestinyFixture, Path, ValueError, __file__, __name__, altered, archive, before, checked_output, checksum, commands, configured, data, directory, edited, entry, env, files, good, hashlib, home, ids, implementation, invalid, io, json, len, list, member, name, obligation, path, receipt, registry_source_files, release, replace, reservations, response, result, row, run_process, scoped_kani_commands, scoped_verus_commands, self, set, source, source_snapshot, str, subprocess, sys, tarfile, text, third, tree, unittest. Outputs/bindings: altered, archive, before, checksum, commands, configured, data, directory, edited, entry, env, files, good, home, ids, implementation, invalid, member, name, obligation, path, receipt, release, reservations, response, result, row, source, text, third, tree.
Calls/effect boundaries: (directory / '.aegis').mkdir, (directory / '.aegis/receipt.json').write_text, (directory / '.cargo').mkdir, (directory / '.cargo/config.toml').write_text, (directory / '.gitignore').write_text, (directory / 'source.rs').write_text, (directory / 'untracked.rs').write_text, (self.root / '.aegis/destiny/attempts').glob, (self.root / 'ordinary').mkdir, (tree / 'build.rs').write_text, Path, Path(__file__).resolve, Path.cwd, archive.parent.mkdir, archive.read_bytes, archive.write_bytes, checked_output, directory.mkdir, good.replace, hashlib.sha256, hashlib.sha256(archive.read_bytes()).hexdigest, implementation.write_text, io.BytesIO, json.loads, len, list, obligation.update, path.write_text, receipt.read_text, receipt.write_text, registry_source_files, release.addfile, replace, reservations[0].read_text, response['text'].encode, run_process, scoped_kani_commands, scoped_verus_commands, self.assertEqual, self.assertFalse, self.assertIn, self.assertLessEqual, self.assertNotEqual, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.call, self.write, set, source.read_bytes, source_snapshot, str, subprocess.run, sys.path.insert, tarfile.TarInfo, tarfile.open, text.replace, tree.mkdir, unittest.main.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:1`; AST `87c18ae2b20aea13abf437e073060bfc9d8812a9c5028fc2acec4275eeaa6e33`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_destiny_hardening.py:2`; AST `70bd9e0c4f1816b9f9f4b04c6c07c6303849eadd90de76e9a14084b9c76de162`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[2]::Import

Source: `infra/tests/test_destiny_hardening.py:3`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[3]::Import

Source: `infra/tests/test_destiny_hardening.py:4`; AST `eb75a54c5d0d93fbb694f468951613f2f071166afbbe97a52903fa47a7cef914`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[4]::Import

Source: `infra/tests/test_destiny_hardening.py:5`; AST `741092dea1f6a53333762688bf68b559454505d7bd20d5f8a7c366b2137afcb4`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[5]::Import

Source: `infra/tests/test_destiny_hardening.py:6`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_destiny_hardening.py:7`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[7]::Import

Source: `infra/tests/test_destiny_hardening.py:8`; AST `9d97d469cf8d66465563e1e22c6dab3b6107819aba2d9956c7080016c1ab9c1b`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[8]::Import

Source: `infra/tests/test_destiny_hardening.py:9`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[9]::Import

Source: `infra/tests/test_destiny_hardening.py:10`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Import evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_destiny_hardening.py:12`; AST `e6e65f5530a52602546758453e338fdf915fa82858a214cf46e5add3f8354038`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[11]::Expr

Source: `infra/tests/test_destiny_hardening.py:14`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[11].value::Call

Source: `infra/tests/test_destiny_hardening.py:14`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[11].value.args[1]::Call

Source: `infra/tests/test_destiny_hardening.py:14`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[11].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_destiny_hardening.py:14`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[11].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_destiny_hardening.py:14`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[11].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[12]::ImportFrom

Source: `infra/tests/test_destiny_hardening.py:15`; AST `c868fca8a1abb5a9d640edb5a5f35b4cbe26037bf059b2bc5a841eb5f304032b`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[13]::ImportFrom

Source: `infra/tests/test_destiny_hardening.py:16`; AST `255dfec4d6ff7dfa92dc78e143e11e331797115bca3317171a233bfe87c5edad`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[14]::ImportFrom

Source: `infra/tests/test_destiny_hardening.py:17`; AST `6b79dd98da3de94850519a5e4023106f4acc0dcb30498a6b5f0c6b030c24dfd1`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[15]::ImportFrom

Source: `infra/tests/test_destiny_hardening.py:18`; AST `20b875c04a5bc467b4634a4ab8c796f858cc4737c0f733bcb0cd515d85ffcf6a`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::root.body[16]::ClassDef

Source: `infra/tests/test_destiny_hardening.py:21`; AST `2fe038984bf1ff527d9ca9e93329e16f6cb1bf4203e77d54371c8233502b99fc`.

Rust module: `infra::tests::test_destiny_hardening`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Path, ValueError, altered, checked_output, commands, configured, entry, good, invalid, obligation, replace, result, run_process, scoped_kani_commands, scoped_verus_commands, self, sys, text, unittest. Outputs/bindings: altered, commands, configured, entry, good, invalid, obligation, result, text.
Calls/effect boundaries: Path.cwd, checked_output, good.replace, obligation.update, replace, run_process, scoped_kani_commands, scoped_verus_commands, self.assertEqual, self.assertFalse, self.assertRaises, self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:22`; AST `bf30690c4428860b25a9a73222c5549965542468b9e618bd153e5dedfc53beea`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, commands, invalid, scoped_kani_commands, self. Outputs/bindings: commands, invalid.
Calls/effect boundaries: scoped_kani_commands, self.assertEqual, self.assertRaises.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[0]::ImportFrom

Source: `infra/tests/test_destiny_hardening.py:23`; AST `56b4ef95c4599d5e937b667fde7f0e5cbde4740d806c2b33c83e94e4f91e93c6`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:24`; AST `d18aace0ad7e789a8e817592c2814b8cbfac6341f4b0958e3b4aa3af34eacd9e`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: commands.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[2]::Expr

Source: `infra/tests/test_destiny_hardening.py:26`; AST `bbd3caa0d6aec4202b1f420ed0ec0117851f66240b18aac2449de329da882a50`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: commands, scoped_kani_commands, self. Outputs/bindings: (none).
Calls/effect boundaries: scoped_kani_commands, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:26`; AST `2e340701d8e5ed2f52a199bafcb0a5c93bdf53e1c0c6ededa4299fd5c122ab97`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: commands, scoped_kani_commands, self. Outputs/bindings: (none).
Calls/effect boundaries: scoped_kani_commands, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[2].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:26`; AST `270f99dab901374d4689e3ab5b2de977841a87e2466a64b6627b7b34dd882785`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: commands, scoped_kani_commands. Outputs/bindings: (none).
Calls/effect boundaries: scoped_kani_commands.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[3]::For

Source: `infra/tests/test_destiny_hardening.py:30`; AST `e8a6799aada1d4b57a2f9406183dbaf6f5d2c3186ced57f9613e83ad625c5129`.

Rust module: `infra::tests::test_destiny_hardening`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ValueError, commands, invalid, scoped_kani_commands, self. Outputs/bindings: invalid.
Calls/effect boundaries: scoped_kani_commands, self.assertRaises.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered For evaluation at root.body[16].body[0].body[3]; no call, error or mutation may be omitted. Iteration: invalid in ([], commands + commands, [['kani']], [['cargo', 'kani', '--harness', 'other']], [['cargo', 'kani', '--output-format']])
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[3].body[0]::With

Source: `infra/tests/test_destiny_hardening.py:32`; AST `bc8e209699a1c5294b8e75c9c0bab13912a165178cddb0f99471fba578481086`.

Rust module: `infra::tests::test_destiny_hardening`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, invalid, scoped_kani_commands, self. Outputs/bindings: (none).
Calls/effect boundaries: scoped_kani_commands, self.assertRaises.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered With evaluation at root.body[16].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[3].body[0].items[0].context_expr::Call

Source: `infra/tests/test_destiny_hardening.py:32`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[3].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[3].body[0].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:32`; AST `2351f46872e56c938388e965208cc8e0ed505ad4a75e203be5252120eb2d9bd0`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: invalid, scoped_kani_commands. Outputs/bindings: (none).
Calls/effect boundaries: scoped_kani_commands.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_kani_preserves_features_contracts_and_exact_selection::root.body[16].body[0].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:32`; AST `2bf1c171fa11dab14a85eaedf6454e63bf45818340a65abdd695a31e7bc5105b`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: invalid, scoped_kani_commands. Outputs/bindings: (none).
Calls/effect boundaries: scoped_kani_commands.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:34`; AST `a404e4d3e66cd820712d8864df6bed2669ca491778521a6c5a1d4a26783fa9b1`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, commands, configured, entry, invalid, scoped_verus_commands, self. Outputs/bindings: commands, configured, entry, invalid.
Calls/effect boundaries: scoped_verus_commands, self.assertEqual, self.assertRaises.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[0]::ImportFrom

Source: `infra/tests/test_destiny_hardening.py:35`; AST `745b0205afb056bb282fa85dab8d9dbebdfe733a2dca000db6547e5949316ce0`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:36`; AST `4afede9d01359a75262891ab630cdeb91e021b32ee9773ed575e4f2167c62ec9`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: entry.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[2]::Assign

Source: `infra/tests/test_destiny_hardening.py:37`; AST `5d31bd312eb55c91e535d871c5cf615a6eb13426beb85b4b1d51eac76b1c8c83`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: configured.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[3]::Assign

Source: `infra/tests/test_destiny_hardening.py:38`; AST `ca3768f5b97583aeb9f9fa77a4f6e9255c1a98cd44288170f4fecc2b26e0c0bb`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: configured. Outputs/bindings: commands.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[4]::Expr

Source: `infra/tests/test_destiny_hardening.py:39`; AST `84b635254c14b10f39f8cfd96ba939e5df4d165a504e33cea03d760697868b1b`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: commands, configured, entry, scoped_verus_commands, self. Outputs/bindings: (none).
Calls/effect boundaries: scoped_verus_commands, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[4].value::Call

Source: `infra/tests/test_destiny_hardening.py:39`; AST `ddbf884364d9cf490638155c1cb894b84c6a10e4f85dcf1c323bcbb2c793f4a3`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: commands, configured, entry, scoped_verus_commands, self. Outputs/bindings: (none).
Calls/effect boundaries: scoped_verus_commands, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[4].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:39`; AST `ce84b38baa0a5e91326ec13d2e44aadd746c91648e5290c59cb3900ba3358c38`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: commands, entry, scoped_verus_commands. Outputs/bindings: (none).
Calls/effect boundaries: scoped_verus_commands.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[5]::For

Source: `infra/tests/test_destiny_hardening.py:41`; AST `fdf8700c205c740fa0e0f981b1a9aede7f0c32b20b22f550127a0888de49ad00`.

Rust module: `infra::tests::test_destiny_hardening`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ValueError, configured, entry, invalid, scoped_verus_commands, self. Outputs/bindings: invalid.
Calls/effect boundaries: scoped_verus_commands, self.assertRaises.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered For evaluation at root.body[16].body[1].body[5]; no call, error or mutation may be omitted. Iteration: invalid in ([], [configured, configured])
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[5].body[0]::With

Source: `infra/tests/test_destiny_hardening.py:42`; AST `00bf19bd7fef63d2000fc5d0611798672ca18cff568f2115a681da8ca031ad00`.

Rust module: `infra::tests::test_destiny_hardening`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, entry, invalid, scoped_verus_commands, self. Outputs/bindings: (none).
Calls/effect boundaries: scoped_verus_commands, self.assertRaises.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered With evaluation at root.body[16].body[1].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[5].body[0].items[0].context_expr::Call

Source: `infra/tests/test_destiny_hardening.py:42`; AST `757fbbfec408fbf0db315a7fa5a544664b7ff6342d5484602c617231b3fd903e`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[5].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[5].body[0].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:42`; AST `36c1f301185482215690d915859c268596cbcc6a431973fb85183ea0f822fcc8`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, invalid, scoped_verus_commands. Outputs/bindings: (none).
Calls/effect boundaries: scoped_verus_commands.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_scoped_verus_preserves_registered_configuration_and_exact_entry::root.body[16].body[1].body[5].body[0].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:42`; AST `e16cd0b8977d55d178305a5620e9616ac12f24364e0b3743df9161729b993fcf`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, invalid, scoped_verus_commands. Outputs/bindings: (none).
Calls/effect boundaries: scoped_verus_commands.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:44`; AST `eb181db117747a1221882e8de6d28227dcd99b7b08bb6858cee1e270070f0e3d`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, altered, checked_output, good, obligation, replace, result, run_process, self, sys, text. Outputs/bindings: altered, good, obligation, result, text.
Calls/effect boundaries: Path.cwd, checked_output, good.replace, obligation.update, replace, run_process, self.assertFalse, self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[0]::Assign

Source: `infra/tests/test_destiny_hardening.py:45`; AST `bf6c0fd9df89152bac82678b05c99a14d1f43a4c3cc81995e679f3a40bd5bd49`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, run_process, sys. Outputs/bindings: result.
Calls/effect boundaries: Path.cwd, run_process.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:45`; AST `94f2c12d5401cdcc216a77d7c81cb5e7c3ef1a17b166771ad776d34a50ae5582`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, run_process, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path.cwd, run_process.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[0].value.keywords[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:45`; AST `db9a457f54120339a519ab0c10b0203c3ebbee68c042f899e0c442fb37c6bc91`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path. Outputs/bindings: (none).
Calls/effect boundaries: Path.cwd.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:46`; AST `ab3275256123a7fc61821aa86bed75c4bfd9cbcab864aa7e3d58ad6d4e7421cd`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: obligation.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[2]::Assign

Source: `infra/tests/test_destiny_hardening.py:47`; AST `e7777635b549a6732d7585d7a50ecb3d90e6cf137bb54f4e931f899e62b5fefe`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: good.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[3]::Expr

Source: `infra/tests/test_destiny_hardening.py:48`; AST `bc7da8e9b8fab5f76ea0c8f335c9c19b7697c67d117f1714e3fcd0282916fa98`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked_output, good, obligation, replace, result, self. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[3].value::Call

Source: `infra/tests/test_destiny_hardening.py:48`; AST `368dd43a0927eee9d08c490ba45b468dcd48a6cfbd3971fdee8b25ede01c971a`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, good, obligation, replace, result, self. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[3].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:48`; AST `07728e1885f7c5a3d0a9872872a5380e115185e6c44808509bb474c2c309839c`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, good, obligation, replace, result. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[3].value.args[0].args[1]::Call

Source: `infra/tests/test_destiny_hardening.py:48`; AST `437016ba6e335d6040089b6cd8143d8f0c0de7eaac561e20a3847bb203fce512`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: good, replace, result. Outputs/bindings: (none).
Calls/effect boundaries: replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[3].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[4]::Expr

Source: `infra/tests/test_destiny_hardening.py:49`; AST `506289f1ed4a977736b79c7e16b61bded07883a9fe5ba89f417cb6279b305eb7`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked_output, good, obligation, replace, result, self. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[4].value::Call

Source: `infra/tests/test_destiny_hardening.py:49`; AST `208b8cc36cb7723aef9bd750a4e7a2f9a0630c8f33f88fe632491e0bb0724fa8`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, good, obligation, replace, result, self. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[4].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:49`; AST `ca27234ec8f763c1b4add86c0d9553fe4f191837af96759038443c17351e25c1`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, good, obligation, replace, result. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[4].value.args[0].args[1]::Call

Source: `infra/tests/test_destiny_hardening.py:49`; AST `63517ac3e30755dcd5d4afb1496a220445b219c1a5834022d0c2e267b004e03c`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: good, replace, result. Outputs/bindings: (none).
Calls/effect boundaries: replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[4].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[5]::For

Source: `infra/tests/test_destiny_hardening.py:50`; AST `bd7a9a1ef444cb49723e8b542bde2a6fc215bb259df52b72a2d68122b30bdb2a`.

Rust module: `infra::tests::test_destiny_hardening`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: checked_output, good, obligation, replace, result, self, text. Outputs/bindings: text.
Calls/effect boundaries: checked_output, good.replace, replace, self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered For evaluation at root.body[16].body[2].body[5]; no call, error or mutation may be omitted. Iteration: text in ('', good * 2, good.replace('proofs::formation', 'other'), good + ' - Status: UNREACHABLE\n', good + ' - Status: FAILURE\n')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[5].iter.elts[2]::Call

Source: `infra/tests/test_destiny_hardening.py:50`; AST `17a9918f743505bd3f631e6c0f4e986da1a61c0b841ae4b101f8425f06245846`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: good. Outputs/bindings: (none).
Calls/effect boundaries: good.replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[5].iter.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[5].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:51`; AST `e82d87dd85f11ebc836d75b35462f8d051dbd4198501ecd447960c4e2469a915`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked_output, obligation, replace, result, self, text. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[5].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:51`; AST `71d5c74d14ad0007b6f66430f99e7b0a7462c9be1627d62d4dfd7d8e5e98d0e7`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, obligation, replace, result, self, text. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[5].body[0].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:51`; AST `8ae31f938007a52bd247303066526d4b0a18f411be0b3e89ec00aec3d8ca8cb4`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, obligation, replace, result, text. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[5].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[5].body[0].value.args[0].args[1]::Call

Source: `infra/tests/test_destiny_hardening.py:51`; AST `c9101db621cdc91bed147d3c553b75550d3178c421a3e45ddfc3d7954ba3cbfa`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: replace, result, text. Outputs/bindings: (none).
Calls/effect boundaries: replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[5].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[6]::For

Source: `infra/tests/test_destiny_hardening.py:52`; AST `2575ecd2761e410f304271e44d8f197cae7b4408c899ba1b867061b3f5b67ca7`.

Rust module: `infra::tests::test_destiny_hardening`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: altered, checked_output, good, obligation, replace, result, self. Outputs/bindings: altered.
Calls/effect boundaries: checked_output, replace, self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered For evaluation at root.body[16].body[2].body[6]; no call, error or mutation may be omitted. Iteration: altered in ({'returncode': 1}, {'timed_out': True}, {'stdout_truncated': True}, {'stderr_truncated': True})
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[6].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:53`; AST `fc9432175a2e07b9616538b253d0c1fd39ee6bb45dd930700f3632f367467cf2`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: altered, checked_output, good, obligation, replace, result, self. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[6].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:53`; AST `13de5cd23c0944bc44a72f9df18c54d1fc5759a5e3adf668811dabb62eba5885`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: altered, checked_output, good, obligation, replace, result, self. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[6].body[0].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:53`; AST `22b2553c247e28d2c1f0ae7bd4843bc8cab61e2067e3445ccb88d7ab44bff513`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: altered, checked_output, good, obligation, replace, result. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[6].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[6].body[0].value.args[0].args[1]::Call

Source: `infra/tests/test_destiny_hardening.py:53`; AST `1824f8c022a391d94ace8fb4cd9e980d82e50595c1326a18c07b93deb71f6c22`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: altered, good, replace, result. Outputs/bindings: (none).
Calls/effect boundaries: replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[6].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[7]::Expr

Source: `infra/tests/test_destiny_hardening.py:54`; AST `fa9a851045b67c86281b7ad9abc7b3ebfbf110457f5e32bbe2afdc689f956a31`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.update.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[7].value::Call

Source: `infra/tests/test_destiny_hardening.py:54`; AST `2c7d765fea9dca16ea5454641d3573d80c790946c1d3c24891db756007fbd4f5`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.update.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[8]::Expr

Source: `infra/tests/test_destiny_hardening.py:55`; AST `b7755e4e3c60e2bb947085c21bdfce197814f24bf66de92d69028ef78a8d0282`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked_output, obligation, replace, result, self. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[8].value::Call

Source: `infra/tests/test_destiny_hardening.py:55`; AST `30c88a19eb9b8970905523148e6449430a7c5b9f22ffc9b6e54b913c036fd48c`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, obligation, replace, result, self. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[8].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:55`; AST `2a40fd8674a7a2d3b8fa70d32a873af41adf96572ab25bb31732c080bdbd1b0f`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, obligation, replace, result. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[8].value.args[0].args[1]::Call

Source: `infra/tests/test_destiny_hardening.py:55`; AST `5d983615c028a12846a453bf297aa4002b42bee625cf8ffc332762c2c7f54992`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: replace, result. Outputs/bindings: (none).
Calls/effect boundaries: replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[8].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[9]::For

Source: `infra/tests/test_destiny_hardening.py:56`; AST `cf31c1f3ec254a1624528ad85cde0ba068272ef00feded0d010e7ff40e485d6e`.

Rust module: `infra::tests::test_destiny_hardening`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: checked_output, obligation, replace, result, self, text. Outputs/bindings: text.
Calls/effect boundaries: checked_output, replace, self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered For evaluation at root.body[16].body[2].body[9]; no call, error or mutation may be omitted. Iteration: text in ('verification results:: 0 verified, 0 errors', 'verification results:: 2 verified, 1 errors', 'verification results:: 2 verified, 0 errors\n' * 2)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[9].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:57`; AST `e82d87dd85f11ebc836d75b35462f8d051dbd4198501ecd447960c4e2469a915`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked_output, obligation, replace, result, self, text. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[9].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:57`; AST `71d5c74d14ad0007b6f66430f99e7b0a7462c9be1627d62d4dfd7d8e5e98d0e7`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, obligation, replace, result, self, text. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace, self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[9].body[0].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:57`; AST `8ae31f938007a52bd247303066526d4b0a18f411be0b3e89ec00aec3d8ca8cb4`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, obligation, replace, result, text. Outputs/bindings: (none).
Calls/effect boundaries: checked_output, replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[9].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestBranchVerifierReuse::test_exact_nonvacuous_kani_and_verus_inventory::root.body[16].body[2].body[9].body[0].value.args[0].args[1]::Call

Source: `infra/tests/test_destiny_hardening.py:57`; AST `c9101db621cdc91bed147d3c553b75550d3178c421a3e45ddfc3d7954ba3cbfa`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: replace, result, text. Outputs/bindings: (none).
Calls/effect boundaries: replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[9].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::root.body[17]::ClassDef

Source: `infra/tests/test_destiny_hardening.py:60`; AST `d5d19761fab7b3e22b0c23bd1e72983754acfb87c4fef80d76a2e55f6ed6b824`.

Rust module: `infra::tests::test_destiny_hardening`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: DestinyFixture, ValueError, archive, before, checksum, data, directory, edited, env, files, hashlib, home, ids, implementation, io, json, len, list, member, name, path, receipt, registry_source_files, release, reservations, response, result, row, self, set, source, source_snapshot, str, subprocess, tarfile, text, third, tree. Outputs/bindings: archive, before, checksum, data, directory, edited, env, files, home, ids, implementation, member, name, path, receipt, release, reservations, response, result, row, source, text, third, tree.
Calls/effect boundaries: (directory / '.aegis').mkdir, (directory / '.aegis/receipt.json').write_text, (directory / '.cargo').mkdir, (directory / '.cargo/config.toml').write_text, (directory / '.gitignore').write_text, (directory / 'source.rs').write_text, (directory / 'untracked.rs').write_text, (self.root / '.aegis/destiny/attempts').glob, (self.root / 'ordinary').mkdir, (tree / 'build.rs').write_text, archive.parent.mkdir, archive.read_bytes, archive.write_bytes, directory.mkdir, hashlib.sha256, hashlib.sha256(archive.read_bytes()).hexdigest, implementation.write_text, io.BytesIO, json.loads, len, list, path.write_text, receipt.read_text, receipt.write_text, registry_source_files, release.addfile, reservations[0].read_text, response['text'].encode, self.assertEqual, self.assertIn, self.assertLessEqual, self.assertNotEqual, self.assertRaisesRegex, self.assertTrue, self.call, self.write, set, source.read_bytes, source_snapshot, str, subprocess.run, tarfile.TarInfo, tarfile.open, text.replace, tree.mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:61`; AST `17973d165b98835a37bd76a3e56f786171239097ecfb9685faaa53d5d2587968`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, archive, checksum, data, env, files, hashlib, home, implementation, io, len, member, registry_source_files, release, self, source, str, tarfile, tree. Outputs/bindings: archive, checksum, data, env, files, home, implementation, member, release, source, tree.
Calls/effect boundaries: (tree / 'build.rs').write_text, archive.parent.mkdir, archive.read_bytes, archive.write_bytes, hashlib.sha256, hashlib.sha256(archive.read_bytes()).hexdigest, implementation.write_text, io.BytesIO, len, registry_source_files, release.addfile, self.assertIn, self.assertRaisesRegex, self.write, source.read_bytes, str, tarfile.TarInfo, tarfile.open, tree.mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:62`; AST `388a2b17c38513b98d99be3269610b3513052829ea1b99e6c6081fd48486bfcf`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:62`; AST `b43e1e6993e8d1846e73bdf2e381e874126d51c21126d74c5750b2dd67587cbf`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:63`; AST `4f117e5b99ec1fbf833822f5aceff2227ecb677555ee08c5288f202147dc53b1`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: home.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[2]::Assign

Source: `infra/tests/test_destiny_hardening.py:64`; AST `3438c953066140fe1651a48e28acf9f8dcaf8ab549a411a3fcaff0914017e2da`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: home. Outputs/bindings: tree.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[3]::Expr

Source: `infra/tests/test_destiny_hardening.py:65`; AST `e33e20d9aed03199e02ee2c2007971ae953d15b30b763001a01b6e318e27e8b2`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tree. Outputs/bindings: (none).
Calls/effect boundaries: tree.mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[3].value::Call

Source: `infra/tests/test_destiny_hardening.py:65`; AST `e60eea1b7000d50fa3a69621bfa6d13cfa728870ca5367dc2f4e5dfe39592694`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tree. Outputs/bindings: (none).
Calls/effect boundaries: tree.mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[4]::Assign

Source: `infra/tests/test_destiny_hardening.py:66`; AST `73acf669299d3b0f0e9c8e6b4f6901e12a96da1e13e8aa34b2d47ab781be4156`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tree. Outputs/bindings: implementation.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[5]::Expr

Source: `infra/tests/test_destiny_hardening.py:67`; AST `f272bace4b1c020d150254623fa9d677dc6b5abbdd9eaab91faa76d8074b31cd`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: implementation. Outputs/bindings: (none).
Calls/effect boundaries: implementation.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[5].value::Call

Source: `infra/tests/test_destiny_hardening.py:67`; AST `f14634c7aaeb535a4b917263ff5f8d5756a965fa02818573afcebef572236697`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: implementation. Outputs/bindings: (none).
Calls/effect boundaries: implementation.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[6]::Expr

Source: `infra/tests/test_destiny_hardening.py:68`; AST `a0520edf93ad4ba974c87f0bbc1d73df58ff0859c28769bbd6e1a4e6bb777633`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tree. Outputs/bindings: (none).
Calls/effect boundaries: (tree / 'build.rs').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[6].value::Call

Source: `infra/tests/test_destiny_hardening.py:68`; AST `9910b3bdc461632313ce89fc822697c3306d49034a5c315086e927dd1672a6bf`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tree. Outputs/bindings: (none).
Calls/effect boundaries: (tree / 'build.rs').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[7]::Assign

Source: `infra/tests/test_destiny_hardening.py:69`; AST `51ca7f2b6bf7d3551cf697558ff3a16417abcf816a5a032315f19781c6302c3c`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: home. Outputs/bindings: archive.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[8]::Expr

Source: `infra/tests/test_destiny_hardening.py:70`; AST `88e1ebf097c517485b24a4af7c907092623ac13dd711999bc78e53c80919f85c`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive. Outputs/bindings: (none).
Calls/effect boundaries: archive.parent.mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[8].value::Call

Source: `infra/tests/test_destiny_hardening.py:70`; AST `2c1805c85aa99831f9392ae4e2f4aee1d4541d2bf8d9aa08199589d91d786a34`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive. Outputs/bindings: (none).
Calls/effect boundaries: archive.parent.mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9]::With

Source: `infra/tests/test_destiny_hardening.py:71`; AST `c704dd65271d144b6eca444bb49c8399eedab62b0539809961fb05d70d5dce64`.

Rust module: `infra::tests::test_destiny_hardening`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: archive, data, implementation, io, len, member, release, source, tarfile, tree. Outputs/bindings: data, member, release, source.
Calls/effect boundaries: io.BytesIO, len, release.addfile, source.read_bytes, tarfile.TarInfo, tarfile.open.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered With evaluation at root.body[17].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].items[0].context_expr::Call

Source: `infra/tests/test_destiny_hardening.py:71`; AST `6b7d17777cf2932465a3f0784fdcd687c56020bb9244ec927e5eac71245d2052`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, tarfile. Outputs/bindings: (none).
Calls/effect boundaries: tarfile.open.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[9].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0]::For

Source: `infra/tests/test_destiny_hardening.py:72`; AST `c3cd70e939491b906151ca42b7c63c03c2114850b349121324c34855ec93754f`.

Rust module: `infra::tests::test_destiny_hardening`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: data, implementation, io, len, member, release, source, tarfile, tree. Outputs/bindings: data, member, source.
Calls/effect boundaries: io.BytesIO, len, release.addfile, source.read_bytes, tarfile.TarInfo.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered For evaluation at root.body[17].body[0].body[9].body[0]; no call, error or mutation may be omitted. Iteration: source in (implementation, tree / 'build.rs')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0].body[0]::Assign

Source: `infra/tests/test_destiny_hardening.py:73`; AST `aa53135bf92ebaa6d027765b2ec67def044fc0258c6e009d08a6fb7c2efc6f62`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: source. Outputs/bindings: data.
Calls/effect boundaries: source.read_bytes.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[9].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:73`; AST `7025313203be3177e434d687d8ce72e4a616e87168ebdf1b6a6752464d4dd93c`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.read_bytes.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[9].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:74`; AST `fadfe9965973c6d7275f182310fcdbadd4cbab9b89df59062f634857770d1169`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: source, tarfile. Outputs/bindings: member.
Calls/effect boundaries: tarfile.TarInfo.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[9].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0].body[1].value::Call

Source: `infra/tests/test_destiny_hardening.py:74`; AST `81b1eaeb8a3bb673ff775f1cbb66753f7332c18579c219f2d435d1f58b945303`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source, tarfile. Outputs/bindings: (none).
Calls/effect boundaries: tarfile.TarInfo.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[9].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0].body[2]::Assign

Source: `infra/tests/test_destiny_hardening.py:75`; AST `abe2a03899398afa16634aa36190d329bf29db910ea8cd4cda75b06a5b731d44`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, len, member. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[9].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:75`; AST `fc74103c13bf8d377d661458ea3a35fc1992328898312d6f40eb90c2671f2ed8`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[9].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0].body[3]::Expr

Source: `infra/tests/test_destiny_hardening.py:76`; AST `f987e1abf9698546e1d3cf07390826dc555a7fbf0a91df9edd3f7fd484abd109`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, io, member, release. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO, release.addfile.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[9].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0].body[3].value::Call

Source: `infra/tests/test_destiny_hardening.py:76`; AST `7176ecf00bd4b0ac7d4b5cc6386e418208bfd78ad65cdd109a724ace2214cb0c`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, io, member, release. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO, release.addfile.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[9].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[9].body[0].body[3].value.args[1]::Call

Source: `infra/tests/test_destiny_hardening.py:76`; AST `7843035dee48266733d1fdb30282e4616f3239a2533ffb35684f5be9cf30b83f`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, io. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[9].body[0].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[10]::Assign

Source: `infra/tests/test_destiny_hardening.py:77`; AST `2df56a272154fb9460ddd37edb6887147b0a657cab5accf33b005e726d66cd79`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive, hashlib. Outputs/bindings: checksum.
Calls/effect boundaries: archive.read_bytes, hashlib.sha256, hashlib.sha256(archive.read_bytes()).hexdigest.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[10].value::Call

Source: `infra/tests/test_destiny_hardening.py:77`; AST `4999c853e46d41065e5697e2f8665bc10343bb5d344e0ad17275c9fdc1f3f9eb`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: archive.read_bytes, hashlib.sha256, hashlib.sha256(archive.read_bytes()).hexdigest.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[10].value.func.value::Call

Source: `infra/tests/test_destiny_hardening.py:77`; AST `cb8a7a73f228604e368827abaed8b82a004d134d513ce17ba21f14efa418d52f`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: archive.read_bytes, hashlib.sha256.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[10].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[10].value.func.value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:77`; AST `f8d150bc0b5cca804f280b3270f894daab1f2f2db7385b8cd4f21c87f4d02832`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive. Outputs/bindings: (none).
Calls/effect boundaries: archive.read_bytes.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[10].value.func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[11]::Expr

Source: `infra/tests/test_destiny_hardening.py:78`; AST `64c37311855bb82b09a5daff1a55cef1b1b26e8e3f6e29291ec533d2259fc8e5`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checksum, self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[11].value::Call

Source: `infra/tests/test_destiny_hardening.py:78`; AST `b0756b8e1022de7bb619c89dca223fb3967df1db36ba6da23ed80d2351349cd1`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checksum, self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[12]::Assign

Source: `infra/tests/test_destiny_hardening.py:79`; AST `851922e2d362f78e251a3b3549a0bf751a284402e1e4fcba3cea548d5bab18ad`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: home, str. Outputs/bindings: env.
Calls/effect boundaries: str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[12].value.values[0]::Call

Source: `infra/tests/test_destiny_hardening.py:79`; AST `1f47b3a7f6e4d874983adb7c5e4b90a6a46b378fcf9dc9c4c8c0fceeab471d62`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[12].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[13]::Assign

Source: `infra/tests/test_destiny_hardening.py:80`; AST `c2012b2509a50f4fef420685c4680b239e5c57af1a35b70fbcdc40e40f8ac210`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, registry_source_files, self. Outputs/bindings: files.
Calls/effect boundaries: registry_source_files.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[13].value::Call

Source: `infra/tests/test_destiny_hardening.py:80`; AST `f8c77d72852198343ebfc25642c687d81f959395df002a148e3db46e632de727`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env, registry_source_files, self. Outputs/bindings: (none).
Calls/effect boundaries: registry_source_files.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[14]::Expr

Source: `infra/tests/test_destiny_hardening.py:81`; AST `f783e369f7996836a8f693a7cfa49a334ad24af28e71b4720f0e8f26168ebf7e`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: files, implementation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[14].value::Call

Source: `infra/tests/test_destiny_hardening.py:81`; AST `78b9fb91b2a941cc0014bdf110dd18fafcce4bf0a20ee6c2fa22761e3573b506`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: files, implementation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[15]::Expr

Source: `infra/tests/test_destiny_hardening.py:82`; AST `db97efa4c7840edce4c27ebd556269cd5e79bd872ce368efd0cf5ad23c53ab1f`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: files, self, tree. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[15].value::Call

Source: `infra/tests/test_destiny_hardening.py:82`; AST `480ec16314c14bfbeaae58f73a1451fd979d50490e089c79888d8589cfd74286`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: files, self, tree. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[16]::Expr

Source: `infra/tests/test_destiny_hardening.py:83`; AST `7e589027bb9d7aa329fb94a4564a891156e4cb2175b0b6624e8ac899e823e295`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: implementation. Outputs/bindings: (none).
Calls/effect boundaries: implementation.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[16].value::Call

Source: `infra/tests/test_destiny_hardening.py:83`; AST `7ab7e62c48108db54de6f9a878c294c41f77beddaac30409fb40b5df15ef393a`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: implementation. Outputs/bindings: (none).
Calls/effect boundaries: implementation.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[17]::With

Source: `infra/tests/test_destiny_hardening.py:84`; AST `ea831548779c8577e53d160d5ed60b7562c9075d9c95564c9ff9d780f7f1cb7f`.

Rust module: `infra::tests::test_destiny_hardening`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, env, registry_source_files, self. Outputs/bindings: (none).
Calls/effect boundaries: registry_source_files, self.assertRaisesRegex.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered With evaluation at root.body[17].body[0].body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[17].items[0].context_expr::Call

Source: `infra/tests/test_destiny_hardening.py:84`; AST `6232a65b6cdc237a668b5c9a001df4d3fbe281ec89ac15348ce766e47c084283`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[17].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[17].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:85`; AST `a49b880538223bdba598a843e465d424317f5ed74872faed7cf11df6eceb25e9`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, registry_source_files, self. Outputs/bindings: (none).
Calls/effect boundaries: registry_source_files.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[17].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:85`; AST `f8c77d72852198343ebfc25642c687d81f959395df002a148e3db46e632de727`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env, registry_source_files, self. Outputs/bindings: (none).
Calls/effect boundaries: registry_source_files.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[18]::Expr

Source: `infra/tests/test_destiny_hardening.py:86`; AST `a4b6d36828a39dd27746fed8eb57bafd7d0040f99e50349f7118a21edf2125af`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive. Outputs/bindings: (none).
Calls/effect boundaries: archive.write_bytes.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[18].value::Call

Source: `infra/tests/test_destiny_hardening.py:86`; AST `65cc638e33a858fdd6c360bf3ff134120c24d8258b2ee5e83f4cd72632ba01ed`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive. Outputs/bindings: (none).
Calls/effect boundaries: archive.write_bytes.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[19]::With

Source: `infra/tests/test_destiny_hardening.py:87`; AST `4a81796c98e714b66464aff77443fd429cc3c4c3a7928efd1a117303046483da`.

Rust module: `infra::tests::test_destiny_hardening`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, env, registry_source_files, self. Outputs/bindings: (none).
Calls/effect boundaries: registry_source_files, self.assertRaisesRegex.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered With evaluation at root.body[17].body[0].body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[19].items[0].context_expr::Call

Source: `infra/tests/test_destiny_hardening.py:87`; AST `15cdd940e9514ab968a3664eb9075bf1d32f43321748e60de3f690dc23506a59`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[19].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[19].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:88`; AST `a49b880538223bdba598a843e465d424317f5ed74872faed7cf11df6eceb25e9`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, registry_source_files, self. Outputs/bindings: (none).
Calls/effect boundaries: registry_source_files.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_proof_registry_payload_binds_actual_math_source_and_build_script::root.body[17].body[0].body[19].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:88`; AST `f8c77d72852198343ebfc25642c687d81f959395df002a148e3db46e632de727`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env, registry_source_files, self. Outputs/bindings: (none).
Calls/effect boundaries: registry_source_files.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:90`; AST `4084792db4967d067717d7cc870258140b7ea56e3d4dfd9d87a13aa35e7c3dd5`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: before, directory, edited, name, self, set, source_snapshot, str, subprocess. Outputs/bindings: before, directory, edited, name.
Calls/effect boundaries: (directory / '.aegis').mkdir, (directory / '.aegis/receipt.json').write_text, (directory / '.cargo').mkdir, (directory / '.cargo/config.toml').write_text, (directory / '.gitignore').write_text, (directory / 'source.rs').write_text, (directory / 'untracked.rs').write_text, directory.mkdir, self.assertEqual, self.assertNotEqual, set, source_snapshot, str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0]::For

Source: `infra/tests/test_destiny_hardening.py:91`; AST `a0717f99bfa5500e42bd76cadafc680a9af5f7c7c4a0cf1cbec00d757ba0e666`.

Rust module: `infra::tests::test_destiny_hardening`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: directory, name, self, str, subprocess. Outputs/bindings: directory, name.
Calls/effect boundaries: (directory / '.gitignore').write_text, (directory / 'source.rs').write_text, directory.mkdir, str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered For evaluation at root.body[17].body[1].body[0]; no call, error or mutation may be omitted. Iteration: name in ('.agents', 'vendor/dependency')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[0]::Assign

Source: `infra/tests/test_destiny_hardening.py:92`; AST `12572ddd0391ba1824f11e0f210c9b30786485f72f8d33fe7a8a919a8162e80a`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, self. Outputs/bindings: directory.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[1]::Expr

Source: `infra/tests/test_destiny_hardening.py:93`; AST `6152b54f8dbe4d2662a3c1356e52c7b0379dd225ff153f38132fb97aeca463b6`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[1].value::Call

Source: `infra/tests/test_destiny_hardening.py:93`; AST `03a941e0af455b4c068c9733df37595ef6d172f8a7249df82fa84e6fa4ca7940`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[2]::Expr

Source: `infra/tests/test_destiny_hardening.py:94`; AST `7440e92d0fc0c42ebcc5f1d96506c130a0530ac88ff312732d44384bdb2a70d3`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:94`; AST `d10e55829cb5c719119658f0f4f6e4358b0c5b3fadc59eb1c823b305f588e81d`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[2].value.args[0].elts[3]::Call

Source: `infra/tests/test_destiny_hardening.py:94`; AST `2d603a2f746adfd4eba56d01dddbc285ad7a323b7cb917b749ad7612e6c17941`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].body[2].value.args[0].elts[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[3]::Expr

Source: `infra/tests/test_destiny_hardening.py:95`; AST `97b81fd78df20ec6f9e317884e789b0af6b1ad07e42917ed2146fff92a268d00`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / 'source.rs').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[3].value::Call

Source: `infra/tests/test_destiny_hardening.py:95`; AST `de4dce019bec700fcebba8674baba0f6893dc8b97316dcd08deed5799c8f7c8c`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / 'source.rs').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[4]::Expr

Source: `infra/tests/test_destiny_hardening.py:96`; AST `66b1aaef6dc6745e144d1ec41e11f274e5c692148be0f7975e11723c507b49da`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.gitignore').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[4].value::Call

Source: `infra/tests/test_destiny_hardening.py:96`; AST `02ce36e654d98b40432c25ef3025120e32afee6ac437abccbce9c30aed1716cc`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.gitignore').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[5]::Expr

Source: `infra/tests/test_destiny_hardening.py:97`; AST `00671b3646ec2ffc456074cf0acaaa96d7fd9adf78c4ccbf7246e71265042621`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[5].value::Call

Source: `infra/tests/test_destiny_hardening.py:97`; AST `480a60d2ab75bd05e450e0c9a8d669b6269a7c426ee5939a8185496c935a9333`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[5].value.args[0].elts[2]::Call

Source: `infra/tests/test_destiny_hardening.py:97`; AST `2d603a2f746adfd4eba56d01dddbc285ad7a323b7cb917b749ad7612e6c17941`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].body[5].value.args[0].elts[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[6]::Expr

Source: `infra/tests/test_destiny_hardening.py:98`; AST `3069c655b84a357d9eb75193c09cba22f26229dc15ce6e10d2b5dfb0c869ca81`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[6].value::Call

Source: `infra/tests/test_destiny_hardening.py:98`; AST `c16db8a94236c8999735e4e611c31c2832f9b79bd99f98586bca3696340450ce`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[0].body[6].value.args[0].elts[2]::Call

Source: `infra/tests/test_destiny_hardening.py:98`; AST `2d603a2f746adfd4eba56d01dddbc285ad7a323b7cb917b749ad7612e6c17941`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].body[6].value.args[0].elts[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:100`; AST `4aea4020d3c13ff76fb133f0612cf8afffa2f7dc0839adec51b19771032fed0d`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_snapshot. Outputs/bindings: before.
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[1].value::Call

Source: `infra/tests/test_destiny_hardening.py:100`; AST `dd829a19f4f396ff4d905b23786313de3d2503c2950ad4851be701a567b35876`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[2]::Expr

Source: `infra/tests/test_destiny_hardening.py:101`; AST `ead3391c99ee1b638d96c2688e15ffdf74a3dfe7683ee5c4f301c492ef6c0100`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self, set. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, set.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:101`; AST `65faf284e926ba1c21db7f61e80bf691b06f073026d824fea6c0c67e20185bb4`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self, set. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, set.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[2].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:101`; AST `992ac72e678bacdd41b5f3658a0ba81a1b80b6697fb4dc1d4d4c06cd5494d6c1`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3]::For

Source: `infra/tests/test_destiny_hardening.py:102`; AST `1173510f811d9be16a616da3a097afe3b01f305439f521f3180fd8252f1302bc`.

Rust module: `infra::tests::test_destiny_hardening`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: before, directory, edited, name, self, source_snapshot. Outputs/bindings: before, directory, edited, name.
Calls/effect boundaries: (directory / '.aegis').mkdir, (directory / '.aegis/receipt.json').write_text, (directory / '.cargo').mkdir, (directory / '.cargo/config.toml').write_text, (directory / 'source.rs').write_text, (directory / 'untracked.rs').write_text, self.assertEqual, self.assertNotEqual, source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered For evaluation at root.body[17].body[1].body[3]; no call, error or mutation may be omitted. Iteration: name in ('.agents', 'vendor/dependency')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[0]::Assign

Source: `infra/tests/test_destiny_hardening.py:103`; AST `12572ddd0391ba1824f11e0f210c9b30786485f72f8d33fe7a8a919a8162e80a`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, self. Outputs/bindings: directory.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[1]::Expr

Source: `infra/tests/test_destiny_hardening.py:104`; AST `7d5bef515c0fa8b4aad0cbbac78328bbbacc7be581d45fd308c5d01095f38b07`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / 'source.rs').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[1].value::Call

Source: `infra/tests/test_destiny_hardening.py:104`; AST `ad69d3887f0c1242b7507b00a9d0a05bd767ccc55200e579e7224ac2f32111ad`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / 'source.rs').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[2]::Assign

Source: `infra/tests/test_destiny_hardening.py:105`; AST `5f84a66e1e2131263c9c81984a83c0368a466bba7107b98b973920144618e75c`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_snapshot. Outputs/bindings: edited.
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:105`; AST `dd829a19f4f396ff4d905b23786313de3d2503c2950ad4851be701a567b35876`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[3]::Expr

Source: `infra/tests/test_destiny_hardening.py:106`; AST `13d01b5123e2168fa9f1d4681df38a591d0614695532816eeef30b29c410c6de`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, edited, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[3].value::Call

Source: `infra/tests/test_destiny_hardening.py:106`; AST `4e6cc5fcd413f6b2d755a7103666905da59cc5cca2b1d34768ac70cfa1b9368b`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, edited, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[4]::Expr

Source: `infra/tests/test_destiny_hardening.py:107`; AST `5a0447a810960bd38da69eddba44e39fbade24876f2cd4adb048653504ca5fdd`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, edited, name, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[4].value::Call

Source: `infra/tests/test_destiny_hardening.py:107`; AST `c76fb019ae161d046422310f45575eb051ef92412458ffa052c079481f558639`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, edited, name, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[5]::Assign

Source: `infra/tests/test_destiny_hardening.py:108`; AST `3fe3dda2463e256c735a42574d89c8102f22a15125f086c0c40f012bb8965000`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: edited. Outputs/bindings: before.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[6]::Expr

Source: `infra/tests/test_destiny_hardening.py:109`; AST `71edbf5c5174e8c13f683a1ef77a17c942c556b6131c2f2ea60f47e1401b74cd`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / 'untracked.rs').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[6].value::Call

Source: `infra/tests/test_destiny_hardening.py:109`; AST `86d367be971747e3691727561853867c1a8806d442b6fbe271c0a675de0110d1`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / 'untracked.rs').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[7]::Expr

Source: `infra/tests/test_destiny_hardening.py:110`; AST `20e9fc6356df29099e2ae16a89c200a86b1db5781714cd15cc74e4f52c155e31`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[7].value::Call

Source: `infra/tests/test_destiny_hardening.py:110`; AST `6803d69d7dd18fa0e960fad3e14442534d8265ff95b5e42bfb84208c5fd8ab22`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[7].value.args[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:110`; AST `dd829a19f4f396ff4d905b23786313de3d2503c2950ad4851be701a567b35876`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[7].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[8]::Assign

Source: `infra/tests/test_destiny_hardening.py:111`; AST `4aea4020d3c13ff76fb133f0612cf8afffa2f7dc0839adec51b19771032fed0d`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_snapshot. Outputs/bindings: before.
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[8].value::Call

Source: `infra/tests/test_destiny_hardening.py:111`; AST `dd829a19f4f396ff4d905b23786313de3d2503c2950ad4851be701a567b35876`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[9]::Expr

Source: `infra/tests/test_destiny_hardening.py:112`; AST `bc1d0044ce5e647f43be6fa75f4342957eb6ae7b07f38801fb00bb81a68ef276`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.cargo').mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[9].value::Call

Source: `infra/tests/test_destiny_hardening.py:112`; AST `a8bcccbff6c287cfcc4eb9dd4d2d44bcf6a10abb4019fc0a44345261261b84ab`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.cargo').mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[10]::Expr

Source: `infra/tests/test_destiny_hardening.py:113`; AST `77b21f0872f70374309347502a6ad7fd822b2feaf8612ed16bcd8bc8ac649e50`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.cargo/config.toml').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[10].value::Call

Source: `infra/tests/test_destiny_hardening.py:113`; AST `2b7bd3bf42f5db06f19a01094eccd5ac5617219ffcc5d545024a84ef62472f04`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.cargo/config.toml').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[11]::Expr

Source: `infra/tests/test_destiny_hardening.py:114`; AST `20e9fc6356df29099e2ae16a89c200a86b1db5781714cd15cc74e4f52c155e31`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[11].value::Call

Source: `infra/tests/test_destiny_hardening.py:114`; AST `6803d69d7dd18fa0e960fad3e14442534d8265ff95b5e42bfb84208c5fd8ab22`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[11].value.args[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:114`; AST `dd829a19f4f396ff4d905b23786313de3d2503c2950ad4851be701a567b35876`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[11].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[12]::Assign

Source: `infra/tests/test_destiny_hardening.py:115`; AST `4aea4020d3c13ff76fb133f0612cf8afffa2f7dc0839adec51b19771032fed0d`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_snapshot. Outputs/bindings: before.
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[3].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[12].value::Call

Source: `infra/tests/test_destiny_hardening.py:115`; AST `dd829a19f4f396ff4d905b23786313de3d2503c2950ad4851be701a567b35876`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[13]::Expr

Source: `infra/tests/test_destiny_hardening.py:116`; AST `f4f770bf0c8f5ec6baad397aab9fdaac3ad55d9e470cd981b379ddd99843c649`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.aegis').mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[13].value::Call

Source: `infra/tests/test_destiny_hardening.py:116`; AST `f6e48fc070fa8d2a887c8e50115c214dfa55fb1aa0ac0d2af2981a4a74bcca4f`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.aegis').mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[14]::Expr

Source: `infra/tests/test_destiny_hardening.py:117`; AST `9300d301793e40a2882e48c2b28fb306b719faed7d93768afa77bcdf32db8bfc`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.aegis/receipt.json').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[14].value::Call

Source: `infra/tests/test_destiny_hardening.py:117`; AST `2203fc9e27bef12a2a4fedb575b4ea1f268924bb3917c3667011bc83abb00011`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: (directory / '.aegis/receipt.json').write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[15]::Expr

Source: `infra/tests/test_destiny_hardening.py:118`; AST `b9974bb1fd256925b0830128ea1f042d639278239b065f51e31e1270bf107a1f`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[15].value::Call

Source: `infra/tests/test_destiny_hardening.py:118`; AST `01c98d32b8b3a24cb7247741913c71c2cd976864b78071484ebb830a6680ea4d`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_embedded_repositories_bind_controller_and_vendor_source_separately::root.body[17].body[1].body[3].body[15].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:118`; AST `dd829a19f4f396ff4d905b23786313de3d2503c2950ad4851be701a567b35876`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].body[15].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_directory_glob_is_not_silently_ignored::root.body[17].body[2]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:120`; AST `bf7bb2ba285fdbdb601a02053d904eea5e121c0d38dca2f3433b0afc4c9d34f2`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'ordinary').mkdir, self.assertRaisesRegex, source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_directory_glob_is_not_silently_ignored::root.body[17].body[2].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:121`; AST `0e77c1d71fc44758328bb3525358ce09d32949d01371ccd62e205e5e40fe8da7`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'ordinary').mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_directory_glob_is_not_silently_ignored::root.body[17].body[2].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:121`; AST `202cf98f68fba2ea4ffc0d4b3a639318f215a1df1898f3272cc00677b6da3c3b`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'ordinary').mkdir.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_directory_glob_is_not_silently_ignored::root.body[17].body[2].body[1]::With

Source: `infra/tests/test_destiny_hardening.py:122`; AST `23b508431e4106b5c1833186f3bf42b7196a86fa2fa596ec25b1ab309b3df8f1`.

Rust module: `infra::tests::test_destiny_hardening`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ValueError, self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered With evaluation at root.body[17].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_directory_glob_is_not_silently_ignored::root.body[17].body[2].body[1].items[0].context_expr::Call

Source: `infra/tests/test_destiny_hardening.py:122`; AST `e428f60e0f9a58c504d3f4a0b4bfe4ab2f81c07fa35335c83811baf37c458692`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_directory_glob_is_not_silently_ignored::root.body[17].body[2].body[1].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:123`; AST `f5cf46028c31a76ad950f16a3be53e160affc9d3b32e363db6ea3f709806893d`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_directory_glob_is_not_silently_ignored::root.body[17].body[2].body[1].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:123`; AST `f076f2cc4718de86e08a17fe6ddf346049dce9f2bc0e1d5b7a94422604f7e9c4`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:125`; AST `a8dd6546e134dda0f865bfc11e0e66fe2fa731cc1577bd790ee1a09562b29b5e`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: before, path, self. Outputs/bindings: before, path.
Calls/effect boundaries: path.write_text, self.assertNotEqual, self.call, self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:126`; AST `a159d244cee66f629609cd4a015d892597576b2b9f8ffd18c5c46029c6f19376`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:126`; AST `120c2d60041d12851b0bfe346231687691b39fc5c97669aa22cda043af1f9357`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:127`; AST `98ee4a11e95ed729c9aa002996a8be8ca6b0cda419faed4fe4e6919c36ce73ea`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[1].value::Call

Source: `infra/tests/test_destiny_hardening.py:127`; AST `e5d0f636902003dd2d1cba2106a07347f0ec779c8cb00b78f50e435d013d2683`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[2]::Assign

Source: `infra/tests/test_destiny_hardening.py:128`; AST `20299100e957df8d4169fcdf1cd85fe8b33d2aaf88aef74e0d5f04772a9d3015`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: before.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:128`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[3]::Expr

Source: `infra/tests/test_destiny_hardening.py:129`; AST `637e96f6ef2789bed2d3c0195187552263c4c74db39100a34cfeceb53a5a82de`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[3].value::Call

Source: `infra/tests/test_destiny_hardening.py:129`; AST `113b884594902d704c90ba76bdb14067ab716f48b8e3fd2d9c9c893afc9acd0e`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[4]::Expr

Source: `infra/tests/test_destiny_hardening.py:130`; AST `89d05664c1550e225ee03ce0d6fa27e46796c0ba38ba64608dc3603cc66a1cf8`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[4].value::Call

Source: `infra/tests/test_destiny_hardening.py:130`; AST `b49b9148244037e1b9663a5a4ca39e212c31e63620a83a131e9b6c9f107c3372`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[4].value.args[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:130`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[4].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[5]::Assign

Source: `infra/tests/test_destiny_hardening.py:131`; AST `20299100e957df8d4169fcdf1cd85fe8b33d2aaf88aef74e0d5f04772a9d3015`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: before.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[5].value::Call

Source: `infra/tests/test_destiny_hardening.py:131`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[6]::Expr

Source: `infra/tests/test_destiny_hardening.py:132`; AST `2c7b067c23659d5557f90fb63abc2fa3c8d307b7225a1f4e79ac8df2d7ed47b5`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[6].value::Call

Source: `infra/tests/test_destiny_hardening.py:132`; AST `d795e40aa448ee562b2935c137b954a02331e284181ede879be0f21092da3040`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[7]::Expr

Source: `infra/tests/test_destiny_hardening.py:133`; AST `89d05664c1550e225ee03ce0d6fa27e46796c0ba38ba64608dc3603cc66a1cf8`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[7].value::Call

Source: `infra/tests/test_destiny_hardening.py:133`; AST `b49b9148244037e1b9663a5a4ca39e212c31e63620a83a131e9b6c9f107c3372`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignored_marker_inputs_are_fingerprinted::root.body[17].body[3].body[7].value.args[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:133`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[7].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:135`; AST `17e72808d9f748c6abe0a560835588463faa58e68659fffbd6e61b25f1118ba5`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: json, len, list, reservations, self, third. Outputs/bindings: reservations, third.
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, json.loads, len, list, reservations[0].read_text, self.assertEqual, self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:136`; AST `ba6d3413a91575634e7b78f0f8ab2b8e3cf25da2fd23934a34eec5c2667a2df9`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:136`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[1]::Expr

Source: `infra/tests/test_destiny_hardening.py:137`; AST `8497414276b02bc75fc408b9515af1330108fcfd31de53d57f06747a55c01a5d`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[1].value::Call

Source: `infra/tests/test_destiny_hardening.py:137`; AST `45dc63ac2eacf9477c070cf530596067a293b84c4d61578a31e7bc1f12f062a2`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[2]::Assign

Source: `infra/tests/test_destiny_hardening.py:138`; AST `1838b219993d5bd5fb5e304fd2ec34d84b3650adaa693131e6e96803c5a11a6c`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: third.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:138`; AST `97a255beecd375f74f02817f5fad16237080a123326f5b09569c58268b2a1dc2`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[3]::Expr

Source: `infra/tests/test_destiny_hardening.py:139`; AST `1545232ee453f9a780626cc21265d051ca05a0fd1fd8a7331b89789073a5a1ed`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, third. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[3].value::Call

Source: `infra/tests/test_destiny_hardening.py:139`; AST `574a108c53c09d51313de67756348a19e7a667ea13dcd5bfb81afb34fdfe6bf8`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, third. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[4]::Assign

Source: `infra/tests/test_destiny_hardening.py:140`; AST `32a019b2f2915f6c1d48b404530e5386c9b1eeec942a561c170fd9f80b9f1eab`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, self. Outputs/bindings: reservations.
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, list.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[4].value::Call

Source: `infra/tests/test_destiny_hardening.py:140`; AST `c12bd87eba5f1e4968be58f62acec133fc1f869672bd9196c1da8cab96af0275`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, list.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[4].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:140`; AST `3fcd698eb5974a0c93b8a0aba35f49a1fe7c3572364ca96f7ba5239d73ac8a6d`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[5]::Expr

Source: `infra/tests/test_destiny_hardening.py:141`; AST `38873c20954ef04b7ebecda7955cb576b8422401ffaf57014c949df440dbad61`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, reservations, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[5].value::Call

Source: `infra/tests/test_destiny_hardening.py:141`; AST `b388680ca168e1b3eaf9e8d3e3ae19388ffc3f4416f445f3150c1c3128899a87`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, reservations, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[5].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:141`; AST `997f7c8527e15b9f4ce9cbeec09329b00049684acc374c06c4ec33a419f60afe`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, reservations. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[6]::Expr

Source: `infra/tests/test_destiny_hardening.py:142`; AST `f8628ab9e7499fcaa53fb4134f65e3ac7f34c5c1bacb7fcf26e246f9bc741659`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, len, reservations, self. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, len, reservations[0].read_text, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[6].value::Call

Source: `infra/tests/test_destiny_hardening.py:142`; AST `1068ac1cab0bb41aa7b740d89b35df647f6121f3934e948abee2d38fddc52a69`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, len, reservations, self. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, len, reservations[0].read_text, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[6].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:142`; AST `2099c67bc78ae7c7706164fd4c5f0ee35050e69339007d60a1a077eb04430cc2`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, len, reservations. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, len, reservations[0].read_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[6].value.args[0].args[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:142`; AST `86d1151eb004423774cd01ebd3e3565380c5a0d17e82ae127e61e02ec652f7af`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, reservations. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, reservations[0].read_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[6].value.args[0].args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_budget_reservations_prevent_repeated_fresh_runs::root.body[17].body[4].body[6].value.args[0].args[0].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:142`; AST `370a48e4a22cbe2b463e2b63039ec40667b18d926d1c7cda7ac6c69c195aedf6`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reservations. Outputs/bindings: (none).
Calls/effect boundaries: reservations[0].read_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[6].value.args[0].args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_redaction_still_respects_context_byte_budget::root.body[17].body[5]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:144`; AST `59289e094b4e06c47bfdca8ab5a7bbc4611846725239ecc418ac9830371bd962`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: len, response, self. Outputs/bindings: response.
Calls/effect boundaries: len, response['text'].encode, self.assertLessEqual, self.call, self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_redaction_still_respects_context_byte_budget::root.body[17].body[5].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:145`; AST `0eab223a0559165692ba302899213c2e627b6083661c11425a7d0f4559274d2e`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_redaction_still_respects_context_byte_budget::root.body[17].body[5].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:145`; AST `454267249f10232dba62252a501f48346f812667dd893f9889f5d5d9b2b6304c`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_redaction_still_respects_context_byte_budget::root.body[17].body[5].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:146`; AST `80835cfc0e689d8f00ad359a9bb0d5938f0eab7ea900504648b8dfbcb1b04e6e`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: response.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_redaction_still_respects_context_byte_budget::root.body[17].body[5].body[1].value::Call

Source: `infra/tests/test_destiny_hardening.py:146`; AST `d4351532f7c0e59ecc82bdee958079cde4f8709e480eb4b8a6c8bd310eb4bba4`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_redaction_still_respects_context_byte_budget::root.body[17].body[5].body[2]::Expr

Source: `infra/tests/test_destiny_hardening.py:147`; AST `2b92127a2de9434becea3a2f944e5c6289746b350edbe3476a92281965c53778`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, response, self. Outputs/bindings: (none).
Calls/effect boundaries: len, response['text'].encode, self.assertLessEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_redaction_still_respects_context_byte_budget::root.body[17].body[5].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:147`; AST `426446cc5930dfcb7dd4bef563ded6014a37a1b6a49b8e02f9777a6abe9e413a`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, response, self. Outputs/bindings: (none).
Calls/effect boundaries: len, response['text'].encode, self.assertLessEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_redaction_still_respects_context_byte_budget::root.body[17].body[5].body[2].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:147`; AST `33f4323530e46b10fa93fba5b85d607612a292861faa2cce79174a921def606b`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, response. Outputs/bindings: (none).
Calls/effect boundaries: len, response['text'].encode.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_redaction_still_respects_context_byte_budget::root.body[17].body[5].body[2].value.args[0].args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:147`; AST `99e9984aad38d4dd66ef0e6c65e4045626163839b02b8769962334b229075673`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: response. Outputs/bindings: (none).
Calls/effect boundaries: response['text'].encode.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:149`; AST `1f1edd940039f85ffc5cac438ea9eb86e23bbb47fc5bc38f6230138b981cb37a`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: len, response, self. Outputs/bindings: response.
Calls/effect boundaries: len, self.assertEqual, self.assertTrue, self.call, self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:150`; AST `99e95d51e16ef0dc4b7df9c828fb4e27a2930c9510ae71d950fb7c94047a0acf`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:150`; AST `8e9fb463c1e5994a4e6ecf561adbac253a0a2ea6cff1382f2b8ce72b24e0ca72`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:151`; AST `f4eed525e9fa6ce67e56173e7360f0f149eec0517959a060ab1f3898816db851`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: response.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[1].value::Call

Source: `infra/tests/test_destiny_hardening.py:151`; AST `f5a1b0c81448d3bbfbea73dbfca3df9c0ffe639c83c75111217d64cbb1239516`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[2]::Expr

Source: `infra/tests/test_destiny_hardening.py:152`; AST `5c8e9d78a940ef7609712718f6498d602e13779421551be8b355718affb727d9`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, response, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:152`; AST `6559beb94fdbf3ebd9da827b4e01e6c0bdb4382e16cb351c70540fed63d4ea4a`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, response, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[2].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:152`; AST `36d254a7b326c3213d4e02521ba5effcce47c722467a3502707c0af7d55b55cc`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, response. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[3]::Expr

Source: `infra/tests/test_destiny_hardening.py:153`; AST `4897e05c6b68f611b335f841f84b270959319f5e4cf2db6e882e2bcfe82715e5`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: response, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[3].value::Call

Source: `infra/tests/test_destiny_hardening.py:153`; AST `188c5ab454a2005cd2c1088c386a6121f3b9d347a1487027b2574ea020983c21`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: response, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[4]::Assign

Source: `infra/tests/test_destiny_hardening.py:154`; AST `f066b86429c23fe255f39bac9d04eab5f3ab1ae309169b120286052b4ddf2f6d`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: response.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[4].value::Call

Source: `infra/tests/test_destiny_hardening.py:154`; AST `0e0138c71bfdb0cb1f47f44a69918ccbcbaa527703cba11c4d53b46a01cea66e`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[5]::Expr

Source: `infra/tests/test_destiny_hardening.py:155`; AST `55a10639f4ee9e9fe6dee0fc6d23ad742edbde2ed8828937d81f06a138c8d606`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: response, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[5].value::Call

Source: `infra/tests/test_destiny_hardening.py:155`; AST `f505f285c449279fcc76217e555b82cefe26ee564673066d1499ab9c86180a63`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: response, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[6]::Assign

Source: `infra/tests/test_destiny_hardening.py:156`; AST `e720a963acb7cc1d0e83408a19235b1e792e691db0b1600eb4830a37d08cf0d6`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: response.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[6].value::Call

Source: `infra/tests/test_destiny_hardening.py:156`; AST `1e7504464140a99df16f5aafeef5f4aa70f2504c3b0ebabfe6f634ed6fe1f879`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[7]::Expr

Source: `infra/tests/test_destiny_hardening.py:157`; AST `8e435d30e5ae6956dfa56f1d371145e1b88f99b505460c8b628b6a1ae0bd2f24`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: response, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_context_handles_long_lines_and_out_of_range_selection::root.body[17].body[6].body[7].value::Call

Source: `infra/tests/test_destiny_hardening.py:157`; AST `dbb293f5d2b6bc949cecd8fcc08d121c7fa8f1b0472dac6799b951dfa5ddca77`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: response, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignore_policy_changes_select_full_matrix::root.body[17].body[7]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:159`; AST `900d55861c2f15f20c0690474d1cc2606a02326d0e2e7e991fa614ebc5adeb40`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ids, row, self. Outputs/bindings: ids, row.
Calls/effect boundaries: self.assertIn, self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignore_policy_changes_select_full_matrix::root.body[17].body[7].body[0]::Assign

Source: `infra/tests/test_destiny_hardening.py:160`; AST `c2bb7c7e6f0c926a188ba170593db2ad125810df6039c0e5a1152f14b1daffd4`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: row, self. Outputs/bindings: ids, row.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignore_policy_changes_select_full_matrix::root.body[17].body[7].body[0].value::SetComp

Source: `infra/tests/test_destiny_hardening.py:160`; AST `91863d4ff5f372d35b8f474d1991241653bcbd079089addcc489a1f42c1c6fba`.

Rust module: `infra::tests::test_destiny_hardening`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: row, self. Outputs/bindings: row.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[17].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignore_policy_changes_select_full_matrix::root.body[17].body[7].body[0].value.generators[0].iter.value::Call

Source: `infra/tests/test_destiny_hardening.py:160`; AST `b75e9aa08495e4ad5bb6241030c393d34a7aa410f4e86ce3d93fdcc191686fea`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[0].value.generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignore_policy_changes_select_full_matrix::root.body[17].body[7].body[1]::Expr

Source: `infra/tests/test_destiny_hardening.py:161`; AST `352bc43e5d64f538847c44d7ceac7d287f317c7a8143ed8468b0d359ec262d71`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_ignore_policy_changes_select_full_matrix::root.body[17].body[7].body[1].value::Call

Source: `infra/tests/test_destiny_hardening.py:161`; AST `ea6eccaf17bda9b03a76bb9a3e435209f0a3982e1b58e46b19145289f58c6f5d`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8]::FunctionDef

Source: `infra/tests/test_destiny_hardening.py:163`; AST `686b0d6483b132207f9556d3bbf28a456c95c0b432be8089f4b02683754980ca`.

Rust module: `infra::tests::test_destiny_hardening`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: receipt, result, self, text. Outputs/bindings: receipt, result, text.
Calls/effect boundaries: receipt.read_text, receipt.write_text, self.assertEqual, self.call, text.replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[0]::Assign

Source: `infra/tests/test_destiny_hardening.py:164`; AST `6095e5e6f3a12b2180157bd3e95d20a1ce808ad0a31224430858d163bcc246db`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:164`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[1]::Assign

Source: `infra/tests/test_destiny_hardening.py:165`; AST `a6d43dbdb866a6ad257eb32a63c25480d6ada121b6fe930373bc7103056b7d8a`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: receipt.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[2]::Assign

Source: `infra/tests/test_destiny_hardening.py:166`; AST `e141161136ed6c8f5806228a69680b15e22397a8a2ccedaa68ec1d9ba2ea0951`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: text.
Calls/effect boundaries: receipt.read_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[2].value::Call

Source: `infra/tests/test_destiny_hardening.py:166`; AST `f38e64c40710d9149ed35c27ed3d29c8014f557fd0eb0982318d50d522e22207`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: receipt.read_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[3]::Expr

Source: `infra/tests/test_destiny_hardening.py:167`; AST `81c7994974908e73f810bd88f0eda7856daf6f3bed06668dbfabd8b6918449fc`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, text. Outputs/bindings: (none).
Calls/effect boundaries: receipt.write_text, text.replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[3].value::Call

Source: `infra/tests/test_destiny_hardening.py:167`; AST `5daf2f542ac748f9a05a65301148bb210332d13dd4a40a3954e1a6e8c3766ba5`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, text. Outputs/bindings: (none).
Calls/effect boundaries: receipt.write_text, text.replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[3].value.args[0]::Call

Source: `infra/tests/test_destiny_hardening.py:167`; AST `bf7e1e07b708db8b8877078163304410ef25649e67be1f014b97afe4bc7a1bc7`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: text.replace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[4]::Expr

Source: `infra/tests/test_destiny_hardening.py:168`; AST `fd53fd8af409653b0a87a0370e9ce189bf149d9470803a2d26e6b8cdbe582507`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[4].value::Call

Source: `infra/tests/test_destiny_hardening.py:168`; AST `2313b002d1d6973486e7fc4915dcb513b96478c83ad3ad23b024a356f1fa1a04`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::TestDestinyHardening::test_duplicate_json_keys_do_not_override_receipt_fields::root.body[17].body[8].body[4].value.args[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:168`; AST `c5f2713d7b7fa3cb1effa468e9bdfb1d2d135455e45c21093613ae0de6fef8e7`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[4].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[18]::If

Source: `infra/tests/test_destiny_hardening.py:171`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_destiny_hardening`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered If evaluation at root.body[18]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[18].body[0]::Expr

Source: `infra/tests/test_destiny_hardening.py:172`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_destiny_hardening`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_hardening.py::module::root.body[18].body[0].value::Call

Source: `infra/tests/test_destiny_hardening.py:172`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_destiny_hardening`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.process, dataclasses, hashlib, io, json, pathlib, subprocess, sys, tarfile, test_destiny, unittest.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
