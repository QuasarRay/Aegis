# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 374. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_cli.py::module::root::Module

Source: `infra/agentinfra/roadmap_cli.py:1`; AST `19698442f14bfc92f941ae8a3acb8d7959156cd10b1a637470ef77254e667f61`.

Rust module: `infra::agentinfra::roadmap_cli`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BudgetLedger, ContractError, KeyError, OSError, Path, TimeoutError, TypeError, __doc__, __file__, a, adjudicate_findings, any, argparse, args, argv, atomic_write_json, atomic_write_text, audit, audit_evidence, authority_inventory, authorize, b, bind_goal, bind_plan, c, capabilities, compile_roadmaps, compiled, confined_path, decision, destination, dict, digest, errors, evidence, exc, execute, field, goal_transition, groups, index, int, inventory, json, ledger, len, markdown, name, obligation, output, p, packet, parser, parts, path, print, project_into_record, proof_errors, r, read_json, read_native_goal, reconcile_inventory, reconcile_native_transition, reconcile_original_tests, record, render_packet, request, require, result, retrieve, review, root, run_recipe, save_compiled, save_inventory, shards, source, str, u, units, v, validate_decision, validate_record, validate_skills, value. Outputs/bindings: a, args, audit, b, c, compiled, decision, destination, errors, evidence, field, groups, index, ledger, name, obligation, output, p, parts, path, r, record, request, result, review, root, source, u, units, v, value.
Calls/effect boundaries: BudgetLedger, ContractError, Path, Path(__file__).resolve, a.add_argument, a.milestones.split, a.root.resolve, adjudicate_findings, any, argparse.ArgumentParser, atomic_write_json, atomic_write_text, audit_evidence, authority_inventory, authorize, b.add_parser, bind_goal, bind_plan, c.add_parser, c.add_parser('read-goal').add_argument, capabilities, compile_roadmaps, confined_path, dict, digest, execute, goal_transition, groups.add_parser, groups.add_parser('budget').add_subparsers, groups.add_parser('codex').add_subparsers, groups.add_parser('review').add_subparsers, groups.add_parser('roadmap').add_subparsers, groups.add_parser('verification').add_subparsers, inventory, json.dumps, ledger.observe_usage, ledger.read, len, markdown, p.add_argument, p.add_subparsers, p.exit, p.parse_args, packet, parser, parts.items, path.read_text, print, project_into_record, proof_errors, r.add_parser, r.add_parser('audit').add_argument, r.add_parser('compile').add_argument, read_json, read_native_goal, reconcile_inventory, reconcile_native_transition, reconcile_original_tests, render_packet, request.get, require, result.get, retrieve, run_recipe, save_compiled, save_inventory, shards, source['path'].replace, str, v.add_parser, validate_decision, validate_record, validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_cli.py:1`; AST `e1cd1ae1a395650fac8cec9d0ee41c63fbf9ba359b88624b5fe0221a665623f0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_cli.py:4`; AST `356e6775028bc09e699d8b986887aaebc5e3e8e414a507fe911e3ba7da1264d9`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_cli.py:5`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:8`; AST `4579a70ea8cbb8754303c4b21d9fa5790c234874c5c8ce34e4bd98dc98ed51e8`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:9`; AST `a16d9c4e2d7e924dd84d61ee969634818b5dd15b3204d9e58e4d407281e3886a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:10`; AST `177a85fb8347e839df14ef8a0afd58d40679e4082ebc486a7d73752bbac99917`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:11`; AST `300d7f64a8bc8e891a6502099eedae00b8da1765a43dc6b001cc12efb7686d6a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:12`; AST `343f057ae45999299056c83e4e9b51b4379abae3632dc3fed9e510bc98dd9da7`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[10]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:13`; AST `ac0c88ff16ae1805e31b1582ec7076cc5013697989d05beddb25f9f38bac9665`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[11]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:14`; AST `ab9e98b74a0e053e110f461ce9708af2d9640306864315f7d3eff0795dbd6900`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[12]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:15`; AST `e8972c456f907fdd3f9b4f5698403697075598f41a2b7e3a020ec5499428cd6f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[13]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:16`; AST `7da1477e1c152e4e0a2fb91d010039d8028b7a1299fe7a712b56c83e8e3462ca`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[14]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:17`; AST `cf946f2b6f9a446883f9e97c16c32abd8f4b2d9a578fc137636511f6383720df`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[15]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:18`; AST `f66cfce668ebcfb5d201a4340b28f6b073fb342c318f8eb73e98209884374c07`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[16]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:19`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17]::FunctionDef

Source: `infra/agentinfra/roadmap_cli.py:22`; AST `d7361f1d70cfa700766a16dc8d1a66f473570ebed921f1004b4d9106b15b53fd`.

Rust module: `infra::agentinfra::roadmap_cli`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, __doc__, __file__, a, argparse, b, c, groups, int, p, r, v. Outputs/bindings: a, b, c, groups, p, r, v.
Calls/effect boundaries: Path, Path(__file__).resolve, a.add_argument, argparse.ArgumentParser, b.add_parser, c.add_parser, c.add_parser('read-goal').add_argument, groups.add_parser, groups.add_parser('budget').add_subparsers, groups.add_parser('codex').add_subparsers, groups.add_parser('review').add_subparsers, groups.add_parser('roadmap').add_subparsers, groups.add_parser('verification').add_subparsers, p.add_argument, p.add_subparsers, r.add_parser, r.add_parser('audit').add_argument, r.add_parser('compile').add_argument, v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:23`; AST `762667c972fb286c0192232e5854a3e820a82233b313373f35aa5309e577c1bc`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: __doc__, argparse. Outputs/bindings: p.
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:23`; AST `d39f39ff7d74d107a287f654b8e1af65d84cce415404e0fd0bba007cadaa9678`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: __doc__, argparse. Outputs/bindings: (none).
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[1]::Expr

Source: `infra/agentinfra/roadmap_cli.py:24`; AST `5e352c2e646e54897ce8d61da0bd9b7d0b87d41475a11e3b64ebbf1063d38b83`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, p. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, p.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:24`; AST `5da6e9cc72817b9a192d9bfbadac445ca27fa5d2cd2b2b02f290b6f2cd58a6f9`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, p. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, p.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[1].value.keywords[1].value.value.value::Call

Source: `infra/agentinfra/roadmap_cli.py:24`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value.keywords[1].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[1].value.keywords[1].value.value.value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:24`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value.keywords[1].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[2]::Assign

Source: `infra/agentinfra/roadmap_cli.py:25`; AST `856499fa778c34b27c8b6f2e21f60a3cadbce7891dc908abadbf898719c06a3d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p. Outputs/bindings: groups.
Calls/effect boundaries: p.add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[2].value::Call

Source: `infra/agentinfra/roadmap_cli.py:25`; AST `4351d59ec5b072d4848a94776321908359fc3bef1cae5221fd4d0419461cc91a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[3]::Assign

Source: `infra/agentinfra/roadmap_cli.py:26`; AST `f6f4873a2d79beaa1e0689530f612b5e0b7608ec6820f91aa5d284bd2947b9c8`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: r.
Calls/effect boundaries: groups.add_parser, groups.add_parser('roadmap').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[3].value::Call

Source: `infra/agentinfra/roadmap_cli.py:26`; AST `bf1a69ee94f63509c92c4ddaf4a409ccadd053391a9cf3fcc76ae2c621a267b8`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('roadmap').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:26`; AST `92bd4be1f871e64f3b231006cf2748a057d6db368711b6fcb5838917bf1da1d2`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[4]::Expr

Source: `infra/agentinfra/roadmap_cli.py:27`; AST `950e026ee6e73b5028e81f04ab3e95af394824f72d0066d16f066fee905e7861`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('compile').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[4].value::Call

Source: `infra/agentinfra/roadmap_cli.py:27`; AST `06852dbd5b542a43495c8f9db43d2b79f09e45472f7d7bfb2f07041454765501`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('compile').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[4].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:27`; AST `0b9f187e08fdf4f2c57fc155f24eeb64de153bd38e4f0f5d8367c8e675fe6962`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[5]::Expr

Source: `infra/agentinfra/roadmap_cli.py:28`; AST `8fb8cc6dadac5eed504fd56be16284c90fdaeaede39b7f33840d2584aebb4fcc`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('audit').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[5].value::Call

Source: `infra/agentinfra/roadmap_cli.py:28`; AST `8abc9763bd166cdc94da8cd836a5e73581ddefa861aca0c6b726889840f4804c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('audit').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[5].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:28`; AST `929859d84bd1d6bfb53dd2da54b56e25445b9c3de2b636974828ce593cc40d4c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[6]::Assign

Source: `infra/agentinfra/roadmap_cli.py:29`; AST `22d979e159529f0f1bcb4f217c643751d985de7b9596b7fc9e5147502f7af9c3`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[6].value::Call

Source: `infra/agentinfra/roadmap_cli.py:29`; AST `bd6fc3360cf8d1d1f7ab06dd7223a7531bb2d2b17634659ffa2c2ac3d093e189`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[7]::Expr

Source: `infra/agentinfra/roadmap_cli.py:29`; AST `2af01447d3e309b3fbdb72b8307d0aeca8aa14e58b263a6d1842c7bd5388429e`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[7].value::Call

Source: `infra/agentinfra/roadmap_cli.py:29`; AST `8f00e756ef7d65949ba6c4549e55b30c05f6771c3cd015ff588fc517e7194e5c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[8]::Expr

Source: `infra/agentinfra/roadmap_cli.py:29`; AST `6cd3dae08fb3d71f72d1d91f230a71b90ae54ea9204989eef837e5c43b9ed75f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[8].value::Call

Source: `infra/agentinfra/roadmap_cli.py:29`; AST `ec44701bf79e9ec6841cbbadae14baebaef5661c113e8c1b06ace8502d0b2b12`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[9]::Assign

Source: `infra/agentinfra/roadmap_cli.py:30`; AST `d5b51a8be1705c6007de0f1fdbf301594f18dd7b2c3b5a0ef793deb136315b01`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[9].value::Call

