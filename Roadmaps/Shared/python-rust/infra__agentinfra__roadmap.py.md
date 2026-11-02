# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 466. Inventory digest: `55908d6e1c52a6979bf39203440a767ddeaa9d20a28eaa708cd5998cc6dc1dd4`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap.py::module::root::Module

Source: `infra/agentinfra/roadmap.py:1`; AST `d7a33f748ad66ad4c9def593f91b1d7689669ec44e0dada72ef7c607844313db`.

Rust module: `infra::agentinfra::roadmap`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: FENCE, FIXED_RECIPES, FileTransaction, GATES, Mutation, Path, ProjectAdapter, accepted, active, actual, amendments, artifact, atomic_write_json, audit, bindings_current, blocks, bool, by_milestone, c, candidates, canonical, capability, compiled, confined_path, consume, contract, count, covered, covered_lines, d, dependencies, dependency, dict, digest, end, evidence, expected_digest, good, ident, ids, input_bindings, int, isinstance, item, len, lines, list, loads, m, mandatory_sources, max_bytes, milestone, milestones, minimum, missing, n, name, obligation, obligations, order, p, path, paths, policy, prefix, priority, profile, project, project_docs, proof, proof_errors, proofs, providers, python_proof_errors, r, range, raw, re, read_json, receipt, receipts, recipe, recipes, record, registry, registry_path, rejected, relative, require, required, requirement, requirement_ids, requirements, result, result_proof, root, s, seen, set, shared, sorted, source, source_names, sources, start, state, str, type, updated, validate_record, visit, work. Outputs/bindings: FENCE, FIXED_RECIPES, GATES, accepted, active, actual, amendments, artifact, blocks, by_milestone, c, candidates, capability, consume, contract, count, covered, covered_lines, d, dependencies, dependency, end, good, ident, ids, input_bindings, item, lines, m, mandatory_sources, milestone, milestones, minimum, missing, n, name, obligation, obligations, order, p, path, paths, policy, prefix, priority, profile, project, project_docs, proof, proofs, providers, r, raw, receipt, receipts, recipe, recipes, record, registry, registry_path, rejected, required, requirement, requirement_ids, requirements, result, result_proof, root, s, seen, shared, source, source_names, sources, start, state, updated, work.
Calls/effect boundaries: '\n'.join, '\n'.join(lines[start - 1:end]).encode, (root / 'Roadmaps' / project).glob, (root / 'bin').glob, (root / 'infra').rglob, (root / 'scripts').glob, (root / 'verification/roadmap').glob, (root / source).read_text, (root / source).read_text().splitlines, (shared / 'ci').glob, (shared / 'codex-protocol').glob, (shared / 'skills').rglob, FENCE.findall, FileTransaction, FileTransaction(root, [Mutation(path, canonical(updated) + b'\n', expected_sha256=expected_digest)], state_dir=root / '.aegis/state/transactions', name='roadmap-projection').commit, Mutation, ProjectAdapter, ProjectAdapter(root, profiles=registry['projects']).update, accepted.append, active.add, active.remove, atomic_write_json, bindings_current, bool, by_milestone.get, by_milestone.setdefault, by_milestone.setdefault(receipt['milestone'], []).append, candidates.add, canonical, confined_path, confined_path(root, artifact, must_exist=True).is_file, covered_lines.update, dict, digest, evidence.get, input_bindings.append, isinstance, len, list, loads, milestones.items, milestones.values, missing.append, obligations.extend, order.append, p.get, p.get('obligation', {}).get, path.read_bytes, path.read_text, path.read_text().splitlines, path.relative_to, path.relative_to(root).as_posix, policy.get, proof.get, proof_errors, providers.get, python_proof_errors, r.get, range, raw.decode, re.compile, read_json, receipt.get, receipt['configuration'].get, recipe.get, recipes.items, registry.get, registry['projects'].items, registry_path.exists, rejected.append, require, root.resolve, seen.add, set, set().union, shared.glob, sorted, type, validate_record, visit.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap.py:1`; AST `269964280ab6f09d102d901e29e0328f9a4cdd258db94b6c4d154ddba76c2692`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap.py:4`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap.py:5`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap.py:7`; AST `1b8b71be5203ae66cf696ad7ae023750f023f11fd20fe2501f8e1d56817881e3`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap.py:8`; AST `9562fa000286b86337306c86577a67ec8369e7f3cb024aa784e673f54af52051`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap.py:10`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap.py:11`; AST `c2a64003604dd1da38b622b02ca5190bea13e78ec6647b9f914f7257516a593e`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap.py:12`; AST `d23622f4f7b8a2a2a2c427bc6818b0ff3b6aa22c3e487fbfab082351aa7c52cb`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[9]::Assign

Source: `infra/agentinfra/roadmap.py:15`; AST `8c8e7048ff50b1fd7b33cfcd5bfdbf1444aa32813f4df582f13ca3b56a413a6f`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: re. Outputs/bindings: FENCE.
Calls/effect boundaries: re.compile.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[9].value::Call

Source: `infra/agentinfra/roadmap.py:15`; AST `6970ee8eff5b8fddd52689f6ee31140225b2732d7995666db76079dbdb557dbc`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re. Outputs/bindings: (none).
Calls/effect boundaries: re.compile.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[10]::Assign

Source: `infra/agentinfra/roadmap.py:16`; AST `544d4ef624212cfa824b5a684cda49024bd3c20c6ef3d7de58cf17b112a90653`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: FIXED_RECIPES.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::root.body[11]::Assign

Source: `infra/agentinfra/roadmap.py:21`; AST `2aa8d89eb41de7e186bef9ef5f0bdb2f4fd394a0260176170f19f3b6f4881a47`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: GATES.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap.py:25`; AST `786149283b3213bbe825080d641eaa5c4e9082492655734a9e33e983a6324432`.

Rust module: `infra::agentinfra::roadmap`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FENCE, FIXED_RECIPES, GATES, Path, active, amendments, artifact, bindings_current, blocks, c, capability, confined_path, consume, count, covered, covered_lines, dependency, dict, digest, end, ident, input_bindings, int, item, len, lines, list, loads, m, mandatory_sources, milestone, milestones, n, name, obligations, order, p, path, paths, policy, prefix, priority, profile, project, project_docs, providers, r, range, raw, read_json, recipe, recipes, registry, require, requirement, requirement_ids, requirements, result, root, s, seen, set, shared, sorted, source, source_names, sources, start, str, type, validate_record, visit. Outputs/bindings: active, amendments, artifact, blocks, c, capability, consume, count, covered, covered_lines, dependency, end, ident, input_bindings, item, lines, m, mandatory_sources, milestone, milestones, n, name, obligations, order, p, path, paths, policy, prefix, priority, profile, project, project_docs, providers, r, raw, recipe, recipes, registry, requirement, requirement_ids, requirements, result, root, s, seen, shared, source, source_names, sources, start.
Calls/effect boundaries: '\n'.join, '\n'.join(lines[start - 1:end]).encode, (root / 'Roadmaps' / project).glob, (root / 'bin').glob, (root / 'infra').rglob, (root / 'scripts').glob, (root / 'verification/roadmap').glob, (root / source).read_text, (root / source).read_text().splitlines, (shared / 'ci').glob, (shared / 'codex-protocol').glob, (shared / 'skills').rglob, FENCE.findall, active.add, active.remove, bindings_current, confined_path, confined_path(root, artifact, must_exist=True).is_file, covered_lines.update, dict, digest, input_bindings.append, len, list, loads, milestones.items, milestones.values, obligations.extend, order.append, path.read_bytes, path.read_text, path.read_text().splitlines, path.relative_to, path.relative_to(root).as_posix, policy.get, providers.get, range, raw.decode, read_json, recipe.get, recipes.items, registry.get, registry['projects'].items, require, root.resolve, seen.add, set, set().union, shared.glob, sorted, type, validate_record, visit.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:26`; AST `7b881662a93f1cabda6daa8de666cd56431dd47a61da7e3a5a8856defd752ca2`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: root.
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:26`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[1]::Assign

Source: `infra/agentinfra/roadmap.py:27`; AST `3380eb1c18d4dd87a0367b29694513b14611664db9c44eab6e802c537b35b080`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: shared.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[2]::Assign

Source: `infra/agentinfra/roadmap.py:28`; AST `2dfa6c735934742ff2cc048a7fc0eac3791e884af21b79c4f78867c650ed4afa`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, shared. Outputs/bindings: registry.
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:28`; AST `ee21aa9e1a9319ef2a84ce3efec7ff77645072ef7ccc0fb83aafa7577a678d3e`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, shared. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[3]::Expr

Source: `infra/agentinfra/roadmap.py:29`; AST `9b947411f4abacd82cfa100285219d3cf2f19548abde762730af9b98eb957b69`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: registry, require. Outputs/bindings: (none).
Calls/effect boundaries: registry.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[3].value::Call

Source: `infra/agentinfra/roadmap.py:29`; AST `e5da7b9611fd0b9b67cffe5010806fce2b6ada7b5880b754c8b311814ad68d17`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: registry, require. Outputs/bindings: (none).
Calls/effect boundaries: registry.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:29`; AST `8aac5315d57ac475fc02b112cc7102feed1b3543c6d004ab21bf4706209d6757`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: registry. Outputs/bindings: (none).
Calls/effect boundaries: registry.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[4]::Assign

Source: `infra/agentinfra/roadmap.py:30`; AST `c33173ef617d49e4106ba8ce651a513269ad2176fa6593feea6fb4a72de55476`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, shared. Outputs/bindings: policy.
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[4].value::Call

Source: `infra/agentinfra/roadmap.py:30`; AST `65277344ddc64eec8065cabdb30455e86847a9e51cdf49a10177a2cc6b733b8d`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, shared. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[5]::Expr

Source: `infra/agentinfra/roadmap.py:31`; AST `5095b008f724a25d62529fe8fde6946d4419f679c75f037652fb0ac0d4b23958`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[5].value::Call

Source: `infra/agentinfra/roadmap.py:31`; AST `b444ec638bacb06f760630d63a5ccf00760ffe96960868fbb8a103081342f7c5`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[5].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap.py:31`; AST `4f4917a694d078dcde9a0b2b3f36334ce31176634b9e12cecc4a86db64cf7e07`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[5].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap.py:31`; AST `f2dfec733c077a3aebd3b374c6918761ce73c3c86dcbf007d8a3e03cb44c6c18`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[6]::Expr

Source: `infra/agentinfra/roadmap.py:32`; AST `2b191bd5a7ed35bfe22f8be67a81647a284e5b0b4460b54b57044ed9c3bd2804`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[6].value::Call

Source: `infra/agentinfra/roadmap.py:32`; AST `90b3b57bd72b0eafdeda7ea9c644192f73c200c41e4989f38c006dffebd0be9c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap.py:32`; AST `8657be06e800b10e2b63778ab8bb176ea3ab7d71552863ea4e4ef3cb542938be`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[6].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap.py:32`; AST `53c5d80942e4427173d108d561a17542bf31e7d981da925709f8b407d4b5e6f5`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[7]::Expr

Source: `infra/agentinfra/roadmap.py:33`; AST `531e0e05c22c8b160e7f7a674a891e5a614dc29eaa2c1d8b5c5d5aecf34e78b0`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[7].value::Call

Source: `infra/agentinfra/roadmap.py:33`; AST `e7007dfea40310065aa7e9a2609924c2a7f71467c925f6204d457bbd8af5f9d5`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[7].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap.py:33`; AST `5fe23f797c59bc6c1e988c36dc363af055f22226e45235e2ebf5fcca202d83c7`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[7].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap.py:33`; AST `d5af83578c3f54ff3623af1c1222cc7fc96e3f6332c9a16dd3d2d3ef19688187`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[8]::Expr

Source: `infra/agentinfra/roadmap.py:35`; AST `7ababb003d6fe94ae818052a2eb9d86da7bea062b6607d72d2b3202c98c6ab09`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[8].value::Call

Source: `infra/agentinfra/roadmap.py:35`; AST `157b9e702e2a506826f1deac74869630ed8e319f9d54651343d73802091bcdb0`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[8].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap.py:35`; AST `6878a60a099661cd9a40f0f29e4d72c95481dbedcd6c287eca4a5242d1303bd0`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[8].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap.py:35`; AST `246838c922a28e5f7a7237dea3f6a47ed0c44cb769469ec7e80cce183ee8aa93`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[9]::Assign

Source: `infra/agentinfra/roadmap.py:37`; AST `f84adbf6d54b290594cf60e6b8337c27ef96bc1ebfbb1c4b64550d43232987e4`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, shared. Outputs/bindings: sources.
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[9].value::Call

Source: `infra/agentinfra/roadmap.py:37`; AST `772ac60886c90a6903148b2792610b7d41f076cc55cfcd1ad4333892ae603faf`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, shared. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[10]::Assign

Source: `infra/agentinfra/roadmap.py:38`; AST `4fd9d214df2540ecbfbabc2d2207b8a7ae91360c4eaa9659f8f17e8757c85ad8`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: mandatory_sources.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[11]::Assign

Source: `infra/agentinfra/roadmap.py:39`; AST `48efe32a0b1db41c9ff381b1d910a3949dd83b5aa192bf83c5c49410ee0fab53`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: s, sources. Outputs/bindings: s, source_names.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[11].value::ListComp

Source: `infra/agentinfra/roadmap.py:39`; AST `0b6ab1672dd947c2347b92c9c8e890f57db210877c8a831dfc051f70a6408113`.

Rust module: `infra::agentinfra::roadmap`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: s, sources. Outputs/bindings: s.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[12]::Expr

Source: `infra/agentinfra/roadmap.py:40`; AST `3da83c0053a2a5af1075a3a70c8863e858772cfd27a338570e3c5ca178e4d650`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, mandatory_sources, require, set, source_names. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[12].value::Call

