# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 252. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/verus_evidence.py::module::root::Module

Source: `infra/agentinfra/verus_evidence.py:1`; AST `0bbf1ec2b67fc52b2630b10cf1c0d981e2b79ff73605282c09658dfe634afb9f`.

Rust module: `infra::agentinfra::verus_evidence`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: MAX_VIR_BYTES, Path, SCHEMA, SimpleNamespace, actual, all, any, argv, artifact, authority, block, body, bool, c, catalog, checked, command, commands, confined_path, declared, digest, entry, expected, external, field, flag, flags, groups, header, ids, inventory, isinstance, k, key, lane, len, log_path, m, mapped, mapped_sites, mode, name, names, obligation, originals, parsed, path, prefix, proof_output, r, re, receipt, require, requirements, root, row, rows, run_id, set, shutil, sorted, source, source_inventory, str, target, text, trusted, value. Outputs/bindings: MAX_VIR_BYTES, SCHEMA, actual, artifact, authority, block, body, c, checked, command, commands, expected, external, field, flag, flags, groups, header, ids, k, key, lane, m, mapped_sites, mode, name, names, originals, parsed, path, prefix, r, requirements, row, rows, source, target, trusted, value.
Calls/effect boundaries: Path, SimpleNamespace, all, any, argv.index, artifact.read_bytes, artifact.read_text, bool, checked.append, confined_path, digest, flags.values, inventory, isinstance, len, log_path, name.startswith, name[1].startswith, names.add, path.is_file, path.read_text, path.stat, path.unlink, proof_output, re.match, re.search, re.split, receipt.get, require, row['applicability_rationale'].strip, row['execution_obligation']['relation'].strip, row['relation'].strip, row['review'].strip, set, shutil.copyfile, sorted, target.parent.mkdir, target.read_bytes, text.encode, trusted.append, value['artifact'].startswith.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::root.body[0]::Expr

Source: `infra/agentinfra/verus_evidence.py:1`; AST `fe6ddfe5eaaad866848a92a6d9d8f789f4d209813c0463d2272ac273a5b118f5`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/verus_evidence.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::root.body[2]::Import

Source: `infra/agentinfra/verus_evidence.py:7`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::root.body[3]::Import

Source: `infra/agentinfra/verus_evidence.py:8`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/verus_evidence.py:10`; AST `d7ba5c5ab38c86b38cd0f11dda549ca5371a85045fe074ec9b009f610f86a3d0`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/verus_evidence.py:11`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::root.body[6]::Assign

Source: `infra/agentinfra/verus_evidence.py:13`; AST `7be780d899467d16380883c4db790f39703583454c1a8cd657b28cb0d30f1078`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: SCHEMA.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::root.body[7]::Assign

Source: `infra/agentinfra/verus_evidence.py:14`; AST `690b679233dea65e8bd2201877c153bee6426608e00675903d5d44df4b4cdb0e`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: MAX_VIR_BYTES.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8]::FunctionDef

Source: `infra/agentinfra/verus_evidence.py:16`; AST `2a4376e23b323787fea9c5cf34dc870564fd0f067348a71554914f8129827d67`.

Rust module: `infra::agentinfra::verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: MAX_VIR_BYTES, Path, SCHEMA, any, block, body, bool, checked, entry, external, flag, flags, header, isinstance, len, mode, name, names, prefix, r, re, require, row, set, sorted, str, text, trusted. Outputs/bindings: block, body, checked, external, flag, flags, header, mode, name, names, prefix, row, trusted.
Calls/effect boundaries: Path, any, bool, checked.append, flags.values, isinstance, len, name[1].startswith, names.add, re.match, re.search, re.split, require, set, sorted, text.encode, trusted.append.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[0]::Expr

Source: `infra/agentinfra/verus_evidence.py:17`; AST `591fa89f196efe3d48d43a100d3eba030bc5fead0f36adc9b4414cb2d5b35e15`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: MAX_VIR_BYTES, isinstance, len, require, str, text. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, len, require, text.encode.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:17`; AST `5df2ec559dd00b26d2496295804aeefcce690a599dffb4bf6f4ea4e9ae804455`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: MAX_VIR_BYTES, isinstance, len, require, str, text. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, len, require, text.encode.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/verus_evidence.py:17`; AST `8602de97d26ce8f584f522a71d3560bc9f98529c4e6c60e68fb82c2bad05fca6`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, str, text. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/verus_evidence.py:17`; AST `80addfdec0c38cd7341886bb1209ec18f446f05b1002e3bd0df467b6fcd56902`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, text. Outputs/bindings: (none).
Calls/effect boundaries: len, text.encode.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[0].value.args[0].values[1].left.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:17`; AST `7b01d8402eaa68fa08a88ea0fe995d452426cfe6dabb2459ddbcf08758697095`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: text.encode.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[1]::Expr

Source: `infra/agentinfra/verus_evidence.py:21`; AST `51eb8f7e870ffc79785ff061588bcea4576e58e211d4031df4eb76a12e30e9aa`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: re, require, text. Outputs/bindings: (none).
Calls/effect boundaries: re.search, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[1].value::Call

Source: `infra/agentinfra/verus_evidence.py:21`; AST `a1701ade964f9c54a98cb36d11ddf8e699d27df969d07a811ab1cdb747d908ec`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re, require, text. Outputs/bindings: (none).
Calls/effect boundaries: re.search, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[1].value.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:21`; AST `3eceffbd0e832ec739ff5613865a855cc5c930d142c03d4ccc4d94ecee93800f`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re, text. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[2]::Assign

Source: `infra/agentinfra/verus_evidence.py:23`; AST `3fb30a24a2008cb78a8429aab63008b90d49879ae41386534e37e8d6e4ead567`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, entry. Outputs/bindings: prefix.
Calls/effect boundaries: Path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[2].value.left.value::Call

Source: `infra/agentinfra/verus_evidence.py:23`; AST `08c3016fd5cf392392f78965f22ff52614a73b57f78325955a79d66d01c9592e`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, entry. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].value.left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[3]::Assign

Source: `infra/agentinfra/verus_evidence.py:24`; AST `c008b91a204b2ee2c431cb501f1dd07b8df7653e2dd4e9189e01ea74a8fbd681`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: checked, names, trusted.
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[3].value.elts[2]::Call

Source: `infra/agentinfra/verus_evidence.py:24`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4]::For

Source: `infra/agentinfra/verus_evidence.py:25`; AST `cde9f2119642816742fba842ae0bc0fade490cf138c142ada1435446c2052f90`.

Rust module: `infra::agentinfra::verus_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: any, block, body, bool, checked, external, flag, flags, header, mode, name, names, prefix, re, require, row, text, trusted. Outputs/bindings: block, body, external, flag, flags, header, mode, name, row.
Calls/effect boundaries: any, bool, checked.append, flags.values, name[1].startswith, names.add, re.match, re.search, re.split, require, trusted.append.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered For evaluation at root.body[8].body[4]; no call, error or mutation may be omitted. Iteration: block in re.split('(?m)(?=^\\(@ )', text)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].iter::Call

Source: `infra/agentinfra/verus_evidence.py:25`; AST `38960e5f82f0bb1adcc0af37671b34ff8bd9913d96a143d6533936541d9c5672`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re, text. Outputs/bindings: (none).
Calls/effect boundaries: re.split.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[0]::Assign

Source: `infra/agentinfra/verus_evidence.py:26`; AST `89e22860c2cfb78b84a2d331bb24a81254026bab23860444c02a5b0aa77cf3c0`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: block, re. Outputs/bindings: header.
Calls/effect boundaries: re.match.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:26`; AST `7c28599c76b355575e4aa76c950ffa79b2ceab75d7cb695baffaf1e0f3ed5e55`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: block, re. Outputs/bindings: (none).
Calls/effect boundaries: re.match.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[1]::If

Source: `infra/agentinfra/verus_evidence.py:27`; AST `1b4e7a47f4b557edc39cbebaf8f7af46c65aac91f154f55db19594c493b07705`.

