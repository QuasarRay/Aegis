# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 407. Inventory digest: `e127540f09d91fbd1c1d975a6a3f27012b86d11c11bb0a664c227259a49dce58`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_atomic_transaction.py::module::root::Module

Source: `infra/tests/test_atomic_transaction.py:1`; AST `958a5c0f3a1585b99abef3007753d8ad36cc6f468dd8136f78036eb80b40052e`.

Rust module: `infra::tests::test_atomic_transaction`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: AtomicWriteError, BaseException, FileLock, FileTransaction, LockError, Mutation, NotImplementedError, OSError, Path, TransactionError, ValueError, __file__, atomic_write_bytes, barrier, bytes, calls, candidate, chr, codepoint, drive, errors, exc, fail, first, first_journal, first_path, index, inspect, journal, journal_path, journals, json, len, lexical_root, link, list, observed, ord, os, owner, path, payload, payloads, range, real, recover_named_transactions, recover_transaction, relative, resolved_root, root, runtime, second, second_journal, second_path, self, stage, stat, state, str, sys, target, td, tempfile, thread, threading, threads, transaction, tx, unittest, value, writer. Outputs/bindings: barrier, calls, candidate, codepoint, drive, errors, first, first_journal, first_path, index, journal, journal_path, journals, lexical_root, link, observed, owner, path, payload, payloads, real, relative, resolved_root, root, runtime, second, second_journal, second_path, state, target, td, thread, threads, transaction, tx, value.
Calls/effect boundaries: (root / '.aegis' / 'state' / 'transactions').mkdir, FileLock, FileLock(path, 'second').release, FileTransaction, FileTransaction(root, [Mutation(first, b'first-after'), Mutation(second, b'second-after')], state_dir=state, name='recovery-preflight').commit, FileTransaction(root, [Mutation(first, b'first-after')], state_dir=state, name='a-install').commit, FileTransaction(root, [Mutation(second, b'second-after')], state_dir=state, name='b-uninstall').commit, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='corrupt').commit, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='journal-order', fault=inspect).commit, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='recover').commit, Mutation, OSError, Path, Path(__file__).resolve, Path.cwd, Path.cwd().resolve, atomic_write_bytes, barrier.wait, bytes, candidate.resolve, chr, drive.resolve, errors.append, first.acquire, first.read_bytes, first.release, first.write_bytes, first_path.read_text, journal_path.read_text, journal_path.write_text, json.dumps, json.loads, len, link.symlink_to, list, observed.append, ord, path.read_text, path.write_text, range, real.read_bytes, real.write_bytes, recover_named_transactions, recover_transaction, resolved_root.relative_to, root.glob, runtime.mkdir, second.read_bytes, second.write_bytes, second_path.read_text, self.assertEqual, self.assertIn, self.assertRaises, self.assertRaisesRegex, self.assertRegex, self.fail, self.skipTest, stat.S_IMODE, state.glob, state.mkdir, str, sys.path.insert, target.chmod, target.read_bytes, target.stat, target.write_bytes, tempfile.TemporaryDirectory, thread.join, thread.start, threading.Barrier, threading.Thread, transaction.commit, tx.commit, unittest.skipIf.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[0]::Import

Source: `infra/tests/test_atomic_transaction.py:1`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Import evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[1]::Import

Source: `infra/tests/test_atomic_transaction.py:2`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[2]::Import

Source: `infra/tests/test_atomic_transaction.py:3`; AST `c22b5a111acc3bea9e5136e41e207f1f95083e90d861516ce34d682526721c86`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[3]::Import

Source: `infra/tests/test_atomic_transaction.py:4`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[4]::Import

Source: `infra/tests/test_atomic_transaction.py:5`; AST `80f21c52b46d18d972ae93db225486a900db10799e9bdba98d07dbcc819ff502`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[5]::Import

Source: `infra/tests/test_atomic_transaction.py:6`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_atomic_transaction.py:7`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[7]::Import

Source: `infra/tests/test_atomic_transaction.py:8`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[8]::Expr

Source: `infra/tests/test_atomic_transaction.py:10`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[8].value::Call

Source: `infra/tests/test_atomic_transaction.py:10`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[8].value.args[1]::Call

Source: `infra/tests/test_atomic_transaction.py:10`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[8].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_atomic_transaction.py:10`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[8].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_atomic_transaction.py:10`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_atomic_transaction.py:12`; AST `248093648532035fb26d9a3bc76f1b0343a4c53f752449cd22b0f7676de91cbb`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_atomic_transaction.py:13`; AST `0e2740e1f66c0ed90a634f2363541ad65e40b16a7553a0cad87ec9129f3c0517`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_atomic_transaction.py:14`; AST `18521ef0e8871ca3fce05ce0781e92dd5cf7c04237929d89f78b3c19204da4bc`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::root.body[12]::ClassDef

Source: `infra/tests/test_atomic_transaction.py:17`; AST `a1cac4e89392caecd916582976c1a5b13bfa9ba6ac880a7ff181e3f970ca43ef`.

Rust module: `infra::tests::test_atomic_transaction`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: AtomicWriteError, BaseException, NotImplementedError, OSError, Path, ValueError, atomic_write_bytes, barrier, bytes, candidate, chr, codepoint, drive, errors, exc, fail, index, len, lexical_root, link, list, ord, os, payload, payloads, range, real, relative, resolved_root, root, runtime, self, stage, stat, target, td, tempfile, thread, threading, threads, unittest, writer. Outputs/bindings: barrier, candidate, codepoint, drive, errors, index, lexical_root, link, payload, payloads, real, relative, resolved_root, root, runtime, target, td, thread, threads.
Calls/effect boundaries: OSError, Path, Path.cwd, Path.cwd().resolve, atomic_write_bytes, barrier.wait, bytes, candidate.resolve, chr, drive.resolve, errors.append, len, link.symlink_to, list, ord, range, real.read_bytes, real.write_bytes, resolved_root.relative_to, root.glob, runtime.mkdir, self.assertEqual, self.assertIn, self.assertRaises, self.assertRaisesRegex, self.fail, self.skipTest, stat.S_IMODE, target.chmod, target.read_bytes, target.stat, target.write_bytes, tempfile.TemporaryDirectory, thread.join, thread.start, threading.Barrier, threading.Thread, unittest.skipIf.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:18`; AST `307d1590af944c1097dd752b5fe241134e72462a741d5920b506334a0340684a`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AtomicWriteError, OSError, Path, ValueError, atomic_write_bytes, candidate, chr, codepoint, drive, exc, lexical_root, ord, os, range, relative, resolved_root, runtime, self, target, td, tempfile. Outputs/bindings: candidate, codepoint, drive, lexical_root, relative, resolved_root, runtime, target, td.
Calls/effect boundaries: Path, Path.cwd, Path.cwd().resolve, atomic_write_bytes, candidate.resolve, chr, drive.resolve, ord, range, resolved_root.relative_to, runtime.mkdir, self.assertEqual, self.fail, self.skipTest, target.read_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:19`; AST `fe235487a5a16c30b9ef0bbe517caa64918c05fad197f33ad8f32df2e4c807f6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: resolved_root.
Calls/effect boundaries: Path.cwd, Path.cwd().resolve.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:19`; AST `9c98f78e1c1a07e0b3ffc0f64befa7930d313aa251dc67253efa4a90aa6495ad`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path. Outputs/bindings: (none).
Calls/effect boundaries: Path.cwd, Path.cwd().resolve.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[0].value.func.value::Call

Source: `infra/tests/test_atomic_transaction.py:19`; AST `db9a457f54120339a519ab0c10b0203c3ebbee68c042f899e0c442fb37c6bc91`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path. Outputs/bindings: (none).
Calls/effect boundaries: Path.cwd.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:20`; AST `1f114036815e200d17119d756b7344ace8a279b64594bda21946db84d53c71fc`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: resolved_root. Outputs/bindings: lexical_root.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2]::If

Source: `infra/tests/test_atomic_transaction.py:21`; AST `e28cf1f37532ce41a278a05043749109ce76fc2c1a9736ff3f3e5e672627ae03`.

Rust module: `infra::tests::test_atomic_transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: OSError, Path, ValueError, candidate, chr, codepoint, drive, ord, os, range, relative, resolved_root. Outputs/bindings: candidate, codepoint, drive, lexical_root, relative.
Calls/effect boundaries: Path, candidate.resolve, chr, drive.resolve, ord, range, resolved_root.relative_to.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered If evaluation at root.body[12].body[0].body[2]; no call, error or mutation may be omitted. Condition: os.name == 'nt'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0]::For

Source: `infra/tests/test_atomic_transaction.py:22`; AST `21fadb5dc7d338973491b7209944b21795ff63b05cccd46394a6f69a7f496c87`.

Rust module: `infra::tests::test_atomic_transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: OSError, Path, ValueError, candidate, chr, codepoint, drive, ord, range, relative, resolved_root. Outputs/bindings: candidate, codepoint, drive, lexical_root, relative.
Calls/effect boundaries: Path, candidate.resolve, chr, drive.resolve, ord, range, resolved_root.relative_to.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered For evaluation at root.body[12].body[0].body[2].body[0]; no call, error or mutation may be omitted. Iteration: codepoint in range(ord('A'), ord('Z') + 1)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].iter::Call

Source: `infra/tests/test_atomic_transaction.py:22`; AST `e80b9e6530cf945cfeb340a0d31f4f18f794eb134c81c8046e3dda268c9473d2`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ord, range. Outputs/bindings: (none).
Calls/effect boundaries: ord, range.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].iter.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:22`; AST `8c9df793d8f959ec3e13a0828bef7c9fc2161e1004b26a191ce95fac567168c8`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ord. Outputs/bindings: (none).
Calls/effect boundaries: ord.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[0].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].iter.args[1].left::Call

Source: `infra/tests/test_atomic_transaction.py:22`; AST `eac26d63a5e3bdd67b5496ccbd09072ce4a92841c7ed9ab3ceef18ed2b906e16`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ord. Outputs/bindings: (none).
Calls/effect boundaries: ord.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[0].iter.args[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:23`; AST `c6bcf15c89cd3f691d3fdce0fb6be2f2a642d98b4d8a8a33daa60ddf3dd09f68`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, chr, codepoint. Outputs/bindings: drive.
Calls/effect boundaries: Path, chr.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:23`; AST `c2d50b5345ea54f21c127efc172119f2e136a77970720d52946509c0ba3cf30b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, chr, codepoint. Outputs/bindings: (none).
Calls/effect boundaries: Path, chr.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[0].value.args[0].values[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:23`; AST `57aae79a5ceff2936909f255109f8f4427b408902dd02c45e5570f589e7a045c`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chr, codepoint. Outputs/bindings: (none).
Calls/effect boundaries: chr.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[0].body[0].value.args[0].values[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1]::Try

Source: `infra/tests/test_atomic_transaction.py:24`; AST `34d26be41edb6b2a7b1ca5a36745259db6c6a3af7e969beb581be8b6c2a7e36f`.

Rust module: `infra::tests::test_atomic_transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, ValueError, candidate, drive, relative, resolved_root. Outputs/bindings: candidate, lexical_root, relative.
Calls/effect boundaries: candidate.resolve, drive.resolve, resolved_root.relative_to.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Try evaluation at root.body[12].body[0].body[2].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:25`; AST `de0b213aa54f517506e397ac731c2716c64591437ee14fdac2c9f251ea3b0c8e`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: drive, resolved_root. Outputs/bindings: relative.
Calls/effect boundaries: drive.resolve, resolved_root.relative_to.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[2].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:25`; AST `eeaee64f58aa2dbcad071f74b1d714a842e1f4d8b5d6be70f88e4f562d43e137`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: drive, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: drive.resolve, resolved_root.relative_to.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].body[0].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:25`; AST `4a9cdd81c4a0c7055ba5572c0fe6fc4cd77f487793e898b873456aa980c11e56`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: drive. Outputs/bindings: (none).
Calls/effect boundaries: drive.resolve.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[0].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:26`; AST `d65cefdb2f76d1940bcb6c370e637bcebc01951cf7f853d4371ab4071c81c4ab`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: drive, relative. Outputs/bindings: candidate.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[2].body[0].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].body[2]::If

Source: `infra/tests/test_atomic_transaction.py:27`; AST `24c64c63b9600b41e5101151efaee2f4fef7e0384014f78f72bf03f2c7662b33`.

Rust module: `infra::tests::test_atomic_transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: candidate, resolved_root. Outputs/bindings: lexical_root.
Calls/effect boundaries: candidate.resolve.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered If evaluation at root.body[12].body[0].body[2].body[0].body[1].body[2]; no call, error or mutation may be omitted. Condition: candidate != resolved_root and candidate.resolve(strict=True) == resolved_root
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].body[2].test.values[1].left::Call

