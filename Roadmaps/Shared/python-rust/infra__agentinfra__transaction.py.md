# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 453. Inventory digest: `d058170a23a7b96d4bf2b713f9f41d15be7710d01f90b992055ebe93b1b1bc38`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/transaction.py::module::root::Module

Source: `infra/agentinfra/transaction.py:1`; AST `5de95ee59ae43a6ec3e86174501e7703cc5c719e30759b7712cca3bafe59b510`.

Rust module: `infra::agentinfra::transaction`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BaseException, Callable, Exception, FaultHook, FileLock, GovernanceViolation, Iterable, Mutation, OSError, Path, RuntimeError, TransactionError, TypeError, ValueError, _RecoveryPlan, _apply_recovery, _fault, _now, _preflight_recovery_batch, _prepare_recovery, _read, _read_recovery_journal, _recover_candidates, _sha, _valid_sha256, acquired, after_hash, any, assert_mutation_allowed, atomic_write_bytes, atomic_write_json, base64, before, before_hash, bool, bytes, candidates, confined_path, data, dataclass, datetime, decoded_before, destinations, dict, directory, durable_unlink, encoded, enumerate, exc, expected_hashes, expected_root, fault, force_rollback, frozenset, hashlib, hook, index, int, isinstance, item, journal, journal_path, journal_root, json, len, list, lock, locks, mode, mutation, mutations, name, names, object, original, path, phase, plan, plans, preview, prior, record, records, recover_pending_transactions, recover_transaction, recovered, rel, relative, remove_recovered, retain, reversed, rollback, root, seen, selected, self, set, sorted, stage, stat, state_dir, str, timezone, tuple, tx_dir, txid, uuid, validated_paths, value, zip. Outputs/bindings: FaultHook, _, acquired, after_hash, before, before_hash, candidates, data, decoded_before, destinations, directory, encoded, expected_exists, expected_hashes, expected_sha256, index, journal, journal_path, journal_root, lock, locks, mode, mutation, name, path, paths, phase, plan, plans, preview, prior, record, records, recovered, rel, relative, rollback, root, seen, selected, state_dir, tx_dir, txid, validated_paths.
Calls/effect boundaries: (tx_dir / 'journal.json').exists, (tx_dir / 'journal.json').unlink, FileLock, Path, Path(journal_root).resolve, TransactionError, ValueError, _RecoveryPlan, _apply_recovery, _fault, _now, _preflight_recovery_batch, _prepare_recovery, _read, _read_recovery_journal, _recover_candidates, _sha, _valid_sha256, acquired.append, any, assert_mutation_allowed, atomic_write_bytes, atomic_write_json, base64.b64decode, base64.b64encode, base64.b64encode(before).decode, candidates.append, confined_path, dataclass, datetime.now, datetime.now(timezone.utc).isoformat, destinations.get, dict.fromkeys, directory.is_dir, directory.is_symlink, directory.iterdir, directory.rmdir, durable_unlink, enumerate, expected_root.resolve, frozenset, hashlib.sha256, hashlib.sha256(data).hexdigest, hook, int, isinstance, journal.get, journal_path.is_file, journal_path.is_symlink, journal_path.read_text, json.dumps, json.loads, len, list, lock.acquire, lock.release, name.strip, path.exists, path.read_bytes, path.relative_to, path.relative_to(self.root).as_posix, path.stat, plan.paths.items, preview.get, record.get, records.append, recover_pending_transactions, recover_transaction, reversed, root.resolve, seen.add, self._preflight, self.state_dir.mkdir, set, sorted, stat.S_IMODE, state_dir.exists, state_dir.iterdir, str, tx_dir.exists, tx_dir.iterdir, tx_dir.mkdir, tx_dir.rmdir, uuid.uuid4, value.lower, zip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[0]::ImportFrom

Source: `infra/agentinfra/transaction.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/transaction.py:3`; AST `321ed2ed3afceb74be547c9905ed4c676e453b1a68fe7cb2d3e214caeac2624d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/transaction.py:4`; AST `85598e37ba96d6e396880fbaf8f1a487d6502e6df91ce2ca25c05c876437624e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[3]::Import

Source: `infra/agentinfra/transaction.py:5`; AST `99ccd02cb758ed604ff1bc1c067c06e1543524012de4421d7b80e9b7ad7717e7`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[4]::Import

Source: `infra/agentinfra/transaction.py:6`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[5]::Import

Source: `infra/agentinfra/transaction.py:7`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[6]::Import

Source: `infra/agentinfra/transaction.py:8`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[7]::Import

Source: `infra/agentinfra/transaction.py:9`; AST `c22b5a111acc3bea9e5136e41e207f1f95083e90d861516ce34d682526721c86`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[8]::Import

Source: `infra/agentinfra/transaction.py:10`; AST `db14cae1a81ee06a1930fa9f46771b454957916d2bbbc048661adf0613fd70de`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/transaction.py:11`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[10]::ImportFrom

Source: `infra/agentinfra/transaction.py:12`; AST `1a590219234186f174f3d3a6220a3eec68409774deca31bc42610714e4013e20`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[11]::ImportFrom

Source: `infra/agentinfra/transaction.py:14`; AST `8858067ade776d79ec42ffe75ebf47e28f03d0fd63b23ad466b0e8a93c7b05fe`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[12]::ImportFrom

Source: `infra/agentinfra/transaction.py:15`; AST `f49eec2be7586a81b0fa34570d7cbaa58bc5eeaa5e471a05fac611f36b0ee7bd`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[13]::ImportFrom

Source: `infra/agentinfra/transaction.py:16`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[14]::ImportFrom

Source: `infra/agentinfra/transaction.py:17`; AST `eb4944c2e741a4a8bcb152b70a25f0d1c5edb1f4f8545b1913283e03370a4605`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::TransactionError::root.body[15]::ClassDef

Source: `infra/agentinfra/transaction.py:20`; AST `d45b4b867ac1558a3ec798e7129552c907877d150ad3db4a2d2a7b4994d0ffe9`.

Rust module: `infra::agentinfra::transaction`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::TransactionError::root.body[15].body[0]::Pass

Source: `infra/agentinfra/transaction.py:21`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Pass evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::root.body[16]::Assign

Source: `infra/agentinfra/transaction.py:24`; AST `8ff56bc2e404072e809340e61b14665fdd92edca6a7b9a493ebc6fb15d0d321a`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Callable, dict, str. Outputs/bindings: FaultHook.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_now::root.body[17]::FunctionDef

Source: `infra/agentinfra/transaction.py:27`; AST `2002d96b29ea73dbaa36fb15a8de921b2b207655e9f6844445bc2640cc932d35`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: datetime, str, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now, datetime.now(timezone.utc).isoformat.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_now::root.body[17].body[0]::Return

Source: `infra/agentinfra/transaction.py:28`; AST `04d97f7b2f56105a8dee137484e2a607e200f29f786ca622301e010f18cb21c8`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now, datetime.now(timezone.utc).isoformat.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_now::root.body[17].body[0].value::Call

Source: `infra/agentinfra/transaction.py:28`; AST `1b110a252c57d72f572683a982afb6160b9f4ceeec701cae738dc9a58366722d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now, datetime.now(timezone.utc).isoformat.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_now::root.body[17].body[0].value.func.value::Call

Source: `infra/agentinfra/transaction.py:28`; AST `7d005ec5c408397d72b2a5196d97d2fa96db0d64d31cc38e5bd68f36bf7badb9`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_sha::root.body[18]::FunctionDef

Source: `infra/agentinfra/transaction.py:31`; AST `0d9066ebde2e5a3e3398d430fe2a282f17c7378c1b85aeb103ba7c21f0bcafc2`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bytes, data, hashlib, str. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_sha::root.body[18].body[0]::Return

Source: `infra/agentinfra/transaction.py:32`; AST `c138b6f9648f397ad1c379891a845efde1767ef55790b4cc4fadaf51c385b5da`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_sha::root.body[18].body[0].value.body::Call

Source: `infra/agentinfra/transaction.py:32`; AST `ec988457fe103b959d993a11b804009071d8c43f7cb3ec64f12df05099c74d63`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_sha::root.body[18].body[0].value.body.func.value::Call

Source: `infra/agentinfra/transaction.py:32`; AST `08f31cedb8064eb17f9167928d61fe53346b78450a1fe6d6c7076f027285d627`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value.body.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::Mutation::root.body[19]::ClassDef

Source: `infra/agentinfra/transaction.py:36`; AST `91d233431f6f487046c5a1093a5981de1ea567e262e57d823d070c8396926507`.

Rust module: `infra::agentinfra::transaction`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Path, bool, bytes, dataclass, int, str. Outputs/bindings: data, expected_exists, expected_sha256, mode, path.
Calls/effect boundaries: dataclass.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::Mutation::root.body[19].body[0]::AnnAssign

Source: `infra/agentinfra/transaction.py:37`; AST `d3875b770eedb512c54cfa40a07917c19082ab47a2d6364a83103c2dc978d73b`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::Mutation::root.body[19].body[1]::AnnAssign

Source: `infra/agentinfra/transaction.py:38`; AST `95183e17f3576efe9f1e2c02e919f1bdda416618849d03208cca4c52ad8668ff`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bytes. Outputs/bindings: data.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::Mutation::root.body[19].body[2]::AnnAssign

Source: `infra/agentinfra/transaction.py:39`; AST `0f605ba7fbed35a5b37faad107857c0286f44cebc11df5e76cf611839dc1fffd`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: expected_sha256.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::Mutation::root.body[19].body[3]::AnnAssign

Source: `infra/agentinfra/transaction.py:40`; AST `0096439fe56eed23d223206996771b9c9d23d3c96568d4c509f6863e38bdb4e7`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool. Outputs/bindings: expected_exists.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[19].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::Mutation::root.body[19].body[4]::AnnAssign

Source: `infra/agentinfra/transaction.py:41`; AST `b3ae3014ee23d899c93f89056bdbd0eecef1a8d045ed70b16b99d04e29d1ea7d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int. Outputs/bindings: mode.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[19].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::Mutation::root.body[19].decorator_list[0]::Call

