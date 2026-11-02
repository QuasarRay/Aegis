# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 416. Inventory digest: `890725b44968fb2878de42e82218718710be28c96bf8504e795b35f64e805945`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_inventory.py::module::root::Module

Source: `infra/agentinfra/roadmap_inventory.py:1`; AST `843d20dc4988b4dc5bbdadcb0bf3d984e7f9e96fce4ec7833388d910d6c6d849`.

Rust module: `infra::agentinfra::roadmap_inventory`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: GitInventory, Mutation, Path, ProjectAdapter, SyntaxError, UnicodeError, ValueError, adapter, all, any, arguments, ast, authority_inventory, before, binding, blob, bool, branch, bytes, c, canonical, child, commit, compile, compile_roadmaps, compiled, components, confined_path, current, current_blobs, deadline, definitions, dict, digest, dirty_only, e, entries, entry, enumerate, exc, field, file, filename, files, filter, float, getattr, git, h, head_tree, header, heads, index, inspect_python, isinstance, item, k, kind, len, line, list, loads, min, minimal_subprocess_env, missing, mode, name, names, nested, node, oid, os, output, owner, p, path, r, raw, read_json, record, refs, relative, remaining, remote, require, result, root, route, run_process, s, selected, self, set, shutil, snapshot, sorted, stage, staged, stat, str, subprocess, sys, tempfile, text, time, tree, tree_id, trees, type, untracked, v, value, visit, working_components, worktree. Outputs/bindings: adapter, before, binding, blob, branch, c, child, commit, compiled, components, current, current_blobs, definitions, e, entries, entry, field, file, files, git, h, head_tree, header, heads, index, item, k, kind, line, missing, mode, name, names, nested, oid, output, owner, p, path, r, raw, record, refs, relative, remaining, result, root, s, selected, snapshot, stage, staged, text, tree, tree_id, trees, untracked, v, value, working_components, worktree.
Calls/effect boundaries: (path / '.git').exists, GitInventory, Mutation, Path, Path(git.executable).read_bytes, Path(sys.executable).read_bytes, ProjectAdapter, adapter.profile.path, adapter.update, all, any, ast.dump, ast.dump(node, include_attributes=False).encode, ast.dump(tree, include_attributes=False).encode, ast.iter_fields, ast.parse, authority_inventory, before.decode, bool, canonical, compile, compile_roadmaps, components.values, confined_path, confined_path(root, file['path'], must_exist=True).read_bytes, current.get, current_blobs.get, definitions.append, digest, entries.append, entry.update, entry['path'].endswith, enumerate, file['path'].endswith, files.append, filter, getattr, git.blob, git.read, git.read('--version').strip, git.read('rev-parse', 'HEAD^{tree}').strip, git.refs, git.remote_heads, git.tree, git.worktree, h['ref'].removeprefix, header.split, inspect_python, isinstance, item.split, item['paths'].append, item['paths'].sort, item['trees'].append, item['trees'].sort, len, line.split, loads, min, minimal_subprocess_env, nested.worktree, os.fsencode, os.readlink, output.read, output.seek, output.tell, path.exists, path.is_dir, path.is_file, path.is_symlink, path.read_bytes, path.stat, read_json, record.get, record.items, refs.append, require, result.stdout.encode, root.resolve, run_process, selected.update, self.read, self.read('diff', '--cached', '--name-only', '--no-renames', '-z', 'HEAD').split, self.read('diff', '--name-only', '--no-renames', '-z', 'HEAD').split, self.read('ls-files', '--others', '--exclude-standard', '-z').split, self.read('ls-files', '--stage', '-z').split, self.read('ls-remote', '--heads', 'origin').splitlines, self.read('ls-tree', '-rz', '--full-tree', oid).split, self.read('rev-parse', '--abbrev-ref', 'HEAD').strip, self.read('rev-parse', 'HEAD').strip, set, shutil.which, snapshot.exists, snapshot.read_bytes, sorted, staged.get, staged.setdefault, staged.setdefault(name, []).append, str, subprocess.run, tempfile.TemporaryFile, text.splitlines, time.monotonic, trees.items, type, visit, working_components.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:1`; AST `f1b8d9c4066d8dbaed62560a5e8f453fa871ea692acbb80eb9bf817d00f3e3f7`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_inventory.py:7`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_inventory.py:9`; AST `bb134ca6c8f43358b0a04f3db40a8957242456961f7c0823aff7ae7a2647bf15`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_inventory.py:10`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_inventory.py:11`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[5]::Import

Source: `infra/agentinfra/roadmap_inventory.py:12`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[6]::Import

Source: `infra/agentinfra/roadmap_inventory.py:13`; AST `c22b5a111acc3bea9e5136e41e207f1f95083e90d861516ce34d682526721c86`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[7]::Import

Source: `infra/agentinfra/roadmap_inventory.py:14`; AST `9d97d469cf8d66465563e1e22c6dab3b6107819aba2d9956c7080016c1ab9c1b`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[8]::Import

Source: `infra/agentinfra/roadmap_inventory.py:15`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[9]::Import

Source: `infra/agentinfra/roadmap_inventory.py:16`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Import evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[10]::Import

Source: `infra/agentinfra/roadmap_inventory.py:17`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Import evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[11]::ImportFrom

Source: `infra/agentinfra/roadmap_inventory.py:19`; AST `cb4b66aa2a9ba9861af7c0b11d312d64af950034a4b89ff32a7fb710e139fffa`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[12]::ImportFrom

Source: `infra/agentinfra/roadmap_inventory.py:20`; AST `516ad522e1b0b153169e0b1e71e6a8b00eec932ec90b5f5c19c35c6062e8bd70`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[13]::ImportFrom

Source: `infra/agentinfra/roadmap_inventory.py:21`; AST `0f6811ca7e77075aa63ceefe7760ce6466de2bb1d53861e9d4247ab45a18a14d`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[14]::ImportFrom

Source: `infra/agentinfra/roadmap_inventory.py:22`; AST `06018155a23f1f83c82d139847669324993143354a3dd3b3aaf896059cf1187a`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[15]::ImportFrom

Source: `infra/agentinfra/roadmap_inventory.py:23`; AST `671c47b9d53095e5ce83f482c65164d9792d075af126956be31bf51da2fdf7ff`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::root.body[16]::ImportFrom

Source: `infra/agentinfra/roadmap_inventory.py:24`; AST `09ff97639465e5a0875c5025b5945bcd88cea889d6db709a2af9f247fcbdc70f`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::root.body[17]::ClassDef

Source: `infra/agentinfra/roadmap_inventory.py:27`; AST `ac938b08fffc81b1e3c1be6a972810f0ae5247ef0f1c3ff4467e6feb7dab7843`.

Rust module: `infra::agentinfra::roadmap_inventory`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: GitInventory, Path, all, any, arguments, blob, bool, branch, bytes, c, commit, confined_path, deadline, dict, digest, dirty_only, entries, entry, files, filter, float, header, item, kind, len, line, list, min, minimal_subprocess_env, mode, name, names, nested, oid, os, output, path, refs, remaining, require, result, root, run_process, s, selected, self, set, shutil, sorted, stage, staged, stat, str, subprocess, tempfile, text, time, tree, untracked. Outputs/bindings: blob, branch, c, commit, entries, entry, files, header, item, kind, line, mode, name, names, nested, oid, output, path, refs, remaining, result, s, selected, stage, staged, text, tree, untracked.
Calls/effect boundaries: (path / '.git').exists, GitInventory, all, any, bool, confined_path, digest, entries.append, entry.update, files.append, filter, header.split, item.split, len, line.split, min, minimal_subprocess_env, nested.worktree, os.fsencode, os.readlink, output.read, output.seek, output.tell, path.exists, path.is_dir, path.is_file, path.is_symlink, path.read_bytes, path.stat, refs.append, require, result.stdout.encode, root.resolve, run_process, selected.update, self.read, self.read('diff', '--cached', '--name-only', '--no-renames', '-z', 'HEAD').split, self.read('diff', '--name-only', '--no-renames', '-z', 'HEAD').split, self.read('ls-files', '--others', '--exclude-standard', '-z').split, self.read('ls-files', '--stage', '-z').split, self.read('ls-remote', '--heads', 'origin').splitlines, self.read('ls-tree', '-rz', '--full-tree', oid).split, self.read('rev-parse', '--abbrev-ref', 'HEAD').strip, self.read('rev-parse', 'HEAD').strip, set, shutil.which, sorted, staged.get, staged.setdefault, staged.setdefault(name, []).append, subprocess.run, tempfile.TemporaryFile, text.splitlines, time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ClassDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::root.body[17].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:28`; AST `0384f399f4a4396ac5c795e5d786eecf599056fd7d0ca93a7ed82bbc71516dbb`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::__init__::root.body[17].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:30`; AST `88c0398008e71c7d9a90ec042ef7ed5768c3c305c12d6ff795ccd60c3f18444b`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, deadline, float, require, root, self, shutil, time. Outputs/bindings: (none).
Calls/effect boundaries: require, root.resolve, shutil.which, time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::__init__::root.body[17].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:31`; AST `eac70191d36cd330a975a12be514d4a5f58088087cc2acfa2746cafe468cc8ae`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::__init__::root.body[17].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:31`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::__init__::root.body[17].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:32`; AST `31ea3256317d0f017eae08e0b7d18fbfd9a9da3838311ed4657e9b3280f71e23`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, self, time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::__init__::root.body[17].body[1].body[1].value.body.left::Call

Source: `infra/agentinfra/roadmap_inventory.py:32`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[1].value.body.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::__init__::root.body[17].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:33`; AST `2eb72a7a8115a4090cedad46860697333ddd1efcbfaa06e3368588a9bd439f00`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.which.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::__init__::root.body[17].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:33`; AST `e358816b94f36e6c457210e899890720d40a021063589a3a040c4e3e8919c2a8`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.which.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::__init__::root.body[17].body[1].body[3]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:34`; AST `8b99b9b7c1a2ff8ae830cb117b870b9e5ca3cebc633eb42a978911f10739d143`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::__init__::root.body[17].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:34`; AST `9503aea223163230135e0ba2cff71d57452c1c0817b595cf4035a8c627cfe8e9`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:36`; AST `633a46eb3d157638a7fb6d8df042721d76c0aabd745b8f5287f9f8b9a2dcfe4b`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: arguments, digest, min, remaining, require, result, run_process, self, str, time. Outputs/bindings: remaining, result.
Calls/effect boundaries: digest, min, require, result.stdout.encode, run_process, time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:37`; AST `1c6c3d9c41f79ddd67b7e18f233ea9b3b8966cd47080721568299b430d683ae8`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, time. Outputs/bindings: remaining.
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[0].value.right::Call