Source: `infra/tests/test_atomic_transaction.py:27`; AST `8853e3e36ce23b3ea3ce6759af5ef18d00566cd842ae93ea369fd805ad99cf88`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate. Outputs/bindings: (none).
Calls/effect boundaries: candidate.resolve.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[0].body[1].body[2].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].body[2].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:28`; AST `68a7cd861760d0367b752d8f5a59db3ffd93f27757f4f85f13cb9af9c85896bb`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate. Outputs/bindings: lexical_root.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[2].body[0].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].body[2].body[1]::Break

Source: `infra/tests/test_atomic_transaction.py:29`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Break evaluation at root.body[12].body[0].body[2].body[0].body[1].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].handlers[0]::ExceptHandler

Source: `infra/tests/test_atomic_transaction.py:30`; AST `98cfa61e0f7632eedc7072041ceda5a14f729d20eed8fb49b1063de592a087a8`.

Rust module: `infra::tests::test_atomic_transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError, ValueError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[12].body[0].body[2].body[0].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[2].body[0].body[1].handlers[0].body[0]::Continue

Source: `infra/tests/test_atomic_transaction.py:31`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Continue evaluation at root.body[12].body[0].body[2].body[0].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[3]::If

Source: `infra/tests/test_atomic_transaction.py:32`; AST `cf439da81f85c6e9e06e14deced2cab17ec8d524a0b5c71ce3c9c3a2a7e0b280`.

Rust module: `infra::tests::test_atomic_transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: lexical_root, resolved_root, self. Outputs/bindings: (none).
Calls/effect boundaries: self.skipTest.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered If evaluation at root.body[12].body[0].body[3]; no call, error or mutation may be omitted. Condition: lexical_root == resolved_root
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[3].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:33`; AST `593e84bf5f2b0cb9bff616bf7a4015e1ee6edec4d179e467604d50171023796d`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.skipTest.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[3].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:33`; AST `1325bf759a3d945b4f206b87876e15b9fd7d7c2cb47f90b1bde72c8b84e4ea2a`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.skipTest.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[4]::Assign

Source: `infra/tests/test_atomic_transaction.py:34`; AST `1fa728f95d9370f8de556957c8404c1a94045491ec160f64963dba8b553a2a99`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lexical_root. Outputs/bindings: runtime.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[5]::Expr

Source: `infra/tests/test_atomic_transaction.py:35`; AST `2f21b0d44fe596747de1390290f5d6b470dc4acecc0d8f51f396181badfbf49d`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: runtime. Outputs/bindings: (none).
Calls/effect boundaries: runtime.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[5].value::Call

Source: `infra/tests/test_atomic_transaction.py:35`; AST `5e155a51895f07a187a40871a2cf90ea3c771e046233110828fac425ca97d1e9`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: runtime. Outputs/bindings: (none).
Calls/effect boundaries: runtime.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6]::With

Source: `infra/tests/test_atomic_transaction.py:36`; AST `5370b0d1676489935304ed82c719926446dc9c59e7cc2f3e1e6bba058837e726`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: AtomicWriteError, Path, atomic_write_bytes, exc, resolved_root, runtime, self, target, td, tempfile. Outputs/bindings: target, td.
Calls/effect boundaries: Path, atomic_write_bytes, self.assertEqual, self.fail, target.read_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:36`; AST `a1ca03af6562fef299875d7dd2594ded1f0abb88c3d5f76a4a650ff1dbf0c372`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: runtime, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:37`; AST `1bf18b0dc02252f20a8b7fb783e9abb9f263ca2d94b4b7b6b8c33206a732fe4c`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: target.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[0].value.left::Call

Source: `infra/tests/test_atomic_transaction.py:37`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[1]::Try

Source: `infra/tests/test_atomic_transaction.py:38`; AST `2ee2e5394f05c22a2ec73b680b6807f92cb42ef92ceafcacd15e98af0f3e1057`.

Rust module: `infra::tests::test_atomic_transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: AtomicWriteError, atomic_write_bytes, exc, resolved_root, self, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, self.fail.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Try evaluation at root.body[12].body[0].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[1].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:39`; AST `e5f291cb57c5109b7ca931e94f298d973281d394bcf0a9049b8d28584ba1eb4e`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_bytes, resolved_root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[1].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:39`; AST `de4193cb4ce9d053dbe6589f6074182eb336811967a7371e71683302bdb137e5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_bytes, resolved_root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[1].handlers[0]::ExceptHandler

Source: `infra/tests/test_atomic_transaction.py:40`; AST `0e78f4b16f23c5ceffa08fdc4e7a68ebc8fe4620daa14d26e847558f622634b3`.

Rust module: `infra::tests::test_atomic_transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: AtomicWriteError, exc, self. Outputs/bindings: (none).
Calls/effect boundaries: self.fail.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[12].body[0].body[6].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[1].handlers[0].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:41`; AST `7ee26c7c24eabbda7d2c4b27c696782aed3898e1225032d1a0a3daa6ccfe6af7`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, self. Outputs/bindings: (none).
Calls/effect boundaries: self.fail.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[6].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[1].handlers[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:41`; AST `9a6f96a5968845fd578e0ad4130dc60dfad070d29d0a6fe88c1e927097208505`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, self. Outputs/bindings: (none).
Calls/effect boundaries: self.fail.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].body[1].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:42`; AST `e4a2ba9945332108418e63456d2b2be23605f2a672ee08794fb395e728f58f89`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:42`; AST `3962f75b929fe87f11c4a0b15ff431be6ec9062b2b3206157dd58cd796c4f239`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_accepts_lexical_alias_of_same_resolved_root::root.body[12].body[0].body[6].body[2].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:42`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:45`; AST `8166937538aff699cf1d3ae7f607d2d5ed6cf508562400c4c5eaaa85a9acbb19`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, atomic_write_bytes, os, root, self, stat, target, td, tempfile, unittest. Outputs/bindings: root, target, td.
Calls/effect boundaries: Path, atomic_write_bytes, self.assertEqual, stat.S_IMODE, target.chmod, target.stat, target.write_bytes, tempfile.TemporaryDirectory, unittest.skipIf.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:46`; AST `931d653552d0eaf5266314efe4fb77f42873f89d72def192b35035f2fd6a35ed`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: Path, atomic_write_bytes, root, self, stat, target, td, tempfile. Outputs/bindings: root, target, td.
Calls/effect boundaries: Path, atomic_write_bytes, self.assertEqual, stat.S_IMODE, target.chmod, target.stat, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:46`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:47`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:47`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:48`; AST `2620b37227fcfeab9c291559c91499bf1720cad3de3dcc149ea521a0bdaa790d`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:49`; AST `e35c2ed76dd37530ca8070f296d82f5b32004b13dfefc22471f2e97682935f6f`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:49`; AST `93daa3096ae5527ca8e39a9e7d07b78fae1a07837c97e0e8b6c719611db06e3d`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[3]::Expr

Source: `infra/tests/test_atomic_transaction.py:50`; AST `7c69abe68dd613368279a922ea433692a38fc8d4bc412eda4f5fff795db8ef85`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.chmod.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[3].value::Call

Source: `infra/tests/test_atomic_transaction.py:50`; AST `906cb7f0f0f3716b7fc135c267c49007ef2a89f1c8b87c2250ae793e5b717325`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.chmod.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[4]::Expr

Source: `infra/tests/test_atomic_transaction.py:51`; AST `7ac542e6a4918ee3b62367f76aa51e38e2954f3a951a0c50046c47fbf064466b`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_bytes, root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[4].value::Call

Source: `infra/tests/test_atomic_transaction.py:51`; AST `1fc3d1be23e7747a7b4f82d4dccbb925ec094a35dedea94fae8060ff6790b63f`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_bytes, root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[5]::Expr

Source: `infra/tests/test_atomic_transaction.py:52`; AST `99786f0d56551b9a8ecdd5ec1faf805b39f56f2d04e6bb4b924a27483b06c503`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, stat, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, stat.S_IMODE, target.stat.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[5].value::Call

Source: `infra/tests/test_atomic_transaction.py:52`; AST `bd82f4773069ed03ab5eb5a16ee9a24be01bcbec9a491e6ba29638573151ac82`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, stat, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, stat.S_IMODE, target.stat.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[5].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:52`; AST `956b0b1b461b344ca36ac0d3c16efe993ef1c6c220b7e36116bfe4859d2411bc`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stat, target. Outputs/bindings: (none).
Calls/effect boundaries: stat.S_IMODE, target.stat.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].body[0].body[5].value.args[0].args[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:52`; AST `2ecd8b29f47d7764f5897ac99ba24c990a22d66fc85e0ba6eb5543c15258a865`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.stat.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[5].value.args[0].args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_preserves_existing_posix_permission_bits::root.body[12].body[1].decorator_list[0]::Call

Source: `infra/tests/test_atomic_transaction.py:44`; AST `d33d2b58447d450c3fe0e5028e58ae4a70715fedfa0ae2c471c3f24f1972a69b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.skipIf.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].decorator_list[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:54`; AST `71ea739b960d9e0629c6e7daa5c2d62d393c7209993bc53cf73f6da140e927bd`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, Path, atomic_write_bytes, fail, list, root, self, stage, target, td, tempfile. Outputs/bindings: root, target, td.
Calls/effect boundaries: OSError, Path, atomic_write_bytes, list, root.glob, self.assertEqual, self.assertRaisesRegex, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:55`; AST `ca891594167baff8b4d3166f8369f14a8c2a599b3ba41c54b3892b8d8d556710`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: OSError, Path, atomic_write_bytes, fail, list, root, self, stage, target, td, tempfile. Outputs/bindings: root, target, td.
Calls/effect boundaries: OSError, Path, atomic_write_bytes, list, root.glob, self.assertEqual, self.assertRaisesRegex, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:55`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:56`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:56`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:57`; AST `d60bcdd382ed9f4152d47e57daefabcd841757576a5c3a91e561e01a7086fead`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:58`; AST `99434e3ef11f3b45d02246123b6b0b87847681e1f703f12c447462bb6599ee8d`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:58`; AST `3f23ae63853bfa8001fa6abeb6d9f112cfe0bb00bacadb5373c7bf86670052d7`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::fail::root.body[12].body[2].body[0].body[3]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:60`; AST `48d0feb9db065a3d9506f724d653c41ab3b05de55ed74b90dac2e5b98f793b84`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, stage. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::fail::root.body[12].body[2].body[0].body[3].body[0]::If

Source: `infra/tests/test_atomic_transaction.py:61`; AST `b456789f2232db4560730a41ffa8be2053290028d6f3212018de50484c3a8d7f`.

Rust module: `infra::tests::test_atomic_transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: OSError, stage. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered If evaluation at root.body[12].body[2].body[0].body[3].body[0]; no call, error or mutation may be omitted. Condition: stage == 'before_replace'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::fail::root.body[12].body[2].body[0].body[3].body[0].body[0]::Raise

Source: `infra/tests/test_atomic_transaction.py:62`; AST `0740ee40865e12e12380bfc8eeda5fee749d06c370abf4418371022b3892142b`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OSError. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Raise evaluation at root.body[12].body[2].body[0].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::fail::root.body[12].body[2].body[0].body[3].body[0].body[0].exc::Call

Source: `infra/tests/test_atomic_transaction.py:62`; AST `ddc8eda9fd8c5a28b4056ed6591992e19674bd05145a1bc1c45d85a88ec6d34c`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OSError. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[3].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[4]::With

Source: `infra/tests/test_atomic_transaction.py:64`; AST `c41a5b454899d5eb1e889d1e6bc2f8f32ddc52eb0ef1b0bf229b83367a47aeaf`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: OSError, atomic_write_bytes, fail, root, self, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[2].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[4].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:64`; AST `e61a0bf3b2fda42da94e9e3315ca1c61eb86f1829d6a482d22b75414128922da`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OSError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[4].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:65`; AST `531c52a3a4057ea14197acf403ab5461bea96ea56d8ce34c40acd35f7eaa9cbb`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_bytes, fail, root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[4].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:65`; AST `5301b5fb97f838b981ee733706278ddf1d26b0c94a7a763bf63c1a2fcf9a74de`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_bytes, fail, root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[5]::Expr

Source: `infra/tests/test_atomic_transaction.py:66`; AST `8a247387c6aebb2a93594a926080c84dcb269caa824147b59d6bf1dda2f3edda`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[5].value::Call

Source: `infra/tests/test_atomic_transaction.py:66`; AST `8b87738034f6eb59564e5a1e4b373c4fc4fb0d00bee852d4149822745e941064`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[5].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:66`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[6]::Expr

Source: `infra/tests/test_atomic_transaction.py:67`; AST `1a0b86dcedaf1e6bf396586807072e38c8ddd17309b8f5307677b0a615148e9a`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, root, self. Outputs/bindings: (none).
Calls/effect boundaries: list, root.glob, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[6].value::Call

Source: `infra/tests/test_atomic_transaction.py:67`; AST `3bcceb9c3d81d2a07c161cad27a958948a7bbd12f94a7beb2edcfa18baa9a30f`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, root, self. Outputs/bindings: (none).
Calls/effect boundaries: list, root.glob, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[6].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:67`; AST `eb71689c6a4219a85647c4992898867fc315a143aad069c4bb784c9f4293af6d`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, root. Outputs/bindings: (none).
Calls/effect boundaries: list, root.glob.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_never_exposes_partial_target_contents::root.body[12].body[2].body[0].body[6].value.args[0].args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:67`; AST `e3c0cd50dd0bcd86e9754b84412187760be29a51ac82ccea279ed4358d7d4526`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.glob.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].body[6].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:69`; AST `cfd73b9438250ecc2510f06c72049d0cb58c29b5bbd5bae384e9726898b73ca6`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AtomicWriteError, NotImplementedError, OSError, Path, atomic_write_bytes, link, real, root, self, td, tempfile. Outputs/bindings: link, real, root, td.
Calls/effect boundaries: Path, atomic_write_bytes, link.symlink_to, real.read_bytes, real.write_bytes, self.assertEqual, self.assertRaises, self.skipTest, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:70`; AST `e315f04446b78a60580bec2e1b58fde1b40981bcb3f0154b607445f3e9fcb93e`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: AtomicWriteError, NotImplementedError, OSError, Path, atomic_write_bytes, link, real, root, self, td, tempfile. Outputs/bindings: link, real, root, td.
Calls/effect boundaries: Path, atomic_write_bytes, link.symlink_to, real.read_bytes, real.write_bytes, self.assertEqual, self.assertRaises, self.skipTest, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:70`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:71`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:71`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:72`; AST `340e57488f3d5429f3f0c170127613d874e85999abfd5bfe43967608ce5f700e`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: real.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:73`; AST `3568be8f59a88371ea80591cacbe28bd0fd5b68894314fd568d43dbbf6f415f2`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: real. Outputs/bindings: (none).
Calls/effect boundaries: real.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:73`; AST `dc4d7303f1c028b696ab12312ed0a547920e3e93c17ad6d09b07f535df41c4f4`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: real. Outputs/bindings: (none).
Calls/effect boundaries: real.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[3]::Assign