Source: `infra/agentinfra/transaction.py:35`; AST `fc70015bf40dfb1bdf9c74c7ec3567232b79ad9aa1cd1edc6c02254994330803`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dataclass. Outputs/bindings: (none).
Calls/effect boundaries: dataclass.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[19].decorator_list[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_RecoveryPlan::root.body[20]::ClassDef

Source: `infra/agentinfra/transaction.py:45`; AST `12f48f26225b935839dee881ef0a13e310d4dd5d673581ce6606a1a7d9432469`.

Rust module: `infra::agentinfra::transaction`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Path, bool, bytes, dataclass, dict, frozenset, str. Outputs/bindings: before, expected_hashes, journal, journal_path, paths, rollback.
Calls/effect boundaries: dataclass.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_RecoveryPlan::root.body[20].body[0]::AnnAssign

Source: `infra/agentinfra/transaction.py:46`; AST `ecf6b18c91dd4592ecde232bef4f1681da83f16f8be4f70286ad01923acfb2e9`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: journal_path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_RecoveryPlan::root.body[20].body[1]::AnnAssign

Source: `infra/agentinfra/transaction.py:47`; AST `3d02f9e6cfef00776a2cb81e1deade7e6c6d3aa6c7b005f571662f53e77d493f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict. Outputs/bindings: journal.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[20].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_RecoveryPlan::root.body[20].body[2]::AnnAssign

Source: `infra/agentinfra/transaction.py:48`; AST `38153b1132843ed0c34bb6b9dfa73f90daa41ddd258bf965b5d8ee45c4c91edd`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool. Outputs/bindings: rollback.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[20].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_RecoveryPlan::root.body[20].body[3]::AnnAssign

Source: `infra/agentinfra/transaction.py:49`; AST `baef5cb1de39104e74c0ce9f0ead9e930b255cc4c4b1ef69a8e8f5b284e09d6f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, dict, str. Outputs/bindings: paths.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[20].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_RecoveryPlan::root.body[20].body[4]::AnnAssign

Source: `infra/agentinfra/transaction.py:50`; AST `8882e4865aec3f27e445ffeaee243beb824d29b34570b294105e222fbc0defc5`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bytes, dict, str. Outputs/bindings: before.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[20].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_RecoveryPlan::root.body[20].body[5]::AnnAssign

Source: `infra/agentinfra/transaction.py:51`; AST `9ee7f2b554b6a9fc672a2bfb470ae7c5e565ad2c0a6fda710fa2aa64ef41fe7b`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, frozenset, str. Outputs/bindings: expected_hashes.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[20].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_RecoveryPlan::root.body[20].decorator_list[0]::Call

Source: `infra/agentinfra/transaction.py:44`; AST `fc70015bf40dfb1bdf9c74c7ec3567232b79ad9aa1cd1edc6c02254994330803`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dataclass. Outputs/bindings: (none).
Calls/effect boundaries: dataclass.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[20].decorator_list[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read::root.body[21]::FunctionDef

Source: `infra/agentinfra/transaction.py:54`; AST `872cc264e87a677928f71f966fdf3b39143f5645fdc9e1031d781ab120c7132e`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, bytes, path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists, path.read_bytes.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read::root.body[21].body[0]::Return

Source: `infra/agentinfra/transaction.py:55`; AST `2d42eba112592148d7d29988bffd38ee4e6e5f2c1b92c1f5115026a9ae6b13bb`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists, path.read_bytes.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read::root.body[21].body[0].value.test::Call

Source: `infra/agentinfra/transaction.py:55`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[21].body[0].value.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read::root.body[21].body[0].value.body::Call

Source: `infra/agentinfra/transaction.py:55`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[21].body[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_fault::root.body[22]::FunctionDef

Source: `infra/agentinfra/transaction.py:58`; AST `984127271414587e2e0f912cff1f29289a9c6a08f357dd7bba6de69fd0501526`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FaultHook, dict, hook, journal, json, stage, str. Outputs/bindings: (none).
Calls/effect boundaries: hook, json.dumps, json.loads.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[22]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_fault::root.body[22].body[0]::If

Source: `infra/agentinfra/transaction.py:59`; AST `2431101421e28214a7ffb0d31b3a578ed25005a059fde8a3a2fe49768cbae1dd`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: hook, journal, json, stage. Outputs/bindings: (none).
Calls/effect boundaries: hook, json.dumps, json.loads.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[22].body[0]; no call, error or mutation may be omitted. Condition: hook is not None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_fault::root.body[22].body[0].body[0]::Expr

Source: `infra/agentinfra/transaction.py:60`; AST `8e4e986a8091d9e651d42634b3bdc9fafcf81233c3b38f9c22ed3b02effd192c`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hook, journal, json, stage. Outputs/bindings: (none).
Calls/effect boundaries: hook, json.dumps, json.loads.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_fault::root.body[22].body[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:60`; AST `8b4debae55853b84ec5f03eeec976a2361ad70bb16708f6df72a3f3e9703441e`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hook, journal, json, stage. Outputs/bindings: (none).
Calls/effect boundaries: hook, json.dumps, json.loads.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_fault::root.body[22].body[0].body[0].value.args[1]::Call

Source: `infra/agentinfra/transaction.py:60`; AST `aea964ec1fc8bd98e105ff24266467d708f62f06527bb499c404ef9e43a81bbc`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, json.loads.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[0].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_fault::root.body[22].body[0].body[0].value.args[1].args[0]::Call

Source: `infra/agentinfra/transaction.py:60`; AST `4cac3e93d51629f81c8b3bf10d321778464d9ade72a70e3567de30297c3c4a19`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[0].body[0].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::root.body[23]::ClassDef

Source: `infra/agentinfra/transaction.py:63`; AST `8c9cfc68470b29b8a1ca283297b87b036b9b9aac9044dd09208c22c0c6580845`.

Rust module: `infra::agentinfra::transaction`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: BaseException, Exception, FaultHook, FileLock, GovernanceViolation, Iterable, Mutation, Path, TransactionError, ValueError, _fault, _now, _read, _sha, any, assert_mutation_allowed, atomic_write_bytes, atomic_write_json, base64, before, before_hash, bool, confined_path, dict, durable_unlink, enumerate, exc, fault, index, journal, journal_path, list, lock, mode, mutation, mutations, name, original, path, record, records, recover_pending_transactions, recover_transaction, rel, retain, rollback, root, seen, self, set, stat, state_dir, str, tuple, tx_dir, txid, uuid, zip. Outputs/bindings: before, before_hash, index, journal, journal_path, lock, mode, mutation, path, record, records, rel, seen, tx_dir, txid.
Calls/effect boundaries: (tx_dir / 'journal.json').exists, (tx_dir / 'journal.json').unlink, FileLock, TransactionError, ValueError, _fault, _now, _read, _sha, any, assert_mutation_allowed, atomic_write_bytes, atomic_write_json, base64.b64encode, base64.b64encode(before).decode, confined_path, durable_unlink, enumerate, list, lock.acquire, lock.release, path.exists, path.relative_to, path.relative_to(self.root).as_posix, path.stat, records.append, recover_pending_transactions, recover_transaction, root.resolve, seen.add, self._preflight, self.state_dir.mkdir, set, stat.S_IMODE, str, tx_dir.exists, tx_dir.iterdir, tx_dir.mkdir, tx_dir.rmdir, uuid.uuid4, zip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[23]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::root.body[23].body[0]::Expr

Source: `infra/agentinfra/transaction.py:64`; AST `4b73a59f69427d53ac98ddc1f1ce74f519187052ed3103bc1170e66b3ffc555d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1]::FunctionDef

Source: `infra/agentinfra/transaction.py:70`; AST `6aa5fa2006540076886fee02af4468fa51bb3da4366fea3e459698362e6d2e80`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FaultHook, GovernanceViolation, Iterable, Mutation, Path, TransactionError, ValueError, assert_mutation_allowed, confined_path, exc, fault, list, mutations, name, root, self, state_dir, str. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, ValueError, assert_mutation_allowed, confined_path, list, root.resolve, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[23].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[0]::Assign

Source: `infra/agentinfra/transaction.py:79`; AST `2f05701fc8e1aa914cf88a3a35c9e5e178d0e3674a075174aa2f298cf310c32d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[0].value::Call

Source: `infra/agentinfra/transaction.py:79`; AST `56ce091af63844ee93125714af2e994600b88740aa8b9bf3bb1ba7526dba15a7`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[1]::Assign

Source: `infra/agentinfra/transaction.py:80`; AST `77ce338f7bf846cd039d41f20dae699d953afbb6b6630e2290e5ef3f4c52db7d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, mutations, self. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[1].value::Call

Source: `infra/agentinfra/transaction.py:80`; AST `579e4147ded20f0070a0468f3928756eb219ccd43b5b1f6b407ad2f43ce2d8b9`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, mutations. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[2]::Try

Source: `infra/agentinfra/transaction.py:81`; AST `35992b31d0b3f7203c4586386ff7fd7cb82afed4ffa84a70b55724767adedad5`.

Rust module: `infra::agentinfra::transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: GovernanceViolation, TransactionError, assert_mutation_allowed, confined_path, exc, self, state_dir, str. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, assert_mutation_allowed, confined_path, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[23].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[2].body[0]::Expr

Source: `infra/agentinfra/transaction.py:82`; AST `54f9c97cbd6f479c1446c9df96d87e3d46dc19421cd311cf89d87eedbeec99f3`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assert_mutation_allowed, self, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: assert_mutation_allowed.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[2].body[0].value::Call

Source: `infra/agentinfra/transaction.py:82`; AST `cb063478cbe0af3a77cf94b1b1550e9339ade1f7ba4ed533aa668ca103c9b202`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assert_mutation_allowed, self, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: assert_mutation_allowed.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[2].body[1]::Assign

Source: `infra/agentinfra/transaction.py:83`; AST `5e4ad93cfbe4bef1ad27c852e03e9a39b538c257e91c3078faa157f51898828e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, self, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[1].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[2].body[1].value::Call

Source: `infra/agentinfra/transaction.py:83`; AST `e7865380a420204b33cfd73b1ef4a34bafd7fa0031c24266a15fabe2d2306f6c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, self, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[2].handlers[0]::ExceptHandler

Source: `infra/agentinfra/transaction.py:84`; AST `165f174ff145002b10e45b541e38e64e5e61450d3b670baf7917f747a304c9fc`.

Rust module: `infra::agentinfra::transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: GovernanceViolation, TransactionError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[23].body[1].body[2].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[2].handlers[0].body[0]::Raise

Source: `infra/agentinfra/transaction.py:85`; AST `d397fcf6862d0f79a97bc5e0aa3aa47ad316578601608469efde09289cc11b2e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[1].body[2].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[2].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:85`; AST `f5aafeeb54ee191e2d99893e2460d8fd521ec628137e551ec65e7855693a178a`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].body[2].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[2].handlers[0].body[0].exc.args[0]::Call

Source: `infra/agentinfra/transaction.py:85`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].body[2].handlers[0].body[0].exc.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[3]::Assign

Source: `infra/agentinfra/transaction.py:86`; AST `eb2769a98b129f21207d4ef2940d29ada2d7c3a325f16f611e5e5a59a9863f5b`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[4]::Assign

Source: `infra/agentinfra/transaction.py:87`; AST `65d92f128ee9a6d942e3e1c1fefb51547ce9dd0106863ef5061f2063164ddf92`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fault, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[5]::If

Source: `infra/agentinfra/transaction.py:88`; AST `184b53a29755c34612d597f03c65a0726be3af0497c344ad8732878c62e5ba6b`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, self. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[1].body[5]; no call, error or mutation may be omitted. Condition: not self.mutations
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[5].body[0]::Raise

Source: `infra/agentinfra/transaction.py:89`; AST `843f77aa388a4f4ba20fafe100ad59dbdd66d54397ab8157ea0ac86a88238e05`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[1].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::__init__::root.body[23].body[1].body[5].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:89`; AST `b928e942818d3a9785078dfd5ef8ebe48a9e3d7ffda69a4bb9568c5b377ed9c3`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].body[5].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2]::FunctionDef

Source: `infra/agentinfra/transaction.py:91`; AST `64bebbfc1886cb6dca48db612d20b54754f7735a72c0e986e8c3c4945ba56964`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GovernanceViolation, Path, TransactionError, _now, _read, _sha, assert_mutation_allowed, base64, before, before_hash, confined_path, dict, enumerate, exc, index, journal, mode, mutation, path, records, rel, seen, self, set, stat, str, tuple, tx_dir, txid, uuid. Outputs/bindings: before, before_hash, index, journal, mode, mutation, path, records, rel, seen, tx_dir, txid.
Calls/effect boundaries: TransactionError, _now, _read, _sha, assert_mutation_allowed, base64.b64encode, base64.b64encode(before).decode, confined_path, enumerate, path.exists, path.relative_to, path.relative_to(self.root).as_posix, path.stat, records.append, seen.add, set, stat.S_IMODE, str, uuid.uuid4.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[23].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[0]::Assign

Source: `infra/agentinfra/transaction.py:92`; AST `779295ccb7c611b49e46496fa386e920b5f5ad6b93cdb4a9e27bb6ce54287e4a`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, uuid. Outputs/bindings: txid.
Calls/effect boundaries: uuid.uuid4.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[0].value.values[2].value.value::Call

Source: `infra/agentinfra/transaction.py:92`; AST `87eafda000cba758be33f767d487f36fa6a34917ff4cfe4cbd289edd7d07163b`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: uuid. Outputs/bindings: (none).
Calls/effect boundaries: uuid.uuid4.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[0].value.values[2].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[1]::Assign

Source: `infra/agentinfra/transaction.py:93`; AST `0150d97ea7eb645d253e43ef241cb31cfa47754909ffb412ad840dc3cc2fef3f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, txid. Outputs/bindings: tx_dir.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[2]::Assign

Source: `infra/agentinfra/transaction.py:94`; AST `8d2b3329d11e5d5fce64c015ffd23e2bd586b14f239a87c8b7c6e2f15d59a922`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: records.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[3]::AnnAssign

Source: `infra/agentinfra/transaction.py:95`; AST `477c4101a4efddf4a3b5ba8285856fbf715d43ea734c34f2c7c3642cf1daf775`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set, str. Outputs/bindings: seen.
Calls/effect boundaries: set.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[23].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[3].value::Call

Source: `infra/agentinfra/transaction.py:95`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4]::For

Source: `infra/agentinfra/transaction.py:96`; AST `98b6d49af9b94d735f5762dbd0e71f511e9faa74c5db6e92a23a080544776cab`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: GovernanceViolation, TransactionError, _read, _sha, assert_mutation_allowed, base64, before, before_hash, confined_path, enumerate, exc, index, mode, mutation, path, records, rel, seen, self, stat, str. Outputs/bindings: before, before_hash, index, mode, mutation, path, rel.
Calls/effect boundaries: TransactionError, _read, _sha, assert_mutation_allowed, base64.b64encode, base64.b64encode(before).decode, confined_path, enumerate, path.exists, path.relative_to, path.relative_to(self.root).as_posix, path.stat, records.append, seen.add, stat.S_IMODE, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[23].body[2].body[4]; no call, error or mutation may be omitted. Iteration: (index, mutation) in enumerate(self.mutations)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].iter::Call

Source: `infra/agentinfra/transaction.py:96`; AST `d7748c0a8320a83d60072c7648f4d6039ca4f489031bca4f0741c121205e5a88`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: enumerate, self. Outputs/bindings: (none).
Calls/effect boundaries: enumerate.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[0]::Try

Source: `infra/agentinfra/transaction.py:97`; AST `fafa7a3130760ddf7a95ba7ae00fe66210dfa00d726449fc649593f4cae5d847`.

Rust module: `infra::agentinfra::transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: GovernanceViolation, TransactionError, assert_mutation_allowed, confined_path, exc, mutation, self, str. Outputs/bindings: path.
Calls/effect boundaries: TransactionError, assert_mutation_allowed, confined_path, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[23].body[2].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[0].body[0]::Expr

Source: `infra/agentinfra/transaction.py:98`; AST `b4d4ff77c35ffd88daa6059fd57f5cd234ee09eceb6ab7897c6d4da83b554f52`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assert_mutation_allowed, mutation, self. Outputs/bindings: (none).
Calls/effect boundaries: assert_mutation_allowed.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[2].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:98`; AST `e309fe3ab785128134830dbd87d5458cfd7aefc2e3328612d46b1a4115d66999`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assert_mutation_allowed, mutation, self. Outputs/bindings: (none).
Calls/effect boundaries: assert_mutation_allowed.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[0].body[1]::Assign

Source: `infra/agentinfra/transaction.py:99`; AST `e9873c18cbd74be1088aebdfa93fe5a7d06a2abd6b205b5437ad77a7f9a01746`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, mutation, self. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2].body[4].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[0].body[1].value::Call

Source: `infra/agentinfra/transaction.py:99`; AST `2f91a71011de0cd27994acbecc24dd872d6ac039957b1c51a7e94b6ce9f4df3d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, mutation, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/transaction.py:100`; AST `165f174ff145002b10e45b541e38e64e5e61450d3b670baf7917f747a304c9fc`.

Rust module: `infra::agentinfra::transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: GovernanceViolation, TransactionError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[23].body[2].body[4].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[0].handlers[0].body[0]::Raise

Source: `infra/agentinfra/transaction.py:101`; AST `d397fcf6862d0f79a97bc5e0aa3aa47ad316578601608469efde09289cc11b2e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[2].body[4].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[0].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:101`; AST `f5aafeeb54ee191e2d99893e2460d8fd521ec628137e551ec65e7855693a178a`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[0].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[0].handlers[0].body[0].exc.args[0]::Call

Source: `infra/agentinfra/transaction.py:101`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[0].handlers[0].body[0].exc.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[1]::Assign

Source: `infra/agentinfra/transaction.py:102`; AST `4c5784ee87aaff089fc195e798bc3db6a4bdeedd712985e41a03e06c0e59e893`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, self. Outputs/bindings: rel.
Calls/effect boundaries: path.relative_to, path.relative_to(self.root).as_posix.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[1].value::Call

Source: `infra/agentinfra/transaction.py:102`; AST `183b483ed3dc2bb017dbb1924e01f7b86f5e2dea535267e9522510e0ce5edc12`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(self.root).as_posix.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[1].value.func.value::Call

Source: `infra/agentinfra/transaction.py:102`; AST `2717a605bfb62d7fe4881c74701659723cf3a3b6419efe59be1aa8b03080cb76`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[2]::If

Source: `infra/agentinfra/transaction.py:103`; AST `ce3ca514999ec4c24f9bf8d2ffe99a342da416f2731b19278011656b92fa8dea`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, rel, seen. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[2].body[4].body[2]; no call, error or mutation may be omitted. Condition: rel in seen
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[2].body[0]::Raise

Source: `infra/agentinfra/transaction.py:104`; AST `5b86c8d68e634a82fdf132ed1d8d1594932f393474c24376132d51b660ce016d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, rel. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[2].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[2].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:104`; AST `6e24a787c63e1a7924d9e08b92055c50d87bc0022511e761502aa214d6ba6fee`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, rel. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[3]::Expr

Source: `infra/agentinfra/transaction.py:105`; AST `620df3f237ed360fb6536e88372cb37a661289734dc9377ed1d22e133c394dbb`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: rel, seen. Outputs/bindings: (none).
Calls/effect boundaries: seen.add.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[2].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[3].value::Call

Source: `infra/agentinfra/transaction.py:105`; AST `a4e44a6e9b439eebffd39326ccf2df95008e37e20c43174d720c9920fcf71008`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: rel, seen. Outputs/bindings: (none).
Calls/effect boundaries: seen.add.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[4]::Assign

Source: `infra/agentinfra/transaction.py:106`; AST `41870ad8a5892437df284336a0c1333edbd172d9690de7eb8492814cbc1fb22f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _read, path. Outputs/bindings: before.
Calls/effect boundaries: _read.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[4].value::Call

Source: `infra/agentinfra/transaction.py:106`; AST `1f2f75b93be5f6f124d7aae1d19cc9f78c318b0a8ab019dfd7079ab453b0731c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read, path. Outputs/bindings: (none).
Calls/effect boundaries: _read.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[5]::Assign

Source: `infra/agentinfra/transaction.py:107`; AST `660b50fe610bdea6f9d761c8fa92324d0ddac42267124288d971a5fd6c379444`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _sha, before. Outputs/bindings: before_hash.
Calls/effect boundaries: _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[5].value::Call

Source: `infra/agentinfra/transaction.py:107`; AST `670cb82ecd33a2ec9b42eebee744ae5259a326646a4f6799800668e97f25135e`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _sha, before. Outputs/bindings: (none).
Calls/effect boundaries: _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[6]::If

Source: `infra/agentinfra/transaction.py:108`; AST `f28aea2d28e5f59c60ec231918720af2d4ec0d3945c2050bbea82c2e2ce2165c`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, before, mutation, rel. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[2].body[4].body[6]; no call, error or mutation may be omitted. Condition: mutation.expected_exists is not None and (before is not None) != mutation.expected_exists
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[6].body[0]::Raise

Source: `infra/agentinfra/transaction.py:109`; AST `419457eaa82b2a93d6b064dfce98cac7f6fb90764aee50f92d8aaf505375859a`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, rel. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[2].body[4].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[6].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:109`; AST `f93cb71adf8301e3e47d8540abab0ddcc87cf380cc87d7d8ef38e26f83881d60`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, rel. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[6].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[7]::If

Source: `infra/agentinfra/transaction.py:110`; AST `ce4c83c4bada61dfbe9b9faafe17b2749ed2e2acdc6ff20d24b46d4bee03b64a`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, before_hash, mutation, rel. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[2].body[4].body[7]; no call, error or mutation may be omitted. Condition: mutation.expected_sha256 is not None and before_hash != mutation.expected_sha256
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[7].body[0]::Raise