Rust module: `infra::agentinfra::verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: header. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered If evaluation at root.body[8].body[4].body[1]; no call, error or mutation may be omitted. Condition: not header
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[1].body[0]::Continue

Source: `infra/agentinfra/verus_evidence.py:28`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Continue evaluation at root.body[8].body[4].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[2]::Assign

Source: `infra/agentinfra/verus_evidence.py:29`; AST `20e0b66c5bb865ead194418042d03b42186433af6b5316204a34e232d5d1b153`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: block, re. Outputs/bindings: name.
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[2].value::Call

Source: `infra/agentinfra/verus_evidence.py:29`; AST `0508fff9d0bf96268488aa636280c12910b7a4a8d7be208414659d11c851bcb5`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: block, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[3]::Expr

Source: `infra/agentinfra/verus_evidence.py:30`; AST `b5a80dfe41abf3fcd06a6bf06f78f9a9fe9a138ada229c4368f6bdc19930ad58`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[3].value::Call

Source: `infra/agentinfra/verus_evidence.py:30`; AST `c1e3bea3a665b62a3b20da6edb68914f14422d70242ab30141ee99ba6289e50b`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[4]::If

Source: `infra/agentinfra/verus_evidence.py:31`; AST `8e5a0a5433d8ee02ee9354901634a5baf07cf2086d85d55020230bfafb9ccd5f`.

Rust module: `infra::agentinfra::verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: name, prefix. Outputs/bindings: (none).
Calls/effect boundaries: name[1].startswith.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered If evaluation at root.body[8].body[4].body[4]; no call, error or mutation may be omitted. Condition: not name[1].startswith(prefix)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[4].test.operand::Call

Source: `infra/agentinfra/verus_evidence.py:31`; AST `7d3a29372d9f5e1dbd5b99f875152162d5acbf6d4c0689dd35d88c445eea2323`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, prefix. Outputs/bindings: (none).
Calls/effect boundaries: name[1].startswith.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[4].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[4].body[0]::Continue

Source: `infra/agentinfra/verus_evidence.py:32`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Continue evaluation at root.body[8].body[4].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[5]::Assign

Source: `infra/agentinfra/verus_evidence.py:33`; AST `a89425e159cfe536c389baf56537d375fafbd5bba1c458c1c9a6a572f108710b`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: block, re. Outputs/bindings: mode.
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[5].value::Call

Source: `infra/agentinfra/verus_evidence.py:33`; AST `545f86401e71da430b296bc71e8394d18124b6aae7afecbb8b9e1c922964011b`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: block, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[6]::Assign

Source: `infra/agentinfra/verus_evidence.py:34`; AST `b1fd110648305c57c487bb5d7f5e2dce0984622d9acf9a9f7ff7d39ebab1caeb`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: block, re. Outputs/bindings: external.
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[6].value::Call

Source: `infra/agentinfra/verus_evidence.py:34`; AST `636118e2d172e15e48e5d210c3895adc4cad92f86bdab207efe9c4842b22c288`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: block, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[7]::Assign

Source: `infra/agentinfra/verus_evidence.py:35`; AST `1b2b802ddf81ad811024751ec0bf2022e9b74b07c11fa107ae9b860dc17adfdf`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: block, re. Outputs/bindings: body.
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[7].value::Call

Source: `infra/agentinfra/verus_evidence.py:35`; AST `270b0fe82d8c0b1700225c5f2858b45408668dad6522ab90fb9460f550c4532a`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: block, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[8]::Expr

Source: `infra/agentinfra/verus_evidence.py:36`; AST `2e41c1b3d2bb9884e22c01952c17a4fd50b3a92b16238d88525d6347e6bc542b`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: body, external, mode, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[8].value::Call

Source: `infra/agentinfra/verus_evidence.py:36`; AST `674faaa421aef4e455e2dfd72827f07201ca4e06bbf218bfb694bd77215c0263`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: body, external, mode, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[9]::Expr

Source: `infra/agentinfra/verus_evidence.py:37`; AST `5802c1cf40c7a1bc4e2eb7d6ac6e8e8c46c2cb81e5c858c0286cc233781aa124`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, names, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[9].value::Call

Source: `infra/agentinfra/verus_evidence.py:37`; AST `3919c466ef10bbc2b3941556add8c857fd61cffa46ec2e830e2beec92e00b39c`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, names, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[10]::Expr

Source: `infra/agentinfra/verus_evidence.py:38`; AST `a31492d132b6c3781d8f9ad0f67734c1931e9e3db5a516f9a926ca3a4d243741`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, names. Outputs/bindings: (none).
Calls/effect boundaries: names.add.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[10].value::Call

Source: `infra/agentinfra/verus_evidence.py:38`; AST `30ab71a20465393d18022397cac511cc9091da212b144ebb4563f47342f94155`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, names. Outputs/bindings: (none).
Calls/effect boundaries: names.add.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[11]::Assign

Source: `infra/agentinfra/verus_evidence.py:39`; AST `9488bd6c20e9a28c1d39e16303490a812a372e1ed5b54f91e6412a6d45aedd59`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: block, bool, flag, re. Outputs/bindings: flag, flags.
Calls/effect boundaries: bool, re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[11].value::DictComp

Source: `infra/agentinfra/verus_evidence.py:39`; AST `04bf7792f35726e06cb4e824c30be77103d2b3a8bc748da4f930c514a5490c49`.

Rust module: `infra::agentinfra::verus_evidence`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: block, bool, flag, re. Outputs/bindings: flag.
Calls/effect boundaries: bool, re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered DictComp evaluation at root.body[8].body[4].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[11].value.value::Call

Source: `infra/agentinfra/verus_evidence.py:39`; AST `25213207ecc0e1be61d2c6a9107d0819590d6fd8e51baff80697d5d9c7e3f216`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: block, bool, flag, re. Outputs/bindings: (none).
Calls/effect boundaries: bool, re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[11].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[11].value.value.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:39`; AST `a5e4dc8f3a838e69e6524c618a0e781baeabcc713d454830e5e93bd4dd605cf1`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: block, flag, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[11].value.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[12]::Assign

Source: `infra/agentinfra/verus_evidence.py:41`; AST `70f6f74cd68182c7371ac7dedb7e0f99762b6759d49a56644a7e518e26ccc9e5`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: body, external, flags, header, mode, name. Outputs/bindings: row.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[4].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13]::If

Source: `infra/agentinfra/verus_evidence.py:43`; AST `93bf2d71b36a3fb2b4fbe8f55aeef180a7e467a3eb9c7b4d2a63f030748c224c`.

Rust module: `infra::agentinfra::verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, block, checked, flags, re, require, row, trusted. Outputs/bindings: (none).
Calls/effect boundaries: any, checked.append, flags.values, re.search, require, trusted.append.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered If evaluation at root.body[8].body[4].body[13]; no call, error or mutation may be omitted. Condition: row['external_body']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].body[0]::Expr

Source: `infra/agentinfra/verus_evidence.py:44`; AST `252a13a89e9d3030fff4d3d671faec82d74f1d0e9a8d50c0e3bbf4982af0d7e5`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: row, trusted. Outputs/bindings: (none).
Calls/effect boundaries: trusted.append.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:44`; AST `16f82ed6a9cf5006615688b79e006857c564e66d78fcc39e5b8c934bc2ab5266`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row, trusted. Outputs/bindings: (none).
Calls/effect boundaries: trusted.append.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0]::If

Source: `infra/agentinfra/verus_evidence.py:45`; AST `46f5acf789daa267a3693da000a8061ba3ef2d7854e8a72b083170832a5ebed0`.

Rust module: `infra::agentinfra::verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, block, checked, flags, re, require, row. Outputs/bindings: (none).
Calls/effect boundaries: any, checked.append, flags.values, re.search, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered If evaluation at root.body[8].body[4].body[13].orelse[0]; no call, error or mutation may be omitted. Condition: row['mode'] in ('Proof', 'Exec')
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[0]::Expr

Source: `infra/agentinfra/verus_evidence.py:46`; AST `3bd9dfc5ed05e1935f795abf5100c188178814d1d4a43331078e2e0953a8bb22`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, row. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[13].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:46`; AST `46fe1e46c9f549615d5bd71843c4814caec594072ced40015fe43980b8bed6e6`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, row. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[13].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[1]::Expr

Source: `infra/agentinfra/verus_evidence.py:47`; AST `2d8977e9fb25f69255f9b3b4fde2e5d509343efb1009a8dfe8dad85b0e9d0e62`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, flags, require. Outputs/bindings: (none).
Calls/effect boundaries: any, flags.values, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[13].orelse[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[1].value::Call

Source: `infra/agentinfra/verus_evidence.py:47`; AST `d14a758719eac30ba47abab067a4ee38fc14d08b84440ead171b74776cac635c`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, flags, require. Outputs/bindings: (none).
Calls/effect boundaries: any, flags.values, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[13].orelse[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[1].value.args[0].operand::Call

Source: `infra/agentinfra/verus_evidence.py:47`; AST `0437be180003ef7cb7176e56401ad44778e399b94383459e74f942296cde4476`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, flags. Outputs/bindings: (none).
Calls/effect boundaries: any, flags.values.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[13].orelse[0].body[1].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[1].value.args[0].operand.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:47`; AST `4c6396ce3421894f38437d3b2e04fafb2c05139d12212091f4e6072e91905965`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: flags. Outputs/bindings: (none).
Calls/effect boundaries: flags.values.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[13].orelse[0].body[1].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[2]::Expr