Source: `infra/tests/test_atomic_transaction.py:74`; AST `ac56b038f5e2593e5a3d28c0405457421428260ff5d001896bdd77721b762afb`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: link.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[4]::Try

Source: `infra/tests/test_atomic_transaction.py:75`; AST `c03186cc2396b57a1f57938dc71104d42156e8f536f23c68bf9001691357e82e`.

Rust module: `infra::tests::test_atomic_transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: NotImplementedError, OSError, link, real, self. Outputs/bindings: (none).
Calls/effect boundaries: link.symlink_to, self.skipTest.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Try evaluation at root.body[12].body[3].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[4].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:76`; AST `cc072c71ffa3565909af667ae2186907aa9d6738e7d2d52110586315507a7125`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: link, real. Outputs/bindings: (none).
Calls/effect boundaries: link.symlink_to.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[4].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:76`; AST `8130642c25067182e9afd743ff3d4cf70c34cbd8fd6ee3169fc5e897ee6571da`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: link, real. Outputs/bindings: (none).
Calls/effect boundaries: link.symlink_to.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[4].handlers[0]::ExceptHandler

Source: `infra/tests/test_atomic_transaction.py:77`; AST `2a92440aff72fefc2c68dbb4b49e51c705a1fe6e8f45e9ebb4353741c9a3221d`.

Rust module: `infra::tests::test_atomic_transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: NotImplementedError, OSError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.skipTest.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[12].body[3].body[0].body[4].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[4].handlers[0].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:78`; AST `b4970fc1c7283f1fdd6e3b242f65439c177bbf53e199cd68bbf632c5cb504540`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.skipTest.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[4].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[4].handlers[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:78`; AST `8b22fe712c52552964be8f3cedafd613a0e68622f302242f27df495911e7a318`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.skipTest.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[4].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[5]::With

Source: `infra/tests/test_atomic_transaction.py:79`; AST `fd35490a4dfb9897627469731629d6980cd3ecbfa0dae4a3171d539b1591d3d4`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: AtomicWriteError, atomic_write_bytes, link, root, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, self.assertRaises.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[3].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[5].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:79`; AST `d1ac5595224ee424f1e7dc81fa0c16e0e23520975ce243e867004e9109d8ae72`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AtomicWriteError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[5].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:80`; AST `bbf1d98f4609e40899bdb6705d2d7968917d9e4e09bb68e5395285784f03a4fd`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_bytes, link, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[5].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:80`; AST `3b0a8343581d8181a9c2c727b2f3244100d1544edad6d17084cad1b74cf53b65`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_bytes, link, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[6]::Expr

Source: `infra/tests/test_atomic_transaction.py:81`; AST `faa54409aeceddc696615185a122fcacbf36b9afe13fb446edd88fd77415325d`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: real, self. Outputs/bindings: (none).
Calls/effect boundaries: real.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[6].value::Call

Source: `infra/tests/test_atomic_transaction.py:81`; AST `aa50cbdac7df624d4064aa0173f66a73f7b36cf10da3b6e771373675a3d75d61`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: real, self. Outputs/bindings: (none).
Calls/effect boundaries: real.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_rejects_target_symlink_when_policy_requires_real_file::root.body[12].body[3].body[0].body[6].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:81`; AST `c579dd978f86c596855a5fe7ffecdc571e6be49f06f1f6ed68e160c4873ba4a6`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: real. Outputs/bindings: (none).
Calls/effect boundaries: real.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:83`; AST `cc399087632f5e3e26d8a02c8d3e4d4a80753f2bb993d94a9416e2c094740478`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, Path, atomic_write_bytes, barrier, bytes, errors, exc, index, len, payload, payloads, range, root, self, target, td, tempfile, thread, threading, threads, writer. Outputs/bindings: barrier, errors, index, payload, payloads, root, target, td, thread, threads.
Calls/effect boundaries: Path, atomic_write_bytes, barrier.wait, bytes, errors.append, len, range, self.assertEqual, self.assertIn, target.read_bytes, tempfile.TemporaryDirectory, thread.join, thread.start, threading.Barrier, threading.Thread.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:84`; AST `ac58e08b35a1ae2b971547ebecbc27782edb222d51d78fb3ca3bdb9ff52bb148`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: BaseException, Path, atomic_write_bytes, barrier, bytes, errors, exc, index, len, payload, payloads, range, root, self, target, td, tempfile, thread, threading, threads, writer. Outputs/bindings: barrier, errors, index, payload, payloads, root, target, td, thread, threads.
Calls/effect boundaries: Path, atomic_write_bytes, barrier.wait, bytes, errors.append, len, range, self.assertEqual, self.assertIn, target.read_bytes, tempfile.TemporaryDirectory, thread.join, thread.start, threading.Barrier, threading.Thread.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:84`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:85`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:85`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:86`; AST `efd9c76709cce3daa9a1be51fbd297f57dc69638ccd4fbf8a03e2caf06ace556`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[2]::Assign

Source: `infra/tests/test_atomic_transaction.py:87`; AST `8c6b539891294ebcdc6d750227411a4c0715eda4b10de1ee65c555f23be661ec`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bytes, index, range. Outputs/bindings: index, payloads.
Calls/effect boundaries: bytes, range.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[2].value::ListComp

Source: `infra/tests/test_atomic_transaction.py:87`; AST `bd066ad0cac010d738462748299a376fecadc62fa8187b408fb064fd2eda7f83`.

Rust module: `infra::tests::test_atomic_transaction`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: bytes, index, range. Outputs/bindings: index.
Calls/effect boundaries: bytes, range.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[4].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[2].value.elt.left::Call

Source: `infra/tests/test_atomic_transaction.py:87`; AST `41bf6da0bb699f9624f19f92a1e958aca62e7a21a51dd3aa09f29df5310d50b0`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bytes, index. Outputs/bindings: (none).
Calls/effect boundaries: bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[2].value.elt.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[2].value.generators[0].iter::Call

Source: `infra/tests/test_atomic_transaction.py:87`; AST `5b272273647f097321d81e2774859e334dc07fa496f8070774fac42fa910fcc3`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[2].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[3]::Assign

Source: `infra/tests/test_atomic_transaction.py:88`; AST `dd15540491a7418f7e86c572e10eb73aa4a826ebecd6153f2b51959db1d1a7e3`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, payloads, threading. Outputs/bindings: barrier.
Calls/effect boundaries: len, threading.Barrier.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[3].value::Call

Source: `infra/tests/test_atomic_transaction.py:88`; AST `84c49ec319cd74981e98e7ac5e12aacca8a568662c85c4bcdfc608fbf77aa450`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, payloads, threading. Outputs/bindings: (none).
Calls/effect boundaries: len, threading.Barrier.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[3].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:88`; AST `72283871a3b5d1f6611256ba4cb15efac2630f0115c789b62246883935e0b5ae`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, payloads. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[4]::Assign

Source: `infra/tests/test_atomic_transaction.py:89`; AST `77905525b1838757d9a36638b843bc37695d709437ca6ae4dd4e7b7ff74949e3`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: errors.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::writer::root.body[12].body[4].body[0].body[5]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:91`; AST `1adb746e921aae413e8117153287d8f488f89f0888dacbfb86e5766a6be85684`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, atomic_write_bytes, barrier, errors, exc, payload, root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, barrier.wait, errors.append.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[4].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::writer::root.body[12].body[4].body[0].body[5].body[0]::Try

Source: `infra/tests/test_atomic_transaction.py:92`; AST `2c7fc82d9667702f57cc12ad7ba8b21f9b68da840958a9a0a1b563d9593da6b0`.

Rust module: `infra::tests::test_atomic_transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, atomic_write_bytes, barrier, errors, exc, payload, root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, barrier.wait, errors.append.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Try evaluation at root.body[12].body[4].body[0].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::writer::root.body[12].body[4].body[0].body[5].body[0].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:93`; AST `d38990dbd1492fa14587d6788256273dc3e585ed55a26e62b4fda4a9d57d46ce`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: barrier. Outputs/bindings: (none).
Calls/effect boundaries: barrier.wait.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::writer::root.body[12].body[4].body[0].body[5].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:93`; AST `24ab74802de623c2cbd002bbf86a856defa279f22663a779ae19e63fcccb48a9`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: barrier. Outputs/bindings: (none).
Calls/effect boundaries: barrier.wait.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::writer::root.body[12].body[4].body[0].body[5].body[0].body[1]::Expr

Source: `infra/tests/test_atomic_transaction.py:94`; AST `22383b9fa3de4dc1eeb8e4eb3f0eaa51c41d0d46510341b8b09b70e783b15f51`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_bytes, payload, root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[5].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::writer::root.body[12].body[4].body[0].body[5].body[0].body[1].value::Call

Source: `infra/tests/test_atomic_transaction.py:94`; AST `ffb94f1af381a9a8a530737d2e9c4472ed80a8b52835a0aa9de9ea24b5e17dbf`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_bytes, payload, root, target. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[5].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::writer::root.body[12].body[4].body[0].body[5].body[0].handlers[0]::ExceptHandler

Source: `infra/tests/test_atomic_transaction.py:95`; AST `e2efaf1d4ff0a1908933eafcd9dc0a36ee0933fd5601be153043b762bad1b333`.

Rust module: `infra::tests::test_atomic_transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, errors, exc. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[12].body[4].body[0].body[5].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::writer::root.body[12].body[4].body[0].body[5].body[0].handlers[0].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:96`; AST `cd3d96b6f215664fe6f582a5349105453074e7d4fcde75f6fd0802e50a6e3e50`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors, exc. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[5].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::writer::root.body[12].body[4].body[0].body[5].body[0].handlers[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:96`; AST `b10be4f4ba7063c84562bb9f7d182c7cb9ea357a013aa6824e60333ff7cb77b6`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors, exc. Outputs/bindings: (none).
Calls/effect boundaries: errors.append.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[5].body[0].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[6]::Assign

