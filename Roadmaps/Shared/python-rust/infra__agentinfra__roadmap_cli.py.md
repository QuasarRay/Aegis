# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 418. Inventory digest: `232ca317b1233c53c4ad4e63d96052d18d9ec536f5def3a5ef5403e3c30f5155`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_cli.py::module::root::Module

Source: `infra/agentinfra/roadmap_cli.py:1`; AST `4795a3ccf05b7cbf1ce6bb07bcb63beb79e7ed4e170dd7e4f58abe451186ea2a`.

Rust module: `infra::agentinfra::roadmap_cli`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BudgetLedger, ContractError, KeyError, OSError, Path, ProjectAdapter, TimeoutError, TransactionError, TypeError, WorkspaceLease, __doc__, __file__, a, adjudicate_findings, any, argparse, args, argv, assemble_implementation, atomic_write_text, audit, audit_evidence, authority_inventory, authorize, b, bind_goal, bind_plan, c, capabilities, check, compare_interfaces, compile_roadmaps, compiled, confined_path, decision, dict, digest, errors, evidence, exc, execute, field, goal_transition, groups, i, int, inventory, json, ledger, obligation, observe_interfaces, output, owner, p, packet, parser, print, project_into_record, proof_errors, proof_result, publish, python_proof_errors, r, read_json, read_native_goal, reconcile_inventory, reconcile_native_transition, reconcile_original_tests, record, recover_operation, refresh_implementation_dependencies, render_packet, request, result, retrieve, review, root, run_recipe, save_compiled, save_inventory, str, v, validate_decision, validate_record, validate_skills. Outputs/bindings: a, args, audit, b, c, compiled, decision, errors, evidence, field, groups, i, ledger, obligation, output, owner, p, proof_result, r, record, request, result, review, root, v.
Calls/effect boundaries: BudgetLedger, ContractError, Path, Path(__file__).resolve, ProjectAdapter, ProjectAdapter(root).read, ProjectAdapter(root).rebind_native_process, ProjectAdapter(root, a.project, profiles=compiled['projects']).describe, WorkspaceLease, WorkspaceLease(root).qualify, a.add_argument, a.milestones.split, a.root.resolve, adjudicate_findings, any, argparse.ArgumentParser, assemble_implementation, atomic_write_text, audit_evidence, authority_inventory, authorize, b.add_parser, bind_goal, bind_plan, c.add_parser, c.add_parser('read-goal').add_argument, c.add_parser('rebind-process').add_argument, capabilities, check, compare_interfaces, compile_roadmaps, confined_path, digest, execute, goal_transition, groups.add_parser, groups.add_parser('budget').add_subparsers, groups.add_parser('codex').add_subparsers, groups.add_parser('interfaces').add_subparsers, groups.add_parser('review').add_subparsers, groups.add_parser('roadmap').add_subparsers, groups.add_parser('verification').add_subparsers, i.add_parser, i.add_parser('compare').add_argument, inventory, json.dumps, ledger.metrics, ledger.observe_usage, ledger.read, ledger.reservation_record, observe_interfaces, p.add_argument, p.add_subparsers, p.exit, p.parse_args, packet, parser, print, project_into_record, proof_errors, publish, python_proof_errors, r.add_parser, r.add_parser('audit').add_argument, r.add_parser('compile').add_argument, r.add_parser('profile').add_argument, read_json, read_native_goal, reconcile_inventory, reconcile_native_transition, reconcile_original_tests, recover_operation, refresh_implementation_dependencies, render_packet, request.get, result.get, retrieve, run_recipe, save_compiled, save_inventory, str, v.add_parser, validate_decision, validate_record, validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[10]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:13`; AST `350ed562c332caf21de7e1cc1f6250fbf4a4b33eedc5bfde1986239c1552271d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

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
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[15]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:18`; AST `36b28dc07c7a83ea7c7593109b2cb6ec6be9b9f500ca428a3a0a60121377f882`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[16]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:19`; AST `06018155a23f1f83c82d139847669324993143354a3dd3b3aaf896059cf1187a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[17]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:20`; AST `f66cfce668ebcfb5d201a4340b28f6b073fb342c318f8eb73e98209884374c07`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[18]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:21`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::root.body[19]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:22`; AST `e1dc3371852e20d912f01f8276a2e30d2ef2733418e593365380322bc53d08fd`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20]::FunctionDef

Source: `infra/agentinfra/roadmap_cli.py:25`; AST `a41ee1ea1a1b9ebcadf5b6c6c839cecf3b16bf7fbf9dffc08db365b8453d192a`.

Rust module: `infra::agentinfra::roadmap_cli`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, __doc__, __file__, a, argparse, b, c, groups, i, int, p, r, v. Outputs/bindings: a, b, c, groups, i, p, r, v.
Calls/effect boundaries: Path, Path(__file__).resolve, a.add_argument, argparse.ArgumentParser, b.add_parser, c.add_parser, c.add_parser('read-goal').add_argument, c.add_parser('rebind-process').add_argument, groups.add_parser, groups.add_parser('budget').add_subparsers, groups.add_parser('codex').add_subparsers, groups.add_parser('interfaces').add_subparsers, groups.add_parser('review').add_subparsers, groups.add_parser('roadmap').add_subparsers, groups.add_parser('verification').add_subparsers, i.add_parser, i.add_parser('compare').add_argument, p.add_argument, p.add_subparsers, r.add_parser, r.add_parser('audit').add_argument, r.add_parser('compile').add_argument, r.add_parser('profile').add_argument, v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:26`; AST `762667c972fb286c0192232e5854a3e820a82233b313373f35aa5309e577c1bc`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: __doc__, argparse. Outputs/bindings: p.
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:26`; AST `d39f39ff7d74d107a287f654b8e1af65d84cce415404e0fd0bba007cadaa9678`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: __doc__, argparse. Outputs/bindings: (none).
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[1]::Expr

Source: `infra/agentinfra/roadmap_cli.py:27`; AST `5e352c2e646e54897ce8d61da0bd9b7d0b87d41475a11e3b64ebbf1063d38b83`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, p. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, p.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:27`; AST `5da6e9cc72817b9a192d9bfbadac445ca27fa5d2cd2b2b02f290b6f2cd58a6f9`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, p. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, p.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[1].value.keywords[1].value.value.value::Call

Source: `infra/agentinfra/roadmap_cli.py:27`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].value.keywords[1].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[1].value.keywords[1].value.value.value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:27`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].value.keywords[1].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[2]::Assign

Source: `infra/agentinfra/roadmap_cli.py:28`; AST `856499fa778c34b27c8b6f2e21f60a3cadbce7891dc908abadbf898719c06a3d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p. Outputs/bindings: groups.
Calls/effect boundaries: p.add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[2].value::Call

Source: `infra/agentinfra/roadmap_cli.py:28`; AST `4351d59ec5b072d4848a94776321908359fc3bef1cae5221fd4d0419461cc91a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[3]::Assign

Source: `infra/agentinfra/roadmap_cli.py:29`; AST `f6f4873a2d79beaa1e0689530f612b5e0b7608ec6820f91aa5d284bd2947b9c8`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: r.
Calls/effect boundaries: groups.add_parser, groups.add_parser('roadmap').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[3].value::Call

Source: `infra/agentinfra/roadmap_cli.py:29`; AST `bf1a69ee94f63509c92c4ddaf4a409ccadd053391a9cf3fcc76ae2c621a267b8`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('roadmap').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:29`; AST `92bd4be1f871e64f3b231006cf2748a057d6db368711b6fcb5838917bf1da1d2`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[4]::Expr

Source: `infra/agentinfra/roadmap_cli.py:30`; AST `950e026ee6e73b5028e81f04ab3e95af394824f72d0066d16f066fee905e7861`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('compile').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[4].value::Call

Source: `infra/agentinfra/roadmap_cli.py:30`; AST `06852dbd5b542a43495c8f9db43d2b79f09e45472f7d7bfb2f07041454765501`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('compile').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[4].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:30`; AST `0b9f187e08fdf4f2c57fc155f24eeb64de153bd38e4f0f5d8367c8e675fe6962`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[5]::Expr

Source: `infra/agentinfra/roadmap_cli.py:31`; AST `8fb8cc6dadac5eed504fd56be16284c90fdaeaede39b7f33840d2584aebb4fcc`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('audit').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[5].value::Call

Source: `infra/agentinfra/roadmap_cli.py:31`; AST `8abc9763bd166cdc94da8cd836a5e73581ddefa861aca0c6b726889840f4804c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('audit').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[5].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:31`; AST `929859d84bd1d6bfb53dd2da54b56e25445b9c3de2b636974828ce593cc40d4c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[5].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[6]::Assign

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `22d979e159529f0f1bcb4f217c643751d985de7b9596b7fc9e5147502f7af9c3`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[6].value::Call

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `bd6fc3360cf8d1d1f7ab06dd7223a7531bb2d2b17634659ffa2c2ac3d093e189`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[7]::Expr

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `2af01447d3e309b3fbdb72b8307d0aeca8aa14e58b263a6d1842c7bd5388429e`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[7].value::Call

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `8f00e756ef7d65949ba6c4549e55b30c05f6771c3cd015ff588fc517e7194e5c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[8]::Expr

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `6cd3dae08fb3d71f72d1d91f230a71b90ae54ea9204989eef837e5c43b9ed75f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[8].value::Call

Source: `infra/agentinfra/roadmap_cli.py:32`; AST `ec44701bf79e9ec6841cbbadae14baebaef5661c113e8c1b06ace8502d0b2b12`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[9]::Assign

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `d5b51a8be1705c6007de0f1fdbf301594f18dd7b2c3b5a0ef793deb136315b01`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[9].value::Call

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `f956a197b089a2123fec496645189a61d736c1db93d4a2c7eab4af5f4eedb41b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[10]::Expr

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `3d0486ff88a6f9f6e1dcde487c67988bed45d1358b9003e3b5aaf0a838a07b6b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[10].value::Call

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `3228d4014d06ad1ffec0d17e434cf21a03ebb971b2b36f5dd30aa884dfce4c71`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[11]::Expr

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `03984ef88a8dd602845af017c489cc36790de3cf0cfd4d330cd2025b9aa65919`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[11].value::Call

Source: `infra/agentinfra/roadmap_cli.py:33`; AST `abc211af0c5ab445e488423d23cbdc4b082e277822d07332c7e4802d70f377c7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[12]::Assign

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `3945683aae44e77e8af4af3ad34ee3ac1d8777ac632891b0db32ad239c58b090`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[12].value::Call

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `a24ee11b768cd79037964a4438ecf82a74e31c9223be6df7b96fb813c216ee27`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[13]::Expr

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `7dce0795c7e6dd95d825de79692e5acb237454821ed836368824370080f6575f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[13].value::Call

Source: `infra/agentinfra/roadmap_cli.py:34`; AST `a775df190be8c5ed7ab113e7549218db03a8321546b14edb7fb64c95e40a7997`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[14]::Assign

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `d46cf1d12b1af188312a81a5e2155d4d7f2e54a81cbb5bcc9e4de1de1cb58c99`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[14].value::Call

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `031a3b5d3a3ea2ac2c18d7752d9e293386210b3ba20a259027e727b5871cc153`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[15]::Expr

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `63430588b005dd401236630998e83a454a69836f24a22dde3eb05a5fb66d471d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[15].value::Call

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `ff897d116f75f8992c76f006f163021570e79dc9eba91992fea14d386ef58462`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[16]::Expr

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `bda24c2b7c450451608cbcce26780431a49325063ba59b13b1608f5f0aa67c31`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[16].value::Call

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `2690f90d4a64211301762d0707a73563a49d0965a9fca7c72ac465bcc8be9510`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[17]::Expr

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `d7eb3e15f38f30286b80020bb2a08d65a7e75b5e32893fab8bcd5ace95f1dad6`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[17].value::Call