Source: `infra/agentinfra/roadmap_cli.py:30`; AST `f956a197b089a2123fec496645189a61d736c1db93d4a2c7eab4af5f4eedb41b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[10]::Expr

Source: `infra/agentinfra/roadmap_cli.py:30`; AST `3d0486ff88a6f9f6e1dcde487c67988bed45d1358b9003e3b5aaf0a838a07b6b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[10].value::Call

Source: `infra/agentinfra/roadmap_cli.py:30`; AST `3228d4014d06ad1ffec0d17e434cf21a03ebb971b2b36f5dd30aa884dfce4c71`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[11]::Expr

Source: `infra/agentinfra/roadmap_cli.py:30`; AST `03984ef88a8dd602845af017c489cc36790de3cf0cfd4d330cd2025b9aa65919`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[11].value::Call

Source: `infra/agentinfra/roadmap_cli.py:30`; AST `abc211af0c5ab445e488423d23cbdc4b082e277822d07332c7e4802d70f377c7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[12]::Assign

Source: `infra/agentinfra/roadmap_cli.py:31`; AST `3945683aae44e77e8af4af3ad34ee3ac1d8777ac632891b0db32ad239c58b090`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[12].value::Call

Source: `infra/agentinfra/roadmap_cli.py:31`; AST `a24ee11b768cd79037964a4438ecf82a74e31c9223be6df7b96fb813c216ee27`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[13]::Expr

Source: `infra/agentinfra/roadmap_cli.py:31`; AST `7dce0795c7e6dd95d825de79692e5acb237454821ed836368824370080f6575f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[13].value::Call

Source: `infra/agentinfra/roadmap_cli.py:31`; AST `a775df190be8c5ed7ab113e7549218db03a8321546b14edb7fb64c95e40a7997`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[14]::Assign

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `d46cf1d12b1af188312a81a5e2155d4d7f2e54a81cbb5bcc9e4de1de1cb58c99`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[14].value::Call

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `031a3b5d3a3ea2ac2c18d7752d9e293386210b3ba20a259027e727b5871cc153`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[15]::Expr

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `63430588b005dd401236630998e83a454a69836f24a22dde3eb05a5fb66d471d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[15].value::Call

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `ff897d116f75f8992c76f006f163021570e79dc9eba91992fea14d386ef58462`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[16]::Expr

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `bda24c2b7c450451608cbcce26780431a49325063ba59b13b1608f5f0aa67c31`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[16].value::Call

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `2690f90d4a64211301762d0707a73563a49d0965a9fca7c72ac465bcc8be9510`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[17]::Expr

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `d7eb3e15f38f30286b80020bb2a08d65a7e75b5e32893fab8bcd5ace95f1dad6`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[17].value::Call

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `0737dc24177da7bc02e079c89728120266f5324b422afee7d13c669d8c1d9e4b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[18]::Assign

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `6c764de193826fe7a95c3337010aed460dee9e2bf7b6acbaf69c9b6ff8d68927`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[18].value::Call

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `0be5fa693a187288b2d71c58989615b2e5a0eee8c0925cae5554252a7b4e86c5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[19]::Expr

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `e3bf4661078c7f87c12b5dd92f70c61fb3cc8073e6fd088c71b8053a8474b6d7`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[19].value::Call

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `f497d0d2312b12f0f32fb1bdeaab42e0e9c46545168a7738bdff9989767e74c4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[20]::Expr

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `eaf5f957214a8d1af9687eaf932ec23ea36d1bb3793b3206509247d8dfc5bf90`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[20]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[20].value::Call

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `e8c6bf82b47e6c36a39f63171cc4dccaa9a810d546815ef486682bbc59a9e0e4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[21]::Expr

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `6bc000dd6b872633d35140708daad5c6372a919b52d4aa5b1c588dfbe8ef74cc`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[21].value::Call

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `d87ab632fb02b68ea48087a425757cbc0cb332903a0f3969f0fb2a3e440bf857`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[22]::Assign

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `764a8e5962e08ae964b525635c9686004f60743eb961ed737f81c221108c23e9`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: a.
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[22]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[22].value::Call

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `723674b65100f7583af2b0149ae9a0666154946fa3698e626c20458bb1509737`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[23]::Expr

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `ef8a5ec404f3b7b62c1658939c6af4dd5b62b4995bdd815b0a590c7d75cb2cac`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[23]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[23].value::Call

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `c45ad4c42d166fbb29668421bc072023b18df0e6c8d4fc6cceb0b21e73774282`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[23].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[24]::Expr

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `c4f842a8c103a30e25972e348908b87879772e85bf5970f812ff8bde440c44f6`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[24]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[24].value::Call

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `b6088a505e65cd6b4e3753b0eba9411ed0e5f1ec51e2ffd75d0c161064f93a7c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[24].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[25]::Expr

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `8c0859270f7c24a4db3ad7c500970156dda38f3c3965c3c1649a586f65e5921c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[25]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[25].value::Call

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `921985407210d4279bdf25f9311b5ce8f3806ea90f60d8248a17d8fbe52e34c9`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[25].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[26]::Assign

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `a4a01e2e98ccf1b812b794269f42ca1b8753dcf59df1e18353ad0b3b32fc5243`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: c.
Calls/effect boundaries: groups.add_parser, groups.add_parser('codex').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[26]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[26].value::Call

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `bbe70fa476fdcc70f780367dd50f4e8da1b3fd1840f711490e77f1ff4c29b582`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('codex').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[26].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[26].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `e4c4f7fa1d3d8f2218821782d254c78d0e15ad3fe1308cda6efcdd0e7b771df5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[26].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[27]::Expr

Source: `infra/agentinfra/roadmap_cli.py:36`; AST `287e077363dd175f7c4d056ea1e02f448a3e7cbcce0aaabf99662ba69ec087b1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[27]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[27].value::Call

Source: `infra/agentinfra/roadmap_cli.py:36`; AST `fe8db032ff91c4b696c4534987f3c9931ab5df709e01f2420aa63dea8e48b95b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[27].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[28]::Expr

Source: `infra/agentinfra/roadmap_cli.py:37`; AST `79a7d58c70480f663238649815032ce683598a498edc5ffb5f6019011c30a6d9`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser, c.add_parser('read-goal').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[28]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[28].value::Call

Source: `infra/agentinfra/roadmap_cli.py:37`; AST `5f2c2e8d9deab27a3c47ecfc56c993d76de6040630d78d41b5d4072cbe196867`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser, c.add_parser('read-goal').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[28].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[28].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:37`; AST `272af53e82adb4cf28e95ef2130c57ac6dceb176c592084bac857dcade512a5a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[28].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[29]::Assign

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `b9a4ebe32ed229cd9bfbb3886a2d90577a0f3d97a4fe779b2e55554603786325`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: a.
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[29]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[29].value::Call

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `19393664434dae5299cfa3d3105081d2709bd925b965e49fa828decef88ae98c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[29].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[30]::Expr

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `e37a4d9aa349c13b27d12a2392421df17990757d2bd592f03b7c43dab683f448`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[30]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[30].value::Call

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `96529487d76d563575ca4fae62fd52a978b89b68ccaeb8936641563459141044`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[30].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[31]::Expr

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `c82940990a3eaefda719781d620b844a060d010693774425cc7408e79478e599`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[31]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[31].value::Call

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `6b09dfa70bdb143f613d12ad71df20d51212bea470c20499b2f915f7ead829b3`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[31].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[32]::Expr

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `71e92d969bc2a96b3d7bee5b5885efdb4685b2badb016029d77d846b5b460b46`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[32]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[32].value::Call

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `2189d4b16c8b0bb3f808bd4d0a741b37c6f8eba5a957592586574f5397dd2760`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[32].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[33]::Expr

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `32a412bdbbe8ae9899ab6f8883f8a310f05512218a9c6f38e763316e433ab705`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[33]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[33].value::Call

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `6106722c7c804d1b5c71a524b6ae77c71a814e74b609a35a319178b0bd112f3a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[33].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[34]::Assign

Source: `infra/agentinfra/roadmap_cli.py:39`; AST `3d5bbba231e2f91c623e2c84a8ad6a4013077edfae441aba83a1dab5ca7881a4`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: a.
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[34]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[34].value::Call

Source: `infra/agentinfra/roadmap_cli.py:39`; AST `0aa3e8eb242378ebe5dad1847bc477c6970c02cbe0c9597befae1c64be07e577`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[34].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[35]::Expr

Source: `infra/agentinfra/roadmap_cli.py:39`; AST `c0d5ee1e30b6205c18610cd6dbf33bfd2f45c3492c768e673fc7c21d3d01d64c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[35]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[35].value::Call

Source: `infra/agentinfra/roadmap_cli.py:39`; AST `3c552efbfebc9cc29748e714ee23f12d46ca9600259029e566fcdbccfe77e048`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[35].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[36]::Expr

Source: `infra/agentinfra/roadmap_cli.py:39`; AST `c2ab40b9dbfd3f50012d6ae1ec9bf0976843b80278107fc6b61a4bc445b1208a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[36]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[36].value::Call