Source: `infra/tests/test_atomic_transaction.py:98`; AST `2a0189e6ddbe60b483ffbc279bc9c396b182f0a94d6c9aa76f525d0d0037f0a0`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: payload, payloads, threading, writer. Outputs/bindings: payload, threads.
Calls/effect boundaries: threading.Thread.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[6].value::ListComp

Source: `infra/tests/test_atomic_transaction.py:98`; AST `3845da970af6981f79e11f9c5787a9fd411b78b0c887e45ee8188e7e3994e038`.

Rust module: `infra::tests::test_atomic_transaction`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: payload, payloads, threading, writer. Outputs/bindings: payload.
Calls/effect boundaries: threading.Thread.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[4].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[6].value.elt::Call

Source: `infra/tests/test_atomic_transaction.py:98`; AST `37c495952eed23c0aa2992c89debab284cec0fd1a1585fa436f3de07886ddbeb`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload, threading, writer. Outputs/bindings: (none).
Calls/effect boundaries: threading.Thread.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[6].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[7]::For

Source: `infra/tests/test_atomic_transaction.py:99`; AST `4cd977966210c0bce53f4431aab698cd23fb4d1e8d9b485e369860c7e7e1138f`.

Rust module: `infra::tests::test_atomic_transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: thread, threads. Outputs/bindings: thread.
Calls/effect boundaries: thread.start.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered For evaluation at root.body[12].body[4].body[0].body[7]; no call, error or mutation may be omitted. Iteration: thread in threads
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[7].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:100`; AST `3258a8d0b89c0cfb474a9ce925505ed568eef21127d26cfb49ef806f873612b0`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: thread. Outputs/bindings: (none).
Calls/effect boundaries: thread.start.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[7].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:100`; AST `e4ebc1eaa133ce1a79a83c0adb9d8dc48a606dd6da8ec13f3b0cfa17d1721a00`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: thread. Outputs/bindings: (none).
Calls/effect boundaries: thread.start.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[8]::For

Source: `infra/tests/test_atomic_transaction.py:101`; AST `45c31fa6d8562cc6e14b92bc20d7c8736acea422fe1e50e10620ea1f05026346`.

Rust module: `infra::tests::test_atomic_transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: thread, threads. Outputs/bindings: thread.
Calls/effect boundaries: thread.join.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered For evaluation at root.body[12].body[4].body[0].body[8]; no call, error or mutation may be omitted. Iteration: thread in threads
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[8].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:102`; AST `1648f96d1d40631251f8f40a1ca033bcf87d9ea380a950171debe0063be7efa3`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: thread. Outputs/bindings: (none).
Calls/effect boundaries: thread.join.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[8].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:102`; AST `e80dceb1eb79ec3421c8bdeeffd9a5ebc9f94624d0b5337c6c807c6d7167f28c`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: thread. Outputs/bindings: (none).
Calls/effect boundaries: thread.join.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[9]::Expr

Source: `infra/tests/test_atomic_transaction.py:103`; AST `c2b211e8dd8f6fe6797fc74d9c816e36ab4d97d48b3ccd37988c881503e35b45`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[9].value::Call

Source: `infra/tests/test_atomic_transaction.py:103`; AST `75f48079c43568ad9ca87a64f39ff017bdf1dbb8733f56e3a421e3111d24e00c`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: errors, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[10]::Expr

Source: `infra/tests/test_atomic_transaction.py:104`; AST `5070d1b63771a9bf5f03369a60011227c110bff2a948a08c0507bdd0aec4e369`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: payloads, self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[10].value::Call

Source: `infra/tests/test_atomic_transaction.py:104`; AST `ba37a918a11c71a9256caeaf8686b90060d0093813cbbfc4d51f6d0185cc51dd`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payloads, self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestAtomicWrite::test_atomic_write_concurrent_writers_never_produce_torn_file::root.body[12].body[4].body[0].body[10].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:104`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::root.body[13]::ClassDef

Source: `infra/tests/test_atomic_transaction.py:107`; AST `7686d5400510c06b1237012326b27759f40ec820a080f9ef03995729d2f9a4f1`.

Rust module: `infra::tests::test_atomic_transaction`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: FileLock, FileTransaction, LockError, Mutation, OSError, Path, TransactionError, calls, fail, first, first_journal, first_path, inspect, journal, journal_path, journals, json, len, list, observed, owner, path, recover_named_transactions, recover_transaction, root, second, second_journal, second_path, self, stage, state, target, td, tempfile, transaction, tx, unittest, value. Outputs/bindings: calls, first, first_journal, first_path, journal, journal_path, journals, observed, owner, path, root, second, second_journal, second_path, state, target, td, transaction, tx, value.
Calls/effect boundaries: (root / '.aegis' / 'state' / 'transactions').mkdir, FileLock, FileLock(path, 'second').release, FileTransaction, FileTransaction(root, [Mutation(first, b'first-after'), Mutation(second, b'second-after')], state_dir=state, name='recovery-preflight').commit, FileTransaction(root, [Mutation(first, b'first-after')], state_dir=state, name='a-install').commit, FileTransaction(root, [Mutation(second, b'second-after')], state_dir=state, name='b-uninstall').commit, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='corrupt').commit, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='journal-order', fault=inspect).commit, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='recover').commit, Mutation, OSError, Path, first.acquire, first.read_bytes, first.release, first.write_bytes, first_path.read_text, journal_path.read_text, journal_path.write_text, json.dumps, json.loads, len, list, observed.append, path.read_text, path.write_text, recover_named_transactions, recover_transaction, second.read_bytes, second.write_bytes, second_path.read_text, self.assertEqual, self.assertRaises, self.assertRaisesRegex, self.assertRegex, state.glob, state.mkdir, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory, transaction.commit, tx.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:108`; AST `ed414bfe4d414cd39d388e12abeafcb7a0542a33c7e8d36125aa5f32b58e121c`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, Mutation, Path, TransactionError, root, self, state, target, td, tempfile, transaction. Outputs/bindings: root, state, target, td, transaction.
Calls/effect boundaries: FileTransaction, Mutation, Path, self.assertEqual, self.assertRaisesRegex, state.mkdir, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory, transaction.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:109`; AST `3ecf875e9e712eeed8b7e9cc55f5195a4abe536292cf5909cd341a5de2284789`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileTransaction, Mutation, Path, TransactionError, root, self, state, target, td, tempfile, transaction. Outputs/bindings: root, state, target, td, transaction.
Calls/effect boundaries: FileTransaction, Mutation, Path, self.assertEqual, self.assertRaisesRegex, state.mkdir, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory, transaction.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:109`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:110`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:110`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:111`; AST `d8d2ca266e8a736df1475b1804eb980f0e06be09e8dbfbe650c370fa6ac723a6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:112`; AST `69e04085199b093eaac5e2af509fe8518fefb21e6f6994c4f1e68977906a5214`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:112`; AST `28a147563ac722ec23c0f204d62f9d1ac3a56abc0b1c08c3bad3b91dff8f088b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[3]::Assign

Source: `infra/tests/test_atomic_transaction.py:113`; AST `2c45b8a0703cc1848e9a86aecb72aca73629056fd88b159cd2b96d52396be317`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[4]::Expr

Source: `infra/tests/test_atomic_transaction.py:114`; AST `727c7a5d572e59f33a49316683b10fa751647acfea6bf804381cd119ea39a7c9`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[4].value::Call

Source: `infra/tests/test_atomic_transaction.py:114`; AST `b8c46d20bb28cddb3f01df122b992f0725601c6ae4d19ba558a866a931bbe4a0`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[5]::Assign

Source: `infra/tests/test_atomic_transaction.py:115`; AST `34003e09a242f0fb4a6d3cda107af466e1527052da9ac80f78f5ef741e8b14c2`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, Mutation, root, state, target. Outputs/bindings: transaction.
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[5].value::Call

Source: `infra/tests/test_atomic_transaction.py:115`; AST `ff154c468545214194310076e22a1998c9d59e7c7f5fb10b6ff0915c479ec7c3`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, root, state, target. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[5].value.args[1].elts[0]::Call

Source: `infra/tests/test_atomic_transaction.py:117`; AST `2b118d592e7e65e487ebe3bcd1a4af325aa7fe1a68e2950b0f28fbdd575fba87`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, target. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[5].value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[6]::With

Source: `infra/tests/test_atomic_transaction.py:121`; AST `8ce3a93a8be23a3df94ebc8a73433e432c485bb618c6b981b54c5a6de5013bbe`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: TransactionError, self, transaction. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, transaction.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[0].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[6].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:121`; AST `18d4134f7838eae1cdfc331b719e4c54d5802522f505dfad35c030f714d7e954`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[6].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[6].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:122`; AST `096da3682c424d7cfe517afb7badd816237ae46aa044a5e16f178d748739305b`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: transaction. Outputs/bindings: (none).
Calls/effect boundaries: transaction.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[0].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[6].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:122`; AST `b698aa591461b55826847a2e71268465007c927f7e7fa953f0eecb9db5e95c9c`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: transaction. Outputs/bindings: (none).
Calls/effect boundaries: transaction.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[7]::Expr

Source: `infra/tests/test_atomic_transaction.py:123`; AST `c08d19ff158ae776aaea0ca13cf60ebe09bc6653d1e1f846be0b9f0c86e386c6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[7].value::Call

Source: `infra/tests/test_atomic_transaction.py:123`; AST `a048647751a5507081d9369ec07ca6efbb4dc2209b3d1b51fa273024b70004a4`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_can_require_destination_absence_without_conflating_empty_file::root.body[13].body[0].body[0].body[7].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:123`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:125`; AST `3ddb50d99e711891ac71486c49e7346418803a2cba5884a8446fe222e2c9fdfe`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, Mutation, OSError, Path, calls, fail, first, root, second, self, stage, td, tempfile, tx. Outputs/bindings: calls, first, root, second, td, tx.
Calls/effect boundaries: (root / '.aegis' / 'state' / 'transactions').mkdir, FileTransaction, Mutation, OSError, Path, first.read_bytes, first.write_bytes, second.read_bytes, second.write_bytes, self.assertEqual, self.assertRaisesRegex, tempfile.TemporaryDirectory, tx.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:126`; AST `40f2da6bdb445784cb319df3ef3c95980d49867d1b2f47060262d49f770158c7`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileTransaction, Mutation, OSError, Path, calls, fail, first, root, second, self, stage, td, tempfile, tx. Outputs/bindings: calls, first, root, second, td, tx.
Calls/effect boundaries: (root / '.aegis' / 'state' / 'transactions').mkdir, FileTransaction, Mutation, OSError, Path, first.read_bytes, first.write_bytes, second.read_bytes, second.write_bytes, self.assertEqual, self.assertRaisesRegex, tempfile.TemporaryDirectory, tx.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:126`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:127`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:127`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[1]::Expr

Source: `infra/tests/test_atomic_transaction.py:128`; AST `968f010e495106e65d36eea4792e735c6d0d3861dd124fa69c71b0fa2b8173ac`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / '.aegis' / 'state' / 'transactions').mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[1].value::Call

Source: `infra/tests/test_atomic_transaction.py:128`; AST `0b995a7c0afc04b2b1f41f651f2a3805af4448f4ef1458228c3f4e5dd11abee0`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / '.aegis' / 'state' / 'transactions').mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[2]::Assign

Source: `infra/tests/test_atomic_transaction.py:129`; AST `3ef43db03c7f88d25539595df9a849b0facfda4796115654180692ace47e92cd`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: first.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[3]::Assign

Source: `infra/tests/test_atomic_transaction.py:130`; AST `5070179907b19889525331b4c11bc4d936cd0a843d0d7623ebebca208c91498e`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: second.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[4]::Expr

Source: `infra/tests/test_atomic_transaction.py:131`; AST `a0bde866181413f36c6ed04a1ccd23851f08a7b05794d61e4a5784661dd8183f`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[4].value::Call

Source: `infra/tests/test_atomic_transaction.py:131`; AST `8a9a30a47add8f7e32a3d13a89e3d7a38204c08f7b8e2941415694e978cf4622`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[5]::Expr

Source: `infra/tests/test_atomic_transaction.py:132`; AST `764f141a1c0b67b643adee5b67d6586d789e20be12123e132cf0b233a9cf2d49`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[5].value::Call

Source: `infra/tests/test_atomic_transaction.py:132`; AST `8222b78f577f8f094326a1be9702e159b43e36ab3a2fdfdb14eefab07e982d5b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[6]::Assign