Source: `infra/agentinfra/transaction.py:111`; AST `9806b598a4248ec9c69438c291a49406adb5d50fc6793456c5e4b084f8eaae02`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, rel. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[2].body[4].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[7].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:111`; AST `ff4603ad5c264f4e966b2a92de276df7ff2f9cc50ab4c0ed28e78575568dfb99`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, rel. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[7].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[8]::Assign

Source: `infra/agentinfra/transaction.py:112`; AST `272bffa3384fa632ee234e1dd3b030e8010c53691842e72b6d5b382592cc0f9b`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mutation, path, stat. Outputs/bindings: mode.
Calls/effect boundaries: path.exists, path.stat, stat.S_IMODE.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2].body[4].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[8].value.test::Call

Source: `infra/agentinfra/transaction.py:112`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[8].value.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[8].value.body::Call

Source: `infra/agentinfra/transaction.py:112`; AST `5000b3727d4a08bc08940fc09e3a239c8cae85b8ce1b1e370944035830d61bda`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, stat. Outputs/bindings: (none).
Calls/effect boundaries: path.stat, stat.S_IMODE.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[8].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[8].value.body.args[0].value::Call

Source: `infra/agentinfra/transaction.py:112`; AST `d0f2660d5c576e75c41493128e9ef73fd43d1401a0dd272c961864f7164b7698`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[8].value.body.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[9]::Expr

Source: `infra/agentinfra/transaction.py:113`; AST `990ad67f6389bb0786bee5da4b2ea8c7a08a695b099e5cd2804b1620cbdc09b1`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _sha, base64, before, before_hash, index, mode, mutation, records, rel. Outputs/bindings: (none).
Calls/effect boundaries: _sha, base64.b64encode, base64.b64encode(before).decode, records.append.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[2].body[4].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[9].value::Call

Source: `infra/agentinfra/transaction.py:113`; AST `4dadfd93f474831b526ced1685dfdef9ba9aa1f793e253e67e23cb701899ebf3`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _sha, base64, before, before_hash, index, mode, mutation, records, rel. Outputs/bindings: (none).
Calls/effect boundaries: _sha, base64.b64encode, base64.b64encode(before).decode, records.append.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[9].value.args[0].values[3]::Call

Source: `infra/agentinfra/transaction.py:118`; AST `51d0b0398228d978bb5ab423cb82d19c8250bc1620d6294064b1c13299dd382d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _sha, mutation. Outputs/bindings: (none).
Calls/effect boundaries: _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[9].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[9].value.args[0].values[4].body::Call

Source: `infra/agentinfra/transaction.py:119`; AST `a0ea7e3bfd3b01250851efadcf1ff0522bb60fc44450e04454d0ad2f58270d57`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base64, before. Outputs/bindings: (none).
Calls/effect boundaries: base64.b64encode, base64.b64encode(before).decode.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[9].value.args[0].values[4].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[4].body[9].value.args[0].values[4].body.func.value::Call

Source: `infra/agentinfra/transaction.py:119`; AST `e0e2e321c9915b9058e2fac213406cca204f7b2392259a979df49642520c60f1`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base64, before. Outputs/bindings: (none).
Calls/effect boundaries: base64.b64encode.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[4].body[9].value.args[0].values[4].body.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[5]::Assign

Source: `infra/agentinfra/transaction.py:124`; AST `d54c00b7f632e8566b641b493dc1eefce89ab2b4f66c47d63c092ac842b12117`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _now, records, self, str, txid. Outputs/bindings: journal.
Calls/effect boundaries: _now, str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[5].value.values[3]::Call

Source: `infra/agentinfra/transaction.py:128`; AST `531d374d6b75ec14086e1aea690b44e54b7402137cf93951c8a96955114178a7`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[5].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[5].value.values[4]::Call

Source: `infra/agentinfra/transaction.py:129`; AST `a45c2ac57befcf1212794e7c42a7aad7870de2198eba961b8d2f47b37f928f0f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].body[5].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::_preflight::root.body[23].body[2].body[6]::Return

Source: `infra/agentinfra/transaction.py:134`; AST `bb40f0d1ce155755d752de9d316de7e6fd24e0f3fb6b2aad02e6c8e598cf7e91`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal, tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[23].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3]::FunctionDef

Source: `infra/agentinfra/transaction.py:136`; AST `d8427abaa2db0d3f556fcc04eff0ffe0022bc4d889397ce260489e0fe86b1af1`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, Exception, FileLock, Path, TransactionError, _fault, _now, _read, _sha, any, atomic_write_bytes, atomic_write_json, bool, dict, durable_unlink, enumerate, index, journal, journal_path, lock, mutation, original, path, record, recover_pending_transactions, recover_transaction, retain, rollback, self, tx_dir, zip. Outputs/bindings: index, journal, journal_path, lock, mutation, path, record, tx_dir.
Calls/effect boundaries: (tx_dir / 'journal.json').exists, (tx_dir / 'journal.json').unlink, FileLock, TransactionError, _fault, _now, _read, _sha, any, atomic_write_bytes, atomic_write_json, durable_unlink, enumerate, lock.acquire, lock.release, recover_pending_transactions, recover_transaction, self._preflight, self.state_dir.mkdir, tx_dir.exists, tx_dir.iterdir, tx_dir.mkdir, tx_dir.rmdir, zip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[23].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[0]::Expr

Source: `infra/agentinfra/transaction.py:137`; AST `8c24d1083ee2e5ec54ce6568ab0d7e964fd25ad3205dfb223c93a006453c6249`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state_dir.mkdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[0].value::Call

Source: `infra/agentinfra/transaction.py:137`; AST `f9c5c605c7dcc233e470014bb1656a4b6b5e7a5aaf2f28a55f89716d6de3ca63`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state_dir.mkdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[1]::Assign

Source: `infra/agentinfra/transaction.py:138`; AST `75282230c637055b1f993eebe1e4eddcc5e4ee2a04bad54f32ed1ef8d1cb01b4`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[1].value::Call

Source: `infra/agentinfra/transaction.py:138`; AST `5913abcaa9dcc949aee08ebf42e613104e16743aa6bb225e501401eaacce728b`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[2]::Expr

Source: `infra/agentinfra/transaction.py:139`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[2].value::Call

Source: `infra/agentinfra/transaction.py:139`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[3]::AnnAssign

Source: `infra/agentinfra/transaction.py:140`; AST `86a842b922f4f91ed633aa4de90392b72b4cffb5e83031bc7747f6bd55178b33`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict. Outputs/bindings: journal.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[23].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[4]::AnnAssign

Source: `infra/agentinfra/transaction.py:141`; AST `7b72ba496c4c944829676092a5f9f74efe23ee268d3c12c64c515320168ede7e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: tx_dir.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[23].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5]::Try

Source: `infra/agentinfra/transaction.py:142`; AST `bb74dfb783bf34ff40b3be407af4919258262601bb8c518785b648111f548668`.

Rust module: `infra::agentinfra::transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, Exception, TransactionError, _fault, _now, _read, _sha, any, atomic_write_bytes, atomic_write_json, durable_unlink, enumerate, index, journal, journal_path, lock, mutation, original, path, record, recover_pending_transactions, recover_transaction, retain, rollback, self, tx_dir, zip. Outputs/bindings: index, journal, journal_path, mutation, path, record, tx_dir.
Calls/effect boundaries: (tx_dir / 'journal.json').exists, (tx_dir / 'journal.json').unlink, TransactionError, _fault, _now, _read, _sha, any, atomic_write_bytes, atomic_write_json, durable_unlink, enumerate, lock.release, recover_pending_transactions, recover_transaction, self._preflight, tx_dir.exists, tx_dir.iterdir, tx_dir.mkdir, tx_dir.rmdir, zip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[23].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[0]::Expr

Source: `infra/agentinfra/transaction.py:143`; AST `9dc75a51bd29acd51f67428f2b242f4bc091b328eee3c8e48436a7b6dbdb2aac`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recover_pending_transactions, self. Outputs/bindings: (none).
Calls/effect boundaries: recover_pending_transactions.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[0].value::Call

Source: `infra/agentinfra/transaction.py:143`; AST `56ca2facf35c64b72ef8654e7a5b1acf9b17ec299061ae67b632c6ff09719e2f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recover_pending_transactions, self. Outputs/bindings: (none).
Calls/effect boundaries: recover_pending_transactions.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[1]::Assign

Source: `infra/agentinfra/transaction.py:144`; AST `bcf9f23ad636467715751251018e36967c71812ec4b26fc6cdf3f851c10b563f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: journal, tx_dir.
Calls/effect boundaries: self._preflight.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[3].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[1].value::Call

Source: `infra/agentinfra/transaction.py:144`; AST `390e8d2b2fb4fae8d21a857d1afcd380fe8297b6ee09dc018f90d55b01fee361`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self._preflight.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[2]::Expr

Source: `infra/agentinfra/transaction.py:145`; AST `c8a3cf33f92102846cce3cf256fddbd772e631bd44d1c330e2b58d1ed8167286`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: tx_dir.mkdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[2].value::Call

Source: `infra/agentinfra/transaction.py:145`; AST `42dfc61fb5bdeb262d64b193753baae2a584ee1ce1ec3eae1eec0e3f2eae5a26`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: tx_dir.mkdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[3]::Assign

Source: `infra/agentinfra/transaction.py:146`; AST `dd7ea5d3db428fd7f4e2546a2ad6538aba7f17c89686139bbef14cfe2c186c3a`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tx_dir. Outputs/bindings: journal_path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[3].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[4]::Expr

Source: `infra/agentinfra/transaction.py:147`; AST `4a1745547bd43f70c05aaeac25905c30d43b22d4feb816d908c53e4e302b7a0f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[4].value::Call

Source: `infra/agentinfra/transaction.py:147`; AST `eee14c2b5f425d54c125336ef8de05b9468cd610a22edd6889f4daee43179a19`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[5]::Expr

Source: `infra/agentinfra/transaction.py:148`; AST `159b7aa235dd71356377dc8acc515ce86fec518f8b667da7366e0576ad47390e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, journal, journal_path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[5].value::Call

Source: `infra/agentinfra/transaction.py:148`; AST `2faab64e8a09567955be6c3667e41a0e933f1753c77bdfce242c8b4a5967fc02`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, journal, journal_path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[6]::Expr

Source: `infra/agentinfra/transaction.py:149`; AST `b53584a4041cbee194ffcc67ce69213154a9648548365751f2ef0addc1ee6483`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[6].value::Call

Source: `infra/agentinfra/transaction.py:149`; AST `824dda6619b86fea5b82486fa9dd1d7f4973da30c43561527a4cd701f9f1eb4f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[7]::Assign

Source: `infra/agentinfra/transaction.py:150`; AST `2b0a2841723927e073466b27d162e8b7f201f7e7dc1348e8ad409a75977f40b6`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[3].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[8]::Expr

Source: `infra/agentinfra/transaction.py:151`; AST `159b7aa235dd71356377dc8acc515ce86fec518f8b667da7366e0576ad47390e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, journal, journal_path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[8].value::Call

Source: `infra/agentinfra/transaction.py:151`; AST `2faab64e8a09567955be6c3667e41a0e933f1753c77bdfce242c8b4a5967fc02`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, journal, journal_path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9]::For

Source: `infra/agentinfra/transaction.py:152`; AST `2dc6b5222ecc42e073cdda2aaa669c8b3173c2a9d9e5923f28de16515d6827de`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: TransactionError, _fault, _read, _sha, atomic_write_bytes, atomic_write_json, durable_unlink, enumerate, index, journal, journal_path, mutation, path, record, self, zip. Outputs/bindings: index, mutation, path, record.
Calls/effect boundaries: TransactionError, _fault, _read, _sha, atomic_write_bytes, atomic_write_json, durable_unlink, enumerate, zip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[23].body[3].body[5].body[9]; no call, error or mutation may be omitted. Iteration: (index, (mutation, record)) in enumerate(zip(self.mutations, journal['records']), 1)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].iter::Call

Source: `infra/agentinfra/transaction.py:152`; AST `35d33842ba13b5c003f3f668a4603ae7b7ccf9edcba9ce7428b25a891d2acadf`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: enumerate, journal, self, zip. Outputs/bindings: (none).
Calls/effect boundaries: enumerate, zip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].iter.args[0]::Call

Source: `infra/agentinfra/transaction.py:152`; AST `eb70c6dc03365d10323e307836d6e2d3b46126ec595371eb71aa57354350e303`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal, self, zip. Outputs/bindings: (none).
Calls/effect boundaries: zip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[0]::Assign

Source: `infra/agentinfra/transaction.py:153`; AST `2d5f90b3ec9ec2ad6db44f32e64ea56cef134e67ed97f9f5e29aceab6d674a6d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[3].body[5].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[1]::If

Source: `infra/agentinfra/transaction.py:154`; AST `0ad189c9411c048fd93ba6befd9a09b05983cc6d95efb39f951470b2b5476838`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, _read, _sha, path, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, _read, _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[3].body[5].body[9].body[1]; no call, error or mutation may be omitted. Condition: _sha(_read(path)) != record['before_sha256']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[1].test.left::Call

Source: `infra/agentinfra/transaction.py:154`; AST `4f28145d3c053ef73304dfffb02e3ebb639dd1c7c5fdea12763aa0716c412eb0`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read, _sha, path. Outputs/bindings: (none).
Calls/effect boundaries: _read, _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[1].test.left.args[0]::Call

Source: `infra/agentinfra/transaction.py:154`; AST `1f2f75b93be5f6f124d7aae1d19cc9f78c318b0a8ab019dfd7079ab453b0731c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read, path. Outputs/bindings: (none).
Calls/effect boundaries: _read.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[1].test.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[1].body[0]::Raise

Source: `infra/agentinfra/transaction.py:155`; AST `d0824f213dd3b412f9060b28802bff9ad6e0445007963a21a18ba1e7d027a0eb`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[3].body[5].body[9].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[1].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:155`; AST `8f2b383e9242ea15f06679450272241a85ad008ab6a8736dfca69fa107ceba59`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[2]::Expr

Source: `infra/agentinfra/transaction.py:156`; AST `29dbd08e43e3651d8ca5bc802ddc7abd77256bf1e357aac30639dec33b82604e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[2].value::Call

Source: `infra/agentinfra/transaction.py:156`; AST `937cb829126789088968eb1ae0b3807a532a294075c1cee42fcbfee3f5134f5c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[3]::If

Source: `infra/agentinfra/transaction.py:157`; AST `c16f6b48c61939d6523de2357c4a1dad03d5ac7ce14bee7e208d1d36b4039203`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: atomic_write_bytes, durable_unlink, mutation, path, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, durable_unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[3].body[5].body[9].body[3]; no call, error or mutation may be omitted. Condition: mutation.data is None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[3].body[0]::Expr

Source: `infra/agentinfra/transaction.py:158`; AST `28a8e3e8d44fc5d06c8e33723476f4bb84c797f2ed7a4cf41c553f6c5809e53a`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: durable_unlink, path, self. Outputs/bindings: (none).
Calls/effect boundaries: durable_unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[9].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[3].body[0].value::Call

Source: `infra/agentinfra/transaction.py:158`; AST `544d3118d95fc4b590f11cf229508d4d86d95a59125e153123c7c2852d80240f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: durable_unlink, path, self. Outputs/bindings: (none).
Calls/effect boundaries: durable_unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[3].orelse[0]::Expr

Source: `infra/agentinfra/transaction.py:160`; AST `41ddd879bdcb3c62ec7a89ec98d311045d01702f83bb91d856ab097bfd67d6ba`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_bytes, mutation, path, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[9].body[3].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[3].orelse[0].value::Call

Source: `infra/agentinfra/transaction.py:160`; AST `519684d7c2a9cbeca7ecd3e0cbaf89a30d57c32a5f818570d64131c149fc6b41`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_bytes, mutation, path, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[3].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[4]::Expr

Source: `infra/agentinfra/transaction.py:161`; AST `e7a42beb995a5b55efc88ddf9d1b744748d0baed4f4cd1a918dc3706cfa507c7`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[4].value::Call

Source: `infra/agentinfra/transaction.py:161`; AST `2f51b205b21be91b041dbd96d924f1419c37b087ffbb218bd6f373117b2ba0db`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[5]::If

Source: `infra/agentinfra/transaction.py:162`; AST `5660041c971b6077568975a2f2f105a44b021cd55f64b94c1f20949fc945454c`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, _read, _sha, path, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, _read, _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[3].body[5].body[9].body[5]; no call, error or mutation may be omitted. Condition: _sha(_read(path)) != record['after_sha256']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[5].test.left::Call

Source: `infra/agentinfra/transaction.py:162`; AST `4f28145d3c053ef73304dfffb02e3ebb639dd1c7c5fdea12763aa0716c412eb0`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read, _sha, path. Outputs/bindings: (none).
Calls/effect boundaries: _read, _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[5].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[5].test.left.args[0]::Call

Source: `infra/agentinfra/transaction.py:162`; AST `1f2f75b93be5f6f124d7aae1d19cc9f78c318b0a8ab019dfd7079ab453b0731c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read, path. Outputs/bindings: (none).
Calls/effect boundaries: _read.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[5].test.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[5].body[0]::Raise