Source: `infra/agentinfra/roadmap.py:40`; AST `272d3b8b32789eaee5ac8e84bef903b9a768f011cf27e53a4a356256c985430c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, mandatory_sources, require, set, source_names. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[12].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap.py:40`; AST `086b6aee4030f6a39de98231cb0dd2161dd9586440ca9ebcc5bd57e8c6f7c8d6`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, source_names. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[12].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:40`; AST `25bf984a237c8f9730f94757ba53ffa4532728f98e61f81c72eadd0eaf5101c8`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, set, source_names. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[12].value.args[0].values[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap.py:40`; AST `fa475bde769853beebe599aab5707011a172e544b0497fc1fe1d06a77ab3d963`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, source_names. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value.args[0].values[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[12].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:40`; AST `fa475bde769853beebe599aab5707011a172e544b0497fc1fe1d06a77ab3d963`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, source_names. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[13]::For

Source: `infra/agentinfra/roadmap.py:41`; AST `cce5d241401d4915132ffcfe0f92e9bdfbd66ab9d5b6ea3f715aa3241d49df1c`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: bindings_current, require, root, source, sources. Outputs/bindings: source.
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[13]; no call, error or mutation may be omitted. Iteration: source in sources['files']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[13].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:42`; AST `fa15032d0af4cc3e7f535970a992ae12bd70d64efb127acd97ef4ac6841f9fa8`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, require, root, source. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[13].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:42`; AST `5940ac75301cc95cb2b4b129f549bb308be4fadc7ab59102ffa071ae348703d3`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, require, root, source. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[13].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap.py:42`; AST `2560b1f55ae492b210a0aee075032822ca6657216c85decee11d03ea96472229`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, root, source. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[14]::Assign

Source: `infra/agentinfra/roadmap.py:43`; AST `49e1f8b7273f16173c14fe61a733c97ba319d3db94ab21d8fd2fa1a8f17b146d`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, shared. Outputs/bindings: requirements.
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[14].value.value::Call

Source: `infra/agentinfra/roadmap.py:43`; AST `fda69cbeff94424f322d93d7d75c1e54e33e6b1e3da3e71fd3401536e6d653a1`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, shared. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15]::For

Source: `infra/agentinfra/roadmap.py:44`; AST `3d5c77ece875c503d8805f9d2d5d475de84b6e52af56a9000d409b2da73ba0a8`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: confined_path, digest, end, len, lines, path, require, requirement, requirements, root, start. Outputs/bindings: end, lines, path, requirement, start.
Calls/effect boundaries: '\n'.join, '\n'.join(lines[start - 1:end]).encode, confined_path, digest, len, path.read_text, path.read_text().splitlines, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[15]; no call, error or mutation may be omitted. Iteration: requirement in requirements
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:45`; AST `cfd24db5859e1dd5634a325ee029e683d542252baa549a6761013b75b3e7151f`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, requirement, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:45`; AST `22592fa5da50ec077dc0fcd36b7079bd97946f836d23a63bf9bc659269095e24`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, requirement, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[1]::Assign

Source: `infra/agentinfra/roadmap.py:46`; AST `669ef12685beac617997dfab445005708f54d39549bdbfdb0ee530b0fd54f465`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: lines.
Calls/effect boundaries: path.read_text, path.read_text().splitlines.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:46`; AST `6ff431918ffde64bb1c1428596401c8ce5e94f2e2e0a999fd96dece2105a2911`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.read_text().splitlines.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[1].value.func.value::Call

Source: `infra/agentinfra/roadmap.py:46`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[2]::Assign

Source: `infra/agentinfra/roadmap.py:47`; AST `c551d6b92518eba7917e278d8224f8b929496452e6252af40e1dab95bd45276e`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: requirement. Outputs/bindings: end, start.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[3]::Expr

Source: `infra/agentinfra/roadmap.py:48`; AST `db1ddde87700ecd753e8673df92e0d4f657dfcf7f15373e227ec6d6589eb1ac3`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: end, len, lines, require, start. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[3].value::Call

Source: `infra/agentinfra/roadmap.py:48`; AST `38a879a7d7bb9bc8f8fdc7076960f20929d16abfb91dc0a8418ef9d8996c8ff1`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: end, len, lines, require, start. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[3].value.args[0].comparators[2]::Call

Source: `infra/agentinfra/roadmap.py:48`; AST `07afbb7a385f382c1b40fcda6b6f7e9c91706969b1e8ab06f90f28b01f56b98a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, lines. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].body[3].value.args[0].comparators[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[4]::Expr

Source: `infra/agentinfra/roadmap.py:49`; AST `0f0d887bf343c3992d47978aa840aef2de255d336db225d86251e0ea1b53aff7`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, end, lines, require, requirement, start. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join, '\n'.join(lines[start - 1:end]).encode, digest, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[4].value::Call

Source: `infra/agentinfra/roadmap.py:49`; AST `6e1107e7cdcbdf2b0f8130daeb6a5369526b433228eddeb93db822aa784655fd`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, end, lines, require, requirement, start. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join, '\n'.join(lines[start - 1:end]).encode, digest, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:49`; AST `53e29919110c6ebf388bda5a770db566bfc79556c04e38cd84dd74f0d42f350f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, end, lines, start. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join, '\n'.join(lines[start - 1:end]).encode, digest.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[4].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap.py:49`; AST `a379ec42f03a72935b49f3070f5f9b74c4b152b99b18456bb24669fd8ce149d3`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: end, lines, start. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join, '\n'.join(lines[start - 1:end]).encode.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].body[4].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[15].body[4].value.args[0].left.args[0].func.value::Call

Source: `infra/agentinfra/roadmap.py:49`; AST `a1344c3e0f3cf07acf05b1e051427850cd3087c56458c518e7bd469e42dac7fd`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: end, lines, start. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].body[4].value.args[0].left.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16]::For

Source: `infra/agentinfra/roadmap.py:50`; AST `dd32b632fb173dcb4eb9f92bef73e7886c6f7e132307600cdda2e1698d8adf6b`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: covered_lines, len, r, range, require, requirements, root, set, source. Outputs/bindings: covered_lines, r, source.
Calls/effect boundaries: (root / source).read_text, (root / source).read_text().splitlines, covered_lines.update, len, range, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[16]; no call, error or mutation may be omitted. Iteration: source in ('Blue_Prompt.md', 'Destiny_Prompt.md')
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:51`; AST `5bfb0b28fe24beaa5a17fb9055dafe4f4687d89354837d7dd35634d58be34d18`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: covered_lines.
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:51`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[1]::For

Source: `infra/agentinfra/roadmap.py:52`; AST `c282df7ec55cff7ba111b3ffba806035f39ab246dace0a59819213a604240510`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: covered_lines, r, range, requirements, source. Outputs/bindings: r.
Calls/effect boundaries: covered_lines.update, range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[16].body[1]; no call, error or mutation may be omitted. Iteration: r in requirements
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[1].body[0]::If

Source: `infra/agentinfra/roadmap.py:53`; AST `362aa483941de17ab476e52cebad6ef25f0c25d6131978b029033bd2bcf38611`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: covered_lines, r, range, source. Outputs/bindings: (none).
Calls/effect boundaries: covered_lines.update, range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[12].body[16].body[1].body[0]; no call, error or mutation may be omitted. Condition: r['source'] == source
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[1].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:54`; AST `61ba8a974aea0e862e9a8e3b349a640b57a48c0225ca772518105c04df2be03b`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: covered_lines, r, range. Outputs/bindings: (none).
Calls/effect boundaries: covered_lines.update, range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[16].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:54`; AST `345839f9bc6c6392359cc45b116ff09c488cc7588b5eb5d8268b2dd09a8d149d`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: covered_lines, r, range. Outputs/bindings: (none).
Calls/effect boundaries: covered_lines.update, range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[1].body[0].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap.py:54`; AST `2f778ff988a12963a2e1589e52940122463f439f773e218943066795b044c5c1`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].body[1].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[2]::Expr

Source: `infra/agentinfra/roadmap.py:55`; AST `57cc80674287bbd3366f10478ff7e044e78334c8fafa4a3b43bcde735ad035a0`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: covered_lines, len, range, require, root, set, source. Outputs/bindings: (none).
Calls/effect boundaries: (root / source).read_text, (root / source).read_text().splitlines, len, range, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:55`; AST `df9abff2017ffbadd0e5d120dbfae855a05e1db445e2d0a0d05cbc4d42f2fc59`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: covered_lines, len, range, require, root, set, source. Outputs/bindings: (none).
Calls/effect boundaries: (root / source).read_text, (root / source).read_text().splitlines, len, range, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[2].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:55`; AST `3843b58acac99936508ded7309f9e9cf56d982335432dbb2dbb2bf46d3a9931f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, range, root, set, source. Outputs/bindings: (none).
Calls/effect boundaries: (root / source).read_text, (root / source).read_text().splitlines, len, range, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].body[2].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[2].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap.py:55`; AST `9af1d8cb30c6b20eeaa47b63d7d68620898c8f158edbef19c0f2e6b1bbd97f53`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, range, root, source. Outputs/bindings: (none).
Calls/effect boundaries: (root / source).read_text, (root / source).read_text().splitlines, len, range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].body[2].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[2].value.args[0].comparators[0].args[0].args[1].left::Call

Source: `infra/agentinfra/roadmap.py:55`; AST `5818dcef18978f48bdd3118cbb22850fc44b40c7e143d1cee73e3a1e3f289a05`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, root, source. Outputs/bindings: (none).
Calls/effect boundaries: (root / source).read_text, (root / source).read_text().splitlines, len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].body[2].value.args[0].comparators[0].args[0].args[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[2].value.args[0].comparators[0].args[0].args[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap.py:55`; AST `3c7834eed22ca776e36b0fa56e60de97a3df2611110116e1c69e1d37edd5004f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source. Outputs/bindings: (none).
Calls/effect boundaries: (root / source).read_text, (root / source).read_text().splitlines.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].body[2].value.args[0].comparators[0].args[0].args[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[16].body[2].value.args[0].comparators[0].args[0].args[1].left.args[0].func.value::Call

Source: `infra/agentinfra/roadmap.py:55`; AST `efcfdcd541ba6cfd13040ede29cf03db3e1041e8c5b1240a89b1c297ef360369`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source. Outputs/bindings: (none).
Calls/effect boundaries: (root / source).read_text.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].body[2].value.args[0].comparators[0].args[0].args[1].left.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[17]::Assign

Source: `infra/agentinfra/roadmap.py:56`; AST `969d1d9b371a4cc15fded623751a1456876a183eaf2b2df37fce0f480d5c85ce`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r, requirements. Outputs/bindings: r, requirement_ids.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[17].value::ListComp

Source: `infra/agentinfra/roadmap.py:56`; AST `f63bee1e8e783ebe5872af4d94a143817781515dcdae16eac770250c51fac21c`.

Rust module: `infra::agentinfra::roadmap`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: r, requirements. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[18]::Expr

Source: `infra/agentinfra/roadmap.py:57`; AST `d7a9c07b3b10d16d14e8a229e3c753b3d2779fd26166048d56d447d11c70f1f5`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, require, requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[18].value::Call

Source: `infra/agentinfra/roadmap.py:57`; AST `656e7435eb8d9664b546030c29b0ddcfaffd8cc2176044158fa24e754be94884`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, require, requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[18].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:57`; AST `e13050e396ff927b60ff33053c5d4cad8022de54e27febb39b1c89177af5fd79`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[18].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[18].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap.py:57`; AST `6f356e3e763cab2108605cbf4b0b1329ec91c323018ffee252107ba13c9b5905`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[18].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[18].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:57`; AST `6ef456de11f025270a3d99832a3c1536aae48e1a95212ea3703c223ebf2452aa`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, requirement_ids. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[18].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[19]::Assign

Source: `infra/agentinfra/roadmap.py:58`; AST `44a41af0833d7f9cf9d7ec545738701f938868a28466c2c466a1895a78489562`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: registry, set. Outputs/bindings: amendments.
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[19].value::Call

Source: `infra/agentinfra/roadmap.py:58`; AST `405e80806658d86e1ae979f2de04359c7cd3e0c3dd894188f461c8ddd5ebf1fc`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: registry, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[20]::Expr

Source: `infra/agentinfra/roadmap.py:59`; AST `cecb945dfccb06fbff9207eff70b9a6692c884d2ec00fd42a941d30b2ac20c30`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: amendments, policy, require, requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[20].value::Call

Source: `infra/agentinfra/roadmap.py:59`; AST `a141578a6ed2a8b0dd3a2fecdb036fda924b1a772a0fc1293ab537e08a832f00`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: amendments, policy, require, requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[20].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:59`; AST `a0a75857d4a3dfeb05a5a63b6ca20fac423d97266fab55af513d0518b0d630e1`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[20].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[20].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:59`; AST `6f356e3e763cab2108605cbf4b0b1329ec91c323018ffee252107ba13c9b5905`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[20].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[21]::Expr

Source: `infra/agentinfra/roadmap.py:60`; AST `aaf4b89afe7373cbef7e597620011e570dedb7868bd96f4ba213dadcb99a4adc`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: n, range, require, requirement_ids, set. Outputs/bindings: n.
Calls/effect boundaries: range, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[21].value::Call

Source: `infra/agentinfra/roadmap.py:60`; AST `b645d02de11dbfaaf9c25c9e2712d838a684b3a9ee090338ec6958ae18d97d61`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: n, range, require, requirement_ids, set. Outputs/bindings: n.
Calls/effect boundaries: range, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[21].value.args[0].left::SetComp

Source: `infra/agentinfra/roadmap.py:60`; AST `ba16a68dd0eb1d8846f6c1ba61e7eab11226f30125c0971ec6b7d1f16c4d26a1`.

Rust module: `infra::agentinfra::roadmap`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: n, range. Outputs/bindings: n.
Calls/effect boundaries: range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[12].body[21].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[21].value.args[0].left.generators[0].iter::Call

Source: `infra/agentinfra/roadmap.py:60`; AST `560bb0be95e8792c936486dc9093c857def211e426d9da784a6a7b366c2f0892`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[21].value.args[0].left.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[21].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:60`; AST `6f356e3e763cab2108605cbf4b0b1329ec91c323018ffee252107ba13c9b5905`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[21].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[22]::For

Source: `infra/agentinfra/roadmap.py:61`; AST `c9513f66e364d82291813f8dfaebc8a41f97e6359075dd7337089d939221b786`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: count, n, prefix, range, require, requirement_ids, set. Outputs/bindings: count, n, prefix.
Calls/effect boundaries: range, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[22]; no call, error or mutation may be omitted. Iteration: (prefix, count) in (('BLUE-A', 14), ('BLUE-U', 22), ('DESTINY-A', 15))
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[22].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:62`; AST `78a42f5a8c951400760e1db8e21670d5b5725aeebbd7cf39f42b92c4638e97e5`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: count, n, prefix, range, require, requirement_ids, set. Outputs/bindings: n.
Calls/effect boundaries: range, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[22].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[22].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:62`; AST `b824313e3549f2b716fee7b2ffb2803bbb06e7efb7fd39a0acb3120c8b457a4a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: count, n, prefix, range, require, requirement_ids, set. Outputs/bindings: n.
Calls/effect boundaries: range, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[22].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[22].body[0].value.args[0].left::SetComp

Source: `infra/agentinfra/roadmap.py:62`; AST `895ad9efbe67b5e25c6332690bcd9a230ac5775494054d206d0c124b53f58706`.

Rust module: `infra::agentinfra::roadmap`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: count, n, prefix, range. Outputs/bindings: n.
Calls/effect boundaries: range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[12].body[22].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[22].body[0].value.args[0].left.generators[0].iter::Call

Source: `infra/agentinfra/roadmap.py:62`; AST `b3f91c11888a644f45ee39612b2789cd46881dfedfa03e7f9b567eae9868ea43`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: count, range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[22].body[0].value.args[0].left.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[22].body[0].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:62`; AST `6f356e3e763cab2108605cbf4b0b1329ec91c323018ffee252107ba13c9b5905`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[22].body[0].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[23]::Assign

Source: `infra/agentinfra/roadmap.py:63`; AST `4d92f99ad6f806d023e63012593b2edc4b7121545fa034de6e36280ccc0279a7`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: registry. Outputs/bindings: recipes.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24]::For