Source: `infra/tests/test_atomic_transaction.py:133`; AST `ea758fc917a6b4e922bd51abc7dcc71234b7b830a643c25f92ef27fbe64b8fc1`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: calls.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::fail::root.body[13].body[1].body[0].body[7]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:135`; AST `701ae7b2755162bb6132b550ec85300d24ce7e1cfb0c5e54712b441d5bf19100`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, calls, stage. Outputs/bindings: calls.
Calls/effect boundaries: OSError.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[1].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::fail::root.body[13].body[1].body[0].body[7].body[0]::Nonlocal

Source: `infra/tests/test_atomic_transaction.py:136`; AST `c5539003e0db0ebedac566426df17741bcc6f80e9d2a9ec08e30f6a300b5e75a`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Nonlocal evaluation at root.body[13].body[1].body[0].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::fail::root.body[13].body[1].body[0].body[7].body[1]::If

Source: `infra/tests/test_atomic_transaction.py:137`; AST `bb95ff573eb6401899883e2d9215d20fb468d46eb6ebf7f45973ae22e76c791e`.

Rust module: `infra::tests::test_atomic_transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: OSError, calls, stage. Outputs/bindings: calls.
Calls/effect boundaries: OSError.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[0].body[7].body[1]; no call, error or mutation may be omitted. Condition: stage == 'after_destination'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::fail::root.body[13].body[1].body[0].body[7].body[1].body[0]::AugAssign

Source: `infra/tests/test_atomic_transaction.py:138`; AST `44c61467ea12e0027fb3c0a954809fc03c5dbe618c3bfc8602508170bc09840b`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: calls.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered AugAssign evaluation at root.body[13].body[1].body[0].body[7].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::fail::root.body[13].body[1].body[0].body[7].body[1].body[1]::If

Source: `infra/tests/test_atomic_transaction.py:139`; AST `d1648a2009daf639b3455d93a10d71d63a68d761a64f39f380d37831005578ca`.

Rust module: `infra::tests::test_atomic_transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: OSError, calls. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[0].body[7].body[1].body[1]; no call, error or mutation may be omitted. Condition: calls == 1
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::fail::root.body[13].body[1].body[0].body[7].body[1].body[1].body[0]::Raise

Source: `infra/tests/test_atomic_transaction.py:140`; AST `ff43437ad3eedebf430d64f5a58facafe86f4382fec2602dd07ece480fbfb882`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OSError. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[1].body[0].body[7].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::fail::root.body[13].body[1].body[0].body[7].body[1].body[1].body[0].exc::Call

Source: `infra/tests/test_atomic_transaction.py:140`; AST `5b09ba11bc0ae800168b4aad4fd5618adbc9176f9f740a7cce7e32f06ba3467a`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OSError. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[7].body[1].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[8]::Assign

Source: `infra/tests/test_atomic_transaction.py:142`; AST `b0767b9b1a0d4d2aacd607f506563792da3483fdc5e61b7193bcadeda0d3aab9`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, Mutation, fail, first, root, second. Outputs/bindings: tx.
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[8].value::Call

Source: `infra/tests/test_atomic_transaction.py:142`; AST `189a619ef6cf1d72599bf12510ae06e0416665ed286a16bf01cf669dd37e591f`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, fail, first, root, second. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[8].value.args[1].elts[0]::Call

Source: `infra/tests/test_atomic_transaction.py:144`; AST `77bf1c593decf36dc93728948c8cb961857a18091f7010e8ea207e42c39f3d40`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, first. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[8].value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[8].value.args[1].elts[1]::Call

Source: `infra/tests/test_atomic_transaction.py:144`; AST `27a4350724b91c97363c68cea2f8b08489289261be6b9d82b42f3ed433cf7952`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, second. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[8].value.args[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[9]::With

Source: `infra/tests/test_atomic_transaction.py:149`; AST `e78823c4e29c5b61dc1a523447747cbc8ae7df65b0d7b22aa784da5eb1f56293`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: OSError, self, tx. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, tx.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[1].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[9].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:149`; AST `e61a0bf3b2fda42da94e9e3315ca1c61eb86f1829d6a482d22b75414128922da`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OSError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[9].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[9].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:150`; AST `a31c561bf414e0577cf3f2976780537cc707a5bb6077e25fc39c8bc78824316b`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tx. Outputs/bindings: (none).
Calls/effect boundaries: tx.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[9].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:150`; AST `5c964b850bc092342e9cbeb360f12f27f650be41a3a3e6a83ff6600fdb0658e2`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tx. Outputs/bindings: (none).
Calls/effect boundaries: tx.commit.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[10]::Expr

Source: `infra/tests/test_atomic_transaction.py:151`; AST `c179be4142e90d1838c303c470b8e81eb08e525bde95650b5ba98dde071a5a4e`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: first.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[10].value::Call

Source: `infra/tests/test_atomic_transaction.py:151`; AST `60b71c7dd5c5732cd6cf2b32d96f1fbd92e4a22056a8cda8ddf1015d9e866977`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: first.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[10].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:151`; AST `3f60cea7167c40fc7e8de55d1da9a6a5268348c51f9de64a7acfe9cdcd46a6aa`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[11]::Expr

Source: `infra/tests/test_atomic_transaction.py:152`; AST `04ea483714aa1335d82523976aeddd8943043d072d81bd26e10f15197d1a5584`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: second.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[11].value::Call

Source: `infra/tests/test_atomic_transaction.py:152`; AST `27e11252f446aef38b53308d8fe4a0baba99c5853940a45ec8aee808192e0aec`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: second.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_commit_is_all_or_nothing_across_multiple_managed_files::root.body[13].body[1].body[0].body[11].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:152`; AST `a969361b88e4bef27234abc44d61c4c159d586c7b4a79663a7d197ae29639f53`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:154`; AST `39b0be4692d1375c83e6eb993586e21ab831cd161d277af3cb0c511dadc7b0da`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, Mutation, Path, inspect, journal, journals, len, list, observed, root, self, stage, state, target, td, tempfile. Outputs/bindings: journals, observed, root, state, target, td.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='journal-order', fault=inspect).commit, Mutation, Path, len, list, observed.append, self.assertEqual, state.glob, state.mkdir, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:155`; AST `6d527a7310752353a9c26952887065bbb235c941a9914025c2c3c117445cee2c`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileTransaction, Mutation, Path, inspect, journal, journals, len, list, observed, root, self, stage, state, target, td, tempfile. Outputs/bindings: journals, observed, root, state, target, td.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='journal-order', fault=inspect).commit, Mutation, Path, len, list, observed.append, self.assertEqual, state.glob, state.mkdir, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:155`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:156`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:156`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:157`; AST `d8d2ca266e8a736df1475b1804eb980f0e06be09e8dbfbe650c370fa6ac723a6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:158`; AST `69e04085199b093eaac5e2af509fe8518fefb21e6f6994c4f1e68977906a5214`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:158`; AST `28a147563ac722ec23c0f204d62f9d1ac3a56abc0b1c08c3bad3b91dff8f088b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[3]::Assign

Source: `infra/tests/test_atomic_transaction.py:159`; AST `2c45b8a0703cc1848e9a86aecb72aca73629056fd88b159cd2b96d52396be317`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[4]::Expr

Source: `infra/tests/test_atomic_transaction.py:160`; AST `99434e3ef11f3b45d02246123b6b0b87847681e1f703f12c447462bb6599ee8d`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[4].value::Call

Source: `infra/tests/test_atomic_transaction.py:160`; AST `3f23ae63853bfa8001fa6abeb6d9f112cfe0bb00bacadb5373c7bf86670052d7`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[5]::Assign

Source: `infra/tests/test_atomic_transaction.py:161`; AST `3802255677d66fe3b0f1533dc249237217e3840125ebef188ba48cc22c5cc440`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: observed.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::inspect::root.body[13].body[2].body[0].body[6]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:163`; AST `9cb48db5ffbe4aa3467f25a4ef2ecb7bceeadb517f8169476a2847d3669022d8`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: journal, journals, len, list, observed, stage, state, target. Outputs/bindings: journals.
Calls/effect boundaries: len, list, observed.append, state.glob, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[2].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::inspect::root.body[13].body[2].body[0].body[6].body[0]::If

Source: `infra/tests/test_atomic_transaction.py:164`; AST `119ff6a5772459253155c7a3b1898fd4cd220247bc8e96f887e7972a2c67f4b3`.

Rust module: `infra::tests::test_atomic_transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: journal, journals, len, list, observed, stage, state, target. Outputs/bindings: journals.
Calls/effect boundaries: len, list, observed.append, state.glob, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered If evaluation at root.body[13].body[2].body[0].body[6].body[0]; no call, error or mutation may be omitted. Condition: stage == 'after_journal'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::inspect::root.body[13].body[2].body[0].body[6].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:165`; AST `f3f56d41db95c43a5833511ca9242328dbb944eb95c9a11d276d22371e84d298`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, state. Outputs/bindings: journals.
Calls/effect boundaries: list, state.glob.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2].body[0].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::inspect::root.body[13].body[2].body[0].body[6].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:165`; AST `e987ad4c282784dfd2b96cc77cb0befe0900f1cd52975d5d6414f4ed9b51680e`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, state. Outputs/bindings: (none).
Calls/effect boundaries: list, state.glob.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::inspect::root.body[13].body[2].body[0].body[6].body[0].body[0].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:165`; AST `85c9cf0f449c515946d15d468a6649c6f28ff8409ebdd11a05eff9ccdc38be05`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.glob.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[6].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::inspect::root.body[13].body[2].body[0].body[6].body[0].body[1]::Expr

Source: `infra/tests/test_atomic_transaction.py:166`; AST `a5516b41bb66a614f5c5a51706a672120906907b760788390b0ca599afad8e68`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal, journals, len, observed, target. Outputs/bindings: (none).
Calls/effect boundaries: len, observed.append, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2].body[0].body[6].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::inspect::root.body[13].body[2].body[0].body[6].body[0].body[1].value::Call

Source: `infra/tests/test_atomic_transaction.py:166`; AST `561bde75abbc3d26947b66287f663c804497eb1fec30a073991466d9a751e7dd`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal, journals, len, observed, target. Outputs/bindings: (none).
Calls/effect boundaries: len, observed.append, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[6].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::inspect::root.body[13].body[2].body[0].body[6].body[0].body[1].value.args[0].elts[0]::Call

Source: `infra/tests/test_atomic_transaction.py:166`; AST `134075afe9cd7098fdcbd8548ce326ce163e8244b640e7a7bc2476de94335244`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journals, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[6].body[0].body[1].value.args[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::inspect::root.body[13].body[2].body[0].body[6].body[0].body[1].value.args[0].elts[1]::Call

Source: `infra/tests/test_atomic_transaction.py:166`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[6].body[0].body[1].value.args[0].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[7]::Expr

Source: `infra/tests/test_atomic_transaction.py:168`; AST `7a26a51bd3b59f0caf3ab69f8f6ca1abd5e67d4eecf56a1dc74372b6e32451a9`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, Mutation, inspect, root, state, target. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='journal-order', fault=inspect).commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[7].value::Call

Source: `infra/tests/test_atomic_transaction.py:168`; AST `9c3fb57f302daeb4198f810716266df860bcf54e8b3348e15280f7baa47f0f07`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, inspect, root, state, target. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='journal-order', fault=inspect).commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[7].value.func.value::Call

Source: `infra/tests/test_atomic_transaction.py:168`; AST `e8600c677aafba673d1a6356bb67729d1610c0320f57c49db6bd5ba1f147a00d`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, inspect, root, state, target. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[7].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[7].value.func.value.args[1].elts[0]::Call

Source: `infra/tests/test_atomic_transaction.py:170`; AST `7b1c0658e87108bbd712eea71383032b974ed067d99ad890f3013a1505fa65a6`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, target. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[7].value.func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[8]::Expr

Source: `infra/tests/test_atomic_transaction.py:175`; AST `7e03ca5dbc99d99fb8bc7ce2ffcced62c050d1f8aa4380f812508fabaf90d7e6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_journal_is_durable_before_irreversible_persistent_commit::root.body[13].body[2].body[0].body[8].value::Call