Source: `infra/agentinfra/transaction.py:163`; AST `b6026f751ee5af3b779f02c2444ce4532921e9cff9d2ae43489111086b2420df`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[3].body[5].body[9].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[5].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:163`; AST `4991b7ae084c159aef794f4add7b47d393cc963e818df002b7a360ddf1311e74`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[5].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[6]::Assign

Source: `infra/agentinfra/transaction.py:164`; AST `da2f6d0064272eb3c84af5912afb191401d6c6ed0404ee1381eae9cf9d9b54bb`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index, journal. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[3].body[5].body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[7]::Expr

Source: `infra/agentinfra/transaction.py:165`; AST `159b7aa235dd71356377dc8acc515ce86fec518f8b667da7366e0576ad47390e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, journal, journal_path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[9].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[9].body[7].value::Call

Source: `infra/agentinfra/transaction.py:165`; AST `2faab64e8a09567955be6c3667e41a0e933f1753c77bdfce242c8b4a5967fc02`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, journal, journal_path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[9].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[10]::Assign

Source: `infra/agentinfra/transaction.py:166`; AST `4730a7d637d47f6420beb6137b4bfff2ff752f7ba081e6dc98c4a27bb42f1b1b`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[3].body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[11]::Assign

Source: `infra/agentinfra/transaction.py:167`; AST `12ac3de00caff31497e9534444a9accc38616fbc96f0561e6bff2a8e1b665b1e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _now, journal. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[3].body[5].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[11].value::Call

Source: `infra/agentinfra/transaction.py:167`; AST `a45c2ac57befcf1212794e7c42a7aad7870de2198eba961b8d2f47b37f928f0f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[12]::Expr

Source: `infra/agentinfra/transaction.py:168`; AST `159b7aa235dd71356377dc8acc515ce86fec518f8b667da7366e0576ad47390e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, journal, journal_path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[12].value::Call

Source: `infra/agentinfra/transaction.py:168`; AST `2faab64e8a09567955be6c3667e41a0e933f1753c77bdfce242c8b4a5967fc02`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, journal, journal_path, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[13]::Expr

Source: `infra/agentinfra/transaction.py:169`; AST `69839961b685c94efd512ce8611c7df4a143cff064ac2eb6c22f4de0d5ca065c`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[13].value::Call

Source: `infra/agentinfra/transaction.py:169`; AST `405fb1e7633df6c07865e0d84b66e11b8d4b4aa4d1ca40c2cd1a97cf119862c1`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _fault, journal, self. Outputs/bindings: (none).
Calls/effect boundaries: _fault.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[14]::If

Source: `infra/agentinfra/transaction.py:170`; AST `065ab808ae0ded07d4782a1ea4e5a42c4788f538cba3be14784a548c4c14c7b0`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: retain, tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: (tx_dir / 'journal.json').unlink, tx_dir.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[3].body[5].body[14]; no call, error or mutation may be omitted. Condition: not retain
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[14].body[0]::Expr

Source: `infra/agentinfra/transaction.py:171`; AST `553ebc351a055bc749376849b763db1cc8d3d23de1e49887476903b258bd7e09`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: (tx_dir / 'journal.json').unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[14].body[0].value::Call

Source: `infra/agentinfra/transaction.py:171`; AST `6062d29a9d0911f2989a4a75cca9a7c4238d977e8adb3d681bd84eb872578fe2`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: (tx_dir / 'journal.json').unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[14].body[1]::Expr

Source: `infra/agentinfra/transaction.py:172`; AST `0893e01afff0552e4c0ae5fb198a6000656da5873a48935979bfa609f0d21db7`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: tx_dir.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[14].body[1].value::Call

Source: `infra/agentinfra/transaction.py:172`; AST `e4202c553d1927155f165a69aa45d05b09341335d23bed1076309f99296342a3`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: tx_dir.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].body[15]::Return

Source: `infra/agentinfra/transaction.py:173`; AST `a7f24192054c43d3f9ec59c1e34e72bd15947d3463104d39b1a7ed707ea679a5`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[23].body[3].body[5].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0]::ExceptHandler

Source: `infra/agentinfra/transaction.py:174`; AST `c43c815c636c0cd4bc5843e237b688656e05b2c7ed8eebd2782c1ba5ecbfeed7`.

Rust module: `infra::agentinfra::transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, Exception, TransactionError, any, journal, original, recover_transaction, rollback, self, tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: (tx_dir / 'journal.json').exists, TransactionError, any, recover_transaction, tx_dir.exists, tx_dir.iterdir, tx_dir.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[23].body[3].body[5].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0]::If

Source: `infra/agentinfra/transaction.py:175`; AST `50b30f7e121a716ae42381bfad46329c5042fcbf6a364de66fe8da34e5b06556`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: Exception, TransactionError, any, journal, original, recover_transaction, rollback, self, tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: (tx_dir / 'journal.json').exists, TransactionError, any, recover_transaction, tx_dir.exists, tx_dir.iterdir, tx_dir.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[3].body[5].handlers[0].body[0]; no call, error or mutation may be omitted. Condition: journal is not None and tx_dir is not None and (tx_dir / 'journal.json').exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].test.values[2]::Call

Source: `infra/agentinfra/transaction.py:175`; AST `e023ad910d3d16262a65f8495c96a0a6b5e9e3a790f1252dd2e2d947da635bba`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: (tx_dir / 'journal.json').exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].handlers[0].body[0].test.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].body[0]::Try

Source: `infra/agentinfra/transaction.py:176`; AST `3682b293cff486cce5eb05ea0f43ab6b23530e0ed605479cfbc3288a6d002b17`.

Rust module: `infra::agentinfra::transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, TransactionError, original, recover_transaction, rollback, self, tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, recover_transaction.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[23].body[3].body[5].handlers[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].body[0].body[0]::Expr

Source: `infra/agentinfra/transaction.py:177`; AST `318f47121d4384146028bfb12241e992b348abea9e81b1853e23f7423730a9d7`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recover_transaction, self, tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].handlers[0].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].body[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:177`; AST `dd9f006502b67aff8f795e10d37a63b5d93c26dbd52dc35a9783edae3157f9a9`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recover_transaction, self, tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: recover_transaction.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].handlers[0].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/transaction.py:178`; AST `e226aa4e286b4bdf521b2ccd328230e8de9b256740842c0586636315d43d0986`.

Rust module: `infra::agentinfra::transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, TransactionError, original, rollback. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[23].body[3].body[5].handlers[0].body[0].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].body[0].handlers[0].body[0]::Raise

Source: `infra/agentinfra/transaction.py:179`; AST `8412bc85361a4c8b6958df5976c4e28fa1cf24997597560d8162a67e00eae4d0`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, original, rollback. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[3].body[5].handlers[0].body[0].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].body[0].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:179`; AST `810d42a1af1045e33da4b6de267f0855e397863c85f17625fab21840282bbb2b`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, original, rollback. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].handlers[0].body[0].body[0].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].orelse[0]::If

Source: `infra/agentinfra/transaction.py:180`; AST `b07720a05ba44f1cf565893d218bcc79e6f4765b4eb83ea37170892d499e0a12`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: any, tx_dir.exists, tx_dir.iterdir, tx_dir.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[3].body[5].handlers[0].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: tx_dir is not None and tx_dir.exists() and (not any(tx_dir.iterdir()))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].test.values[1]::Call

Source: `infra/agentinfra/transaction.py:180`; AST `f2ef6bcfbc57df03efc578fae0a1a818b0c69f54b775c30290451dd087ea6ff5`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: tx_dir.exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].test.values[2].operand::Call

Source: `infra/agentinfra/transaction.py:180`; AST `601d971ad590489e836d619ffa70718b9a61fd992651ecc16f5ce0cdd26376ab`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: any, tx_dir.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].test.values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].test.values[2].operand.args[0]::Call

Source: `infra/agentinfra/transaction.py:180`; AST `8319450184a8bec9fe89268d6556efde3219337d27fa5414f3f9db1343d11077`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: tx_dir.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].test.values[2].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].body[0]::Expr

Source: `infra/agentinfra/transaction.py:181`; AST `0893e01afff0552e4c0ae5fb198a6000656da5873a48935979bfa609f0d21db7`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: tx_dir.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:181`; AST `e4202c553d1927155f165a69aa45d05b09341335d23bed1076309f99296342a3`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tx_dir. Outputs/bindings: (none).
Calls/effect boundaries: tx_dir.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].handlers[0].body[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].handlers[0].body[1]::Raise

Source: `infra/agentinfra/transaction.py:182`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[3].body[5].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].finalbody[0]::Expr

Source: `infra/agentinfra/transaction.py:184`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3].body[5].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::FileTransaction::commit::root.body[23].body[3].body[5].finalbody[0].value::Call

Source: `infra/agentinfra/transaction.py:184`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].body[5].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24]::FunctionDef

Source: `infra/agentinfra/transaction.py:187`; AST `9ea3ace0dab362d32600aabdc9a637d159f32da2679805aa9040573aae010183`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Exception, Path, TransactionError, dict, exc, isinstance, journal, journal_path, json. Outputs/bindings: journal.
Calls/effect boundaries: TransactionError, isinstance, journal_path.read_text, json.loads.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[24]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[0]::Try

Source: `infra/agentinfra/transaction.py:188`; AST `a992fb0c36c7501f180b4e5c614345cbda14ce9f68ba2ee45c3357988df8fb85`.

Rust module: `infra::agentinfra::transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, TransactionError, exc, journal_path, json. Outputs/bindings: journal.
Calls/effect boundaries: TransactionError, journal_path.read_text, json.loads.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[24].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[0].body[0]::Assign

Source: `infra/agentinfra/transaction.py:189`; AST `3d949e8a7e2ee483f2cb9162e991de12b2849d8129a9e33fa0ed707412dd03d0`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal_path, json. Outputs/bindings: journal.
Calls/effect boundaries: journal_path.read_text, json.loads.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:189`; AST `7aa8b6b8dfde94dd031a68c49df73731c43ae7746b526a40598675b68961559f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path, json. Outputs/bindings: (none).
Calls/effect boundaries: journal_path.read_text, json.loads.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[24].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[0].body[0].value.args[0]::Call

Source: `infra/agentinfra/transaction.py:189`; AST `1201965971c265219ad2e691a60f02d9a8eab01ce00ae6d2b8538b12b05e8a3c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path. Outputs/bindings: (none).
Calls/effect boundaries: journal_path.read_text.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[24].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/transaction.py:190`; AST `68a3da96c80dcf25bc45b32a93b9feb80e24ae3f0e89abfaf7b8fad7f078f2ca`.

Rust module: `infra::agentinfra::transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, TransactionError, exc, journal_path. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[24].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[0].handlers[0].body[0]::Raise

Source: `infra/agentinfra/transaction.py:191`; AST `caa7869ce62a99753f303137cb496f9b085bac2e01981e4c98b583729419cc86`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, exc, journal_path. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[24].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[0].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:191`; AST `a49de9e3f5651abd9d9288459949292d190ef876730386a368dcd6ff5868334f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, exc, journal_path. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[24].body[0].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[1]::If

Source: `infra/agentinfra/transaction.py:192`; AST `bf9a6356be8d65d34e49a8e75be34951142ffa5d4f71754db38f92f3219fedaf`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, dict, isinstance, journal. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, isinstance.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[24].body[1]; no call, error or mutation may be omitted. Condition: not isinstance(journal, dict)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[1].test.operand::Call

Source: `infra/agentinfra/transaction.py:192`; AST `7c31912f3a9473c35a6943432fdf15403f71cd728a323923db3b900b5f3c32a7`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, journal. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[24].body[1].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[1].body[0]::Raise

Source: `infra/agentinfra/transaction.py:193`; AST `a9ebdfb569717263d937799842281aaa80825f8322b5deb84e4ddfff2e940ffd`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[24].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[1].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:193`; AST `6554c396d0433555e7c3c152d48707b6f47fa1c84a5caed77955c79cb30e896f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[24].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_read_recovery_journal::root.body[24].body[2]::Return

Source: `infra/agentinfra/transaction.py:194`; AST `a7f24192054c43d3f9ec59c1e34e72bd15947d3463104d39b1a7ed707ea679a5`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[24].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25]::FunctionDef

Source: `infra/agentinfra/transaction.py:197`; AST `fde9cc710ee0e43448af5e38c0876ac9af8a3250c0148bcec01f961143d95a45`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, bool, int, isinstance, len, object, str, value. Outputs/bindings: (none).
Calls/effect boundaries: int, isinstance, len, value.lower.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[25]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[0]::If

Source: `infra/agentinfra/transaction.py:198`; AST `67ea56b37fdec5a27f3610360abd4b91f55caf93ee612747341b922d7e72eb35`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[25].body[0]; no call, error or mutation may be omitted. Condition: value is None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[0].body[0]::Return

Source: `infra/agentinfra/transaction.py:199`; AST `4a8ef490a01d3017cb999fbea58c2adfb60a40ad736e0d23eceb176a236b14c3`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[25].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[1]::If

Source: `infra/agentinfra/transaction.py:200`; AST `bf42a3d9ec0512f6aa1020d9c3931620544decae9ed06f6e421d961bc84cad33`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: isinstance, len, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, len.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[25].body[1]; no call, error or mutation may be omitted. Condition: not isinstance(value, str) or len(value) != 64
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[1].test.values[0].operand::Call

Source: `infra/agentinfra/transaction.py:200`; AST `f0937843eac35cb846ed896776839197deebad579475d870c722a45446739540`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[1].test.values[1].left::Call

Source: `infra/agentinfra/transaction.py:200`; AST `57bdbf809c25115282faa72b8f2a20b503b69c9d181b909be2b57a332a04a030`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[1].body[0]::Return

Source: `infra/agentinfra/transaction.py:201`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[25].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[2]::Try

Source: `infra/agentinfra/transaction.py:202`; AST `0437f159a94956fe18ecbbdc4901ff2d03cf6319f69802aef7d0fec492a73cf7`.

Rust module: `infra::agentinfra::transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ValueError, int, value. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[25].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[2].body[0]::Expr

Source: `infra/agentinfra/transaction.py:203`; AST `0a3da9980018d26138bba5d67352c79aca7528cddb55dabb84a662851215e2e7`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, value. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[2].body[0].value::Call

Source: `infra/agentinfra/transaction.py:203`; AST `1b9398b4fbde64f886a92e15020a3ffc26ab72f6eb6af91a80fad751a0c5e405`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, value. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[2].handlers[0]::ExceptHandler

Source: `infra/agentinfra/transaction.py:204`; AST `4883d4e0749e17f2c554fb7af5eba78a188ed801a4efb2f9c21a51787382ae77`.

Rust module: `infra::agentinfra::transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[25].body[2].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[2].handlers[0].body[0]::Return

Source: `infra/agentinfra/transaction.py:205`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[25].body[2].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[3]::Return

Source: `infra/agentinfra/transaction.py:206`; AST `6291d64bdcc9c490d9aa34e0e6b9c6868c61df433d63cf3ee1d6e7ba267c6b7b`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: value.lower.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[25].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_valid_sha256::root.body[25].body[3].value.comparators[0]::Call

Source: `infra/agentinfra/transaction.py:206`; AST `ee9426de8425e05f2e39b6a5c1ef00c436a34bc24ead8f1cb30fade220836da0`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: value.lower.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[3].value.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26]::FunctionDef