Source: `infra/agentinfra/roadmap.py:64`; AST `0a071f5f1096f385e2ae3c24227e78d24b87d3af4be53f5b8e0c2e2a0a5a126c`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: FIXED_RECIPES, int, name, recipe, recipes, require, type. Outputs/bindings: name, recipe.
Calls/effect boundaries: recipe.get, recipes.items, require, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[24]; no call, error or mutation may be omitted. Iteration: (name, recipe) in recipes.items()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].iter::Call

Source: `infra/agentinfra/roadmap.py:64`; AST `6a622bee49a8feaf0ce375e53a9c405ad7dbf0ae197aea1dd0c26304578e4741`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipes. Outputs/bindings: (none).
Calls/effect boundaries: recipes.items.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:65`; AST `9b90c11e417d0304c3e92d0c9fd8a4081f770aa09b2bd217940dcf8ce601d1bf`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[24].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:65`; AST `fbd6af8ade09803699fa2ffd9880eb91b6e338d658f5dfe381664ae36f28f932`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:65`; AST `09e7bb3f474c377bada1e64013a4817e11b655e5e7f7a8056e1a15e4fd3966ae`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[1]::Expr

Source: `infra/agentinfra/roadmap.py:66`; AST `e7aa3f7c84a79865f88d637a6d094cf2d9d19296357e00a729eed41be2dfcea8`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, recipe, require, type. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get, require, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[24].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:66`; AST `8070f612d7de7224988fc902a2acf04dfeff57cc29c9db7bcea2d9086a5c29ea`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, recipe, require, type. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get, require, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap.py:66`; AST `dbc88e1d518f71a8aab96f1865e6cb866c124cfa27c4522f34aa4e9ace07d26e`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe, type. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[1].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap.py:66`; AST `2aea0e0dabfba68824270c6ff2333d127a225abc6f2438712b598921af27c58c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].body[1].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[2]::Expr

Source: `infra/agentinfra/roadmap.py:67`; AST `7856ea02aa26b86b39afb96c2ca0b17ed926d88f1368e60f13abe44fbcc16864`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, recipe, require, type. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get, require, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[24].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:67`; AST `a79abdbcfc3a267bd3c2d1aa9dc55d08a53bcc6f80e23b4d200901856d56edf7`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, recipe, require, type. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get, require, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap.py:67`; AST `6c68256ba67c4a363beff309741a1dd1acf9437191d37b6d232ad0759eb6e97c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe, type. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[2].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap.py:67`; AST `876800936a7b0cea37d8487f5b6277ba4310c734f5abbb574e4e1ba749ae72d3`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe. Outputs/bindings: (none).
Calls/effect boundaries: recipe.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].body[2].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[3]::If

Source: `infra/agentinfra/roadmap.py:68`; AST `7e72ce84f6ad265200866ca116625c357c546a7b4975cc3c3903b7b8a868d47c`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: FIXED_RECIPES, name, recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[12].body[24].body[3]; no call, error or mutation may be omitted. Condition: recipe['kind'] == 'local_validation'
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:69`; AST `e0cc0eb4d3dda7f0f976afed99e6e9adce2e2263345dd72ecbb79c5442d6e9ee`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FIXED_RECIPES, name, recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[24].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[24].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:69`; AST `7d03a50f9278faca5c7487b4f3c5864c1f45ffe0849f76d248c5d0f79b597ad4`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FIXED_RECIPES, name, recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[24].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[25]::Assign

Source: `infra/agentinfra/roadmap.py:70`; AST `ef7bb1cf2b70352cbaf10bf1b611f328797a0a20e60324bb035c4ed5f04cb58e`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: milestones.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[25]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[26]::Assign

Source: `infra/agentinfra/roadmap.py:71`; AST `a63deea88f87a0b095f4c698da0cd0fd567fda80faed0a1d21aa38c90a132389`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, sources. Outputs/bindings: input_bindings.
Calls/effect boundaries: list.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[26]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[26].value::Call

Source: `infra/agentinfra/roadmap.py:71`; AST `3808ee1281387c09eed5c6a505bcf71f71a6a4563cb7e08e6ec08ebb42ff1550`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, sources. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[26].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27]::For

Source: `infra/agentinfra/roadmap.py:72`; AST `93bcbd087511c3e0ca1370f3c443b5c975c1a007853572012803a888ae530e68`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: FENCE, GATES, amendments, artifact, blocks, confined_path, dict, digest, ident, input_bindings, item, len, loads, milestones, path, paths, profile, project, raw, recipes, registry, require, requirement_ids, root, set, sorted, validate_record. Outputs/bindings: artifact, blocks, ident, item, path, paths, profile, project, raw.
Calls/effect boundaries: (root / 'Roadmaps' / project).glob, FENCE.findall, confined_path, confined_path(root, artifact, must_exist=True).is_file, dict, digest, input_bindings.append, len, loads, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, raw.decode, registry['projects'].items, require, set, sorted, validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[27]; no call, error or mutation may be omitted. Iteration: (project, profile) in registry['projects'].items()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].iter::Call

Source: `infra/agentinfra/roadmap.py:72`; AST `24b626e62d367bb5fae24fd8e5b734e7fa747aa37f61cc735a23072923a633cf`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: registry. Outputs/bindings: (none).
Calls/effect boundaries: registry['projects'].items.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:73`; AST `680e40669754d128f7308c98ce1782aa59aedd157758501f9bdab4043eb74461`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profile, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:73`; AST `f062319fbd72194e8e55a8eaf50c321a21daf2a88a3140f1163bcc0c6b2cbc6a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[1]::Assign

Source: `infra/agentinfra/roadmap.py:74`; AST `82a20c993bf4a8073da7dfdb96d60a095d7a085541c17cd58b955cd62a4f8e57`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: project, root, sorted. Outputs/bindings: paths.
Calls/effect boundaries: (root / 'Roadmaps' / project).glob, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[27].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:74`; AST `d0f8a5ea5b1b58f0d88accb26e2d2ad69ee6054c708e3903a2228ca29321fa1b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project, root, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'Roadmaps' / project).glob, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap.py:74`; AST `76a1c7b206fc91fe2f2719d9a9ed79c5ba3266b65f59e30a7110267664100dbd`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project, root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'Roadmaps' / project).glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[2]::Expr

Source: `infra/agentinfra/roadmap.py:75`; AST `dff2a614bf5fa74b7a7c2e4c5cfbe464944b06b9ae18120dd4abc6011a464e79`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, paths, profile, project, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:75`; AST `c1b3ba89bb0e8554ea362b2551b7473c64e236beb6d54481c48c59bc5f40303a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, paths, profile, project, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:75`; AST `f3a94d5a6b4b27987e5d6b89f94fd57d18ca3311ec9ced2a5262a2483df89046`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, paths. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[2].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:75`; AST `bff3a4e74365fd6022d8e5154cb9b9d477a315e81e10b6df1b4418391738f07f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, profile. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[2].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3]::For

Source: `infra/agentinfra/roadmap.py:76`; AST `028384e4b5acd970cafbfe400dfcdac63d70b1ba6d9562116716a53a31791c8d`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: FENCE, GATES, amendments, artifact, blocks, confined_path, dict, digest, ident, input_bindings, item, len, loads, milestones, path, paths, profile, project, raw, recipes, registry, require, requirement_ids, root, set, validate_record. Outputs/bindings: artifact, blocks, ident, item, path, raw.
Calls/effect boundaries: FENCE.findall, confined_path, confined_path(root, artifact, must_exist=True).is_file, dict, digest, input_bindings.append, len, loads, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, raw.decode, require, set, validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[27].body[3]; no call, error or mutation may be omitted. Iteration: path in paths
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:77`; AST `cb5aaaf42a08c91666ce0e4859112cf066cdeebf56910b462a58b24332914278`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: raw.
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[27].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:77`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap.py:78`; AST `371dfd96ff59d3a5f5b06d817c6c11c6206e6c1ceed347810af3d391dd209d68`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FENCE, raw. Outputs/bindings: blocks.
Calls/effect boundaries: FENCE.findall, raw.decode.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[27].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:78`; AST `18f7b95a40b0446b040f40ce24e79bde90ade3daa2695f707861af7581b06141`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FENCE, raw. Outputs/bindings: (none).
Calls/effect boundaries: FENCE.findall, raw.decode.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap.py:78`; AST `245aa6e406d6efc480215a639e092703d5658ef44570968198988a49d0620cdd`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.decode.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap.py:79`; AST `4ded7680d6e3c1895e2d1eaa88add4e7c65516b40532dcf9ec99150a63bf06d5`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: blocks, len, path, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:79`; AST `b8cbed62e1068c113a217ac10a7bd5e1bef88d27ad42ca868031bf6b2125809f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: blocks, len, path, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:79`; AST `10412414d7c108694ba58ff6bbaa85028ff907aa822e4f77e80d96cf09d31e2b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: blocks, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[3]::Assign

Source: `infra/agentinfra/roadmap.py:80`; AST `0a3b3f6fb7f0a208a420f42cb61879611000aaa75397211a5f88fc76175229f5`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: blocks, loads. Outputs/bindings: item.
Calls/effect boundaries: loads.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[27].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[3].value::Call

Source: `infra/agentinfra/roadmap.py:80`; AST `5a0c00eef83a37922fd5b0a2784d41cf902c8ddd30dd8689138398e6ebac4425`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: blocks, loads. Outputs/bindings: (none).
Calls/effect boundaries: loads.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[4]::Expr

Source: `infra/agentinfra/roadmap.py:81`; AST `011becb6a8226010a195edfb5232f49b9566bb37ae2e746ef4d8e424a68e0b2d`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[4].value::Call

Source: `infra/agentinfra/roadmap.py:81`; AST `0ca2a0f202afda25ab48147434af44dc42b9ec55b18c79afc3a83299d1dec7b7`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[5]::Assign

Source: `infra/agentinfra/roadmap.py:82`; AST `ea10ddee607f8143e2b3d623d48edb98e86ae1852002a4ae53a77742366c1b19`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item. Outputs/bindings: ident.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[27].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[6]::Expr

Source: `infra/agentinfra/roadmap.py:83`; AST `2db31379136c150f25f1df33cd1596e5d0b8e4a783e313a05b7732d1900f9ae3`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, milestones, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[6].value::Call

Source: `infra/agentinfra/roadmap.py:83`; AST `8e94629d6217d962f458bc14dc5d5eeef59507c6a88d6fc39b191ed660a33c7f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, milestones, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[7]::Expr

Source: `infra/agentinfra/roadmap.py:84`; AST `24eb5b428cfc6a01d9a8d3d8d77b2054eb717fb987fd265fbbda4ad998bd6da2`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, item, profile, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[7].value::Call

Source: `infra/agentinfra/roadmap.py:84`; AST `85291d3ea7a7eb0be0b3cdf7821346a17c70d9475fd7253770d460cd991f8069`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, item, profile, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[8]::Expr

Source: `infra/agentinfra/roadmap.py:85`; AST `979e3dd5158f13458106105d6f95dd9e634ac7c4c85b629d598e1a23bbad60fc`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, item, require, requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[8].value::Call

Source: `infra/agentinfra/roadmap.py:85`; AST `85d06e1cd0feddb458fe4b39cae0d3ca6145816c25b9af4d6c7317ced9733922`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, item, require, requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[8].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:85`; AST `64b5f71f9106f6705acdb8a018c182f84ca4b54977e363a835b694d29afc2d90`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[8].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[8].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:85`; AST `6f356e3e763cab2108605cbf4b0b1329ec91c323018ffee252107ba13c9b5905`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[8].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[9]::Expr

Source: `infra/agentinfra/roadmap.py:86`; AST `2e317770f997a7c7a84031c6ea1bcbdce73fb8e9fc90e9acf33fff07b6b8b1ae`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: amendments, ident, item, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[9].value::Call

Source: `infra/agentinfra/roadmap.py:86`; AST `02df6d2ee8561b9cf6dd34f1bc693f19ae31673f4abd88f429188283d539697b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: amendments, ident, item, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[9].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:86`; AST `0e5f5b23465090053aa0af36303d486111c7fb38e48b64efce90be4d932c7ee2`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[9].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[10]::Expr

Source: `infra/agentinfra/roadmap.py:87`; AST `4891681e60e73caee6f1b1a0c0fc9605bfc3df20766ad4d2c86593c42d937c5e`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, item, recipes, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[10].value::Call

Source: `infra/agentinfra/roadmap.py:87`; AST `ca1e13dfe41dd804ca9f9d8696fdf3beb14c10bb654c37472bac347553e8a34a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, item, recipes, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[10].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:87`; AST `90bd4cb86b8ce4122974cd667f1f10317c7397cacca32bf34a0582e00b0fd346`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[10].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[10].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:87`; AST `afcb4c99bddd7278b33dfb5118ae1a597ed55e9d1e515bfb2328dd13eac8cbbc`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipes, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[10].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[11]::Expr

Source: `infra/agentinfra/roadmap.py:88`; AST `0bed3b109bce68d26d1ce8dec890aa5669a091f41f35f96dd8afac77a6946a9b`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GATES, ident, item, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[11].value::Call