Source: `infra/tests/test_atomic_transaction.py:175`; AST `ac812d88417393254fa3998c16e76eae55c8db2602df55f5129d19ece4c07768`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:177`; AST `91c531ce6fedb088a59a7f89fc965d4c4bc5ec136378471429edc273fc2a7d60`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, Mutation, Path, first, journal, journal_path, recover_transaction, root, second, self, state, target, td, tempfile. Outputs/bindings: first, journal, journal_path, root, second, state, target, td.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='recover').commit, Mutation, Path, recover_transaction, self.assertEqual, state.mkdir, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:178`; AST `6803c3367c4f10ec6c20579e669ba1d3de5467cb7814a2c4f00d8ee185fc014d`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileTransaction, Mutation, Path, first, journal, journal_path, recover_transaction, root, second, self, state, target, td, tempfile. Outputs/bindings: first, journal, journal_path, root, second, state, target, td.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='recover').commit, Mutation, Path, recover_transaction, self.assertEqual, state.mkdir, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:178`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:179`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:179`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:180`; AST `d8d2ca266e8a736df1475b1804eb980f0e06be09e8dbfbe650c370fa6ac723a6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:181`; AST `69e04085199b093eaac5e2af509fe8518fefb21e6f6994c4f1e68977906a5214`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:181`; AST `28a147563ac722ec23c0f204d62f9d1ac3a56abc0b1c08c3bad3b91dff8f088b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[3]::Assign

Source: `infra/tests/test_atomic_transaction.py:182`; AST `2c45b8a0703cc1848e9a86aecb72aca73629056fd88b159cd2b96d52396be317`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[4]::Expr

Source: `infra/tests/test_atomic_transaction.py:183`; AST `99434e3ef11f3b45d02246123b6b0b87847681e1f703f12c447462bb6599ee8d`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[4].value::Call

Source: `infra/tests/test_atomic_transaction.py:183`; AST `3f23ae63853bfa8001fa6abeb6d9f112cfe0bb00bacadb5373c7bf86670052d7`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[5]::Assign

Source: `infra/tests/test_atomic_transaction.py:184`; AST `c03aafb846e1f358cd76de8beb0fec0c905b17b7de718d8407df5009cf8194ea`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, Mutation, root, state, target. Outputs/bindings: journal.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='recover').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[5].value::Call

Source: `infra/tests/test_atomic_transaction.py:184`; AST `2eecce5b60b9b23cfaf07ba604a599f63ce83854316d6ca552fdf67d47c351c9`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, root, state, target. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='recover').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[5].value.func.value::Call

Source: `infra/tests/test_atomic_transaction.py:184`; AST `79a3bdcb6642dd964fc5937dc8682ecd6918a142cb6d6a53c70a2ad64e83dbb3`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, root, state, target. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[5].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[5].value.func.value.args[1].elts[0]::Call

Source: `infra/tests/test_atomic_transaction.py:186`; AST `7b1c0658e87108bbd712eea71383032b974ed067d99ad890f3013a1505fa65a6`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, target. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[5].value.func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[6]::Assign

Source: `infra/tests/test_atomic_transaction.py:190`; AST `e4dd2aacba7c8c497397c80a23b792e02b3beac3d092b3c31be853b4824b0eaf`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal, state. Outputs/bindings: journal_path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[7]::Assign

Source: `infra/tests/test_atomic_transaction.py:191`; AST `2579541b85c929928dc8b75c5707a1b0b3057489fa53e513332b98291ac5555e`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal_path, recover_transaction, root. Outputs/bindings: first.
Calls/effect boundaries: recover_transaction.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[7].value::Call

Source: `infra/tests/test_atomic_transaction.py:191`; AST `d50fbfb28d246cd2657fb3a253bf9be5780080fda01af484051918ef36511f59`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path, recover_transaction, root. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[8]::Assign

Source: `infra/tests/test_atomic_transaction.py:192`; AST `581c7e2d0bb5a5ba514ca5d498dc823fd41713d5764d25e21a773219693b7f69`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal_path, recover_transaction, root. Outputs/bindings: second.
Calls/effect boundaries: recover_transaction.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[8].value::Call

Source: `infra/tests/test_atomic_transaction.py:192`; AST `d50fbfb28d246cd2657fb3a253bf9be5780080fda01af484051918ef36511f59`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path, recover_transaction, root. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[9]::Expr

Source: `infra/tests/test_atomic_transaction.py:193`; AST `4f392042c406f625bb4c6fe3cb66a80079a28e1092352aa973fd37d2615e3f8e`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[9].value::Call

Source: `infra/tests/test_atomic_transaction.py:193`; AST `0770708ab9183598d02c08389598e7ca070969ebe8d3571aa089e1690e4e4514`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[10]::Expr

Source: `infra/tests/test_atomic_transaction.py:194`; AST `815c6baa62ab7250e806549303549631d4d995a0aa4139c5f563ffe835ce7ec4`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[10].value::Call

Source: `infra/tests/test_atomic_transaction.py:194`; AST `7d5f3ee1a284b4b1b4fbda541e16fa83d2b3cc6b08dba65b4dd3b6e3c6be944c`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[11]::Expr

Source: `infra/tests/test_atomic_transaction.py:195`; AST `054828ffabd46c735597d9fc8c5382a0082fae43e72973c24c9fbb6567f34347`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[11].value::Call

Source: `infra/tests/test_atomic_transaction.py:195`; AST `9277a7efe86a17a1622e1e79d1e953593d90b2a0d93332d0ccff427c08880b81`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_is_idempotent::root.body[13].body[3].body[0].body[11].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:195`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:197`; AST `31aaad8a9cf48bfd65fd9cb98536e605d45c81257048c554f4c28c93c088cfec`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, Mutation, Path, TransactionError, journal, journal_path, json, recover_transaction, root, self, state, target, td, tempfile, value. Outputs/bindings: journal, journal_path, root, state, target, td, value.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='corrupt').commit, Mutation, Path, journal_path.read_text, journal_path.write_text, json.dumps, json.loads, recover_transaction, self.assertEqual, self.assertRaisesRegex, state.mkdir, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:198`; AST `939a651f01b4633c74554b4259ebd06616d2f93b8f307145cd930d1800f3d0ac`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileTransaction, Mutation, Path, TransactionError, journal, journal_path, json, recover_transaction, root, self, state, target, td, tempfile, value. Outputs/bindings: journal, journal_path, root, state, target, td, value.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='corrupt').commit, Mutation, Path, journal_path.read_text, journal_path.write_text, json.dumps, json.loads, recover_transaction, self.assertEqual, self.assertRaisesRegex, state.mkdir, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:198`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:199`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:199`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:200`; AST `d8d2ca266e8a736df1475b1804eb980f0e06be09e8dbfbe650c370fa6ac723a6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:201`; AST `69e04085199b093eaac5e2af509fe8518fefb21e6f6994c4f1e68977906a5214`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:201`; AST `28a147563ac722ec23c0f204d62f9d1ac3a56abc0b1c08c3bad3b91dff8f088b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[3]::Assign

Source: `infra/tests/test_atomic_transaction.py:202`; AST `2c45b8a0703cc1848e9a86aecb72aca73629056fd88b159cd2b96d52396be317`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[4]::Expr

Source: `infra/tests/test_atomic_transaction.py:203`; AST `99434e3ef11f3b45d02246123b6b0b87847681e1f703f12c447462bb6599ee8d`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[4].value::Call

Source: `infra/tests/test_atomic_transaction.py:203`; AST `3f23ae63853bfa8001fa6abeb6d9f112cfe0bb00bacadb5373c7bf86670052d7`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[5]::Assign

Source: `infra/tests/test_atomic_transaction.py:204`; AST `4c61331d5380010668bf453db9041995a81b2d4c46949bfe57688b662a363895`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, Mutation, root, state, target. Outputs/bindings: journal.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='corrupt').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[5].value::Call

Source: `infra/tests/test_atomic_transaction.py:204`; AST `3a9bfa779c51db69cfd5bd10408c73488e2955a12c3c482bfba5a50d4613a74b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, root, state, target. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(target, b'after')], state_dir=state, name='corrupt').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[5].value.func.value::Call

Source: `infra/tests/test_atomic_transaction.py:204`; AST `6ad37a609409bb15d24ee2032524603e13b9743e2428960ba3b8ccdd23a29313`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, root, state, target. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[5].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[5].value.func.value.args[1].elts[0]::Call

Source: `infra/tests/test_atomic_transaction.py:204`; AST `7b1c0658e87108bbd712eea71383032b974ed067d99ad890f3013a1505fa65a6`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, target. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[5].value.func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[6]::Assign

Source: `infra/tests/test_atomic_transaction.py:205`; AST `e4dd2aacba7c8c497397c80a23b792e02b3beac3d092b3c31be853b4824b0eaf`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal, state. Outputs/bindings: journal_path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[7]::Assign

Source: `infra/tests/test_atomic_transaction.py:206`; AST `3795a24b67f2cb64729ad16854bcabec39aa0dd5f676b43d55dff8a1ed52f7a6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal_path, json. Outputs/bindings: value.
Calls/effect boundaries: journal_path.read_text, json.loads.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[7].value::Call

Source: `infra/tests/test_atomic_transaction.py:206`; AST `7aa8b6b8dfde94dd031a68c49df73731c43ae7746b526a40598675b68961559f`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path, json. Outputs/bindings: (none).
Calls/effect boundaries: journal_path.read_text, json.loads.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[7].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:206`; AST `1201965971c265219ad2e691a60f02d9a8eab01ce00ae6d2b8538b12b05e8a3c`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path. Outputs/bindings: (none).
Calls/effect boundaries: journal_path.read_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[8]::Assign

Source: `infra/tests/test_atomic_transaction.py:207`; AST `49f149572068f194e46a76e9fae800fd0eb3632c563864299fc8fcb3382e89fc`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[9]::Expr

Source: `infra/tests/test_atomic_transaction.py:208`; AST `7b15468ad963843b6a9ecb7d78abafc16161834aca8ea215469c3ca207a71c89`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal_path, json, value. Outputs/bindings: (none).
Calls/effect boundaries: journal_path.write_text, json.dumps.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[9].value::Call

Source: `infra/tests/test_atomic_transaction.py:208`; AST `b25c3f3439663f1ac95aa3c83344af51cecb29b668700d902107934155de27cf`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path, json, value. Outputs/bindings: (none).
Calls/effect boundaries: journal_path.write_text, json.dumps.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[9].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:208`; AST `ccf75a3fee685fba92dbd87286589aeb7a31a140dc5ab06ed02ae7cde17c019e`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[9].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[10]::With

Source: `infra/tests/test_atomic_transaction.py:209`; AST `5d46471d2c05f9fad44b52074130a979612505e0e9259c41b0ba31a8739d0e76`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: TransactionError, journal_path, recover_transaction, root, self. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction, self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[4].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[10].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:209`; AST `eb682bbbfcf0d45c7f8989cf08f5bb008eafb36b497b7c2033f7364392c2b999`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[10].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[10].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:210`; AST `0f1bb91a1152ecc7620b7c34685486cd34ac1143e816e4cb515ed6bb698b2590`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal_path, recover_transaction, root. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[0].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[10].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:210`; AST `6a2ff4fa16da66aded5fa0f47033d317529a75e8effa448cee78642d996fea8a`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path, recover_transaction, root. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[11]::Expr

Source: `infra/tests/test_atomic_transaction.py:211`; AST `054828ffabd46c735597d9fc8c5382a0082fae43e72973c24c9fbb6567f34347`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[11].value::Call