Source: `infra/agentinfra/transaction.py:209`; AST `7c52e37e81bbb317ffa0de74adc3f3ab4ab4b084919efbec51c8ee5ee4a3bf75`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, TransactionError, TypeError, ValueError, _RecoveryPlan, _read_recovery_journal, _sha, _valid_sha256, after_hash, base64, before, bool, bytes, confined_path, decoded_before, dict, encoded, exc, expected_hashes, expected_root, force_rollback, frozenset, isinstance, journal, journal_path, journal_root, list, path, phase, record, relative, root, seen, set, str, validated_paths. Outputs/bindings: after_hash, before, decoded_before, encoded, expected_hashes, journal, journal_root, path, phase, record, relative, root, seen, validated_paths.
Calls/effect boundaries: Path, Path(journal_root).resolve, TransactionError, _RecoveryPlan, _read_recovery_journal, _sha, _valid_sha256, base64.b64decode, confined_path, expected_root.resolve, frozenset, isinstance, journal.get, record.get, seen.add, set.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[26]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[0]::Assign

Source: `infra/agentinfra/transaction.py:216`; AST `23436bed0070a09ad971ec28ad067d589b5eb1755c57faefed2307a5cb614d84`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _read_recovery_journal, journal, journal_path. Outputs/bindings: journal.
Calls/effect boundaries: _read_recovery_journal.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[0].value.body::Call

Source: `infra/agentinfra/transaction.py:216`; AST `c8903d2ab060fbb22c76e470db2e8bbc7dbceef3cd440e57d200efcb4ce641bc`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read_recovery_journal, journal_path. Outputs/bindings: (none).
Calls/effect boundaries: _read_recovery_journal.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[1]::If

Source: `infra/agentinfra/transaction.py:217`; AST `51045895c4919f199dea830602b75f5bb4ae16990f3bfee7df7ddddd4cf0a67d`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, isinstance, journal, list. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, isinstance, journal.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[1]; no call, error or mutation may be omitted. Condition: journal.get('schema') != 1 or not isinstance(journal.get('records'), list)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[1].test.values[0].left::Call

Source: `infra/agentinfra/transaction.py:217`; AST `9a2e18c1887f766def4638fd9f8a24c829777773bf0da7df069d2f05352357be`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: journal.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[1].test.values[1].operand::Call

Source: `infra/agentinfra/transaction.py:217`; AST `48b531291622d3a06af293841bb5975c164efb3594dda1bd862d8e569c0beaa1`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, journal, list. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, journal.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[1].test.values[1].operand.args[0]::Call

Source: `infra/agentinfra/transaction.py:217`; AST `bae87bf06241466ffb5a5f766c8e18a5ca6530434a33afc05cc2a631393da95d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: journal.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].test.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[1].body[0]::Raise

Source: `infra/agentinfra/transaction.py:218`; AST `a9ebdfb569717263d937799842281aaa80825f8322b5deb84e4ddfff2e940ffd`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[26].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[1].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:218`; AST `6554c396d0433555e7c3c152d48707b6f47fa1c84a5caed77955c79cb30e896f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[2]::Assign

Source: `infra/agentinfra/transaction.py:219`; AST `842e88f3c779d57165dfa9081fbe4277a76c251e9aa2b717733267c8bfa28b6f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected_root. Outputs/bindings: root.
Calls/effect boundaries: expected_root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[2].value::Call

Source: `infra/agentinfra/transaction.py:219`; AST `fb6ef22fdb74dc3c57363b53033446b9a9fd3f8ef8437a925f05d8c21ff1aa1d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected_root. Outputs/bindings: (none).
Calls/effect boundaries: expected_root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[3]::Assign

Source: `infra/agentinfra/transaction.py:220`; AST `8de6b2cf21d96bdeff00225fa78f2192af02170c0aa87de3c16018c6ac6d8b12`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: journal_root.
Calls/effect boundaries: journal.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[3].value::Call

Source: `infra/agentinfra/transaction.py:220`; AST `ad44222abbda5d7c545edb7f5ec6cffb917591cb34c83d3282cc807ff674bac0`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: journal.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[4]::If

Source: `infra/agentinfra/transaction.py:221`; AST `ddf8e30f83f83cf8087ba7cfe2d0a903706edba60e2fb55c957b477dae091cac`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: Path, TransactionError, isinstance, journal_root, root, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(journal_root).resolve, TransactionError, isinstance.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[4]; no call, error or mutation may be omitted. Condition: not isinstance(journal_root, str) or not journal_root or Path(journal_root).resolve() != root
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[4].test.values[0].operand::Call

Source: `infra/agentinfra/transaction.py:221`; AST `b021d264b5f3e63a5bf5009f81cd7f454261d7b093b49b56c246ada6e89a6d24`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, journal_root, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[4].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[4].test.values[2].left::Call

Source: `infra/agentinfra/transaction.py:221`; AST `1c49675accc20ea2f8f8f52a12f392588e0d1af0f361658ae001a14848681172`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, journal_root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(journal_root).resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[4].test.values[2].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[4].test.values[2].left.func.value::Call

Source: `infra/agentinfra/transaction.py:221`; AST `69df3df436059e9d699f7209cc7a6f72f4b9c475931b61eea89bc6a462a518ed`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, journal_root. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[4].test.values[2].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[4].body[0]::Raise

Source: `infra/agentinfra/transaction.py:222`; AST `cf02751bc7d07d3991ed881ce4f2c383e01e2dc83efa85a0e1f2f7edca800a75`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[26].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[4].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:222`; AST `c85b52e41dbe7d1f8f722387d43918ea787ea1375db62098cba99b759cca8c9d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[4].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[5]::Assign

Source: `infra/agentinfra/transaction.py:223`; AST `b6948ac1fa5662365d246ec1122062631fe671209c8ab409c7f114f8f15ab4b8`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: phase.
Calls/effect boundaries: journal.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[5].value::Call

Source: `infra/agentinfra/transaction.py:223`; AST `077d571ef6a47a7cbf28cf48f8b6871f0d8565e94f21c6e232161b858c175c24`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: journal.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[6]::If

Source: `infra/agentinfra/transaction.py:224`; AST `198c9e839fe68c6bb856a35f0ac95a6456e51defb935ac5f720dc828a3e3f23c`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, phase. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[6]; no call, error or mutation may be omitted. Condition: phase not in {'PREPARED', 'APPLYING', 'COMMITTED', 'ROLLED_BACK'}
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[6].body[0]::Raise

Source: `infra/agentinfra/transaction.py:225`; AST `19264f974b2520c3f68483a099de0fcde4e2ae4ab6394978630131419472e30d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, phase. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[26].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[6].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:225`; AST `bfc7f8d2e1647db1d93e0f380123da7d5689f6a5892bff6bb1a11ee4c75c4b5c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, phase. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[6].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[7]::AnnAssign

Source: `infra/agentinfra/transaction.py:226`; AST `0784331ccabd725abb581709c9733cd82a9ad9441a06fb2534567141caf8ee46`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bytes, dict, str. Outputs/bindings: decoded_before.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[26].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[8]::AnnAssign

Source: `infra/agentinfra/transaction.py:227`; AST `df504e23e514070f8c20f8677ff8d8a6eafaa2278b228cea6e28ec99140893b3`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, dict, str. Outputs/bindings: validated_paths.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[26].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[9]::AnnAssign

Source: `infra/agentinfra/transaction.py:228`; AST `8a6e0f6e25a870ca720763ad72304e1527d1059e7d57666de99f86e53ac5d479`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, frozenset, str. Outputs/bindings: expected_hashes.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[26].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[10]::AnnAssign

Source: `infra/agentinfra/transaction.py:229`; AST `477c4101a4efddf4a3b5ba8285856fbf715d43ea734c34f2c7c3642cf1daf775`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set, str. Outputs/bindings: seen.
Calls/effect boundaries: set.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[26].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[10].value::Call

Source: `infra/agentinfra/transaction.py:229`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11]::For

Source: `infra/agentinfra/transaction.py:230`; AST `a4eba12d10f3140cd73844b89afd18133a409364857f35e243db89e9dcaa4c82`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: TransactionError, TypeError, ValueError, _sha, _valid_sha256, after_hash, base64, before, confined_path, decoded_before, dict, encoded, exc, expected_hashes, force_rollback, frozenset, isinstance, journal, path, phase, record, relative, root, seen, str, validated_paths. Outputs/bindings: after_hash, before, encoded, path, record, relative.
Calls/effect boundaries: TransactionError, _sha, _valid_sha256, base64.b64decode, confined_path, frozenset, isinstance, record.get, seen.add.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[26].body[11]; no call, error or mutation may be omitted. Iteration: record in journal['records']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[0]::If

Source: `infra/agentinfra/transaction.py:231`; AST `119b29203f887e4041a2918a3a42b39f7a5d04fb89628c932244986c4e67702d`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, dict, isinstance, record, str. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, isinstance, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[11].body[0]; no call, error or mutation may be omitted. Condition: not isinstance(record, dict) or not isinstance(record.get('path'), str)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/transaction.py:231`; AST `c1638e93b515785b3f31d5067c2fdc6324d1520c3d7614e7a0790bbe77a30e77`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, record. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[0].test.values[1].operand::Call

Source: `infra/agentinfra/transaction.py:231`; AST `42ebd41cd660ea67dcbfc7928836d58708e1e12cc73304225f375afcf9df3db3`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, record, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[0].test.values[1].operand.args[0]::Call

Source: `infra/agentinfra/transaction.py:231`; AST `fc6fd7b7ce84b0d19889bfd402f7c75897d860c5cf4be04a33cc65c79846d064`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[0].test.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[0].body[0]::Raise

Source: `infra/agentinfra/transaction.py:232`; AST `45d5a2827b78fb9495662cf21acda9fa70c5550f5828222eb2176810ece8a50e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[26].body[11].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[0].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:232`; AST `67775f6fb2369545a9ddbb22a7a22da4ef27c29d2206657d338a0acdc67ffac9`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[1]::Assign

Source: `infra/agentinfra/transaction.py:233`; AST `8536655cefc8ec64fab317bda84bce1853e8a45ef242fde4ed7ed04531dfd704`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: relative.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[2]::If

Source: `infra/agentinfra/transaction.py:234`; AST `52c938752547c002f90910ef13b0aca253f7e64664aac0be6e0a5fc0145b7b4c`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, relative, seen. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[11].body[2]; no call, error or mutation may be omitted. Condition: relative in seen
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[2].body[0]::Raise

Source: `infra/agentinfra/transaction.py:235`; AST `c0b62032bd67d749b534d2dcc8074e921d4a053db63e9b0fcf8346d0d3714a4d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, relative. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[26].body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[2].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:235`; AST `e064eb7ac2a45fd4b0452bb6fff60b90441491396a5705ff5973f241197c56ab`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, relative. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[3]::Expr

Source: `infra/agentinfra/transaction.py:236`; AST `2cef66d1181e068118bf45dcd342329e47f00ca94905130b8dce4d3278c6061f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative, seen. Outputs/bindings: (none).
Calls/effect boundaries: seen.add.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[26].body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[3].value::Call

Source: `infra/agentinfra/transaction.py:236`; AST `3b4ba3175c3314469a08252227eb504de5f11a1b3ca704047b45014285aa5a31`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative, seen. Outputs/bindings: (none).
Calls/effect boundaries: seen.add.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[4]::Assign

Source: `infra/agentinfra/transaction.py:237`; AST `fb45c8da2f3adf0f8bca96e64129877c7e6f7d61978ff4520d7b8ea59f00c496`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, relative, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[4].value::Call

Source: `infra/agentinfra/transaction.py:237`; AST `1e724b0ee6cd9e11e8f24934bd90c067902329ee0df7f7c98e48a82cf0b89157`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[5]::Assign

Source: `infra/agentinfra/transaction.py:238`; AST `14303c00a3942814226d8cbdf4c513e36d176b234931bb8700e01ab32c3b3112`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: encoded.
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[5].value::Call

Source: `infra/agentinfra/transaction.py:238`; AST `d278d913fa24b6ef2c6a8061f2560da3f56086e9ad069e5c7de28ea325f49ffe`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[6]::Try

Source: `infra/agentinfra/transaction.py:239`; AST `9f0f66f082f20640a223add8b1520999e620c5598d25cf54208aaff7e6a848e5`.

Rust module: `infra::agentinfra::transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: TransactionError, TypeError, ValueError, base64, encoded, exc, record. Outputs/bindings: before.
Calls/effect boundaries: TransactionError, base64.b64decode, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[26].body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[6].body[0]::Assign

Source: `infra/agentinfra/transaction.py:240`; AST `c5f84a1e79b0610083c81e30503dead823e102897448c74dfa16dfe99724aa29`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base64, encoded. Outputs/bindings: before.
Calls/effect boundaries: base64.b64decode.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[6].body[0].value.body::Call

Source: `infra/agentinfra/transaction.py:240`; AST `022473aef581c049597dc80e0f4db52d982246d223f3518918fb0b0f4fd6c9f5`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base64, encoded. Outputs/bindings: (none).
Calls/effect boundaries: base64.b64decode.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[6].body[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[6].handlers[0]::ExceptHandler

Source: `infra/agentinfra/transaction.py:241`; AST `f270ce624c98a8d691d38418bd85b8533c55c212d8f714be2c0dddff86e38930`.

Rust module: `infra::agentinfra::transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: TransactionError, TypeError, ValueError, exc, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[26].body[11].body[6].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[6].handlers[0].body[0]::Raise

Source: `infra/agentinfra/transaction.py:242`; AST `9068fee7b138489670f26a300dcba3fdc646565d004e61b1a1610c1f3a3fcbf1`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, exc, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[26].body[11].body[6].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[6].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:242`; AST `f04e2e90ce852a161d64f5056f2fc99dfdffa6dc155f820e6c1b83588f26e6dd`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[6].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[6].handlers[0].body[0].exc.args[0].values[1].value::Call

Source: `infra/agentinfra/transaction.py:242`; AST `fc6fd7b7ce84b0d19889bfd402f7c75897d860c5cf4be04a33cc65c79846d064`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[6].handlers[0].body[0].exc.args[0].values[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[7]::If

Source: `infra/agentinfra/transaction.py:243`; AST `1725b432ff78e7ed562ddfc0f71f349b3c3289a3f5883cd0980c4e1046fefc43`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, _sha, before, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, _sha, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[11].body[7]; no call, error or mutation may be omitted. Condition: _sha(before) != record.get('before_sha256')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[7].test.left::Call

Source: `infra/agentinfra/transaction.py:243`; AST `670cb82ecd33a2ec9b42eebee744ae5259a326646a4f6799800668e97f25135e`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _sha, before. Outputs/bindings: (none).
Calls/effect boundaries: _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[7].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[7].test.comparators[0]::Call

Source: `infra/agentinfra/transaction.py:243`; AST `d5c07dbe1191cf0399df005854452d0958205c52cc1f42b26412d9024e47d65a`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[7].test.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[7].body[0]::Raise

Source: `infra/agentinfra/transaction.py:244`; AST `c33b67a696a8a738f2e65bb2cd64dd52602dff6b0277156ece8c1dbdff4d9a33`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[26].body[11].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[7].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:244`; AST `c2712fecc2089f2ecdb7ed2f5364e5d3821403bf90f1df019510072ed737bda2`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[7].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[8]::Assign

Source: `infra/agentinfra/transaction.py:245`; AST `9d1ef2f5d11e1ea1e5dccd552de407af001b68dea75a7d7fc92f2626ac85da54`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: after_hash.
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[8].value::Call

Source: `infra/agentinfra/transaction.py:245`; AST `b1a88486e30d1fb5715437d8d8b017e73acab3fa10f507e28e6a8df2caf6f289`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[9]::If

Source: `infra/agentinfra/transaction.py:246`; AST `981ba3a9e7f9ce0479e87f291c1b538181a4fed8c8f5636d42d5988438c4fa9e`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, _valid_sha256, after_hash, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, _valid_sha256.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[11].body[9]; no call, error or mutation may be omitted. Condition: not _valid_sha256(after_hash)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[9].test.operand::Call

Source: `infra/agentinfra/transaction.py:246`; AST `7d243016d8993a13ef63dd4d6d802d12939fec455d63f9b64d1fe0af97a9d8bf`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _valid_sha256, after_hash. Outputs/bindings: (none).
Calls/effect boundaries: _valid_sha256.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[9].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[9].body[0]::Raise