Source: `infra/agentinfra/roadmap_inventory.py:37`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:38`; AST `95bdfd302d43404163f3dadd8b47144aec814b6b359aa0aad21eb2425829b982`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:38`; AST `e6f1f51af1b3481319d8815f1d4e285a686086633b1785ceb262e0a7f40c72e0`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[2]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:39`; AST `2b38cb0eb6dba5e1d2bd36e37332d93a030717f32fb03e5ddbd6d3774a27e05a`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: arguments, min, remaining, run_process, self. Outputs/bindings: result.
Calls/effect boundaries: min, run_process.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:39`; AST `bd77d20042fb18ca8e256e2abbccc63af599aa2f4384a31823ef2785d53a8060`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: arguments, min, remaining, run_process, self. Outputs/bindings: (none).
Calls/effect boundaries: min, run_process.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[2].value.keywords[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:40`; AST `c91e42bb5f35ce8a2ee3671de913e74f8fd555fa1a8b54c654894209b419a332`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: min, remaining. Outputs/bindings: (none).
Calls/effect boundaries: min.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[2].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[3]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:41`; AST `70e48f414747a3909e13d40261827337a8a4295ea8cc404a68344521120c7062`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: arguments, require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[3].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:41`; AST `40e84cfb6c379648689970b256a7eae9bb4e1f871f26d14139b0f6e9315a30e3`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: arguments, require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[4]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:45`; AST `610b2bf8ea5547988a1cd7865f6f22a4fadc8c92487618ab8a9c22cc2ad6d6a0`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, require, result. Outputs/bindings: (none).
Calls/effect boundaries: digest, require, result.stdout.encode.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[4].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:45`; AST `d8bf9a42a2e343c96b5b71c87160caa04feb0d4eef050de6f443a615d33b6e73`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, require, result. Outputs/bindings: (none).
Calls/effect boundaries: digest, require, result.stdout.encode.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:45`; AST `5b10d593178b8e1f91431cdc11541f883e7d6f0628159b735118fd6473555569`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, result. Outputs/bindings: (none).
Calls/effect boundaries: digest, result.stdout.encode.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[4].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:45`; AST `0f2a6f719da67c08ca5df035db5a156a5300b897c06161c887c4813298a718b5`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.stdout.encode.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[4].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::read::root.body[17].body[2].body[5]::Return

Source: `infra/agentinfra/roadmap_inventory.py:47`; AST `f128f8a967f413784ea20e8a109d2122795a6618ca3f2e4503c5e2fcd966d370`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[17].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:49`; AST `a06d88f4c66079100a0fd1737edbd53c7d5f37d07bbc1f6ab6de22a9d5b0bda9`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, bytes, c, len, min, minimal_subprocess_env, oid, output, remaining, require, result, self, str, subprocess, tempfile, time. Outputs/bindings: c, output, remaining, result.
Calls/effect boundaries: all, len, min, minimal_subprocess_env, output.read, output.seek, output.tell, require, subprocess.run, tempfile.TemporaryFile, time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:50`; AST `9300503ec9c47cd89b5aedc4bc4d046188d064cb0cfdfdc194a7018bb579a2b2`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, c, len, oid, require. Outputs/bindings: c.
Calls/effect boundaries: all, len, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:50`; AST `6a3f5eaa0fe7ddc80d165729afee9d03e2b951217cadce801196aecb20e31c94`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, len, oid, require. Outputs/bindings: c.
Calls/effect boundaries: all, len, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:50`; AST `9167f9c03ed156cd976871cc5afdbbe75fa8daf8456a05b8a714784b7dc9cec1`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, oid. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:50`; AST `6efd67bf86c48eee2b4fbf87e96fbace6810e1a993fe14eaaa23a3f3f54d5751`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, oid. Outputs/bindings: c.
Calls/effect boundaries: all.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[0].value.args[0].values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_inventory.py:50`; AST `2cdc071ea7d136894589957c654254ab25090c20c6f22f53d6398033328d259e`.

Rust module: `infra::agentinfra::roadmap_inventory`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, oid. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[3].body[0].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1]::With

Source: `infra/agentinfra/roadmap_inventory.py:54`; AST `fe420d137494b19f4a726ca92e7ea296e8b719acc1f0068fcfea4f7315f03058`.

Rust module: `infra::agentinfra::roadmap_inventory`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: min, minimal_subprocess_env, oid, output, remaining, require, result, self, subprocess, tempfile, time. Outputs/bindings: output, remaining, result.
Calls/effect boundaries: min, minimal_subprocess_env, output.read, output.seek, output.tell, require, subprocess.run, tempfile.TemporaryFile, time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered With evaluation at root.body[17].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_inventory.py:54`; AST `8efcbb7bc31f88cdf33f4f01fad96bba261f7fc49d84d6135d920fc61517442a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryFile.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:55`; AST `1c6c3d9c41f79ddd67b7e18f233ea9b3b8966cd47080721568299b430d683ae8`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, time. Outputs/bindings: remaining.
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[0].value.right::Call

Source: `infra/agentinfra/roadmap_inventory.py:55`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[1]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:56`; AST `95bdfd302d43404163f3dadd8b47144aec814b6b359aa0aad21eb2425829b982`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:56`; AST `e6f1f51af1b3481319d8815f1d4e285a686086633b1785ceb262e0a7f40c72e0`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:57`; AST `4ca47e059995ff3c1d18ea3967aeff80dcd359fea262842fc8b9c6cbe155164a`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: min, minimal_subprocess_env, oid, output, remaining, self, subprocess. Outputs/bindings: result.
Calls/effect boundaries: min, minimal_subprocess_env, subprocess.run.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:57`; AST `f52ddf62e11d2b566123cf21e9e7bf1b628f126acb17b294e1fb11e752dcd66b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: min, minimal_subprocess_env, oid, output, remaining, self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: min, minimal_subprocess_env, subprocess.run.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[2].value.keywords[3].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:59`; AST `c91e42bb5f35ce8a2ee3671de913e74f8fd555fa1a8b54c654894209b419a332`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: min, remaining. Outputs/bindings: (none).
Calls/effect boundaries: min.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[2].value.keywords[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[2].value.keywords[4].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:59`; AST `9e9061036bd9e328e720270b436538e3d5500df22e91a0d49a0d1cd8cd8d5695`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: minimal_subprocess_env. Outputs/bindings: (none).
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[2].value.keywords[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[3]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:60`; AST `f3e166538b1d668f26b097ee676c9e8c2d7de358a896fa5e446b2cf70ccef4f7`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:60`; AST `71007d45df9a3ed7ea528928ddf2022a8de8a69db2a7893730e627927175014b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[4]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:61`; AST `1bf9894c4168acfd38d27be1964b4931da8ad282569af28a2d26f360c662a7c8`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output, require. Outputs/bindings: (none).
Calls/effect boundaries: output.tell, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[4].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:61`; AST `edf00d8793c6c499f8be2d85b9cc1b85ad3eceb20e5445ee041d17cd7d088fe0`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, require. Outputs/bindings: (none).
Calls/effect boundaries: output.tell, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:61`; AST `f18a8ab6f962b252da03499fd18f10ac2f71a13338210dfeac115599914e4ee7`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.tell.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[5]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:62`; AST `146b91738aa757261dfe6780a06fdd52062837157b85ccdad69f367499d097fa`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.seek.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[5].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:62`; AST `43152eafcb8dd72f3771ef6effead2fe6b389989554cf60cdc660a8592f42ffd`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.seek.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[6]::Return

Source: `infra/agentinfra/roadmap_inventory.py:63`; AST `5a6f488417becf270d74b12ed19aa91c154dbd8fb22bee9c49ce591e0bfb67db`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[17].body[3].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::blob::root.body[17].body[3].body[1].body[6].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:63`; AST `7a2fced922787f726c41bc7141e0414f268fe9e347bfb8c1ef50fbbee8802d02`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:65`; AST `4e11016603e02dcfd6d073ceb280a3367777dd35dece05901379dd914e711ee8`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bool, commit, dict, line, list, name, refs, require, self, text, tree. Outputs/bindings: commit, line, name, refs, text, tree.
Calls/effect boundaries: bool, line.split, refs.append, require, self.read, text.splitlines.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:66`; AST `7ef1258cc809d8dad18081841f504a13dbd9a9b554e7d10c435c8850448a922e`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: text.
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:66`; AST `496fa59108f759f446036e6cd7312763907653e2cb867876636b4486bd6d76b8`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:68`; AST `dd7b74389e668ab5d30f8573848ba2c8494ad6d4c7a3d2f4b7d62a841ced7a8b`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: refs.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[2]::For

Source: `infra/agentinfra/roadmap_inventory.py:69`; AST `a061a9e2f723312f5d7b6978b311726010bfbe325c9b4b19aad90f20477c04ed`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: bool, commit, line, name, refs, require, text, tree. Outputs/bindings: commit, line, name, tree.
Calls/effect boundaries: bool, line.split, refs.append, require, text.splitlines.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[17].body[4].body[2]; no call, error or mutation may be omitted. Iteration: line in text.splitlines()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[2].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:69`; AST `bda3ac3a2925504d5011edd2471f37355dc82ad5408131d0219f6728a1cad638`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: text.splitlines.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:70`; AST `bfc1a64a8b6aeb7cae50c1579938088bc0dd682c7d56b5701be5e1d32a40283f`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: line. Outputs/bindings: commit, name, tree.
Calls/effect boundaries: line.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:70`; AST `0de13a85339b15a72d19790179048595d150e9e7459d0a265f5ab544c79f0968`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: line. Outputs/bindings: (none).
Calls/effect boundaries: line.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:71`; AST `ce64d9b03727a5c57c2a89d8746f3603e2b9202d866d23ab882f86948a583df8`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, name, require, tree. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:71`; AST `d1fb42821f9fb643f4691af435082b35c7a3b397c940e3c4797fcb2a426fdc5c`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, name, require, tree. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[2].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:71`; AST `fc0736af6a5df6f8d77126e5571ad52b5e51f362773be55dfcd9dc39aaf62838`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, tree. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[2].body[2]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:72`; AST `409ea3207e473c8dd441f59480093c5a9e13f96deec94ed9843c247f69a3cbaf`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: commit, name, refs, tree. Outputs/bindings: (none).
Calls/effect boundaries: refs.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:72`; AST `a8127e0bb00fca9fabb6eef68d677fbfa246eba383ddef32015a740016df46fc`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: commit, name, refs, tree. Outputs/bindings: (none).
Calls/effect boundaries: refs.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[3]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:73`; AST `4ca4e5d9f001b53ff1c5e50906c39a24405377b72e266a1a0be71c76325f475f`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, refs, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[3].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:73`; AST `f2fa5930025fa66e3b2af4769d7799b95277a8c38c52de6478ace025b58220fc`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, refs, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:73`; AST `75b510baf91576ae970b5b31d0b94bbd2c469dd34c4ca52eb825c880ce5d929a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, refs. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::refs::root.body[17].body[4].body[4]::Return

Source: `infra/agentinfra/roadmap_inventory.py:74`; AST `21bf1985239d0a4532aa006fab75d2ff3543d862f640d8f470de733266df3412`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: refs. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[17].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:76`; AST `593b74c456e23f94fcae799d624886129a4f2ae86bd059abab971fcba4428b93`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: blob, dict, entries, header, item, kind, list, mode, oid, path, self, str. Outputs/bindings: blob, entries, header, item, kind, mode, path.
Calls/effect boundaries: entries.append, header.split, item.split, self.read, self.read('ls-tree', '-rz', '--full-tree', oid).split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:77`; AST `ec3f86f08a81f7b97437221ea42b199a5f65a46b6786febd426f3d97d4202618`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: entries.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1]::For

Source: `infra/agentinfra/roadmap_inventory.py:78`; AST `f53220605bdec57340680445dd5dfd4bb0e9c9d7a69d4c4438be879985779375`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: blob, entries, header, item, kind, mode, oid, path, self. Outputs/bindings: blob, header, item, kind, mode, path.
Calls/effect boundaries: entries.append, header.split, item.split, self.read, self.read('ls-tree', '-rz', '--full-tree', oid).split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[17].body[5].body[1]; no call, error or mutation may be omitted. Iteration: item in self.read('ls-tree', '-rz', '--full-tree', oid).split('\x00')
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:78`; AST `0368e612da3ed0b57b34e619503fea7c2975b8f6d3216e44fb82a34a34a73fb2`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: oid, self. Outputs/bindings: (none).
Calls/effect boundaries: self.read, self.read('ls-tree', '-rz', '--full-tree', oid).split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1].iter.func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:78`; AST `b8b6e72b33a6250a0816e5d68c40e83dc90ec568c54b8e824f48e0129339e6f1`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: oid, self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].iter.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:79`; AST `7b757a004c01a05e172f28ddc02583a92446686e4119ce9f1b854f579448345b`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: blob, entries, header, item, kind, mode, path. Outputs/bindings: blob, header, kind, mode, path.
Calls/effect boundaries: entries.append, header.split, item.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[17].body[5].body[1].body[0]; no call, error or mutation may be omitted. Condition: item
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:80`; AST `5c90e6d23d820cf96171e5d33669325976bd294c1bda24a43a1aa96f825ca7ad`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item. Outputs/bindings: header, path.
Calls/effect boundaries: item.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[5].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:80`; AST `19bb54f718cbb52c63f533477056053357924a9f11e167d3be545a86b4d4bf4c`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: item.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:81`; AST `177a119b54f30f88f8cefc89176c4c76b5315aef9bad8896e88f11ea12fad602`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: header. Outputs/bindings: blob, kind, mode.
Calls/effect boundaries: header.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[5].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:81`; AST `e677a70667cc2d5dad3a282665bad2327f43520a9cc61b336762ee787c6eaa96`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: header. Outputs/bindings: (none).
Calls/effect boundaries: header.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1].body[0].body[2]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:82`; AST `e70def7137415482a2370419f3fc2b3147004d46e97bec473317c890eeb7a38a`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: blob, entries, kind, mode, path. Outputs/bindings: (none).
Calls/effect boundaries: entries.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[5].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[1].body[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:82`; AST `0d44b29756d1047ed33d2b3c132cd3a7aa2d00179a298206c0a3bb5c88bc8463`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: blob, entries, kind, mode, path. Outputs/bindings: (none).
Calls/effect boundaries: entries.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::tree::root.body[17].body[5].body[2]::Return

Source: `infra/agentinfra/roadmap_inventory.py:83`; AST `26f3b282d6814e347b4b282e9c249b7c54ae80ecfba4b579fa76142590ce7e98`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entries. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[17].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::remote_heads::root.body[17].body[6]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:85`; AST `fa3a4d25311cae78e0a21d117c6661d94f7f9858b917c3ba1e872f3a20ea0560`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, line, list, self. Outputs/bindings: line.
Calls/effect boundaries: line.split, self.read, self.read('ls-remote', '--heads', 'origin').splitlines.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::remote_heads::root.body[17].body[6].body[0]::Return

Source: `infra/agentinfra/roadmap_inventory.py:86`; AST `600616161d18a3dd3770fd1be142520630913bb6c3d8adfa6c72282ad8456940`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: line, self. Outputs/bindings: line.
Calls/effect boundaries: line.split, self.read, self.read('ls-remote', '--heads', 'origin').splitlines.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[17].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::remote_heads::root.body[17].body[6].body[0].value::ListComp

Source: `infra/agentinfra/roadmap_inventory.py:86`; AST `7d2b0c4d5a8a7c3e045355ee0145d09be7b1497291b5b52d2a97d80bd321d913`.

Rust module: `infra::agentinfra::roadmap_inventory`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: line, self. Outputs/bindings: line.
Calls/effect boundaries: line.split, self.read, self.read('ls-remote', '--heads', 'origin').splitlines.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[17].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::remote_heads::root.body[17].body[6].body[0].value.elt.values[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:86`; AST `de80f93c4c3bfa9ed6b5f1d4aad6f0a544e67a8bb5bd5d3278a8b36e962a9a31`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: line. Outputs/bindings: (none).
Calls/effect boundaries: line.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].value.elt.values[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::remote_heads::root.body[17].body[6].body[0].value.elt.values[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:86`; AST `de80f93c4c3bfa9ed6b5f1d4aad6f0a544e67a8bb5bd5d3278a8b36e962a9a31`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: line. Outputs/bindings: (none).
Calls/effect boundaries: line.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].value.elt.values[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::remote_heads::root.body[17].body[6].body[0].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:87`; AST `37af8eb69595fe506e9671a385f5558af4c745ca1847eea288b67a02845e5c86`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read, self.read('ls-remote', '--heads', 'origin').splitlines.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::remote_heads::root.body[17].body[6].body[0].value.generators[0].iter.func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:87`; AST `2966bb311cb78c791580d72115878193119061436086aae0091dbddfdb6d49e4`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].value.generators[0].iter.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:89`; AST `49368c736d226feca4b96c55c4914c2d2ca38793dab628c64ed99e215288e956`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GitInventory, any, bool, branch, confined_path, dict, digest, dirty_only, entry, files, filter, header, item, mode, name, names, nested, oid, os, path, require, s, selected, self, set, sorted, stage, staged, stat, untracked. Outputs/bindings: branch, entry, files, header, item, mode, name, names, nested, oid, path, s, selected, stage, staged, untracked.
Calls/effect boundaries: (path / '.git').exists, GitInventory, any, bool, confined_path, digest, entry.update, files.append, filter, header.split, item.split, nested.worktree, os.fsencode, os.readlink, path.exists, path.is_dir, path.is_file, path.is_symlink, path.read_bytes, path.stat, require, selected.update, self.read, self.read('diff', '--cached', '--name-only', '--no-renames', '-z', 'HEAD').split, self.read('diff', '--name-only', '--no-renames', '-z', 'HEAD').split, self.read('ls-files', '--others', '--exclude-standard', '-z').split, self.read('ls-files', '--stage', '-z').split, self.read('rev-parse', '--abbrev-ref', 'HEAD').strip, self.read('rev-parse', 'HEAD').strip, set, sorted, staged.get, staged.setdefault, staged.setdefault(name, []).append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:90`; AST `af9fd509dcd3fac8607425ef66d4656f15479760d30d8db5904dff9103410b7c`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: staged.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1]::For