Source: `infra/agentinfra/roadmap_cli.py:35`; AST `0737dc24177da7bc02e079c89728120266f5324b422afee7d13c669d8c1d9e4b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[18]::Assign

Source: `infra/agentinfra/roadmap_cli.py:36`; AST `23ba405c9d5b979b5a102e44e7c843ac35214de43deac116a2f3fc2d5a5c53b2`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[18].value::Call

Source: `infra/agentinfra/roadmap_cli.py:36`; AST `704d503637bf1a5f74b2cc3acca5a790df6cb5fede5f95387b85094ce6f8fb99`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[19]::Expr

Source: `infra/agentinfra/roadmap_cli.py:36`; AST `dd3118bf1a1a71ba50dba1e131531a44a4b4efb127f68c304429be148fafabae`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[19].value::Call

Source: `infra/agentinfra/roadmap_cli.py:36`; AST `3f1b3ad3074bb4ac27d488d71caa0721f6a17fec34fdcc3e48a933e7b2720e21`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[20]::Expr

Source: `infra/agentinfra/roadmap_cli.py:36`; AST `d7aea0fa794e0a695536747e525cd24f68ccb1267b6c94f570be91c361b79957`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[20]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[20].value::Call

Source: `infra/agentinfra/roadmap_cli.py:36`; AST `b91ee5bdca65b7ab052bad9155a8d93f72985fe8d187a507c6211f3443c12de7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[21]::Assign

Source: `infra/agentinfra/roadmap_cli.py:37`; AST `a1ce0bda12b256465984121700f86cfd6309c08e8561b2e1149c531c47491255`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[21].value::Call

Source: `infra/agentinfra/roadmap_cli.py:37`; AST `913e2d4581ab2a05fa25ca4bf9b556897dba1a4aeb7210b096ab5d738f7c4d4d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[22]::Expr

Source: `infra/agentinfra/roadmap_cli.py:37`; AST `a56b779ba53c8e307473edb4eb27537593bbe5ce6605c3b005e43484705d64a5`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[22]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[22].value::Call

Source: `infra/agentinfra/roadmap_cli.py:37`; AST `1c6d4e2ab2c5c74680addb4a3db620ffddd384e482439f1f8ba748ae8718b847`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[23]::Expr

Source: `infra/agentinfra/roadmap_cli.py:37`; AST `d7aea0fa794e0a695536747e525cd24f68ccb1267b6c94f570be91c361b79957`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[23]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[23].value::Call

Source: `infra/agentinfra/roadmap_cli.py:37`; AST `b91ee5bdca65b7ab052bad9155a8d93f72985fe8d187a507c6211f3443c12de7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[23].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[24]::Assign

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `6c764de193826fe7a95c3337010aed460dee9e2bf7b6acbaf69c9b6ff8d68927`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[24]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[24].value::Call

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `0be5fa693a187288b2d71c58989615b2e5a0eee8c0925cae5554252a7b4e86c5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[24].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[25]::Expr

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `e3bf4661078c7f87c12b5dd92f70c61fb3cc8073e6fd088c71b8053a8474b6d7`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[25]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[25].value::Call

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `f497d0d2312b12f0f32fb1bdeaab42e0e9c46545168a7738bdff9989767e74c4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[25].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[26]::Expr

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `eaf5f957214a8d1af9687eaf932ec23ea36d1bb3793b3206509247d8dfc5bf90`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[26]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[26].value::Call

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `e8c6bf82b47e6c36a39f63171cc4dccaa9a810d546815ef486682bbc59a9e0e4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[26].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[27]::Expr

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `6bc000dd6b872633d35140708daad5c6372a919b52d4aa5b1c588dfbe8ef74cc`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[27]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[27].value::Call

Source: `infra/agentinfra/roadmap_cli.py:38`; AST `d87ab632fb02b68ea48087a425757cbc0cb332903a0f3969f0fb2a3e440bf857`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[27].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[28]::Expr

Source: `infra/agentinfra/roadmap_cli.py:39`; AST `c4ad04cc59fd70e0a8871e839c495b902ffbf81a86a64cb719ff3f80a1e12d66`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('profile').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[28]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[28].value::Call

Source: `infra/agentinfra/roadmap_cli.py:39`; AST `1f9467b31e5914cf2cd612b4a812262d56361fc525c7d1c1f55402b37b51c52c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser, r.add_parser('profile').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[28].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[28].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:39`; AST `7b27e0b529f4a60bca190aa562022878ef20dc27807619bc2eb3af68e6fbc188`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[28].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[29]::Assign

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `764a8e5962e08ae964b525635c9686004f60743eb961ed737f81c221108c23e9`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: a.
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[29]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[29].value::Call

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `723674b65100f7583af2b0149ae9a0666154946fa3698e626c20458bb1509737`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[29].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[30]::Expr

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `ef8a5ec404f3b7b62c1658939c6af4dd5b62b4995bdd815b0a590c7d75cb2cac`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[30]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[30].value::Call

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `c45ad4c42d166fbb29668421bc072023b18df0e6c8d4fc6cceb0b21e73774282`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[30].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[31]::Expr

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `c4f842a8c103a30e25972e348908b87879772e85bf5970f812ff8bde440c44f6`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[31]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[31].value::Call

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `b6088a505e65cd6b4e3753b0eba9411ed0e5f1ec51e2ffd75d0c161064f93a7c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[31].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[32]::Expr

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `8c0859270f7c24a4db3ad7c500970156dda38f3c3965c3c1649a586f65e5921c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[32]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[32].value::Call

Source: `infra/agentinfra/roadmap_cli.py:40`; AST `921985407210d4279bdf25f9311b5ce8f3806ea90f60d8248a17d8fbe52e34c9`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[32].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[33]::Assign

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `a4a01e2e98ccf1b812b794269f42ca1b8753dcf59df1e18353ad0b3b32fc5243`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: c.
Calls/effect boundaries: groups.add_parser, groups.add_parser('codex').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[33]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[33].value::Call

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `bbe70fa476fdcc70f780367dd50f4e8da1b3fd1840f711490e77f1ff4c29b582`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('codex').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[33].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[33].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:41`; AST `e4c4f7fa1d3d8f2218821782d254c78d0e15ad3fe1308cda6efcdd0e7b771df5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[33].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[34]::Expr

Source: `infra/agentinfra/roadmap_cli.py:42`; AST `287e077363dd175f7c4d056ea1e02f448a3e7cbcce0aaabf99662ba69ec087b1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[34]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[34].value::Call

Source: `infra/agentinfra/roadmap_cli.py:42`; AST `fe8db032ff91c4b696c4534987f3c9931ab5df709e01f2420aa63dea8e48b95b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[34].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[35]::Expr

Source: `infra/agentinfra/roadmap_cli.py:43`; AST `79a7d58c70480f663238649815032ce683598a498edc5ffb5f6019011c30a6d9`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser, c.add_parser('read-goal').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[35]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[35].value::Call

Source: `infra/agentinfra/roadmap_cli.py:43`; AST `5f2c2e8d9deab27a3c47ecfc56c993d76de6040630d78d41b5d4072cbe196867`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser, c.add_parser('read-goal').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[35].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[35].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:43`; AST `272af53e82adb4cf28e95ef2130c57ac6dceb176c592084bac857dcade512a5a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[35].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[36]::Expr

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `eaaabaf6b912b42070a7d0fe27708f94e4a0812538592393a6455bf3d275de83`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[36]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[36].value::Call

Source: `infra/agentinfra/roadmap_cli.py:44`; AST `910594d838cf7312584529870c45f27c71a6b87f1ca6c261ab90ee073bbfad20`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[36].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[37]::Expr

Source: `infra/agentinfra/roadmap_cli.py:45`; AST `01fdf8ac2c569ad6859e507ebf63f03350e8009f151a00600c58053631905e1a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, int. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser, c.add_parser('rebind-process').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[37]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[37].value::Call

Source: `infra/agentinfra/roadmap_cli.py:45`; AST `c9d7c6dbefbeb067884dc9bc32736beab2306b03050f3e65aa141e50f291fa28`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, int. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser, c.add_parser('rebind-process').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[37].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[37].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:45`; AST `b0dd790764701c71b5c47b714958fa519ae8f14d91c6260b04123cd417f6d20b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[37].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[38]::Assign

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `b9a4ebe32ed229cd9bfbb3886a2d90577a0f3d97a4fe779b2e55554603786325`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: a.
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[38]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[38].value::Call

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `19393664434dae5299cfa3d3105081d2709bd925b965e49fa828decef88ae98c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[38].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[39]::Expr

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `e37a4d9aa349c13b27d12a2392421df17990757d2bd592f03b7c43dab683f448`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[39]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[39].value::Call

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `96529487d76d563575ca4fae62fd52a978b89b68ccaeb8936641563459141044`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[39].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[40]::Expr

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `c82940990a3eaefda719781d620b844a060d010693774425cc7408e79478e599`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[40]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[40].value::Call

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `6b09dfa70bdb143f613d12ad71df20d51212bea470c20499b2f915f7ead829b3`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[40].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[41]::Expr

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `71e92d969bc2a96b3d7bee5b5885efdb4685b2badb016029d77d846b5b460b46`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[41]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[41].value::Call

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `2189d4b16c8b0bb3f808bd4d0a741b37c6f8eba5a957592586574f5397dd2760`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[41].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[42]::Expr

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `32a412bdbbe8ae9899ab6f8883f8a310f05512218a9c6f38e763316e433ab705`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[42]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[42].value::Call

Source: `infra/agentinfra/roadmap_cli.py:46`; AST `6106722c7c804d1b5c71a524b6ae77c71a814e74b609a35a319178b0bd112f3a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[42].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[43]::Assign

Source: `infra/agentinfra/roadmap_cli.py:47`; AST `3d5bbba231e2f91c623e2c84a8ad6a4013077edfae441aba83a1dab5ca7881a4`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: a.
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[43]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[43].value::Call

Source: `infra/agentinfra/roadmap_cli.py:47`; AST `0aa3e8eb242378ebe5dad1847bc477c6970c02cbe0c9597befae1c64be07e577`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[43].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[44]::Expr

Source: `infra/agentinfra/roadmap_cli.py:47`; AST `c0d5ee1e30b6205c18610cd6dbf33bfd2f45c3492c768e673fc7c21d3d01d64c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[44]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[44].value::Call

Source: `infra/agentinfra/roadmap_cli.py:47`; AST `3c552efbfebc9cc29748e714ee23f12d46ca9600259029e566fcdbccfe77e048`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[44].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[45]::Expr

Source: `infra/agentinfra/roadmap_cli.py:47`; AST `c2ab40b9dbfd3f50012d6ae1ec9bf0976843b80278107fc6b61a4bc445b1208a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[45]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[45].value::Call