Source: `infra/agentinfra/transaction.py:247`; AST `e784e0958b44964163cbea20006b7300c8512dd2e7f390473936d0e5cf4c8fd6`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[26].body[11].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[9].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:247`; AST `c7e38daefb5a2176239349992761d3876a66f4b100c7e5125bd03c362873f4cf`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, record. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[9].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[10]::Assign

Source: `infra/agentinfra/transaction.py:248`; AST `c6c3ec0558d795e0aa4c276a18b485a0b7805ba21d359d1b1cdbaabc43e3cccb`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, decoded_before, relative. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[11]::Assign

Source: `infra/agentinfra/transaction.py:249`; AST `be41fa70a7d2650266415bde5b373719bd111c24a1d8a6ac963466743e618154`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, relative, validated_paths. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[12]::If

Source: `infra/agentinfra/transaction.py:250`; AST `7863486f3cf9f4fc7c285ab35ee056c80dd1889ae34dfe29e64283dea6da15d5`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after_hash, expected_hashes, force_rollback, frozenset, phase, record, relative. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[11].body[12]; no call, error or mutation may be omitted. Condition: phase == 'ROLLED_BACK'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[12].body[0]::Assign

Source: `infra/agentinfra/transaction.py:251`; AST `0b8a1d018bbb81cb02618006fd77036a70b6fdc41a90e6ffac5b39c6359c4818`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected_hashes, frozenset, record, relative. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[12].body[0].value::Call

Source: `infra/agentinfra/transaction.py:251`; AST `e4028cd20391af7660bf48a15323ffe047f48e1161d75d96f722ecc90f8a6c2c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: frozenset, record. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[12].orelse[0]::If

Source: `infra/agentinfra/transaction.py:252`; AST `59ad959f23a6b2b2baac99d6412215417394ec91769f77e2897625534b7206a3`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after_hash, expected_hashes, force_rollback, frozenset, phase, record, relative. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[11].body[12].orelse[0]; no call, error or mutation may be omitted. Condition: phase == 'COMMITTED' and (not force_rollback)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[12].orelse[0].body[0]::Assign

Source: `infra/agentinfra/transaction.py:253`; AST `9abd45b55a417a9e4392c3e6d0f9f5d7fd1d2f0afd4fe392541888da9c0648da`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after_hash, expected_hashes, frozenset, relative. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[12].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[12].orelse[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:253`; AST `cebd305cc3f6846984a106e7cc78aa1498f61ba24917ffc82dafec7604f89c3d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after_hash, frozenset. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[12].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[12].orelse[0].orelse[0]::Assign

Source: `infra/agentinfra/transaction.py:255`; AST `3032fed090f2235c17a50cd016463406c76f9f6ae0dc4842c619aaa6f6e73237`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after_hash, expected_hashes, frozenset, record, relative. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[26].body[11].body[12].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[11].body[12].orelse[0].orelse[0].value::Call

Source: `infra/agentinfra/transaction.py:255`; AST `a4a6191e84ae685198a101505afba320d703144ac10bcb1d11d596e37897f33a`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after_hash, frozenset, record. Outputs/bindings: (none).
Calls/effect boundaries: frozenset.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[11].body[12].orelse[0].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[12]::Return

Source: `infra/agentinfra/transaction.py:256`; AST `35d7f57e2123e07a3c7854216eaf9e8278dd4b2c767d43f994ac9e883061f16f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _RecoveryPlan, decoded_before, expected_hashes, force_rollback, journal, journal_path, phase, validated_paths. Outputs/bindings: (none).
Calls/effect boundaries: _RecoveryPlan.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[26].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_prepare_recovery::root.body[26].body[12].value::Call

Source: `infra/agentinfra/transaction.py:256`; AST `b13d04f736de1ff6026c677ef5af2dd49a6472961a99b2f29b7308231f127683`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _RecoveryPlan, decoded_before, expected_hashes, force_rollback, journal, journal_path, phase, validated_paths. Outputs/bindings: (none).
Calls/effect boundaries: _RecoveryPlan.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27]::FunctionDef

Source: `infra/agentinfra/transaction.py:266`; AST `b834b1eeca55797f65f5916098c57774f9cb17626513389e275f686d1f3372d5`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, TransactionError, _RecoveryPlan, _read, _sha, bool, destinations, dict, list, path, plan, plans, prior, relative, tuple. Outputs/bindings: destinations, path, plan, prior, relative.
Calls/effect boundaries: TransactionError, _read, _sha, destinations.get, plan.paths.items.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[27]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[0]::AnnAssign

Source: `infra/agentinfra/transaction.py:267`; AST `0b0b8fde75026e083a52942a1a85eaf90edcacaa0896176c1c55b662011accbf`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, bool, dict, tuple. Outputs/bindings: destinations.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[27].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[1]::For

Source: `infra/agentinfra/transaction.py:268`; AST `cf792aa120fb76722c4e8ea9763bbd1cf4c8a228cdeb7278f40293268fea8dc8`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: TransactionError, destinations, path, plan, plans, prior, relative. Outputs/bindings: path, plan, prior, relative.
Calls/effect boundaries: TransactionError, destinations.get, plan.paths.items.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[27].body[1]; no call, error or mutation may be omitted. Iteration: plan in plans
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[1].body[0]::For

Source: `infra/agentinfra/transaction.py:269`; AST `b1b0556ac49be44f872e8d9b74442dc85eb3b28d8e7d6f324cdb553913cf99be`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: TransactionError, destinations, path, plan, prior, relative. Outputs/bindings: path, prior, relative.
Calls/effect boundaries: TransactionError, destinations.get, plan.paths.items.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[27].body[1].body[0]; no call, error or mutation may be omitted. Iteration: (relative, path) in plan.paths.items()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[1].body[0].iter::Call

Source: `infra/agentinfra/transaction.py:269`; AST `0f561cfb1bbf619a340932c41020d400dd51c13512aed77353d94c79314be581`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.paths.items.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[1].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[1].body[0].body[0]::Assign

Source: `infra/agentinfra/transaction.py:270`; AST `913f0ed21d5790afc4d89dd20a5a624f32003d383a22b3d444edea4e9fb41543`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destinations, path. Outputs/bindings: prior.
Calls/effect boundaries: destinations.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[27].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:270`; AST `e9aa320fe56957d901cd4d4e55a0567e97f232829fab2636d375398637363d68`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destinations, path. Outputs/bindings: (none).
Calls/effect boundaries: destinations.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[1].body[0].body[1]::If

Source: `infra/agentinfra/transaction.py:271`; AST `bfb97a3b8ded95da27bf9d17c7a1e81681ad44489556b6b5547f2243bed958e9`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, plan, prior, relative. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[27].body[1].body[0].body[1]; no call, error or mutation may be omitted. Condition: prior is not None and (prior[1] or plan.rollback)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[1].body[0].body[1].body[0]::Raise

Source: `infra/agentinfra/transaction.py:272`; AST `25530b3d614dc3472536e677739712689f495a703cea21f13e6fe79246c6f254`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, plan, prior, relative. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[27].body[1].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[1].body[0].body[1].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:272`; AST `91a37db5095115605de86484ea06ee5bf6fa13f5c363e21aa7d80e1d4d0dc72e`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, plan, prior, relative. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[1].body[0].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[1].body[0].body[2]::Assign

Source: `infra/agentinfra/transaction.py:276`; AST `2028a9e6a2f2e8185fc384d42d62e2aaf7e3a640e575bde3160f2428a0d7ede1`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destinations, path, plan. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[27].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[2]::For

Source: `infra/agentinfra/transaction.py:277`; AST `8d7e08743caf99f2a06f55116e75bb1da678b0526d6d9cdf72ae0e9c9bc169ee`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: TransactionError, _read, _sha, path, plan, plans, relative. Outputs/bindings: path, plan, relative.
Calls/effect boundaries: TransactionError, _read, _sha, plan.paths.items.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[27].body[2]; no call, error or mutation may be omitted. Iteration: plan in plans
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[2].body[0]::For

Source: `infra/agentinfra/transaction.py:278`; AST `aadb511cf8a9bbc21432647027d76ffc8afa05f8131e590f478afa5e7d84ec8a`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: TransactionError, _read, _sha, path, plan, relative. Outputs/bindings: path, relative.
Calls/effect boundaries: TransactionError, _read, _sha, plan.paths.items.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[27].body[2].body[0]; no call, error or mutation may be omitted. Iteration: (relative, path) in plan.paths.items()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[2].body[0].iter::Call

Source: `infra/agentinfra/transaction.py:278`; AST `0f561cfb1bbf619a340932c41020d400dd51c13512aed77353d94c79314be581`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.paths.items.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[2].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[2].body[0].body[0]::If

Source: `infra/agentinfra/transaction.py:279`; AST `c2c48099ca9350502996b65b3610117335ae5eae15d098f2ed01c6ac8b89b7fe`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, _read, _sha, path, plan, relative. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, _read, _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[27].body[2].body[0].body[0]; no call, error or mutation may be omitted. Condition: _sha(_read(path)) not in plan.expected_hashes[relative]
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[2].body[0].body[0].test.left::Call

Source: `infra/agentinfra/transaction.py:279`; AST `4f28145d3c053ef73304dfffb02e3ebb639dd1c7c5fdea12763aa0716c412eb0`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read, _sha, path. Outputs/bindings: (none).
Calls/effect boundaries: _read, _sha.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[2].body[0].body[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[2].body[0].body[0].test.left.args[0]::Call

Source: `infra/agentinfra/transaction.py:279`; AST `1f2f75b93be5f6f124d7aae1d19cc9f78c318b0a8ab019dfd7079ab453b0731c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read, path. Outputs/bindings: (none).
Calls/effect boundaries: _read.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[2].body[0].body[0].test.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[2].body[0].body[0].body[0]::Raise

Source: `infra/agentinfra/transaction.py:280`; AST `47fbd5843c1dbf79b64803d98b2e7e8468cdac0fe384360ae0f7b1468bdb083f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, relative. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[27].body[2].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_preflight_recovery_batch::root.body[27].body[2].body[0].body[0].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:280`; AST `ab984624f47f20642421ee4f35168142939e3fbde28848d8add377268470d54b`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, relative. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[2].body[0].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28]::FunctionDef

Source: `infra/agentinfra/transaction.py:283`; AST `2b0331da5c46029ffdb0116fb7f9ac593b3d8605b17823b3405a58db2c11278f`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _RecoveryPlan, _now, atomic_write_bytes, atomic_write_json, before, dict, durable_unlink, journal, path, plan, record, reversed, root. Outputs/bindings: before, journal, path, record.
Calls/effect boundaries: _now, atomic_write_bytes, atomic_write_json, durable_unlink, record.get, reversed.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[28]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[0]::Assign

Source: `infra/agentinfra/transaction.py:284`; AST `030589f2764a5781bf22b8f3a0c006cef9627b0b82c3b1c4c4e5c84182a46275`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan. Outputs/bindings: journal.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[1]::If

Source: `infra/agentinfra/transaction.py:285`; AST `fc4c4293f5bb42e110443b61d027cf197d6dbb307cd0619bf70d20068ab94a42`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: journal, plan. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[28].body[1]; no call, error or mutation may be omitted. Condition: not plan.rollback
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[1].body[0]::Return

Source: `infra/agentinfra/transaction.py:286`; AST `a7f24192054c43d3f9ec59c1e34e72bd15947d3463104d39b1a7ed707ea679a5`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[28].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2]::For

Source: `infra/agentinfra/transaction.py:287`; AST `056838b9e0684fcf935c38d6682bf0bbaca37dc1294b93972f4864d6a3ae290f`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: atomic_write_bytes, before, durable_unlink, journal, path, plan, record, reversed, root. Outputs/bindings: before, path, record.
Calls/effect boundaries: atomic_write_bytes, durable_unlink, record.get, reversed.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[28].body[2]; no call, error or mutation may be omitted. Iteration: record in reversed(journal['records'])
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2].iter::Call

Source: `infra/agentinfra/transaction.py:287`; AST `b367bdfc3866b0d39664b29c6ec42996c185dcfbafa69ed80a7ceda8868f3628`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal, reversed. Outputs/bindings: (none).
Calls/effect boundaries: reversed.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2].body[0]::Assign

Source: `infra/agentinfra/transaction.py:288`; AST `d179559a1ff82180b030078707d825baeeced233d3a6aac905b215878abbca34`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan, record. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2].body[1]::Assign

Source: `infra/agentinfra/transaction.py:289`; AST `ed42aa7ef1995ee17297c1dc9159996b9284ea6bee42f6f9c80a3302ee48d555`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan, record. Outputs/bindings: before.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2].body[2]::If

Source: `infra/agentinfra/transaction.py:290`; AST `8bc0a89fff2b6a2482d52d5894c376ee09c271d43ef58e7e0cdb038a4ee74f17`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: atomic_write_bytes, before, durable_unlink, path, record, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, durable_unlink, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[28].body[2].body[2]; no call, error or mutation may be omitted. Condition: before is None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2].body[2].body[0]::Expr

Source: `infra/agentinfra/transaction.py:291`; AST `aab53cade8c5006d982f72099912f805ff2c2bd402830e4407481b20babe0cbb`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: durable_unlink, path, root. Outputs/bindings: (none).
Calls/effect boundaries: durable_unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2].body[2].body[0].value::Call

Source: `infra/agentinfra/transaction.py:291`; AST `2394127256b24ede9dc68c370a6b460574abb8c99691fdee91f2df2b6dfddb0b`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: durable_unlink, path, root. Outputs/bindings: (none).
Calls/effect boundaries: durable_unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[2].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2].body[2].orelse[0]::Expr

Source: `infra/agentinfra/transaction.py:293`; AST `5a2ab2285e9a1553e041deea8aa271af3c715b438ac5026aec30f315cb00d9ab`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_bytes, before, path, record, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[2].body[2].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2].body[2].orelse[0].value::Call

Source: `infra/agentinfra/transaction.py:293`; AST `e6aa6daff108013595f7252a8b097649eb737aa8d6d12b9b1c28be6f39ee9838`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_bytes, before, path, record, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[2].body[2].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[2].body[2].orelse[0].value.keywords[1].value::Call

Source: `infra/agentinfra/transaction.py:297`; AST `a8e6c119e6a626a4dc381f7a7ab4f76344322672cd762d7606abe35789bb839d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[2].body[2].orelse[0].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[3]::Assign

Source: `infra/agentinfra/transaction.py:299`; AST `5f0a703a1ceab90178f61f2499443a4dab157178f149e7c0b59d3d7254be1d97`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[4]::Assign

Source: `infra/agentinfra/transaction.py:300`; AST `b90967c364240f40930569a76c8e9d894a1a29e1e73a102a946c6f0bb8d41e9d`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _now, journal. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[4].value::Call

Source: `infra/agentinfra/transaction.py:300`; AST `a45c2ac57befcf1212794e7c42a7aad7870de2198eba961b8d2f47b37f928f0f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[5]::Assign

Source: `infra/agentinfra/transaction.py:301`; AST `efcd4401afd271ce3e07a99a12fa8258b19548cdc5582a6aab420206adfd5c84`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[6]::Expr

Source: `infra/agentinfra/transaction.py:302`; AST `7006bbe88a1886488d4a1c07a93f6dce21e2a91150737e2fdfa9d1ac964043ef`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, journal, plan, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[6].value::Call

Source: `infra/agentinfra/transaction.py:302`; AST `d3f86d9688a09fc971a2c17f132ce788e006a6096eb5c1900b2625da106f0251`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, journal, plan, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_apply_recovery::root.body[28].body[7]::Return

Source: `infra/agentinfra/transaction.py:303`; AST `a7f24192054c43d3f9ec59c1e34e72bd15947d3463104d39b1a7ed707ea679a5`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: journal. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[28].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_transaction::root.body[29]::FunctionDef

Source: `infra/agentinfra/transaction.py:306`; AST `f22a1966b0f53c01cf886fbcdc76a493a1a6c06f575a2256d8c84ef6cf8f338f`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _apply_recovery, _preflight_recovery_batch, _prepare_recovery, bool, dict, expected_root, force_rollback, journal_path, plan, root. Outputs/bindings: plan, root.
Calls/effect boundaries: _apply_recovery, _preflight_recovery_batch, _prepare_recovery, expected_root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[29]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_transaction::root.body[29].body[0]::Assign