Source: `infra/agentinfra/roadmap_inventory.py:91`; AST `b76642a2c87699f68e5e22c5fbfd9614c24f3f150eaf41a2b900335ae2dc8efd`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: header, item, mode, name, oid, self, stage, staged. Outputs/bindings: header, item, mode, name, oid, stage.
Calls/effect boundaries: header.split, item.split, self.read, self.read('ls-files', '--stage', '-z').split, staged.setdefault, staged.setdefault(name, []).append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[17].body[7].body[1]; no call, error or mutation may be omitted. Iteration: item in self.read('ls-files', '--stage', '-z').split('\x00')
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:91`; AST `cee41dd164a6cd9edd3880dca49dcd4fcf74c446a949bc3a82c6a2dec2a7971e`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read, self.read('ls-files', '--stage', '-z').split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].iter.func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:91`; AST `634bd88ef7f606c9886129dc7c28abdbeaa1502b077c6328f831e85dd50d3595`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[1].iter.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:92`; AST `82202f77fc9041999390e57c2f1e35a07c3a58244d43d567cea022d6b9a3fa7c`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[17].body[7].body[1].body[0]; no call, error or mutation may be omitted. Condition: not item
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].body[0].body[0]::Continue

Source: `infra/agentinfra/roadmap_inventory.py:93`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Continue evaluation at root.body[17].body[7].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:94`; AST `6767e5a758cc110c2e0c6904082c6c214ea6f5ad0fcd33986ea693bb835d9383`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item. Outputs/bindings: header, name.
Calls/effect boundaries: item.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:94`; AST `19bb54f718cbb52c63f533477056053357924a9f11e167d3be545a86b4d4bf4c`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: item.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:95`; AST `586806c8ebd1b48b217ce1912b7e0852033de9c2ae01f9fca33b6c36cfe791e6`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: header. Outputs/bindings: mode, oid, stage.
Calls/effect boundaries: header.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:95`; AST `e677a70667cc2d5dad3a282665bad2327f43520a9cc61b336762ee787c6eaa96`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: header. Outputs/bindings: (none).
Calls/effect boundaries: header.split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].body[3]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:96`; AST `ace1eae42a53f74fbee90a6f3496caca6d695a9bcca2c32cc0d78c8a59db3293`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mode, name, oid, stage, staged. Outputs/bindings: (none).
Calls/effect boundaries: staged.setdefault, staged.setdefault(name, []).append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:96`; AST `ba5c3ee383059d50d22436b89c959c22c4a3d7fffb0b9d2b1af94eddd974c349`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mode, name, oid, stage, staged. Outputs/bindings: (none).
Calls/effect boundaries: staged.setdefault, staged.setdefault(name, []).append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[1].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:96`; AST `957ac1f3ba4d4d5e930de6c18198dbf5c6983bf6056b40559c33c2680b6437ee`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, staged. Outputs/bindings: (none).
Calls/effect boundaries: staged.setdefault.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[1].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[2]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:97`; AST `d4121004a3ea61d3560a0ab7d275bf2b3e097393a033f58de09eec3d940f9bdb`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: filter, self, set. Outputs/bindings: untracked.
Calls/effect boundaries: filter, self.read, self.read('ls-files', '--others', '--exclude-standard', '-z').split, set.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:97`; AST `dc88aec740e14fe8efc4ee0ea0870e5cea851e74b2948e15625a7514a8eaec04`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: filter, self, set. Outputs/bindings: (none).
Calls/effect boundaries: filter, self.read, self.read('ls-files', '--others', '--exclude-standard', '-z').split, set.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:97`; AST `ce179636ebc0b458783e32d067de78400529519ead59ab45b49d1a4296864e4d`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: filter, self. Outputs/bindings: (none).
Calls/effect boundaries: filter, self.read, self.read('ls-files', '--others', '--exclude-standard', '-z').split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[2].value.args[0].args[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:97`; AST `7d120e907bdab15e6f7403c6831e46e0ad9ad398e62a3102f4dd966921d32241`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read, self.read('ls-files', '--others', '--exclude-standard', '-z').split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[2].value.args[0].args[1].func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:97`; AST `4a66f575466c8a64a91623e291679b3ba252ddf7cc7481fe9f3e2cfb66d340a2`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].value.args[0].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[3]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:99`; AST `18eae7cd2fc96447d07d050bcc8114bf784d01a9aff2bad686698445d122b323`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set, staged. Outputs/bindings: selected.
Calls/effect boundaries: set.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[3].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:99`; AST `b0849ece77587d65a98f4c4f791e8684011bcb9eeef6a47bb806f93286bdb19b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, staged. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4]::If

Source: `infra/agentinfra/roadmap_inventory.py:100`; AST `3acf78036a5d6b0291bfdae37156d3eedaf1aa6560765436e1ba8d652085a9b6`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dirty_only, filter, selected, self, set. Outputs/bindings: selected.
Calls/effect boundaries: filter, selected.update, self.read, self.read('diff', '--cached', '--name-only', '--no-renames', '-z', 'HEAD').split, self.read('diff', '--name-only', '--no-renames', '-z', 'HEAD').split, set.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[17].body[7].body[4]; no call, error or mutation may be omitted. Condition: dirty_only
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:101`; AST `981406dbac0f3cea63925ea09b5ef26e5e49f490dac01853b2ee6a91d0e26954`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: filter, self, set. Outputs/bindings: selected.
Calls/effect boundaries: filter, self.read, self.read('diff', '--name-only', '--no-renames', '-z', 'HEAD').split, set.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:101`; AST `718838408be0c5081809a2263ef00738a3ee527dcec0305fbd2e3d7062eeef1f`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: filter, self, set. Outputs/bindings: (none).
Calls/effect boundaries: filter, self.read, self.read('diff', '--name-only', '--no-renames', '-z', 'HEAD').split, set.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:101`; AST `b59604666d8ff476e3928fa23c8ffdebdb717afa68335703a94dbc1db5bb0e84`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: filter, self. Outputs/bindings: (none).
Calls/effect boundaries: filter, self.read, self.read('diff', '--name-only', '--no-renames', '-z', 'HEAD').split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[4].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[0].value.args[0].args[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:101`; AST `7c2c050453be655ef9dd1967f566105eba686d2a285cb4855d3c6df60378b0ec`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read, self.read('diff', '--name-only', '--no-renames', '-z', 'HEAD').split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[4].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[0].value.args[0].args[1].func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:101`; AST `52325246ed4240e867dd0856111b7441bff18b1fcb1ba534a052850436cdcee7`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[4].body[0].value.args[0].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[1]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:102`; AST `a3de4a2a3c33ad7186971620d692dd5fa0f608ff8bca829a7462e489d57b43e8`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: filter, selected, self. Outputs/bindings: (none).
Calls/effect boundaries: filter, selected.update, self.read, self.read('diff', '--cached', '--name-only', '--no-renames', '-z', 'HEAD').split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:102`; AST `b6a3d5f1b845af6ce222a14a0dfe38545a580940e3d49f0fa5f826cbdf1ed698`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: filter, selected, self. Outputs/bindings: (none).
Calls/effect boundaries: filter, selected.update, self.read, self.read('diff', '--cached', '--name-only', '--no-renames', '-z', 'HEAD').split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:102`; AST `2908069410be752dee818aca70f5f1a0df654a92e155c12759561d73bef764eb`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: filter, self. Outputs/bindings: (none).
Calls/effect boundaries: filter, self.read, self.read('diff', '--cached', '--name-only', '--no-renames', '-z', 'HEAD').split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[4].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[1].value.args[0].args[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:102`; AST `0b0959de11d9256e543b701e03aa082788f658d1c9a989f3c12308460662b515`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read, self.read('diff', '--cached', '--name-only', '--no-renames', '-z', 'HEAD').split.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[4].body[1].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[4].body[1].value.args[0].args[1].func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:102`; AST `5aa889ab3d2e32d4e7649617c54aca2896483a21f0d3f3cbe6944a3a70806621`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[4].body[1].value.args[0].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[5]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:103`; AST `a7b7965b3a170a32f4c832dcadf816c9226ac79ee05946309198f15736139c37`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: selected, sorted, untracked. Outputs/bindings: names.
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[5].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:103`; AST `23f0b786f59374ddc3c919302f5f31053ba35c798e01e6a8711df66d9240ea81`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: selected, sorted, untracked. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[6]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:104`; AST `0c2eacfd48f178abcf50aa532a831f3b6a5a5e8a9f897cca11dcde7734ab24d2`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: files.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7]::For

Source: `infra/agentinfra/roadmap_inventory.py:105`; AST `4892013ced9e632c809ed113f5553adc76d302d5b3cc100b46ba9628aa340e48`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: GitInventory, any, bool, confined_path, digest, entry, files, name, names, nested, os, path, require, s, self, staged, stat. Outputs/bindings: entry, name, nested, path, s.
Calls/effect boundaries: (path / '.git').exists, GitInventory, any, bool, confined_path, digest, entry.update, files.append, nested.worktree, os.fsencode, os.readlink, path.exists, path.is_dir, path.is_file, path.is_symlink, path.read_bytes, path.stat, require, staged.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[17].body[7].body[7]; no call, error or mutation may be omitted. Iteration: name in names
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:106`; AST `16c8e9194cc4e905a83d3c71092388e0be89d88461647b1e485eaa9b22d71c6b`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[1]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:108`; AST `4e36a2058e5fe3f1082ba443483fc98f3ccb927075a5273bb500afc471db7ea6`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:108`; AST `cf8bf6878ed5997cce8e00b1c40f3508e9945c78489da6b3da18d9d8b42cc8af`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[2]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:109`; AST `25497d1892d7585551ffa6434e322a93e6eb739e9d3ad01f298af6ae7b8836f2`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, staged. Outputs/bindings: entry.
Calls/effect boundaries: staged.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[2].value.values[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:109`; AST `07f2655ca00c205cc069d1695386fc82cb36916825c560a17dd5ccd15f0373c6`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, staged. Outputs/bindings: (none).
Calls/effect boundaries: staged.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[2].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3]::If