Source: `infra/agentinfra/roadmap_cli.py:39`; AST `f52304d1aad02d069bcbdf8a816810c03283600222e1e911fc0dbbeda00649e5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[36].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[37]::Assign

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `3a159d8709f69f7fc88c900165737ec8eb09435b2069be2f64936921a3d6c4f1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: a.
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[37]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[37].value::Call

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `53abee8bd76449923c5f40cd3f09bbd7ab27c1a734ca2e9ee74a3e680605d687`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[37].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[38]::Expr

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `5b9e6150c43a9c0e52e24b85c4d3853fda3a2f190e332d5271435ec91b316005`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[38]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[38].value::Call

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `8f52639ff87f62d49c908f1769999970c0bcbaa022defd3418f90cd013fae8a0`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[38].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[39]::Expr

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `b425e17ee822af2386aa8d581e5adce32228200c0408f41ce1142d493c68a0b5`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[39]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[39].value::Call

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `89ceccc11a51fc88875f3eba472140b04e7c157486a2c5fa55eb4972c5866b5d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[39].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[40]::Assign

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `842efa54cc7a5f08b52b619d4e576e5bd359a10620dff76d88a971f26640dc5d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: a.
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[40]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[40].value::Call

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `d92bfda9042696f53321d9ef4bd090c2cafb9e6e7dd56e4c9c524888777c1209`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[40].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[41]::Expr

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `fe55ba69edcac54af71da747f370dedb174329188361b57a6d1a4ec7f9b321e0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[41]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[41].value::Call

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `8a87b3d3016576005ef0cfd4a197f8d405b10a93ef5639160cd3bdb6ddce272b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[41].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[42]::Expr

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `a485fbfbc58182583fd3694a58dd82a28fd1dfaa31fae689d80fa02059e5c092`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[42]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[42].value::Call

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `e70ba37c00e188d759ab36d85fa5ebbf87a73bcf2765a878c71961a9f90ab5cb`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[42].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[43]::Expr

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `8d6ba6f7cc09aa62911d0be05059eb6fad8553dfc2e4157f7a9980a1593a86b4`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[43]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[43].value::Call

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `2b7a0000b9ed04baa95397f271511e5f41076f1203dbc4f6498f8bb952b62f93`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[43].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[44]::Expr

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `43d85dab326783c19f03be0e071b24f7144e15c3cc32f370ed52986421a69674`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[44]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[44].value::Call

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `fd49d79bb5807849d8683ee17042036525ee17ad9b8dff7b28b7588bd8be62cb`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[44].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[45]::Assign

Source: `infra/agentinfra/roadmap_cli.py:42`; AST `9ac91b03d8f39868fa366e5663436b77cf33bfe27e1f8bd12b6662ac66328de1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: v.
Calls/effect boundaries: groups.add_parser, groups.add_parser('verification').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[45]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[45].value::Call

Source: `infra/agentinfra/roadmap_cli.py:42`; AST `62c8bd5fdca8515b2a2033c484c6ba785dca5dae05798cfb7169fd13a8daf660`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('verification').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[45].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[45].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:42`; AST `535ea8de47f9f7142c88349bb5786f9889ec58dc6fd206f1ac347058ee8eea2f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[45].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[46]::Assign

Source: `infra/agentinfra/roadmap_cli.py:43`; AST `a1b75be477794363a19277ab398320b98d4547033e0c295d06c830bccb5897a2`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: v. Outputs/bindings: a.
Calls/effect boundaries: v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[46]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[46].value::Call

Source: `infra/agentinfra/roadmap_cli.py:43`; AST `e67efe9cf70347db3754444d8d7e75aaa26ff65056a0ffef3388b603c9164900`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: v. Outputs/bindings: (none).
Calls/effect boundaries: v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[46].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[47]::Expr

Source: `infra/agentinfra/roadmap_cli.py:43`; AST `531b11a9328c0be6c3fe5f15f535b9d8a98a6f3958bfd9f1782d88ae816d12e0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[47]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[47].value::Call

Source: `infra/agentinfra/roadmap_cli.py:43`; AST `925c6cbb6e7cf12e10c0d8c37940b969dcdf6c923fcdcb33566a5f08f4024704`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[47].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[48]::Expr

Source: `infra/agentinfra/roadmap_cli.py:43`; AST `ebfbdda927643885aa1b488d70da44db3b26c878155901cdb758f4c4f05d613e`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[48]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[48].value::Call

Source: `infra/agentinfra/roadmap_cli.py:43`; AST `ec9aecd10fa86e8c00077b24bccd48bc982802bf0916bc853970ce4b71ff23d1`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[48].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[49]::Assign

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `51dc696785a7b7936a593ca4f2612dc2cc3eba2a2596a12ead580c0bae998765`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: v. Outputs/bindings: a.
Calls/effect boundaries: v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[49]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[49].value::Call

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `4080abe0faf2568fc16cc4f6291eddb4c9768f25e250cc2ff1d4da6f3d687399`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: v. Outputs/bindings: (none).
Calls/effect boundaries: v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[49].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[50]::Expr

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `7dce0795c7e6dd95d825de79692e5acb237454821ed836368824370080f6575f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[50]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[50].value::Call

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `a775df190be8c5ed7ab113e7549218db03a8321546b14edb7fb64c95e40a7997`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[50].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[51]::Expr

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `4b1e14ece0982af96c2762959211e3d583884ee2f3b9bebbb88f1b84e47f63fa`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[51]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[51].value::Call

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `002611d0889b889da6b0be651a39aed59e44d474c2ba3e12384292c3e1a02a76`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[51].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[52]::Expr

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `6e2897d3db4e86f9d6f543dd98d505190bb3c8c45d3f3d7cb8123b8088d4c04a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[52]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[52].value::Call

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `459e59eefb8b675c1bb126f8798081f94416cda40ff4392bead9326cadff5b5a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[52].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[53]::Assign

Source: `infra/agentinfra/roadmap_cli.py:45`; AST `735a9ba7a7f611b3f83d8e4774debf82670fc941eb484ecce094336065961be0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: b.
Calls/effect boundaries: groups.add_parser, groups.add_parser('budget').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[53]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[53].value::Call

Source: `infra/agentinfra/roadmap_cli.py:45`; AST `59c27d9e3797d9ee37be152cd5f9c9db71844600d295e9bdf7dcf2fdb8aa94d5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('budget').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[53].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[53].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:45`; AST `2ade4a9d9cce96664c01cbe2fb196b5394d2f05909af8d60282fcdb621e99af7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[53].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[54]::Expr

Source: `infra/agentinfra/roadmap_cli.py:45`; AST `00af5968639af7bd7c3df8916f9044761e023015e49fc86b7fe2fffc5aa7e2d8`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[54]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[54].value::Call

Source: `infra/agentinfra/roadmap_cli.py:45`; AST `e61633fde93f0e88325f9dbeeac982ad446b656e67bbfd727673c219907a37a4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[54].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[55]::Assign

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `3bee63ecf90e9987c99ee7eb14c09d74abec2dbaaba17e09c99baf537bbc5936`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b. Outputs/bindings: a.
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[55]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[55].value::Call

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `0788958feb4134253b9ffc18bbf4850df395582f89866477ca2a0aecbd4f49ef`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[55].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[56]::Expr

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `c82940990a3eaefda719781d620b844a060d010693774425cc7408e79478e599`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[56]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[56].value::Call

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `6b09dfa70bdb143f613d12ad71df20d51212bea470c20499b2f915f7ead829b3`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[56].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[57]::Expr

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `c9d5df6a05dae1cc585eb20b3eaaeea919dc5749eef85f6a35a7cc7abcd2bad0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[57]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[57].value::Call

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `2696138e272bca18cab5f8f64e805743a6ea0ea9afb8006672b66139e13d93b7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[57].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[58]::Expr

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `6b6feceac1fb19f983200ba12442a9f80d3b5a2787607d1842a883a1901ee239`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[58]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[58].value::Call

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `be71e91c80c330c713f4e4de1f31902cfc4ee15e48d244bad2be7d984f3eb79f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[58].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[59]::Assign

Source: `infra/agentinfra/roadmap_cli.py:47`; AST `8d7b412a970ea44d160cb5bf42f6ea130a678851c5374ce87d0f2242b7ea5ebb`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: r.
Calls/effect boundaries: groups.add_parser, groups.add_parser('review').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[59]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[59].value::Call

Source: `infra/agentinfra/roadmap_cli.py:47`; AST `004b21daf1bc93b418195098a3049d4eea32e29caef05dd727b356995b908a91`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('review').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[59].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[59].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:47`; AST `7ef2964c46579a87c89720f5cd7f826c0ef91210e4993ae34a32d8e4c9684043`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[59].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[60]::Assign

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `1f33b4f552ee8c9ab8a9b6e13fda178f96f48fe0a71040f91191b77e79892d21`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[60]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[60].value::Call

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `aeaaa8d6fd333e6c2699eb5f0756cda380be40a9bb1324e07747b51d98112448`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[60].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[61]::Expr

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `2887208acd2a4455692c96521261ade0eab8372189d3ac6d588febeca1595d0b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[61]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[61].value::Call

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `68130a57d27d804ce68d4c033ac36babe7d6a6ac9be99f1c3ca0704516260517`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[61].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[62]::Expr

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `882f89f3fd646937b6ab51176aebdcbd1a0cd63ee8940c0385947fb5b018b1ae`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[62]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[62].value::Call

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `ed59d7d8b165ec868fa0f82c9021da4367d6af7acf07ee52b7b829161e2b2dce`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[62].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[63]::Assign

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `92a11b27a344984e5d0083169e6e5251d5b09791e7390c22a028ab1f66cef576`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[63]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[63].value::Call

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `7983ed6a649832814140ede8ae23ba7464c9a41b7e958c01cef14026be9139fc`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[63].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[64]::Expr

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `2887208acd2a4455692c96521261ade0eab8372189d3ac6d588febeca1595d0b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[64]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[64].value::Call

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `68130a57d27d804ce68d4c033ac36babe7d6a6ac9be99f1c3ca0704516260517`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[64].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[65]::Expr

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `068d7126eac73f88ea17156a6c54b194dee5e50900d2edfc085488322df09cc9`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[65]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[65].value::Call

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `1de64bf94ca5e5b99f5006d36789ac323c6c26bb7996b87f058c0292c2705687`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[65].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[66]::Assign

Source: `infra/agentinfra/roadmap_cli.py:50`; AST `248a84df2fb9affae88171dd40f03a4b912929221ebd55dd538c7bff006d9b3c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[66]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[66].value::Call

Source: `infra/agentinfra/roadmap_cli.py:50`; AST `dce5d5f7fd7ee97ae4e9daceaaf035bd5d1484425eb79c4a52ac1a4eb8f78d2d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[66].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[67]::Expr

Source: `infra/agentinfra/roadmap_cli.py:50`; AST `5f7dd24ced1606201e72daee4fcf61a91284adb1672e1cabf0563dbfc01464ee`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[67]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[67].value::Call