Source: `infra/agentinfra/roadmap.py:88`; AST `ca63b5d33312bd2f0e34ecd6f4803f78433f862bbdd2ef97ede562c4be637e83`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GATES, ident, item, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[11].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:88`; AST `367d3266a8bbfabd26c2af459a3fa34134d395f84775b405dc4ccdb2e9d61977`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[11].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[12]::Expr

Source: `infra/agentinfra/roadmap.py:89`; AST `894d3a9f1d54a37f78e081a4123bd482751bd279e4fa85b52202fda8e62fd3eb`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, item, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[12].value::Call

Source: `infra/agentinfra/roadmap.py:89`; AST `dc336a71483a6f2450a81db73f27abef12c9308c220ba396b7ea45897d75f66f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, item, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[13]::If

Source: `infra/agentinfra/roadmap.py:91`; AST `db8de646e8ff899b135d69810edba09aa8da7ca49b34f126253ffdd90a18d85b`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ident, item, registry, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[12].body[27].body[3].body[13]; no call, error or mutation may be omitted. Condition: item['phase'] == 'modernization'
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[13].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:92`; AST `6385b387b85aeaef1ab446ad0194bea1171c0816ef4e76a92f8a620f66000ec3`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, item, registry, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[13].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:92`; AST `ae0e943985ed563bc6b5aa51efbaadf8e28045fa3f0fc424c8129a16c20abd5c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, item, registry, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[13].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:92`; AST `146616ea39e46a75a95f2501a8fbfb2def8e2a983ac1786f2954cbc0e070920f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[13].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[13].body[0].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:92`; AST `361e2b2bda243682693c2766fff4c535390ae04a295ddfac85923cb5f47e951f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: registry, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[13].body[0].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[14]::For

Source: `infra/agentinfra/roadmap.py:93`; AST `a608330cae03ed9d47175d44c654ea17bd915667e540d710dbded6776f82732d`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: artifact, confined_path, item, require, root. Outputs/bindings: artifact.
Calls/effect boundaries: confined_path, confined_path(root, artifact, must_exist=True).is_file, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[27].body[3].body[14]; no call, error or mutation may be omitted. Iteration: artifact in item['references']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[14].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:94`; AST `d8502b4fcb2dca122519a65db83c400130a3c4421970c726e2a7436bb9073e83`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifact, confined_path, require, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, artifact, must_exist=True).is_file, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[14].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:94`; AST `43bbd4aff2fd3ca46104b36db047e93ca042daa05e1f7d2af06ee1a941cd8ad3`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifact, confined_path, require, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, artifact, must_exist=True).is_file, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[14].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap.py:94`; AST `a18559e127db2205a27dc9cdf69d06b1be15260cd6feb3c0c31e18b1b6cfd44f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifact, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, artifact, must_exist=True).is_file.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[14].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[14].body[0].value.args[0].func.value::Call

Source: `infra/agentinfra/roadmap.py:94`; AST `f187bffa03f2e71c97e9455984506845210456be85b999b76cb7243c2f736631`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifact, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[14].body[0].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[15]::Assign

Source: `infra/agentinfra/roadmap.py:95`; AST `6c4db0193a30ad48386f77060b1ac3094e29df78f6a42917aafe88b211cbe487`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, ident, item, milestones, path, root. Outputs/bindings: (none).
Calls/effect boundaries: dict, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[27].body[3].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[15].value::Call

Source: `infra/agentinfra/roadmap.py:95`; AST `a04dea1f59349f5774d7f497805842e5668e07a31dd4960e4abd1a9bcbcda905`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, item, path, root. Outputs/bindings: (none).
Calls/effect boundaries: dict, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[15].value.keywords[0].value::Call

Source: `infra/agentinfra/roadmap.py:95`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[15].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[15].value.keywords[0].value.func.value::Call

Source: `infra/agentinfra/roadmap.py:95`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[15].value.keywords[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[16]::Expr

Source: `infra/agentinfra/roadmap.py:96`; AST `3c035d10bcae5af42e3158283c4b98950111ed0bc871af3349b43adacba647d3`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, input_bindings, path, raw, root. Outputs/bindings: (none).
Calls/effect boundaries: digest, input_bindings.append, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[27].body[3].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[16].value::Call

Source: `infra/agentinfra/roadmap.py:96`; AST `984a53ce1f92bfd9ebab27b251359e35a21ef428e7c80a00c22b30ec37928c9a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, input_bindings, path, raw, root. Outputs/bindings: (none).
Calls/effect boundaries: digest, input_bindings.append, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[16].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap.py:96`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[16].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[16].value.args[0].values[0].func.value::Call

Source: `infra/agentinfra/roadmap.py:96`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[16].value.args[0].values[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[27].body[3].body[16].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap.py:96`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[27].body[3].body[16].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[28]::Assign

Source: `infra/agentinfra/roadmap.py:97`; AST `a8d44bd598291983265afde8adbf239a8f1dd93329df6ff906313b13ad555944`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: m, milestones, set. Outputs/bindings: covered, m.
Calls/effect boundaries: milestones.values, set, set().union.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[28]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[28].value::Call

Source: `infra/agentinfra/roadmap.py:97`; AST `2b62cea571bf42ac601201a19420b7d3ea31152ceff0c0ef3d9d004653a0b952`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: m, milestones, set. Outputs/bindings: m.
Calls/effect boundaries: milestones.values, set, set().union.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[28].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[28].value.func.value::Call

Source: `infra/agentinfra/roadmap.py:97`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[28].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[28].value.args[0].value::GeneratorExp

Source: `infra/agentinfra/roadmap.py:97`; AST `f94de8cc39e37af42d337ef95e2fb34ab140002d15de19aaee92ad842ad63be7`.

Rust module: `infra::agentinfra::roadmap`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: m, milestones, set. Outputs/bindings: m.
Calls/effect boundaries: milestones.values, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[28].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[28].value.args[0].value.elt::Call

Source: `infra/agentinfra/roadmap.py:97`; AST `39379b2370a126d0b0956219763e99fb17142227f3e1ccc591d13e63e1c145c9`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: m, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[28].value.args[0].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[28].value.args[0].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap.py:97`; AST `c826d9dc4eccf0348efa4031850fac70e53da15296e61224d654052dcb05e840`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestones. Outputs/bindings: (none).
Calls/effect boundaries: milestones.values.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[28].value.args[0].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[29]::Expr

Source: `infra/agentinfra/roadmap.py:98`; AST `a7bb65759f62f5c73fd4f45be8f6a26659de4de47d80a081c7c40eb4711f6207`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: covered, require, requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[29]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[29].value::Call

Source: `infra/agentinfra/roadmap.py:98`; AST `8db8593453dc4f177346367c30e0ff5f6fc3b3975fec7d9e3b88406627b139ec`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: covered, require, requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[29].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[29].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:98`; AST `6f356e3e763cab2108605cbf4b0b1329ec91c323018ffee252107ba13c9b5905`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[29].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[29].value.args[1].values[1].value.left::Call