Source: `infra/agentinfra/roadmap_inventory.py:110`; AST `37bac7f64a313e6ef84e8a1daa62d079269b15f72e103121a88f3cf92f956d6c`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GitInventory, any, bool, digest, entry, name, nested, os, path, require, s, self, stat. Outputs/bindings: nested, s.
Calls/effect boundaries: (path / '.git').exists, GitInventory, any, bool, digest, entry.update, nested.worktree, os.fsencode, os.readlink, path.exists, path.is_dir, path.is_file, path.is_symlink, path.read_bytes, path.stat, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[17].body[7].body[7].body[3]; no call, error or mutation may be omitted. Condition: path.is_symlink()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].test::Call

Source: `infra/agentinfra/roadmap_inventory.py:110`; AST `59b1c604985dcd3e66bb0b7ae49c367ee9372b6c297d22636b1ad06e54b90bcc`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_symlink.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:111`; AST `99b033ae8e37703d221faef4d172cd16593834ddf5fd140705273c2068677b72`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, entry, os, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, entry.update, os.fsencode, os.readlink.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:111`; AST `9ea148d4ffc2ada058b28c40ffa1173bbe29a9ee3ed6d0a7c1f81091c09182a7`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, entry, os, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, entry.update, os.fsencode, os.readlink.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].body[0].value.keywords[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:111`; AST `e96d8d6c85ef9c4584e0c34dcbfebe2458351b724812f209bea943f5082a44f4`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, os, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, os.fsencode, os.readlink.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].body[0].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].body[0].value.keywords[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:111`; AST `8484669251b48f50d00435ea30fe0d1a23b0369242b60bbfb8b26497b4339ee5`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, path. Outputs/bindings: (none).
Calls/effect boundaries: os.fsencode, os.readlink.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].body[0].value.keywords[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].body[0].value.keywords[1].value.args[0].args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:111`; AST `23c309da4cd59ccc8fbea7b975a3e62dfd69bda6bde87c6b3174f9fe653f2dee`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, path. Outputs/bindings: (none).
Calls/effect boundaries: os.readlink.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].body[0].value.keywords[1].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:112`; AST `75014f84567afdf264848be8dea73563da3ce79f6ddc17e5ed5ec891aa2d63b0`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GitInventory, any, bool, digest, entry, name, nested, path, require, s, self, stat. Outputs/bindings: nested, s.
Calls/effect boundaries: (path / '.git').exists, GitInventory, any, bool, digest, entry.update, nested.worktree, path.exists, path.is_dir, path.is_file, path.read_bytes, path.stat, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[17].body[7].body[7].body[3].orelse[0]; no call, error or mutation may be omitted. Condition: not path.exists()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].test.operand::Call

Source: `infra/agentinfra/roadmap_inventory.py:112`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:113`; AST `0f47cc06a52fce4916ccc5936ff629d312a493a2dc475ef680e263cfd512b50d`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.update.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[3].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:113`; AST `1d45ca7cdb9ba396d26e40197a2b8fe1c61c6ea6c8b177d4f63b7c5f14dbacbd`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.update.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:114`; AST `32ecb484185009f2e7bdb92bcaf80bb6087bf0a25b3ee4939eeea51d2ba74d89`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GitInventory, any, bool, digest, entry, name, nested, path, require, s, self, stat. Outputs/bindings: nested, s.
Calls/effect boundaries: (path / '.git').exists, GitInventory, any, bool, digest, entry.update, nested.worktree, path.is_dir, path.is_file, path.read_bytes, path.stat, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0]; no call, error or mutation may be omitted. Condition: path.is_file()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_inventory.py:114`; AST `d2081c59f0765455ac12b468dbfc8371bdf81a7d49d474e10d779496c1e121ac`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_file.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:115`; AST `44d5ec7f093fba44d992795bb75cddd973f2646713d1d5f4ecc765b59bb56031`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, digest, entry, path, stat. Outputs/bindings: (none).
Calls/effect boundaries: bool, digest, entry.update, path.read_bytes, path.stat.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:115`; AST `8e70fe70b3e471611e20bd25ef8b37c3eae76f89d9ad7cd0c1f149ab64a60218`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, digest, entry, path, stat. Outputs/bindings: (none).
Calls/effect boundaries: bool, digest, entry.update, path.read_bytes, path.stat.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value.keywords[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:115`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value.keywords[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:115`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value.keywords[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value.keywords[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:116`; AST `6726d169a6b73a9d4f55ca32fae6852aa45746ae5df1fe78eff877fb2c1cfc74`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, path, stat. Outputs/bindings: (none).
Calls/effect boundaries: bool, path.stat.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value.keywords[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value.keywords[2].value.args[0].left.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:116`; AST `4ad13a92d4c0491c8737b8fcfacd38c225911ac2f24bdb5ec5c2f1fd76d4a178`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].body[0].value.keywords[2].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:117`; AST `fa6ca352692c28da2f47d9bbe11a39cde63c5c463491212ac6e8eb89584e63af`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: GitInventory, any, entry, name, nested, path, require, s, self. Outputs/bindings: nested, s.
Calls/effect boundaries: (path / '.git').exists, GitInventory, any, entry.update, nested.worktree, path.is_dir, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0]; no call, error or mutation may be omitted. Condition: path.is_dir() and any((s['mode'] == '160000' for s in entry['index']))
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].test.values[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:117`; AST `6819eb54369694522640db8bd92d541e88abcce62d8bf6b40d60b47c12339610`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_dir.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].test.values[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:117`; AST `bded6e71be162b3407d0451fb8d1e9751f3af567189a5a3951c231718a7b1a65`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, entry, s. Outputs/bindings: s.
Calls/effect boundaries: any.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].test.values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_inventory.py:117`; AST `190f0def709c821b819693f29899c2550fffe32ca3e8c52d39a22a6c50701367`.

Rust module: `infra::agentinfra::roadmap_inventory`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: entry, s. Outputs/bindings: s.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].test.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:118`; AST `3be9ef0d3b78f6cfbb88649febc7bb817284e0aa0a3da252513675146ebfce0b`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GitInventory, path, self. Outputs/bindings: nested.
Calls/effect boundaries: GitInventory.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:118`; AST `85692bc791f846de62daad91bad3a009620063e24300110a7893ff2bf1f6a006`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GitInventory, path, self. Outputs/bindings: (none).
Calls/effect boundaries: GitInventory.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1]::If

Source: `infra/agentinfra/roadmap_inventory.py:120`; AST `d24b3b984282fb0bccb3e7bb71139a6ddc8ee7f9c73bab24fbe96bc72d031b38`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: entry, nested, path. Outputs/bindings: (none).
Calls/effect boundaries: (path / '.git').exists, entry.update, nested.worktree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1]; no call, error or mutation may be omitted. Condition: (path / '.git').exists()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].test::Call