Source: `infra/agentinfra/verus_evidence.py:48`; AST `fa53b369e5ccf4fe2d3ce450a3a65c4be65aba2c6173d6e64b32846d871ef55d`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: block, re, require. Outputs/bindings: (none).
Calls/effect boundaries: re.search, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[13].orelse[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[2].value::Call

Source: `infra/agentinfra/verus_evidence.py:48`; AST `addb11999ac1e4d7a05ab861638c166e3c0351cdf46c725def06bed39bd94a06`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: block, re, require. Outputs/bindings: (none).
Calls/effect boundaries: re.search, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[13].orelse[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[2].value.args[0].operand::Call

Source: `infra/agentinfra/verus_evidence.py:48`; AST `2432798d4cee0d774e93a3b4855c8ce9f0602476ecc0a795a340d5b846f02ae1`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: block, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[13].orelse[0].body[2].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[3]::Expr

Source: `infra/agentinfra/verus_evidence.py:50`; AST `1bb70f01c985e3b628be35acbe721bf10b239446d1dccab4666deea62eb9addb`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked, row. Outputs/bindings: (none).
Calls/effect boundaries: checked.append.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4].body[13].orelse[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[4].body[13].orelse[0].body[3].value::Call

Source: `infra/agentinfra/verus_evidence.py:50`; AST `d40128e3c6e2a882d197d60394aca4f61244ea34126c201dc7db21cc2b7e8ded`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked, row. Outputs/bindings: (none).
Calls/effect boundaries: checked.append.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].body[13].orelse[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[5]::Expr

Source: `infra/agentinfra/verus_evidence.py:51`; AST `0cae50f594ce69110d9f36a3a659828b98701b12b9f9d6f5ed20ed1b1cfc6974`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[5].value::Call

Source: `infra/agentinfra/verus_evidence.py:51`; AST `8a77675dc0f5b7feca68a7d2bc5895d59d79159a0366ee7b8eee25f0a5b78f0c`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[6]::Return

Source: `infra/agentinfra/verus_evidence.py:52`; AST `fadfba1d6b1a078582bac90687d4370754ca6020f1ac5f5280e56996db49f0f7`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SCHEMA, checked, entry, r, re, sorted, text, trusted. Outputs/bindings: (none).
Calls/effect boundaries: re.search, sorted.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Return evaluation at root.body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[6].value.values[2]::Call

Source: `infra/agentinfra/verus_evidence.py:52`; AST `8302d24fa3d823cfc866689f2a700cf073004376b15607ceced9739f2ffe78d4`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked, r, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[6].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[6].value.values[2].keywords[0].value::Lambda

Source: `infra/agentinfra/verus_evidence.py:52`; AST `5e09ba0a653568bd90b4fa539998150426b5529ba90c1f320a13cd64e1acc273`.

Rust module: `infra::agentinfra::verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Lambda evaluation at root.body[8].body[6].value.values[2].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[6].value.values[3]::Call

Source: `infra/agentinfra/verus_evidence.py:53`; AST `14e86d2812a6188a8d5d457fe70888209f0a139f96289921a859f04edfaea89a`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, sorted, trusted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[6].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[6].value.values[3].keywords[0].value::Lambda

Source: `infra/agentinfra/verus_evidence.py:53`; AST `5e09ba0a653568bd90b4fa539998150426b5529ba90c1f320a13cd64e1acc273`.

Rust module: `infra::agentinfra::verus_evidence`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Lambda evaluation at root.body[8].body[6].value.values[3].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::inventory::root.body[8].body[6].value.values[4].value::Call

Source: `infra/agentinfra/verus_evidence.py:54`; AST `f5a95ccd5bdfebf66db27f498541144fb9226a002fd944184a32648e4ebddb7b`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re, text. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[8].body[6].value.values[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9]::FunctionDef

Source: `infra/agentinfra/verus_evidence.py:56`; AST `472825eef963dcf8afe954298e213e42642a4db37883561065c381d8bedc880a`.

Rust module: `infra::agentinfra::verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: argv, confined_path, name, require, root. Outputs/bindings: name.
Calls/effect boundaries: argv.index, confined_path, name.startswith, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[0]::If

Source: `infra/agentinfra/verus_evidence.py:57`; AST `0fe064ddd2f11d8d2a87fff561b75907d6d8fdf9af2a38cd6653f55e6782ccbd`.

Rust module: `infra::agentinfra::verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: argv. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered If evaluation at root.body[9].body[0]; no call, error or mutation may be omitted. Condition: '--log' not in argv or '--log-dir' not in argv
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[0].body[0]::Return

Source: `infra/agentinfra/verus_evidence.py:58`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Return evaluation at root.body[9].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[1]::Expr

Source: `infra/agentinfra/verus_evidence.py:59`; AST `55d5d633008c00cd3d22a00ace6c672809b58c288f03f7464a91f1fd15ee6757`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, require. Outputs/bindings: (none).
Calls/effect boundaries: argv.index, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[1].value::Call

Source: `infra/agentinfra/verus_evidence.py:59`; AST `21a38e831277a08531991a4a6062c3651017fda0f5e2077277c4c7dbeb28cf16`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, require. Outputs/bindings: (none).
Calls/effect boundaries: argv.index, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[1].value.args[0].left.slice.left::Call

Source: `infra/agentinfra/verus_evidence.py:59`; AST `1147aa64f33f311108f8e2593533c4538577d1245f6f50b87ad834cff3376c9b`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv. Outputs/bindings: (none).
Calls/effect boundaries: argv.index.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value.args[0].left.slice.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[2]::Assign

Source: `infra/agentinfra/verus_evidence.py:60`; AST `cd3e4ac6a250d567ec1af97424297bcae00f0db94b330e288e16a2587598a059`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv. Outputs/bindings: name.
Calls/effect boundaries: argv.index.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[2].value.slice.left::Call

Source: `infra/agentinfra/verus_evidence.py:60`; AST `857377c7ec6d7dda684f96972c1dbb2e23fca44a830e69ed76b475035308cf52`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv. Outputs/bindings: (none).
Calls/effect boundaries: argv.index.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].value.slice.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[3]::Expr

Source: `infra/agentinfra/verus_evidence.py:61`; AST `416ad9c463e656ea3c59f024ac1ec0eea15755cd9d24262beaf41bf617cbf90c`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, require. Outputs/bindings: (none).
Calls/effect boundaries: name.startswith, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[3].value::Call

Source: `infra/agentinfra/verus_evidence.py:61`; AST `304c74e50252620b1dde7ee460de5c4a967eb8dcdc4510e659668536d7a2f3df`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, require. Outputs/bindings: (none).
Calls/effect boundaries: name.startswith, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[3].value.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:61`; AST `4e1a137c76437cfaab5c3d84866ccfb2baa16e297eba341c024774373c46c038`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.startswith.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[4]::Return

Source: `infra/agentinfra/verus_evidence.py:62`; AST `f53a99e6fed84686d81e2fe591bf4f1b3a49edcd0bb984e8b581df6eeb7eaf5c`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Return evaluation at root.body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::log_path::root.body[9].body[4].value::Call

Source: `infra/agentinfra/verus_evidence.py:62`; AST `27f4b76b49df2038277261ba7b99886d82f74ecdf0944a9b8d9891ce9f7c4d6c`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::prepare_log::root.body[10]::FunctionDef

Source: `infra/agentinfra/verus_evidence.py:64`; AST `f662598e9b8e7ea110c5ec4ab1d021d4b6124518456c072d7c484bb0929751b9`.

Rust module: `infra::agentinfra::verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: argv, log_path, path, root. Outputs/bindings: path.
Calls/effect boundaries: log_path, path.unlink.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::prepare_log::root.body[10].body[0]::Assign

Source: `infra/agentinfra/verus_evidence.py:65`; AST `9563a317e2b45a33a58751b48b471f544cd338c033f3509e6b10885127681395`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, log_path, root. Outputs/bindings: path.
Calls/effect boundaries: log_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::prepare_log::root.body[10].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:65`; AST `fa209d2a79104e9af25524f11b0ec5a592f78c0cbf220959773910988e62f616`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, log_path, root. Outputs/bindings: (none).
Calls/effect boundaries: log_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::prepare_log::root.body[10].body[1]::If

Source: `infra/agentinfra/verus_evidence.py:66`; AST `fdcac20015079a3e149f32b9faa4c5a1893e0d1aaddc793d23ef1d0a99f601b5`.

Rust module: `infra::agentinfra::verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.unlink.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered If evaluation at root.body[10].body[1]; no call, error or mutation may be omitted. Condition: path is not None
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::prepare_log::root.body[10].body[1].body[0]::Expr

Source: `infra/agentinfra/verus_evidence.py:68`; AST `1a3e2bd93bb9ff2dadd301e73083350e612c7804c2cfe200859953ebc393cf59`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.unlink.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::prepare_log::root.body[10].body[1].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:68`; AST `fdafd60c5264fbca4fa9066d77d601f95e76d97d7929480b85dd70e6cbb98a9b`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.unlink.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11]::FunctionDef

Source: `infra/agentinfra/verus_evidence.py:70`; AST `d451972674fd161083fcb83c6ca6df85b7b26d9164ebfce8d4a10f5502f1b693`.

Rust module: `infra::agentinfra::verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: MAX_VIR_BYTES, argv, artifact, confined_path, digest, inventory, log_path, parsed, path, require, root, run_id, shutil, target. Outputs/bindings: artifact, parsed, path, target.
Calls/effect boundaries: confined_path, digest, inventory, log_path, path.is_file, path.read_text, path.stat, require, shutil.copyfile, target.parent.mkdir, target.read_bytes.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[0]::Assign

Source: `infra/agentinfra/verus_evidence.py:71`; AST `9563a317e2b45a33a58751b48b471f544cd338c033f3509e6b10885127681395`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, log_path, root. Outputs/bindings: path.
Calls/effect boundaries: log_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:71`; AST `fa209d2a79104e9af25524f11b0ec5a592f78c0cbf220959773910988e62f616`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, log_path, root. Outputs/bindings: (none).
Calls/effect boundaries: log_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[1]::If

Source: `infra/agentinfra/verus_evidence.py:72`; AST `f31b4e8eebe74372e7eb8cf402112fb33b59ce72f87c335281d167d4588dad18`.

Rust module: `infra::agentinfra::verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_file.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered If evaluation at root.body[11].body[1]; no call, error or mutation may be omitted. Condition: path is None or not path.is_file()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[1].test.values[1].operand::Call

Source: `infra/agentinfra/verus_evidence.py:72`; AST `d2081c59f0765455ac12b468dbfc8371bdf81a7d49d474e10d779496c1e121ac`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_file.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[1].body[0]::Return

Source: `infra/agentinfra/verus_evidence.py:73`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Return evaluation at root.body[11].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[2]::Expr

Source: `infra/agentinfra/verus_evidence.py:74`; AST `d0234849d2eb8584efe60a79773fe2423987a00ed2d59756d43db48351f519a7`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: MAX_VIR_BYTES, path, require. Outputs/bindings: (none).
Calls/effect boundaries: path.stat, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[2].value::Call

Source: `infra/agentinfra/verus_evidence.py:74`; AST `466ea8f6460971e233922b5fcc2a9d5434c5e84f4bcf4d9b7fcac93f79b2d700`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: MAX_VIR_BYTES, path, require. Outputs/bindings: (none).
Calls/effect boundaries: path.stat, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[2].value.args[0].left.value::Call

Source: `infra/agentinfra/verus_evidence.py:74`; AST `4ad13a92d4c0491c8737b8fcfacd38c225911ac2f24bdb5ec5c2f1fd76d4a178`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[3]::Assign

Source: `infra/agentinfra/verus_evidence.py:75`; AST `2b20fdce10e0bb01bc420a39e7452f8c803263a47f3acf0728b0423fb13fb97d`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, inventory, path. Outputs/bindings: parsed.
Calls/effect boundaries: inventory, path.read_text.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[3].value::Call

Source: `infra/agentinfra/verus_evidence.py:75`; AST `cc35fb968f3d658430a1e309387da80c763429b470a6d4fba259b87d33e360e1`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, inventory, path. Outputs/bindings: (none).
Calls/effect boundaries: inventory, path.read_text.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[3].value.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:75`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[4]::Assign

Source: `infra/agentinfra/verus_evidence.py:76`; AST `8e87e9c44b258fc2616cd57bae15d1c6f102fc3cd16fef44071d8db5c8b461ab`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: run_id. Outputs/bindings: artifact.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[5]::Assign

Source: `infra/agentinfra/verus_evidence.py:77`; AST `0a4e34ef6b62e33e1fca1f2c88117b76eb6a51488ada6765e60d3f89f5de14ef`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifact, confined_path, root. Outputs/bindings: target.
Calls/effect boundaries: confined_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[5].value::Call

Source: `infra/agentinfra/verus_evidence.py:77`; AST `30cb3ab5d65e3a7ab8b5fcf8cbfa8c667aae2be2116734e34041d21435cb8875`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifact, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[6]::Expr

Source: `infra/agentinfra/verus_evidence.py:78`; AST `e28cb5b2a9367313ba3b6470f9081a2b8186dd82dbfeec416a8d5f23d955b886`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.parent.mkdir.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[6].value::Call

Source: `infra/agentinfra/verus_evidence.py:78`; AST `58c379428a4dcb05097164e1e9cd0aa827bbb5a613fe07fceba4b6c0e390d1c9`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.parent.mkdir.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[7]::Expr

Source: `infra/agentinfra/verus_evidence.py:79`; AST `9ba1329134773f2965aed58630bfb5a3cecd999370fb8f35c27d34fd299cdca6`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, shutil, target. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[7].value::Call

Source: `infra/agentinfra/verus_evidence.py:79`; AST `4f488c2a3c16a9e28ae89d68abb05510039eb56512a19c3c6dc252f74d60a4f1`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, shutil, target. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[8]::Return

Source: `infra/agentinfra/verus_evidence.py:80`; AST `aa1cdc6c6a14114050b9ad39612d586cc131c8c0282e40279791150d595b6a5f`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifact, digest, parsed, target. Outputs/bindings: (none).
Calls/effect boundaries: digest, target.read_bytes.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Return evaluation at root.body[11].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[8].value.values[2]::Call

Source: `infra/agentinfra/verus_evidence.py:80`; AST `3ad3dee046217dc4ee3b2f99ccda41115ef05e1a3ddb207b6c8951280bee2830`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, target. Outputs/bindings: (none).
Calls/effect boundaries: digest, target.read_bytes.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::capture::root.body[11].body[8].value.values[2].args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:80`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].value.values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12]::FunctionDef

Source: `infra/agentinfra/verus_evidence.py:82`; AST `ad30bab0f5d4e8d7d86e49a6ad8f097024ef25f0594d5061434067ed7c84a480`.

Rust module: `infra::agentinfra::verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: SCHEMA, SimpleNamespace, actual, all, any, artifact, c, command, commands, confined_path, digest, inventory, k, key, len, obligation, proof_output, receipt, require, root, set, value. Outputs/bindings: actual, artifact, c, command, commands, k, key, value.
Calls/effect boundaries: SimpleNamespace, all, any, artifact.read_bytes, artifact.read_text, confined_path, digest, inventory, len, proof_output, receipt.get, require, set, value['artifact'].startswith.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[0]::ImportFrom

Source: `infra/agentinfra/verus_evidence.py:83`; AST `9506afda020e7ed6bc6b6b044d0562a6810aa0b91bca19d190635df64a8b3aa5`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[1]::ImportFrom

Source: `infra/agentinfra/verus_evidence.py:84`; AST `271cd8a5819453f6952690fd43e9ce152386df249c8de9a1999907454b0006b7`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[2]::Expr

Source: `infra/agentinfra/verus_evidence.py:85`; AST `2c995a64fcf620bc243583ab84b6ce1ad559ee3eb9e99b5734840a1a4114def5`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[2].value::Call

Source: `infra/agentinfra/verus_evidence.py:85`; AST `bb97ba026777f712dcc27d9e043079e4a50ceab5be839534f937e877e8e2f6e0`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[3]::Expr

Source: `infra/agentinfra/verus_evidence.py:86`; AST `0f60c8dd2ade08a6189281707f2bac39ee2830a8062fc5cb411d6b2987146267`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[3].value::Call

Source: `infra/agentinfra/verus_evidence.py:86`; AST `e1195f623291aeb96599627cbed4956600bc42df279bb8ddedfcba1258310cc6`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[4]::Expr

Source: `infra/agentinfra/verus_evidence.py:87`; AST `0db04afebee7c1d2dd13e4e4e8b83080e0850553cfc506a4f1c14a483e68ed10`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[4].value::Call

Source: `infra/agentinfra/verus_evidence.py:87`; AST `9807deb65aca4fed656f442a3a7f5d3356ef52dbb5a44883c175cd23c9294db0`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[5]::Assign

Source: `infra/agentinfra/verus_evidence.py:90`; AST `b6a8c66f324bcfbff7feb3f5b16ab705a85346b4488b561ba4d5ef2a1b0620a3`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: commands.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[6]::Expr

Source: `infra/agentinfra/verus_evidence.py:91`; AST `9506b1232d0fd475a5910aeb7297c359e078d7251e61288deaa5f89ad2d3b60b`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, commands, len, receipt, require. Outputs/bindings: c.
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[6].value::Call

Source: `infra/agentinfra/verus_evidence.py:91`; AST `a5bb5c686f2e579f146bdc1f5e930cd163530e628bec2342892636cc8eb308bd`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, commands, len, receipt, require. Outputs/bindings: c.
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/verus_evidence.py:91`; AST `320f1f02e509b145c08c887496907f9115c569cfe076ee3504266ee643de94dc`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: commands, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[6].value.args[0].values[1].left::ListComp

Source: `infra/agentinfra/verus_evidence.py:91`; AST `74612d84d772f805d86e17fc16a85e01eb3c5ab1322e38c50b7361b90c52d2f4`.

Rust module: `infra::agentinfra::verus_evidence`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: c, commands. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[6].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[7]::Assign

Source: `infra/agentinfra/verus_evidence.py:92`; AST `8df249cc9828a621bafb4a15d035b033d6fbb8462f8de338b8e1042d2b4b3798`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: commands. Outputs/bindings: command.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[8]::Expr

Source: `infra/agentinfra/verus_evidence.py:93`; AST `a5c0733066fa86ce6fc66230c70087f7863700aa2b57a2779bc1aa1b78943b5c`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, command, k, require. Outputs/bindings: k.
Calls/effect boundaries: any, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[8].value::Call

Source: `infra/agentinfra/verus_evidence.py:93`; AST `0449b0eef10874313360690a599074b6c5a6d48864c8053f5894db820f815cbf`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, command, k, require. Outputs/bindings: k.
Calls/effect boundaries: any, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[8].value.args[0].values[1].operand::Call

Source: `infra/agentinfra/verus_evidence.py:93`; AST `d01a29b31344ad5a078e0e17bfcea9cc9c79f576f0075645008c61d736284056`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, command, k. Outputs/bindings: k.
Calls/effect boundaries: any.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.args[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[8].value.args[0].values[1].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/verus_evidence.py:93`; AST `e3c8a7a0a991e0584bb44da1bef01b667a159bf94b4ef2e108271dc5c8632553`.

Rust module: `infra::agentinfra::verus_evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: command, k. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[8].value.args[0].values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[9]::Expr

Source: `infra/agentinfra/verus_evidence.py:95`; AST `d018558b33d505ac75d748bdbe48177ac72cdfcd2e4364cbc22347d4cab334d0`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: command, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[9].value::Call

Source: `infra/agentinfra/verus_evidence.py:95`; AST `61695b6cf7603c6ff75d320d94bb0d6320e40b3208f0520d766fa14647acecbf`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: command, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[9].value.args[0].operand.left::Call

Source: `infra/agentinfra/verus_evidence.py:95`; AST `598d75558fc9ebececdc8967220984c8adcb122d8c737521198a6e8f06429368`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: command, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].operand.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[10]::Expr

Source: `infra/agentinfra/verus_evidence.py:97`; AST `617bdf9f2b5c8c05cf7196c6b268396f1264dc9931c6c0d479eb59f828ffd44e`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SimpleNamespace, command, proof_output, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace, proof_output, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[10].value::Call

Source: `infra/agentinfra/verus_evidence.py:97`; AST `2af5eb1bd08c8b84b1ba6e4e7bd2e5e6ba3ad1305741012221ba4f7f228e7e4d`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace, command, proof_output, receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace, proof_output, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[10].value.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:97`; AST `8c97885430c416e363ee5d4ce1643720ce8dc5b55f0c97437c82d7534d6ae073`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace, command, proof_output, receipt. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace, proof_output.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[10].value.args[0].args[1]::Call

Source: `infra/agentinfra/verus_evidence.py:97`; AST `a5376eb9a27d3044fef92f8a52bca30030fc709d75b245b15f86ab9683d80293`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace, command. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[11]::Assign

Source: `infra/agentinfra/verus_evidence.py:98`; AST `94330f91c75e062692259c436583c72aea19d7f7025ddddc39e551106e248b4d`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: value.
Calls/effect boundaries: receipt.get.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[11].value::Call

Source: `infra/agentinfra/verus_evidence.py:98`; AST `21140c691b6d29ac2d4e9db97f132c69fec87108cedf2c0f13265a1d0b9d7d7a`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: receipt.get.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[12]::Expr

Source: `infra/agentinfra/verus_evidence.py:99`; AST `e5b3b65c00dea79ab0f917bb0c9c4591c5a49d7b052b8025b05a92bb36e79093`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SCHEMA, obligation, require, value. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[12].value::Call

Source: `infra/agentinfra/verus_evidence.py:99`; AST `41d2dfe3cc39a051bae3e01c9e31299b9f9aa742a45ca4bafe3fb2f9bb19df66`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SCHEMA, obligation, require, value. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[13]::Assign

Source: `infra/agentinfra/verus_evidence.py:100`; AST `f6115b5bb8a67d9cd3ffd64400fefbbd577bbf35952a2a3db420b80e2d048afe`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, root, value. Outputs/bindings: artifact.
Calls/effect boundaries: confined_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[13].value::Call

Source: `infra/agentinfra/verus_evidence.py:100`; AST `544d795946b64437526940321413dbe8c9e802839e6740a886e8198f3e96bac5`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, value. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[14]::Expr

Source: `infra/agentinfra/verus_evidence.py:101`; AST `17b202d5fb6dd136b0c74ab30e2957086e063cdaaeb796756e70960154295651`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, value. Outputs/bindings: (none).
Calls/effect boundaries: require, value['artifact'].startswith.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[14].value::Call

Source: `infra/agentinfra/verus_evidence.py:101`; AST `53d501a907dd8708893191d256db99d6e3725f9e494eda548f3c7b1854877cbe`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, value. Outputs/bindings: (none).
Calls/effect boundaries: require, value['artifact'].startswith.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[14].value.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:101`; AST `45d87960a4843e02631631a5bb6190251fdcccaf6a884f6fde20b3656c33be71`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: value['artifact'].startswith.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[15]::Expr

Source: `infra/agentinfra/verus_evidence.py:102`; AST `7e04f1bbf489ed59932e06b6189696756cf77f8917bd21aca8ff15ee4fc3ce5a`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifact, digest, require, value. Outputs/bindings: (none).
Calls/effect boundaries: artifact.read_bytes, digest, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[15].value::Call

Source: `infra/agentinfra/verus_evidence.py:102`; AST `ba79b31ccb0ce6528091d69dcc0e3ae99174e6395536420a507c4fc3a7dbf1f5`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifact, digest, require, value. Outputs/bindings: (none).
Calls/effect boundaries: artifact.read_bytes, digest, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[15].value.args[0].left::Call

Source: `infra/agentinfra/verus_evidence.py:102`; AST `6c13cf6fd1b042bb73e0a640164161432e95c72e05be2af6a416312e3a8a40b5`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifact, digest. Outputs/bindings: (none).
Calls/effect boundaries: artifact.read_bytes, digest.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[15].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:102`; AST `626b6fc85e7682744f15e4cbc61ef300c401c7196405ee4cc0d3acefd8b58d3f`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifact. Outputs/bindings: (none).
Calls/effect boundaries: artifact.read_bytes.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[16]::Assign

Source: `infra/agentinfra/verus_evidence.py:103`; AST `49ca713854115b908fa1bd125532e8588002ba44c4812f6976f9babe57a052b8`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifact, inventory, obligation. Outputs/bindings: actual.
Calls/effect boundaries: artifact.read_text, inventory.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[16].value::Call

Source: `infra/agentinfra/verus_evidence.py:103`; AST `63f2facaad84f61f67af5eddc85e0482d0428c15613eb8f95994101b193ffda0`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifact, inventory, obligation. Outputs/bindings: (none).
Calls/effect boundaries: artifact.read_text, inventory.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[16].value.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:103`; AST `b876d3effae49582b3e61197a3d1f442a242d1b7e99b6b9502e74019d80abf3c`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifact. Outputs/bindings: (none).
Calls/effect boundaries: artifact.read_text.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[17]::Expr

Source: `infra/agentinfra/verus_evidence.py:104`; AST `80507f7195ba08bb03b5b2210cc62b8e637d40251382c3e0162410f58e8621a0`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, all, key, require, value. Outputs/bindings: key.
Calls/effect boundaries: all, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[17].value::Call

Source: `infra/agentinfra/verus_evidence.py:104`; AST `fd246eb554cbd806b400182ac1052a294ce652ca3acffe8ebecd5be1f584ef51`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, all, key, require, value. Outputs/bindings: key.
Calls/effect boundaries: all, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[17].value.args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:104`; AST `744c3a75c9f7f09bcf5e2a718c6279ce75de85014f6fc7eb5dbc9590d8827109`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, all, key, value. Outputs/bindings: key.
Calls/effect boundaries: all.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[17].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[17].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/verus_evidence.py:104`; AST `a820dbeba6fa486b245724685a74f61d40a28d17b324f9d75ca2514ab5dbb4c7`.

Rust module: `infra::agentinfra::verus_evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: actual, key, value. Outputs/bindings: key.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[17].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[18]::Expr

Source: `infra/agentinfra/verus_evidence.py:105`; AST `6b252908291fee88e6cefc23a53dadd5d4c5527ccfad5068f773352078921ee3`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, len, obligation, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[18].value::Call

Source: `infra/agentinfra/verus_evidence.py:105`; AST `100e58ef88253eb35630d2acf054842f061de271b8cc724d933c2aed65eab794`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, len, obligation, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[18].value.args[0].left::Call

Source: `infra/agentinfra/verus_evidence.py:105`; AST `0dedcf82230ced78adb5df19378588ae6a05222357fc5b91a0e9db0309295b4f`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[12].body[18].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::current_inventory::root.body[12].body[19]::Return

Source: `infra/agentinfra/verus_evidence.py:106`; AST `c6e836f0ce3bc5a8f6cbbba53edfe26738a77388db276f21cb107f34b75b0dbd`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Return evaluation at root.body[12].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13]::FunctionDef