Source: `infra/tests/test_atomic_transaction.py:211`; AST `9277a7efe86a17a1622e1e79d1e953593d90b2a0d93332d0ccff427c08880b81`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_rejects_rollback_bytes_not_bound_to_before_hash::root.body[13].body[4].body[0].body[11].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:211`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:213`; AST `98e7ec680dae4f1d483cea645042af07a1b018381dba81098865346895fa8591`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, Mutation, Path, TransactionError, first, journal, journal_path, recover_transaction, root, second, self, state, td, tempfile. Outputs/bindings: first, journal, journal_path, root, second, state, td.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(first, b'first-after'), Mutation(second, b'second-after')], state_dir=state, name='recovery-preflight').commit, Mutation, Path, first.read_bytes, first.write_bytes, recover_transaction, second.read_bytes, second.write_bytes, self.assertEqual, self.assertRaisesRegex, state.mkdir, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:214`; AST `f776b743a40f9d3a7c2a15ed7aabbd78959cb9a2e605b282bff49fde7cddb158`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileTransaction, Mutation, Path, TransactionError, first, journal, journal_path, recover_transaction, root, second, self, state, td, tempfile. Outputs/bindings: first, journal, journal_path, root, second, state, td.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(first, b'first-after'), Mutation(second, b'second-after')], state_dir=state, name='recovery-preflight').commit, Mutation, Path, first.read_bytes, first.write_bytes, recover_transaction, second.read_bytes, second.write_bytes, self.assertEqual, self.assertRaisesRegex, state.mkdir, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:214`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:215`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:215`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:216`; AST `d8d2ca266e8a736df1475b1804eb980f0e06be09e8dbfbe650c370fa6ac723a6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:217`; AST `69e04085199b093eaac5e2af509fe8518fefb21e6f6994c4f1e68977906a5214`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:217`; AST `28a147563ac722ec23c0f204d62f9d1ac3a56abc0b1c08c3bad3b91dff8f088b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[3]::Assign

Source: `infra/tests/test_atomic_transaction.py:218`; AST `3ef43db03c7f88d25539595df9a849b0facfda4796115654180692ace47e92cd`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: first.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[4]::Assign

Source: `infra/tests/test_atomic_transaction.py:219`; AST `5070179907b19889525331b4c11bc4d936cd0a843d0d7623ebebca208c91498e`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: second.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[5]::Expr

Source: `infra/tests/test_atomic_transaction.py:220`; AST `a0bde866181413f36c6ed04a1ccd23851f08a7b05794d61e4a5784661dd8183f`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[5].value::Call

Source: `infra/tests/test_atomic_transaction.py:220`; AST `8a9a30a47add8f7e32a3d13a89e3d7a38204c08f7b8e2941415694e978cf4622`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[6]::Expr

Source: `infra/tests/test_atomic_transaction.py:221`; AST `764f141a1c0b67b643adee5b67d6586d789e20be12123e132cf0b233a9cf2d49`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[6].value::Call

Source: `infra/tests/test_atomic_transaction.py:221`; AST `8222b78f577f8f094326a1be9702e159b43e36ab3a2fdfdb14eefab07e982d5b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[7]::Assign

Source: `infra/tests/test_atomic_transaction.py:222`; AST `6932df97e1ddb396db6090bd78dff7b7043eba070c98c0d17cde581e21dc5527`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, Mutation, first, root, second, state. Outputs/bindings: journal.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(first, b'first-after'), Mutation(second, b'second-after')], state_dir=state, name='recovery-preflight').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[7].value::Call

Source: `infra/tests/test_atomic_transaction.py:222`; AST `df4763a547f36dbb6b493e8cb8f485b48888c4fa7d23faf759c9d04a154fe527`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, first, root, second, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(first, b'first-after'), Mutation(second, b'second-after')], state_dir=state, name='recovery-preflight').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[7].value.func.value::Call

Source: `infra/tests/test_atomic_transaction.py:222`; AST `7506d92021206a18cb57c4cc7817fc12825afdd34c056072aa5e45c744bc40f1`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, first, root, second, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[7].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[7].value.func.value.args[1].elts[0]::Call

Source: `infra/tests/test_atomic_transaction.py:224`; AST `77bf1c593decf36dc93728948c8cb961857a18091f7010e8ea207e42c39f3d40`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, first. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[7].value.func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[7].value.func.value.args[1].elts[1]::Call

Source: `infra/tests/test_atomic_transaction.py:224`; AST `27a4350724b91c97363c68cea2f8b08489289261be6b9d82b42f3ed433cf7952`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, second. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[7].value.func.value.args[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[8]::Assign

Source: `infra/tests/test_atomic_transaction.py:228`; AST `e4dd2aacba7c8c497397c80a23b792e02b3beac3d092b3c31be853b4824b0eaf`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal, state. Outputs/bindings: journal_path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[9]::Expr

Source: `infra/tests/test_atomic_transaction.py:229`; AST `abc6668acc955b89246a145f12925a5ee6d9fb5b6da2b127084a038c9c27dd85`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[9].value::Call

Source: `infra/tests/test_atomic_transaction.py:229`; AST `3520b35d6ddbbbc8c2ae06c6b414523623dcf34b75dde870fb1655800c7d51bb`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[10]::With

Source: `infra/tests/test_atomic_transaction.py:231`; AST `3dd62a05aa8b220e878cf1a7b3cd4c84f4774e0cfa94678c55344b8d24cf27e4`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: TransactionError, journal_path, recover_transaction, root, self. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction, self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[5].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[10].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:231`; AST `23b4da156817f17b5771991ceb4d5ea9be0df6a9db5ef2dac374ebdc4abeb5aa`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[10].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[10].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:232`; AST `0f1bb91a1152ecc7620b7c34685486cd34ac1143e816e4cb515ed6bb698b2590`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal_path, recover_transaction, root. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[10].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:232`; AST `6a2ff4fa16da66aded5fa0f47033d317529a75e8effa448cee78642d996fea8a`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path, recover_transaction, root. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[11]::Expr

Source: `infra/tests/test_atomic_transaction.py:234`; AST `055633d77252bcad5856e3ed9681052ae5e27130a820cbd04054560aeac29f93`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: first.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[11].value::Call

Source: `infra/tests/test_atomic_transaction.py:234`; AST `7b66ac92c0e2986743ddb32eae7ef522ae8a2fd10a2fb50dd73fdec6144390aa`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: first.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[11].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:234`; AST `3f60cea7167c40fc7e8de55d1da9a6a5268348c51f9de64a7acfe9cdcd46a6aa`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[12]::Expr

Source: `infra/tests/test_atomic_transaction.py:235`; AST `7ea42512306cb839de839003008a7f293320993cacf925363c8e8672616b98fe`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: second.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[12].value::Call

Source: `infra/tests/test_atomic_transaction.py:235`; AST `392010d79e5ba8f84647a4e0f25a04943e58425c973a557714034f91f238894b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: second.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_recovery_preflights_every_destination_before_rollback::root.body[13].body[5].body[0].body[12].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:235`; AST `a969361b88e4bef27234abc44d61c4c159d586c7b4a79663a7d197ae29639f53`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:237`; AST `eee71a3e4d1d565bc1fa16c5f6924808d3c1f1448630c80d677c830812de5246`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, Mutation, Path, TransactionError, first, first_journal, first_path, json, path, recover_named_transactions, root, second, second_journal, second_path, self, state, td, tempfile, value. Outputs/bindings: first, first_journal, first_path, path, root, second, second_journal, second_path, state, td, value.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(first, b'first-after')], state_dir=state, name='a-install').commit, FileTransaction(root, [Mutation(second, b'second-after')], state_dir=state, name='b-uninstall').commit, Mutation, Path, first.read_bytes, first.write_bytes, first_path.read_text, json.dumps, json.loads, path.read_text, path.write_text, recover_named_transactions, second.read_bytes, second.write_bytes, second_path.read_text, self.assertEqual, self.assertRaisesRegex, state.mkdir, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:238`; AST `44ae4130dd033f24860f07c57a1864bedc63f6c0ec1a77383ab25dc0ab8aed61`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileTransaction, Mutation, Path, TransactionError, first, first_journal, first_path, json, path, recover_named_transactions, root, second, second_journal, second_path, self, state, td, tempfile, value. Outputs/bindings: first, first_journal, first_path, path, root, second, second_journal, second_path, state, td, value.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(first, b'first-after')], state_dir=state, name='a-install').commit, FileTransaction(root, [Mutation(second, b'second-after')], state_dir=state, name='b-uninstall').commit, Mutation, Path, first.read_bytes, first.write_bytes, first_path.read_text, json.dumps, json.loads, path.read_text, path.write_text, recover_named_transactions, second.read_bytes, second.write_bytes, second_path.read_text, self.assertEqual, self.assertRaisesRegex, state.mkdir, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:238`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:239`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:239`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:240`; AST `d8d2ca266e8a736df1475b1804eb980f0e06be09e8dbfbe650c370fa6ac723a6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:241`; AST `69e04085199b093eaac5e2af509fe8518fefb21e6f6994c4f1e68977906a5214`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:241`; AST `28a147563ac722ec23c0f204d62f9d1ac3a56abc0b1c08c3bad3b91dff8f088b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.mkdir.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[3]::Assign

Source: `infra/tests/test_atomic_transaction.py:242`; AST `3ef43db03c7f88d25539595df9a849b0facfda4796115654180692ace47e92cd`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: first.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[4]::Assign

Source: `infra/tests/test_atomic_transaction.py:243`; AST `5070179907b19889525331b4c11bc4d936cd0a843d0d7623ebebca208c91498e`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: second.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[5]::Expr

Source: `infra/tests/test_atomic_transaction.py:244`; AST `a0bde866181413f36c6ed04a1ccd23851f08a7b05794d61e4a5784661dd8183f`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[5].value::Call

Source: `infra/tests/test_atomic_transaction.py:244`; AST `8a9a30a47add8f7e32a3d13a89e3d7a38204c08f7b8e2941415694e978cf4622`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[6]::Expr

Source: `infra/tests/test_atomic_transaction.py:245`; AST `764f141a1c0b67b643adee5b67d6586d789e20be12123e132cf0b233a9cf2d49`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[6].value::Call

Source: `infra/tests/test_atomic_transaction.py:245`; AST `8222b78f577f8f094326a1be9702e159b43e36ab3a2fdfdb14eefab07e982d5b`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[7]::Assign

Source: `infra/tests/test_atomic_transaction.py:246`; AST `3a0f9c9fa491329c976baca130eb513dd872accf6bd295d7679806287b0bfa88`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, Mutation, first, root, state. Outputs/bindings: first_journal.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(first, b'first-after')], state_dir=state, name='a-install').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[7].value::Call

Source: `infra/tests/test_atomic_transaction.py:246`; AST `f80037140c770a0fdb896d82ba4fd2d0edd0dbb443d9eb7b2ecd88683e242ae5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, first, root, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(first, b'first-after')], state_dir=state, name='a-install').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[7].value.func.value::Call

Source: `infra/tests/test_atomic_transaction.py:246`; AST `3656982e1110e9dc8a9995e73bc17174215cf5e8194425058300cb74832604d6`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, first, root, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[7].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[7].value.func.value.args[1].elts[0]::Call

Source: `infra/tests/test_atomic_transaction.py:248`; AST `77bf1c593decf36dc93728948c8cb961857a18091f7010e8ea207e42c39f3d40`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, first. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[7].value.func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[8]::Assign

Source: `infra/tests/test_atomic_transaction.py:252`; AST `75fd9c17cb403d03815efe5ae8f8a5bf036a238062496663c1dc63c5a95c9fff`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, Mutation, root, second, state. Outputs/bindings: second_journal.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(second, b'second-after')], state_dir=state, name='b-uninstall').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[8].value::Call

Source: `infra/tests/test_atomic_transaction.py:252`; AST `0c717b2e4ce48b883f68e2e7642163a197af28816ab53b7a86b27be77a2b5fea`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, root, second, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(second, b'second-after')], state_dir=state, name='b-uninstall').commit, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[8].value.func.value::Call

Source: `infra/tests/test_atomic_transaction.py:252`; AST `c86c0b283186ae53d32dfd636cb1177894eb79154a615b015c34f3e6335a7f95`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, root, second, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[8].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[8].value.func.value.args[1].elts[0]::Call

Source: `infra/tests/test_atomic_transaction.py:254`; AST `27a4350724b91c97363c68cea2f8b08489289261be6b9d82b42f3ed433cf7952`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, second. Outputs/bindings: (none).
Calls/effect boundaries: Mutation.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[8].value.func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[9]::Assign

Source: `infra/tests/test_atomic_transaction.py:258`; AST `51c33df93f6e4afbecbdfc9da4b454bb7ed726ee211b47ef3c9e6b617ca6f2da`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first_journal, state. Outputs/bindings: first_path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[10]::Assign

Source: `infra/tests/test_atomic_transaction.py:259`; AST `e9997fa255f07f872d9b3363f770a3ff62fd3ac30b6ed5501bbec98dc0604662`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second_journal, state. Outputs/bindings: second_path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[11]::For

Source: `infra/tests/test_atomic_transaction.py:260`; AST `ce32e74ab4701fa9a29b398aa9faafc5ae1774ea7de6b996d1220fa004dbd12d`.

Rust module: `infra::tests::test_atomic_transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: first_path, json, path, second_path, value. Outputs/bindings: path, value.
Calls/effect boundaries: json.dumps, json.loads, path.read_text, path.write_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered For evaluation at root.body[13].body[6].body[0].body[11]; no call, error or mutation may be omitted. Iteration: path in (first_path, second_path)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[11].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:261`; AST `15567424f006294b54611720ab067f3a35becac5c893a7ecfce3d394a279dc72`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path. Outputs/bindings: value.
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[11].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:261`; AST `78de6374442893c897b38631d9e0e792a86e0399b2b9cf016c0c8cb503df6d07`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[11].body[0].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:261`; AST `d7d2b1d3f5b3313cd24906b00f77863075a83ccc502a11ff12b073fd43d10854`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[11].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[11].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:262`; AST `14d0c93108c9be6eb0275929dca6775e0b53cb3a9fb008828fb376310a86a1b8`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[11].body[2]::Expr