Source: `infra/agentinfra/roadmap_cli.py:47`; AST `f52304d1aad02d069bcbdf8a816810c03283600222e1e911fc0dbbeda00649e5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[45].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[46]::Assign

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `3a159d8709f69f7fc88c900165737ec8eb09435b2069be2f64936921a3d6c4f1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: a.
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[46]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[46].value::Call

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `53abee8bd76449923c5f40cd3f09bbd7ab27c1a734ca2e9ee74a3e680605d687`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[46].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[47]::Expr

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `5b9e6150c43a9c0e52e24b85c4d3853fda3a2f190e332d5271435ec91b316005`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[47]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[47].value::Call

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `8f52639ff87f62d49c908f1769999970c0bcbaa022defd3418f90cd013fae8a0`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[47].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[48]::Expr

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `b425e17ee822af2386aa8d581e5adce32228200c0408f41ce1142d493c68a0b5`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[48]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[48].value::Call

Source: `infra/agentinfra/roadmap_cli.py:48`; AST `89ceccc11a51fc88875f3eba472140b04e7c157486a2c5fa55eb4972c5866b5d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[48].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[49]::Assign

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `842efa54cc7a5f08b52b619d4e576e5bd359a10620dff76d88a971f26640dc5d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: a.
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[49]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[49].value::Call

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `d92bfda9042696f53321d9ef4bd090c2cafb9e6e7dd56e4c9c524888777c1209`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[49].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[50]::Expr

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `fe55ba69edcac54af71da747f370dedb174329188361b57a6d1a4ec7f9b321e0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[50]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[50].value::Call

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `8a87b3d3016576005ef0cfd4a197f8d405b10a93ef5639160cd3bdb6ddce272b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[50].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[51]::Expr

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `a485fbfbc58182583fd3694a58dd82a28fd1dfaa31fae689d80fa02059e5c092`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[51]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[51].value::Call

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `e70ba37c00e188d759ab36d85fa5ebbf87a73bcf2765a878c71961a9f90ab5cb`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[51].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[52]::Expr

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `8d6ba6f7cc09aa62911d0be05059eb6fad8553dfc2e4157f7a9980a1593a86b4`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[52]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[52].value::Call

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `2b7a0000b9ed04baa95397f271511e5f41076f1203dbc4f6498f8bb952b62f93`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[52].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[53]::Expr

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `43d85dab326783c19f03be0e071b24f7144e15c3cc32f370ed52986421a69674`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[53]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[53].value::Call

Source: `infra/agentinfra/roadmap_cli.py:49`; AST `fd49d79bb5807849d8683ee17042036525ee17ad9b8dff7b28b7588bd8be62cb`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[53].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[54]::Assign

Source: `infra/agentinfra/roadmap_cli.py:50`; AST `9ac91b03d8f39868fa366e5663436b77cf33bfe27e1f8bd12b6662ac66328de1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: v.
Calls/effect boundaries: groups.add_parser, groups.add_parser('verification').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[54]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[54].value::Call

Source: `infra/agentinfra/roadmap_cli.py:50`; AST `62c8bd5fdca8515b2a2033c484c6ba785dca5dae05798cfb7169fd13a8daf660`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('verification').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[54].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[54].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:50`; AST `535ea8de47f9f7142c88349bb5786f9889ec58dc6fd206f1ac347058ee8eea2f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[54].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[55]::Assign

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `a1b75be477794363a19277ab398320b98d4547033e0c295d06c830bccb5897a2`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: v. Outputs/bindings: a.
Calls/effect boundaries: v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[55]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[55].value::Call

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `e67efe9cf70347db3754444d8d7e75aaa26ff65056a0ffef3388b603c9164900`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: v. Outputs/bindings: (none).
Calls/effect boundaries: v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[55].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[56]::Expr

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `531b11a9328c0be6c3fe5f15f535b9d8a98a6f3958bfd9f1782d88ae816d12e0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[56]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[56].value::Call

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `925c6cbb6e7cf12e10c0d8c37940b969dcdf6c923fcdcb33566a5f08f4024704`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[56].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[57]::Expr

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `ebfbdda927643885aa1b488d70da44db3b26c878155901cdb758f4c4f05d613e`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[57]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[57].value::Call

Source: `infra/agentinfra/roadmap_cli.py:51`; AST `ec9aecd10fa86e8c00077b24bccd48bc982802bf0916bc853970ce4b71ff23d1`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[57].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[58]::Assign

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `51dc696785a7b7936a593ca4f2612dc2cc3eba2a2596a12ead580c0bae998765`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: v. Outputs/bindings: a.
Calls/effect boundaries: v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[58]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[58].value::Call

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `4080abe0faf2568fc16cc4f6291eddb4c9768f25e250cc2ff1d4da6f3d687399`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: v. Outputs/bindings: (none).
Calls/effect boundaries: v.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[58].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[59]::Expr

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `7dce0795c7e6dd95d825de79692e5acb237454821ed836368824370080f6575f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[59]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[59].value::Call

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `a775df190be8c5ed7ab113e7549218db03a8321546b14edb7fb64c95e40a7997`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[59].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[60]::Expr

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `4b1e14ece0982af96c2762959211e3d583884ee2f3b9bebbb88f1b84e47f63fa`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[60]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[60].value::Call

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `002611d0889b889da6b0be651a39aed59e44d474c2ba3e12384292c3e1a02a76`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[60].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[61]::Expr

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `6e2897d3db4e86f9d6f543dd98d505190bb3c8c45d3f3d7cb8123b8088d4c04a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[61]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[61].value::Call

Source: `infra/agentinfra/roadmap_cli.py:52`; AST `459e59eefb8b675c1bb126f8798081f94416cda40ff4392bead9326cadff5b5a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[61].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[62]::Assign

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `735a9ba7a7f611b3f83d8e4774debf82670fc941eb484ecce094336065961be0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: b.
Calls/effect boundaries: groups.add_parser, groups.add_parser('budget').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[62]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[62].value::Call

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `59c27d9e3797d9ee37be152cd5f9c9db71844600d295e9bdf7dcf2fdb8aa94d5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('budget').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[62].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[62].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `2ade4a9d9cce96664c01cbe2fb196b5394d2f05909af8d60282fcdb621e99af7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[62].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[63]::Expr

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `00af5968639af7bd7c3df8916f9044761e023015e49fc86b7fe2fffc5aa7e2d8`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[63]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[63].value::Call

Source: `infra/agentinfra/roadmap_cli.py:53`; AST `e61633fde93f0e88325f9dbeeac982ad446b656e67bbfd727673c219907a37a4`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[63].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[64]::Assign

Source: `infra/agentinfra/roadmap_cli.py:54`; AST `3bee63ecf90e9987c99ee7eb14c09d74abec2dbaaba17e09c99baf537bbc5936`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b. Outputs/bindings: a.
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[64]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[64].value::Call

Source: `infra/agentinfra/roadmap_cli.py:54`; AST `0788958feb4134253b9ffc18bbf4850df395582f89866477ca2a0aecbd4f49ef`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[64].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[65]::Expr

Source: `infra/agentinfra/roadmap_cli.py:54`; AST `c82940990a3eaefda719781d620b844a060d010693774425cc7408e79478e599`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[65]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[65].value::Call

Source: `infra/agentinfra/roadmap_cli.py:54`; AST `6b09dfa70bdb143f613d12ad71df20d51212bea470c20499b2f915f7ead829b3`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[65].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[66]::Expr

Source: `infra/agentinfra/roadmap_cli.py:54`; AST `c9d5df6a05dae1cc585eb20b3eaaeea919dc5749eef85f6a35a7cc7abcd2bad0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[66]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[66].value::Call

Source: `infra/agentinfra/roadmap_cli.py:54`; AST `2696138e272bca18cab5f8f64e805743a6ea0ea9afb8006672b66139e13d93b7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[66].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[67]::Expr

Source: `infra/agentinfra/roadmap_cli.py:54`; AST `6b6feceac1fb19f983200ba12442a9f80d3b5a2787607d1842a883a1901ee239`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[67]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[67].value::Call

Source: `infra/agentinfra/roadmap_cli.py:54`; AST `be71e91c80c330c713f4e4de1f31902cfc4ee15e48d244bad2be7d984f3eb79f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[67].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[68]::Expr

Source: `infra/agentinfra/roadmap_cli.py:55`; AST `c7d3cfbe2b2f4ecb4a69b55368b0d1aca92771f3ac1d6fbfe3210ba5dc3eb787`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[68]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[68].value::Call

Source: `infra/agentinfra/roadmap_cli.py:55`; AST `f7be307bb0783f6d1d8a8bf3e255b32c5e276cd789214abaad384729d1622c4d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[68].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[69]::Assign

Source: `infra/agentinfra/roadmap_cli.py:56`; AST `17c4731a0d0e893860a561632e8e6cc1aa2bf7aa014da9bf935ffc4df510c728`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b. Outputs/bindings: a.
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[69]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[69].value::Call

Source: `infra/agentinfra/roadmap_cli.py:56`; AST `3b5e0e25e39802edefa4e916880951d67df1d6ba5ac54c17a973b3f799d4f6b5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[69].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[70]::Expr

Source: `infra/agentinfra/roadmap_cli.py:56`; AST `3aa1dc9b284ec5471c7311c52d53fcb3fb68748887c0e57e3ac995b6d23bffba`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[70]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[70].value::Call

Source: `infra/agentinfra/roadmap_cli.py:56`; AST `944013b3e68c03f18f6dd717e40404885d477d47cf14a28aa2a42edceb1b00e3`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[70].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[71]::Assign

Source: `infra/agentinfra/roadmap_cli.py:57`; AST `5cf8db1a5d356600d0d1d3adabb6536d76b02348463aaf47d1b17825cc92e6fc`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b. Outputs/bindings: a.
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[71]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[71].value::Call

Source: `infra/agentinfra/roadmap_cli.py:57`; AST `1a58b83178a83d04f4a9ae4e8540735c87be833697335af79ed814d353bca8f0`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: b.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[71].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[72]::Expr

Source: `infra/agentinfra/roadmap_cli.py:57`; AST `3aa1dc9b284ec5471c7311c52d53fcb3fb68748887c0e57e3ac995b6d23bffba`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[72]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[72].value::Call

Source: `infra/agentinfra/roadmap_cli.py:57`; AST `944013b3e68c03f18f6dd717e40404885d477d47cf14a28aa2a42edceb1b00e3`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[72].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[73]::Assign

Source: `infra/agentinfra/roadmap_cli.py:58`; AST `8d7b412a970ea44d160cb5bf42f6ea130a678851c5374ce87d0f2242b7ea5ebb`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: r.
Calls/effect boundaries: groups.add_parser, groups.add_parser('review').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[73]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[73].value::Call

Source: `infra/agentinfra/roadmap_cli.py:58`; AST `004b21daf1bc93b418195098a3049d4eea32e29caef05dd727b356995b908a91`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('review').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[73].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[73].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:58`; AST `7ef2964c46579a87c89720f5cd7f826c0ef91210e4993ae34a32d8e4c9684043`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[73].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[74]::Assign

Source: `infra/agentinfra/roadmap_cli.py:59`; AST `1f33b4f552ee8c9ab8a9b6e13fda178f96f48fe0a71040f91191b77e79892d21`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[74]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[74].value::Call

Source: `infra/agentinfra/roadmap_cli.py:59`; AST `aeaaa8d6fd333e6c2699eb5f0756cda380be40a9bb1324e07747b51d98112448`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[74].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[75]::Expr