Source: `infra/agentinfra/roadmap_cli.py:50`; AST `0ea5718ae31e75efda1fcea1ce7849822baf95b019d7549f1ff671cc09a94f40`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[67].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[68]::Assign

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `3cbb2dcf48f6859c62b1a5dbf846fd11ee7410727b6d83e8876443357f24ce1c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: a.
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[68]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[68].value::Call

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `7a383a5a9182412cff7abce664e23a45c46563d24f3a2e55c057d84ff62fb33f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[68].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[69]::Expr

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `df14bec3101d63dd0f91777dd229c227a7ac90144b8e51d40cf99082c3d638ee`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[69]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[69].value::Call

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `bc134093f7a57fcb709e49e3242475a1f35a45641aae995d1e08bc2724868ddb`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[69].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[70]::Assign

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `4bccbd1c1da7c4cbbdf97bc5b6b1f1606fab311e9c7ba31c80f1f08dca67d14a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: a.
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[70]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[70].value::Call

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `7b78cdfa4c0f2af9894674b5dc09f74946df9ba208826a1e0fd5d5dbb1bef23e`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[70].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[71]::Expr

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `66e779575fa3fedb27ecac860048980574989dbaaa77a6c03ecf01493d6e313b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[71]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[71].value::Call

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `da44aa014432b1ad99cd6ac42a4e0ab5059f8633c71728ef8957011d126be297`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[71].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[72]::Assign

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `4921bef45f64d4e3ec46ed4bd918692ad841bc750c2a04b8f59837862dac8fd0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: a.
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[72]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[72].value::Call

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `fbe6eb869a621e947c12c5f0e612f91a4948a8f2ca630e3b36cd4e7726fdc0be`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[72].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[73]::Expr

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `e91064d5161e9cd38ed2c50840ad437bd1200a11e053f407932b45b483d9cec7`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[73]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[73].value::Call

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `a8ec9547f4d23916c6d09ea30ca5d98ae042c4b7a03ecd9256c9a082f867de86`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[73].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[74]::Expr

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `339d86fd78ef28936cb867f22d96889136425a29f46206a30c6a1dfa99198192`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[74]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[74].value::Call

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `f0a96293a59ab077ec08fe10c5ca219499f3fb4a5f63778d3b080efc8e2470dc`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[74].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[75]::Expr

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `1569a706aa9235e0941f9875c3145b4d0842bb09629da548002e9fec438f5609`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[75]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[75].value::Call

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `c5f07cc256b9397aec97c29669c42da59e084b87f1b7b89e67803019b25bd002`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[75].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[76]::Expr

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `431c1f251716d5b79d3cb5cc3cb6a1cdd75868d72aa8ebfe4d73d6f1cf526547`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[76]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[76].value::Call

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `beaa7ea323bde41f0404b821d5c58e6ee4cb36763d52f76e51b6d16315ea825b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[17].body[76].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[17].body[77]::Return

Source: `infra/agentinfra/roadmap_cli.py:54`; AST `cb7563fa3b6c0b90880aba1ea365b272a9a70d833d2d33fa1733c5f883e28868`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[17].body[77]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18]::FunctionDef

Source: `infra/agentinfra/roadmap_cli.py:57`; AST `1e049e872fdd6813777aec90ea7fbe51bd98d6eeb84afdb9654f1d8adb5b3bb7`.

Rust module: `infra::agentinfra::roadmap_cli`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, ContractError, a, adjudicate_findings, atomic_write_json, atomic_write_text, audit, audit_evidence, authority_inventory, authorize, bind_goal, bind_plan, capabilities, compile_roadmaps, compiled, confined_path, decision, destination, dict, digest, errors, evidence, goal_transition, index, inventory, ledger, len, markdown, name, obligation, output, packet, parts, path, project_into_record, proof_errors, read_json, read_native_goal, reconcile_inventory, reconcile_native_transition, reconcile_original_tests, record, render_packet, request, require, retrieve, review, root, run_recipe, save_compiled, save_inventory, shards, source, str, u, units, validate_decision, validate_record, validate_skills, value. Outputs/bindings: audit, compiled, decision, destination, errors, evidence, index, ledger, name, obligation, output, parts, path, record, request, review, root, source, u, units, value.
Calls/effect boundaries: BudgetLedger, ContractError, a.milestones.split, a.root.resolve, adjudicate_findings, atomic_write_json, atomic_write_text, audit_evidence, authority_inventory, authorize, bind_goal, bind_plan, capabilities, compile_roadmaps, confined_path, dict, digest, goal_transition, inventory, ledger.observe_usage, ledger.read, len, markdown, packet, parts.items, path.read_text, project_into_record, proof_errors, read_json, read_native_goal, reconcile_inventory, reconcile_native_transition, reconcile_original_tests, render_packet, request.get, require, retrieve, run_recipe, save_compiled, save_inventory, shards, source['path'].replace, str, validate_decision, validate_record, validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:58`; AST `79f35e3dd72e6dfce47e3635b369764f01c3076e2afc775f888cf3623afcbe82`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: root.
Calls/effect boundaries: a.root.resolve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:58`; AST `e8091945a45887165301774a3ac5ca0ff6f6c3cf96c857f6524674dbbb816b9f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.root.resolve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1]::If

Source: `infra/agentinfra/roadmap_cli.py:59`; AST `71e5fb925d3fe140bc82c7f0cfaa8e8db1266934b3109d89ef0a6917bb184eb8`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, audit, audit_evidence, authority_inventory, compile_roadmaps, compiled, evidence, packet, project_into_record, read_json, reconcile_inventory, record, root, run_recipe, save_compiled, save_inventory. Outputs/bindings: audit, compiled, evidence, record.
Calls/effect boundaries: audit_evidence, authority_inventory, compile_roadmaps, packet, project_into_record, read_json, reconcile_inventory, run_recipe, save_compiled, save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1]; no call, error or mutation may be omitted. Condition: a.family == 'roadmap'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:60`; AST `8deac8da987fee33047b87c849024fe4b35da2d8f7167922e3c744059f79a3b1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:60`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[1]::If

Source: `infra/agentinfra/roadmap_cli.py:61`; AST `f6d020ffdd877094286f7587bbb1b6b05b0e88e7359d1c5c6caab9ffce0b4aaa`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, compiled, root, save_compiled. Outputs/bindings: (none).
Calls/effect boundaries: save_compiled.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[1]; no call, error or mutation may be omitted. Condition: a.action == 'compile'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_cli.py:62`; AST `2831da051a07a3fd00e69bfa4c61012066019809684d277c2bbb3aafb7dd6f79`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, compiled, root, save_compiled. Outputs/bindings: (none).
Calls/effect boundaries: save_compiled.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[1].body[0]; no call, error or mutation may be omitted. Condition: a.save
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[1].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_cli.py:62`; AST `14e8a80bc21d0ae3652a959443ecb7aba34beb1db31da32791603d6af017399d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, root, save_compiled. Outputs/bindings: (none).
Calls/effect boundaries: save_compiled.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:62`; AST `58d259b1074dcd62ede16a454a8895ab259d355c6864597b31b8e6d26bfd50be`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, root, save_compiled. Outputs/bindings: (none).
Calls/effect boundaries: save_compiled.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[1].body[1]::Return

Source: `infra/agentinfra/roadmap_cli.py:63`; AST `92976245473cda52a06eb9d15364d44da96631301bc207c683dfe72632458e44`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `245f27baaaa8518746edf736be33f203e7905c315962267294139eed9ca124dc`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, authority_inventory, record, root, save_inventory. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory, save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[2]; no call, error or mutation may be omitted. Condition: a.action == 'inventory'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:65`; AST `e81acdaa3b233e455f1c84080e10ddd499a45c29142fd1572da1bee8b106cdf6`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, authority_inventory, root. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:65`; AST `2e577ab27acd72b09a76021cf0f9a3d521d2edf99bac989808cfe9cfcd33b678`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, authority_inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[2].body[1]::If

Source: `infra/agentinfra/roadmap_cli.py:66`; AST `5af3af8404b85183e106e3bc4fd159b34558319b3f7a69d0038ba322cfbef5db`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, record, root, save_inventory. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[2].body[1]; no call, error or mutation may be omitted. Condition: a.save
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[2].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:67`; AST `a3ecb08dd0f68713f85439403925bdbedda5007653cf191bb00d1bc2d96bee18`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, root, save_inventory. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[2].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:67`; AST `58347316038ab3e9efbe5f11758dcacdf73bfa09fe020f176e7abc4dfe272574`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, root, save_inventory. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[2].body[2]::Return

Source: `infra/agentinfra/roadmap_cli.py:68`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:69`; AST `12df41223f6cc02c7347cef5ef52dc570a0b2f5b294b5f54181c328faa7daa8e`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, read_json, reconcile_inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[3]; no call, error or mutation may be omitted. Condition: a.action == 'reconcile'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[3].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:69`; AST `3d9897098b34252d4194a5f1d04ffab02772ed1efc5f69df7c2242b818c7afa1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json, reconcile_inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:69`; AST `b65137420a5bf73e44cb15b344b10f283878f89d82ed3a62a61e7527750de7ac`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json, reconcile_inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[3].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:69`; AST `f0ce24a1a2ed4f7895a254a16fe0d6a8f62209fbf23ca6caa0bc90c530ae0849`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[4]::If

Source: `infra/agentinfra/roadmap_cli.py:70`; AST `ae2a3b7f03c51c8348e5117b9d3c83dc99f8a9e98d87c708855d9eddb47a67e3`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, compiled, root, run_recipe. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[4]; no call, error or mutation may be omitted. Condition: a.action == 'run'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[4].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:70`; AST `0a8a76593ce4a3ea9274b5cac526332a6ec4478aa4dfeda3eb9f400a518f0552`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, compiled, root, run_recipe. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:70`; AST `9581e1525ed509ea9d46b494b1c4a8759635cb8d16d3c2499bc36605ba0a2d34`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, compiled, root, run_recipe. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[5]::Assign

Source: `infra/agentinfra/roadmap_cli.py:71`; AST `295be51fe27e4e884248ae9f08830d86dcb5609af75fa53f64a6c25be168e783`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, compiled, read_json. Outputs/bindings: evidence.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[5].value.body::Call

Source: `infra/agentinfra/roadmap_cli.py:71`; AST `fc25ea2cd6abde821bb1c3a2a02e2053cfb544754b883c3589b7e4894bb8c825`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[5].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[6]::Assign

Source: `infra/agentinfra/roadmap_cli.py:72`; AST `5b9bb2d45a4363d27939471107c4f967c1c80ff0a1d43d1e67785198f647c140`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit_evidence, compiled, evidence, root. Outputs/bindings: audit.
Calls/effect boundaries: audit_evidence.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[6].value::Call

Source: `infra/agentinfra/roadmap_cli.py:72`; AST `15e12735a35059c13d4e0dfc2ee22d0526ab26ef50db74dcba2999220bbcfb0c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: audit_evidence, compiled, evidence, root. Outputs/bindings: (none).
Calls/effect boundaries: audit_evidence.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[7]::If