Source: `infra/tests/test_atomic_transaction.py:263`; AST `c1c0ea579d683338117a7ce8a60cab8f15fc04a2c068263f98815d0ce58d3081`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[11].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:263`; AST `7773f527b974d96239d75e6365a332db12b75e409f033d4e0f197b44c5fa732d`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[11].body[2].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:263`; AST `ccf75a3fee685fba92dbd87286589aeb7a31a140dc5ab06ed02ae7cde17c019e`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[11].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[12]::Expr

Source: `infra/tests/test_atomic_transaction.py:264`; AST `9f69b6e7e62fba613b566274caf5b949d068d60d3f3080de90ab375f54a445f6`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[12].value::Call

Source: `infra/tests/test_atomic_transaction.py:264`; AST `58156cdd00c5ae5ef37b1ff982337f5bf58603c4546834995ac9bd157b0689c6`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.write_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[13]::With

Source: `infra/tests/test_atomic_transaction.py:266`; AST `824e8e711c1c80300e41a61f50d622ea513e5ffb4e53689c6be1fc65bbc539a2`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: TransactionError, recover_named_transactions, root, self, state. Outputs/bindings: (none).
Calls/effect boundaries: recover_named_transactions, self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[6].body[0].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[13].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:266`; AST `23b4da156817f17b5771991ceb4d5ea9be0df6a9db5ef2dac374ebdc4abeb5aa`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[13].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[13].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:267`; AST `654003b6733d1b5cdd73fc3f257f2983e1d90a7e9add2a58f9cc8d3ddf8927f2`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recover_named_transactions, root, state. Outputs/bindings: (none).
Calls/effect boundaries: recover_named_transactions.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[13].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:267`; AST `4ca21b76c2ad342146c5e1e35143d9a90d8428500dfcb7e8b0394e5c67b020d8`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recover_named_transactions, root, state. Outputs/bindings: (none).
Calls/effect boundaries: recover_named_transactions.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[14]::Expr

Source: `infra/tests/test_atomic_transaction.py:273`; AST `6009ba90b36f0e6d63053eb04d9b3fadd935a1a848e87b0350a3184ef4185866`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: first.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[14].value::Call

Source: `infra/tests/test_atomic_transaction.py:273`; AST `2cfd4e0e4c26ff4d35e66fef92e593369b7f9409ddd09351626b2224ebd423fd`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: first.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[14].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:273`; AST `3f60cea7167c40fc7e8de55d1da9a6a5268348c51f9de64a7acfe9cdcd46a6aa`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[14].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[15]::Expr

Source: `infra/tests/test_atomic_transaction.py:274`; AST `a0287fc4347e4a088086e07cb87934b4143956e5b73fcd0ed0e9572c272738f9`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: second.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[15].value::Call

Source: `infra/tests/test_atomic_transaction.py:274`; AST `9d4789e835c2d0540de9552c3afbf85213edcbc99eb47b0cf35f43b57a0dfa20`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: second.read_bytes, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[15].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:274`; AST `a969361b88e4bef27234abc44d61c4c159d586c7b4a79663a7d197ae29639f53`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second.read_bytes.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[15].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[16]::Expr

Source: `infra/tests/test_atomic_transaction.py:275`; AST `5bb72d79cf7273992d2261de5609612123dd0b1ccd9c54e8a974e4bfd781b443`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first_path, json, self. Outputs/bindings: (none).
Calls/effect boundaries: first_path.read_text, json.loads, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[16].value::Call

Source: `infra/tests/test_atomic_transaction.py:275`; AST `de5713df212b5c74d8e9d82ffc3d14dc24a62621afd2854e357bc814127adeb8`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first_path, json, self. Outputs/bindings: (none).
Calls/effect boundaries: first_path.read_text, json.loads, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[16].value.args[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:275`; AST `f7f3d150184c364b2f59a562ed29c9c97bc67b466f6ec3379c96156f4e97a435`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first_path, json. Outputs/bindings: (none).
Calls/effect boundaries: first_path.read_text, json.loads.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[16].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[16].value.args[0].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:275`; AST `c932ae936017a9f00fe4695ce363eba464f9bd4b5bbf82181917f986a0d85819`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first_path. Outputs/bindings: (none).
Calls/effect boundaries: first_path.read_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[16].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[17]::Expr

Source: `infra/tests/test_atomic_transaction.py:276`; AST `8c6258315ff118eeac8780050ac76b3a558cb6bc5930fb286a4a032dd6198108`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, second_path, self. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, second_path.read_text, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6].body[0].body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[17].value::Call

Source: `infra/tests/test_atomic_transaction.py:276`; AST `bfe6fc943bc8f92f4be41fb412b86a09c82e166531df35507364390b92805b08`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, second_path, self. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, second_path.read_text, self.assertEqual.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[17].value.args[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:276`; AST `78716f4b64849b83670774ee2ebfd540a4e023cfdac20397486016dcc8882a22`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, second_path. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, second_path.read_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[17].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_named_recovery_preflights_every_journal_before_any_rollback::root.body[13].body[6].body[0].body[17].value.args[0].value.args[0]::Call

Source: `infra/tests/test_atomic_transaction.py:276`; AST `e58e3f03b5cb57d5b4f170383a707d7f9aa364f3dab63e1cb63a7061c72b3916`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second_path. Outputs/bindings: (none).
Calls/effect boundaries: second_path.read_text.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[0].body[17].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7]::FunctionDef

Source: `infra/tests/test_atomic_transaction.py:278`; AST `901c68bde57f59e0b74f405c7bd963c217edc8f75c6ecb73c67ed9cd025649a5`.

Rust module: `infra::tests::test_atomic_transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, LockError, Path, first, owner, path, self, td, tempfile. Outputs/bindings: first, owner, path, td.
Calls/effect boundaries: FileLock, FileLock(path, 'second').release, Path, first.acquire, first.release, self.assertRaises, self.assertRegex, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0]::With

Source: `infra/tests/test_atomic_transaction.py:279`; AST `fe13a236e6ef7f47cf4846de2dabb674a8d491a71f29a156e46bc111792bd063`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileLock, LockError, Path, first, owner, path, self, td, tempfile. Outputs/bindings: first, owner, path, td.
Calls/effect boundaries: FileLock, FileLock(path, 'second').release, Path, first.acquire, first.release, self.assertRaises, self.assertRegex, tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:279`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[0]::Assign

Source: `infra/tests/test_atomic_transaction.py:280`; AST `06d51adad9f9977c8494852fc90278dcb5382fc3ee569813d761d7c6f4e67065`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: path.
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[0].value.left::Call

Source: `infra/tests/test_atomic_transaction.py:280`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[1]::Assign

Source: `infra/tests/test_atomic_transaction.py:281`; AST `38c5b07864d516ca1bdb3a95d8b613d995addedd99c4600e4399f77fcab58bbf`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, path. Outputs/bindings: first.
Calls/effect boundaries: FileLock.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[7].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[1].value::Call

Source: `infra/tests/test_atomic_transaction.py:281`; AST `ad71097662e0bba602ae933d2db23aa3b3c1fe15413d51524adc277ce7516727`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, path. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[2]::Assign

Source: `infra/tests/test_atomic_transaction.py:282`; AST `22ccfbc4d431b1fe1f8803bcac6a4dcbc538af7c19c249d532100925cd35ef41`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first. Outputs/bindings: owner.
Calls/effect boundaries: first.acquire.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[7].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[2].value::Call

Source: `infra/tests/test_atomic_transaction.py:282`; AST `162a86cc0d7c30996dff233856bfaac8dfb79a0fcc5212a41a4924bcd20e19af`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.acquire.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[3]::Expr

Source: `infra/tests/test_atomic_transaction.py:283`; AST `858a98622dc7356b5cce308dc7af44076bf3785991abb1173b4cf3706ec35f65`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[3].value::Call

Source: `infra/tests/test_atomic_transaction.py:283`; AST `07285a6a48bfa488c4a34abc3907c5b447dfa145601598097486f52fbd69c2bd`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRegex.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[4]::With

Source: `infra/tests/test_atomic_transaction.py:284`; AST `e9b9b4482e81fbdcf94d7a89dca1406cdf62e9c48cb7d521ca54644781910852`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileLock, LockError, owner, path, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, FileLock(path, 'second').release, self.assertRaises.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[7].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[4].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:284`; AST `26cbcad8e1105b09f68f62b372acd98e18b49c0ec6ef47b865867087935ab1fb`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[4].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:285`; AST `99d8a90b8d5f34bd215471440f9eda0b7cb1aafa030949c7560072f973f19a81`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, owner, path. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, FileLock(path, 'second').release.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7].body[0].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[4].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:285`; AST `149ea4992cfc4127751798c1f21cc90c6c8cdd95f7d02514823df5262f4e3eed`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, owner, path. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, FileLock(path, 'second').release.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[4].body[0].value.func.value::Call

Source: `infra/tests/test_atomic_transaction.py:285`; AST `84f005b3fa78f1ea99ff88a9954b087f353f31ac8a8077ae69c60636818f42f3`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, path. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[4].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[5]::With

Source: `infra/tests/test_atomic_transaction.py:286`; AST `48bf517c3d7aa401dfe8347bbd88c47e74300f1253ebd7d329a4604e08a61da0`.

Rust module: `infra::tests::test_atomic_transaction`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: LockError, first, self. Outputs/bindings: (none).
Calls/effect boundaries: first.release, self.assertRaises.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered With evaluation at root.body[13].body[7].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[5].items[0].context_expr::Call

Source: `infra/tests/test_atomic_transaction.py:286`; AST `26cbcad8e1105b09f68f62b372acd98e18b49c0ec6ef47b865867087935ab1fb`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[5].body[0]::Expr

Source: `infra/tests/test_atomic_transaction.py:287`; AST `ec09888abe1fdb0f91570072a13eb4f4a41e13535c96f4a28436e92f093d9aca`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.release.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7].body[0].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[5].body[0].value::Call

Source: `infra/tests/test_atomic_transaction.py:287`; AST `2ce0300cb5aa81ba742c13ba2549f0e6f6216f24df9a662115035f0c3a89f619`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.release.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[6]::Expr

Source: `infra/tests/test_atomic_transaction.py:288`; AST `407ba4f0a57ab63a52e6decb109319e3e6e84ede01c25d21e53347173b2a2350`.

Rust module: `infra::tests::test_atomic_transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, owner. Outputs/bindings: (none).
Calls/effect boundaries: first.release.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_atomic_transaction.py::module::TestFileTransaction::test_transaction_lock_has_unique_owner_nonce_not_pid_only::root.body[13].body[7].body[0].body[6].value::Call

Source: `infra/tests/test_atomic_transaction.py:288`; AST `13a2b77c00736b6a0c695ecea922ed176a5a7c6117946673f81cf4ea14d48dda`.

Rust module: `infra::tests::test_atomic_transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, owner. Outputs/bindings: (none).
Calls/effect boundaries: first.release.
Dependencies: agentinfra.atomic, agentinfra.locks, agentinfra.transaction, json, os, pathlib, stat, sys, tempfile, threading, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::sync plus OS file locks
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