Source: `infra/agentinfra/roadmap_cli.py:59`; AST `2887208acd2a4455692c96521261ade0eab8372189d3ac6d588febeca1595d0b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[75]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[75].value::Call

Source: `infra/agentinfra/roadmap_cli.py:59`; AST `68130a57d27d804ce68d4c033ac36babe7d6a6ac9be99f1c3ca0704516260517`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[75].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[76]::Expr

Source: `infra/agentinfra/roadmap_cli.py:59`; AST `882f89f3fd646937b6ab51176aebdcbd1a0cd63ee8940c0385947fb5b018b1ae`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[76]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[76].value::Call

Source: `infra/agentinfra/roadmap_cli.py:59`; AST `ed59d7d8b165ec868fa0f82c9021da4367d6af7acf07ee52b7b829161e2b2dce`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[76].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[77]::Assign

Source: `infra/agentinfra/roadmap_cli.py:60`; AST `92a11b27a344984e5d0083169e6e5251d5b09791e7390c22a028ab1f66cef576`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[77]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[77].value::Call

Source: `infra/agentinfra/roadmap_cli.py:60`; AST `7983ed6a649832814140ede8ae23ba7464c9a41b7e958c01cef14026be9139fc`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[77].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[78]::Expr

Source: `infra/agentinfra/roadmap_cli.py:60`; AST `2887208acd2a4455692c96521261ade0eab8372189d3ac6d588febeca1595d0b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[78]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[78].value::Call

Source: `infra/agentinfra/roadmap_cli.py:60`; AST `68130a57d27d804ce68d4c033ac36babe7d6a6ac9be99f1c3ca0704516260517`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[78].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[79]::Expr

Source: `infra/agentinfra/roadmap_cli.py:60`; AST `068d7126eac73f88ea17156a6c54b194dee5e50900d2edfc085488322df09cc9`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[79]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[79].value::Call

Source: `infra/agentinfra/roadmap_cli.py:60`; AST `1de64bf94ca5e5b99f5006d36789ac323c6c26bb7996b87f058c0292c2705687`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[79].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[80]::Assign

Source: `infra/agentinfra/roadmap_cli.py:61`; AST `248a84df2fb9affae88171dd40f03a4b912929221ebd55dd538c7bff006d9b3c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: a.
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[80]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[80].value::Call

Source: `infra/agentinfra/roadmap_cli.py:61`; AST `dce5d5f7fd7ee97ae4e9daceaaf035bd5d1484425eb79c4a52ac1a4eb8f78d2d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[80].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[81]::Expr

Source: `infra/agentinfra/roadmap_cli.py:61`; AST `5f7dd24ced1606201e72daee4fcf61a91284adb1672e1cabf0563dbfc01464ee`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[81]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[81].value::Call

Source: `infra/agentinfra/roadmap_cli.py:61`; AST `0ea5718ae31e75efda1fcea1ce7849822baf95b019d7549f1ff671cc09a94f40`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[81].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[82]::Assign

Source: `infra/agentinfra/roadmap_cli.py:62`; AST `3cbb2dcf48f6859c62b1a5dbf846fd11ee7410727b6d83e8876443357f24ce1c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: a.
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[82]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[82].value::Call

Source: `infra/agentinfra/roadmap_cli.py:62`; AST `7a383a5a9182412cff7abce664e23a45c46563d24f3a2e55c057d84ff62fb33f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[82].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[83]::Expr

Source: `infra/agentinfra/roadmap_cli.py:62`; AST `df14bec3101d63dd0f91777dd229c227a7ac90144b8e51d40cf99082c3d638ee`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[83]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[83].value::Call

Source: `infra/agentinfra/roadmap_cli.py:62`; AST `bc134093f7a57fcb709e49e3242475a1f35a45641aae995d1e08bc2724868ddb`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[83].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[84]::Assign

Source: `infra/agentinfra/roadmap_cli.py:63`; AST `4bccbd1c1da7c4cbbdf97bc5b6b1f1606fab311e9c7ba31c80f1f08dca67d14a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: a.
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[84]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[84].value::Call

Source: `infra/agentinfra/roadmap_cli.py:63`; AST `7b78cdfa4c0f2af9894674b5dc09f74946df9ba208826a1e0fd5d5dbb1bef23e`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[84].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[85]::Expr

Source: `infra/agentinfra/roadmap_cli.py:63`; AST `66e779575fa3fedb27ecac860048980574989dbaaa77a6c03ecf01493d6e313b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[85]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[85].value::Call

Source: `infra/agentinfra/roadmap_cli.py:63`; AST `da44aa014432b1ad99cd6ac42a4e0ab5059f8633c71728ef8957011d126be297`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[85].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[86]::Assign

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `4921bef45f64d4e3ec46ed4bd918692ad841bc750c2a04b8f59837862dac8fd0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: a.
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[86]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[86].value::Call

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `fbe6eb869a621e947c12c5f0e612f91a4948a8f2ca630e3b36cd4e7726fdc0be`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[86].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[87]::Expr

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `e91064d5161e9cd38ed2c50840ad437bd1200a11e053f407932b45b483d9cec7`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[87]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[87].value::Call

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `a8ec9547f4d23916c6d09ea30ca5d98ae042c4b7a03ecd9256c9a082f867de86`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[87].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[88]::Expr

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `339d86fd78ef28936cb867f22d96889136425a29f46206a30c6a1dfa99198192`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[88]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[88].value::Call

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `f0a96293a59ab077ec08fe10c5ca219499f3fb4a5f63778d3b080efc8e2470dc`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[88].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[89]::Expr

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `1569a706aa9235e0941f9875c3145b4d0842bb09629da548002e9fec438f5609`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[89]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[89].value::Call

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `c5f07cc256b9397aec97c29669c42da59e084b87f1b7b89e67803019b25bd002`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[89].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[90]::Expr

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `431c1f251716d5b79d3cb5cc3cb6a1cdd75868d72aa8ebfe4d73d6f1cf526547`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[90]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[90].value::Call

Source: `infra/agentinfra/roadmap_cli.py:64`; AST `beaa7ea323bde41f0404b821d5c58e6ee4cb36763d52f76e51b6d16315ea825b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, int. Outputs/bindings: (none).
Calls/effect boundaries: a.add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[90].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[91]::Assign

Source: `infra/agentinfra/roadmap_cli.py:65`; AST `45d35406263fabf0a0750054582eff140c3d48ef1c3aac57301c6e5d3f9a247b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups. Outputs/bindings: i.
Calls/effect boundaries: groups.add_parser, groups.add_parser('interfaces').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[91]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[91].value::Call

Source: `infra/agentinfra/roadmap_cli.py:65`; AST `c7f0195e15b5d076124ef72e85571e13b676d6e6402cd386acac0107b9d7233a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser, groups.add_parser('interfaces').add_subparsers.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[91].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[91].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:65`; AST `0ee2fba04d79ea2c5aa9a517648f3b77009d63b7794cbbbdfd7667712f4d3a57`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups. Outputs/bindings: (none).
Calls/effect boundaries: groups.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[91].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[92]::Expr

Source: `infra/agentinfra/roadmap_cli.py:66`; AST `55b3f3b1ca850a68d30112766dc33d3d555fff7036dc9733be1adb4b5f7e3722`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: i. Outputs/bindings: (none).
Calls/effect boundaries: i.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[92]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[92].value::Call

Source: `infra/agentinfra/roadmap_cli.py:66`; AST `395f9b1a146b98a3d98b89651623f809e26c0152bb3e365ef78d02f8ea4a58bd`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: i. Outputs/bindings: (none).
Calls/effect boundaries: i.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[92].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[93]::Expr

Source: `infra/agentinfra/roadmap_cli.py:67`; AST `ab37e1be6b7d57b94deddf8ce5ae42d9619231f787b55c60218f7529376d27c0`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: i. Outputs/bindings: (none).
Calls/effect boundaries: i.add_parser, i.add_parser('compare').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[93]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[93].value::Call

Source: `infra/agentinfra/roadmap_cli.py:67`; AST `ec76f9f5cb99dce53d11d1b2a34709159543cae5d3f72412ff9617c2c50172d7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: i. Outputs/bindings: (none).
Calls/effect boundaries: i.add_parser, i.add_parser('compare').add_argument.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[93].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[93].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:67`; AST `1e3864ca608fe6d5c0e4d9011e1e23a1e217af961dfcfad6a46f3d59bf8ec4ac`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: i. Outputs/bindings: (none).
Calls/effect boundaries: i.add_parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[93].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::parser::root.body[20].body[94]::Return

Source: `infra/agentinfra/roadmap_cli.py:68`; AST `cb7563fa3b6c0b90880aba1ea365b272a9a70d833d2d33fa1733c5f883e28868`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[20].body[94]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21]::FunctionDef

Source: `infra/agentinfra/roadmap_cli.py:71`; AST `595cae8d435362cf3e4c94eaa32c8ae7e1e9794856f64719e8cb269e93925643`.

Rust module: `infra::agentinfra::roadmap_cli`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, ContractError, ProjectAdapter, WorkspaceLease, a, adjudicate_findings, assemble_implementation, atomic_write_text, audit, audit_evidence, authority_inventory, authorize, bind_goal, bind_plan, capabilities, check, compare_interfaces, compile_roadmaps, compiled, confined_path, decision, dict, digest, errors, evidence, goal_transition, inventory, ledger, obligation, observe_interfaces, output, owner, packet, project_into_record, proof_errors, proof_result, publish, python_proof_errors, read_json, read_native_goal, reconcile_inventory, reconcile_native_transition, reconcile_original_tests, record, recover_operation, refresh_implementation_dependencies, render_packet, request, retrieve, review, root, run_recipe, save_compiled, save_inventory, str, validate_decision, validate_record, validate_skills. Outputs/bindings: audit, compiled, decision, errors, evidence, ledger, obligation, output, owner, proof_result, record, request, review, root.
Calls/effect boundaries: BudgetLedger, ContractError, ProjectAdapter, ProjectAdapter(root).read, ProjectAdapter(root).rebind_native_process, ProjectAdapter(root, a.project, profiles=compiled['projects']).describe, WorkspaceLease, WorkspaceLease(root).qualify, a.milestones.split, a.root.resolve, adjudicate_findings, assemble_implementation, atomic_write_text, audit_evidence, authority_inventory, authorize, bind_goal, bind_plan, capabilities, check, compare_interfaces, compile_roadmaps, confined_path, digest, goal_transition, inventory, ledger.metrics, ledger.observe_usage, ledger.read, ledger.reservation_record, observe_interfaces, packet, project_into_record, proof_errors, publish, python_proof_errors, read_json, read_native_goal, reconcile_inventory, reconcile_native_transition, reconcile_original_tests, recover_operation, refresh_implementation_dependencies, render_packet, request.get, retrieve, run_recipe, save_compiled, save_inventory, str, validate_decision, validate_record, validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:72`; AST `79f35e3dd72e6dfce47e3635b369764f01c3076e2afc775f888cf3623afcbe82`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a. Outputs/bindings: root.
Calls/effect boundaries: a.root.resolve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:72`; AST `e8091945a45887165301774a3ac5ca0ff6f6c3cf96c857f6524674dbbb816b9f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.root.resolve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1]::If