Source: `infra/agentinfra/verus_evidence.py:108`; AST `5b5019350ee5a1950524f88446e7d9086e65ba04744b83406b89520c9c7a6e1c`.

Rust module: `infra::agentinfra::verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: SCHEMA, actual, declared, expected, len, r, require, row, rows, set. Outputs/bindings: expected, r, row, rows.
Calls/effect boundaries: len, require, row['relation'].strip, row['review'].strip, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[0]::Expr

Source: `infra/agentinfra/verus_evidence.py:109`; AST `f0b9590dd591957f33ca8e2546b3efbfdc5c67d60807646a4872c84fb48f9c03`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SCHEMA, actual, declared, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:109`; AST `01b7eae229a698742a17100c033a51f92be90fd773d2f3844bfd9537558d6715`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SCHEMA, actual, declared, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[1]::Assign

Source: `infra/agentinfra/verus_evidence.py:110`; AST `68b6301d8b35f16ea8a1adb490247e2deec8173cfe122d41e9b851f270b41d73`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, row. Outputs/bindings: expected, row.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[1].value::DictComp

Source: `infra/agentinfra/verus_evidence.py:110`; AST `e5487053bb9de6e4f266e1e9e943bf4191d9f16324a56d958079267e16631ba3`.

Rust module: `infra::agentinfra::verus_evidence`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: actual, row. Outputs/bindings: row.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered DictComp evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[2]::Assign