Source: `infra/agentinfra/roadmap_inventory.py:120`; AST `6998d5ba769d6670dc1567d117c37a485f5d8ebb4211e7f2f9f7f5fa2edb85c0`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: (path / '.git').exists.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:124`; AST `bac02dbefdee71628dc60003dde5ce3ec64ae9257aa2dac9173b4104f5a1a256`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, nested. Outputs/bindings: (none).
Calls/effect boundaries: entry.update, nested.worktree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:124`; AST `4c3aaa3c8b1523db40592735e041e2de57f365195845e6750d76b6d7f5f937da`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, nested. Outputs/bindings: (none).
Calls/effect boundaries: entry.update, nested.worktree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].body[0].value.keywords[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:124`; AST `a82a770594ced27cafc5ad6be42a9c1b5470b325826251a191787f5bd6d567e4`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: nested.worktree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].body[0].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].orelse[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:126`; AST `09786f7c6f8834b50a39a3cf10e19a8e45d12edce0ed834bd704a9f5eeab698b`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.update.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].orelse[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:126`; AST `a2c035d6f2e66e252d09d14bcac198ec2d79474043b91792bb81f85752f7556e`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.update.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].body[1].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].orelse[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:128`; AST `e8729d5e284086fee9626647d8db6e4b4d81e9151f763a68d5817eae7fd0e0f0`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].orelse[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:128`; AST `a8f6f0a3a0ee1e88980f03f0f61c8afc75254e635d85d09e1770075673b1e4a8`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[3].orelse[0].orelse[0].orelse[0].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[4]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:129`; AST `5f5b39599b914247bc2f030b6d85cfee7bf7194510c51b8731c168ba2be1123a`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, files. Outputs/bindings: (none).
Calls/effect boundaries: files.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[7].body[4].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:129`; AST `12c4146401224ddeaa7e580222a3df9737df0fbd2db607c5b72b653710e238ea`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, files. Outputs/bindings: (none).
Calls/effect boundaries: files.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[8]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:130`; AST `54d02ebfbf7fa7c3495a4d48982110ef0523124027f194d9c6c25d47b16ac6d0`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: branch.
Calls/effect boundaries: self.read, self.read('rev-parse', '--abbrev-ref', 'HEAD').strip.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[8].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:130`; AST `592e67d2aa141421b43d804c965484a84510820b5c26bdf0b8e47ce043c0caeb`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read, self.read('rev-parse', '--abbrev-ref', 'HEAD').strip.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[8].value.func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:130`; AST `2f3a9abd9e29ec648a9e3818caa36e0fbbb4d78ae9048ff425ab5e7b604813d7`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[8].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[9]::Return

Source: `infra/agentinfra/roadmap_inventory.py:131`; AST `4c38b95277ecc76e0a300e211657f24498491d60442ef4263c51526148f353fa`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: branch, files, self. Outputs/bindings: (none).
Calls/effect boundaries: self.read, self.read('rev-parse', 'HEAD').strip.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[17].body[7].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[9].value.values[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:132`; AST `77919bd5ceb15e4cf19294333f1dc7af1b6e2b40bd3ca7be618f8f27180c0c0b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read, self.read('rev-parse', 'HEAD').strip.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[9].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[9].value.values[1].func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:132`; AST `ce84b264586593cb7296ac95aefd8b3198eb324760bfb45fa5b2a1a5f8903a4f`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[9].value.values[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::GitInventory::worktree::root.body[17].body[7].body[9].value.values[2]::Call

Source: `infra/agentinfra/roadmap_inventory.py:133`; AST `a0be92c25520e20fbf6c2593c7716d3edec873e922ab8fbfc68dc6dc35814749`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[9].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:137`; AST `fe55cfc079945ea5e965fc32d5733144133b82f6c31003333a8a7554e5c019e3`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: SyntaxError, UnicodeError, ValueError, ast, bytes, child, compile, definitions, dict, digest, enumerate, exc, field, filename, getattr, index, isinstance, list, node, owner, raw, route, str, tree, type, value, visit. Outputs/bindings: child, definitions, field, index, owner, tree, value.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, ast.dump(tree, include_attributes=False).encode, ast.iter_fields, ast.parse, compile, definitions.append, digest, enumerate, getattr, isinstance, type, visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:138`; AST `891a02b9e06705679da9918876916b7152ec3005726fe8e1f15dc62b8dfe8e5e`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[1]::Try

Source: `infra/agentinfra/roadmap_inventory.py:139`; AST `2d53ba257a694f2f9174dfc9d883a8d7696ab705cf7a5fcf647abbccb7f794f8`.

Rust module: `infra::agentinfra::roadmap_inventory`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: SyntaxError, UnicodeError, ValueError, ast, compile, exc, filename, getattr, raw, tree, type. Outputs/bindings: tree.
Calls/effect boundaries: ast.parse, compile, getattr, type.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Try evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:140`; AST `86b6ab8fdcb9b72e0a1b5542bd794176338a98fdef08eef50adbc9ccbd2ec60a`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, filename, raw. Outputs/bindings: tree.
Calls/effect boundaries: ast.parse.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:140`; AST `35db86c7cd5d61063b3eca13912138c2a355fe6db5e98828f3883e81416ef1eb`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, filename, raw. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[1].body[1]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:141`; AST `c797da441b497c6403b546d2b030a3c62283553e1dadd687a52884e8db235ae1`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile, filename, tree. Outputs/bindings: (none).
Calls/effect boundaries: compile.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:141`; AST `1b1f43045f5cfcc4d68d423d3274299ebb0c81f348305d26de95456301e645be`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile, filename, tree. Outputs/bindings: (none).
Calls/effect boundaries: compile.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_inventory.py:142`; AST `91756adac9b8dfd3077fedc38bb3f99fd13df7096cb3203128ece17c8022a525`.

Rust module: `infra::agentinfra::roadmap_inventory`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: SyntaxError, UnicodeError, ValueError, exc, getattr, type. Outputs/bindings: (none).
Calls/effect boundaries: getattr, type.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[18].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[1].handlers[0].body[0]::Return

Source: `infra/agentinfra/roadmap_inventory.py:143`; AST `76d631812bd49082901b4feec1b347b1495cd76e57e4f1d5ea633627b6dfdc42`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, getattr, type. Outputs/bindings: (none).
Calls/effect boundaries: getattr, type.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[1].handlers[0].body[0].value.values[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:143`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].handlers[0].body[0].value.values[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[1].handlers[0].body[0].value.values[2]::Call

Source: `infra/agentinfra/roadmap_inventory.py:144`; AST `ac71978045fdb1021cd56acb4323d6e13ca4331ec17b3a56a31949058e812969`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, getattr. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].handlers[0].body[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[2]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:145`; AST `18778529a6243b540e11b6da884f9ae2c8e8b38c981c1f5ec7b79994b62688da`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: definitions.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:147`; AST `fa728dd603fcc2a130975bde5f2abc7a830a2ad65c32af8961b74664c0172255`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ast, child, definitions, digest, enumerate, field, index, isinstance, list, node, owner, route, str, type, value, visit. Outputs/bindings: child, field, index, owner, value.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, ast.iter_fields, definitions.append, digest, enumerate, isinstance, type, visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:148`; AST `7dd475bf63ff66d6a0b5f3514aa301edef08189572fc8c56cb0a2d5ab1b684dc`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, definitions, digest, isinstance, node, owner, route, type. Outputs/bindings: owner.
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, definitions.append, digest, isinstance, type.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[18].body[3].body[0]; no call, error or mutation may be omitted. Condition: isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[0].test::Call

Source: `infra/agentinfra/roadmap_inventory.py:148`; AST `03f4d863af03611234c7247b6ee125dada11915164b7ebf16339435bb5a26fde`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, node. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:149`; AST `e45c4d864edc768baa185c827dcde863bf51eb598dee5358c17d9cfa7a377ead`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: node, owner. Outputs/bindings: owner.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:150`; AST `ce2ccaa0bfc0265de1d67ee2204005874404a90624f41caae61f0d6b6805b9d8`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, definitions, digest, node, owner, route, type. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, definitions.append, digest, type.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:150`; AST `81ec4861919ef92240b60a0433c38870920d977ab4173e590a25a002348ab7c2`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, definitions, digest, node, owner, route, type. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, definitions.append, digest, type.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[0].body[1].value.args[0].values[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:150`; AST `40afb9a8f383eda39b712357dc51899dc0008773e996773254337d7013a38657`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: node, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[1].value.args[0].values[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[0].body[1].value.args[0].values[4]::Call

Source: `infra/agentinfra/roadmap_inventory.py:152`; AST `7e015840e16c88c823dd5259f4b55423b299ef9fa3c5de015b0073b6888bb2fb`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, digest, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode, digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[1].value.args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[0].body[1].value.args[0].values[4].args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:152`; AST `62642a7f86696182149656fb0833b390cc3f67cf8dd17c2b5151717295dc243e`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(node, include_attributes=False).encode.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[1].value.args[0].values[4].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[0].body[1].value.args[0].values[4].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:152`; AST `3fb94b2b8e1dc6a1bc206dc19bca3c2e71190137190d141090f14ace7aaa9d73`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[1].value.args[0].values[4].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1]::For

Source: `infra/agentinfra/roadmap_inventory.py:153`; AST `f7fafb90064eeb9b88cb9cfcbc9901f3c1405b95963f76fbb294bba4754c3b8e`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, child, enumerate, field, index, isinstance, list, node, owner, route, value, visit. Outputs/bindings: child, field, index, value.
Calls/effect boundaries: ast.iter_fields, enumerate, isinstance, visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[18].body[3].body[1]; no call, error or mutation may be omitted. Iteration: (field, value) in ast.iter_fields(node)
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:153`; AST `09b6e3b003896a4fa601486a87b76cab47e19e25562c99483afd9a0fa4af0043`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, node. Outputs/bindings: (none).
Calls/effect boundaries: ast.iter_fields.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:154`; AST `d40ad1edd51be5110313e43e6be7b13597042508ff1cb19af7100a8f12b2d9f9`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, child, enumerate, field, index, isinstance, list, owner, route, value, visit. Outputs/bindings: child, index.
Calls/effect boundaries: enumerate, isinstance, visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[18].body[3].body[1].body[0]; no call, error or mutation may be omitted. Condition: isinstance(value, ast.AST)
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].test::Call

Source: `infra/agentinfra/roadmap_inventory.py:154`; AST `518ae0204e0bc2a7a9a0fdeab27cd350bacc9a97c1a593b3402c0f44457a4dd2`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:155`; AST `6695b0b740b6632a90cf02afb2122b8b02a144a2d2ce624c484ec7c04a11ff5f`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, owner, route, value, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:155`; AST `9db1cadd88efa75cb6c19a1601e6455496eaa68e0a300d4c157f72e55edc369d`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, owner, route, value, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:156`; AST `c72a72b957257ea1567dc843050aaf2c996519ea8b5b5aca89f1fbfd71e4bad4`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, child, enumerate, field, index, isinstance, list, owner, route, value, visit. Outputs/bindings: child, index.
Calls/effect boundaries: enumerate, isinstance, visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[18].body[3].body[1].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(value, list)
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].orelse[0].test::Call

Source: `infra/agentinfra/roadmap_inventory.py:156`; AST `f5635b2e334fb6e97f358f32dbb2b0086496303066699278ebd49fcf85562492`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].body[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].orelse[0].body[0]::For

Source: `infra/agentinfra/roadmap_inventory.py:157`; AST `314a8f9e72555b0f1b578b1857527b45f5333848b79b4626e609220292661d4f`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ast, child, enumerate, field, index, isinstance, owner, route, value, visit. Outputs/bindings: child, index.
Calls/effect boundaries: enumerate, isinstance, visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[18].body[3].body[1].body[0].orelse[0].body[0]; no call, error or mutation may be omitted. Iteration: (index, child) in enumerate(value)
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].orelse[0].body[0].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:157`; AST `7319a75af29aa16ce29cee5b47f4824c2eea50c99daf127db96a63b65622d4e7`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: enumerate, value. Outputs/bindings: (none).
Calls/effect boundaries: enumerate.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].body[0].orelse[0].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].orelse[0].body[0].body[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:158`; AST `e9de5e884d5e9b11e4f0beb3d195739dde68c05c7d9c105a10c48252ba0d2fa5`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ast, child, field, index, isinstance, owner, route, visit. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[18].body[3].body[1].body[0].orelse[0].body[0].body[0]; no call, error or mutation may be omitted. Condition: isinstance(child, ast.AST)
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].orelse[0].body[0].body[0].test::Call

Source: `infra/agentinfra/roadmap_inventory.py:158`; AST `bfd7a1d88fedbb3dac987f7a025d0b34fc3cab5882e0033352cecaa2e8492640`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, child, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].body[0].orelse[0].body[0].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].orelse[0].body[0].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:159`; AST `5b313a481047d99f0e39ca6840bb45bbc1d7234f6326cdaaa9c5a2d19abd1f1e`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: child, field, index, owner, route, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[1].body[0].orelse[0].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::visit::root.body[18].body[3].body[1].body[0].orelse[0].body[0].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:159`; AST `5613a18bedac69b9bc3642282a75f29b107af55a04a97afa423ed69a6caf397e`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: child, field, index, owner, route, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].body[0].orelse[0].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[4]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:161`; AST `cf5b7f268e71083a292c249902b2e7f6ba9bde87d724e00a88b2abc89ec1e85d`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tree, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[4].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:161`; AST `54d9837e7b8ee2da2a44fcc7b0d9ac2e34afef27ad26515c17ea2951989f198a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tree, visit. Outputs/bindings: (none).
Calls/effect boundaries: visit.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[5]::Return

Source: `infra/agentinfra/roadmap_inventory.py:162`; AST `c0b49165bd51cf86235f47f241667e6ced5681eab9777fbf5916c867cffd19b3`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, definitions, digest, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(tree, include_attributes=False).encode, digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[18].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[5].value.values[2]::Call

Source: `infra/agentinfra/roadmap_inventory.py:163`; AST `63ec8ffd75472e7162aad7ff10d0226ea2ec3986df20c7aeae7dc155dc6fdf95`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, digest, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(tree, include_attributes=False).encode, digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[5].value.values[2].args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:163`; AST `1ec20836085042906967e7e671253607bd2161e950e03150e5f22548d0d3322b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump, ast.dump(tree, include_attributes=False).encode.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::inspect_python::root.body[18].body[5].value.values[2].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:163`; AST `3972af2bd928b841027c6c53c8f7129ccd5f740103602dda5405fe078141fa83`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, tree. Outputs/bindings: (none).
Calls/effect boundaries: ast.dump.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.values[2].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:167`; AST `14302fc454799cd79c62d0c521b5e98081e7eea13f8365ea4e14cc4c6b23e263`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GitInventory, Path, any, bool, compile_roadmaps, compiled, components, confined_path, current_blobs, dict, digest, e, entries, entry, file, git, h, head_tree, heads, inspect_python, item, k, missing, oid, p, r, raw, read_json, record, refs, remote, require, root, sorted, sys, tree_id, trees, working_components, worktree. Outputs/bindings: compiled, components, current_blobs, e, entries, entry, file, git, h, head_tree, heads, item, k, missing, oid, p, r, raw, record, refs, root, tree_id, trees, working_components, worktree.
Calls/effect boundaries: GitInventory, Path, Path(git.executable).read_bytes, Path(sys.executable).read_bytes, any, compile_roadmaps, components.values, confined_path, confined_path(root, file['path'], must_exist=True).read_bytes, current_blobs.get, digest, entry['path'].endswith, file['path'].endswith, git.blob, git.read, git.read('--version').strip, git.read('rev-parse', 'HEAD^{tree}').strip, git.refs, git.remote_heads, git.tree, git.worktree, h['ref'].removeprefix, inspect_python, item['paths'].append, item['paths'].sort, item['trees'].append, item['trees'].sort, read_json, require, root.resolve, sorted, trees.items, working_components.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:168`; AST `7b881662a93f1cabda6daa8de666cd56431dd47a61da7e3a5a8856defd752ca2`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: root.
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:168`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[1]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:169`; AST `8deac8da987fee33047b87c849024fe4b35da2d8f7167922e3c744059f79a3b1`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:169`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[2]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:170`; AST `6be60ecbd9492af5c5dd6b3f753a825879749c93ccb83967aa9f6d22383d5117`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GitInventory, root. Outputs/bindings: git.
Calls/effect boundaries: GitInventory.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:170`; AST `c4f3e6818765e5df9cc7a91d7bfc9093ba441ac55f12b5153bb08ff3dd3b1703`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GitInventory, root. Outputs/bindings: (none).
Calls/effect boundaries: GitInventory.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[3]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:171`; AST `99b6e86b0f4a69a11739aab5f99a9f575f271a426b8232d7ed23a5eeeda4acc2`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git. Outputs/bindings: refs, worktree.
Calls/effect boundaries: git.refs, git.worktree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[3].value.elts[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:171`; AST `78c13c308b6e2bd0dac49d4f1ed702896988a9415d5ff722750b7c04655a265d`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.refs.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[3].value.elts[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:171`; AST `eaccaf9506c6a1a432ae26f9b9533f3e61d71e9655e377a30dc9234b441f9d96`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.worktree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[4]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:172`; AST `57b92808ea3b9f06701a2fa9b881b0d1ab86349b8c201e569dc437fff0a44553`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git, remote. Outputs/bindings: heads.
Calls/effect boundaries: git.remote_heads.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[4].value.body::Call

Source: `infra/agentinfra/roadmap_inventory.py:172`; AST `6d794f5f8b0c73eaf63b099dbde4618f83779fee41fb8f4ff4e28bc4a0b73fca`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.remote_heads.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[5]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:173`; AST `50149d327a2c82992a30c766fae26ae1eae4e5816ebcd936379a3c0da92f92dc`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git, oid, r, refs, sorted. Outputs/bindings: oid, r, trees.
Calls/effect boundaries: git.tree, sorted.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[5].value::DictComp

Source: `infra/agentinfra/roadmap_inventory.py:173`; AST `a0c4ccd29fadc11a3f048833d69313cc30e30f36cd8f29c303069e09171d933f`.

Rust module: `infra::agentinfra::roadmap_inventory`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: git, oid, r, refs, sorted. Outputs/bindings: oid, r.
Calls/effect boundaries: git.tree, sorted.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered DictComp evaluation at root.body[19].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[5].value.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:173`; AST `1e04bc07447db05816209e7783c19f8207d435ecc240d003c38c7840d1e8aac4`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git, oid. Outputs/bindings: (none).
Calls/effect boundaries: git.tree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[5].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:173`; AST `922864109ebb62ced918530a50c1edf34da0c6da20d5516514e536d8d4de0868`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, refs, sorted. Outputs/bindings: r.
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[5].value.generators[0].iter.args[0]::SetComp

Source: `infra/agentinfra/roadmap_inventory.py:173`; AST `460b0a1881b0ee0127ec1d51afb6cc821240ae2dedaf41dc572a8c3e273116b3`.

Rust module: `infra::agentinfra::roadmap_inventory`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: r, refs. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered SetComp evaluation at root.body[19].body[5].value.generators[0].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[6]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:174`; AST `93e175e5285e9837b16f95f52c140f64cbe6871dc5ad2edc86b24fd5e504ac12`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git. Outputs/bindings: head_tree.
Calls/effect boundaries: git.read, git.read('rev-parse', 'HEAD^{tree}').strip.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[6].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:174`; AST `7d255e4f127872492c1765b0271060d7c55da9fcb4cc9e28496d5d1c0f83f69b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.read, git.read('rev-parse', 'HEAD^{tree}').strip.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[6].value.func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:174`; AST `ff910a80c0eaea1e9d9c60201c4cd2f354a8dcdb4b2ec43c823194cb4d8953ba`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[7]::If

Source: `infra/agentinfra/roadmap_inventory.py:175`; AST `8d7223d13ee6483f768ff711c2bd96863e64ce082574c114e98b9902a37ac7d6`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: git, head_tree, trees. Outputs/bindings: (none).
Calls/effect boundaries: git.tree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[19].body[7]; no call, error or mutation may be omitted. Condition: head_tree not in trees
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[7].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:176`; AST `b05aefed36c2d9c963fbb0585c50c1a058b587a46fa546ce73f62613fb08a2f5`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git, head_tree, trees. Outputs/bindings: (none).
Calls/effect boundaries: git.tree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:176`; AST `75e714892ffcf0378c78ba8c2caddaeaa634ef2c10b0e8e186fd05fa0bba410c`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git, head_tree. Outputs/bindings: (none).
Calls/effect boundaries: git.tree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[8]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:177`; AST `8df7a968182792cfd5a0bcfba10f0206d051c827fed89c9d55efeaf5dea2976f`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: e, head_tree, trees. Outputs/bindings: current_blobs, e.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[8].value::DictComp

Source: `infra/agentinfra/roadmap_inventory.py:177`; AST `0dd0847c84b0c40c46aafeda301c939a4ec01590078f202259cf6147aedf66a0`.

Rust module: `infra::agentinfra::roadmap_inventory`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: e, head_tree, trees. Outputs/bindings: e.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered DictComp evaluation at root.body[19].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[9]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:178`; AST `e41bce7bae300ad13f11ac9b97d64c51c783777bf7de2dc68b66d7fcbd070b85`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: components.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10]::For

Source: `infra/agentinfra/roadmap_inventory.py:179`; AST `77728748402a73c0edf48c683064ff6d2ff152f09254778b93f581a0b390fee8`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: components, digest, entries, entry, git, inspect_python, item, oid, raw, tree_id, trees. Outputs/bindings: entries, entry, item, oid, raw, tree_id.
Calls/effect boundaries: digest, entry['path'].endswith, git.blob, inspect_python, item['paths'].append, item['trees'].append, trees.items.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[19].body[10]; no call, error or mutation may be omitted. Iteration: (tree_id, entries) in trees.items()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:179`; AST `dcd4409fbcca47504cfd6baf2bb54017156ee4e01dee966cf33dd59aba300d34`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: trees. Outputs/bindings: (none).
Calls/effect boundaries: trees.items.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0]::For

Source: `infra/agentinfra/roadmap_inventory.py:180`; AST `dc52c6c0d9a932562594a8c15a61055259b7194fa8703e59b25a849b4f2a6852`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: components, digest, entries, entry, git, inspect_python, item, oid, raw, tree_id. Outputs/bindings: entry, item, oid, raw.
Calls/effect boundaries: digest, entry['path'].endswith, git.blob, inspect_python, item['paths'].append, item['trees'].append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[19].body[10].body[0]; no call, error or mutation may be omitted. Iteration: entry in entries
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:181`; AST `563cf6bea8e7aabddbe84462289ed93bfeb7627437f25f061c5bface024d544a`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry['path'].endswith.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[19].body[10].body[0].body[0]; no call, error or mutation may be omitted. Condition: entry['type'] != 'blob' or entry['mode'] == '120000' or (not entry['path'].endswith('.py'))
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[0].test.values[2].operand::Call

Source: `infra/agentinfra/roadmap_inventory.py:181`; AST `8abb863a5b1ee69fee160afa4714babc5755aca91161d451a2ad4a895c95a2e5`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry['path'].endswith.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].body[0].test.values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[0].body[0]::Continue

Source: `infra/agentinfra/roadmap_inventory.py:182`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Continue evaluation at root.body[19].body[10].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:183`; AST `be4eab38b06b8a75a0c9eeed1f9bd97055f7e9b4ca0a5954a2cb3df2a20290ef`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: oid.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[10].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[2]::If

Source: `infra/agentinfra/roadmap_inventory.py:184`; AST `d20c187afc128ed787d27668f116906446eaac9daa783fcda0376c572f36b1a9`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: components, digest, entry, git, inspect_python, oid, raw. Outputs/bindings: raw.
Calls/effect boundaries: digest, git.blob, inspect_python.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[19].body[10].body[0].body[2]; no call, error or mutation may be omitted. Condition: oid not in components
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:185`; AST `d9d136ca810c20a6d02d118b91f03cbe57303b0b659ec6ad00ac325d1cc66db3`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git, oid. Outputs/bindings: raw.
Calls/effect boundaries: git.blob.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[10].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:185`; AST `e5b33526f31ca7f0935dbd1cdc5e5ba0c9f3b6cf7fc4a4cbd9638def07c145b8`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git, oid. Outputs/bindings: (none).
Calls/effect boundaries: git.blob.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[2].body[1]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:186`; AST `55803e0bd6eacf3ed907e071374fb3f7cdeeb34fe853946e9a008a6af8f597a8`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: components, digest, entry, inspect_python, oid, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest, inspect_python.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[10].body[0].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[2].body[1].value.values[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:186`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].body[2].body[1].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[2].body[1].value.values[4]::Call