Source: `infra/agentinfra/roadmap.py:98`; AST `6f356e3e763cab2108605cbf4b0b1329ec91c323018ffee252107ba13c9b5905`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirement_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[29].value.args[1].values[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[30]::For

Source: `infra/agentinfra/roadmap.py:99`; AST `e6463795af9a41511d9e53a3614b28943578a748c62c9efb32829eb78db95d96`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ident, milestones, require, requirement, requirements, set. Outputs/bindings: ident, requirement.
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[30]; no call, error or mutation may be omitted. Iteration: requirement in requirements
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[30].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:100`; AST `de8fcddb63b298ed64b7d98f8b5fe355d66b460d54903b00280b7242b8f127cb`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: milestones, require, requirement, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[30].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[30].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:100`; AST `f6a859b11bcc59d6e7d4ef05a8117d7d0aa1cf301a7932c06b9868ee15fd4252`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestones, require, requirement, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[30].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[30].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap.py:100`; AST `19b0eb490711b34e340794c7d56e8d4d055e884a5c2c3ef2c9dad1d1fc4f2e73`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirement, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[30].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[30].body[0].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:100`; AST `8d953eab800d96d498898fbf6ddd1b00d4e6ad037de36abcc45c88a1769bdf9b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestones, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[30].body[0].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[30].body[1]::For

Source: `infra/agentinfra/roadmap.py:101`; AST `49c6a5f2a2d59a14d9c7221c71f5216035e9b76e995c942c14073ee0fb01491b`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ident, milestones, require, requirement. Outputs/bindings: ident.
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[30].body[1]; no call, error or mutation may be omitted. Iteration: ident in requirement['milestones']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[30].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:102`; AST `46a998a6bb1556d53cea6fafa9198dfcec8f6434cafa4b1713aec59c47f2c606`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, milestones, require, requirement. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[30].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[30].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:102`; AST `f78408293080a1c3170f2d951081bd8d5eaca50fef33fba16b125d2871d0f8ca`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, milestones, require, requirement. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[30].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[31]::Assign

Source: `infra/agentinfra/roadmap.py:103`; AST `c7205f12f5cf7a5d23d180efeb73eba144ea11b512125e958f977480a916b420`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: active, order, seen.
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[31]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[31].value.elts[1]::Call

Source: `infra/agentinfra/roadmap.py:103`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[31].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[31].value.elts[2]::Call

Source: `infra/agentinfra/roadmap.py:103`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[31].value.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32]::FunctionDef

Source: `infra/agentinfra/roadmap.py:105`; AST `984fcfcc48282fdf44e6fd87390a49e222c625a847f277c80c934176c55747d8`.

Rust module: `infra::agentinfra::roadmap`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: active, dependency, ident, milestones, order, require, seen, sorted, str, visit. Outputs/bindings: dependency.
Calls/effect boundaries: active.add, active.remove, order.append, require, seen.add, sorted, visit.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[32]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:106`; AST `4048364bf047fde7770219f59ef3f5742dbc97db09bff7e1c1f135f92aaddce1`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, milestones, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[32].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:106`; AST `1ce2fe8dc36653cbea15de03e0e16d49eac4122cc3573b3fc0d75844e50f9a22`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, milestones, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[32].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[1]::Expr

Source: `infra/agentinfra/roadmap.py:107`; AST `b30f78dd24d75b60fe077e09ddfac1ffedeb2b0101995df7e022d6ad9e0e4c21`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: active, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[32].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:107`; AST `c56d1d66a7c07a8bb3e3815215b85a5d0da2036ecdf690243b21bb425d775eb0`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: active, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[32].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[2]::If

Source: `infra/agentinfra/roadmap.py:108`; AST `04e1c2fe4242be9d15d39c3bb847533b2a20e5016ab00bf8f1db0a4f0c44cdda`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ident, seen. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[12].body[32].body[2]; no call, error or mutation may be omitted. Condition: ident in seen
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap.py:109`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[12].body[32].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[3]::Expr

Source: `infra/agentinfra/roadmap.py:110`; AST `af1fddf4b3be98d38aa8568a5a96b860d29092923d557313939e060fe33f479d`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: active, ident. Outputs/bindings: (none).
Calls/effect boundaries: active.add.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[32].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[3].value::Call

Source: `infra/agentinfra/roadmap.py:110`; AST `b1988eeaa32e518434edb249f09e73a1a44a71c87369533d5e0d86309744056b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: active, ident. Outputs/bindings: (none).
Calls/effect boundaries: active.add.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[32].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[4]::For

Source: `infra/agentinfra/roadmap.py:111`; AST `81cbb915dd44cf9b415bba147e00df4c35dca9237b771289eac9c15a0060fd2d`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: dependency, ident, milestones, sorted, visit. Outputs/bindings: dependency.
Calls/effect boundaries: sorted, visit.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[32].body[4]; no call, error or mutation may be omitted. Iteration: dependency in sorted(milestones[ident]['dependencies'])
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[4].iter::Call

Source: `infra/agentinfra/roadmap.py:111`; AST `a9a7307d5e65f7cca2f3e4fa9ecf37a2c6218be89ee8400388c2f743bbb38a98`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, milestones, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[32].body[4].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:112`; AST `3cb9dd38da71c2ec15360fb2286fa3968b4dfcf99d4eb62654d1265d8091d397`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependency, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[32].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:112`; AST `33569d1901374ca48cd0f727764eacf73e9b1891368ad198d3a4569d8bba4c68`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[32].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[5]::Expr

Source: `infra/agentinfra/roadmap.py:113`; AST `b016f2eb9c68b3532988c11ca4012abb5f624632c0a8111f2892d302c2674db7`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: active, ident. Outputs/bindings: (none).
Calls/effect boundaries: active.remove.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[32].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[5].value::Call

Source: `infra/agentinfra/roadmap.py:113`; AST `8c4fd86f5b05f7f98eeeaa723e90f494eaafb65b8c9811d3bfb459b7f8fc802b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: active, ident. Outputs/bindings: (none).
Calls/effect boundaries: active.remove.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[32].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[6]::Expr

Source: `infra/agentinfra/roadmap.py:114`; AST `ae485f9ed2a02a5e3883e0a06b5fb14e0cda759d9500a0f0532774ee45f5dd89`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, seen. Outputs/bindings: (none).
Calls/effect boundaries: seen.add.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[32].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[6].value::Call

Source: `infra/agentinfra/roadmap.py:114`; AST `99ef893a2ff59cde446f36de0b92fd3548ca3bbb4aecc02702e21c38df2688a4`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, seen. Outputs/bindings: (none).
Calls/effect boundaries: seen.add.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[32].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[7]::Expr

Source: `infra/agentinfra/roadmap.py:115`; AST `485ae783f5b7390d2e5b1d84f353c17383113283c6f3a8602e9c809cb592ad2c`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, order. Outputs/bindings: (none).
Calls/effect boundaries: order.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[32].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::visit::root.body[12].body[32].body[7].value::Call

Source: `infra/agentinfra/roadmap.py:115`; AST `02419f86ea7054935ae93a1850d7e9e9fca5498e5dad7f1ee15ed70e09f04f3f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, order. Outputs/bindings: (none).
Calls/effect boundaries: order.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[32].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[33]::Assign

Source: `infra/agentinfra/roadmap.py:117`; AST `30004d15b8e5baf3cf669158c4348c874f9bf261abd5ab7b9f61257c2dc956a7`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: registry. Outputs/bindings: priority.
Calls/effect boundaries: registry.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[33]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[33].value::Call

Source: `infra/agentinfra/roadmap.py:117`; AST `81d25d1f97807305395ec1330ad3fadaffb4f2b233250e626f7089d5eaa9b5d0`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: registry. Outputs/bindings: (none).
Calls/effect boundaries: registry.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[33].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[34]::Expr

Source: `infra/agentinfra/roadmap.py:118`; AST `05bee37dbd008ca2024737e52ee1c0220de3ff814e1c9641214d832e4a0b1ab1`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, milestones, priority, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[34]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[34].value::Call

Source: `infra/agentinfra/roadmap.py:118`; AST `0d173e8d4889aca0d6ee4eadb5eee8d30375642a9698677bae10c5a168c92595`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, milestones, priority, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[34].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[34].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap.py:118`; AST `09d65db51f4c9dd778450f047f4aa3fa31492bfc0bdad8d5929ee2f57c2bc55f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, priority. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[34].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[34].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:118`; AST `5e12e74639d1bda2f5a03213bde2f41a8b97fce1a2378fe4c77d675329d8b1b1`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, milestones. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[34].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[34].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap.py:118`; AST `db881e16d94d484210794b786b2d89c1fc37ff1038f3eef773261ce68e656c0a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: priority, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[34].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[34].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:118`; AST `8d953eab800d96d498898fbf6ddd1b00d4e6ad037de36abcc45c88a1769bdf9b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestones, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[34].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[35]::For

Source: `infra/agentinfra/roadmap.py:119`; AST `b72d5d82541b8fd85d9e15cd3608126ec8326f2e902137946dce533fe97c868e`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ident, priority, visit. Outputs/bindings: ident.
Calls/effect boundaries: visit.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[35]; no call, error or mutation may be omitted. Iteration: ident in priority
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[35].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:120`; AST `8e0b272716f493f7d26d5f12930322cee59ce6b64eb2be966ae3f8b97c3079fd`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ident, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[35].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[35].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:120`; AST `e979bb23ca5b2f071b6c2209fa79e28decefd9250b55f7fcfb1ccf384871efd5`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ident, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[35].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[36]::Assign

Source: `infra/agentinfra/roadmap.py:121`; AST `2c5093df1eb4c8ddb6ae5d578ff122cdec23546244224814eeda0280045a7c35`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: providers.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[36]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[37]::Assign

Source: `infra/agentinfra/roadmap.py:122`; AST `14f84baf8a6fc17df14edece45469b8b85d42a65608c214a1d9ee882495acadd`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: obligations.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[37]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[38]::For

Source: `infra/agentinfra/roadmap.py:123`; AST `6ced81a3d34e37cc090ef3c64dbf4376a31dea5d1014db2cfcf7fe5042f1d00e`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: capability, ident, milestone, milestones, obligations, p, providers, require. Outputs/bindings: capability, ident, milestone, p.
Calls/effect boundaries: milestones.items, obligations.extend, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[38]; no call, error or mutation may be omitted. Iteration: (ident, milestone) in milestones.items()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[38].iter::Call

Source: `infra/agentinfra/roadmap.py:123`; AST `7194cb78f47315038b72cc27a3253835bb37196a10576c1713fafc578e789a91`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestones. Outputs/bindings: (none).
Calls/effect boundaries: milestones.items.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[38].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[38].body[0]::For

Source: `infra/agentinfra/roadmap.py:124`; AST `c51f2bdf0da78f0ca2a67ced1513264b7f6aa6d5f7b9c9084a189a19e8464a14`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: capability, ident, milestone, providers, require. Outputs/bindings: capability.
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[38].body[0]; no call, error or mutation may be omitted. Iteration: capability in milestone['provides']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[38].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:125`; AST `598570a81dd654fc0292b306e1970b10b57d321ae38a6764287ae313ab889779`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: capability, providers, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[38].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[38].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:125`; AST `2cfcd5791f8067ed6020498f913aae04b88b37f411aa0c0dec769af5713a0251`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: capability, providers, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[38].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[38].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap.py:126`; AST `9c1b09e88585e563f99881872a3b2e4afcfd6d610c4c19339bc09a6300cfb491`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: capability, ident, providers. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[38].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[38].body[1]::Expr

Source: `infra/agentinfra/roadmap.py:127`; AST `62226bb52e4474a5a896b7fcaa9e6ea8231b0035951a4e20564db626cbaede1e`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: milestone, obligations, p. Outputs/bindings: p.
Calls/effect boundaries: obligations.extend.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[38].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[38].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:127`; AST `42a563512f749fc57d5d2f095e60da4ed617275ad0380b8f8be4a73781125437`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestone, obligations, p. Outputs/bindings: p.
Calls/effect boundaries: obligations.extend.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[38].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[38].body[1].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap.py:127`; AST `dcd005687ce0da7ce34c25d717cf44d295a962597fe2b772c07e8303e8cf20a3`.

Rust module: `infra::agentinfra::roadmap`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: milestone, p. Outputs/bindings: p.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[38].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[39]::Expr

Source: `infra/agentinfra/roadmap.py:128`; AST `885bc98a45427e7ae7af716cd46a1727e6f75c8fa89260c1a996bf0cbdb1325c`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, obligations, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[39]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[39].value::Call

Source: `infra/agentinfra/roadmap.py:128`; AST `d4f4a2795597bb86df189c521dd8ca13178e6b03f76ef530e8d84ad9c71d82d3`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, obligations, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[39].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[39].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:128`; AST `aa832eaca9b8ad712344696fda175a5d53b6e55b2bda9c89270711d081b70dab`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, obligations. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[39].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[39].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:128`; AST `31dd98fac989937bf1005b40958258004ed58743c538b3f785093c619c3dfef3`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, obligations, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[39].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[39].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap.py:128`; AST `b48e7b355ad4da7241a4389f06b6a9fc17f07267ba61836e729108bcc33a33e0`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligations, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[39].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40]::For

Source: `infra/agentinfra/roadmap.py:129`; AST `5ef9ee34191cfb48973dc34624a46b42c6a56848b8e170de77bf379580df5017`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: c, consume, milestone, milestones, providers, require, set. Outputs/bindings: c, consume, milestone.
Calls/effect boundaries: milestones.values, providers.get, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[40]; no call, error or mutation may be omitted. Iteration: milestone in milestones.values()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40].iter::Call

Source: `infra/agentinfra/roadmap.py:129`; AST `c826d9dc4eccf0348efa4031850fac70e53da15296e61224d654052dcb05e840`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestones. Outputs/bindings: (none).
Calls/effect boundaries: milestones.values.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[40].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:130`; AST `150dcef5760278074909b4fad0f3ba500be08a50631db0b9b4c8534769c3a8bb`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, milestone, require, set. Outputs/bindings: c.
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[40].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:130`; AST `cca34d367556f56c569829a7eb3a7f7f244ab83dba1a5b4529e8c2be5b5e1d9d`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, milestone, require, set. Outputs/bindings: c.
Calls/effect boundaries: require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[40].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40].body[0].value.args[0].left::SetComp

Source: `infra/agentinfra/roadmap.py:130`; AST `3bb959df9b114be88c61db5241558e8842579fdffc9b8df0e4847aac30b7fd25`.

Rust module: `infra::agentinfra::roadmap`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: c, milestone. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[12].body[40].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40].body[0].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:130`; AST `9050b4d2019778fae2059a4711b93c13f82af3b0c7e9fbec89a30b4a05aa584a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestone, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[40].body[0].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40].body[1]::For

Source: `infra/agentinfra/roadmap.py:131`; AST `c7e458da6999564d8514a606aa5b32996c97282280396f00000e0293a3f4cb95`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: consume, milestone, providers, require. Outputs/bindings: consume.
Calls/effect boundaries: providers.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[40].body[1]; no call, error or mutation may be omitted. Iteration: consume in milestone['consumes']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:132`; AST `9d1b2969bda1c360268401d02a0d6b540d8021d753a49202bf4596d7d47dbf91`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: consume, providers, require. Outputs/bindings: (none).
Calls/effect boundaries: providers.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[40].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:132`; AST `a32944caf4cc662882c6bc2dfa9d0f9fe8cd4b2b4487409709c909d38cfbc514`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: consume, providers, require. Outputs/bindings: (none).
Calls/effect boundaries: providers.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[40].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[40].body[1].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:132`; AST `092c6dc3818969264b71f446d46ab25eb245f7a63cc2fe53390208b20106e8bd`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: consume, providers. Outputs/bindings: (none).
Calls/effect boundaries: providers.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[40].body[1].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[41]::Assign

Source: `infra/agentinfra/roadmap.py:133`; AST `e0789fd1dc65712f17d1b91fa64b6f4bb5ba48552e99e8bf16906e38964493de`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, p, registry, root. Outputs/bindings: name, p, project_docs.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[41]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[41].value::SetComp

Source: `infra/agentinfra/roadmap.py:133`; AST `bd4f5c4135c6bd56ab987f1f7bf7d6b1694ef7dd95f0a86ce47efec3a530cc80`.

Rust module: `infra::agentinfra::roadmap`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: name, p, registry, root. Outputs/bindings: name, p.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[12].body[41].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42]::For

Source: `infra/agentinfra/roadmap.py:134`; AST `07f125c40bcd8fe491ad1ac112f6a751e4de2e41d13fe9e9fd304a866b170068`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: digest, input_bindings, path, project_docs, root, set, shared, sorted. Outputs/bindings: path.
Calls/effect boundaries: (root / 'bin').glob, (root / 'infra').rglob, (root / 'scripts').glob, (root / 'verification/roadmap').glob, (shared / 'ci').glob, (shared / 'codex-protocol').glob, (shared / 'skills').rglob, digest, input_bindings.append, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, set, shared.glob, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[12].body[42]; no call, error or mutation may be omitted. Iteration: path in sorted(set(shared.glob('*.json')) | set(shared.glob('*.md')) | set((shared / 'codex-protocol').glob('*.json')) | set((root / 'infra').rglob('*.py')) | set((root / 'scripts').glob('*.py')) | set((root / 'bin').glob('*.py')) | set((root / 'verification/roadmap').glob('*.py')) | set((shared / 'ci').glob('*.py')) | set((shared / 'skills').rglob('SKILL.md')) | project_docs)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter::Call

Source: `infra/agentinfra/roadmap.py:134`; AST `aa0e20d6c901935e3b6d8de0618183f4c282cd58d632a69df357de87775e48ef`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: project_docs, root, set, shared, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'bin').glob, (root / 'infra').rglob, (root / 'scripts').glob, (root / 'verification/roadmap').glob, (shared / 'ci').glob, (shared / 'codex-protocol').glob, (shared / 'skills').rglob, set, shared.glob, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.left.left::Call

Source: `infra/agentinfra/roadmap.py:134`; AST `59bab370a96ddf0bc45cac099fcc835cad110302ccf8aac24453d8f1fb8d8031`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, shared. Outputs/bindings: (none).
Calls/effect boundaries: set, shared.glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.left.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.left.left.args[0]::Call

Source: `infra/agentinfra/roadmap.py:134`; AST `ceca5cbab320aca2690ae9f36fa34e897d53274ce105f1f408acf542e0b263d4`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.left.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.left.right::Call

Source: `infra/agentinfra/roadmap.py:134`; AST `3a183307d9d237008894d591ddad7ba70a93f33ada7e41227350cf4eff1fecd5`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, shared. Outputs/bindings: (none).
Calls/effect boundaries: set, shared.glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.left.right.args[0]::Call

Source: `infra/agentinfra/roadmap.py:134`; AST `83a24911565da1f444d43bf5626e9e1cc1d065b96865a81285e304500f652d84`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.right::Call

Source: `infra/agentinfra/roadmap.py:134`; AST `186a66dcff949773fde335d5c7bd9464d2e21178f30b18f63df887abf9d9ed1a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, shared. Outputs/bindings: (none).
Calls/effect boundaries: (shared / 'codex-protocol').glob, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.right.args[0]::Call

Source: `infra/agentinfra/roadmap.py:134`; AST `1f0de6fbc7a58a295d9294555eb6c5dff9913316ace819a6afab21ccae99b32b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: (shared / 'codex-protocol').glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.left.left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.left.right::Call

Source: `infra/agentinfra/roadmap.py:135`; AST `8a47de429e4215622d79c9c9d1809b362b52d302adc8185c66d5b89eb2febc73`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, set. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra').rglob, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.left.right.args[0]::Call

Source: `infra/agentinfra/roadmap.py:135`; AST `6d42e6184f06d1165e25c013f9418f175c05dac844e71463851265e7bf43a6ca`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'infra').rglob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.right::Call

Source: `infra/agentinfra/roadmap.py:135`; AST `d2c1db7eb05319145c95915ccfdcc6fa4c3f5ece8b3f67f65e72d8491957de80`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, set. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'scripts').glob, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.left.right.args[0]::Call

Source: `infra/agentinfra/roadmap.py:135`; AST `ae5f0edbcf92cc78cb6dce612731896115f5650f586e47d47edaa7b292ef0a83`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'scripts').glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.right::Call

Source: `infra/agentinfra/roadmap.py:136`; AST `5c2040b6b1ebab31b909317da1be94bd9a189a7549a36a20e9e9bede6b63a903`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, set. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'bin').glob, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.left.right.args[0]::Call

Source: `infra/agentinfra/roadmap.py:136`; AST `388f98757f38e7ab0897c03548f9c1425934d97de8ca6900b4391a4a5807da0c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'bin').glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.right::Call

Source: `infra/agentinfra/roadmap.py:136`; AST `46f3c6036715d98a3c50d311aadf17ae5ccfc13b6ff1cff26c22a5e36fb6660f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, set. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'verification/roadmap').glob, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.left.right.args[0]::Call

Source: `infra/agentinfra/roadmap.py:136`; AST `8f5ae242590b776ec07afc9e23454e62b6f72c97e10834bbfc54d686e33d9310`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'verification/roadmap').glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.right::Call

Source: `infra/agentinfra/roadmap.py:137`; AST `57cc8b5cca4b3f2bb32914724068134a719485716daad322eb955240c676354d`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, shared. Outputs/bindings: (none).
Calls/effect boundaries: (shared / 'ci').glob, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.left.right.args[0]::Call

Source: `infra/agentinfra/roadmap.py:137`; AST `ee4f273fac5e6f5d83f5c4695baf54766b79673c5a0defe0dd067ae6695d29de`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: (shared / 'ci').glob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.right::Call

Source: `infra/agentinfra/roadmap.py:137`; AST `a9fcd44855914133c0f49c802bb4bd2146c1d178df7c1de7f16ce09a25a6a323`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, shared. Outputs/bindings: (none).
Calls/effect boundaries: (shared / 'skills').rglob, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].iter.args[0].left.right.args[0]::Call