Source: `infra/agentinfra/transaction.py:307`; AST `842e88f3c779d57165dfa9081fbe4277a76c251e9aa2b717733267c8bfa28b6f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected_root. Outputs/bindings: root.
Calls/effect boundaries: expected_root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[29].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_transaction::root.body[29].body[0].value::Call

Source: `infra/agentinfra/transaction.py:307`; AST `fb6ef22fdb74dc3c57363b53033446b9a9fd3f8ef8437a925f05d8c21ff1aa1d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected_root. Outputs/bindings: (none).
Calls/effect boundaries: expected_root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[29].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_transaction::root.body[29].body[1]::Assign

Source: `infra/agentinfra/transaction.py:308`; AST `53ec75a2692a5178e8647b2c87ba5e799c6f53cc6a15f3b86bfb8d9d075e03c7`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _prepare_recovery, force_rollback, journal_path, root. Outputs/bindings: plan.
Calls/effect boundaries: _prepare_recovery.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[29].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_transaction::root.body[29].body[1].value::Call

Source: `infra/agentinfra/transaction.py:308`; AST `ed717c553ec665f7acc5e0c0c37919823bcdfc9c2e165288dea3fbd5c0cd206f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _prepare_recovery, force_rollback, journal_path, root. Outputs/bindings: (none).
Calls/effect boundaries: _prepare_recovery.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[29].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_transaction::root.body[29].body[2]::Expr

Source: `infra/agentinfra/transaction.py:309`; AST `ad5b18295640da6bc5bcacf1ebc38f4977193c32183a6e5f0ffaf3efcb27b6b7`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _preflight_recovery_batch, plan. Outputs/bindings: (none).
Calls/effect boundaries: _preflight_recovery_batch.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[29].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_transaction::root.body[29].body[2].value::Call

Source: `infra/agentinfra/transaction.py:309`; AST `68bc18643d3bef247895afda8fd66681a27e7163ee2432f728beb89b87b82869`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _preflight_recovery_batch, plan. Outputs/bindings: (none).
Calls/effect boundaries: _preflight_recovery_batch.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[29].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_transaction::root.body[29].body[3]::Return

Source: `infra/agentinfra/transaction.py:310`; AST `e22403fc77e6b98856434329bad7329ff2aebacecf336168956b159746c38030`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _apply_recovery, plan, root. Outputs/bindings: (none).
Calls/effect boundaries: _apply_recovery.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[29].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_transaction::root.body[29].body[3].value::Call

Source: `infra/agentinfra/transaction.py:310`; AST `0b5ae95b08bf1a763dc8ec9f7c35dd24a8b2cfc0e03ccbbc30efd984e2d7a5f7`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _apply_recovery, plan, root. Outputs/bindings: (none).
Calls/effect boundaries: _apply_recovery.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[29].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30]::FunctionDef

Source: `infra/agentinfra/transaction.py:313`; AST `365dfc34d849d835f03f56356a987d3d7d35b3592f87cc527688e635c060913e`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, Path, TransactionError, _apply_recovery, _preflight_recovery_batch, _prepare_recovery, _read_recovery_journal, any, bool, candidates, dict, directory, durable_unlink, exc, item, journal_path, list, names, path, plan, plans, preview, recovered, remove_recovered, root, set, sorted, state_dir, str, tuple. Outputs/bindings: _, candidates, directory, journal_path, path, plan, plans, preview, recovered.
Calls/effect boundaries: TransactionError, _apply_recovery, _preflight_recovery_batch, _prepare_recovery, _read_recovery_journal, any, candidates.append, directory.is_dir, directory.is_symlink, directory.iterdir, directory.rmdir, durable_unlink, journal_path.is_file, journal_path.is_symlink, preview.get, sorted, state_dir.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[30]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[0]::AnnAssign

Source: `infra/agentinfra/transaction.py:320`; AST `73492a5f7d06008bc584a0ac6d2bc180343b3752f5a9e82b8f355f276db8dd0e`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, dict, list, tuple. Outputs/bindings: candidates.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[30].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1]::For

Source: `infra/agentinfra/transaction.py:321`; AST `04f769259901b676c1e955dd746ed0a26ec3976ed36502a82d1c48c6aae20320`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: TransactionError, _read_recovery_journal, any, candidates, directory, item, journal_path, names, path, preview, remove_recovered, sorted, state_dir. Outputs/bindings: directory, journal_path, path, preview.
Calls/effect boundaries: TransactionError, _read_recovery_journal, any, candidates.append, directory.is_dir, directory.is_symlink, directory.iterdir, journal_path.is_file, journal_path.is_symlink, preview.get, sorted, state_dir.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[30].body[1]; no call, error or mutation may be omitted. Iteration: directory in sorted(state_dir.iterdir(), key=lambda item: item.name)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].iter::Call

Source: `infra/agentinfra/transaction.py:321`; AST `6b3fdcd618c812a46a00d519d890d3361b667cb78f6fe3a2ed29080d4e97625d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, sorted, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: sorted, state_dir.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].iter.args[0]::Call

Source: `infra/agentinfra/transaction.py:321`; AST `f1a196640bb43cbd9885c560590d0095badc62f8ecca644abb264e645fe2bb78`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state_dir. Outputs/bindings: (none).
Calls/effect boundaries: state_dir.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].iter.keywords[0].value::Lambda

Source: `infra/agentinfra/transaction.py:321`; AST `e7b222ffcc49b7b8bb922c256d4035311335ade5a81b682409e52489a3691a67`.

Rust module: `infra::agentinfra::transaction`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Lambda evaluation at root.body[30].body[1].iter.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[0]::If

Source: `infra/agentinfra/transaction.py:322`; AST `ef3d6a0dbec3873b9b403d7cee72732908405390d65a2a30aba70253d4101735`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.is_dir, directory.is_symlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[30].body[1].body[0]; no call, error or mutation may be omitted. Condition: not directory.is_dir() or directory.is_symlink()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/transaction.py:322`; AST `e09b891583ec6b6bcaff90dfee50a8e4fe5cce8cf1cf3038629362fb9506070f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.is_dir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[0].test.values[1]::Call

Source: `infra/agentinfra/transaction.py:322`; AST `e90e39c3e33727737a6d73a5317b04292741306577c75f8221b92fa37988c585`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.is_symlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[0].body[0]::Continue

Source: `infra/agentinfra/transaction.py:323`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Continue evaluation at root.body[30].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[1]::Assign

Source: `infra/agentinfra/transaction.py:324`; AST `c22cc6f60837f92971ccdfd662f2b3f15c5a064dd9f738d367ee050d827acac2`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: journal_path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[30].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[2]::If

Source: `infra/agentinfra/transaction.py:325`; AST `f344d0102abf2de6e245fbc027515b63d862601eb155ad13782e9e0ceee9eed7`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, directory, journal_path. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, journal_path.is_file, journal_path.is_symlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[30].body[1].body[2]; no call, error or mutation may be omitted. Condition: not journal_path.is_file() or journal_path.is_symlink()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[2].test.values[0].operand::Call

Source: `infra/agentinfra/transaction.py:325`; AST `ab0c8a3fe4a46465ac881d77821a159101948b39756a9bab6c5ee9dd7f5162e1`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path. Outputs/bindings: (none).
Calls/effect boundaries: journal_path.is_file.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[2].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[2].test.values[1]::Call

Source: `infra/agentinfra/transaction.py:325`; AST `ebd371260f4fc963096a86f0e0ef3645d3fa294b3ec1d3c13d79034aea93f313`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: journal_path. Outputs/bindings: (none).
Calls/effect boundaries: journal_path.is_symlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[2].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[2].body[0]::Raise

Source: `infra/agentinfra/transaction.py:326`; AST `d18a0e46353f56a718e6623d6ffb2b77570957b6e7218a65a627b6a6a5832c63`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, directory. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[30].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[2].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:326`; AST `2e884defe54e6768a27ce7cea1df5863478839b82111ee15d2cd8a83c46afe25`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, directory. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[3]::Assign

Source: `infra/agentinfra/transaction.py:327`; AST `2eb9b24ef7c0849704acfa94718c2df94fef968cfa515a9e8a6216e0f57ec9f2`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _read_recovery_journal, journal_path. Outputs/bindings: preview.
Calls/effect boundaries: _read_recovery_journal.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[30].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[3].value::Call

Source: `infra/agentinfra/transaction.py:327`; AST `c8903d2ab060fbb22c76e470db2e8bbc7dbceef3cd440e57d200efcb4ce641bc`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read_recovery_journal, journal_path. Outputs/bindings: (none).
Calls/effect boundaries: _read_recovery_journal.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[4]::If

Source: `infra/agentinfra/transaction.py:328`; AST `6b2e068c70da0e1675dff13c553adac879dcf8783bbcffc3f586be68db3013cc`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: names, preview. Outputs/bindings: (none).
Calls/effect boundaries: preview.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[30].body[1].body[4]; no call, error or mutation may be omitted. Condition: names is not None and preview.get('name') not in names
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[4].test.values[1].left::Call

Source: `infra/agentinfra/transaction.py:328`; AST `e75e2bc5f0c1c7964ddf7a04d0cb35de2faacb86d7928b43b6ff1219812ddeb9`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: preview. Outputs/bindings: (none).
Calls/effect boundaries: preview.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[4].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[4].body[0]::Continue

Source: `infra/agentinfra/transaction.py:329`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Continue evaluation at root.body[30].body[1].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[5]::If

Source: `infra/agentinfra/transaction.py:330`; AST `d300b27b732a085b7e42173ce1c4746d8641f518066b7b27b805c7595bb37aa0`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TransactionError, any, directory, journal_path, path, remove_recovered. Outputs/bindings: path.
Calls/effect boundaries: TransactionError, any, directory.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[30].body[1].body[5]; no call, error or mutation may be omitted. Condition: remove_recovered and any((path != journal_path for path in directory.iterdir()))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[5].test.values[1]::Call

Source: `infra/agentinfra/transaction.py:330`; AST `e98860c6f4824e903e54fb69917a00d7b5bd5ebb3f8417ef4c36829b95b4c91e`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, directory, journal_path, path. Outputs/bindings: path.
Calls/effect boundaries: any, directory.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[5].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[5].test.values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/transaction.py:330`; AST `d5a21f75193bf783c2bc885c42ba3c0db48425e84fb0cdd331168b43452611c8`.

Rust module: `infra::agentinfra::transaction`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: directory, journal_path, path. Outputs/bindings: path.
Calls/effect boundaries: directory.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[30].body[1].body[5].test.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[5].test.values[1].args[0].generators[0].iter::Call

Source: `infra/agentinfra/transaction.py:330`; AST `2fe0a2d72ade179d3553e4e50c13b9ca8f1fde55e65031a1e384f826229c5e36`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.iterdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[5].test.values[1].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[5].body[0]::Raise

Source: `infra/agentinfra/transaction.py:331`; AST `9fd4181b75eaad7ab27d3f04e141ca950c05dd2a519d2fc5613be7f63cc811a1`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, directory. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[30].body[1].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[5].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:331`; AST `ed7978b56b2aa9aac5ae678bfa50b505c0a130c2bcb488142c505f1d17f4cd2a`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, directory. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[5].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[6]::Expr

Source: `infra/agentinfra/transaction.py:332`; AST `08b3d3265bc454fc3477ceacde046661273aec1d295f055b5d8654c1e5b1dfaa`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidates, directory, journal_path, preview. Outputs/bindings: (none).
Calls/effect boundaries: candidates.append.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[30].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[1].body[6].value::Call

Source: `infra/agentinfra/transaction.py:332`; AST `e272407ed157578149792779fdd95dbe26cff1aab87adbc577706565d1ac031c`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidates, directory, journal_path, preview. Outputs/bindings: (none).
Calls/effect boundaries: candidates.append.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[1].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[2]::Assign

Source: `infra/agentinfra/transaction.py:334`; AST `916d600b55225fac821789e6893cd3c42820baad4b73115bc8965dda4fe82ebe`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _prepare_recovery, candidates, journal_path, preview, root. Outputs/bindings: _, journal_path, plans, preview.
Calls/effect boundaries: _prepare_recovery, preview.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[30].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[2].value::ListComp

Source: `infra/agentinfra/transaction.py:334`; AST `55f594043723bafad7a2dcb4954e6e90ac0695d148c6d12c1a9e09f3e57316af`.

Rust module: `infra::agentinfra::transaction`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _prepare_recovery, candidates, journal_path, preview, root. Outputs/bindings: _, journal_path, preview.
Calls/effect boundaries: _prepare_recovery, preview.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ListComp evaluation at root.body[30].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[2].value.elt::Call

Source: `infra/agentinfra/transaction.py:335`; AST `aa9e42cac9aa5c150f8419a2da3fe830af2f0df5e0fc7ec9d8728d4852b6d0f0`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _prepare_recovery, journal_path, preview, root. Outputs/bindings: (none).
Calls/effect boundaries: _prepare_recovery, preview.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[2].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[2].value.elt.keywords[1].value.left::Call

Source: `infra/agentinfra/transaction.py:338`; AST `518e371203358e8f77f1e5ac3c0759e78e5890860fbf548eaf47acdae8e302ae`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: preview. Outputs/bindings: (none).
Calls/effect boundaries: preview.get.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[2].value.elt.keywords[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[3]::Expr

Source: `infra/agentinfra/transaction.py:346`; AST `7fb1703ee71da23006feb331d3b300ab9daa3665815d8585899e1b0e5436b400`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _preflight_recovery_batch, plans. Outputs/bindings: (none).
Calls/effect boundaries: _preflight_recovery_batch.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[30].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[3].value::Call

Source: `infra/agentinfra/transaction.py:346`; AST `73295fbc02e3cefe5afe5c6ab96144b83bae92c268f37926882616633295b685`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _preflight_recovery_batch, plans. Outputs/bindings: (none).
Calls/effect boundaries: _preflight_recovery_batch.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[4]::Assign

Source: `infra/agentinfra/transaction.py:347`; AST `8d78754ce079bd2945fe83f8f5d775628baf0f42133b935404518a02e10b24f2`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _apply_recovery, plan, plans, root. Outputs/bindings: plan, recovered.
Calls/effect boundaries: _apply_recovery.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[30].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[4].value::ListComp

Source: `infra/agentinfra/transaction.py:347`; AST `a1da68e77119378d04662ffa4be9c368ca2e12d6fa5c637d0384c5e20306d356`.

Rust module: `infra::agentinfra::transaction`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _apply_recovery, plan, plans, root. Outputs/bindings: plan.
Calls/effect boundaries: _apply_recovery.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ListComp evaluation at root.body[30].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[4].value.elt::Call

Source: `infra/agentinfra/transaction.py:347`; AST `0b5ae95b08bf1a763dc8ec9f7c35dd24a8b2cfc0e03ccbbc30efd984e2d7a5f7`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _apply_recovery, plan, root. Outputs/bindings: (none).
Calls/effect boundaries: _apply_recovery.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[4].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5]::If

Source: `infra/agentinfra/transaction.py:348`; AST `bdcc1e2838dcf8140e4192e86462f4f88ac43081ee347f67923da8b1640cfc7a`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: OSError, TransactionError, candidates, directory, durable_unlink, exc, journal_path, remove_recovered, root. Outputs/bindings: _, directory, journal_path.
Calls/effect boundaries: TransactionError, directory.rmdir, durable_unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[30].body[5]; no call, error or mutation may be omitted. Condition: remove_recovered
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5].body[0]::For

Source: `infra/agentinfra/transaction.py:349`; AST `c7953b6d99a88b07b36078bfa3068c85f57291b6c8c72b1701b2e7a714ce9f7b`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: OSError, TransactionError, candidates, directory, durable_unlink, exc, journal_path, root. Outputs/bindings: _, directory, journal_path.
Calls/effect boundaries: TransactionError, directory.rmdir, durable_unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[30].body[5].body[0]; no call, error or mutation may be omitted. Iteration: (directory, journal_path, _) in candidates
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5].body[0].body[0]::Expr

Source: `infra/agentinfra/transaction.py:350`; AST `b0dc20eae8fa01b384596c2a357a2672440563a66191c10294b4a07f73b380e1`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: durable_unlink, journal_path, root. Outputs/bindings: (none).
Calls/effect boundaries: durable_unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[30].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5].body[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:350`; AST `509b55b830ba4c6cca056d76754e99e18abfa5b9fa16b9f0d4b907b37b1f10d2`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: durable_unlink, journal_path, root. Outputs/bindings: (none).
Calls/effect boundaries: durable_unlink.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5].body[0].body[1]::Try