Source: `infra/agentinfra/roadmap_inventory.py:187`; AST `5999ef6bb61b0dd0991615e08f12c70fee66d4a55e6e7b75f11c705aba84364d`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, inspect_python, raw. Outputs/bindings: (none).
Calls/effect boundaries: inspect_python.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].body[2].body[1].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[3]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:188`; AST `37beb7ecf079ccd764ca0c9f702417dfe975dea8eb4fe558577482dbf7eb6ab8`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: components, oid. Outputs/bindings: item.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[10].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[4]::If

Source: `infra/agentinfra/roadmap_inventory.py:189`; AST `61e8ccf56589bdcd381317f1f6b2fa02745f62057f75f1f096d58939dc9c9dce`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: entry, item. Outputs/bindings: (none).
Calls/effect boundaries: item['paths'].append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[19].body[10].body[0].body[4]; no call, error or mutation may be omitted. Condition: entry['path'] not in item['paths']
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:190`; AST `85302255ed4daa8a03c0f1c025d9c5e60aad268e8f4b55d8de2b360b277dc688`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, item. Outputs/bindings: (none).
Calls/effect boundaries: item['paths'].append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[10].body[0].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:190`; AST `25ed559f4276df8e8aaf9de2c181c15b11099f11190ffc485ec44a72825ad112`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, item. Outputs/bindings: (none).
Calls/effect boundaries: item['paths'].append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[5]::If

Source: `infra/agentinfra/roadmap_inventory.py:191`; AST `6d92caf44dc31ef0ca754bee519f81aa3e023d315cd6ec06d69489f3c139582a`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: item, tree_id. Outputs/bindings: (none).
Calls/effect boundaries: item['trees'].append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[19].body[10].body[0].body[5]; no call, error or mutation may be omitted. Condition: tree_id not in item['trees']
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:192`; AST `e28bca93cdb3487a1124c574fac4296ddfce5678ce545c8f42664c3bbd860851`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item, tree_id. Outputs/bindings: (none).
Calls/effect boundaries: item['trees'].append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[10].body[0].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[10].body[0].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:192`; AST `eec1c32121782d6972424d337a21eeb3ad483797ab65d6c614c0bb6136be3e83`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item, tree_id. Outputs/bindings: (none).
Calls/effect boundaries: item['trees'].append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11]::For

Source: `infra/agentinfra/roadmap_inventory.py:193`; AST `eaf1a266f060b4990d08ef39d28e4c6941040f86fd58c982a496a4bbb67f78ab`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: components, current_blobs, item, p. Outputs/bindings: item, p.
Calls/effect boundaries: components.values, current_blobs.get, item['paths'].sort, item['trees'].sort.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[19].body[11]; no call, error or mutation may be omitted. Iteration: item in components.values()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:193`; AST `f5be0c19deaa24b573fcaa250fdbce4f86f16fed527b5a821606bd956588698b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: components. Outputs/bindings: (none).
Calls/effect boundaries: components.values.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[11].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:194`; AST `d50acfc11f83ec6e1fc10882d504626aeb8c40bf9392d63a94aaecb94050004f`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: item['paths'].sort.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:194`; AST `097e59fbf7ed599eb24ba1e8529523645ef0a93d64e731b160ea9d96fbe59b92`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: item['paths'].sort.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11].body[1]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:195`; AST `c3b457ed963ba02ac0b3f7745868bc8136709d666bf37291ee4d92f63051c114`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: item['trees'].sort.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:195`; AST `d72398fcff666a98ceb4d821f74d3566e593fd673a5c86865c8f1fce9fee195e`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: item['trees'].sort.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11].body[2]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:196`; AST `4c13052fd47d8ace27fffcca5032fadb12e641ceab2d835b4df3908ec3b99ffc`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current_blobs, item, p. Outputs/bindings: p.
Calls/effect boundaries: current_blobs.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11].body[2].value::ListComp

Source: `infra/agentinfra/roadmap_inventory.py:196`; AST `0b09617fad03f26d3e38e02d6789e449f3bdbac300321721282c7cc60649e792`.

Rust module: `infra::agentinfra::roadmap_inventory`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: current_blobs, item, p. Outputs/bindings: p.
Calls/effect boundaries: current_blobs.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[19].body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11].body[2].value.generators[0].ifs[0].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:196`; AST `1f4f2d781e17786451a7b49c915d176ac9874e6ac71fb0cfade8bfe4d8078d15`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_blobs, p. Outputs/bindings: (none).
Calls/effect boundaries: current_blobs.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[11].body[2].value.generators[0].ifs[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[11].body[3]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:197`; AST `f6db9a6d698326a027535e612a3e9659b2f56f0b0e670965f501b0c7ffe38df0`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: item. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[12]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:199`; AST `0423cb4f69e6df71a56d7e20f54eec7a23fe0145fb694c6c2121cdb21d149d57`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: working_components.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13]::For

Source: `infra/agentinfra/roadmap_inventory.py:200`; AST `84447d4b3f061a0f398dd4d7b0a1787d02ac35a01b50199062b7080d2b402b5a`.

Rust module: `infra::agentinfra::roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: confined_path, digest, file, inspect_python, raw, require, root, working_components, worktree. Outputs/bindings: file, raw.
Calls/effect boundaries: confined_path, confined_path(root, file['path'], must_exist=True).read_bytes, digest, file['path'].endswith, inspect_python, require, working_components.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered For evaluation at root.body[19].body[13]; no call, error or mutation may be omitted. Iteration: file in worktree['files']
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0]::If