Source: `infra/agentinfra/roadmap.py:137`; AST `2d334d07dabba027b40fa42f7763dfa2eabbb621e464a320e3fd815582b13baa`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: (shared / 'skills').rglob.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].iter.args[0].left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:138`; AST `7b6012a7064f8e439111a07501164be7dc887f5777adadf49cdf2a2dbbb18f22`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, input_bindings, path, root. Outputs/bindings: (none).
Calls/effect boundaries: digest, input_bindings.append, path.read_bytes, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[42].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:138`; AST `af3607b98a190294bdb193530839fc967d12dae46271669bd51e619883183d13`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, input_bindings, path, root. Outputs/bindings: (none).
Calls/effect boundaries: digest, input_bindings.append, path.read_bytes, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap.py:138`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].body[0].value.args[0].values[0].func.value::Call

Source: `infra/agentinfra/roadmap.py:138`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].body[0].value.args[0].values[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap.py:138`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[42].body[0].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap.py:138`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[42].body[0].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[43]::Assign

Source: `infra/agentinfra/roadmap.py:139`; AST `c3435d810664301402f6f68980773504d54bf0266ffd17fb776a68eac222edf9`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: input_bindings, milestones, order, policy, recipes, registry, requirement_ids. Outputs/bindings: result.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[43]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[44]::Assign

Source: `infra/agentinfra/roadmap.py:143`; AST `ea550629d25e1f9e71896bf31374af5bfddb3e00134f1ff852e05146c14aecd2`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, result. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[44]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[44].value::Call

Source: `infra/agentinfra/roadmap.py:143`; AST `9ddec37ebb871d950d3273f3c19aaf26231ea1c560172aa64604b6f8dc8f2faf`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, result. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[12].body[44].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::compile_roadmaps::root.body[12].body[45]::Return

Source: `infra/agentinfra/roadmap.py:144`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[12].body[45]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap.py:147`; AST `80181bbd2e87de2b0af0c314d0265286ef81b938026f5567559f1a008db45599`.

Rust module: `infra::agentinfra::roadmap`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, accepted, actual, bindings_current, bool, by_milestone, candidates, compiled, contract, d, dependencies, dict, digest, evidence, good, ident, ids, isinstance, len, list, minimum, missing, obligation, p, proof, proof_errors, proofs, python_proof_errors, r, receipt, receipts, rejected, require, required, result, result_proof, root, set, sorted, state, validate_record. Outputs/bindings: accepted, actual, by_milestone, candidates, contract, d, dependencies, good, ident, ids, minimum, missing, obligation, p, proof, proofs, r, receipt, receipts, rejected, required, result, result_proof, state.
Calls/effect boundaries: accepted.append, bindings_current, bool, by_milestone.get, by_milestone.setdefault, by_milestone.setdefault(receipt['milestone'], []).append, candidates.add, digest, evidence.get, isinstance, len, missing.append, p.get, p.get('obligation', {}).get, proof.get, proof_errors, python_proof_errors, r.get, receipt.get, receipt['configuration'].get, rejected.append, require, set, sorted, validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:148`; AST `aa3e51a46dbd8d68e03129205e7cfe71cddc8de42eb4fab4ff9336c0d304b3a3`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[1]::Expr

Source: `infra/agentinfra/roadmap.py:153`; AST `c43935402f60bb1bc3c071d11081f51eedc1f98a56fea232a5a9b171ac69bf7f`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: evidence, require. Outputs/bindings: (none).
Calls/effect boundaries: evidence.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:153`; AST `6a8ad037c803073129dc24d3336b11999bc0611d18f63ee16b39a305bb5ccbe1`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: evidence, require. Outputs/bindings: (none).
Calls/effect boundaries: evidence.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:153`; AST `51cfce680f3302fe29bb7b109bf58495e5a7ddcd056987c63d190e91b224baa9`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: evidence. Outputs/bindings: (none).
Calls/effect boundaries: evidence.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap.py:154`; AST `de78e18bef6f76e6e5d02447120b138282c94496b2a2240a5d1435453360b47e`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:154`; AST `3266697421ec65f1c9ddda37802c950e891845622ee7eeeff961aca7f6857c8b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap.py:154`; AST `e4376bee10cb5ac58b23e27129b2002e1436b91face64325fcbf8a25771ff8e7`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[3]::Expr

Source: `infra/agentinfra/roadmap.py:155`; AST `81acf5d98e86faeac16713119cebbf37e1254b3144d14317bcdc6906d1cd3870`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, evidence, require. Outputs/bindings: (none).
Calls/effect boundaries: evidence.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[3].value::Call

Source: `infra/agentinfra/roadmap.py:155`; AST `32eb80e4f5054a217feed3924c5e66983a23c6533a6650b0be38f71db83a35de`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, evidence, require. Outputs/bindings: (none).
Calls/effect boundaries: evidence.get, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:155`; AST `fc6622a8c004fac8ff7c87e76c00f53e3c7e268f26bc9b7792123ff7a432b1ab`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: evidence. Outputs/bindings: (none).
Calls/effect boundaries: evidence.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[4]::Assign

Source: `infra/agentinfra/roadmap.py:156`; AST `976b6a9ed2593b3423f2fca8dbf0480e92291af368e07adc0c7e70f530e989cb`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: evidence. Outputs/bindings: receipts.
Calls/effect boundaries: evidence.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[4].value::Call

Source: `infra/agentinfra/roadmap.py:156`; AST `cb6b1ffbe2a92a3f994b56f52eeddb29058dddaa1c1400af33200d72beec7c13`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: evidence. Outputs/bindings: (none).
Calls/effect boundaries: evidence.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[5]::Expr

Source: `infra/agentinfra/roadmap.py:157`; AST `ac07a978a6bacd225565cf1b5b2b3abf67cda4e3fb5c0c04b2dbafd89d57b1d3`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isinstance, list, receipts, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[5].value::Call

Source: `infra/agentinfra/roadmap.py:157`; AST `b35bc563de720e629eac10bffcd0f641f1a1486c4e794c85cd8801e4c0261229`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, receipts, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[5].value.args[0]::Call

Source: `infra/agentinfra/roadmap.py:157`; AST `3dd43ad0fb2bdc28a7ee72373e1e1589773cafad8c2d362de296e12813b438a7`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, receipts. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[6]::Assign

Source: `infra/agentinfra/roadmap.py:158`; AST `18a32bdd618d0ef2732491047c9aa80a7a20792c4396a134dc463e71c1d3fc00`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r, receipts. Outputs/bindings: ids, r.
Calls/effect boundaries: r.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[6].value::ListComp

Source: `infra/agentinfra/roadmap.py:158`; AST `2b22aec3bb9e3db98b5e18ab014d45332873d4c54facfabe30946b45964967a0`.

Rust module: `infra::agentinfra::roadmap`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: r, receipts. Outputs/bindings: r.
Calls/effect boundaries: r.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[6].value.elt::Call

Source: `infra/agentinfra/roadmap.py:158`; AST `653487600c190ce4495e638ea5fd820466f7c750d9527534ab567008dc7eae66`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[7]::Expr

Source: `infra/agentinfra/roadmap.py:159`; AST `e32fd340e13220d6e74ee3de9ad16c8d954ec94ba562a554a6c2f5ddd1709307`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[7].value::Call

Source: `infra/agentinfra/roadmap.py:159`; AST `acb121fab656eaddd2f5e8f75147cc72df1eec1c57d77a35dd9a5058e116a608`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[7].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:159`; AST `e9ff8c6d4cd447580e3ae476d39cdd538e64139104de929c715ef5318d853424`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[7].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:159`; AST `392a9c6c899c1b887c4cb41a948a33de0352ff7c7be2a32c7a4d965ee6b3a8a2`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[7].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap.py:159`; AST `b5d0e953c49c3b05c4f5acc7b5c0af435cfb16d965600b49af73f1b9fe8b980e`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[8]::Assign

Source: `infra/agentinfra/roadmap.py:160`; AST `64a25def128075d2827686ba5950aff1831a1128094a40b87add42132643e328`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: by_milestone.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[9]::For

Source: `infra/agentinfra/roadmap.py:161`; AST `3b383978abd07f2e5b4f3b242d007f37f366b7c763441a2038e9686802a42653`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: by_milestone, compiled, receipt, receipts, require, root, validate_record. Outputs/bindings: receipt.
Calls/effect boundaries: by_milestone.setdefault, by_milestone.setdefault(receipt['milestone'], []).append, require, validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[13].body[9]; no call, error or mutation may be omitted. Iteration: receipt in receipts
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[9].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:162`; AST `c9b2f0103891b1cd42b7839dd114c406f24421dc914796e9cd4de891d190d258`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:162`; AST `ea4e054b22d82ce959d88540507f7d4dcae88502dbfbd701b7adfebe5531ccda`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[9].body[1]::Expr

Source: `infra/agentinfra/roadmap.py:163`; AST `e7b5bbe6fd7b1e06328aa12ec2f2110a9b970f4e3bb7637d053c5be731d6184e`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[9].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:163`; AST `45ba2e272e80470aa8f2d641bd9dbc9a5e6502c1c409ac52a01f7e9eba06e0a4`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[9].body[2]::Expr

Source: `infra/agentinfra/roadmap.py:164`; AST `3dd116446e44c84564c8304fc0a8ae528caf9b349230d4bfbb62fbecb4990175`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: by_milestone, receipt. Outputs/bindings: (none).
Calls/effect boundaries: by_milestone.setdefault, by_milestone.setdefault(receipt['milestone'], []).append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[9].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:164`; AST `61fc5c54e7468f32a79df19a09e82762db80ed35b2d93cf5c0294457e77879c0`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_milestone, receipt. Outputs/bindings: (none).
Calls/effect boundaries: by_milestone.setdefault, by_milestone.setdefault(receipt['milestone'], []).append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[9].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap.py:164`; AST `00a8af9ba9d65a4939c88c998e23898a23f90b4564dfe73463dacb5894dc6bf2`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_milestone, receipt. Outputs/bindings: (none).
Calls/effect boundaries: by_milestone.setdefault.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[10]::Assign

Source: `infra/agentinfra/roadmap.py:165`; AST `2c435ecac12c985901bb8025f4efe5e5ad7e200542d8b36f3e0370612550a391`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: result.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11]::For

Source: `infra/agentinfra/roadmap.py:166`; AST `dfc83f74927730a834a23b80b98b506e340d9de9e3fa51ff6706279037f5713d`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: accepted, actual, bindings_current, bool, by_milestone, candidates, compiled, contract, d, dependencies, digest, good, ident, len, minimum, missing, obligation, p, proof, proof_errors, proofs, python_proof_errors, receipt, rejected, require, required, result, result_proof, root, set, sorted, state, validate_record. Outputs/bindings: accepted, actual, candidates, contract, d, dependencies, good, ident, minimum, missing, obligation, p, proof, proofs, receipt, rejected, required, result_proof, state.
Calls/effect boundaries: accepted.append, bindings_current, bool, by_milestone.get, candidates.add, digest, len, missing.append, p.get, p.get('obligation', {}).get, proof.get, proof_errors, python_proof_errors, receipt.get, receipt['configuration'].get, rejected.append, require, set, sorted, validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[13].body[11]; no call, error or mutation may be omitted. Iteration: ident in compiled['order']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:167`; AST `3274c77af5359007d2f8bc496a87be7437eb15d49a0bc0b11aae356556b2afcb`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, ident. Outputs/bindings: contract.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[1]::Assign

Source: `infra/agentinfra/roadmap.py:168`; AST `56f2d51e7749f0a88aeddd55978b4ed2946071972abaf7c8819f55861b184065`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: accepted.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[2]::Assign

Source: `infra/agentinfra/roadmap.py:169`; AST `3f4bb7b1490fad9df6256b46fb045ee38f06644dba497d3977edda6c820ba8bf`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: candidates.
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:169`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[3]::Assign

Source: `infra/agentinfra/roadmap.py:170`; AST `846056777d95337933ada8586b67d5a5ee112e9c5aa07a9993438cfb83ad6527`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: rejected.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4]::For

Source: `infra/agentinfra/roadmap.py:171`; AST `7a23753bb478e67ae6e19643982f4e6ca3bb2698a9680f104a5d489abd98a563`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: accepted, actual, bindings_current, bool, by_milestone, candidates, contract, digest, good, ident, len, minimum, obligation, p, proof, proof_errors, proofs, python_proof_errors, receipt, rejected, require, required, result_proof, root, set, sorted, validate_record. Outputs/bindings: actual, good, minimum, obligation, p, proof, proofs, receipt, required, result_proof.
Calls/effect boundaries: accepted.append, bindings_current, bool, by_milestone.get, candidates.add, digest, len, p.get, p.get('obligation', {}).get, proof.get, proof_errors, python_proof_errors, receipt.get, receipt['configuration'].get, rejected.append, require, set, sorted, validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[13].body[11].body[4]; no call, error or mutation may be omitted. Iteration: receipt in by_milestone.get(ident, [])
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].iter::Call

Source: `infra/agentinfra/roadmap.py:171`; AST `2b9ebf75d2ae439e3992e37523c3b63782fd2a00d5138cada10738db4103c027`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_milestone, ident. Outputs/bindings: (none).
Calls/effect boundaries: by_milestone.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:172`; AST `693b554bbfaa1a45447fdea0ff8c627db16dd8150f40d1b4e29a9c6d2cdb3105`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:172`; AST `a98176bb65b47611af7d5fdafe8716be8d321816258d6e7090b95da2a478f568`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap.py:173`; AST `9ffef77ea4a07902e279e0de5d8e038842912718757224de40640db8d41ef2ab`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, contract, digest, receipt, root. Outputs/bindings: good.
Calls/effect boundaries: bindings_current, digest.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[1].value.values[2].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:174`; AST `1253f0f07ad69eba5dc7892142a2e1dca56b8de30947ef3013ae84aeb4801584`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[1].value.values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[1].value.values[3]::Call

Source: `infra/agentinfra/roadmap.py:175`; AST `1269aff854076b908d26831e2a0004c1469e3db3f78bbf9cb5944dcdd64c9ffc`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, receipt, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[1].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[1].value.values[4]::Call

Source: `infra/agentinfra/roadmap.py:176`; AST `4135bda17568f5f6bc1ed34100bacdbba6adfd6c3b68935a2af63ac5c70e6ee7`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, receipt, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[1].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[1].value.values[5]::Call

Source: `infra/agentinfra/roadmap.py:177`; AST `87f2691b8821c182523602ddb7c1bd15a4bd72ab1695b2129c36ca9337d7fdf4`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, receipt, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[1].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[2]::If