Source: `infra/agentinfra/roadmap_cli.py:73`; AST `f2768018683461dbd9e80a635938c8c42a62d97302e7b7fda3274a1804dd438e`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, audit. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[7]; no call, error or mutation may be omitted. Condition: a.action == 'audit'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[7].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:73`; AST `0e0c7b4c8f0a58f4fc44537e62bfb09aaf9562bce62ab0949405fb3ea08424d9`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[8]::If

Source: `infra/agentinfra/roadmap_cli.py:74`; AST `1e23778989d9cdb74c6b38d9abce355933ddcb2bdd07da74433ce08a9df52b21`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, audit, compiled, packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[8]; no call, error or mutation may be omitted. Condition: a.action == 'packet'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[8].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:74`; AST `9407424a9edf75c5b357e208a1942e3f720fd51a0b82be5b3c8c5a62018bd2df`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, audit, compiled, packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:74`; AST `65d70effdfa770e9b6709654e695fd32e4aaf2788be8b883cb41c4e554c6f1cb`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, audit, compiled, packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[9]::Return

Source: `infra/agentinfra/roadmap_cli.py:75`; AST `07d650373b04d59df181e2d935390e5da232b4522f9556de9b6dabb68633908c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, audit, project_into_record, root. Outputs/bindings: (none).
Calls/effect boundaries: project_into_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[1].body[9].value::Call

Source: `infra/agentinfra/roadmap_cli.py:75`; AST `4c516e41e82c04c7823a8877d0f188e97c14c71d69b6d1cef5ef1e800c0d6fc6`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, audit, project_into_record, root. Outputs/bindings: (none).
Calls/effect boundaries: project_into_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:76`; AST `9bcd36524e85445bc3c5cd168b786cf399ebe848ef79c6ba3feb560e20cf549d`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, authorize, read_json. Outputs/bindings: (none).
Calls/effect boundaries: authorize, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[2]; no call, error or mutation may be omitted. Condition: a.family == 'policy'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:76`; AST `38658a6f1850481d81e11b3a047dae179a3bde74200c32ad79df15730868c069`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, authorize, read_json. Outputs/bindings: (none).
Calls/effect boundaries: authorize, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:76`; AST `04f259d6440639ff562fba17978b5d95403ba9a53fd55a9335599dabcf8624c2`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, authorize, read_json. Outputs/bindings: (none).
Calls/effect boundaries: authorize, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[2].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:76`; AST `ae730821ef8d59cf26da05ed18b5192dfb66e1b27429f5e0c7254bf664d9cc9a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:77`; AST `5976d3c7c1c4c0f329a14c2085b70c4c45435897ebad607b9921fe1d75561985`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, bind_goal, bind_plan, capabilities, compile_roadmaps, goal_transition, read_json, read_native_goal, reconcile_native_transition, request, root. Outputs/bindings: request.
Calls/effect boundaries: a.milestones.split, bind_goal, bind_plan, capabilities, compile_roadmaps, goal_transition, read_json, read_native_goal, reconcile_native_transition, request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[3]; no call, error or mutation may be omitted. Condition: a.family == 'codex'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[0]::If

Source: `infra/agentinfra/roadmap_cli.py:78`; AST `b9de212170a4972ad65d795f8db4750c8951532110e1638a9de24581d595c58b`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, capabilities. Outputs/bindings: (none).
Calls/effect boundaries: capabilities.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[3].body[0]; no call, error or mutation may be omitted. Condition: a.action == 'inspect'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:78`; AST `515da2ca20337b4ec525cfaa31f0ed44a377c2696695f3f07079074207aa699f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: capabilities. Outputs/bindings: (none).
Calls/effect boundaries: capabilities.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:78`; AST `3779a25857e47741422b43e04448f6a5fb5452309510474af85559d2512e1d70`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: capabilities. Outputs/bindings: (none).
Calls/effect boundaries: capabilities.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[1]::If

Source: `infra/agentinfra/roadmap_cli.py:79`; AST `2292d8990b2fee587f9c5a7ecad7c594478e0b9d7d1d2c9aed425be97715cae6`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, read_native_goal. Outputs/bindings: (none).
Calls/effect boundaries: read_native_goal.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[3].body[1]; no call, error or mutation may be omitted. Condition: a.action == 'read-goal'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:79`; AST `37b16d3c3e5605f5ddac4df5362dc9586ad3b8cc66e529d6225c1507aa6cb89e`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_native_goal. Outputs/bindings: (none).
Calls/effect boundaries: read_native_goal.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:79`; AST `9166b7feb5ec16c8e871783ece15c4886a0aaf224f323bd1f53ddc2c2b4f4e53`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_native_goal. Outputs/bindings: (none).
Calls/effect boundaries: read_native_goal.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:80`; AST `a0f2d0f8a972d399a4ed0a020dd8e57b55b03245db4a2a5318c5cad70bb75875`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, bind_goal, read_json. Outputs/bindings: (none).
Calls/effect boundaries: bind_goal, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[3].body[2]; no call, error or mutation may be omitted. Condition: a.action == 'bind'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:80`; AST `97e57d272863bb2e70ba47896e3152a1ef697d2648e16871b265d0d2d52f6c5c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, bind_goal, read_json. Outputs/bindings: (none).
Calls/effect boundaries: bind_goal, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:80`; AST `f4496966fef2a26f75eadb6db9e3fb562aa0f5f7a5b19a688d7ac03c290e2342`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, bind_goal, read_json. Outputs/bindings: (none).
Calls/effect boundaries: bind_goal, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[2].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:80`; AST `96ff96906ae694bd0c37891263e3e06cea1f5a647193c11940e89243cf99bfc2`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[2].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:81`; AST `32793b48f97769c0fe6dbe0efb4b090a4754fc94f5c343766ff154e84346abe7`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, bind_plan, compile_roadmaps, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: a.milestones.split, bind_plan, compile_roadmaps, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[3].body[3]; no call, error or mutation may be omitted. Condition: a.action == 'plan'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[3].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:81`; AST `dc46bb7d3d209c75955a80b4332a8de0c31fe4ba8e9c81c27ce2ca67425e60ab`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, bind_plan, compile_roadmaps, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: a.milestones.split, bind_plan, compile_roadmaps, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[3].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:81`; AST `a57c596e4d2c19ccb2f748d97e29d5fc2fd6d4ba6e1311f373eab4478b879ebc`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, bind_plan, compile_roadmaps, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: a.milestones.split, bind_plan, compile_roadmaps, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[3].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:81`; AST `0d81a1b62ae0add0f6856dc19465a7b87f3c6a7d9ff56c4e7d642f1c6da29243`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[3].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[3].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:81`; AST `4d90abaf98d724d834adb4b31b8504efacb6c4a754f49c596a336d7563531146`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.milestones.split.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[3].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[3].body[0].value.args[2]::Call

Source: `infra/agentinfra/roadmap_cli.py:81`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[3].body[0].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[4]::If

Source: `infra/agentinfra/roadmap_cli.py:82`; AST `90160c06518acc42535875d5cd2f7573278302c8efbac8c098070acebfa0df65`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, read_json, reconcile_native_transition. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_native_transition.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[3].body[4]; no call, error or mutation may be omitted. Condition: a.action == 'reconcile'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[4].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:82`; AST `f72e2c235e7348aaed52b08e40a4cd163e4164c49bb529ad9dcf6fc53a521b95`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json, reconcile_native_transition. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_native_transition.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[3].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:82`; AST `c2b6fe545a446946d3ffbd98837378b7604e0f704061a8c8ce5c1d908f4cb4c7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json, reconcile_native_transition. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_native_transition.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[4].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:82`; AST `d874b0d9b3dbd861625df2b1bb5a2e99a0009921c29becf70f0f01f0de9f0577`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[4].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[4].body[0].value.args[1].body::Call

Source: `infra/agentinfra/roadmap_cli.py:82`; AST `3e14c09ef2e407a6410ec771283038e4498e496be544977090334a81c2de3ded`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[4].body[0].value.args[1].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[4].body[0].value.args[2].body::Call

Source: `infra/agentinfra/roadmap_cli.py:82`; AST `00d1a848d2b6dee479d3c6b65533732b9a9746678bd6305830d89330547d0840`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[4].body[0].value.args[2].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[5]::Assign

Source: `infra/agentinfra/roadmap_cli.py:83`; AST `91064dc9252a793622ee877ff1c84343be4fc10513fdbfb826a42a615be6e70b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json. Outputs/bindings: request.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[5].value::Call