Source: `infra/agentinfra/transaction.py:351`; AST `1e351049c06fe13fc924bdf6ea75407e519038796276d9bc4f5372da0dbfe30b`.

Rust module: `infra::agentinfra::transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, TransactionError, directory, exc. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError, directory.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[30].body[5].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5].body[0].body[1].body[0]::Expr

Source: `infra/agentinfra/transaction.py:352`; AST `d20ac790a8ac3f27d0831ef41ca90e7a800233d0cbcd0f26c1807cfc7cabdcdb`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[30].body[5].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5].body[0].body[1].body[0].value::Call

Source: `infra/agentinfra/transaction.py:352`; AST `f52432c45c0d10b74560c0c46f78e855f641ee647aef7316fdd048440cf6795f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.rmdir.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[5].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5].body[0].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/transaction.py:353`; AST `1055266b5539e8fa6e8b580ced3c478ca26512429c30c9e9284834f0b193d390`.

Rust module: `infra::agentinfra::transaction`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError, TransactionError, directory, exc. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[30].body[5].body[0].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5].body[0].body[1].handlers[0].body[0]::Raise

Source: `infra/agentinfra/transaction.py:354`; AST `db8b21c7666049ac6e87875e4875345915d6e678c6e27d0f1d61d67d784059f0`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TransactionError, directory, exc. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[30].body[5].body[0].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[5].body[0].body[1].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:354`; AST `ed7978b56b2aa9aac5ae678bfa50b505c0a130c2bcb488142c505f1d17f4cd2a`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TransactionError, directory. Outputs/bindings: (none).
Calls/effect boundaries: TransactionError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[30].body[5].body[0].body[1].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::_recover_candidates::root.body[30].body[6]::Return

Source: `infra/agentinfra/transaction.py:355`; AST `838ce9d42d2b506fb85caf6ff2fe363a32e65548e7d391a862866f8bde757a03`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recovered. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[30].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31]::FunctionDef

Source: `infra/agentinfra/transaction.py:358`; AST `2f1c82d6ef08e2c018c9dcffa82d30a378e7c7f2735e07c1a0783b0010d6a881`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _recover_candidates, bool, confined_path, dict, expected_root, list, name, remove_recovered, root, state_dir, str. Outputs/bindings: root, state_dir.
Calls/effect boundaries: _recover_candidates, confined_path, expected_root.resolve, state_dir.exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[31]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[0]::Expr

Source: `infra/agentinfra/transaction.py:365`; AST `c1f55a952795a0a884d3a21a8ab4f27d96f8e77eb1b972c8259c521f2df4a147`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[31].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[1]::Assign

Source: `infra/agentinfra/transaction.py:370`; AST `842e88f3c779d57165dfa9081fbe4277a76c251e9aa2b717733267c8bfa28b6f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected_root. Outputs/bindings: root.
Calls/effect boundaries: expected_root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[31].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[1].value::Call

Source: `infra/agentinfra/transaction.py:370`; AST `fb6ef22fdb74dc3c57363b53033446b9a9fd3f8ef8437a925f05d8c21ff1aa1d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected_root. Outputs/bindings: (none).
Calls/effect boundaries: expected_root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[31].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[2]::Assign

Source: `infra/agentinfra/transaction.py:371`; AST `0acb3f2edfca38c3b8e1bafad259cea7e25c9e8d1ffed183e7dd874aa8b0da2c`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, root, state_dir. Outputs/bindings: state_dir.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[31].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[2].value::Call

Source: `infra/agentinfra/transaction.py:371`; AST `b322b57e109ff05f8456785c2379f2566e9939b0f99617c64c477a0e44e5deb3`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[31].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[3]::If

Source: `infra/agentinfra/transaction.py:372`; AST `b4e25eb6eb0ec0d48b67c3f52e389d90e7fdb1fb2e3d13b2bc21fd9a7b0e33c0`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: state_dir. Outputs/bindings: (none).
Calls/effect boundaries: state_dir.exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[31].body[3]; no call, error or mutation may be omitted. Condition: not state_dir.exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[3].test.operand::Call

Source: `infra/agentinfra/transaction.py:372`; AST `4f3fc52af5b18b100ef641674bae8b506d06e7690f2010c2783d57f10585021f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state_dir. Outputs/bindings: (none).
Calls/effect boundaries: state_dir.exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[31].body[3].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[3].body[0]::Return

Source: `infra/agentinfra/transaction.py:373`; AST `b98d3492e7d9cf3ad08a6755e4ee962ff6b89d6d238688050439ce1c9205f710`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[31].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[4]::Return

Source: `infra/agentinfra/transaction.py:374`; AST `2c909eaa72213cd3b8e68f063fdf2a63b516bcbd97477910e93189b9b404efea`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _recover_candidates, name, remove_recovered, root, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: _recover_candidates.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[31].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_pending_transactions::root.body[31].body[4].value::Call

Source: `infra/agentinfra/transaction.py:374`; AST `dc424567b4fad16a99f7515356e68ef3f560b748cf6b60a72171b2030a4e7c35`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _recover_candidates, name, remove_recovered, root, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: _recover_candidates.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[31].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32]::FunctionDef

Source: `infra/agentinfra/transaction.py:382`; AST `cede9ef7678eadb2c9c372a85bddc8068e341faea980de5c4a3b638b7413f5bd`.

Rust module: `infra::agentinfra::transaction`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, Iterable, Path, ValueError, _recover_candidates, acquired, confined_path, dict, expected_root, isinstance, list, lock, locks, name, names, reversed, root, selected, set, sorted, state_dir, str. Outputs/bindings: acquired, lock, locks, name, root, selected, state_dir.
Calls/effect boundaries: FileLock, ValueError, _recover_candidates, acquired.append, confined_path, dict.fromkeys, expected_root.resolve, isinstance, list, lock.acquire, lock.release, name.strip, reversed, set, sorted, state_dir.exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[32]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[0]::Expr

Source: `infra/agentinfra/transaction.py:383`; AST `331d667f9925130fa2cf0260ebf13bad8fdb78da40fd3ef08e457320aa28928b`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[32].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[1]::Assign

Source: `infra/agentinfra/transaction.py:384`; AST `842e88f3c779d57165dfa9081fbe4277a76c251e9aa2b717733267c8bfa28b6f`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected_root. Outputs/bindings: root.
Calls/effect boundaries: expected_root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[32].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[1].value::Call

Source: `infra/agentinfra/transaction.py:384`; AST `fb6ef22fdb74dc3c57363b53033446b9a9fd3f8ef8437a925f05d8c21ff1aa1d`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected_root. Outputs/bindings: (none).
Calls/effect boundaries: expected_root.resolve.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[2]::Assign

Source: `infra/agentinfra/transaction.py:385`; AST `0acb3f2edfca38c3b8e1bafad259cea7e25c9e8d1ffed183e7dd874aa8b0da2c`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, root, state_dir. Outputs/bindings: state_dir.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[32].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[2].value::Call

Source: `infra/agentinfra/transaction.py:385`; AST `b322b57e109ff05f8456785c2379f2566e9939b0f99617c64c477a0e44e5deb3`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[3]::If

Source: `infra/agentinfra/transaction.py:386`; AST `b4e25eb6eb0ec0d48b67c3f52e389d90e7fdb1fb2e3d13b2bc21fd9a7b0e33c0`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: state_dir. Outputs/bindings: (none).
Calls/effect boundaries: state_dir.exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[32].body[3]; no call, error or mutation may be omitted. Condition: not state_dir.exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[3].test.operand::Call

Source: `infra/agentinfra/transaction.py:386`; AST `4f3fc52af5b18b100ef641674bae8b506d06e7690f2010c2783d57f10585021f`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state_dir. Outputs/bindings: (none).
Calls/effect boundaries: state_dir.exists.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[3].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[3].body[0]::Return

Source: `infra/agentinfra/transaction.py:387`; AST `b98d3492e7d9cf3ad08a6755e4ee962ff6b89d6d238688050439ce1c9205f710`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[32].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[4]::Assign

Source: `infra/agentinfra/transaction.py:388`; AST `dfdd0d851d1b77f27235ab02b2ad39bf5b210a9a634d92f8e54e88feb8c04b43`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, list, names. Outputs/bindings: selected.
Calls/effect boundaries: dict.fromkeys, list.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[32].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[4].value::Call

Source: `infra/agentinfra/transaction.py:388`; AST `09e7499e2216123ac2903d8ae91a5d6265291ed7842c96efee1ebd4d7d132d24`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, list, names. Outputs/bindings: (none).
Calls/effect boundaries: dict.fromkeys, list.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[4].value.args[0]::Call

Source: `infra/agentinfra/transaction.py:388`; AST `b47c5d735f5bb50fed9d7d68461fe123454caeae5a08fc767280eb607b7c91ce`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, names. Outputs/bindings: (none).
Calls/effect boundaries: dict.fromkeys.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[5]::For

Source: `infra/agentinfra/transaction.py:389`; AST `8cd354b887a46fa403f9cec3615452e0f5ee3728c27e01a210a5be4b20fd4d27`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ValueError, isinstance, name, selected, str. Outputs/bindings: name.
Calls/effect boundaries: ValueError, isinstance, name.strip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[32].body[5]; no call, error or mutation may be omitted. Iteration: name in selected
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[5].body[0]::If

Source: `infra/agentinfra/transaction.py:390`; AST `f4fc673e8f2275e45e6464f6aad6c37075f4f78c822412b1185b5fc9e4347b38`.

Rust module: `infra::agentinfra::transaction`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, isinstance, name, str. Outputs/bindings: (none).
Calls/effect boundaries: ValueError, isinstance, name.strip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[32].body[5].body[0]; no call, error or mutation may be omitted. Condition: not isinstance(name, str) or not name.strip()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[5].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/transaction.py:390`; AST `ec1885a68f635e9b05e21bf549ce84222799f1b460b2e2b511d6c9a601fd0627`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, name, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[5].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[5].body[0].test.values[1].operand::Call

Source: `infra/agentinfra/transaction.py:390`; AST `eece2e999f39f90ddfe01061cdcf0ffa084aa0e7c49785ed066148fbcc165539`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.strip.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[5].body[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[5].body[0].body[0]::Raise

Source: `infra/agentinfra/transaction.py:391`; AST `aa58c100ce391d2faf4e634df2d05d715959aaddb3d6af812df8bea5f540aab4`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[32].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[5].body[0].body[0].exc::Call

Source: `infra/agentinfra/transaction.py:391`; AST `8222d82ecfd4df38383494ae2b8bf28b317afcab45d9cf399edbe064a267a0ed`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[5].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[6]::Assign

Source: `infra/agentinfra/transaction.py:392`; AST `40c4d652027b5fa5f83593a4dc14f8330d15f742cfd40d406e7c53fad4e78209`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, name, selected, sorted, state_dir. Outputs/bindings: locks, name.
Calls/effect boundaries: FileLock, sorted.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[32].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[6].value::ListComp

Source: `infra/agentinfra/transaction.py:392`; AST `be83f5e3f8591bb87c8f4aa41db5d66c42bd79efc329b7611c594a882324ee21`.

Rust module: `infra::agentinfra::transaction`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: FileLock, name, selected, sorted, state_dir. Outputs/bindings: name.
Calls/effect boundaries: FileLock, sorted.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered ListComp evaluation at root.body[32].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[6].value.elt::Call

Source: `infra/agentinfra/transaction.py:392`; AST `f54d76b327ca969bd86d3b507cd5333576fbc9ea77e0b963762c19b4c3886b96`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, name, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[6].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[6].value.generators[0].iter::Call

Source: `infra/agentinfra/transaction.py:392`; AST `147f6d5e20829fc9a7dc9eb9ad77f8370cf83e0b48d7af6d1bef8e658bbf78af`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: selected, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[6].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[7]::AnnAssign

Source: `infra/agentinfra/transaction.py:393`; AST `f74a1731a0283ff87d1e37c4c6516ff7be7c5a1f6c94754c1e8568c25f5ba147`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, list. Outputs/bindings: acquired.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[32].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8]::Try

Source: `infra/agentinfra/transaction.py:394`; AST `fc439fdeb5d55a05b9754ae301c9110a95ad87a90e2e0c6673811aa28d5b64b8`.

Rust module: `infra::agentinfra::transaction`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: _recover_candidates, acquired, lock, locks, reversed, root, selected, set, state_dir. Outputs/bindings: lock.
Calls/effect boundaries: _recover_candidates, acquired.append, lock.acquire, lock.release, reversed, set.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[32].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].body[0]::For

Source: `infra/agentinfra/transaction.py:395`; AST `683dfb3ecaf0b3d005a370a3b6adb582c52c17fc3cb38840733e8c253c2c5d34`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: acquired, lock, locks. Outputs/bindings: lock.
Calls/effect boundaries: acquired.append, lock.acquire.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[32].body[8].body[0]; no call, error or mutation may be omitted. Iteration: lock in locks
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].body[0].body[0]::Expr

Source: `infra/agentinfra/transaction.py:396`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[32].body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].body[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:396`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[8].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].body[0].body[1]::Expr

Source: `infra/agentinfra/transaction.py:397`; AST `bf1a3be13db2cb1d9e805ba7dba1284a6c8634a0d21daffa3aab925118a815d1`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: acquired, lock. Outputs/bindings: (none).
Calls/effect boundaries: acquired.append.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[32].body[8].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].body[0].body[1].value::Call

Source: `infra/agentinfra/transaction.py:397`; AST `e7216f689a414ad084265d6da66a7ce46551f94ba4468e327f84bf314e43d48e`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: acquired, lock. Outputs/bindings: (none).
Calls/effect boundaries: acquired.append.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[8].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].body[1]::Return

Source: `infra/agentinfra/transaction.py:398`; AST `6df1e918559429cd544ea95ec5754118992bea582d7ffb2a2ca6962255525699`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _recover_candidates, root, selected, set, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: _recover_candidates, set.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[32].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].body[1].value::Call

Source: `infra/agentinfra/transaction.py:398`; AST `8903be365cb0e5e98031493f1ef3dd93f7d8e5559376beb3c923e6853712c945`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _recover_candidates, root, selected, set, state_dir. Outputs/bindings: (none).
Calls/effect boundaries: _recover_candidates, set.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].body[1].value.keywords[1].value::Call

Source: `infra/agentinfra/transaction.py:401`; AST `e541c2f73caf451c363e9efe74ef3635e9ae7e5d1d4968c9c214a3f907f3a854`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: selected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[8].body[1].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].finalbody[0]::For

Source: `infra/agentinfra/transaction.py:405`; AST `6593aab4663b5f9234786327aa88ee0e3e8dd08e298ad73b061a4140958b4723`.

Rust module: `infra::agentinfra::transaction`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: acquired, lock, reversed. Outputs/bindings: lock.
Calls/effect boundaries: lock.release, reversed.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[32].body[8].finalbody[0]; no call, error or mutation may be omitted. Iteration: lock in reversed(acquired)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].finalbody[0].iter::Call

Source: `infra/agentinfra/transaction.py:405`; AST `7e8c9d066bdc86ba5ade396ff9a52cf314ff196e907db97a6664774fd8dd5259`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: acquired, reversed. Outputs/bindings: (none).
Calls/effect boundaries: reversed.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[8].finalbody[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].finalbody[0].body[0]::Expr

Source: `infra/agentinfra/transaction.py:406`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::transaction`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[32].body[8].finalbody[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/transaction.py::module::recover_named_transactions::root.body[32].body[8].finalbody[0].body[0].value::Call

Source: `infra/agentinfra/transaction.py:406`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::transaction`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, base64, dataclasses, datetime, governance, hashlib, json, locks, os, pathlib, security, stat, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[32].body[8].finalbody[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