Source: `infra/agentinfra/roadmap.py:178`; AST `1a1189369f0a96da30c681da50bed445357d9e6697eb79cec673cdf69292ae2c`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: contract, good, receipt, sorted. Outputs/bindings: good.
Calls/effect boundaries: receipt['configuration'].get, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[11].body[4].body[2]; no call, error or mutation may be omitted. Condition: receipt['gate'] == 'implemented_outputs'
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:179`; AST `8a39a3e46637ae07e18d47b4e99d77b481a83aac785e4570b64218f21f26f739`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, good, receipt, sorted. Outputs/bindings: good.
Calls/effect boundaries: receipt['configuration'].get, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[2].body[0].value.values[1].left::Call

Source: `infra/agentinfra/roadmap.py:179`; AST `0ad4b9cbf3e66552157992c8f59d7be19856a2ce2435ceedb6a04fa751ebd56b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, sorted. Outputs/bindings: (none).
Calls/effect boundaries: receipt['configuration'].get, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[2].body[0].value.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[2].body[0].value.values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap.py:179`; AST `bd990d4592cf6666c99482235a0ab20bc35b245867319b703d2d5f01d835b99a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: receipt['configuration'].get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[2].body[0].value.values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[2].body[0].value.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:179`; AST `99f2775bbb4bacc2d3df544f3cc06c28988f99304e45e6e064865b94463d73ac`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[2].body[0].value.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[2].body[0].value.values[2].left::Call

Source: `infra/agentinfra/roadmap.py:180`; AST `24e866170b485fc1f55a89c79e45d30a3045d8cd3c0b362cf5f4e34cc2a244d8`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, sorted. Outputs/bindings: (none).
Calls/effect boundaries: receipt['configuration'].get, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[2].body[0].value.values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[2].body[0].value.values[2].left.args[0]::Call

Source: `infra/agentinfra/roadmap.py:180`; AST `ccc569ea09515a975f9a2081ef3c6af28817481bdeff2c989c91a6e1804f72ce`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: receipt['configuration'].get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[2].body[0].value.values[2].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[2].body[0].value.values[2].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:180`; AST `16eaa1749d7ed0f49569539776a24f9acb9e286b08a542f3a0e4828588e1ed5b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[2].body[0].value.values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3]::If

Source: `infra/agentinfra/roadmap.py:181`; AST `ba25f7317f2de39c221752e9a2550573f23075b8a7681f19efdfc4186781e256`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: actual, bindings_current, bool, contract, good, len, minimum, obligation, p, proof, proof_errors, proofs, python_proof_errors, receipt, required, result_proof, root, set, sorted, validate_record. Outputs/bindings: actual, good, minimum, obligation, p, proof, proofs, required, result_proof.
Calls/effect boundaries: bindings_current, bool, len, p.get, p.get('obligation', {}).get, proof.get, proof_errors, python_proof_errors, receipt.get, receipt['configuration'].get, set, sorted, validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[11].body[4].body[3]; no call, error or mutation may be omitted. Condition: receipt['gate'] == 'full_domain_proof'
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:182`; AST `871d372e170c57dbe49c7c33d5b26dc5e2e9a4461c5bb4def10e3cbac9154706`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: proofs.
Calls/effect boundaries: receipt.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[4].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:182`; AST `c58d3438fa2c2d1c51b2d7a9a0b7cb20327113b36550e5760cec5fe2d5439081`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: receipt.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap.py:183`; AST `4d1475468466bf0f9b9995cc936fb06519ca4c2b7cf39c00c34262cf69f9b71a`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: required.
Calls/effect boundaries: receipt['configuration'].get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[4].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:183`; AST `2dac18202d25beab9ea8942b2273eff944b1db131d2c0025b7590c41e2b563e9`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: receipt['configuration'].get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[2]::Assign

Source: `infra/agentinfra/roadmap.py:184`; AST `65b93ba8b9880e3214caf8283790358a891ab82a084b88247c868616e2d66454`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p, proofs. Outputs/bindings: actual, p.
Calls/effect boundaries: p.get, p.get('obligation', {}).get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[4].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[2].value::ListComp

Source: `infra/agentinfra/roadmap.py:184`; AST `10d166513d0f5381ac2abe3093287901ae1db50e479179169b7b341456f9d1f9`.

Rust module: `infra::agentinfra::roadmap`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: p, proofs. Outputs/bindings: p.
Calls/effect boundaries: p.get, p.get('obligation', {}).get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[11].body[4].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[2].value.elt::Call

Source: `infra/agentinfra/roadmap.py:184`; AST `56613ecb13d3e0695f630707265925edd81def16a83a794ce0a966699428d887`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.get, p.get('obligation', {}).get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[2].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[2].value.elt.func.value::Call

Source: `infra/agentinfra/roadmap.py:184`; AST `2391935b32428c65f51d127f991749a9519f63956747df49297e3ef15a58564d`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[2].value.elt.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[3]::Assign

Source: `infra/agentinfra/roadmap.py:185`; AST `c9567e7732df3bdbe6d83f24bc5ed6117a39fc15fbb8e887b11ac4b064b48c55`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, p. Outputs/bindings: minimum, p.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[4].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[3].value::SetComp

Source: `infra/agentinfra/roadmap.py:185`; AST `7f5d0092e404abd99550b15a1bcbcdc327eb77d12762c725062c160650273e57`.

Rust module: `infra::agentinfra::roadmap`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: contract, p. Outputs/bindings: p.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[11].body[4].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[4]::Assign

Source: `infra/agentinfra/roadmap.py:186`; AST `12db66332dbef20f81fc15f31b45a5b3f1eaa81385c414e54e6e09bac4b4b262`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, bool, good, len, minimum, required, set, sorted. Outputs/bindings: good.
Calls/effect boundaries: bool, len, set, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[4].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[4].value.values[1]::Call

Source: `infra/agentinfra/roadmap.py:186`; AST `36a656515d1fed103d071b8a04f760b19474e347e094327b17a942de466ef0f5`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, required. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[4].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[4].value.values[2].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:186`; AST `80501c0ec40fe29b73f36c3dfa25a3f820126585e1d283c476b217a199ece8cd`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: required, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[4].value.values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[4].value.values[3].left::Call

Source: `infra/agentinfra/roadmap.py:187`; AST `90a1982def62dfa1037d7200016e32235f53757032252f8eebfed9b1603095e7`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, required. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[4].value.values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[4].value.values[3].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:187`; AST `907a664a05565bd0a99bb3c8260dfe4a3f766a27f3b867850f0b0f9b62d38f45`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, required, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[4].value.values[3].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[4].value.values[3].comparators[0].args[0]::Call

Source: `infra/agentinfra/roadmap.py:187`; AST `80501c0ec40fe29b73f36c3dfa25a3f820126585e1d283c476b217a199ece8cd`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: required, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[4].value.values[3].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[4].value.values[4].left::Call

Source: `infra/agentinfra/roadmap.py:187`; AST `0124cac58d657ecfd7323988ef683ecb99334a4a6c2aa0ccf1f4964dbb4e6ddd`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[4].value.values[4].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[4].value.values[4].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:187`; AST `f0eb72205455ed55daf591b4d4d2e61928dfbabfc74700baf10e61a10479c607`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: required, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[4].value.values[4].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5]::For

Source: `infra/agentinfra/roadmap.py:188`; AST `749896b71fb98027f292492d6c8a9b76484dd735fca2169db02c16c0213ee9ba`.

Rust module: `infra::agentinfra::roadmap`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: bindings_current, good, obligation, proof, proof_errors, proofs, python_proof_errors, receipt, result_proof, root, validate_record. Outputs/bindings: good, obligation, proof, result_proof.
Calls/effect boundaries: bindings_current, proof.get, proof_errors, python_proof_errors, validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[13].body[11].body[4].body[3].body[5]; no call, error or mutation may be omitted. Iteration: proof in proofs
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:189`; AST `7d13ed8f2d58d0dbd15a70c3a5b4f8d460ce6d111c2688db76a59f7d5852e871`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proof. Outputs/bindings: obligation, result_proof.
Calls/effect boundaries: proof.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[4].body[3].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[0].value.elts[0]::Call

Source: `infra/agentinfra/roadmap.py:189`; AST `87dd75576c1fe44a3b5af4247e7a25822712dce59f9d731c09ddb70890c1bab5`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof. Outputs/bindings: (none).
Calls/effect boundaries: proof.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[5].body[0].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[0].value.elts[1]::Call

Source: `infra/agentinfra/roadmap.py:189`; AST `3f90f8a1a3b4ca2522bc5256fcf6aad27ef43438dbd4d10dcd4da89620eb31e1`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proof. Outputs/bindings: (none).
Calls/effect boundaries: proof.get.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[5].body[0].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[1]::Expr

Source: `infra/agentinfra/roadmap.py:190`; AST `2e179482e3a69ad877f8ac58b2c3ebca3a6f9b190e07a75f3b9dc8778a4015ac`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[11].body[4].body[3].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:190`; AST `9a42878ffb0512bc22fcb3d19d90820d1600e599b18525cff9deb2c80d8c4034`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[2]::ImportFrom

Source: `infra/agentinfra/roadmap.py:191`; AST `40199cc11d0fa227ccd8f555dc15746ff5b1ed7b006f59ed7374a185cc092732`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[11].body[4].body[3].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[3]::Assign

Source: `infra/agentinfra/roadmap.py:192`; AST `6feeebf3aabb48dd53a68c6150a26d1a52d25b0efd64ac3d0cef08856f769ece`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, good, obligation, proof_errors, python_proof_errors, receipt, result_proof, root. Outputs/bindings: good.
Calls/effect boundaries: bindings_current, proof_errors, python_proof_errors.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[4].body[3].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[3].value.values[1].operand::Call

Source: `infra/agentinfra/roadmap.py:192`; AST `ca8748d417dbd6ba566924ee7e893816f955141453fea42fb7073bf4ae12f0f3`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation, proof_errors, result_proof. Outputs/bindings: (none).
Calls/effect boundaries: proof_errors.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[5].body[3].value.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[3].value.values[2].operand::Call

Source: `infra/agentinfra/roadmap.py:193`; AST `8f9d5adbead617cedcbacf1063f0ba92bd790289208a58d79b9a8bd159fab85d`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation, python_proof_errors, result_proof, root. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[5].body[3].value.values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[3].body[5].body[3].value.values[4]::Call

Source: `infra/agentinfra/roadmap.py:195`; AST `fb78ae661c54f9029c088fc64a42f859e92ead477bb59c89e9abc0b7cbe4281b`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, obligation, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[3].body[5].body[3].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[4]::If

Source: `infra/agentinfra/roadmap.py:196`; AST `670f6de5876196a8a965935fded20d34614119423b6cf978430ac63a8e455909`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: accepted, candidates, good, receipt, rejected. Outputs/bindings: (none).
Calls/effect boundaries: accepted.append, candidates.add, rejected.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[11].body[4].body[4]; no call, error or mutation may be omitted. Condition: good
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:197`; AST `ee76d98ab7e3bbba2657b7cb3d7d587888918d28366dfc9fd60fd91e41f8f723`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: accepted, receipt. Outputs/bindings: (none).
Calls/effect boundaries: accepted.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[11].body[4].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:197`; AST `728dc00f9b8f1820002c112587c82f9d96a9fa4431f6c1f00b058a0b95d93d85`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: accepted, receipt. Outputs/bindings: (none).
Calls/effect boundaries: accepted.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[4].body[1]::Expr

Source: `infra/agentinfra/roadmap.py:198`; AST `2ca7c16d5fc24ce72c7442b3d434cd8f08cec591cec5d2f4908a1fc5441f3def`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidates, receipt. Outputs/bindings: (none).
Calls/effect boundaries: candidates.add.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[11].body[4].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:198`; AST `14a4eabf30f39f8fddc284d1a700ee425ddaea60c4c59d0c3717b495ffeb1bd0`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidates, receipt. Outputs/bindings: (none).
Calls/effect boundaries: candidates.add.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[4].orelse[0]::Expr

Source: `infra/agentinfra/roadmap.py:200`; AST `f347006d8bafac26f90fd1c0c0a0d803f3704e4ce94a2dd0f2a56d88c9b3b81d`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, rejected. Outputs/bindings: (none).
Calls/effect boundaries: rejected.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[11].body[4].body[4].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[4].body[4].orelse[0].value::Call

Source: `infra/agentinfra/roadmap.py:200`; AST `77d7e8050ad9366296432db4d4149b98114239667ec2d6b5786f7e5962c04860`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, rejected. Outputs/bindings: (none).
Calls/effect boundaries: rejected.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[4].body[4].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[5]::Assign

Source: `infra/agentinfra/roadmap.py:201`; AST `d5b315d55d70eaa37121ffa7b5619bbdc754d0973a9903d8209a63b171aa6e8f`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: accepted, contract, set, sorted. Outputs/bindings: missing.
Calls/effect boundaries: set, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[5].value::Call

Source: `infra/agentinfra/roadmap.py:201`; AST `2b96a554f0bd3b6cf11f4234a439810de2a11d523eebc9d0efade984a9d8b30c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: accepted, contract, set, sorted. Outputs/bindings: (none).
Calls/effect boundaries: set, sorted.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[5].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:201`; AST `667b0281782ac167fc2e5367fc5549364a09446c91c8958b05f7cd1b838bb333`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[5].value.args[0].right::Call

Source: `infra/agentinfra/roadmap.py:201`; AST `ae9d79a63249e0e675299892f8ea9e26593b5f98aa7140c36fbe5facb2c188bf`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: accepted, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[5].value.args[0].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[6]::Assign

Source: `infra/agentinfra/roadmap.py:202`; AST `191551da83baf23bb9cf8d7496e6da93ce01084008457d54f485a8426ab13a93`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract, d, result. Outputs/bindings: d, dependencies.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[6].value::ListComp

Source: `infra/agentinfra/roadmap.py:202`; AST `7ad556fb4b221e50286b0be66ca4c429291c2918cc6e17250188a96df98eea01`.

Rust module: `infra::agentinfra::roadmap`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: contract, d, result. Outputs/bindings: d.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[13].body[11].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[7]::If

Source: `infra/agentinfra/roadmap.py:203`; AST `73652496f19951e91832674a6e7e40312c30f0637ea132801dc0be176c2ccc75`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: candidates, len, missing. Outputs/bindings: (none).
Calls/effect boundaries: len, missing.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[11].body[7]; no call, error or mutation may be omitted. Condition: len(candidates) > 1
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[7].test.left::Call

Source: `infra/agentinfra/roadmap.py:203`; AST `9426902e357b3e5024d3c0d03052392aad689ad588b74440859346f8aaac663c`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidates, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[7].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:204`; AST `0b0cda2bed370cf222abafe9bee552d14fb6e9febeec788f23a1152343b19539`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: missing. Outputs/bindings: (none).
Calls/effect boundaries: missing.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[11].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:204`; AST `1417a2946ce30907c13b5fb0558480b4718cecc5afec76831bb8ed353fee519a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: missing. Outputs/bindings: (none).
Calls/effect boundaries: missing.append.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[8]::If