Source: `infra/agentinfra/roadmap_cli.py:83`; AST `9882c1cd687efea83eceee7d9a34d69d4146c2b837396aa92795925e6e60483d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[6]::Return

Source: `infra/agentinfra/roadmap_cli.py:84`; AST `3610df6d8d1c3188b34aaf364426076c9c103212cdbbb7e081d2201a67c8e4ee`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, goal_transition, read_json, request. Outputs/bindings: (none).
Calls/effect boundaries: goal_transition, read_json, request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[6].value.values[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:84`; AST `a4d8a0ef453edb21087b037d6e1a77ea94d01151413413ffe2a9e060f7a4c905`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, goal_transition, read_json, request. Outputs/bindings: (none).
Calls/effect boundaries: goal_transition, read_json, request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[6].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[6].value.values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:84`; AST `98164bcaa7d7b39fd20b1bb79671d32916f53482044b9b953171e13f595b20ff`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[6].value.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[6].value.values[1].keywords[0].value.left::Call

Source: `infra/agentinfra/roadmap_cli.py:85`; AST `15b957912b41f944cf4bcfc03f8108964f688a04e33abcf6cf24bfd042e00895`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: request. Outputs/bindings: (none).
Calls/effect boundaries: request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[6].value.values[1].keywords[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[3].body[6].value.values[1].keywords[1].value.left::Call

Source: `infra/agentinfra/roadmap_cli.py:85`; AST `47e928e15f5fd9d6187d759a78a0dbdbb8121a5178efe9fbcbb0c49d0c32236a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: request. Outputs/bindings: (none).
Calls/effect boundaries: request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[6].value.values[1].keywords[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4]::If

Source: `infra/agentinfra/roadmap_cli.py:86`; AST `b0325d861cd7f635c005f0a371d08d9870564b47a06ec3aa0ac9e3a1c68fc65a`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, errors, obligation, proof_errors, read_json, reconcile_original_tests, root, validate_record. Outputs/bindings: errors, obligation.
Calls/effect boundaries: proof_errors, read_json, reconcile_original_tests, validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[4]; no call, error or mutation may be omitted. Condition: a.family == 'verification'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[0]::If

Source: `infra/agentinfra/roadmap_cli.py:87`; AST `68fd8a34344a4930d525901ac814597b201ff8ae466bdb0bd544e872fc373cc9`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, read_json, reconcile_original_tests. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_original_tests.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[4].body[0]; no call, error or mutation may be omitted. Condition: a.action == 'reconcile-tests'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:87`; AST `fcc95b0ddbc96646105bc8a283aa9ba66c6ae304867d7aaa4e71569e97b4a1db`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json, reconcile_original_tests. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_original_tests.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:87`; AST `1f973ce14adbf16c75002a9fc1f67056c23deb3ce107be9df6c3616b8dfb948f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json, reconcile_original_tests. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_original_tests.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[0].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:87`; AST `f0ce24a1a2ed4f7895a254a16fe0d6a8f62209fbf23ca6caa0bc90c530ae0849`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[0].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:87`; AST `eeefe24bc579000a9d07c7951a1aab24ae3afa0c140261d436febc40396a8b8f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:88`; AST `2b866acaba7b4bada6bd020106258480da7af06d477b96f444f901d9968b9d96`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json. Outputs/bindings: obligation.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:88`; AST `218c8fe81c0885a1ba433250fd166d649e82f376d91360fef4d21f55dedd4b1a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[2]::Expr

Source: `infra/agentinfra/roadmap_cli.py:88`; AST `2e179482e3a69ad877f8ac58b2c3ebca3a6f9b190e07a75f3b9dc8778a4015ac`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[2].value::Call

Source: `infra/agentinfra/roadmap_cli.py:88`; AST `9a42878ffb0512bc22fcb3d19d90820d1600e599b18525cff9deb2c80d8c4034`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[3]::Assign

Source: `infra/agentinfra/roadmap_cli.py:89`; AST `611937c2e59fd1a880627c83438ba725da7c90a78704820472c4117fbcd8c80f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, obligation, proof_errors, read_json. Outputs/bindings: errors.
Calls/effect boundaries: proof_errors, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[3].value::Call