Source: `infra/agentinfra/verus_evidence.py:111`; AST `adeca159de0c4a7609984aa4b687350b4ea25c2f4f8ca4963c78e0123415f076`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: declared. Outputs/bindings: rows.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[3]::Expr

Source: `infra/agentinfra/verus_evidence.py:112`; AST `0bb72203c87173aab02216d27d1ab3b06badcd8af30df2f41dfb410ce78e03e1`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, len, r, require, rows. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[3].value::Call

Source: `infra/agentinfra/verus_evidence.py:112`; AST `01c61e21213773483eff7f10bb642c3de93116438f7693269e796790ecebf574`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len, r, require, rows. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[3].value.args[0].values[1].left::Call

Source: `infra/agentinfra/verus_evidence.py:112`; AST `0ea89ccf64714bf68d73a0787f966d27dbc61ef098aa73a74b057b16edd97566`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, rows. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[3].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/verus_evidence.py:112`; AST `c2d06b163e3f45e9d7be910cb5ac5a89b21e57724763b4159be61fb15e2f5005`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[3].value.args[0].values[2].left::Call

Source: `infra/agentinfra/verus_evidence.py:112`; AST `978295b8ea2e60bc6b25cdc13dafa6696b6ecafdcd357c67696dc19537729273`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, r, rows. Outputs/bindings: r.
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[3].value.args[0].values[2].left.args[0]::SetComp

Source: `infra/agentinfra/verus_evidence.py:112`; AST `ebf0a9c55e13fffd2901f2610e8f20e7e8841d90c0898695869ce088fecf3618`.

Rust module: `infra::agentinfra::verus_evidence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: r, rows. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[3].value.args[0].values[2].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[3].value.args[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/verus_evidence.py:112`; AST `0ea89ccf64714bf68d73a0787f966d27dbc61ef098aa73a74b057b16edd97566`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, rows. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.args[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[4]::Expr

Source: `infra/agentinfra/verus_evidence.py:113`; AST `49a536a47b7e317f98b6da8ddb5d1ecd51ab02090082f8c3600b8ba7a5710c3f`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, r, require, rows, set. Outputs/bindings: r.
Calls/effect boundaries: require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[4].value::Call

Source: `infra/agentinfra/verus_evidence.py:113`; AST `77bdc73e3241808b9f2b9d35c4187cc59c5edb7d855c598a19b9c5d3e5128b58`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, r, require, rows, set. Outputs/bindings: r.
Calls/effect boundaries: require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[4].value.args[0].left::SetComp

Source: `infra/agentinfra/verus_evidence.py:113`; AST `ebf0a9c55e13fffd2901f2610e8f20e7e8841d90c0898695869ce088fecf3618`.

Rust module: `infra::agentinfra::verus_evidence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: r, rows. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered SetComp evaluation at root.body[13].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[4].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/verus_evidence.py:113`; AST `8065006d3e7f0aec9df46549354158a7684ad8f3e04977773498c5d7231e93b7`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[5]::For

Source: `infra/agentinfra/verus_evidence.py:114`; AST `b1e60678f7344d807267fba6202678f7904923f96743d5dbab66804de25be999`.

Rust module: `infra::agentinfra::verus_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: expected, require, row, rows. Outputs/bindings: row.
Calls/effect boundaries: require, row['relation'].strip, row['review'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered For evaluation at root.body[13].body[5]; no call, error or mutation may be omitted. Iteration: row in rows
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[5].body[0]::Expr

Source: `infra/agentinfra/verus_evidence.py:115`; AST `71ef0edaa7c9ac76fe10e8813dbae123e46b787f0fa3f99cc9fe7dc65f12a003`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, require, row. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[5].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:115`; AST `4dc0313834935ba6a1ae43c974464a2a44e2f36ae26297ffbbd4bd8b1446f1d3`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, require, row. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[5].body[1]::Expr

Source: `infra/agentinfra/verus_evidence.py:116`; AST `5ddc87e9733afdd65972f0adf6359862758e6aab9374c2e78f35d81db1eeea78`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, row. Outputs/bindings: (none).
Calls/effect boundaries: require, row['relation'].strip, row['review'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[5].body[1].value::Call

Source: `infra/agentinfra/verus_evidence.py:116`; AST `b4525946249452b69685ecd219945d0c9281688f52ec2ddee2951226a6fa167e`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, row. Outputs/bindings: (none).
Calls/effect boundaries: require, row['relation'].strip, row['review'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[5].body[1].value.args[0].values[1]::Call

Source: `infra/agentinfra/verus_evidence.py:116`; AST `8644f48ecff567d4591ab174b55b8a123912f4f1a749001c88c893192398ecf2`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row. Outputs/bindings: (none).
Calls/effect boundaries: row['relation'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[1].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[5].body[1].value.args[0].values[2]::Call

Source: `infra/agentinfra/verus_evidence.py:116`; AST `438b59eccde6cb5bfb283b1668ff73bef6038da5da32b1abeaeff8c71110d51d`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row. Outputs/bindings: (none).
Calls/effect boundaries: row['review'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[1].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[6]::Return

Source: `infra/agentinfra/verus_evidence.py:117`; AST `9e53d52f717636f1eeca1cc41f082a7efed0462a043c98df48798d82d44dbc35`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Return evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_symbol_mapping::root.body[13].body[6].value::Call

Source: `infra/agentinfra/verus_evidence.py:117`; AST `8065006d3e7f0aec9df46549354158a7684ad8f3e04977773498c5d7231e93b7`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14]::FunctionDef

Source: `infra/agentinfra/verus_evidence.py:119`; AST `12cfe21da6e934be674e327ab129fb6d5f95c0d3341e1ac8e2aced343d600aa4`.

Rust module: `infra::agentinfra::verus_evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, authority, catalog, field, groups, ids, lane, len, m, mapped, mapped_sites, originals, r, require, requirements, row, rows, set, source, source_inventory. Outputs/bindings: authority, field, groups, ids, lane, m, mapped_sites, originals, r, requirements, row, rows, source.
Calls/effect boundaries: all, len, require, row['applicability_rationale'].strip, row['execution_obligation']['relation'].strip, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[0]::Expr

Source: `infra/agentinfra/verus_evidence.py:120`; AST `07dd4a15d750b9b4aac08ac7e2bf883f55c44d279ca933594d76643c746fb336`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[1]::Assign

Source: `infra/agentinfra/verus_evidence.py:121`; AST `bd5e3ef57b6f8b370d4dbf00a386e2d16be35fd8d73f8538a4cd73713d4adf1b`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: catalog, row. Outputs/bindings: ids, row.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[1].value::SetComp

Source: `infra/agentinfra/verus_evidence.py:121`; AST `8f788503c0b8ace9c3c3207257137b9ff7d7edc5396b66c01486b36d9e817142`.

Rust module: `infra::agentinfra::verus_evidence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: catalog, row. Outputs/bindings: row.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered SetComp evaluation at root.body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[2]::Expr

Source: `infra/agentinfra/verus_evidence.py:122`; AST `de5e8c1abb0bab383ec7144fe6fa782dc0f18a2124370942f2bc11f18cf885b1`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: catalog, ids, len, r, require. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[2].value::Call

Source: `infra/agentinfra/verus_evidence.py:122`; AST `b4b4e244109c28518bca75a497b9921dc5838515e4aa78a4c13405c287719cbb`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: catalog, ids, len, r, require. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[2].value.args[0].left.elts[0]::Call

Source: `infra/agentinfra/verus_evidence.py:122`; AST `d940cfa593b15493d58a127688c370c72c03970a7c689a9309f3d570ae21ccba`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: catalog, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.args[0].left.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[2].value.args[0].left.elts[1]::Call

Source: `infra/agentinfra/verus_evidence.py:122`; AST `e9ff8c6d4cd447580e3ae476d39cdd538e64139104de929c715ef5318d853424`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.args[0].left.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[2].value.args[0].left.elts[2]::Call

Source: `infra/agentinfra/verus_evidence.py:122`; AST `aebba34ae6db871ab3efb46c3beea095d740323d1a37a289a4712a4ae94a8301`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: catalog, len, r. Outputs/bindings: r.
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.args[0].left.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[2].value.args[0].left.elts[2].args[0]::SetComp

Source: `infra/agentinfra/verus_evidence.py:122`; AST `ae0a6c6bdf0b804c6264aa8bbdc1cc64a8bbcf567d0e36b0e711841e654122fc`.

Rust module: `infra::agentinfra::verus_evidence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: catalog, r. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered SetComp evaluation at root.body[14].body[2].value.args[0].left.elts[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[2].value.args[0].left.elts[3]::Call

Source: `infra/agentinfra/verus_evidence.py:123`; AST `cb222c43dc47dd529839e44d30add6732d908bfddae447b9ba8b518e2bbde6fa`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: catalog, len, r. Outputs/bindings: r.
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.args[0].left.elts[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[2].value.args[0].left.elts[3].args[0]::SetComp

Source: `infra/agentinfra/verus_evidence.py:123`; AST `69f238f5b3bd37b228b4f0f47697b1bc40a15e47111eb410efbfc1a7cf93f044`.

Rust module: `infra::agentinfra::verus_evidence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: catalog, r. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered SetComp evaluation at root.body[14].body[2].value.args[0].left.elts[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[3]::Assign

Source: `infra/agentinfra/verus_evidence.py:124`; AST `d4f9230a79ad7faa01b1912cfcc7ddcd472eee707ec5428037945aa8025df948`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: row, source_inventory. Outputs/bindings: originals, row.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[3].value::DictComp

Source: `infra/agentinfra/verus_evidence.py:124`; AST `c64fb11ae5b50804c1958b93ce5adf7733b0a816e8e5a6aeb482d93b331580df`.

Rust module: `infra::agentinfra::verus_evidence`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: row, source_inventory. Outputs/bindings: row.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered DictComp evaluation at root.body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[4]::Assign

Source: `infra/agentinfra/verus_evidence.py:125`; AST `30753f6d4a2a751388579f1e3178721bd7928953dc8290fe2cd251d785d10ad9`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mapped, row. Outputs/bindings: row, rows.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[4].value::DictComp

Source: `infra/agentinfra/verus_evidence.py:125`; AST `2c39937a70f38578f95466c9678fb8dface9f5c588930b45db1c3e404ef9259e`.

Rust module: `infra::agentinfra::verus_evidence`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: mapped, row. Outputs/bindings: row.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered DictComp evaluation at root.body[14].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[5]::Expr

Source: `infra/agentinfra/verus_evidence.py:126`; AST `3508f11091c716130d98c2d1b44f1ba707e42b3928d9d8546f8ca0915addbb59`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, mapped, originals, require, rows, source_inventory. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[5].value::Call

Source: `infra/agentinfra/verus_evidence.py:126`; AST `c65021a0cb09fa7b82bc35baa141751647254e48a693e80a55f58d8a5220b637`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, mapped, originals, require, rows, source_inventory. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[5].value.args[0].left::Call

Source: `infra/agentinfra/verus_evidence.py:126`; AST `76b9f27c7032a9e8eb29913f41caed940f7f0c5b10482095ed080fe3498901de`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, source_inventory. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[5].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/verus_evidence.py:126`; AST `9fcaf184388e17e9736fdeccfd404b344e945944d8b76a5a862ff45b0a36f344`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, originals. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[5].value.args[0].comparators[1]::Call

Source: `infra/agentinfra/verus_evidence.py:126`; AST `74ba2f19026eb21170df74de65fd9d688e860ca305a830132a1aae214e2eff94`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, mapped. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].comparators[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[5].value.args[0].comparators[2]::Call

Source: `infra/agentinfra/verus_evidence.py:126`; AST `0ea89ccf64714bf68d73a0787f966d27dbc61ef098aa73a74b057b16edd97566`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, rows. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].comparators[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[6]::Expr

Source: `infra/agentinfra/verus_evidence.py:128`; AST `e82e81b62a7f04680ae23544de908ab8e922ac8a678effd530b9a5fa0f20c56b`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, originals, require, rows, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[6].value::Call

Source: `infra/agentinfra/verus_evidence.py:128`; AST `49a80f42949a8434e8746ba7c71168a0ce6248862da524728592f5971ded3637`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, originals, require, rows, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[6].value.args[0].left::Call

Source: `infra/agentinfra/verus_evidence.py:128`; AST `654d6305ae83efe97ba187da797183659026e9f706590b10f96f7a5802d221bc`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: originals, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[6].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/verus_evidence.py:128`; AST `f9958c50c3dc60fe258a64d9ed44ea927f7756ff514d6cc22fba4fe146804b2b`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: rows, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[7]::Expr

Source: `infra/agentinfra/verus_evidence.py:129`; AST `6e38a35c7c534ac14873682f92605e51c7bb8ea98c72017db085d59a5e3056e0`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: catalog, mapped, require, source_inventory. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[7].value::Call

Source: `infra/agentinfra/verus_evidence.py:129`; AST `dd915327fef7aff032072fd334e4cc9f2b80572d3b9f39be61b5021fa1ae335a`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: catalog, mapped, require, source_inventory. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[8]::Assign

Source: `infra/agentinfra/verus_evidence.py:130`; AST `a5a5a6b83ae309c85ec10b70133787e7e85d0452306422cbbb7ce3b43394b18d`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mapped. Outputs/bindings: groups.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[9]::Expr

Source: `infra/agentinfra/verus_evidence.py:131`; AST `35568763ade3b705570f23003ff8574c25a1ad4ac4b92f6866d8bded534f74a9`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: groups, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[9].value::Call

Source: `infra/agentinfra/verus_evidence.py:131`; AST `b0760df3bd60c3575ad54014f69a85e3ff766bc5b24952ad781794d1eaa37263`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: groups, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10]::For

Source: `infra/agentinfra/verus_evidence.py:132`; AST `2f4f763bb3222c61dbd18d184d1d9b4865e77f1d31cdc61e5f69fd1c23426dcc`.

Rust module: `infra::agentinfra::verus_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: all, authority, catalog, field, groups, lane, len, m, mapped_sites, originals, r, require, requirements, row, rows, set, source. Outputs/bindings: authority, field, lane, m, mapped_sites, r, requirements, row, source.
Calls/effect boundaries: all, len, require, row['applicability_rationale'].strip, row['execution_obligation']['relation'].strip, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered For evaluation at root.body[14].body[10]; no call, error or mutation may be omitted. Iteration: authority in catalog
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[0]::Assign

Source: `infra/agentinfra/verus_evidence.py:133`; AST `7d280018381051a16b95d41b84d5366d56655ff0b49451a4ef1e718cab3a889f`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority, rows. Outputs/bindings: row.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[1]::Assign

Source: `infra/agentinfra/verus_evidence.py:133`; AST `7611802554a53b45e6f15e710e99d1fba7e5adb0c7139468eccb09057ef6b95a`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority, originals. Outputs/bindings: source.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[2]::Expr

Source: `infra/agentinfra/verus_evidence.py:134`; AST `8a67f214aeb50efdf28dd5637e370372b63e29d77a90b9f9814115dbc8a4449a`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority, require, row, source. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[2].value::Call

Source: `infra/agentinfra/verus_evidence.py:134`; AST `79065cda30506604852f2ed924ffb1b57977e222d0621d037d7d4abfa914e6bb`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority, require, row, source. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[3]::For

Source: `infra/agentinfra/verus_evidence.py:136`; AST `962803d8672a09ff3be4cb174874e9c6c669af9265b8b44ef66f99fa8e53cd5c`.

Rust module: `infra::agentinfra::verus_evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: field, lane, len, m, mapped_sites, require, row, set, source. Outputs/bindings: field, lane, m, mapped_sites.
Calls/effect boundaries: len, require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered For evaluation at root.body[14].body[10].body[3]; no call, error or mutation may be omitted. Iteration: (lane, field) in (('assertion', 'assertion_ids'), ('dependency', 'dependency_ids'))
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[3].body[0]::Assign

Source: `infra/agentinfra/verus_evidence.py:137`; AST `fc550981734e8914598677b7551a84e29928584c878cf2107e1577dd3a944b1f`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lane, row. Outputs/bindings: mapped_sites.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[3].body[1]::Expr

Source: `infra/agentinfra/verus_evidence.py:138`; AST `d95fa907f962a2f1332fd344655f4773fb97d4cad9fcbc4aed146934136b7751`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, lane, len, m, mapped_sites, require, row, set, source. Outputs/bindings: m.
Calls/effect boundaries: len, require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[10].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[3].body[1].value::Call

Source: `infra/agentinfra/verus_evidence.py:138`; AST `d84b7e2d464df78db99b523955834ab58064572cbd21cabab5dbe7e939826032`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, lane, len, m, mapped_sites, require, row, set, source. Outputs/bindings: m.
Calls/effect boundaries: len, require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[3].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/verus_evidence.py:138`; AST `19b2931a7a09a72a17fc672d744241334c0243f70d80462286fd3b7919a3975e`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, mapped_sites. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[3].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[3].body[1].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/verus_evidence.py:138`; AST `8a5ed379be82604b1b39aadcd5b15c9f59d416effabd4d96ed507d7a0aebd61e`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, len, source. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[3].body[1].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[3].body[1].value.args[0].values[2].left::SetComp

Source: `infra/agentinfra/verus_evidence.py:139`; AST `18c2586bdaab4c646cb524d4fd2710b8c301e3f028af81d555bacfd47efe69bb`.

Rust module: `infra::agentinfra::verus_evidence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: m, mapped_sites. Outputs/bindings: m.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered SetComp evaluation at root.body[14].body[10].body[3].body[1].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[3].body[1].value.args[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/verus_evidence.py:139`; AST `ac25867de20a2632e920a47d85eca2c1b7da4a8176b0e3e27eb42788a84eaa61`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, set, source. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[3].body[1].value.args[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[4]::Expr

Source: `infra/agentinfra/verus_evidence.py:140`; AST `53255602f62fa0786d33cbc65f7b1c9ceeb92b6e2b9bd3697a4525a28d7d955a`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, row. Outputs/bindings: (none).
Calls/effect boundaries: require, row['execution_obligation']['relation'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[4].value::Call

Source: `infra/agentinfra/verus_evidence.py:140`; AST `419528d333c52d9398a66bf1a132ad7d9277aad0b0f2fdabf33bbdcd74559ba3`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, row. Outputs/bindings: (none).
Calls/effect boundaries: require, row['execution_obligation']['relation'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[4].value.args[0].values[1]::Call

Source: `infra/agentinfra/verus_evidence.py:140`; AST `2c4418f015d76a9360d73d03f9ea290378818bf3efd466eb936174a1587985b6`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row. Outputs/bindings: (none).
Calls/effect boundaries: row['execution_obligation']['relation'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[4].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[5]::Assign

Source: `infra/agentinfra/verus_evidence.py:142`; AST `d4d80251c194ef8e219de82b804f09003d8afce1ce2c8c7886aa77a438aec0fd`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: row. Outputs/bindings: requirements.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[6]::Expr

Source: `infra/agentinfra/verus_evidence.py:143`; AST `23b0e2704a254ef4ea216e50d6c719632506ceaf61966eac48a85b03324383b5`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, groups, len, r, require, requirements, set. Outputs/bindings: r.
Calls/effect boundaries: all, len, require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[6].value::Call

Source: `infra/agentinfra/verus_evidence.py:143`; AST `67a888db5246d9444229bdbcaaca86c5ac2ceee079f32b1c812861ca8b69f34f`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, groups, len, r, require, requirements, set. Outputs/bindings: r.
Calls/effect boundaries: all, len, require, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/verus_evidence.py:143`; AST `b439bc46998c1bdb1c86a8832bcfefc2a98550a90b17c5467baa9bef678067f4`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, requirements. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[6].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/verus_evidence.py:143`; AST `384a2945c780d01051e512703497fe1da2009b38322e880ec229cf88529689fe`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, requirements, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[6].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[6].value.args[0].values[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/verus_evidence.py:143`; AST `35a4d1d9ade301de784d31ec3c5686ff96dafffc2662a1b2f5984dbe97dab016`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirements, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[6].value.args[0].values[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[6].value.args[0].values[1]::Call

Source: `infra/agentinfra/verus_evidence.py:143`; AST `8d4c247805899e7182d40a653ef8619a6365bbbd742b153d35dbeb841a5e007e`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, groups, r, requirements. Outputs/bindings: r.
Calls/effect boundaries: all.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[6].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[6].value.args[0].values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/verus_evidence.py:143`; AST `760193653c9a24f2d9f2d3ff1ce1bd20faded6af7a93707a5aac02c8cf34cba5`.

Rust module: `infra::agentinfra::verus_evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: groups, r, requirements. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[14].body[10].body[6].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[7]::If

Source: `infra/agentinfra/verus_evidence.py:144`; AST `658ac9df9717853962eb39818fa8faeb9daff7dc2c65ad0289681078f76e9374`.

Rust module: `infra::agentinfra::verus_evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: require, requirements, row. Outputs/bindings: (none).
Calls/effect boundaries: require, row['applicability_rationale'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered If evaluation at root.body[14].body[10].body[7]; no call, error or mutation may be omitted. Condition: row['concurrency_relevance'] == 'required_concurrency_obligation'
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[7].body[0]::Expr

Source: `infra/agentinfra/verus_evidence.py:145`; AST `fad96e31b0d149add5b4a7ffd762a05d382a09678ad715e4945330ee7af924c9`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, requirements, row. Outputs/bindings: (none).
Calls/effect boundaries: require, row['applicability_rationale'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[10].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[7].body[0].value::Call

Source: `infra/agentinfra/verus_evidence.py:145`; AST `4d082f447f66c4e5a942f735766d38495ab91e66e71c09224c0b403a7a29b0c8`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, requirements, row. Outputs/bindings: (none).
Calls/effect boundaries: require, row['applicability_rationale'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[10].body[7].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/verus_evidence.py:145`; AST `207fd8735220da75df058f19e9cfc5d59b34cf6a18d44ed5b1828e482421cfd2`.

Rust module: `infra::agentinfra::verus_evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row. Outputs/bindings: (none).
Calls/effect boundaries: row['applicability_rationale'].strip.
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[7].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/verus_evidence.py::module::validate_case_map::root.body[14].body[11]::Return

Source: `infra/agentinfra/verus_evidence.py:146`; AST `e8d62c7bb685945ea0a81e6d4c73e7fe86bcf8b904a9d5c35c30d98b70af7c94`.

Rust module: `infra::agentinfra::verus_evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: rows. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny_reuse, evidence, pathlib, re, security, shutil, types.

Invariants: Preserve ordered Return evaluation at root.body[14].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