Source: `infra/agentinfra/roadmap_cli.py:73`; AST `54a4dda336163d7e91edfffb864cf7cb890ac2738ac603016bcba93f7fde2c85`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ProjectAdapter, a, assemble_implementation, audit, audit_evidence, authority_inventory, compile_roadmaps, compiled, evidence, packet, project_into_record, read_json, reconcile_inventory, record, refresh_implementation_dependencies, root, run_recipe, save_compiled, save_inventory. Outputs/bindings: audit, compiled, evidence, record.
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root, a.project, profiles=compiled['projects']).describe, assemble_implementation, audit_evidence, authority_inventory, compile_roadmaps, packet, project_into_record, read_json, reconcile_inventory, refresh_implementation_dependencies, run_recipe, save_compiled, save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1]; no call, error or mutation may be omitted. Condition: a.family == 'roadmap'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:74`; AST `8deac8da987fee33047b87c849024fe4b35da2d8f7167922e3c744059f79a3b1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:74`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[1]::If

Source: `infra/agentinfra/roadmap_cli.py:75`; AST `f6d020ffdd877094286f7587bbb1b6b05b0e88e7359d1c5c6caab9ffce0b4aaa`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, compiled, root, save_compiled. Outputs/bindings: (none).
Calls/effect boundaries: save_compiled.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[1]; no call, error or mutation may be omitted. Condition: a.action == 'compile'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_cli.py:76`; AST `2831da051a07a3fd00e69bfa4c61012066019809684d277c2bbb3aafb7dd6f79`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, compiled, root, save_compiled. Outputs/bindings: (none).
Calls/effect boundaries: save_compiled.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[1].body[0]; no call, error or mutation may be omitted. Condition: a.save
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[1].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_cli.py:76`; AST `14e8a80bc21d0ae3652a959443ecb7aba34beb1db31da32791603d6af017399d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, root, save_compiled. Outputs/bindings: (none).
Calls/effect boundaries: save_compiled.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[1].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:76`; AST `58d259b1074dcd62ede16a454a8895ab259d355c6864597b31b8e6d26bfd50be`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, root, save_compiled. Outputs/bindings: (none).
Calls/effect boundaries: save_compiled.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[1].body[1]::Return

Source: `infra/agentinfra/roadmap_cli.py:77`; AST `92976245473cda52a06eb9d15364d44da96631301bc207c683dfe72632458e44`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:78`; AST `245f27baaaa8518746edf736be33f203e7905c315962267294139eed9ca124dc`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, authority_inventory, record, root, save_inventory. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory, save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[2]; no call, error or mutation may be omitted. Condition: a.action == 'inventory'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:79`; AST `e81acdaa3b233e455f1c84080e10ddd499a45c29142fd1572da1bee8b106cdf6`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, authority_inventory, root. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:79`; AST `2e577ab27acd72b09a76021cf0f9a3d521d2edf99bac989808cfe9cfcd33b678`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, authority_inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[2].body[1]::If

Source: `infra/agentinfra/roadmap_cli.py:80`; AST `5af3af8404b85183e106e3bc4fd159b34558319b3f7a69d0038ba322cfbef5db`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, record, root, save_inventory. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[2].body[1]; no call, error or mutation may be omitted. Condition: a.save
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[2].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:81`; AST `a3ecb08dd0f68713f85439403925bdbedda5007653cf191bb00d1bc2d96bee18`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, root, save_inventory. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[2].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:81`; AST `58347316038ab3e9efbe5f11758dcacdf73bfa09fe020f176e7abc4dfe272574`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, root, save_inventory. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[2].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[2].body[2]::Return

Source: `infra/agentinfra/roadmap_cli.py:82`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:83`; AST `12df41223f6cc02c7347cef5ef52dc570a0b2f5b294b5f54181c328faa7daa8e`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, read_json, reconcile_inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[3]; no call, error or mutation may be omitted. Condition: a.action == 'reconcile'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[3].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:83`; AST `3d9897098b34252d4194a5f1d04ffab02772ed1efc5f69df7c2242b818c7afa1`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json, reconcile_inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:83`; AST `b65137420a5bf73e44cb15b344b10f283878f89d82ed3a62a61e7527750de7ac`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json, reconcile_inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[3].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:83`; AST `f0ce24a1a2ed4f7895a254a16fe0d6a8f62209fbf23ca6caa0bc90c530ae0849`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[3].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[4]::If

Source: `infra/agentinfra/roadmap_cli.py:84`; AST `04833844582de327f5ec678ba181dd52086c43b6bb081e4d24164541fd8848eb`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ProjectAdapter, a, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root, a.project, profiles=compiled['projects']).describe.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[4]; no call, error or mutation may be omitted. Condition: a.action == 'profile'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[4].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:84`; AST `d3bf292c06b7c38b01e8a9b94178890778b2bf106c4a4454c08ec0842629d249`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectAdapter, a, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root, a.project, profiles=compiled['projects']).describe.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:84`; AST `d05a7e791478cb59f7c93541ab1cd2a99d89bee8075f1ca6e846cc07c48591ae`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, a, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root, a.project, profiles=compiled['projects']).describe.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[4].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:84`; AST `eba5eabab2003075d1a56f64664dcec9799fbbdc831f800e03c5d8b019cd54f3`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, a, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[4].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[5]::If

Source: `infra/agentinfra/roadmap_cli.py:85`; AST `ae2a3b7f03c51c8348e5117b9d3c83dc99f8a9e98d87c708855d9eddb47a67e3`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, compiled, root, run_recipe. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[5]; no call, error or mutation may be omitted. Condition: a.action == 'run'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[5].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:85`; AST `0a8a76593ce4a3ea9274b5cac526332a6ec4478aa4dfeda3eb9f400a518f0552`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, compiled, root, run_recipe. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:85`; AST `9581e1525ed509ea9d46b494b1c4a8759635cb8d16d3c2499bc36605ba0a2d34`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, compiled, root, run_recipe. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[6]::If

Source: `infra/agentinfra/roadmap_cli.py:86`; AST `5557bf75d4e76798e0c4b4e5189fcef861e4c53b5884138e8c9b19cc4c73c025`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, assemble_implementation, root. Outputs/bindings: (none).
Calls/effect boundaries: assemble_implementation.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[6]; no call, error or mutation may be omitted. Condition: a.action == 'accept-implementation'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[6].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:87`; AST `b9abc274c2efbe37a0e6e41e07fc651fec4b4b49f60a115e2b8d4926537a9e8e`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[21].body[1].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[6].body[1]::Return

Source: `infra/agentinfra/roadmap_cli.py:88`; AST `751c6698d655424c7a6b2ccdac87ed18229e94a4107bb35a2f363bf9842d7fb5`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, assemble_implementation, root. Outputs/bindings: (none).
Calls/effect boundaries: assemble_implementation.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:88`; AST `b8cb58b4d51e2aa4d431ee1d68a5154d595a4eedd61a469850b59cedbf73bd5a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, assemble_implementation, root. Outputs/bindings: (none).
Calls/effect boundaries: assemble_implementation.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[7]::If

Source: `infra/agentinfra/roadmap_cli.py:89`; AST `ade8a3b058142b61892e78b990974769414d348c38e701cc68b494e9c97803cf`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, refresh_implementation_dependencies, root. Outputs/bindings: (none).
Calls/effect boundaries: refresh_implementation_dependencies.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[7]; no call, error or mutation may be omitted. Condition: a.action == 'refresh-dependencies'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[7].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:90`; AST `92a8cb33b44bcb3e70ccb6eca857fb873bb407190d142aeb6a1d53c8e28198ee`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[21].body[1].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[7].body[1]::Return

Source: `infra/agentinfra/roadmap_cli.py:91`; AST `ffb7377fe84282c64b6cd1bf88623d56453d953a534554b7baa79df3bb17e3bb`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, refresh_implementation_dependencies, root. Outputs/bindings: (none).
Calls/effect boundaries: refresh_implementation_dependencies.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[7].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:91`; AST `3e19ad04454d2ef758adac1d85f0f43898da85a13c84f7a8111638792b082958`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, refresh_implementation_dependencies, root. Outputs/bindings: (none).
Calls/effect boundaries: refresh_implementation_dependencies.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[8]::Assign

Source: `infra/agentinfra/roadmap_cli.py:92`; AST `295be51fe27e4e884248ae9f08830d86dcb5609af75fa53f64a6c25be168e783`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, compiled, read_json. Outputs/bindings: evidence.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[8].value.body::Call

Source: `infra/agentinfra/roadmap_cli.py:92`; AST `fc25ea2cd6abde821bb1c3a2a02e2053cfb544754b883c3589b7e4894bb8c825`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[8].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[9]::Assign

Source: `infra/agentinfra/roadmap_cli.py:93`; AST `5b9bb2d45a4363d27939471107c4f967c1c80ff0a1d43d1e67785198f647c140`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit_evidence, compiled, evidence, root. Outputs/bindings: audit.
Calls/effect boundaries: audit_evidence.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[9].value::Call

Source: `infra/agentinfra/roadmap_cli.py:93`; AST `15e12735a35059c13d4e0dfc2ee22d0526ab26ef50db74dcba2999220bbcfb0c`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: audit_evidence, compiled, evidence, root. Outputs/bindings: (none).
Calls/effect boundaries: audit_evidence.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[10]::If

Source: `infra/agentinfra/roadmap_cli.py:94`; AST `f2768018683461dbd9e80a635938c8c42a62d97302e7b7fda3274a1804dd438e`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, audit. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[10]; no call, error or mutation may be omitted. Condition: a.action == 'audit'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[10].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:94`; AST `0e0c7b4c8f0a58f4fc44537e62bfb09aaf9562bce62ab0949405fb3ea08424d9`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[11]::If

Source: `infra/agentinfra/roadmap_cli.py:95`; AST `1e23778989d9cdb74c6b38d9abce355933ddcb2bdd07da74433ce08a9df52b21`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, audit, compiled, packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[1].body[11]; no call, error or mutation may be omitted. Condition: a.action == 'packet'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[11].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:95`; AST `9407424a9edf75c5b357e208a1942e3f720fd51a0b82be5b3c8c5a62018bd2df`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, audit, compiled, packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[11].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:95`; AST `65d70effdfa770e9b6709654e695fd32e4aaf2788be8b883cb41c4e554c6f1cb`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, audit, compiled, packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[12]::Return

Source: `infra/agentinfra/roadmap_cli.py:96`; AST `07d650373b04d59df181e2d935390e5da232b4522f9556de9b6dabb68633908c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, audit, project_into_record, root. Outputs/bindings: (none).
Calls/effect boundaries: project_into_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[1].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[1].body[12].value::Call

Source: `infra/agentinfra/roadmap_cli.py:96`; AST `4c516e41e82c04c7823a8877d0f188e97c14c71d69b6d1cef5ef1e800c0d6fc6`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, audit, project_into_record, root. Outputs/bindings: (none).
Calls/effect boundaries: project_into_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:97`; AST `9bcd36524e85445bc3c5cd168b786cf399ebe848ef79c6ba3feb560e20cf549d`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, authorize, read_json. Outputs/bindings: (none).
Calls/effect boundaries: authorize, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[2]; no call, error or mutation may be omitted. Condition: a.family == 'policy'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:97`; AST `38658a6f1850481d81e11b3a047dae179a3bde74200c32ad79df15730868c069`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, authorize, read_json. Outputs/bindings: (none).
Calls/effect boundaries: authorize, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:97`; AST `04f259d6440639ff562fba17978b5d95403ba9a53fd55a9335599dabcf8624c2`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, authorize, read_json. Outputs/bindings: (none).
Calls/effect boundaries: authorize, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[2].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:97`; AST `ae730821ef8d59cf26da05ed18b5192dfb66e1b27429f5e0c7254bf664d9cc9a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[2].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:98`; AST `dd1c33bed2f7a97cd9f5412cbc651d2ce139573b7c0cb1fadd547a6a72d198b3`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ProjectAdapter, WorkspaceLease, a, bind_goal, bind_plan, capabilities, compile_roadmaps, goal_transition, owner, read_json, read_native_goal, reconcile_native_transition, request, root. Outputs/bindings: owner, request.
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root).read, ProjectAdapter(root).rebind_native_process, WorkspaceLease, WorkspaceLease(root).qualify, a.milestones.split, bind_goal, bind_plan, capabilities, compile_roadmaps, goal_transition, read_json, read_native_goal, reconcile_native_transition, request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[3]; no call, error or mutation may be omitted. Condition: a.family == 'codex'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[0]::If