Source: `infra/agentinfra/roadmap_inventory.py:201`; AST `f64d5cb5fead024205c402bcce292228cc98acfb4bcde31213192429bd87c7df`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: confined_path, digest, file, inspect_python, raw, require, root, working_components. Outputs/bindings: raw.
Calls/effect boundaries: confined_path, confined_path(root, file['path'], must_exist=True).read_bytes, digest, file['path'].endswith, inspect_python, require, working_components.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[19].body[13].body[0]; no call, error or mutation may be omitted. Condition: file['kind'] == 'file' and file['path'].endswith('.py')
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].test.values[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:201`; AST `acef9e34c7e0804321211b2878bf09943d1103dc6d3d6064b17f152514e7117b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file. Outputs/bindings: (none).
Calls/effect boundaries: file['path'].endswith.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[13].body[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:202`; AST `cc04531a43db0c8f0e8ea5159b494a1bbce401d1f76f6d18995c39339eb21ed3`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, file, root. Outputs/bindings: raw.
Calls/effect boundaries: confined_path, confined_path(root, file['path'], must_exist=True).read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[13].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:202`; AST `b0d1f55ccd31481c5f8e909b42f487f08720e66975872eb5c00e29095bbd7a62`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, file, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, confined_path(root, file['path'], must_exist=True).read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[13].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:202`; AST `a6db50407fd8cdeffcc7527e45c33d70316b02a6a07df8b9cf7be5c688ef3850`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, file, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[13].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:203`; AST `9f1c5236d11ccaa9ea674d020505f60831ebdf9449ce8ad833e5b7f73b39ae4b`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, file, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[13].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:203`; AST `9f199de31e9b8dc8830d960c4df8d3b2534a63e2e7c279c08090863b8f74c8ed`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, file, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[13].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:203`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[13].body[0].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].body[2]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:204`; AST `9983f5a24be01deab4998b2e46dd844c36e9f637e70a93b214dbd564f6c41370`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file, inspect_python, raw, working_components. Outputs/bindings: (none).
Calls/effect boundaries: inspect_python, working_components.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[13].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:204`; AST `a073cd6b8eb364f3ffa370f987ab3c1872c2a173f1d058dac9421b72d95a850b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file, inspect_python, raw, working_components. Outputs/bindings: (none).
Calls/effect boundaries: inspect_python, working_components.append.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[13].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[13].body[0].body[2].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_inventory.py:205`; AST `72b18b44f8d42ce1133fc61116685958491e1299629a0f2f4e54445c84b4e85f`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file, inspect_python, raw. Outputs/bindings: (none).
Calls/effect boundaries: inspect_python.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[13].body[0].body[2].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[14]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:206`; AST `8653ee2003dbdb68272bccee7e8f5b8ce3dfdea8c883449db950bcf676dd4c1e`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, h, heads, r, refs. Outputs/bindings: h, missing, r.
Calls/effect boundaries: any, h['ref'].removeprefix.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[14].value.orelse::ListComp

Source: `infra/agentinfra/roadmap_inventory.py:206`; AST `80cd487894ce02c295dd966af686f57d368a4e9bc6c2bfde7ad7b50f70e331db`.

Rust module: `infra::agentinfra::roadmap_inventory`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: any, h, heads, r, refs. Outputs/bindings: h, r.
Calls/effect boundaries: any, h['ref'].removeprefix.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[19].body[14].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[14].value.orelse.generators[0].ifs[0].operand::Call

Source: `infra/agentinfra/roadmap_inventory.py:206`; AST `4faf89e898298fcf3a90cd81bf06b74c3aff50df3af58dc025ed4c1b2a83ef5a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, h, r, refs. Outputs/bindings: r.
Calls/effect boundaries: any, h['ref'].removeprefix.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[14].value.orelse.generators[0].ifs[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[14].value.orelse.generators[0].ifs[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_inventory.py:206`; AST `60103a7bef0d71e76b4f0185af7c396bd0aa2cde88e373fb567461ab436332e3`.

Rust module: `infra::agentinfra::roadmap_inventory`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: h, r, refs. Outputs/bindings: r.
Calls/effect boundaries: h['ref'].removeprefix.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[19].body[14].value.orelse.generators[0].ifs[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[14].value.orelse.generators[0].ifs[0].operand.args[0].elt.values[0].comparators[0].right::Call

Source: `infra/agentinfra/roadmap_inventory.py:207`; AST `043a710ebda2e64fb3d306695e08e11295390509d13a050d2f95938141e100c5`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: h. Outputs/bindings: (none).
Calls/effect boundaries: h['ref'].removeprefix.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[14].value.orelse.generators[0].ifs[0].operand.args[0].elt.values[0].comparators[0].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[15]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:209`; AST `0976e6d993464edd230ade1f031f74c8122807967c77964d9e2f80621bbbd140`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git, refs, require, worktree. Outputs/bindings: (none).
Calls/effect boundaries: git.refs, git.worktree, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[15].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:209`; AST `c71fd1aae156ba72b13fa88a3c60d50b21cbf46646ac25cf16430418b092128d`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git, refs, require, worktree. Outputs/bindings: (none).
Calls/effect boundaries: git.refs, git.worktree, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[15].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:209`; AST `78c13c308b6e2bd0dac49d4f1ed702896988a9415d5ff722750b7c04655a265d`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.refs.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[15].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[15].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:209`; AST `eaccaf9506c6a1a432ae26f9b9533f3e61d71e9655e377a30dc9234b441f9d96`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.worktree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[15].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[16]::If

Source: `infra/agentinfra/roadmap_inventory.py:211`; AST `060abc5309b793ea86e2975fd88d50d2bc090f1bc6bd45dd15f0545f034ba5c4`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: git, heads, remote, require. Outputs/bindings: (none).
Calls/effect boundaries: git.remote_heads, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[19].body[16]; no call, error or mutation may be omitted. Condition: remote
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[16].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:212`; AST `5cb5402a623086721a09006a66e2108a60f0612902ba2716889e49abc38c0210`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git, heads, require. Outputs/bindings: (none).
Calls/effect boundaries: git.remote_heads, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[16].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:212`; AST `83bcbd035dc91c412fa72f4a5895b68d09b9cda05dee3183cf273f458792346f`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git, heads, require. Outputs/bindings: (none).
Calls/effect boundaries: git.remote_heads, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[16].body[0].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:212`; AST `6d794f5f8b0c73eaf63b099dbde4618f83779fee41fb8f4ff4e28bc4a0b73fca`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.remote_heads.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[16].body[0].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[17]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:213`; AST `b3840a63f3ba5d3df36678fabeae981478f99a0b03b7822a2df27ad268f62c14`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[17].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:213`; AST `db51dbad2db923b48be8b90bb6e23903eb8427fdd1497b4c1164103b20e433ca`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[17].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:213`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[17].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:214`; AST `a6aca29595099b3608196fe729f0f22a158298c74d4a92ed7bfa51037aeee7dd`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, compiled, components, digest, git, heads, k, missing, read_json, refs, root, sorted, sys, trees, working_components, worktree. Outputs/bindings: k, record.
Calls/effect boundaries: Path, Path(git.executable).read_bytes, Path(sys.executable).read_bytes, digest, git.read, git.read('--version').strip, read_json, sorted.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[3].values[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:215`; AST `a8d9d42eba3d34d3c0d4354d79fd3dd86d177a4a598f1ed9882bafbac5a218c0`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.read, git.read('--version').strip.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[3].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[3].values[0].func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:215`; AST `230810e4120f5f2f8e0a98e08d3bba67e62ee641f325fb0738b91e12476ec607`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.read.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[3].values[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[3].values[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:216`; AST `a6577458ff666da80fffc72a7490094fc3fe44e0a432ff58bd3ec64aa01c115f`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, digest, git. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(git.executable).read_bytes, digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[3].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[3].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:216`; AST `0aa89ddb9b8010b7201252ae10eceb268a930cd3f85ae70daaff02bbb29be120`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, git. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(git.executable).read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[3].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[3].values[1].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:216`; AST `7e574d149f43754241590b9c19aa6e0c9d7b8a8673224ad8bab492dfbad37fa4`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, git. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[3].values[1].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[4].values[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:217`; AST `528ea3efa8d833443ff176961af24a64957faeab5035acec50efb249cc33cc26`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, digest, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(sys.executable).read_bytes, digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[4].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[4].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:217`; AST `6ba59d0cde0384f15a99107ebe91ed97a2207941295cc5fe8bd44d690ab106cf`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(sys.executable).read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[4].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[4].values[1].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_inventory.py:217`; AST `0dfff54cbeeb64407db17d4e6b154f3aff810a988368a772f2aaa5d71265f9f3`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[4].values[1].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[5].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:218`; AST `af70a22f720ae73f648afa912b6f043c56b23a86a00a84ebf5da685d712fa8ca`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[6].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:219`; AST `f4ebe3be84bb03a3d5ab28ad91db4aeb8b81839964a1a9e0feb834d586af6ea5`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[9]::ListComp

Source: `infra/agentinfra/roadmap_inventory.py:220`; AST `630277040438beac59f9c6ed3d17882e3f714aceae84ae06d6b766122330142c`.

Rust module: `infra::agentinfra::roadmap_inventory`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: components, k, sorted. Outputs/bindings: k.
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered ListComp evaluation at root.body[19].body[18].value.values[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[18].value.values[9].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:220`; AST `2c127772f33b0b44bf9dd594ecbb8d4a1bf6c092add067532f066cab8d3f70da`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: components, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[18].value.values[9].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[19]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:230`; AST `2cd571b5f223c91bf0c2b7adc8375639657e29aeb0946de69040a188919c46fd`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[19].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:230`; AST `459942b3b031c512f2c84b1ead1f069f2c56349cbb6bb8b33eba095d39132ca1`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[19].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::authority_inventory::root.body[19].body[20]::Return

Source: `infra/agentinfra/roadmap_inventory.py:231`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[19].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:234`; AST `312507ed990b0797e1d56f2712e081e19a375cbf7a2ae074e4cb842ad8f6d57d`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: GitInventory, Mutation, Path, ProjectAdapter, adapter, before, binding, canonical, compile_roadmaps, compiled, confined_path, current, dict, digest, git, k, loads, path, raw, record, relative, require, root, snapshot, str, v. Outputs/bindings: adapter, before, binding, compiled, current, git, k, path, raw, relative, root, snapshot, v.
Calls/effect boundaries: GitInventory, Mutation, ProjectAdapter, adapter.profile.path, adapter.update, before.decode, canonical, compile_roadmaps, confined_path, current.get, digest, git.refs, git.remote_heads, git.worktree, loads, path.exists, path.read_bytes, record.get, record.items, require, root.resolve, snapshot.exists, snapshot.read_bytes, str.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:235`; AST `944a1f867bb4825dc44514d8c35404597404228cb5c7cfd39bcd924506db252e`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[1]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:236`; AST `7b881662a93f1cabda6daa8de666cd56431dd47a61da7e3a5a8856defd752ca2`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: root.
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:236`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[2]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:237`; AST `0989424e6c002f729af744d3badda86a1c9f15a948c91a652170add0ff2c800c`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, k, record, require, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, record.get, record.items, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:237`; AST `e50b9329a7fffcad43ba8d2f0c909477ef285647d7fa5f6fdd0705f46a53659b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, k, record, require, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, record.get, record.items, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:237`; AST `d1e3876e5f2eab25e6fd365f06eea6e829f195ef666744ac41314682d8aa382c`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[2].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:237`; AST `c3bb259e3d43611733c89814383b6ebd2b5de06afd3f21d65c230b51a110c055`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[2].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:238`; AST `f85b4dd47821e9991a0d126a378f7f1f3492e554e34a9b78bdb37dc80e7c748a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, k, record, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, record.items.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[2].value.args[0].values[2].left.args[0]::DictComp

Source: `infra/agentinfra/roadmap_inventory.py:238`; AST `b76e2c4132c2758688026e637ebefcf3d952ee95e37afeee51bbb08ffe18aa4a`.

Rust module: `infra::agentinfra::roadmap_inventory`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: k, record, v. Outputs/bindings: k, v.
Calls/effect boundaries: record.items.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered DictComp evaluation at root.body[20].body[2].value.args[0].values[2].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[2].value.args[0].values[2].left.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_inventory.py:238`; AST `0c638694dd9bcc5a47f4372464afd715778fa5400c2fd2354815e3b19345576f`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.items.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].value.args[0].values[2].left.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[2].value.args[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:238`; AST `cc902335b5e84a60d3f5d436c4e9605eac2331bc08cddbd8a4aa3c5cd6a89b05`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].value.args[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[3]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:240`; AST `8deac8da987fee33047b87c849024fe4b35da2d8f7167922e3c744059f79a3b1`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[3].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:240`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[4]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:241`; AST `4b576526b1b155300d86e5b573617dc9845483a880fcddadc59dc114421ad514`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[4].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:241`; AST `f0707a2321952495d029e14e7f9f0aa50dd3056f68efcf7f9abbca2ef399aff0`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[5]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:242`; AST `6be60ecbd9492af5c5dd6b3f753a825879749c93ccb83967aa9f6d22383d5117`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: GitInventory, root. Outputs/bindings: git.
Calls/effect boundaries: GitInventory.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[5].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:242`; AST `c4f3e6818765e5df9cc7a91d7bfc9093ba441ac55f12b5153bb08ff3dd3b1703`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: GitInventory, root. Outputs/bindings: (none).
Calls/effect boundaries: GitInventory.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[6]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:243`; AST `399b513ef34b941a4c52dc45b08a4f060e451fec6b587212f67fa45104ac72cc`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git, record, require. Outputs/bindings: (none).
Calls/effect boundaries: git.refs, git.worktree, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[6].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:243`; AST `0580e6a46967c90dd42be1bc09b26a47dbf92d13bd14caac1e9b86d8704aed20`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git, record, require. Outputs/bindings: (none).
Calls/effect boundaries: git.refs, git.worktree, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:243`; AST `78c13c308b6e2bd0dac49d4f1ed702896988a9415d5ff722750b7c04655a265d`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.refs.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[6].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:243`; AST `eaccaf9506c6a1a432ae26f9b9533f3e61d71e9655e377a30dc9234b441f9d96`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.worktree.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[6].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[7]::If

Source: `infra/agentinfra/roadmap_inventory.py:245`; AST `f9d23aa8057e921d614fcb2363c562bbc667577859db65f73463918f2bd65533`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: git, record, require. Outputs/bindings: (none).
Calls/effect boundaries: git.remote_heads, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[20].body[7]; no call, error or mutation may be omitted. Condition: record['remote_heads'] is not None
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:246`; AST `1816ed401b0b1c3d8cf17aa61c91b6c7eab5021802ad0b86806fefb0550ff692`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: git, record, require. Outputs/bindings: (none).
Calls/effect boundaries: git.remote_heads, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:246`; AST `d70b3e7b055a996f767b2b85e8352e003e98393b2a9daf992cb0d3ca17f2b3e7`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git, record, require. Outputs/bindings: (none).
Calls/effect boundaries: git.remote_heads, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[7].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:246`; AST `6d794f5f8b0c73eaf63b099dbde4618f83779fee41fb8f4ff4e28bc4a0b73fca`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: git. Outputs/bindings: (none).
Calls/effect boundaries: git.remote_heads.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[7].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[8]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:247`; AST `b6172125a67c50c8d5431ca2430da716f0fd6d36dbe751f8d007ca848ae4689f`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectAdapter, compiled, root. Outputs/bindings: adapter.
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[8].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:247`; AST `34070b08bb0c7b59cc573fde0061a38262446fb5c93884879e95b4abee99e94e`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectAdapter, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: ProjectAdapter.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[9]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:248`; AST `c2f66728d4257ec5cc608da0d3a9e21bdec7f01e866e1398a18863e33002c193`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adapter. Outputs/bindings: path.
Calls/effect boundaries: adapter.profile.path.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[9].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:248`; AST `927525f77bb177789ff98c6b0b191aecb990be874c5131819c07ab4a33f375ea`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: adapter.profile.path.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[10]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:249`; AST `364d0fe982fb1e9a6aaf875395a3ff50afbc7a163dde40b7c13e3188964c3c13`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: before.
Calls/effect boundaries: path.exists, path.read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[10].value.test::Call

Source: `infra/agentinfra/roadmap_inventory.py:249`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[10].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[10].value.body::Call

Source: `infra/agentinfra/roadmap_inventory.py:249`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[10].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[11]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:250`; AST `92d200e267e0e5669e452d334e8c4bcb3cdafe97ce3c7988af666cb5363da2f7`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, loads. Outputs/bindings: current.
Calls/effect boundaries: before.decode, loads.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[11].value.body::Call

Source: `infra/agentinfra/roadmap_inventory.py:250`; AST `1bdeb6848cd90df0a771ae4e779d89aed864d15bc2917c477a4084431f9beebf`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, loads. Outputs/bindings: (none).
Calls/effect boundaries: before.decode, loads.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[11].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[11].value.body.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:250`; AST `797b7f1e852c5adfb7f77d47f99dd7b7483943b0928c21cd3aea703a3d98f4fb`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before.decode.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[11].value.body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[12]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:251`; AST `53956a0f6c74192c801f6e9c171f36f3176ba3fdd7bdd52d1b667ab2da65c120`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[12].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:251`; AST `7157b24da640e5186cc30aa69b1daf5dc53b5c383ce9e3c7686c954f2e9b6cee`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, require. Outputs/bindings: (none).
Calls/effect boundaries: current.get, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[12].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:251`; AST `39e99b38bcfc4b09f7f37b19c5ef27e320272361c64ac31fa17eb517df036a80`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[12].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:251`; AST `be1a99d81582e11823fc499e8be4c6824f9ecbe66e705ee429308b48fd6745f8`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[12].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[13]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:253`; AST `655e93d533d80cf7bf9194f690cb64ac5815d9ecb2c84c19a366abf59ab6c3a7`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: relative.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[14]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:254`; AST `96cc5fde99b94c7284b0793e7084fa47be1c7481982e1be9203c9b907c0f93d5`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, relative, root. Outputs/bindings: snapshot.
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[14].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:254`; AST `3e1e1c10888d3cc5f92d24591daa47142fdd193b697a734ec655b65fc78de42f`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[15]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:255`; AST `26a7e4a1a3c656ea1d39f700570d3d5729e6c58c45053967ef85f16d8fc8c949`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, record. Outputs/bindings: raw.
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[15].value.left::Call

Source: `infra/agentinfra/roadmap_inventory.py:255`; AST `54f160f3a3abda8314755593356f77dc6e10daab8f07552bdf9b5f9e686d526c`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, record. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[15].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[16]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:256`; AST `8bd6d874c9a1fbad82398a94c9206782de08022d030ea3f54800d6ffd14a3f9e`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw, require, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: require, snapshot.exists, snapshot.read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[16].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:256`; AST `d8a476f7a220b9befd6e11b3827565a30340cc5c47004a0f859a3e6fa746318a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw, require, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: require, snapshot.exists, snapshot.read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[16].value.args[0].values[0].operand::Call

Source: `infra/agentinfra/roadmap_inventory.py:256`; AST `e15f906b3d8cab52f1caac2292719549dd72595619885b7447bd3453d4b5e948`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: snapshot. Outputs/bindings: (none).
Calls/effect boundaries: snapshot.exists.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[16].value.args[0].values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[16].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_inventory.py:256`; AST `475d3ac6c92d22a97ca26d2f884fa473467e837f7fdedb97296b493c8e016c6d`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: snapshot. Outputs/bindings: (none).
Calls/effect boundaries: snapshot.read_bytes.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[16].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[17]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:257`; AST `a2da067d662f06c2c3aac3769cab0d046b3268eb08a1bbab831aef2a9b8fabb3`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, raw, relative. Outputs/bindings: binding.
Calls/effect boundaries: digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[17].value.values[1]::Call

Source: `infra/agentinfra/roadmap_inventory.py:257`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[17].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[18]::If

Source: `infra/agentinfra/roadmap_inventory.py:258`; AST `f934229d3fcaa7214877b5ea72b470ebe971296246749941040d9dc89fd0f474`.

Rust module: `infra::agentinfra::roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: binding, current, path, str. Outputs/bindings: (none).
Calls/effect boundaries: current.get, str.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered If evaluation at root.body[20].body[18]; no call, error or mutation may be omitted. Condition: current.get('authority_inventory') == binding
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[18].test.left::Call

Source: `infra/agentinfra/roadmap_inventory.py:258`; AST `5fa7e77035a4057b699c4a5f2daaf838c6da9fdeca388f3299bd12413d771379`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[18].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[18].body[0]::Return

Source: `infra/agentinfra/roadmap_inventory.py:259`; AST `7e035b357db2256b456ab0249c5cda2ab90b4869b7f36e19a5e8dcdbaf7f77d2`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[20].body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[18].body[0].value.values[2]::Call

Source: `infra/agentinfra/roadmap_inventory.py:259`; AST `b69621d1d2cfab110acfa6b4ec39b44f2e36ecd25b7402532cc02261af94b6bf`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[18].body[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[19]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:260`; AST `bb477c8f9a3895a9f8dff3b1ae502c451cc0ee4aad92cd5420ccc0b15bf6d7ea`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Mutation, adapter, before, binding, digest, raw, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, adapter.update, digest, snapshot.exists.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[19].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:260`; AST `074dd69a33bfe76b9d7fb2ed2d9fe1f6860758b76ee39a15ded3fd0d6bdc6521`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, adapter, before, binding, digest, raw, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, adapter.update, digest, snapshot.exists.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[19].value.keywords[1].value.body::Call

Source: `infra/agentinfra/roadmap_inventory.py:261`; AST `4a63ff00fb497e1d094ddb9e4f8ada535aacd403c14cfceee7fc8dd669fbee57`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[19].value.keywords[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[19].value.keywords[2].value.elts[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:262`; AST `d557c503ea17f150639a682b843c164d1919b3488d94b144923592355d393dbd`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, digest, raw, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, digest, snapshot.exists.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[19].value.keywords[2].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[19].value.keywords[2].value.elts[0].keywords[0].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:262`; AST `e15f906b3d8cab52f1caac2292719549dd72595619885b7447bd3453d4b5e948`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: snapshot. Outputs/bindings: (none).
Calls/effect boundaries: snapshot.exists.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[19].value.keywords[2].value.elts[0].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[19].value.keywords[2].value.elts[0].keywords[1].value.test::Call

Source: `infra/agentinfra/roadmap_inventory.py:263`; AST `e15f906b3d8cab52f1caac2292719549dd72595619885b7447bd3453d4b5e948`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: snapshot. Outputs/bindings: (none).
Calls/effect boundaries: snapshot.exists.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[19].value.keywords[2].value.elts[0].keywords[1].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[19].value.keywords[2].value.elts[0].keywords[1].value.body::Call

Source: `infra/agentinfra/roadmap_inventory.py:263`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[19].value.keywords[2].value.elts[0].keywords[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[20]::Return

Source: `infra/agentinfra/roadmap_inventory.py:264`; AST `5ecbabb34568b288f0a09b5ca5835051aea68e853155c2e4a736bfe71e2ada59`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[20].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::save_inventory::root.body[20].body[20].value.values[2]::Call

Source: `infra/agentinfra/roadmap_inventory.py:264`; AST `b69621d1d2cfab110acfa6b4ec39b44f2e36ecd25b7402532cc02261af94b6bf`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[20].body[20].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21]::FunctionDef

Source: `infra/agentinfra/roadmap_inventory.py:267`; AST `b763c192cc6ae489ca0537a5456f05a214f8b645796f2a5c00cc64014ee19638`.

Rust module: `infra::agentinfra::roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, all, authority_inventory, c, current, dict, len, record, require, root. Outputs/bindings: c, current.
Calls/effect boundaries: all, authority_inventory, len, record.get, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[0]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:268`; AST `357feda87629b79e6bdc41d72401b719bc9bbddcf62403e7eb6e1e3e4c539973`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[1]::Assign

Source: `infra/agentinfra/roadmap_inventory.py:269`; AST `d70f3d6e1f37b1ccec2b5eb8628bd61a7c130f9cc7f1b4575ea529b6123e841f`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, record, root. Outputs/bindings: current.
Calls/effect boundaries: authority_inventory, record.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[1].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:269`; AST `40a755d1de5c6d6150a2c04fc5ff24b03f575aa2cd652e4f6e9b287ccb9e338b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, record, root. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory, record.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[1].value.keywords[0].value.left::Call

Source: `infra/agentinfra/roadmap_inventory.py:269`; AST `0d07ab72302c3fa54e812f7e4776b3a0ad7a9691504ae3bcf664bb5ef3bce73b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value.keywords[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[2]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:270`; AST `34ae11d9e110f914e2062eedab3d328da4b8cd3c8868ef5d6da803bf4682a675`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[2].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:270`; AST `bfa8265e21decd31c404b93e548b4a65da1311211668244a465752e03fdad7bf`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[3]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:271`; AST `3506c1168e00112c24c67a032518efdc904ddb64d33a5f47afdcf068a63e7151`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[3].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:271`; AST `87d50bc3eda6a3d02551eacd7efa8aef422036bd14e37440e3b631a6d56e165b`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[4]::Expr

Source: `infra/agentinfra/roadmap_inventory.py:272`; AST `48bc59b7afe160e7b64a16cf244b22df7b32d89d248ae70dae2154add8ab72c1`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, c, record, require. Outputs/bindings: c.
Calls/effect boundaries: all, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[4].value::Call

Source: `infra/agentinfra/roadmap_inventory.py:272`; AST `81578d5d44425f16b02f9e0db4637dc21c2d8d969d03330ac724c48f108412e0`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, record, require. Outputs/bindings: c.
Calls/effect boundaries: all, require.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap_inventory.py:272`; AST `1b6ac409df0433b9cd49625ebf8ae48e45536d943834470968c498db48f58c73`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, record. Outputs/bindings: c.
Calls/effect boundaries: all.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[4].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_inventory.py:272`; AST `b89281ae62855301e7030a34e910c9787ba0a051b84f6423218974541e16e9cb`.

Rust module: `infra::agentinfra::roadmap_inventory`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, record. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[21].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[5]::Return

Source: `infra/agentinfra/roadmap_inventory.py:274`; AST `b8fe814c7feb249fbd7f0024fee49d999a6a1368dad7b0e408f22dffa496be3d`.

Rust module: `infra::agentinfra::roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Return evaluation at root.body[21].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[5].value.values[3]::Call

Source: `infra/agentinfra/roadmap_inventory.py:275`; AST `f9f296d929a1e508826936efc7fce617bfedb9f8ad37c22ca82a8b5cfec6c85f`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[5].value.values[4]::Call

Source: `infra/agentinfra/roadmap_inventory.py:275`; AST `664755452b4ce05e17cbeca95d2220a1808c91571a00988624968595d3915164`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[5].value.values[5]::Call

Source: `infra/agentinfra/roadmap_inventory.py:276`; AST `35a6aeda0fbc49cdaf3a8a3ea06c8470c884af5680e2239cb8bae2eb7fb9c043`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[5].value.values[6]::Call

Source: `infra/agentinfra/roadmap_inventory.py:276`; AST `a737279aafc7d909a127ebc2675357ce1932abc1449e9e0909cdb70947904a80`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_inventory.py::module::reconcile_inventory::root.body[21].body[5].value.values[7]::Call

Source: `infra/agentinfra/roadmap_inventory.py:277`; AST `fc17d3a53c8a108945d1e66edaf932813bd4b88ca216b2fbdf077823474112af`.

Rust module: `infra::agentinfra::roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, ast, os, pathlib, process, roadmap, roadmap_project, roadmap_records, security, shutil, stat, subprocess, sys, tempfile, time, transaction.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