Source: `infra/agentinfra/roadmap_cli.py:89`; AST `74c99ca4c8373279712e0e6270d6c5dc6891c8e5a8bd256fb3cb4a54a0c6d195`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, obligation, proof_errors, read_json. Outputs/bindings: (none).
Calls/effect boundaries: proof_errors, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[3].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:89`; AST `acba4d9b63c226ba10fba6d5989b51dd7451295c68d8547fff53be8f58968fb1`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[4].body[4]::Return

Source: `infra/agentinfra/roadmap_cli.py:90`; AST `c30fad21d4bc965a0500e7e2fdbbbb9613d2d7d44477f1c0e9ae67aca9b0f372`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[5]::If

Source: `infra/agentinfra/roadmap_cli.py:91`; AST `e2aea67ec70ff5dcb8f33e5b59bfe64e69f9a167d1738932e7ee4e65302ff30e`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: BudgetLedger, a, ledger, root. Outputs/bindings: ledger.
Calls/effect boundaries: BudgetLedger, ledger.observe_usage, ledger.read.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[5]; no call, error or mutation may be omitted. Condition: a.family == 'budget'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:92`; AST `dc2fd1ede60c6438c487511f87ef8eedec8bb87e6ab3d1c5380ff1542be015c2`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, root. Outputs/bindings: ledger.
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:92`; AST `df43247d3e9a1323119ce795d3f01353dada1c7e238477cf98ed400282fae762`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, root. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[5].body[1]::Return

Source: `infra/agentinfra/roadmap_cli.py:93`; AST `aedfa89cf3e2fd1225a8c78d487f9292ef60455f435c5da94adb1a58c1a08785`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.observe_usage, ledger.read.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[5].body[1].value.body::Call

Source: `infra/agentinfra/roadmap_cli.py:93`; AST `97bf15ee0985708addfb91473f1c9a324eb4e700d9a5a949145f8b93d423dbb2`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.read.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[5].body[1].value.orelse::Call

Source: `infra/agentinfra/roadmap_cli.py:93`; AST `6f635f7bccf485e753e97db386821c2065629b582c2b133f22a3c69ebd0e27ae`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.observe_usage.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[1].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6]::If

Source: `infra/agentinfra/roadmap_cli.py:94`; AST `d86e9a1c8d1ec0ed82150d93a263d5a78aefb1864a7c281bd51149d6ccf3caa1`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, adjudicate_findings, atomic_write_text, confined_path, decision, digest, output, read_json, render_packet, review, root, str, validate_decision, validate_record. Outputs/bindings: decision, output, review.
Calls/effect boundaries: adjudicate_findings, atomic_write_text, confined_path, digest, read_json, render_packet, str, validate_decision, validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[6]; no call, error or mutation may be omitted. Condition: a.family == 'review'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[0]::If

Source: `infra/agentinfra/roadmap_cli.py:95`; AST `59b50194357d402467c8d0f51f72aa6465b150318853d0829791c2e312260e94`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, adjudicate_findings, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: adjudicate_findings, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[6].body[0]; no call, error or mutation may be omitted. Condition: a.action == 'findings'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:95`; AST `8030a303f2383dcd27c7e41e42d77419775bb87a0450a48e2276e718202af7ec`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, adjudicate_findings, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: adjudicate_findings, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[0].body[0].value.values[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:95`; AST `fef85d040a556c5d551f2c3ce9d0c582785bb29ab412b211d4ef1138730cafe1`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, adjudicate_findings, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: adjudicate_findings, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[0].body[0].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[0].body[0].value.values[0].args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:95`; AST `ba2e037c249060aa994cb7cdd399af6ca6412389ec535254e4d71c8e3ec8b159`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[0].body[0].value.values[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:96`; AST `2064d27d432cc4f1e728bb7c802ed2d030151c13e7a45af19d16ebaf8f9f21e7`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json. Outputs/bindings: review.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:96`; AST `1ce8bc32ec262e834458b495b0c1db54cccd88aa659286e524f2af778941ba4f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:97`; AST `23076d1b52a0112f303cbb78a05c805a7e8ca40df8ed2bafd58a17e0946fd786`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, atomic_write_text, confined_path, digest, output, render_packet, review, root, str. Outputs/bindings: output.
Calls/effect boundaries: atomic_write_text, confined_path, digest, render_packet, str.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[6].body[2]; no call, error or mutation may be omitted. Condition: a.action == 'render'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:98`; AST `9bc857a9c259ffb8498c8ad6aec0eb37b6a5c65d1337f5af179d4c3a6ead4a81`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, confined_path, root. Outputs/bindings: output.
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:98`; AST `8772d9314c0b7dd22d22e6244a777898fc2b45883955c41d834a353f76d6647d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_cli.py:99`; AST `a1b81b41da846f5a98e45da83d505909f72b5c37c9a3983b607b9496a87da9dd`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_text, output, render_packet, review, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_text, render_packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[6].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:99`; AST `b4d27b01aed560cdc9e1a56b1c34f27455f8aa67ca08be44afac04f6a07004b7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_text, output, render_packet, review, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_text, render_packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[2].body[1].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:99`; AST `b7dc504ba7e9fb0b2705ec2c3dbaf8fd8adfc7cb27ea4f695fdb22c69cf39bf7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: render_packet, review, root. Outputs/bindings: (none).
Calls/effect boundaries: render_packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[2].body[1].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[2].body[2]::Return

Source: `infra/agentinfra/roadmap_cli.py:100`; AST `2a58ec5c2ada76640d8e0a0a11954672602fb55afdf2df2a6d6ed157c3fe61ad`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, output, review, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, str.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[6].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[2].body[2].value.values[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:100`; AST `ac21b5e6705c69eec368406129c3927fb69226e1c7181f1f7830ab68cf750b41`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[2].body[2].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[2].body[2].value.values[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:100`; AST `d36ee616fab72f11a9b8fa05d8b03628acdcfc6aa2d8e2513c316f915994eead`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, review. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[2].body[2].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[3]::Assign

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `7ff3842184ad38d386d3fbda72d4b63b5dfe203d3173d1c290ff8e9ddcde0b0b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json. Outputs/bindings: decision.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[3].value::Call

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `76628dd778b220d48ec2a53893457a3b78cd25f15167d52b9065ca1cafc6dbde`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[4]::Expr

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `9eff61797fbda476656325e1f568cf0c33d242e0294b5c1c8d340776f52f3edf`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: decision, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[4].value::Call

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `c7a602387eada360323a4fb3d1ca7d887a837880376ede3782c142d79c2301d7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[5]::Expr

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `2ef727bf50ad878a6cef5f34097c625aabfb5dca20eda630d436c298577204cb`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: decision, review, validate_decision. Outputs/bindings: (none).
Calls/effect boundaries: validate_decision.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[5].value::Call

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `cfe68890edc351089e87f7bbe56be4d679ba4d6c38c06491b981791a1ad540d7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision, review, validate_decision. Outputs/bindings: (none).
Calls/effect boundaries: validate_decision.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[6].body[6]::Return

Source: `infra/agentinfra/roadmap_cli.py:102`; AST `fb44afbf6d110f4331989b733995932640bc207ef77c8376a16401ee04c9885d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[7]::If

Source: `infra/agentinfra/roadmap_cli.py:103`; AST `25b790c0f2fbfe2cff60d496bed55873a0e4933be1e521a55040950f666ec9fa`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, root, validate_skills. Outputs/bindings: (none).
Calls/effect boundaries: validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[7]; no call, error or mutation may be omitted. Condition: a.family == 'skills'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[7].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:103`; AST `7fd1f5c078c677852c1a9e96ee1ad8cba91999b6edf00abb4f044dfdb23b5626`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, validate_skills. Outputs/bindings: (none).
Calls/effect boundaries: validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:103`; AST `058a684a59952bf7321b2dca779c67fea9fccce702659f76c7c2ae7f32107527`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, validate_skills. Outputs/bindings: (none).
Calls/effect boundaries: validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[8]::If

Source: `infra/agentinfra/roadmap_cli.py:104`; AST `38a7a387bb052cf16ed74202b8859039f0cbdab72698c229bbad3f1933069b3c`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, retrieve, root. Outputs/bindings: (none).
Calls/effect boundaries: retrieve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[8]; no call, error or mutation may be omitted. Condition: a.family == 'knowledge'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[8].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:104`; AST `068483da203a4f6e539d8e5f83b4805e16509d2a447571683ccfceef37f22b6b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, retrieve, root. Outputs/bindings: (none).
Calls/effect boundaries: retrieve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:104`; AST `f61c38307560937a0d84d223d433e8b69e32e24d21b8d5efdf1b3a44b3a051d7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, retrieve, root. Outputs/bindings: (none).
Calls/effect boundaries: retrieve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9]::If

Source: `infra/agentinfra/roadmap_cli.py:105`; AST `708324bafdfd8b68d79ed27783e3d1987afec972816ea27d9d43cf9596f7f8e7`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, atomic_write_json, atomic_write_text, destination, dict, index, inventory, len, markdown, name, parts, path, read_json, record, require, root, shards, source, u, units, value. Outputs/bindings: destination, index, name, parts, path, record, source, u, units, value.
Calls/effect boundaries: atomic_write_json, atomic_write_text, dict, inventory, len, markdown, parts.items, path.read_text, read_json, require, shards, source['path'].replace.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[9]; no call, error or mutation may be omitted. Condition: a.family == 'portability'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:106`; AST `015514a635c8911569abe27c13b24b38a29e13bb5116d66c13bbd87de1f4b7e2`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, root. Outputs/bindings: record.
Calls/effect boundaries: inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:106`; AST `865ab48cd6a5f9f39dbe8c1a00c6302e98015cad7159c31875dcf06bf0c972b7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:106`; AST `5499099aa48dfd490ae43313ddaf372a5d34df3a08ef12c248426452898dbb08`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: destination.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[2]::Assign

Source: `infra/agentinfra/roadmap_cli.py:107`; AST `806d41510d2b87f0e2a670736c45f29bf811987a186e491dab8e2c48a6049c7f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, shards. Outputs/bindings: index, parts.
Calls/effect boundaries: shards.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[2].value::Call

Source: `infra/agentinfra/roadmap_cli.py:107`; AST `e993f6a2d7fa159b4f0163de851c48636bc8f18aed60f6bbd164da3c8a9a397e`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, shards. Outputs/bindings: (none).
Calls/effect boundaries: shards.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:108`; AST `df9fdc5ce9d1a93a9c1b4b51543d31b3daeefd831f5947aa24f11680eda3f985`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, atomic_write_json, atomic_write_text, destination, dict, index, len, markdown, name, parts, path, record, root, source, u, units, value. Outputs/bindings: name, path, source, u, units, value.
Calls/effect boundaries: atomic_write_json, atomic_write_text, dict, len, markdown, parts.items, source['path'].replace.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[18].body[9].body[3]; no call, error or mutation may be omitted. Condition: a.action == 'build'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[0]::For

Source: `infra/agentinfra/roadmap_cli.py:109`; AST `4bbeac527b675cf6dc8f8a3080ea662550ec9b4a226be4cca999f877e30dd482`.

Rust module: `infra::agentinfra::roadmap_cli`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: atomic_write_json, destination, name, parts, root, value. Outputs/bindings: name, value.
Calls/effect boundaries: atomic_write_json, parts.items.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered For evaluation at root.body[18].body[9].body[3].body[0]; no call, error or mutation may be omitted. Iteration: (name, value) in parts.items()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[0].iter::Call

Source: `infra/agentinfra/roadmap_cli.py:109`; AST `2141119718c6153bf438d761a03d90f528922a00b6347b49ce2232dc5bc7f360`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parts. Outputs/bindings: (none).
Calls/effect boundaries: parts.items.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_cli.py:110`; AST `bd4d7f5541582d9956c450924e71e1110926794c02c35a5d938b69ce1e824ca4`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, destination, name, root, value. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[9].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:110`; AST `d07b44d5eafeb28ed79d7bb9345cc940162d232fa7e3047ddca45d3a77484d56`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, destination, name, root, value. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[1]::For

Source: `infra/agentinfra/roadmap_cli.py:111`; AST `0c999c341429a9e587ea60a602d17c4bef767970f50abfe8d20c08bb36f993c9`.

Rust module: `infra::agentinfra::roadmap_cli`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: atomic_write_text, destination, dict, markdown, path, record, root, source, u, units. Outputs/bindings: path, source, u, units.
Calls/effect boundaries: atomic_write_text, dict, markdown, source['path'].replace.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered For evaluation at root.body[18].body[9].body[3].body[1]; no call, error or mutation may be omitted. Iteration: source in record['files']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:112`; AST `2cbc6a685af61bdc304987fe82a1969899b2a8b40a792e255ce37e30f2eb07a1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, source, u. Outputs/bindings: u, units.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[9].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[1].body[0].value::ListComp

Source: `infra/agentinfra/roadmap_cli.py:112`; AST `8c3a41aa19526923efb80703034df2bb0908e38a152bb6f470320106bab452fd`.

Rust module: `infra::agentinfra::roadmap_cli`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: record, source, u. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[9].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:113`; AST `c429a61b501e3892ea093c5254bd801a34da054e0c02fcae545fe3d102fa4fc4`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, source. Outputs/bindings: path.
Calls/effect boundaries: source['path'].replace.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[9].body[3].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[1].body[1].value.right.left::Call

Source: `infra/agentinfra/roadmap_cli.py:113`; AST `9b2de27704610ae2cbf3b2beffecf18cf8cdd0f1d8e61bbef3eb0ac16d02a512`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source['path'].replace.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[1].body[1].value.right.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_cli.py:114`; AST `ed2d774da2504f14a1400487757169e8baa069342643686857242767823d4620`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_text, dict, markdown, path, record, root, source, units. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_text, dict, markdown.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[9].body[3].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_cli.py:114`; AST `4d10b61a1e41f1828e9a2ace9a856ba175104039651c7ee679e56da88dfb19aa`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_text, dict, markdown, path, record, root, source, units. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_text, dict, markdown.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[1].body[2].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:114`; AST `729dab877983035be0f48ebab897b6fc74f9858a79bde4abfe9eb69e37cca802`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, markdown, record, source, units. Outputs/bindings: (none).
Calls/effect boundaries: dict, markdown.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[1].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[1].body[2].value.args[1].args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:114`; AST `d8fa34e6da027262ece2b06813b7e92c0dbea1bf6e21ce25e929730abf804190`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, record, source, units. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[1].body[2].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap_cli.py:116`; AST `ee134dd4792cbeeb7cd7de23f136f25cadf3fca248c2025066898677e39dad42`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, destination, index, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[9].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_cli.py:116`; AST `a70638dc6385262148589df77607a1deef3f5c8914d6e7472f4c5f4b0208e202`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, destination, index, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[3]::Return

Source: `infra/agentinfra/roadmap_cli.py:117`; AST `878b24072fcff043e8739b26948c2ac54d48755374bb115a0274b5d3e692a3b6`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, parts, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[9].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[3].value.values[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:117`; AST `df46df88acf5e6ef901488c4610d14a5b71f816377a047e8ea3cd040d31bfe4e`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[3].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[3].value.values[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:117`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[3].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[3].body[3].value.values[2]::Call

Source: `infra/agentinfra/roadmap_cli.py:117`; AST `059b0e4f7177f35990c6a2d1d8eee991b362a7579d462eedd70a67c44c33444a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, parts. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[3].body[3].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[4]::Expr

Source: `infra/agentinfra/roadmap_cli.py:118`; AST `619695d68716d53ae79dbd08cc73ed5c3559e188ff8ef2f455085cf915b94d92`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, index, read_json, require. Outputs/bindings: (none).
Calls/effect boundaries: read_json, require.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[4].value::Call

Source: `infra/agentinfra/roadmap_cli.py:118`; AST `c34b1e4d36635ab28eb902ff6f2d9b5dfe8d541a7c2286fc1ab4b191604c8ddb`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, index, read_json, require. Outputs/bindings: (none).
Calls/effect boundaries: read_json, require.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_cli.py:118`; AST `7b67331f44b99643904672082eef41c3a275309e1d6c46fba4e0a04c3dd32464`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[5]::For

Source: `infra/agentinfra/roadmap_cli.py:119`; AST `237ecd9a2d680fc39ded4e3ccc2b9206c61204e3b4e3320b8af63103d12ffee4`.

Rust module: `infra::agentinfra::roadmap_cli`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: destination, name, parts, read_json, require, value. Outputs/bindings: name, value.
Calls/effect boundaries: parts.items, read_json, require.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered For evaluation at root.body[18].body[9].body[5]; no call, error or mutation may be omitted. Iteration: (name, value) in parts.items()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[5].iter::Call

Source: `infra/agentinfra/roadmap_cli.py:119`; AST `2141119718c6153bf438d761a03d90f528922a00b6347b49ce2232dc5bc7f360`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parts. Outputs/bindings: (none).
Calls/effect boundaries: parts.items.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[5].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_cli.py:120`; AST `bf50832597b4d72b4465d53c16f2ab99bf20f0cb43a49cc51068793034f1ac90`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, name, read_json, require, value. Outputs/bindings: (none).
Calls/effect boundaries: read_json, require.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[9].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:120`; AST `71b0ca4f70ecdb6fcde66db3833bbcbe906e2bfa86598ccd04720f2bc046eb52`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, name, read_json, require, value. Outputs/bindings: (none).
Calls/effect boundaries: read_json, require.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[5].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_cli.py:120`; AST `00cd1e7c97307a1377b931c6e3c36ebe8772fcb22459342408d1f29b76a47cf4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, name, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[5].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6]::For

Source: `infra/agentinfra/roadmap_cli.py:121`; AST `f3fd1ce980cb5949736b14961aeb97e6b843b04221e10694227163591ca13bd0`.

Rust module: `infra::agentinfra::roadmap_cli`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: destination, dict, markdown, path, record, require, source, u, units. Outputs/bindings: path, source, u, units.
Calls/effect boundaries: dict, markdown, path.read_text, require, source['path'].replace.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered For evaluation at root.body[18].body[9].body[6]; no call, error or mutation may be omitted. Iteration: source in record['files']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:122`; AST `c429a61b501e3892ea093c5254bd801a34da054e0c02fcae545fe3d102fa4fc4`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, source. Outputs/bindings: path.
Calls/effect boundaries: source['path'].replace.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[9].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6].body[0].value.right.left::Call

Source: `infra/agentinfra/roadmap_cli.py:122`; AST `9b2de27704610ae2cbf3b2beffecf18cf8cdd0f1d8e61bbef3eb0ac16d02a512`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source['path'].replace.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[6].body[0].value.right.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:123`; AST `2cbc6a685af61bdc304987fe82a1969899b2a8b40a792e255ce37e30f2eb07a1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, source, u. Outputs/bindings: u, units.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[9].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6].body[1].value::ListComp

Source: `infra/agentinfra/roadmap_cli.py:123`; AST `8c3a41aa19526923efb80703034df2bb0908e38a152bb6f470320106bab452fd`.

Rust module: `infra::agentinfra::roadmap_cli`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: record, source, u. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[9].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6].body[2]::Expr