Source: `infra/agentinfra/roadmap_cli.py:99`; AST `b9de212170a4972ad65d795f8db4750c8951532110e1638a9de24581d595c58b`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, capabilities. Outputs/bindings: (none).
Calls/effect boundaries: capabilities.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[3].body[0]; no call, error or mutation may be omitted. Condition: a.action == 'inspect'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:99`; AST `515da2ca20337b4ec525cfaa31f0ed44a377c2696695f3f07079074207aa699f`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: capabilities. Outputs/bindings: (none).
Calls/effect boundaries: capabilities.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:99`; AST `3779a25857e47741422b43e04448f6a5fb5452309510474af85559d2512e1d70`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: capabilities. Outputs/bindings: (none).
Calls/effect boundaries: capabilities.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[1]::If

Source: `infra/agentinfra/roadmap_cli.py:100`; AST `2292d8990b2fee587f9c5a7ecad7c594478e0b9d7d1d2c9aed425be97715cae6`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, read_native_goal. Outputs/bindings: (none).
Calls/effect boundaries: read_native_goal.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[3].body[1]; no call, error or mutation may be omitted. Condition: a.action == 'read-goal'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:100`; AST `37b16d3c3e5605f5ddac4df5362dc9586ad3b8cc66e529d6225c1507aa6cb89e`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_native_goal. Outputs/bindings: (none).
Calls/effect boundaries: read_native_goal.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:100`; AST `9166b7feb5ec16c8e871783ece15c4886a0aaf224f323bd1f53ddc2c2b4f4e53`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_native_goal. Outputs/bindings: (none).
Calls/effect boundaries: read_native_goal.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `629a2a4c2cb462243703923cd316ecb30e0476fc10ee9062029942c7c174e2ff`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ProjectAdapter, a, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root).rebind_native_process.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[3].body[2]; no call, error or mutation may be omitted. Condition: a.action == 'rebind-process'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `a4662f0d4fa3cfd1e9a6f687d2b50ef0d0e4696697d5d6c70bc82dca903e955b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectAdapter, a, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root).rebind_native_process.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `274c4d71e11298805295d6d689ed0bc59063f7dbb8b0dbb88314ef255b0bb69b`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, a, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root).rebind_native_process.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[2].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:101`; AST `a885979b048414ab9ab482a4aaa51e20efe2db175d6aaf5096c07c6e15434558`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[2].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:102`; AST `e721d393e062b7c7f67336b1c856e386ec6bdb4c245b18df206b6edfae5d3e1b`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ProjectAdapter, WorkspaceLease, a, owner, root. Outputs/bindings: owner.
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root).read, WorkspaceLease, WorkspaceLease(root).qualify.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[3].body[3]; no call, error or mutation may be omitted. Condition: a.action == 'owner'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[3].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:103`; AST `09d8e9e8f6fd64b1de599cd7bc89a5b39b492565154c1945944f226444aab849`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[21].body[3].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:104`; AST `b4c68f9f7e142abe64f96b586807935033f17843a90f0c6c06c76565c897539b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectAdapter, root. Outputs/bindings: owner.
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root).read.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[3].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[3].body[1].value.value.value::Call

Source: `infra/agentinfra/roadmap_cli.py:104`; AST `aebfe9f0e99b7598f3da209b858f5afb31082b520cf878a8582e3946d9cfd8f6`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root).read.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[3].body[1].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[3].body[1].value.value.value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:104`; AST `a885979b048414ab9ab482a4aaa51e20efe2db175d6aaf5096c07c6e15434558`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[3].body[1].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[3].body[2]::Return

Source: `infra/agentinfra/roadmap_cli.py:105`; AST `a1bebba3a80060a45d397c906e7df89fcdf533341f0172ccc6c193d55b66e441`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, owner, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).qualify.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[3].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_cli.py:105`; AST `6a19f5587161b47d8f25bfda6adc44c3edd41af0c4c7f0b79bb69a62032cad73`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, owner, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).qualify.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[3].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap_cli.py:105`; AST `9af565e67ae5d334b545886bccb7b0f27fb8d8189b6644c9267610cbdb6cc4e6`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[3].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[4]::If

Source: `infra/agentinfra/roadmap_cli.py:106`; AST `a0f2d0f8a972d399a4ed0a020dd8e57b55b03245db4a2a5318c5cad70bb75875`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, bind_goal, read_json. Outputs/bindings: (none).
Calls/effect boundaries: bind_goal, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[3].body[4]; no call, error or mutation may be omitted. Condition: a.action == 'bind'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[4].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:106`; AST `97e57d272863bb2e70ba47896e3152a1ef697d2648e16871b265d0d2d52f6c5c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, bind_goal, read_json. Outputs/bindings: (none).
Calls/effect boundaries: bind_goal, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[3].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:106`; AST `f4496966fef2a26f75eadb6db9e3fb562aa0f5f7a5b19a688d7ac03c290e2342`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, bind_goal, read_json. Outputs/bindings: (none).
Calls/effect boundaries: bind_goal, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[4].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:106`; AST `96ff96906ae694bd0c37891263e3e06cea1f5a647193c11940e89243cf99bfc2`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[4].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[5]::If

Source: `infra/agentinfra/roadmap_cli.py:107`; AST `32793b48f97769c0fe6dbe0efb4b090a4754fc94f5c343766ff154e84346abe7`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, bind_plan, compile_roadmaps, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: a.milestones.split, bind_plan, compile_roadmaps, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[3].body[5]; no call, error or mutation may be omitted. Condition: a.action == 'plan'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[5].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:107`; AST `dc46bb7d3d209c75955a80b4332a8de0c31fe4ba8e9c81c27ce2ca67425e60ab`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, bind_plan, compile_roadmaps, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: a.milestones.split, bind_plan, compile_roadmaps, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[3].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:107`; AST `a57c596e4d2c19ccb2f748d97e29d5fc2fd6d4ba6e1311f373eab4478b879ebc`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, bind_plan, compile_roadmaps, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: a.milestones.split, bind_plan, compile_roadmaps, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[5].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:107`; AST `0d81a1b62ae0add0f6856dc19465a7b87f3c6a7d9ff56c4e7d642f1c6da29243`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[5].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[5].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:107`; AST `4d90abaf98d724d834adb4b31b8504efacb6c4a754f49c596a336d7563531146`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.milestones.split.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[5].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[5].body[0].value.args[2]::Call

Source: `infra/agentinfra/roadmap_cli.py:107`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[5].body[0].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[6]::If

Source: `infra/agentinfra/roadmap_cli.py:108`; AST `90160c06518acc42535875d5cd2f7573278302c8efbac8c098070acebfa0df65`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, read_json, reconcile_native_transition. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_native_transition.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[3].body[6]; no call, error or mutation may be omitted. Condition: a.action == 'reconcile'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[6].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:108`; AST `f72e2c235e7348aaed52b08e40a4cd163e4164c49bb529ad9dcf6fc53a521b95`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json, reconcile_native_transition. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_native_transition.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[3].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:108`; AST `c2b6fe545a446946d3ffbd98837378b7604e0f704061a8c8ce5c1d908f4cb4c7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json, reconcile_native_transition. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_native_transition.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[6].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:108`; AST `d874b0d9b3dbd861625df2b1bb5a2e99a0009921c29becf70f0f01f0de9f0577`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[6].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[6].body[0].value.args[1].body::Call

Source: `infra/agentinfra/roadmap_cli.py:108`; AST `3e14c09ef2e407a6410ec771283038e4498e496be544977090334a81c2de3ded`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[6].body[0].value.args[1].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[6].body[0].value.args[2].body::Call

Source: `infra/agentinfra/roadmap_cli.py:108`; AST `00d1a848d2b6dee479d3c6b65533732b9a9746678bd6305830d89330547d0840`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[6].body[0].value.args[2].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[7]::Assign

Source: `infra/agentinfra/roadmap_cli.py:109`; AST `91064dc9252a793622ee877ff1c84343be4fc10513fdbfb826a42a615be6e70b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json. Outputs/bindings: request.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[7].value::Call

Source: `infra/agentinfra/roadmap_cli.py:109`; AST `9882c1cd687efea83eceee7d9a34d69d4146c2b837396aa92795925e6e60483d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[8]::Return

Source: `infra/agentinfra/roadmap_cli.py:110`; AST `3610df6d8d1c3188b34aaf364426076c9c103212cdbbb7e081d2201a67c8e4ee`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, goal_transition, read_json, request. Outputs/bindings: (none).
Calls/effect boundaries: goal_transition, read_json, request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[8].value.values[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:110`; AST `a4d8a0ef453edb21087b037d6e1a77ea94d01151413413ffe2a9e060f7a4c905`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, goal_transition, read_json, request. Outputs/bindings: (none).
Calls/effect boundaries: goal_transition, read_json, request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[8].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[8].value.values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:110`; AST `98164bcaa7d7b39fd20b1bb79671d32916f53482044b9b953171e13f595b20ff`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[8].value.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[8].value.values[1].keywords[0].value.left::Call

Source: `infra/agentinfra/roadmap_cli.py:111`; AST `15b957912b41f944cf4bcfc03f8108964f688a04e33abcf6cf24bfd042e00895`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: request. Outputs/bindings: (none).
Calls/effect boundaries: request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[8].value.values[1].keywords[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[3].body[8].value.values[1].keywords[1].value.left::Call

Source: `infra/agentinfra/roadmap_cli.py:111`; AST `47e928e15f5fd9d6187d759a78a0dbdbb8121a5178efe9fbcbb0c49d0c32236a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: request. Outputs/bindings: (none).
Calls/effect boundaries: request.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].body[8].value.values[1].keywords[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4]::If

Source: `infra/agentinfra/roadmap_cli.py:112`; AST `39f8c65447df81a6405aab3ad8bb3a75753deda49d36f2851185f57a23cec3ee`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, errors, obligation, proof_errors, proof_result, python_proof_errors, read_json, reconcile_original_tests, root, validate_record. Outputs/bindings: errors, obligation, proof_result.
Calls/effect boundaries: proof_errors, python_proof_errors, read_json, reconcile_original_tests, validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[4]; no call, error or mutation may be omitted. Condition: a.family == 'verification'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[0]::If

Source: `infra/agentinfra/roadmap_cli.py:113`; AST `68fd8a34344a4930d525901ac814597b201ff8ae466bdb0bd544e872fc373cc9`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, read_json, reconcile_original_tests. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_original_tests.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[4].body[0]; no call, error or mutation may be omitted. Condition: a.action == 'reconcile-tests'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:113`; AST `fcc95b0ddbc96646105bc8a283aa9ba66c6ae304867d7aaa4e71569e97b4a1db`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json, reconcile_original_tests. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_original_tests.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:113`; AST `1f973ce14adbf16c75002a9fc1f67056c23deb3ce107be9df6c3616b8dfb948f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json, reconcile_original_tests. Outputs/bindings: (none).
Calls/effect boundaries: read_json, reconcile_original_tests.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[0].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:113`; AST `f0ce24a1a2ed4f7895a254a16fe0d6a8f62209fbf23ca6caa0bc90c530ae0849`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[0].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:113`; AST `eeefe24bc579000a9d07c7951a1aab24ae3afa0c140261d436febc40396a8b8f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[0].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:114`; AST `2b866acaba7b4bada6bd020106258480da7af06d477b96f444f901d9968b9d96`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json. Outputs/bindings: obligation.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:114`; AST `218c8fe81c0885a1ba433250fd166d649e82f376d91360fef4d21f55dedd4b1a`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[2]::Expr