Source: `infra/agentinfra/roadmap.py:205`; AST `c1cf558849b07fa91120b2d2a9d629baf26b57ece695bf9cac616689c210b1d6`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dependencies, missing. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[13].body[11].body[8]; no call, error or mutation may be omitted. Condition: missing or dependencies
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[8].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:206`; AST `f62db6db6029f3af80834de0749e5189047f81a6c4fbaaa62b7b5f8bbebc4f86`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[8].orelse[0]::Assign

Source: `infra/agentinfra/roadmap.py:208`; AST `2da18a79c8abf709fbdcfc6c7b9b192a6a9cc7347e80d83b08239c5bdb558607`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[8].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[11].body[9]::Assign

Source: `infra/agentinfra/roadmap.py:209`; AST `59cd0f49aadc7ee4b6f1d21dea1bb90f041596a690daacb62161a17b464b2d95`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies, ident, missing, rejected, result, state. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::audit_evidence::root.body[13].body[12]::Return

Source: `infra/agentinfra/roadmap.py:211`; AST `b4927875bad39a33ba922bb9a13e4335478820dc5e4958e30e8a4d584c519782`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[13].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap.py:215`; AST `867cf7d989ee13a18513b147a34ba6dae5a34116c7d2909fd723d563c01d45f6`.

Rust module: `infra::agentinfra::roadmap`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: audit, canonical, compiled, contract, dict, digest, ident, int, len, max_bytes, require, str, type, work. Outputs/bindings: contract, work.
Calls/effect boundaries: canonical, digest, len, require, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[0]::Expr

Source: `infra/agentinfra/roadmap.py:216`; AST `e3ecf5adf64340ba497200b4aed058a36e427b7b948b3af308a7588ebba104c5`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:216`; AST `9e198ebc6d92ddca6b100ce84976f4c9314da319c04b6fb8460232be60354290`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[1]::Expr

Source: `infra/agentinfra/roadmap.py:217`; AST `32fe43ca0cd7fa0bbcf4c7bcf2be8ed011c76c3cad0977799ae9bfb24c8cb989`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, max_bytes, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:217`; AST `b26a022b005005fb5503399e34590dd2364434ad1a815e79577082d0e8d4199f`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, max_bytes, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap.py:217`; AST `c99ed4947b38c030b13015cab080bcc1db01a4478b079df565678d930d284956`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: max_bytes, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[2]::Expr

Source: `infra/agentinfra/roadmap.py:218`; AST `1b2e966a0413ddc4e801fffb37319b4dbd02f8fe25fb2a00ece49f927110be4a`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit, compiled, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:218`; AST `a2a2e810da5fc59cdd5ef76f26d998fe239bd491270a9e6a3e2e305dbde9d9fb`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: audit, compiled, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[3]::Assign

Source: `infra/agentinfra/roadmap.py:219`; AST `3274c77af5359007d2f8bc496a87be7437eb15d49a0bc0b11aae356556b2afcb`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, ident. Outputs/bindings: contract.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[4]::Assign

Source: `infra/agentinfra/roadmap.py:220`; AST `2d8cfd0e26e5029aad29ee3b70194ec071b138fcb2b9ec4dc677ad928fedb24c`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit, compiled, contract, digest, ident. Outputs/bindings: work.
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[4].value.values[1]::Call

Source: `infra/agentinfra/roadmap.py:220`; AST `ab8c82f092253a6ac285d0a5ea2feea96b49def1854b2fa28f28fc221655dfba`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, digest, ident. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[5]::Expr

Source: `infra/agentinfra/roadmap.py:223`; AST `720a78483778845532349110ad8d5a2ad3d3411bda09ef826d032db4f68e7d6e`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, len, max_bytes, require, work. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[5].value::Call

Source: `infra/agentinfra/roadmap.py:223`; AST `8a20bd55e5755c84dacfad9b87adc9c09a2c069d2020f18226f1c22e1216e124`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len, max_bytes, require, work. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[5].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:223`; AST `16aeaff010804f092f7a6e46fb11f14dc5a8b6e491a971ab17bf06dd80a3feab`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len, work. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[5].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap.py:223`; AST `631ffb163234f466c95d4740a96863b32bf0e0890f8f14e71eadfb97f1b357ce`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, work. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::packet::root.body[14].body[6]::Return

Source: `infra/agentinfra/roadmap.py:224`; AST `17f3cf8fc6ad1f5a68e728b74dae935fa253163a06b139c09a0593fe0350cc87`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: work. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15]::FunctionDef

Source: `infra/agentinfra/roadmap.py:227`; AST `21804a9eb0776efcced09b127836a194c90f7d2cab7169bc702cb30df4b39ee4`.

Rust module: `infra::agentinfra::roadmap`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, Mutation, Path, ProjectAdapter, audit, canonical, confined_path, dict, digest, expected_digest, isinstance, loads, path, raw, read_json, record, registry, registry_path, relative, require, root, str, updated. Outputs/bindings: path, raw, record, registry, registry_path, updated.
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(path, canonical(updated) + b'\n', expected_sha256=expected_digest)], state_dir=root / '.aegis/state/transactions', name='roadmap-projection').commit, Mutation, ProjectAdapter, ProjectAdapter(root, profiles=registry['projects']).update, canonical, confined_path, dict, digest, isinstance, loads, path.read_bytes, raw.decode, read_json, registry_path.exists, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:228`; AST `e46824fd830d49aa0997b5da19da993dd7e9cb85a0ba53ccab360b6a9a0037b9`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, relative, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[0].value::Call

Source: `infra/agentinfra/roadmap.py:228`; AST `63c9acf4cfde20a50eacc658154bbb4ec3954f19236b82666a93c852e8d25e5a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[1]::Assign

Source: `infra/agentinfra/roadmap.py:229`; AST `cb5aaaf42a08c91666ce0e4859112cf066cdeebf56910b462a58b24332914278`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: raw.
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:229`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[2]::Expr

Source: `infra/agentinfra/roadmap.py:230`; AST `7a1f5c3d1d90fc2916c5df884e628537d0afd760f79345f06756a88ef4058642`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, expected_digest, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[2].value::Call

Source: `infra/agentinfra/roadmap.py:230`; AST `230fe3a306e6e36673ba0e0194486b0bb99b461f1aadf95a729f5c9fe0221eff`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, expected_digest, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap.py:230`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[3]::Assign

Source: `infra/agentinfra/roadmap.py:231`; AST `1a7caabea4334daf42677c8266724166b02ad867b1e9a036ef5bd6a5104aec68`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: loads, raw. Outputs/bindings: record.
Calls/effect boundaries: loads, raw.decode.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[3].value::Call

Source: `infra/agentinfra/roadmap.py:231`; AST `3cd9d6689794920e55f390bde47f66ddf243c378516a5469daece740a88f9b01`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: loads, raw. Outputs/bindings: (none).
Calls/effect boundaries: loads, raw.decode.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap.py:231`; AST `7e5976c358f689cbba4847a37b23914e4dfb23dfd1a0d1c4648c224ea0e5dc22`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.decode.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[4]::Expr

Source: `infra/agentinfra/roadmap.py:232`; AST `aabf535c8abca8d5d98bb469a42757f683fb5091cff6ad4864c162af67bcfedf`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, isinstance, record, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[4].value::Call

Source: `infra/agentinfra/roadmap.py:232`; AST `546651c4a8dd9d3488441abc7cc2d788c6f6b013d1c5bf492d88521cc7298a83`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, record, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap.py:232`; AST `c1638e93b515785b3f31d5067c2fdc6324d1520c3d7614e7a0790bbe77a30e77`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, record. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[5]::Assign

Source: `infra/agentinfra/roadmap.py:233`; AST `6c6398067ecfac429edb3e05b95490aff08467495994df9e5b6460a57a785012`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: registry_path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[6]::Assign

Source: `infra/agentinfra/roadmap.py:234`; AST `bec2afbc1dbd4c438ba30e8136e52924d3182cf099094dcc170c192bad859e4d`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, registry_path. Outputs/bindings: registry.
Calls/effect boundaries: read_json, registry_path.exists.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[6].value.test::Call

Source: `infra/agentinfra/roadmap.py:234`; AST `b1622850fd06bbc2d9dc1c35aab393c51e51ef0ec6dfe4839df51c11c9f2d604`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: registry_path. Outputs/bindings: (none).
Calls/effect boundaries: registry_path.exists.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[6].value.body::Call

Source: `infra/agentinfra/roadmap.py:234`; AST `7193deef5dc52d03fdd6795bb006e4b1afb5634d3e47a2203ea12bc39d31affa`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, registry_path. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[7]::If

Source: `infra/agentinfra/roadmap.py:235`; AST `0106ccde7acee29f1f73eb64e9243eece543ece1745578487c3ad5c7cb1994f7`.

Rust module: `infra::agentinfra::roadmap`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ProjectAdapter, audit, confined_path, expected_digest, path, registry, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root, profiles=registry['projects']).update, confined_path.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[15].body[7]; no call, error or mutation may be omitted. Condition: registry and path == confined_path(root, registry['projects']['Aegis']['canonical_record'])
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[7].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap.py:235`; AST `6f5194fa2144b51492f727b5189670703447764512d5872079b0c036512173bb`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, registry, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[7].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap.py:236`; AST `06018155a23f1f83c82d139847669324993143354a3dd3b3aaf896059cf1187a`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[7].body[1]::Return

Source: `infra/agentinfra/roadmap.py:237`; AST `b15f4e5235d100364e9a152d9a10cce4fe980916abecd51d16112544cb8c43bb`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectAdapter, audit, expected_digest, registry, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root, profiles=registry['projects']).update.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[15].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[7].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:237`; AST `7175525e140aceaf4e9988adbb2739b130a4b38f9c0fb0462a9f951f0a6e98f2`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, audit, expected_digest, registry, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter, ProjectAdapter(root, profiles=registry['projects']).update.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[7].body[1].value.func.value::Call

Source: `infra/agentinfra/roadmap.py:237`; AST `1d9e839d5392c1b2bae35d82259a28ec9d25ca50b4e55dedc677648509dc31e8`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, registry, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[8]::Assign

Source: `infra/agentinfra/roadmap.py:239`; AST `b01b7e304a80eb4a531c88daf27f556db585de3bf6bcf64a82f7c34a4924bd6f`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: audit, dict, record. Outputs/bindings: updated.
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[8].value::Call

Source: `infra/agentinfra/roadmap.py:239`; AST `db288ea7c8ea41ee39f7b40fac7f79af75f7d39badd2d3f7e4f3b894b69d6c04`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: audit, dict, record. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[9]::Return

Source: `infra/agentinfra/roadmap.py:240`; AST `61713c720676d06952a67a9356bac7c03ba2537f9af2a647dbe740a973e45d80`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, Mutation, canonical, expected_digest, path, root, updated. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(path, canonical(updated) + b'\n', expected_sha256=expected_digest)], state_dir=root / '.aegis/state/transactions', name='roadmap-projection').commit, Mutation, canonical.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[15].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[9].value::Call

Source: `infra/agentinfra/roadmap.py:240`; AST `4bcb3c27b2420156684fe55450b3edbcaded7926ee945be7adae1a772d742cbf`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, canonical, expected_digest, path, root, updated. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(root, [Mutation(path, canonical(updated) + b'\n', expected_sha256=expected_digest)], state_dir=root / '.aegis/state/transactions', name='roadmap-projection').commit, Mutation, canonical.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[9].value.func.value::Call

Source: `infra/agentinfra/roadmap.py:240`; AST `754763462a376d0181dcb18a3ed798d5e4d91d62af7e0d940cdb532f0d833fb9`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, Mutation, canonical, expected_digest, path, root, updated. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation, canonical.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[9].value.func.value.args[1].elts[0]::Call

Source: `infra/agentinfra/roadmap.py:240`; AST `ff97c09b3f4969467208b075f107207fb14391a19b30ed40062427e760336216`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, canonical, expected_digest, path, updated. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, canonical.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::project_into_record::root.body[15].body[9].value.func.value.args[1].elts[0].args[1].left::Call

Source: `infra/agentinfra/roadmap.py:240`; AST `55c97ce00fe8675ff74e1eed48ded4cd22b3be31d967e0ab26715026d67f484e`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, updated. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].value.func.value.args[1].elts[0].args[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::save_compiled::root.body[16]::FunctionDef

Source: `infra/agentinfra/roadmap.py:244`; AST `410ef4d2f84293b09a5c855d8337473f265b466cda80c1a6dc8163a0c7d5021f`.

Rust module: `infra::agentinfra::roadmap`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, atomic_write_json, compiled, dict, path, root. Outputs/bindings: path.
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::save_compiled::root.body[16].body[0]::Assign

Source: `infra/agentinfra/roadmap.py:245`; AST `83e1f91fc11cb9a36f1e3a80bb903eb6defec1b85c5384d90904727bf6984d53`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::save_compiled::root.body[16].body[1]::Expr

Source: `infra/agentinfra/roadmap.py:246`; AST `48c3c778fb98e175b53200a53c668afb3fb70889b8fc08fe346b91b58e6e62de`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, compiled, path, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::save_compiled::root.body[16].body[1].value::Call

Source: `infra/agentinfra/roadmap.py:246`; AST `3cd5dcb28a38db4ad27ca53c4ad6a5eaeba1c1d5397a7635f73bca2b94d8df2e`.

Rust module: `infra::agentinfra::roadmap`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, compiled, path, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap.py::module::save_compiled::root.body[16].body[2]::Return

Source: `infra/agentinfra/roadmap.py:247`; AST `6a83e41742422cefd09401a733b9520de25fdaca4b583a6ac2a8659697bf9fee`.

Rust module: `infra::agentinfra::roadmap`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, pathlib, re, roadmap_policy, roadmap_project, roadmap_python, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