Source: `infra/agentinfra/roadmap_cli.py:124`; AST `36d37125c9eae7aa380f213c6648f6b1e21ce999c061f85d5ecbb22213b08905`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, markdown, path, record, require, source, units. Outputs/bindings: (none).
Calls/effect boundaries: dict, markdown, path.read_text, require.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[9].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6].body[2].value::Call

Source: `infra/agentinfra/roadmap_cli.py:124`; AST `3c2da3f8f9faa03e2920e9728dafd4b473ca3e590c1732bd866ba7f645e09c2d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, markdown, path, record, require, source, units. Outputs/bindings: (none).
Calls/effect boundaries: dict, markdown, path.read_text, require.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_cli.py:124`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[6].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6].body[2].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:124`; AST `729dab877983035be0f48ebab897b6fc74f9858a79bde4abfe9eb69e37cca802`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, markdown, record, source, units. Outputs/bindings: (none).
Calls/effect boundaries: dict, markdown.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[6].body[2].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[6].body[2].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:124`; AST `d8fa34e6da027262ece2b06813b7e92c0dbea1bf6e21ce25e929730abf804190`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, record, source, units. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[6].body[2].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[7]::Return

Source: `infra/agentinfra/roadmap_cli.py:125`; AST `6756fafdd70b48524e65932e80fa90066ba1be33989aba3e91465d64818bda96`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[18].body[9].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[7].value.values[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:125`; AST `df46df88acf5e6ef901488c4610d14a5b71f816377a047e8ea3cd040d31bfe4e`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[7].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[9].body[7].value.values[2]::Call

Source: `infra/agentinfra/roadmap_cli.py:125`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[7].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[10]::Raise

Source: `infra/agentinfra/roadmap_cli.py:126`; AST `debed461b974cbf336edaea02428ffc216957df0d7a917536d6e2de5587e1315`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Raise evaluation at root.body[18].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[18].body[10].exc::Call

Source: `infra/agentinfra/roadmap_cli.py:126`; AST `333142f0e1fa20905c27448d9162355696f52b65354b52edfbd65aa2378e21f1`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[18].body[10].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19]::FunctionDef

Source: `infra/agentinfra/roadmap_cli.py:129`; AST `0f6d1262dfef087511c88e2049bb4128052c6bcafcbb60ccbbcdce3495072c6d`.

Rust module: `infra::agentinfra::roadmap_cli`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, KeyError, OSError, TimeoutError, TypeError, any, args, argv, exc, execute, field, int, json, p, parser, print, result. Outputs/bindings: args, field, p, result.
Calls/effect boundaries: any, execute, json.dumps, p.exit, p.parse_args, parser, print, result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:130`; AST `9dc8c44f59c3161d0cc156f6aecd07f170ee9f31037805aa1f48124aef10b25a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: p.
Calls/effect boundaries: parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:130`; AST `df5895e3f1cab8e578b78958e7e659d10948f3aac705dca2c579407a606b00f5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:130`; AST `3800b3ee5d4ab1b24a9a4cc9deecd976f4e7ffc367ecb2fe78fd2badbbff7645`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, p. Outputs/bindings: args.
Calls/effect boundaries: p.parse_args.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:130`; AST `9936886f5866377ccb6f8939c42f52f219208c2e43a6ba529ece17a973a13833`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, p. Outputs/bindings: (none).
Calls/effect boundaries: p.parse_args.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2]::Try

Source: `infra/agentinfra/roadmap_cli.py:131`; AST `0a5654b110cdd66ddf69be07f9ff8ad82084f456780087519a38ea1e1ccc490d`.

Rust module: `infra::agentinfra::roadmap_cli`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ContractError, KeyError, OSError, TimeoutError, TypeError, any, args, exc, execute, field, json, p, print, result. Outputs/bindings: field, result.
Calls/effect boundaries: any, execute, json.dumps, p.exit, print, result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Try evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:132`; AST `a6c8557b1594077d4c64d47935b11cd262272a3adaf7bc565e76c7ae84138991`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, execute. Outputs/bindings: result.
Calls/effect boundaries: execute.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:132`; AST `5f653271dab8375b133a694587bc52c1b28bb67d9f643515cb52cb696d923ca5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, execute. Outputs/bindings: (none).
Calls/effect boundaries: execute.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_cli.py:133`; AST `1f1d4d7bd101d7f32b676d6e3e16cddb87fa100cab5023be61a29ac0cbfa582c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, print, result. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, print.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:133`; AST `1076a09dd0da2d2c92ba1f149118ae6010f84f733b08b2def2729c50cb9ed40d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, print, result. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, print.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:133`; AST `482b5db37e2273e04f7ab894193fdb1f74861d89d051bd1a93d17dfecf567250`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, result. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `fb28d1d9fcb889cfee33592bc4a09ad0cf3b797209cd5d02970e48217c8b9763`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, field, result. Outputs/bindings: field.
Calls/effect boundaries: any, result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[19].body[2].body[2]; no call, error or mutation may be omitted. Condition: any((result.get(field) is False for field in ('allowed', 'accepted', 'complete', 'confirmed')))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[2].test::Call

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `e051239d848cf33f499947b07608fce94dc603b4c39f21081d0468be4d308607`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, field, result. Outputs/bindings: field.
Calls/effect boundaries: any, result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].body[2].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[2].test.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `58e5b651eeb8b83f249f4a96954e3ce3ca4d1d5222525a56f97652ee21192b7d`.

Rust module: `infra::agentinfra::roadmap_cli`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: field, result. Outputs/bindings: field.
Calls/effect boundaries: result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[19].body[2].body[2].test.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[2].test.args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `9d473b3f36dfac6c9aaf2b6fabe3b438dcd768708fb7d8484e19c3445f685829`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].body[2].test.args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `4d9e3bd49f1ca0e5c82918a80328eaa190b6c6419b7b4aa57c05de813ded1b78`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[19].body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:135`; AST `c060bda3132b81a27d4f1d01c9c1a493e80e7d15f47c69c80bede2f55498187c`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: args, result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered If evaluation at root.body[19].body[2].body[3]; no call, error or mutation may be omitted. Condition: args.family == 'roadmap' and args.action == 'run'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[3].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:136`; AST `8dafa2403497ce3d782c0f2c34a3f25d163ce6f342082909b5bc39b1e5b7fa79`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[19].body[2].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].body[4]::Return

Source: `infra/agentinfra/roadmap_cli.py:137`; AST `b2bbc444950f9b0b0b967dc529eb889a7cf0d4003be033124fc090f4e1571b48`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Return evaluation at root.body[19].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_cli.py:138`; AST `9508f3c2a28f9ada3eeec6182e8684fd368c99eaa08ba56f728972a00c36d746`.

Rust module: `infra::agentinfra::roadmap_cli`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ContractError, KeyError, OSError, TimeoutError, TypeError, exc, p. Outputs/bindings: (none).
Calls/effect boundaries: p.exit.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[19].body[2].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_cli.py:139`; AST `5f7322c48418c569c165551f656c775fae092884420f03f0593047d7b35f2e3c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, p. Outputs/bindings: (none).
Calls/effect boundaries: p.exit.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[2].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[19].body[2].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:139`; AST `082fec13c8186df8eeb6e9e284d04cda702d72d8c713be8d84307cbfe23799a0`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, p. Outputs/bindings: (none).
Calls/effect boundaries: p.exit.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_codex, roadmap_inventory, roadmap_knowledge, roadmap_policy, roadmap_portability, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, security.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