Source: `infra/agentinfra/roadmap_cli.py:114`; AST `2e179482e3a69ad877f8ac58b2c3ebca3a6f9b190e07a75f3b9dc8778a4015ac`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[2].value::Call

Source: `infra/agentinfra/roadmap_cli.py:114`; AST `9a42878ffb0512bc22fcb3d19d90820d1600e599b18525cff9deb2c80d8c4034`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:115`; AST `40199cc11d0fa227ccd8f555dc15746ff5b1ed7b006f59ed7374a185cc092732`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[21].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[4]::Assign

Source: `infra/agentinfra/roadmap_cli.py:116`; AST `7e6f879f2f5196e08fe3b4fc4c268b7923d61b58714fbeff10c4f60e7bc40bca`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json. Outputs/bindings: proof_result.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[4].value::Call

Source: `infra/agentinfra/roadmap_cli.py:116`; AST `acba4d9b63c226ba10fba6d5989b51dd7451295c68d8547fff53be8f58968fb1`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[5]::Assign

Source: `infra/agentinfra/roadmap_cli.py:117`; AST `8ee7d7406720e1267e37177d3f4e3d9181ae85708eb2b17372e161f857d5236d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation, proof_errors, proof_result, python_proof_errors, root. Outputs/bindings: errors.
Calls/effect boundaries: proof_errors, python_proof_errors.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[5].value.left::Call

Source: `infra/agentinfra/roadmap_cli.py:117`; AST `244b460f85de51418d6ae2ab3f1b40b7b73f319d22142c8d4115d1cdfa742429`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation, proof_errors, proof_result. Outputs/bindings: (none).
Calls/effect boundaries: proof_errors.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[5].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[5].value.right::Call

Source: `infra/agentinfra/roadmap_cli.py:117`; AST `9fd63fef0fc01733354a17b88754025e1b93971f4b897974efcdbe0c84157250`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation, proof_result, python_proof_errors, root. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].body[5].value.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[4].body[6]::Return

Source: `infra/agentinfra/roadmap_cli.py:118`; AST `c30fad21d4bc965a0500e7e2fdbbbb9613d2d7d44477f1c0e9ae67aca9b0f372`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: errors. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5]::If

Source: `infra/agentinfra/roadmap_cli.py:119`; AST `4006fb9e68c98249847a08dd4dcc795b8007318d0b49d94a4515afb03416aca8`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: BudgetLedger, a, ledger, recover_operation, root. Outputs/bindings: ledger.
Calls/effect boundaries: BudgetLedger, ledger.metrics, ledger.observe_usage, ledger.read, ledger.reservation_record, recover_operation.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[5]; no call, error or mutation may be omitted. Condition: a.family == 'budget'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:120`; AST `dc2fd1ede60c6438c487511f87ef8eedec8bb87e6ab3d1c5380ff1542be015c2`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, root. Outputs/bindings: ledger.
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:120`; AST `df43247d3e9a1323119ce795d3f01353dada1c7e238477cf98ed400282fae762`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, root. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[1]::If

Source: `infra/agentinfra/roadmap_cli.py:121`; AST `a85ba6f8bd31e906e6c0d816b7e9496c72e2430a9ecfc86dc98ffd3aaf6554c5`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.metrics.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[5].body[1]; no call, error or mutation may be omitted. Condition: a.action == 'metrics'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:121`; AST `2cf91c2819122e4a03efc5e03833ee20ecc14200534edc0d8f910c93c946bd65`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.metrics.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:121`; AST `a198a50182fcadb1fd405fbd30f49194d1fb2f7ef3cd1516ade9b3ccc3d97606`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.metrics.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:122`; AST `a16680ec8fec3ef4051b5f0f740553c935eb443de8b922dc54c5d8bb52a8a44a`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.reservation_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[5].body[2]; no call, error or mutation may be omitted. Condition: a.action == 'reservation'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:122`; AST `46e72f9031612e3230fa0e2d21c8a469f70be23e298c5473c00278bea59e870e`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.reservation_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:122`; AST `4600f7d5733e60c2a601a778bef145b7ba279dac27718bdb1e40597ce65d8d8f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.reservation_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:123`; AST `2c19c3fcbacc7bac9abff0a59516bb8b48388d4d950cb8f2db101d5ccce73988`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, recover_operation, root. Outputs/bindings: (none).
Calls/effect boundaries: recover_operation.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[5].body[3]; no call, error or mutation may be omitted. Condition: a.action == 'recover'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[3].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_cli.py:124`; AST `79105e0b749ab57cf92b174e92d938d3032d7ae18d4a91a9c8541b2dd3cb0f2d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[21].body[5].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[3].body[1]::Return

Source: `infra/agentinfra/roadmap_cli.py:125`; AST `fb32381cf1ae007cd22a83da3839a8c4dc85e53e30948d79f170d7f0ec5e9fce`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, recover_operation, root. Outputs/bindings: (none).
Calls/effect boundaries: recover_operation.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[5].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:125`; AST `e9547ab6cacb74bf2d5e5684ae522769a583f22a646dd1c8d61086f8b52d004e`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, recover_operation, root. Outputs/bindings: (none).
Calls/effect boundaries: recover_operation.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[4]::Return

Source: `infra/agentinfra/roadmap_cli.py:126`; AST `aedfa89cf3e2fd1225a8c78d487f9292ef60455f435c5da94adb1a58c1a08785`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.observe_usage, ledger.read.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[4].value.body::Call

Source: `infra/agentinfra/roadmap_cli.py:126`; AST `97bf15ee0985708addfb91473f1c9a324eb4e700d9a5a949145f8b93d423dbb2`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.read.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[4].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[5].body[4].value.orelse::Call

Source: `infra/agentinfra/roadmap_cli.py:126`; AST `6f635f7bccf485e753e97db386821c2065629b582c2b133f22a3c69ebd0e27ae`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.observe_usage.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].body[4].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6]::If

Source: `infra/agentinfra/roadmap_cli.py:127`; AST `d86e9a1c8d1ec0ed82150d93a263d5a78aefb1864a7c281bd51149d6ccf3caa1`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, adjudicate_findings, atomic_write_text, confined_path, decision, digest, output, read_json, render_packet, review, root, str, validate_decision, validate_record. Outputs/bindings: decision, output, review.
Calls/effect boundaries: adjudicate_findings, atomic_write_text, confined_path, digest, read_json, render_packet, str, validate_decision, validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[6]; no call, error or mutation may be omitted. Condition: a.family == 'review'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[0]::If

Source: `infra/agentinfra/roadmap_cli.py:128`; AST `59b50194357d402467c8d0f51f72aa6465b150318853d0829791c2e312260e94`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, adjudicate_findings, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: adjudicate_findings, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[6].body[0]; no call, error or mutation may be omitted. Condition: a.action == 'findings'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:128`; AST `8030a303f2383dcd27c7e41e42d77419775bb87a0450a48e2276e718202af7ec`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, adjudicate_findings, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: adjudicate_findings, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[0].body[0].value.values[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:128`; AST `fef85d040a556c5d551f2c3ce9d0c582785bb29ab412b211d4ef1138730cafe1`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, adjudicate_findings, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: adjudicate_findings, read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[0].body[0].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[0].body[0].value.values[0].args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:128`; AST `ba2e037c249060aa994cb7cdd399af6ca6412389ec535254e4d71c8e3ec8b159`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[0].body[0].value.values[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:129`; AST `2064d27d432cc4f1e728bb7c802ed2d030151c13e7a45af19d16ebaf8f9f21e7`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json. Outputs/bindings: review.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:129`; AST `1ce8bc32ec262e834458b495b0c1db54cccd88aa659286e524f2af778941ba4f`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:130`; AST `23076d1b52a0112f303cbb78a05c805a7e8ca40df8ed2bafd58a17e0946fd786`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, atomic_write_text, confined_path, digest, output, render_packet, review, root, str. Outputs/bindings: output.
Calls/effect boundaries: atomic_write_text, confined_path, digest, render_packet, str.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[6].body[2]; no call, error or mutation may be omitted. Condition: a.action == 'render'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:131`; AST `9bc857a9c259ffb8498c8ad6aec0eb37b6a5c65d1337f5af179d4c3a6ead4a81`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, confined_path, root. Outputs/bindings: output.
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:131`; AST `8772d9314c0b7dd22d22e6244a777898fc2b45883955c41d834a353f76d6647d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_cli.py:132`; AST `a1b81b41da846f5a98e45da83d505909f72b5c37c9a3983b607b9496a87da9dd`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_text, output, render_packet, review, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_text, render_packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:132`; AST `b4d27b01aed560cdc9e1a56b1c34f27455f8aa67ca08be44afac04f6a07004b7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_text, output, render_packet, review, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_text, render_packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[2].body[1].value.args[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:132`; AST `b7dc504ba7e9fb0b2705ec2c3dbaf8fd8adfc7cb27ea4f695fdb22c69cf39bf7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: render_packet, review, root. Outputs/bindings: (none).
Calls/effect boundaries: render_packet.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[2].body[1].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[2].body[2]::Return

Source: `infra/agentinfra/roadmap_cli.py:133`; AST `2a58ec5c2ada76640d8e0a0a11954672602fb55afdf2df2a6d6ed157c3fe61ad`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, output, review, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, str.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[6].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[2].body[2].value.values[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:133`; AST `ac21b5e6705c69eec368406129c3927fb69226e1c7181f1f7830ab68cf750b41`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[2].body[2].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[2].body[2].value.values[1]::Call

Source: `infra/agentinfra/roadmap_cli.py:133`; AST `d36ee616fab72f11a9b8fa05d8b03628acdcfc6aa2d8e2513c316f915994eead`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, review. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[2].body[2].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[3]::Assign

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `7ff3842184ad38d386d3fbda72d4b63b5dfe203d3173d1c290ff8e9ddcde0b0b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, read_json. Outputs/bindings: decision.
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[3].value::Call

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `76628dd778b220d48ec2a53893457a3b78cd25f15167d52b9065ca1cafc6dbde`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[4]::Expr

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `9eff61797fbda476656325e1f568cf0c33d242e0294b5c1c8d340776f52f3edf`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: decision, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[4].value::Call

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `c7a602387eada360323a4fb3d1ca7d887a837880376ede3782c142d79c2301d7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[5]::Expr

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `2ef727bf50ad878a6cef5f34097c625aabfb5dca20eda630d436c298577204cb`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: decision, review, validate_decision. Outputs/bindings: (none).
Calls/effect boundaries: validate_decision.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[5].value::Call

Source: `infra/agentinfra/roadmap_cli.py:134`; AST `cfe68890edc351089e87f7bbe56be4d679ba4d6c38c06491b981791a1ad540d7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision, review, validate_decision. Outputs/bindings: (none).
Calls/effect boundaries: validate_decision.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[6].body[6]::Return

Source: `infra/agentinfra/roadmap_cli.py:135`; AST `fb44afbf6d110f4331989b733995932640bc207ef77c8376a16401ee04c9885d`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[7]::If

Source: `infra/agentinfra/roadmap_cli.py:136`; AST `25b790c0f2fbfe2cff60d496bed55873a0e4933be1e521a55040950f666ec9fa`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, root, validate_skills. Outputs/bindings: (none).
Calls/effect boundaries: validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[7]; no call, error or mutation may be omitted. Condition: a.family == 'skills'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[7].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:136`; AST `7fd1f5c078c677852c1a9e96ee1ad8cba91999b6edf00abb4f044dfdb23b5626`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, validate_skills. Outputs/bindings: (none).
Calls/effect boundaries: validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:136`; AST `058a684a59952bf7321b2dca779c67fea9fccce702659f76c7c2ae7f32107527`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, validate_skills. Outputs/bindings: (none).
Calls/effect boundaries: validate_skills.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[8]::If

Source: `infra/agentinfra/roadmap_cli.py:137`; AST `f86ba5f494caf44eddbb9de1d30122bf16c314f7b634a117e946b54c002eaf7c`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, compare_interfaces, observe_interfaces, root. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, observe_interfaces.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[8]; no call, error or mutation may be omitted. Condition: a.family == 'interfaces'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[8].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:138`; AST `daed15f00ae103b4fc73fcd8e4f016e926af736fb7c4509a17e60dd4f5c89cef`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, compare_interfaces, observe_interfaces, root. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, observe_interfaces.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[8].body[0].value.body::Call

Source: `infra/agentinfra/roadmap_cli.py:138`; AST `e3b835733344cc4702b993e1dfafa68c05951883e31c5b65824bdf1022d38cb1`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_interfaces, root. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[8].body[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[8].body[0].value.orelse::Call

Source: `infra/agentinfra/roadmap_cli.py:138`; AST `4095ec58ddcd88bcdd25f1d73c342e4b21d49422d5f713395bd022cac80f2e5d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, compare_interfaces, root. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[8].body[0].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[9]::If

Source: `infra/agentinfra/roadmap_cli.py:139`; AST `38a7a387bb052cf16ed74202b8859039f0cbdab72698c229bbad3f1933069b3c`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, retrieve, root. Outputs/bindings: (none).
Calls/effect boundaries: retrieve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[9]; no call, error or mutation may be omitted. Condition: a.family == 'knowledge'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[9].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:139`; AST `068483da203a4f6e539d8e5f83b4805e16509d2a447571683ccfceef37f22b6b`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, retrieve, root. Outputs/bindings: (none).
Calls/effect boundaries: retrieve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:139`; AST `f61c38307560937a0d84d223d433e8b69e32e24d21b8d5efdf1b3a44b3a051d7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, retrieve, root. Outputs/bindings: (none).
Calls/effect boundaries: retrieve.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[10]::If

Source: `infra/agentinfra/roadmap_cli.py:140`; AST `93920b4b47e02417159a33da74438cde4b3b39773e0021918422e60c9ad20603`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, check, inventory, publish, record, root. Outputs/bindings: record.
Calls/effect boundaries: check, inventory, publish.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[21].body[10]; no call, error or mutation may be omitted. Condition: a.family == 'portability'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:141`; AST `015514a635c8911569abe27c13b24b38a29e13bb5116d66c13bbd87de1f4b7e2`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, root. Outputs/bindings: record.
Calls/effect boundaries: inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:141`; AST `865ab48cd6a5f9f39dbe8c1a00c6302e98015cad7159c31875dcf06bf0c972b7`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, root. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[10].body[1]::Return

Source: `infra/agentinfra/roadmap_cli.py:142`; AST `5e000400d4fe3d3e9658547d062d302e080d922b476c255dbf47c7bdc4f72353`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, check, publish, record, root. Outputs/bindings: (none).
Calls/effect boundaries: check, publish.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[10].body[1].value.body::Call

Source: `infra/agentinfra/roadmap_cli.py:142`; AST `fb571239a3f2ae515097646dc54c2325136515606b0d75337a66a5f3c200fe98`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, record, root. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[10].body[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[10].body[1].value.orelse::Call

Source: `infra/agentinfra/roadmap_cli.py:142`; AST `1f3f2facd3e136d60afefa95fd8cfdecefa0487485ed04cc0c9d289e1127ea29`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, record, root. Outputs/bindings: (none).
Calls/effect boundaries: check.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[10].body[1].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[11]::Raise

Source: `infra/agentinfra/roadmap_cli.py:143`; AST `debed461b974cbf336edaea02428ffc216957df0d7a917536d6e2de5587e1315`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::execute::root.body[21].body[11].exc::Call

Source: `infra/agentinfra/roadmap_cli.py:143`; AST `333142f0e1fa20905c27448d9162355696f52b65354b52edfbd65aa2378e21f1`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[11].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22]::FunctionDef

Source: `infra/agentinfra/roadmap_cli.py:146`; AST `788d147c825afd76cbfaf6683109940b5b7acc546b3ec217b6a97644ea7e4acd`.

Rust module: `infra::agentinfra::roadmap_cli`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, KeyError, OSError, TimeoutError, TransactionError, TypeError, any, args, argv, exc, execute, field, int, json, p, parser, print, result. Outputs/bindings: args, field, p, result.
Calls/effect boundaries: any, execute, json.dumps, p.exit, p.parse_args, parser, print, result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[22]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:147`; AST `9dc8c44f59c3161d0cc156f6aecd07f170ee9f31037805aa1f48124aef10b25a`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: p.
Calls/effect boundaries: parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:147`; AST `df5895e3f1cab8e578b78958e7e659d10948f3aac705dca2c579407a606b00f5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[1]::Assign

Source: `infra/agentinfra/roadmap_cli.py:147`; AST `3800b3ee5d4ab1b24a9a4cc9deecd976f4e7ffc367ecb2fe78fd2badbbff7645`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, p. Outputs/bindings: args.
Calls/effect boundaries: p.parse_args.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:147`; AST `9936886f5866377ccb6f8939c42f52f219208c2e43a6ba529ece17a973a13833`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, p. Outputs/bindings: (none).
Calls/effect boundaries: p.parse_args.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2]::Try

Source: `infra/agentinfra/roadmap_cli.py:148`; AST `217a39baba4d037b534f47e81346384c7fcdcf5fce7dd9c65177a4e1aeef5e56`.

Rust module: `infra::agentinfra::roadmap_cli`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ContractError, KeyError, OSError, TimeoutError, TransactionError, TypeError, any, args, exc, execute, field, json, p, print, result. Outputs/bindings: field, result.
Calls/effect boundaries: any, execute, json.dumps, p.exit, print, result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Try evaluation at root.body[22].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_cli.py:149`; AST `a6c8557b1594077d4c64d47935b11cd262272a3adaf7bc565e76c7ae84138991`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, execute. Outputs/bindings: result.
Calls/effect boundaries: execute.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:149`; AST `5f653271dab8375b133a694587bc52c1b28bb67d9f643515cb52cb696d923ca5`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, execute. Outputs/bindings: (none).
Calls/effect boundaries: execute.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_cli.py:150`; AST `1f1d4d7bd101d7f32b676d6e3e16cddb87fa100cab5023be61a29ac0cbfa582c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, print, result. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, print.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_cli.py:150`; AST `1076a09dd0da2d2c92ba1f149118ae6010f84f733b08b2def2729c50cb9ed40d`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, print, result. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, print.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_cli.py:150`; AST `482b5db37e2273e04f7ab894193fdb1f74861d89d051bd1a93d17dfecf567250`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, result. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[2]::If

Source: `infra/agentinfra/roadmap_cli.py:151`; AST `fb28d1d9fcb889cfee33592bc4a09ad0cf3b797209cd5d02970e48217c8b9763`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, field, result. Outputs/bindings: field.
Calls/effect boundaries: any, result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[22].body[2].body[2]; no call, error or mutation may be omitted. Condition: any((result.get(field) is False for field in ('allowed', 'accepted', 'complete', 'confirmed')))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[2].test::Call

Source: `infra/agentinfra/roadmap_cli.py:151`; AST `e051239d848cf33f499947b07608fce94dc603b4c39f21081d0468be4d308607`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, field, result. Outputs/bindings: field.
Calls/effect boundaries: any, result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].body[2].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[2].test.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_cli.py:151`; AST `58e5b651eeb8b83f249f4a96954e3ce3ca4d1d5222525a56f97652ee21192b7d`.

Rust module: `infra::agentinfra::roadmap_cli`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: field, result. Outputs/bindings: field.
Calls/effect boundaries: result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[22].body[2].body[2].test.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[2].test.args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_cli.py:151`; AST `9d473b3f36dfac6c9aaf2b6fabe3b438dcd768708fb7d8484e19c3445f685829`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].body[2].test.args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:151`; AST `4d9e3bd49f1ca0e5c82918a80328eaa190b6c6419b7b4aa57c05de813ded1b78`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[22].body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[3]::If

Source: `infra/agentinfra/roadmap_cli.py:152`; AST `0e59426f4cd82f97b12a07fc02dd90621c0ade9e8ca922883b344b1253eb189a`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[22].body[2].body[3]; no call, error or mutation may be omitted. Condition: result.get('structural_compatible') is False
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[3].test.left::Call

Source: `infra/agentinfra/roadmap_cli.py:152`; AST `2955460cff0a61da6b294595b812c34fa96d7ea1a5ffb5491557500f1676c55e`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].body[3].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[3].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:152`; AST `4d9e3bd49f1ca0e5c82918a80328eaa190b6c6419b7b4aa57c05de813ded1b78`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[22].body[2].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[4]::If

Source: `infra/agentinfra/roadmap_cli.py:153`; AST `c060bda3132b81a27d4f1d01c9c1a493e80e7d15f47c69c80bede2f55498187c`.

Rust module: `infra::agentinfra::roadmap_cli`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: args, result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[22].body[2].body[4]; no call, error or mutation may be omitted. Condition: args.family == 'roadmap' and args.action == 'run'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[4].body[0]::Return

Source: `infra/agentinfra/roadmap_cli.py:154`; AST `8dafa2403497ce3d782c0f2c34a3f25d163ce6f342082909b5bc39b1e5b7fa79`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[22].body[2].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].body[5]::Return

Source: `infra/agentinfra/roadmap_cli.py:155`; AST `b2bbc444950f9b0b0b967dc529eb889a7cf0d4003be033124fc090f4e1571b48`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[22].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_cli.py:156`; AST `c89313afaa1ceaee716b507ee78865a4bf3f0d6404b3f9e8656be968c2121978`.

Rust module: `infra::agentinfra::roadmap_cli`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ContractError, KeyError, OSError, TimeoutError, TransactionError, TypeError, exc, p. Outputs/bindings: (none).
Calls/effect boundaries: p.exit.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[22].body[2].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_cli.py:157`; AST `5f7322c48418c569c165551f656c775fae092884420f03f0593047d7b35f2e3c`.

Rust module: `infra::agentinfra::roadmap_cli`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, p. Outputs/bindings: (none).
Calls/effect boundaries: p.exit.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[2].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_cli.py::module::main::root.body[22].body[2].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_cli.py:157`; AST `082fec13c8186df8eeb6e9e284d04cda702d72d8c713be8d84307cbfe23799a0`.

Rust module: `infra::agentinfra::roadmap_cli`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, p. Outputs/bindings: (none).
Calls/effect boundaries: p.exit.
Dependencies: __future__, argparse, atomic, json, pathlib, roadmap, roadmap_acceptance, roadmap_codex, roadmap_interfaces, roadmap_inventory, roadmap_knowledge, roadmap_lease, roadmap_policy, roadmap_portability, roadmap_project, roadmap_python, roadmap_records, roadmap_review, roadmap_runtime, roadmap_verification, roadmap_work, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
