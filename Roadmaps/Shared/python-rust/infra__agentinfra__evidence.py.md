# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 316. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/evidence.py::module::root::Module

Source: `infra/agentinfra/evidence.py:1`; AST `4ff07914605ef903c8689452f5e568dcf856e9d3a03f2da09944ee93fbdae1c1`.

Rust module: `infra::agentinfra::evidence`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: OSError, PROFILE, Path, SecurityError, ValueError, __file__, actual, all, any, body, bool, c, cache_key, candidate, candidates, checked_output, command, confined_path, counts, current, current_receipt, digest, env, environment, exact_keys, expected, external_paths, field, identity, int, isinstance, k, kani_properties, kind, len, line, list, location, manifest, manifest_root, match, matches_version, n, name, number, numbers, obligation, observation, ord, out, output, outputs, p, path, previous, probe, probes, profile, properties, prose, r, range, re, read, receipt, receipts, record, relative, require, result, root, row, rows, s, scenarios, scope, set, sha256_file, sorted, source, source_snapshot, spec, state_path, status, str, successful, tool, tool_payload, type, unseal, value, witness, zip. Outputs/bindings: actual, body, c, cache_key, candidate, candidates, command, counts, current, env, expected, external_paths, field, identity, k, line, location, manifest_root, match, n, name, number, numbers, observation, out, outputs, p, path, previous, probe, probes, properties, r, receipt, receipts, record, relative, row, rows, s, scenarios, scope, source, spec, status, successful, tool, value, witness.
Calls/effect boundaries: '\n'.join, (root / witness['file']).resolve, Path, Path(__file__).parent.glob, Path(__file__).with_name, Path(tool['path']).is_file, actual.is_absolute, all, any, bool, candidate.resolve, candidate.resolve().relative_to, candidate.resolve().relative_to(root.resolve()).as_posix, checked_output, confined_path, current_receipt, digest, environment, exact_keys, identity.get, identity.get('proof_inputs', {}).items, identity['external'].items, identity['tools'].values, int, isinstance, kani_properties, len, list, match.groups, matches_version, name.strip, numbers.append, obligation.get, ord, p.resolve, properties.get, prose, range, re.escape, re.findall, re.finditer, re.fullmatch, re.search, read, require, result.get, root.resolve, row.get, rows.append, rows.items, rows.values, set, sha256_file, sorted, source.is_file, source.read_text, source.read_text().splitlines, source_snapshot, spec.get, state_path, str, successful.update, tool_payload, type, unseal, value.strip, zip.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::root.body[0]::Expr

Source: `infra/agentinfra/evidence.py:1`; AST `6787d06e8111baa6e1fc4933f87711438e8c90692372771f700608334e4a274e`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/evidence.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::root.body[2]::Import

Source: `infra/agentinfra/evidence.py:7`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/evidence.py:9`; AST `11d159f31a0d7770b11034e5c6f4deb12c77e9673635a8fd309426248b9eddd4`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/evidence.py:10`; AST `899bd8a7edfa3f8a4675642ab4ef89fc11057d543d281a15055619bfd2ee6931`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5]::FunctionDef

Source: `infra/agentinfra/evidence.py:13`; AST `7af88355f1efc897de5b7aa8dffa054bcd902a286f884c1d6fbbff2020d67bd3`.

Rust module: `infra::agentinfra::evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: any, c, isinstance, kind, len, ord, re, str, value. Outputs/bindings: c.
Calls/effect boundaries: any, isinstance, len, ord, re.escape, re.fullmatch, value.strip.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0]::Return

Source: `infra/agentinfra/evidence.py:16`; AST `3b7200382e053bf34a72df745b2571c2fc3aba9962792a81d800f7287047d25c`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, c, isinstance, kind, len, ord, re, str, value. Outputs/bindings: c.
Calls/effect boundaries: any, isinstance, len, ord, re.escape, re.fullmatch, value.strip.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0].value.values[0]::Call

Source: `infra/agentinfra/evidence.py:16`; AST `f0937843eac35cb846ed896776839197deebad579475d870c722a45446739540`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0].value.values[1].left::Call

Source: `infra/agentinfra/evidence.py:16`; AST `57bdbf809c25115282faa72b8f2a20b503b69c9d181b909be2b57a332a04a030`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0].value.values[2].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:16`; AST `7d389057b81f97945d507ad29556bbeb4cd0d442c311a6de949b3a4d38e1cedd`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: value.strip.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value.values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0].value.values[3].operand::Call

Source: `infra/agentinfra/evidence.py:17`; AST `186744cd9c7315f4250f1ae824fed2bd5f7d6142c51dda0ccce75657d5358f91`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, c, ord, value. Outputs/bindings: c.
Calls/effect boundaries: any, ord.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value.values[3].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0].value.values[3].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/evidence.py:17`; AST `079554bb8125d107ce3d1c5e93184f43edf33cc89e9ce398759513f35295e441`.

Rust module: `infra::agentinfra::evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, ord, value. Outputs/bindings: c.
Calls/effect boundaries: ord.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[5].body[0].value.values[3].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0].value.values[3].operand.args[0].elt.values[0].left::Call

Source: `infra/agentinfra/evidence.py:17`; AST `9f3fdd78d63be4c52ff42d37687f7f1a9d2320e894edbf3cd2fc8b672f6de5dc`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, ord. Outputs/bindings: (none).
Calls/effect boundaries: ord.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value.values[3].operand.args[0].elt.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0].value.values[3].operand.args[0].elt.values[1].left::Call

Source: `infra/agentinfra/evidence.py:17`; AST `9f3fdd78d63be4c52ff42d37687f7f1a9d2320e894edbf3cd2fc8b672f6de5dc`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, ord. Outputs/bindings: (none).
Calls/effect boundaries: ord.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value.values[3].operand.args[0].elt.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0].value.values[4].left::Call

Source: `infra/agentinfra/evidence.py:18`; AST `49c92cf1a50332feddd2db3b2958a4db42d0facb864577b79454b7a7758b0427`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: kind, re, value. Outputs/bindings: (none).
Calls/effect boundaries: re.escape, re.fullmatch.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value.values[4].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_name::root.body[5].body[0].value.values[4].left.args[0].left.right::Call

Source: `infra/agentinfra/evidence.py:18`; AST `6490d51f87855cac53de33b687679324bb4ef59549df318289996d2e4b115b7d`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: kind, re. Outputs/bindings: (none).
Calls/effect boundaries: re.escape.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].value.values[4].left.args[0].left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6]::FunctionDef

Source: `infra/agentinfra/evidence.py:21`; AST `595e53cccbbf19097e060e681c6f50db42cd8bb5435d71c091595191890a8a72`.

Rust module: `infra::agentinfra::evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, Path, SecurityError, ValueError, actual, candidate, candidates, confined_path, int, len, line, location, manifest, re, relative, root, row, source. Outputs/bindings: actual, candidate, candidates, line, location, relative, source.
Calls/effect boundaries: Path, actual.is_absolute, candidate.resolve, candidate.resolve().relative_to, candidate.resolve().relative_to(root.resolve()).as_posix, confined_path, int, len, re.fullmatch, root.resolve, row.get, source.is_file, source.read_text, source.read_text().splitlines.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[0]::Assign

Source: `infra/agentinfra/evidence.py:22`; AST `6e9701650c9ee0957271bbb4e9e052bba985d6b54ca9905d9045a5d9e8c4a1cb`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: re, row. Outputs/bindings: location.
Calls/effect boundaries: re.fullmatch, row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[0].value::Call

Source: `infra/agentinfra/evidence.py:22`; AST `62e70bf61b1fa57b82f69447fa194bfb68bffa47731d9ea8b8d87114332a42a3`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re, row. Outputs/bindings: (none).
Calls/effect boundaries: re.fullmatch, row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[0].value.args[1]::Call

Source: `infra/agentinfra/evidence.py:22`; AST `55d67da988036a292ee7f67fa87366a11399528c56d3a171e15a77758562753d`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row. Outputs/bindings: (none).
Calls/effect boundaries: row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[1]::If

Source: `infra/agentinfra/evidence.py:23`; AST `6bdc4cf4760dc124dd0c6fb16bbf9783289036144b2f85d7a84ac7eeb4185c57`.

Rust module: `infra::agentinfra::evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: location. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered If evaluation at root.body[6].body[1]; no call, error or mutation may be omitted. Condition: location is None
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[1].body[0]::Return

Source: `infra/agentinfra/evidence.py:24`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[2]::Assign

Source: `infra/agentinfra/evidence.py:25`; AST `8c230d8f17abb54392a64560b87cc8f4a4115dba2ccc9aa2caf53d298a12dff3`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, location. Outputs/bindings: actual.
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[2].value::Call

Source: `infra/agentinfra/evidence.py:25`; AST `4477dbdf4e121e4f9cb656ad66aaa7aa5c84c7897d9507c5335b2f724b027602`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, location. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[3]::Assign

Source: `infra/agentinfra/evidence.py:26`; AST `0a587fd8ae071f97060095c03cd72351c9fa6c077baf5f78c0c75f3f5fafc183`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, manifest, root. Outputs/bindings: candidates.
Calls/effect boundaries: actual.is_absolute.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[3].value.test::Call

Source: `infra/agentinfra/evidence.py:26`; AST `9d49711554b9e93085ead4996602b7a6f9b3ba2dc1d0b7d780936a8a4f96dbbe`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual. Outputs/bindings: (none).
Calls/effect boundaries: actual.is_absolute.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[3].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4]::For

Source: `infra/agentinfra/evidence.py:27`; AST `83cbaa8fa33f9ffa466d5d58cea018ce61fffe1b281f7ae18b83e8e0a627aaff`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: OSError, SecurityError, ValueError, candidate, candidates, confined_path, int, len, line, location, relative, root, source. Outputs/bindings: candidate, line, relative, source.
Calls/effect boundaries: candidate.resolve, candidate.resolve().relative_to, candidate.resolve().relative_to(root.resolve()).as_posix, confined_path, int, len, root.resolve, source.is_file, source.read_text, source.read_text().splitlines.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[6].body[4]; no call, error or mutation may be omitted. Iteration: candidate in candidates
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0]::Try

Source: `infra/agentinfra/evidence.py:28`; AST `39dc6c2c25950e8628c68debe9617b4cd658bfed7e47678eecc33bdf6563bfc8`.

Rust module: `infra::agentinfra::evidence`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, SecurityError, ValueError, candidate, confined_path, int, len, line, location, relative, root, source. Outputs/bindings: line, relative, source.
Calls/effect boundaries: candidate.resolve, candidate.resolve().relative_to, candidate.resolve().relative_to(root.resolve()).as_posix, confined_path, int, len, root.resolve, source.is_file, source.read_text, source.read_text().splitlines.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Try evaluation at root.body[6].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[0]::Assign

Source: `infra/agentinfra/evidence.py:29`; AST `acd17077398e8aef7a5fbbaa5c40f5db3cb0623c18e908cb94cf01b76597ea2f`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, root. Outputs/bindings: relative.
Calls/effect boundaries: candidate.resolve, candidate.resolve().relative_to, candidate.resolve().relative_to(root.resolve()).as_posix, root.resolve.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[0].value::Call

Source: `infra/agentinfra/evidence.py:29`; AST `0a1e15668df25606fd3030634148aa2677954b50e797c0986db53077fb0e0f39`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, root. Outputs/bindings: (none).
Calls/effect boundaries: candidate.resolve, candidate.resolve().relative_to, candidate.resolve().relative_to(root.resolve()).as_posix, root.resolve.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[0].value.func.value::Call

Source: `infra/agentinfra/evidence.py:29`; AST `29b3dddc38bf3abd2ecdbf0f6a32425609f83d20e9381ede311334a97dcdbc39`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, root. Outputs/bindings: (none).
Calls/effect boundaries: candidate.resolve, candidate.resolve().relative_to, root.resolve.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[0].value.func.value.func.value::Call

Source: `infra/agentinfra/evidence.py:29`; AST `5db8ac06bac2b3b70e31ea80c1f0ca91d87672d489a33eb95ec5e48df0405e0f`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate. Outputs/bindings: (none).
Calls/effect boundaries: candidate.resolve.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[0].value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[0].value.func.value.args[0]::Call

Source: `infra/agentinfra/evidence.py:29`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[0].value.func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[1]::Assign

Source: `infra/agentinfra/evidence.py:30`; AST `46a449027c7be3bdbc52e184bea4ba99d16e48f3f48bd8f7ef3550375ab30dab`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, relative, root. Outputs/bindings: source.
Calls/effect boundaries: confined_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[4].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[1].value::Call

Source: `infra/agentinfra/evidence.py:30`; AST `63c9acf4cfde20a50eacc658154bbb4ec3954f19236b82666a93c852e8d25e5a`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, relative, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[2]::Assign

Source: `infra/agentinfra/evidence.py:31`; AST `d706ec9335c293e8983598dc9a9cd45559036d065413d31de8509763b4667547`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, location. Outputs/bindings: line.
Calls/effect boundaries: int.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[4].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[2].value::Call

Source: `infra/agentinfra/evidence.py:31`; AST `2b0d42663eac444e6e5d0a1a7893e020ad33436c2974115c25d8f552f58158d4`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, location. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[3]::If

Source: `infra/agentinfra/evidence.py:32`; AST `8ac120259c0c5efd5d2d1b0e0c92d3be0b6cc5e8f0ade0feb2d289fd259c7c76`.

Rust module: `infra::agentinfra::evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: len, line, relative, source. Outputs/bindings: (none).
Calls/effect boundaries: len, source.is_file, source.read_text, source.read_text().splitlines.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered If evaluation at root.body[6].body[4].body[0].body[3]; no call, error or mutation may be omitted. Condition: source.is_file() and 1 <= line <= len(source.read_text().splitlines())
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[3].test.values[0]::Call

Source: `infra/agentinfra/evidence.py:32`; AST `0213b25dd3fd96762f6caaca48442a4403a5405b76fcc8886d4aceb4674687c8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.is_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[3].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[3].test.values[1].comparators[1]::Call

Source: `infra/agentinfra/evidence.py:32`; AST `3badc59417216ae438e32fd63bddfaf7e4beaa0e8c1af48f8e6e3ef4dbbaaefb`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, source. Outputs/bindings: (none).
Calls/effect boundaries: len, source.read_text, source.read_text().splitlines.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[3].test.values[1].comparators[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[3].test.values[1].comparators[1].args[0]::Call

Source: `infra/agentinfra/evidence.py:32`; AST `b45fc3d58380a6263a4cf8dc25f4a7d6f2db8a7c7124323b1a21f671cb6037ed`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.read_text, source.read_text().splitlines.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[3].test.values[1].comparators[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[3].test.values[1].comparators[1].args[0].func.value::Call

Source: `infra/agentinfra/evidence.py:32`; AST `6c1e5441d9f3a8009a1291ac3a347c9696b9950e44674d6a3088f82b392bb8dc`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.read_text.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].body[3].test.values[1].comparators[1].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].body[3].body[0]::Return

Source: `infra/agentinfra/evidence.py:33`; AST `a29f56e31f0f365353d970fe867cf9868e0a3a19b9a455d47168d6a6a9a0981e`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: line, relative. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[6].body[4].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/evidence.py:34`; AST `a15bfcd562c3012d1421a67160d3407f6240fadfa4b67e8677e5dca6f4c72a19`.

Rust module: `infra::agentinfra::evidence`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError, SecurityError, ValueError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[6].body[4].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[4].body[0].handlers[0].body[0]::Continue

Source: `infra/agentinfra/evidence.py:35`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Continue evaluation at root.body[6].body[4].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::property_location::root.body[6].body[5]::Return

Source: `infra/agentinfra/evidence.py:36`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7]::FunctionDef

Source: `infra/agentinfra/evidence.py:39`; AST `cc41404d387d15dc64e2439b9c4be7daffc2ad95db8cc938213be32616b13c1d`.

Rust module: `infra::agentinfra::evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: body, int, len, list, location, match, name, number, numbers, output, range, re, require, rows, status. Outputs/bindings: body, location, match, name, number, numbers, rows, status.
Calls/effect boundaries: int, len, list, match.groups, name.strip, numbers.append, range, re.findall, re.finditer, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[0]::Assign

Source: `infra/agentinfra/evidence.py:40`; AST `df4673da866e41173fddde9b63f602bd87c25cde758b62448a23926237b8df16`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: rows.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[1]::Assign

Source: `infra/agentinfra/evidence.py:41`; AST `680b7c8563cc0ea8208ac3a05ee5ee9ae7c76b26ed48c822749399aa8111a233`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: numbers.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2]::For

Source: `infra/agentinfra/evidence.py:42`; AST `70b837e1d48896ed66e59e993c1e46b845b9e93774facdbd1d5db8fab55ee5d9`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: body, int, len, location, match, name, number, numbers, output, re, require, rows, status. Outputs/bindings: body, location, match, name, number, status.
Calls/effect boundaries: int, len, match.groups, name.strip, numbers.append, re.findall, re.finditer, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[7].body[2]; no call, error or mutation may be omitted. Iteration: match in re.finditer('^Check (\\d+): ([^\\r\\n]+)\\r?\\n(.*?)(?=^Check \\d+:|^SUMMARY:|^VERIFICATION:|\\Z)', output, re.M | re.S)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].iter::Call

Source: `infra/agentinfra/evidence.py:42`; AST `9370e4511a6026f14080ca14bb676363821e0d8b16bf3fc29313601cbce93884`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.finditer.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[0]::Assign

Source: `infra/agentinfra/evidence.py:43`; AST `51c20541f85464f167c7583e5605bd3b8369dae5ee51eab64f8e70da87b8eedb`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: match. Outputs/bindings: body, name, number.
Calls/effect boundaries: match.groups.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[0].value::Call

Source: `infra/agentinfra/evidence.py:43`; AST `9c47fa7c79009eec7b4eeca3ca2a8d1b4ac272286842074e8c81efd71d7d8c1b`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: match. Outputs/bindings: (none).
Calls/effect boundaries: match.groups.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[1]::Assign

Source: `infra/agentinfra/evidence.py:44`; AST `c1de943cc96b59e70d1c756656241928e2bf67195d1fb277156c2ce3eac0f334`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name. Outputs/bindings: name.
Calls/effect boundaries: name.strip.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[1].value::Call

Source: `infra/agentinfra/evidence.py:44`; AST `eece2e999f39f90ddfe01061cdcf0ffa084aa0e7c49785ed066148fbcc165539`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.strip.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[2]::Expr

Source: `infra/agentinfra/evidence.py:45`; AST `08a8b4a8c07b0d24cc2a3f3f547310d0a07484552f005e2409f73dc251f58587`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, number, numbers. Outputs/bindings: (none).
Calls/effect boundaries: int, numbers.append.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[2].value::Call

Source: `infra/agentinfra/evidence.py:45`; AST `0706564fc48f4d1ddf345856c8d7f652eaf95a28b27bac73cdc8bb4c1d2ea257`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, number, numbers. Outputs/bindings: (none).
Calls/effect boundaries: int, numbers.append.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[2].value.args[0]::Call

Source: `infra/agentinfra/evidence.py:45`; AST `65457aca9cd71b7a1664c649fbcdbc9340ada4dcd176121be11baf0a9c04bc21`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, number. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[3]::Assign

Source: `infra/agentinfra/evidence.py:46`; AST `1fc9a4664e5e145fd7c50cd8894c3825be5dbb7e9a01a31bb1d87d83ac873049`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: body, re. Outputs/bindings: status.
Calls/effect boundaries: re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[3].value::Call

Source: `infra/agentinfra/evidence.py:46`; AST `093fb4076f02dd81f4a802f8b5715aaf14e23476c471346e130b19ed95f431d3`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: body, re. Outputs/bindings: (none).
Calls/effect boundaries: re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[4]::Assign

Source: `infra/agentinfra/evidence.py:47`; AST `6919fa5b2e4b09185f1b1d1d7b50a0b5b352f3e0b5b263934b5fbb06985d0b5a`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: body, re. Outputs/bindings: location.
Calls/effect boundaries: re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[4].value::Call

Source: `infra/agentinfra/evidence.py:47`; AST `597ea9054781b9767495310d3de1325ccfaa2a7d9416c98eaf97dff5953d4a72`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: body, re. Outputs/bindings: (none).
Calls/effect boundaries: re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[5]::Expr

Source: `infra/agentinfra/evidence.py:48`; AST `6b22c83ffbe6cc453342acf49251b02288f2dfb5e20d504bbbb393a34fe0061a`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, name, require, rows, status. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[5].value::Call

Source: `infra/agentinfra/evidence.py:48`; AST `8e53cd7d6baebb764db825467dd5b2ea5783fb9283b53e91fa95f8096946b399`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, name, require, rows, status. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[5].value.args[0].values[1].left::Call

Source: `infra/agentinfra/evidence.py:48`; AST `73fc434e7a6735598e3eefc09b4153726c0e731a2af545f7d9281b200f550640`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, status. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[5].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[6]::Assign

Source: `infra/agentinfra/evidence.py:49`; AST `f858f2a6ead80168597fe4b7064ba78075b473360d90e1a35c9577320049b02a`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, location, name, rows, status. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[2].body[6].value.values[1].test.left::Call

Source: `infra/agentinfra/evidence.py:49`; AST `5cc98ea9583628a435a1e8374e15c6e6b063eedc22a5febedc1e15f90a00df2e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, location. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[6].value.values[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[3]::Expr

Source: `infra/agentinfra/evidence.py:50`; AST `94c84d33f39a3b997a4f1ce14e4ed121a7d2e09c369e93397cffe3d9b8c44d40`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, output, re, require, rows. Outputs/bindings: (none).
Calls/effect boundaries: len, re.findall, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[3].value::Call

Source: `infra/agentinfra/evidence.py:50`; AST `c1f9d33ab33b3148d0b035213659b08b21d58710f761b820fab3a4d5b185d351`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, output, re, require, rows. Outputs/bindings: (none).
Calls/effect boundaries: len, re.findall, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[3].value.args[0].left::Call

Source: `infra/agentinfra/evidence.py:50`; AST `0ea89ccf64714bf68d73a0787f966d27dbc61ef098aa73a74b057b16edd97566`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, rows. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[3].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:50`; AST `24303f91fac356b3f8010d24169e1ea7e0a92700219d19a167faec0d08a65a55`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, output, re. Outputs/bindings: (none).
Calls/effect boundaries: len, re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[3].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/evidence.py:50`; AST `fdb01fae28894c3cfd97aa1cd245703c015e8b53f7a1da50f2a13675af9880dd`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, re. Outputs/bindings: (none).
Calls/effect boundaries: re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[4]::Expr

Source: `infra/agentinfra/evidence.py:51`; AST `a2efe08a3233fec219709df426adbc22134e4b3adcb5a3c29107740f395636db`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, list, numbers, range, require. Outputs/bindings: (none).
Calls/effect boundaries: len, list, range, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[4].value::Call

Source: `infra/agentinfra/evidence.py:51`; AST `faeac3256112ebfe7a99a894a7200d9fdc36a2567e36decc65720191b834672a`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, list, numbers, range, require. Outputs/bindings: (none).
Calls/effect boundaries: len, list, range, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[4].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:51`; AST `e275e4b51f75775d16f5d1955f4a1567d6c58eb6ac3e1b0095fdcc4597493a91`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, list, numbers, range. Outputs/bindings: (none).
Calls/effect boundaries: len, list, range.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[4].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/evidence.py:51`; AST `c78a8a4b08828f4a53e71531d46207b9cc00cb2917f5a49ed49d84a61dca35b8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, numbers, range. Outputs/bindings: (none).
Calls/effect boundaries: len, range.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[4].value.args[0].comparators[0].args[0].args[1].left::Call

Source: `infra/agentinfra/evidence.py:51`; AST `c18e7e6451d5d3128973b19cee76f67f992874044259152a9ddcc58096b1410c`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, numbers. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].value.args[0].comparators[0].args[0].args[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::kani_properties::root.body[7].body[5]::Return

Source: `infra/agentinfra/evidence.py:52`; AST `e8d62c7bb685945ea0a81e6d4c73e7fe86bcf8b904a9d5c35c30d98b70af7c94`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: rows. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8]::FunctionDef

Source: `infra/agentinfra/evidence.py:55`; AST `13c4dd01f6462b0678dcf4c22e53a2fe80c91e699866acacc3455f654264e16c`.

Rust module: `infra::agentinfra::evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, all, any, bool, checked_output, kani_properties, n, obligation, r, result, rows. Outputs/bindings: n, r, rows.
Calls/effect boundaries: all, any, bool, checked_output, kani_properties, rows.items, rows.values.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[0]::If

Source: `infra/agentinfra/evidence.py:56`; AST `331e761e4b86f061983d81f615ade884ffc3922932558d850dcff51a3ae0234d`.

Rust module: `infra::agentinfra::evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: checked_output, obligation, result. Outputs/bindings: (none).
Calls/effect boundaries: checked_output.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered If evaluation at root.body[8].body[0]; no call, error or mutation may be omitted. Condition: not checked_output(obligation, result)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[0].test.operand::Call

Source: `infra/agentinfra/evidence.py:56`; AST `d112d9685f0bcd1f37234312989cf51ff7b3fbc4601687b0d8644cab9a0271b7`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, obligation, result. Outputs/bindings: (none).
Calls/effect boundaries: checked_output.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[0].body[0]::Return

Source: `infra/agentinfra/evidence.py:57`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[1]::If

Source: `infra/agentinfra/evidence.py:58`; AST `c6ef8b9d3f257a0e727a9daebb90f6cddf3034246f1750f49e92e14050781c02`.

Rust module: `infra::agentinfra::evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered If evaluation at root.body[8].body[1]; no call, error or mutation may be omitted. Condition: obligation['method'] != 'kani'
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[1].body[0]::Return

Source: `infra/agentinfra/evidence.py:59`; AST `4a8ef490a01d3017cb999fbea58c2adfb60a40ad736e0d23eceb176a236b14c3`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[8].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[2]::Try

Source: `infra/agentinfra/evidence.py:60`; AST `7c11b5d0ccda062efbc276acbce65f49dfd24f59ce3fc643296e69cfbb0617ab`.

Rust module: `infra::agentinfra::evidence`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ValueError, kani_properties, result. Outputs/bindings: rows.
Calls/effect boundaries: kani_properties.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Try evaluation at root.body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[2].body[0]::Assign

Source: `infra/agentinfra/evidence.py:61`; AST `21ad413b929d193fc0098ca8c8ad31d6bda2b99ca468bac108ffe462ed5ddeb0`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: kani_properties, result. Outputs/bindings: rows.
Calls/effect boundaries: kani_properties.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[2].body[0].value::Call

Source: `infra/agentinfra/evidence.py:61`; AST `df763b8574f072f2308204e9b8315db4fb173934fafc1b83c25bc80ec9e81636`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: kani_properties, result. Outputs/bindings: (none).
Calls/effect boundaries: kani_properties.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[2].handlers[0]::ExceptHandler

Source: `infra/agentinfra/evidence.py:62`; AST `4883d4e0749e17f2c554fb7af5eba78a188ed801a4efb2f9c21a51787382ae77`.

Rust module: `infra::agentinfra::evidence`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[8].body[2].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[2].handlers[0].body[0]::Return

Source: `infra/agentinfra/evidence.py:63`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[8].body[2].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3]::Return

Source: `infra/agentinfra/evidence.py:66`; AST `890d75bbef1fa40e43f6bbe72a02cbb5925ce7229affefdf9c692be064afa53a`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, any, bool, n, r, rows. Outputs/bindings: n, r.
Calls/effect boundaries: all, any, bool, rows.items, rows.values.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[0]::Call

Source: `infra/agentinfra/evidence.py:66`; AST `d0dffa625e10b837c91e078312619c2668969f9be68b1b0830a02a3ad6d555ac`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, rows. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[1]::Call

Source: `infra/agentinfra/evidence.py:66`; AST `e6d1b66cb2a2f6198c8b5f9f99de33e8bd7d428ddc3183ca970910037e70ca55`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, r, rows. Outputs/bindings: r.
Calls/effect boundaries: all, rows.values.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/evidence.py:66`; AST `f073dc87b67790807d11e1158fdddc30883a57663659a3b2f7585ee8d0d7ab88`.

Rust module: `infra::agentinfra::evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: r, rows. Outputs/bindings: r.
Calls/effect boundaries: rows.values.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[3].value.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[1].args[0].generators[0].iter::Call

Source: `infra/agentinfra/evidence.py:66`; AST `c4fa7b32f0603e90cd5161974ab4c3dde9aa10d1bef21039be2516bfd167a362`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: rows. Outputs/bindings: (none).
Calls/effect boundaries: rows.values.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[1].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[2]::Call

Source: `infra/agentinfra/evidence.py:67`; AST `b90e245f6ed463e04a43bec6e50deb0c65aa2493eb1fd35557ea8884fabbf1c8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, n, r, rows. Outputs/bindings: n, r.
Calls/effect boundaries: any, rows.items.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[2].args[0]::GeneratorExp

Source: `infra/agentinfra/evidence.py:67`; AST `c87f806fea07702e0c01893c2fd4446664f3676efa879ff6dcba7cc56e0c77b1`.

Rust module: `infra::agentinfra::evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: n, r, rows. Outputs/bindings: n, r.
Calls/effect boundaries: rows.items.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[3].value.values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[2].args[0].generators[0].iter::Call

Source: `infra/agentinfra/evidence.py:67`; AST `a048cd7c49e5ab559e4527824f2323fa76ca4b2c75c65db484e69475cb146100`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: rows. Outputs/bindings: (none).
Calls/effect boundaries: rows.items.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[2].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[3]::Call

Source: `infra/agentinfra/evidence.py:68`; AST `3e6e353e6fefedf810e623715e0da73419a498262c8e3528a21030fea268bc03`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, n, r, rows. Outputs/bindings: n, r.
Calls/effect boundaries: any, rows.items.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[3].args[0]::GeneratorExp

Source: `infra/agentinfra/evidence.py:68`; AST `9316696f3743c1ff7a90418dd420a97a58cceddf89c7af7938f2412b7b4670c4`.

Rust module: `infra::agentinfra::evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: n, r, rows. Outputs/bindings: n, r.
Calls/effect boundaries: rows.items.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[3].value.values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_output::root.body[8].body[3].value.values[3].args[0].generators[0].iter::Call

Source: `infra/agentinfra/evidence.py:68`; AST `a048cd7c49e5ab559e4527824f2323fa76ca4b2c75c65db484e69475cb146100`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: rows. Outputs/bindings: (none).
Calls/effect boundaries: rows.items.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.values[3].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_identity::root.body[9]::FunctionDef

Source: `infra/agentinfra/evidence.py:71`; AST `a8329b53867fab99a17b20961a2eaf6478dbf091bc2b77d6dc0f6fed32c450f3`.

Rust module: `infra::agentinfra::evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: confined_path, field, name, obligation, root, sha256_file. Outputs/bindings: field, name.
Calls/effect boundaries: confined_path, obligation.get, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_identity::root.body[9].body[0]::ImportFrom

Source: `infra/agentinfra/evidence.py:72`; AST `e3032151acd9fcf40260758bebecaff812b64d93fb7f57eb031341f3937723da`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_identity::root.body[9].body[1]::Return

Source: `infra/agentinfra/evidence.py:73`; AST `57e1f9a04e069673af4e309bfed54dd4d6bf0d37caeea627994d7395180589a5`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, field, name, obligation, root, sha256_file. Outputs/bindings: field, name.
Calls/effect boundaries: confined_path, obligation.get, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_identity::root.body[9].body[1].value.values[3].body::Call

Source: `infra/agentinfra/evidence.py:75`; AST `94f2d35bc9df1e595e42888181d2b0a52cb928808a0dc031e182369f66732863`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value.values[3].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_identity::root.body[9].body[1].value.values[4]::DictComp

Source: `infra/agentinfra/evidence.py:76`; AST `a3c0567b5fd1eaf880619b5eec3ece8e6c32ca94757006c594667417431b91b5`.

Rust module: `infra::agentinfra::evidence`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: confined_path, field, name, obligation, root, sha256_file. Outputs/bindings: field, name.
Calls/effect boundaries: confined_path, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered DictComp evaluation at root.body[9].body[1].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_identity::root.body[9].body[1].value.values[4].value::DictComp

Source: `infra/agentinfra/evidence.py:76`; AST `410af672649654d4a97a477f179cafec3e6044b33373297b24514bfb7bfbbc4f`.

Rust module: `infra::agentinfra::evidence`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: confined_path, field, name, obligation, root, sha256_file. Outputs/bindings: name.
Calls/effect boundaries: confined_path, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered DictComp evaluation at root.body[9].body[1].value.values[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_identity::root.body[9].body[1].value.values[4].value.value::Call

Source: `infra/agentinfra/evidence.py:76`; AST `65e16a26698962261c20cad68e9afec46870bb80c309fb612020d11d84d7d18d`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, name, root, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value.values[4].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_identity::root.body[9].body[1].value.values[4].value.value.args[0]::Call

Source: `infra/agentinfra/evidence.py:76`; AST `84ad204db26e498c59a40ccefeec068f82fca59b0dd091cc081652642986ed46`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value.values[4].value.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::proof_identity::root.body[9].body[1].value.values[5]::Call

Source: `infra/agentinfra/evidence.py:78`; AST `772f7787041ada1056d843bc24609c2b849eafbdae460f70f8699ae65e50a570`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10]::FunctionDef

Source: `infra/agentinfra/evidence.py:81`; AST `5929cbbfad266e06b482592bbdfc099292c7864a03eeaaf506853ac804a62b92`.

Rust module: `infra::agentinfra::evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: PROFILE, Path, __file__, any, c, command, confined_path, current, digest, env, environment, expected, external_paths, identity, k, len, matches_version, name, outputs, p, path, previous, probe, probes, profile, receipt, require, result, root, sha256_file, sorted, source, source_snapshot, spec, state_path, str, tool, tool_payload, unseal, zip. Outputs/bindings: c, command, current, env, expected, external_paths, identity, k, name, outputs, p, path, previous, probe, probes, receipt, source, spec, tool.
Calls/effect boundaries: Path, Path(__file__).parent.glob, Path(__file__).with_name, Path(tool['path']).is_file, any, confined_path, digest, environment, identity.get, identity.get('proof_inputs', {}).items, identity['external'].items, identity['tools'].values, len, matches_version, require, result.get, sha256_file, sorted, source_snapshot, spec.get, state_path, str, tool_payload, unseal, zip.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[0]::Expr

Source: `infra/agentinfra/evidence.py:82`; AST `bb8d31f72eed23921ac337f5723e37984dca1da7314528bcbe361d3bcbab86c0`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[1]::ImportFrom

Source: `infra/agentinfra/evidence.py:83`; AST `f82621390f131b67b7452344c77c40734dca6dd2be1c5ec7cf088612c33659ca`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[2]::ImportFrom

Source: `infra/agentinfra/evidence.py:84`; AST `26852cc1d729af4ad8127aeb4e583fc8c4f28779c194069665643430d1d6d0b6`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[3]::Expr

Source: `infra/agentinfra/evidence.py:85`; AST `7cfe60e663a45ec3d904730a78c6d7712752216fe44d6944b4bed031f38458e5`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, result. Outputs/bindings: (none).
Calls/effect boundaries: require, result.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[3].value::Call

Source: `infra/agentinfra/evidence.py:85`; AST `2ade0fc4434151038826689b80920c8fa690ef69409d6d2d80ad29f1737eae2d`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, result. Outputs/bindings: (none).
Calls/effect boundaries: require, result.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[3].value.args[0].values[0].left::Call

Source: `infra/agentinfra/evidence.py:85`; AST `8abf622c79396d7fc6c5ebfb8c543fcf17fc9225dbeed2ed55a57027d5d991e8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[3].value.args[0].values[1].left::Call

Source: `infra/agentinfra/evidence.py:85`; AST `27c18dc9e36361ad373e3a25c80feb42fab1b867ec7169a27d35468d95c69b08`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[4]::Assign

Source: `infra/agentinfra/evidence.py:86`; AST `5d26eba15daf3b79206352142ca5efbf79dcdaac942ba1a7c8004982d2597390`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, result, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[4].value::Call

Source: `infra/agentinfra/evidence.py:86`; AST `6d44351ad18255c24e82f6a640cdc7297bdcf78fc07122c0048e238c1180903d`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, result, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[5]::Expr

Source: `infra/agentinfra/evidence.py:87`; AST `3c385d5c6c1c0f3cde1246f09044c2984a5ae3a720a5296aee77ece1961a02fd`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, require, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: require, state_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[5].value::Call

Source: `infra/agentinfra/evidence.py:87`; AST `dbce9960384257a4827cece382a74bd53bd2a0492002123f2f9c0c83cb17b27b`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, require, root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: require, state_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[5].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:87`; AST `eccff6c8ea4af8fd15ae1539f4c4a4018d8073f662bfcbfd0fc77ad346cd0e91`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, state_path. Outputs/bindings: (none).
Calls/effect boundaries: state_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[6]::Assign

Source: `infra/agentinfra/evidence.py:88`; AST `870b0b8ca2713db1bdb44112c56a068694cf377c9bb625bd407983773f678b2b`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, unseal. Outputs/bindings: receipt.
Calls/effect boundaries: unseal.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[6].value::Call

Source: `infra/agentinfra/evidence.py:88`; AST `568af2bc89ce861a8a6a796d7b6f2a9db1fd6cf14ffbe1799810f22aa8706cf0`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, unseal. Outputs/bindings: (none).
Calls/effect boundaries: unseal.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[7]::Expr

Source: `infra/agentinfra/evidence.py:89`; AST `05aca7c05952eacc5af155c8b3ab447921ccda39decee1653e4424c6a9082935`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[7].value::Call

Source: `infra/agentinfra/evidence.py:89`; AST `b5d2c46c85d1a910c619cc526e7ed1171898bc3f1d8b12165ea1d18bbf660317`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[8]::Assign

Source: `infra/agentinfra/evidence.py:90`; AST `dd12b57ffbef6ca1a29eaf118518d8501086a7931f35271afa6092c378c83c33`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: identity.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[9]::Expr

Source: `infra/agentinfra/evidence.py:91`; AST `db36b8d7327c6e85f3cd3d18c165fa8f0871eede7f5ba2bc404b6091ffcc1b61`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, identity, receipt, require, result. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[9].value::Call

Source: `infra/agentinfra/evidence.py:91`; AST `7934e168ce01fc9d23df063997d0d59244f17ff75115f28d42a2176a3602559d`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, identity, receipt, require, result. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[9].value.args[0].values[0].comparators[1]::Call

Source: `infra/agentinfra/evidence.py:91`; AST `bc03eedd743514881f3902c119b7ba433016f4bf981a6c10871bb821c2ab861d`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, identity. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[9].value.args[0].values[0].comparators[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[10]::Assign

Source: `infra/agentinfra/evidence.py:92`; AST `5db23fc69ff80892852897f7949826f7b4c662e25da5b1bfe3fd543293bb1469`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profile, receipt. Outputs/bindings: spec.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[11]::Expr

Source: `infra/agentinfra/evidence.py:93`; AST `5199d3e2fe22f4bad978cf7d9209a41c03ab0e192348c84cc443923ab08d66d4`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identity, require, root, str. Outputs/bindings: (none).
Calls/effect boundaries: require, str.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[11].value::Call

Source: `infra/agentinfra/evidence.py:93`; AST `2cbc84e2e425822bdda1d912b0c1b8582b3b331a4fac637d7257cb531052cca8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity, require, root, str. Outputs/bindings: (none).
Calls/effect boundaries: require, str.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[11].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:93`; AST `0558894338b4e37e4aaf64136b1647fc227573a783699714f1608da395993d9a`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[11].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[12]::Expr

Source: `infra/agentinfra/evidence.py:94`; AST `11a7eccff3365fda6d73c8c657f17b6ed588b2fffdb0cda28fcb3ce7cfd2eefd`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identity, receipt, require, root, source_snapshot, spec. Outputs/bindings: (none).
Calls/effect boundaries: identity.get, require, source_snapshot, spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[12].value::Call

Source: `infra/agentinfra/evidence.py:94`; AST `d53a8b63a2a069ea78fe734a160f4da0ef116de7a427aac8d6ad57d2501f3fb6`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity, receipt, require, root, source_snapshot, spec. Outputs/bindings: (none).
Calls/effect boundaries: identity.get, require, source_snapshot, spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[12].value.args[0].comparators[1]::Call

Source: `infra/agentinfra/evidence.py:94`; AST `274f621b9d1bae52c2312010c86880549a6bf645e5635eca226615b5333dfc2c`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity, root, source_snapshot, spec. Outputs/bindings: (none).
Calls/effect boundaries: identity.get, source_snapshot, spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].value.args[0].comparators[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[12].value.args[0].comparators[1].args[1]::Call

Source: `infra/agentinfra/evidence.py:94`; AST `4e224733c9549704a7c50b3afd0a6f69e8a059e0dce12ec25fceff1030604f7e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity, spec. Outputs/bindings: (none).
Calls/effect boundaries: identity.get, spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].value.args[0].comparators[1].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[12].value.args[0].comparators[1].args[1].args[1]::Call

Source: `infra/agentinfra/evidence.py:94`; AST `4b3b5d8904138ce99555d067c850e4f3f977358ed361cd2b645e85a39817eda7`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: spec. Outputs/bindings: (none).
Calls/effect boundaries: spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[12].value.args[0].comparators[1].args[1].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[13]::For

Source: `infra/agentinfra/evidence.py:95`; AST `57836a447b51ce9df82a76e823192647e2f5fa38edaaae19d24b31c1d1c700bf`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: confined_path, identity, name, previous, require, root, sha256_file. Outputs/bindings: name, previous.
Calls/effect boundaries: confined_path, identity.get, identity.get('proof_inputs', {}).items, require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[10].body[13]; no call, error or mutation may be omitted. Iteration: (name, previous) in identity.get('proof_inputs', {}).items()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[13].iter::Call

Source: `infra/agentinfra/evidence.py:95`; AST `5ac896a65df264c3d6240962406a40473c11a44b7c4d2a7a9ca71533fce85e96`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity. Outputs/bindings: (none).
Calls/effect boundaries: identity.get, identity.get('proof_inputs', {}).items.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[13].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[13].iter.func.value::Call

Source: `infra/agentinfra/evidence.py:95`; AST `85d8e48c38de1888e710ab3822a0f3d00a11a3a7d7de3addb3e0f960a8e13a8e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity. Outputs/bindings: (none).
Calls/effect boundaries: identity.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[13].iter.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[13].body[0]::Expr

Source: `infra/agentinfra/evidence.py:96`; AST `5812ccfdd9cb175cc11c0ac1759f351d195f7c398352a8a2113112df0e6502c3`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, name, previous, require, root, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[13].body[0].value::Call

Source: `infra/agentinfra/evidence.py:96`; AST `d9e04603745f4e24aaa0b3fef4e3796af305d0aa2b4cedbefc7ae84ee2a6e913`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, name, previous, require, root, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[13].body[0].value.args[0].left::Call

Source: `infra/agentinfra/evidence.py:96`; AST `65e16a26698962261c20cad68e9afec46870bb80c309fb612020d11d84d7d18d`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, name, root, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[13].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[13].body[0].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/evidence.py:96`; AST `84ad204db26e498c59a40ccefeec068f82fca59b0dd091cc081652642986ed46`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[13].body[0].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[14]::Expr

Source: `infra/agentinfra/evidence.py:97`; AST `db55a445e7e9ef7fc51c864dd8c87d386bcb1e2e87ff0b53cd5c84e989683c1b`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PROFILE, identity, require, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[14].value::Call

Source: `infra/agentinfra/evidence.py:97`; AST `f078dc849eccecc1deee391367b1233201abe524bf2f50b9d1bebed2dcdeb5e7`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PROFILE, identity, require, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[14].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:97`; AST `0fa0a7c40051ecebbe8e9e47f0e1b89d521bd99bf613d3383d6031cfaf6baeed`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PROFILE, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[14].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[15]::Expr

Source: `infra/agentinfra/evidence.py:98`; AST `fe4a64a7536dae1dd94fb4f293ac73f923d533cbb26ca0ce6f681df2dad38395`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, identity, require, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).with_name, require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[15].value::Call

Source: `infra/agentinfra/evidence.py:98`; AST `56b5ec5bf7469f710750e25efb6c407835913f98d7595539ddb98f1224bdf5d0`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, identity, require, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).with_name, require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[15].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:98`; AST `3f23b10f43195da95c3abed4a48a7a34c6e579a35ff777de7a89ff8e2fa6f316`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).with_name, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[15].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[15].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/evidence.py:98`; AST `e66b22593b98d7096f8afabfce489aab2430876dcd257dad362605a0e8266106`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).with_name.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[15].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[15].value.args[0].comparators[0].args[0].func.value::Call

Source: `infra/agentinfra/evidence.py:98`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[15].value.args[0].comparators[0].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[16]::Expr

Source: `infra/agentinfra/evidence.py:99`; AST `b222ec630f3a642ef4b6f37eb855c7223093c4d93d73b1398e91c627138dc4d7`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, digest, identity, p, require, sha256_file, sorted. Outputs/bindings: p.
Calls/effect boundaries: Path, Path(__file__).parent.glob, digest, require, sha256_file, sorted.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[16].value::Call

Source: `infra/agentinfra/evidence.py:99`; AST `afb26666a642f7ea41c3458fd72078fa6b4873179365e6c84ca13764b05b6459`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, digest, identity, p, require, sha256_file, sorted. Outputs/bindings: p.
Calls/effect boundaries: Path, Path(__file__).parent.glob, digest, require, sha256_file, sorted.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[16].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:99`; AST `65f30002cbb97151a6205ece5e97d1cb7bcdb7af3ded22f48cf0cfe4b4175f9e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, digest, p, sha256_file, sorted. Outputs/bindings: p.
Calls/effect boundaries: Path, Path(__file__).parent.glob, digest, sha256_file, sorted.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[16].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[16].value.args[0].comparators[0].args[0]::DictComp

Source: `infra/agentinfra/evidence.py:99`; AST `c9f59209d6c0d38f31b4623cbd9025338e571b045b5fd81ff535b6cafb484eed`.

Rust module: `infra::agentinfra::evidence`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: Path, __file__, p, sha256_file, sorted. Outputs/bindings: p.
Calls/effect boundaries: Path, Path(__file__).parent.glob, sha256_file, sorted.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered DictComp evaluation at root.body[10].body[16].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[16].value.args[0].comparators[0].args[0].value::Call

Source: `infra/agentinfra/evidence.py:99`; AST `10ff965a98abd23dad94b70fab85cccd23b07ff31fab5f20e7d34b872a90d58a`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[16].value.args[0].comparators[0].args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[16].value.args[0].comparators[0].args[0].generators[0].iter::Call

Source: `infra/agentinfra/evidence.py:99`; AST `1b1be6b7301fe6fb2861595016d372f7f9464eb7c987745116f8d4f6863322f3`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, sorted. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).parent.glob, sorted.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[16].value.args[0].comparators[0].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[16].value.args[0].comparators[0].args[0].generators[0].iter.args[0]::Call

Source: `infra/agentinfra/evidence.py:99`; AST `926fcef66035113a543c591d5e52a14943908a47c6acb65f1801ff09d0ba60e9`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).parent.glob.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[16].value.args[0].comparators[0].args[0].generators[0].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[16].value.args[0].comparators[0].args[0].generators[0].iter.args[0].func.value.value::Call

Source: `infra/agentinfra/evidence.py:99`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[16].value.args[0].comparators[0].args[0].generators[0].iter.args[0].func.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[17]::Assign

Source: `infra/agentinfra/evidence.py:100`; AST `edaf653a3892cec250f9c921796c1a097c4bb0951cd3d6e7cae46bdf51ec19a1`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, identity, root. Outputs/bindings: env.
Calls/effect boundaries: environment.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[17].value::Call

Source: `infra/agentinfra/evidence.py:100`; AST `ba76b982d9671407fa0cb36aa839f305b594c583391350247421afa51f983a61`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: environment, identity, root. Outputs/bindings: (none).
Calls/effect boundaries: environment.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[18]::Assign

Source: `infra/agentinfra/evidence.py:101`; AST `14ed4960e9b788c467a2c2867eebacd82ded15d44520b0336b842f147fb4a087`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identity. Outputs/bindings: external_paths.
Calls/effect boundaries: identity.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[18].value::Call

Source: `infra/agentinfra/evidence.py:101`; AST `d09ce5eedbad1a60b32b74116ac15ed760ebb38d9362e681eedbeadeeaf0f840`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity. Outputs/bindings: (none).
Calls/effect boundaries: identity.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19]::For

Source: `infra/agentinfra/evidence.py:102`; AST `e6ee56d80e98fc9ef422d5ee8748880efe8b6a93e1ee33e97313507d87290b1f`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, current, env, external_paths, identity, name, previous, require, sha256_file, source, source_snapshot, str. Outputs/bindings: current, name, previous, source.
Calls/effect boundaries: Path, identity['external'].items, require, sha256_file, source_snapshot, str.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[10].body[19]; no call, error or mutation may be omitted. Iteration: (name, previous) in identity['external'].items()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].iter::Call

Source: `infra/agentinfra/evidence.py:102`; AST `12b1d4fe17db96439c63413dc67ac276d7ba5241e9341f726c6a51b158afd0a9`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity. Outputs/bindings: (none).
Calls/effect boundaries: identity['external'].items.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[19].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[0]::Expr

Source: `infra/agentinfra/evidence.py:103`; AST `5f241476133d612cd9d2a5e5c49e9b0e47f31ec06b33b067376eb15cbeb5d5bc`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: external_paths, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[0].value::Call

Source: `infra/agentinfra/evidence.py:103`; AST `10d8e6caaa26f6066206742621a56ef6139ad056cff7d857230a040b5ada290a`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: external_paths, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[1]::Assign

Source: `infra/agentinfra/evidence.py:104`; AST `0161daa5a605e120cc33410bf3c208eff05384c21a1e03dbe36889d584f9802f`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, external_paths, name. Outputs/bindings: source.
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[1].value::Call

Source: `infra/agentinfra/evidence.py:104`; AST `27ccbca57c782c983bdb1a552d3bff15db08f060aab692e3e3f6b865db90e6e0`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, external_paths, name. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[19].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[2]::Assign

Source: `infra/agentinfra/evidence.py:105`; AST `e1570d12ab8f6f8580a49b6898a04ca943c2a316cfd6f485e7c730d9b449c4c1`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, sha256_file, source, source_snapshot. Outputs/bindings: current.
Calls/effect boundaries: sha256_file, source_snapshot.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[2].value.body::Call

Source: `infra/agentinfra/evidence.py:105`; AST `7c3bc417991c21c12653dd6c537b5116c5c21119aee629946070ba38aa54e260`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sha256_file, source. Outputs/bindings: (none).
Calls/effect boundaries: sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[19].body[2].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[2].value.orelse::Call

Source: `infra/agentinfra/evidence.py:105`; AST `ec5793596c059480d97d9b073a274735151a473af13d5521e89e90d42d5c0ebd`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source, source_snapshot. Outputs/bindings: (none).
Calls/effect boundaries: source_snapshot.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[19].body[2].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[3]::Expr

Source: `infra/agentinfra/evidence.py:106`; AST `5b904bfc052224ef9f6d82426fe94a83cd30287845ee59baeab80afa2e0449f3`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, previous, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[19].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[3].value::Call

Source: `infra/agentinfra/evidence.py:106`; AST `69787aa0c80251c967360788567722f122ff0fe634b1d243d0e65bfe71f46df5`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, previous, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[19].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[4]::If

Source: `infra/agentinfra/evidence.py:107`; AST `4f4d5d3b612cb0f8a3450eed12cc379ff858a5f60ae757d8a0f44b86aa74373e`.

Rust module: `infra::agentinfra::evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: env, name, source, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered If evaluation at root.body[10].body[19].body[4]; no call, error or mutation may be omitted. Condition: name == 'library'
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[4].body[0]::Assign

Source: `infra/agentinfra/evidence.py:108`; AST `e21fd6a7db5c672a5774354fc45ee1a337d2c98316c6f882c09a8b8447d1e6c6`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, source, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[19].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[19].body[4].body[0].value::Call

Source: `infra/agentinfra/evidence.py:108`; AST `e84c9c7864af0fee24e28123120dae12990caa3a9145d280b7a0f55e8d6cb247`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[19].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[20]::Expr

Source: `infra/agentinfra/evidence.py:109`; AST `15826c75d4961cd6f18c9adc05691b73ca4f5d540c3493d9d042361277da2e7c`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, env, identity, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[20].value::Call

Source: `infra/agentinfra/evidence.py:109`; AST `fb1eec0cc0af0961ea043059a44c235caffc72497dc1a4ee699ad79ddc3a5e1e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, env, identity, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[20].value.args[0].left::Call

Source: `infra/agentinfra/evidence.py:109`; AST `98fee4591edd6b760f3915fde96e05d33704e53d725aa3fe4c770dd99831108e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, env. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[20].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21]::For

Source: `infra/agentinfra/evidence.py:110`; AST `a7e129747a34f76e31e5573f270d6bbc4bd01f6ba974bf4bd5660ccf81e729cd`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, identity, require, sha256_file, tool. Outputs/bindings: tool.
Calls/effect boundaries: Path, Path(tool['path']).is_file, identity['tools'].values, require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[10].body[21]; no call, error or mutation may be omitted. Iteration: tool in identity['tools'].values()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21].iter::Call

Source: `infra/agentinfra/evidence.py:110`; AST `0909c58f86fb3039c15083f7d2175f4cbce5822a0d4eb88ac0deb2629409865a`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity. Outputs/bindings: (none).
Calls/effect boundaries: identity['tools'].values.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[21].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21].body[0]::Expr

Source: `infra/agentinfra/evidence.py:111`; AST `84023fd419b70fdfbf28ccb42880f71203c54691bbe0ce53f12d83806db4e768`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, require, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(tool['path']).is_file, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21].body[0].value::Call

Source: `infra/agentinfra/evidence.py:111`; AST `31f35f80b8c8f953bb19e26bc65a644c1ed1d2762f22f75c09c9a08b176980a7`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, require, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(tool['path']).is_file, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[21].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21].body[0].value.args[0]::Call

Source: `infra/agentinfra/evidence.py:111`; AST `b084c33b62ebdcf75f0cc3f624a2edf4911c00a31a0d3eda7c76b7a5100c1fee`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(tool['path']).is_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[21].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21].body[0].value.args[0].func.value::Call

Source: `infra/agentinfra/evidence.py:111`; AST `3187e6c8320fa972bf5c8b61411bec3c23606724c7b8dd3b88d43927a6acf91b`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[21].body[0].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21].body[1]::Expr

Source: `infra/agentinfra/evidence.py:112`; AST `065ecee66ba1adb290353475b41257a3cc5319aecbacb87ac8260703c7d495f7`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, require, sha256_file, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path, require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[21].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21].body[1].value::Call

Source: `infra/agentinfra/evidence.py:112`; AST `fefe833517669f12ffba3064288d0f3fae461ba63b27f8255c6efbfa271396af`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, require, sha256_file, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path, require, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[21].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21].body[1].value.args[0].left::Call

Source: `infra/agentinfra/evidence.py:112`; AST `71b6611f5fda93081d4709bfa19027b3f3a0dfbc81d77e841b55f17ef52edc68`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, sha256_file, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path, sha256_file.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[21].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[21].body[1].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/evidence.py:112`; AST `3187e6c8320fa972bf5c8b61411bec3c23606724c7b8dd3b88d43927a6acf91b`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, tool. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[21].body[1].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[22]::Expr

Source: `infra/agentinfra/evidence.py:113`; AST `ce6ae03567eb0e152a26b8bc40bd75f7985e24a07f30c27286900243942ee27e`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, identity, profile, receipt, require, root, tool_payload. Outputs/bindings: (none).
Calls/effect boundaries: identity.get, require, tool_payload.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[22].value::Call

Source: `infra/agentinfra/evidence.py:113`; AST `9d6d13d1ecca3de66c2e58db6ecb21dc3956eecc47995dfe60bba9090fd9feac`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env, identity, profile, receipt, require, root, tool_payload. Outputs/bindings: (none).
Calls/effect boundaries: identity.get, require, tool_payload.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[22].value.args[0].left::Call

Source: `infra/agentinfra/evidence.py:113`; AST `40f5897ac071e47eada311161057482b988e039923d94b38d652e59ae8d646a4`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity. Outputs/bindings: (none).
Calls/effect boundaries: identity.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[22].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[22].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:113`; AST `a7d940c56b20ec100d914e93a576d5218f5aac23eb74edfd63043b54da8fdd52`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env, identity, profile, receipt, root, tool_payload. Outputs/bindings: (none).
Calls/effect boundaries: tool_payload.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[22].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[23]::Assign

Source: `infra/agentinfra/evidence.py:115`; AST `da87c5a5a6a8d79fd4c6fc830d00dd5a431d385c38cd0f48e9111dcf224690b1`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: probes.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[24]::Expr

Source: `infra/agentinfra/evidence.py:116`; AST `5de446826c9d777db69f98b31a87dd18ef4f54a2abf7944fb63493371d057a57`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identity, require, spec. Outputs/bindings: (none).
Calls/effect boundaries: identity.get, require, spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[24]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[24].value::Call

Source: `infra/agentinfra/evidence.py:116`; AST `7bf3e6e1032d11aa13799a561d6bd0e70e77a50dc7c2d9bc23dd01f033bf3c43`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity, require, spec. Outputs/bindings: (none).
Calls/effect boundaries: identity.get, require, spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[24].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[24].value.args[0].left::Call

Source: `infra/agentinfra/evidence.py:116`; AST `c2a6f6be158f4563f1184884d393a8ff19e5d7b95f5532c94573a1437dc738b4`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity. Outputs/bindings: (none).
Calls/effect boundaries: identity.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[24].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[24].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:116`; AST `28e2d49fb31827d8e61e35e2ab40b49c241d0d678bc013c4c899889c7b9815a8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: spec. Outputs/bindings: (none).
Calls/effect boundaries: spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[24].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[25]::Expr

Source: `infra/agentinfra/evidence.py:117`; AST `7d34db8301db5430d5a67d762589c7d0d9c823fef187aca6b6e44ad1fe192a53`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, probes, require, spec. Outputs/bindings: (none).
Calls/effect boundaries: len, require, spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[25]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[25].value::Call

Source: `infra/agentinfra/evidence.py:117`; AST `c3bc3c4aafbdf0fa950f8b841f4884f1e56f60fc214ae372ed697954eafc6e7b`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, probes, require, spec. Outputs/bindings: (none).
Calls/effect boundaries: len, require, spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[25].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[25].value.args[0].left::Call

Source: `infra/agentinfra/evidence.py:117`; AST `a4e9c8de625b3af0a834d64d567a1e5166b7fe24b370323c31243c7b7d8d2246`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, probes. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[25].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[25].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:117`; AST `9eaef7a0ba21d8d98180c531cb1d7682646bdd03b1c4e28b10813db5dd91f3ae`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, spec. Outputs/bindings: (none).
Calls/effect boundaries: len, spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[25].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[25].value.args[0].comparators[0].args[0]::Call

Source: `infra/agentinfra/evidence.py:117`; AST `28e2d49fb31827d8e61e35e2ab40b49c241d0d678bc013c4c899889c7b9815a8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: spec. Outputs/bindings: (none).
Calls/effect boundaries: spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[25].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[26]::For

Source: `infra/agentinfra/evidence.py:118`; AST `e4ad032b8c06400ce3be73b127486d861e2d2dedd1143238649b591b3b2af76a`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: expected, matches_version, probe, probes, require, spec, zip. Outputs/bindings: expected, probe.
Calls/effect boundaries: matches_version, require, spec.get, zip.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[10].body[26]; no call, error or mutation may be omitted. Iteration: (probe, expected) in zip(probes, spec.get('expect', []))
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[26].iter::Call

Source: `infra/agentinfra/evidence.py:118`; AST `8d9b4683b740d19ceec7e5c59a86a185d6dfe7ed420c99f532425e875b587554`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: probes, spec, zip. Outputs/bindings: (none).
Calls/effect boundaries: spec.get, zip.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[26].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[26].iter.args[1]::Call

Source: `infra/agentinfra/evidence.py:118`; AST `28e2d49fb31827d8e61e35e2ab40b49c241d0d678bc013c4c899889c7b9815a8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: spec. Outputs/bindings: (none).
Calls/effect boundaries: spec.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[26].iter.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[26].body[0]::Expr

Source: `infra/agentinfra/evidence.py:119`; AST `2fed414f7cf7ae03aa4294e1e2386c40ece921b17c6d73ac2cc615d20eb7f06e`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, matches_version, probe, require. Outputs/bindings: (none).
Calls/effect boundaries: matches_version, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[26].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[26].body[0].value::Call

Source: `infra/agentinfra/evidence.py:119`; AST `459c09e5c2ca9879e07e26bbd7d5763dee0f5a891139d858b6e61f0a9db4a57e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, matches_version, probe, require. Outputs/bindings: (none).
Calls/effect boundaries: matches_version, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[26].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[26].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/evidence.py:119`; AST `90b785ddb821808f1c02ac3845497495e476c71446331f57607e7fd823229179`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, matches_version, probe. Outputs/bindings: (none).
Calls/effect boundaries: matches_version.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[26].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[27]::Assign

Source: `infra/agentinfra/evidence.py:120`; AST `79eaf35a42ed827caac6856a2b0168b3fb2e9e79b0023fe784a040e75c38ac23`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: outputs.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[27]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[28]::Expr

Source: `infra/agentinfra/evidence.py:121`; AST `12ee56295e429c3725cc712b32e6f3a1c02e1e127c7291cd081056280bd2e011`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, identity, outputs, require. Outputs/bindings: c.
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[28]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[28].value::Call

Source: `infra/agentinfra/evidence.py:121`; AST `5e9496622f385f8c4e60001787fad21f503c9389baf2f46da31a4d738f98be0f`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, identity, outputs, require. Outputs/bindings: c.
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[28].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[28].value.args[0].values[1].left::ListComp

Source: `infra/agentinfra/evidence.py:121`; AST `1ad7813bba08530c7d6e5989704d1ac850ed4b03acc8961147f2f625de8624b2`.

Rust module: `infra::agentinfra::evidence`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: c, outputs. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ListComp evaluation at root.body[10].body[28].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[29]::For

Source: `infra/agentinfra/evidence.py:122`; AST `9cb5c56207cea6badbd8baf6c4061b4c42db7e1fad972d66355762da590b774d`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: any, command, k, outputs, require. Outputs/bindings: command, k.
Calls/effect boundaries: any, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[10].body[29]; no call, error or mutation may be omitted. Iteration: command in outputs
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[29].body[0]::Expr

Source: `infra/agentinfra/evidence.py:123`; AST `8e1e7f71625ffff478e0a14556d3e77961aa5cd4378628abc04c957b00d16428`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, command, k, require. Outputs/bindings: k.
Calls/effect boundaries: any, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[29].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[29].body[0].value::Call

Source: `infra/agentinfra/evidence.py:123`; AST `ea13149953cc4c0ae2e96a34aeebed15b539b23a5c06f631fdbc25afcc47858b`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, command, k, require. Outputs/bindings: k.
Calls/effect boundaries: any, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[29].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[29].body[0].value.args[0].values[1].operand::Call

Source: `infra/agentinfra/evidence.py:123`; AST `d01a29b31344ad5a078e0e17bfcea9cc9c79f576f0075645008c61d736284056`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, command, k. Outputs/bindings: k.
Calls/effect boundaries: any.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[29].body[0].value.args[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[29].body[0].value.args[0].values[1].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/evidence.py:123`; AST `e3c8a7a0a991e0584bb44da1bef01b667a159bf94b4ef2e108271dc5c8632553`.

Rust module: `infra::agentinfra::evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: command, k. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[10].body[29].body[0].value.args[0].values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::current_receipt::root.body[10].body[30]::Return

Source: `infra/agentinfra/evidence.py:124`; AST `9b378eb582403574e9c02456d9dbe8d3ccc96e049aa98ec3ceee97d8b1bff879`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[10].body[30]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11]::FunctionDef

Source: `infra/agentinfra/evidence.py:127`; AST `d2d983597375f51259e359a88b5ac55bc0cc643b260578593bce17014b7c55bb`.

Rust module: `infra::agentinfra::evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, actual, c, candidates, int, kani_properties, location, manifest_root, name, obligation, p, properties, re, receipt, require, root, row, scope, witness. Outputs/bindings: actual, c, candidates, location, manifest_root, name, p, properties, row, scope, witness.
Calls/effect boundaries: '\n'.join, (root / witness['file']).resolve, Path, actual.is_absolute, int, kani_properties, obligation.get, p.resolve, properties.get, re.fullmatch, require, row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[0]::Expr

Source: `infra/agentinfra/evidence.py:128`; AST `1f1b169dac2279e912c182c02943d273c75a21389c0df48fc15f6112d4f925ad`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[1]::Assign

Source: `infra/agentinfra/evidence.py:133`; AST `69af81a87bbaa6742b5a8547f9600d95ee8116ec1f25d9af4ba6a97f3e2a24ac`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation. Outputs/bindings: scope.
Calls/effect boundaries: obligation.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[1].value::Call

Source: `infra/agentinfra/evidence.py:133`; AST `772f7787041ada1056d843bc24609c2b849eafbdae460f70f8699ae65e50a570`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[2]::If

Source: `infra/agentinfra/evidence.py:134`; AST `ace8c62eea2332f8c707fa5009a69872d5fc79773af9517d42ed371a6c0f9c21`.

Rust module: `infra::agentinfra::evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: scope. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered If evaluation at root.body[11].body[2]; no call, error or mutation may be omitted. Condition: not scope
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[2].body[0]::Return

Source: `infra/agentinfra/evidence.py:135`; AST `e9723d4cabc24849fbe1bf6450789cc4f95cd2fc6104809ec0a254a07d0723bb`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[3]::Assign

Source: `infra/agentinfra/evidence.py:136`; AST `2fd9a8cbcdcedc05e68e42dc183cb3f8c11057bfc6566aae651fd8ec7aab491d`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, kani_properties, receipt. Outputs/bindings: c, properties.
Calls/effect boundaries: '\n'.join, kani_properties.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[3].value::Call

Source: `infra/agentinfra/evidence.py:136`; AST `4079370d592fcb3f4d84331cbf7dee5b7c4bfacc7cd2a3bab8120caa1de194f8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, kani_properties, receipt. Outputs/bindings: c.
Calls/effect boundaries: '\n'.join, kani_properties.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[3].value.args[0]::Call

Source: `infra/agentinfra/evidence.py:136`; AST `97fd48d0adc00f1fe41caac8ea500302a1b3cccedd68154572817f06f6914aa6`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, receipt. Outputs/bindings: c.
Calls/effect boundaries: '\n'.join.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[3].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/evidence.py:136`; AST `99301bd55520cd17935d43f9d763a96f3c2135e544e4322b050c98113c0607f1`.

Rust module: `infra::agentinfra::evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, receipt. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[3].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[4]::For

Source: `infra/agentinfra/evidence.py:137`; AST `1aae83b9304fbd543c8505a4a27201a2e89446954a61245ebd8d94313609d428`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: name, properties, require, scope. Outputs/bindings: name.
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[11].body[4]; no call, error or mutation may be omitted. Iteration: name in scope['assertion_properties']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[4].body[0]::Expr

Source: `infra/agentinfra/evidence.py:138`; AST `b2615f9681b6207472cc706024568869a2a26d92dbe4bc2aa812a9c0868ec5a5`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, properties, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[4].body[0].value::Call

Source: `infra/agentinfra/evidence.py:138`; AST `28a81a998b1f4479c017de87e0044622fa63040bacb182cf0aa62e129febd6ea`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, properties, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5]::For

Source: `infra/agentinfra/evidence.py:139`; AST `73d511a77f1dd1c35cc4c9711c5619286adaf8e4322742319077f139b87d305d`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, actual, candidates, int, location, manifest_root, obligation, p, properties, re, require, root, row, scope, witness. Outputs/bindings: actual, candidates, location, manifest_root, p, row, witness.
Calls/effect boundaries: (root / witness['file']).resolve, Path, actual.is_absolute, int, obligation.get, p.resolve, properties.get, re.fullmatch, require, row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[11].body[5]; no call, error or mutation may be omitted. Iteration: witness in scope['reachability']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[0]::Assign

Source: `infra/agentinfra/evidence.py:140`; AST `a5791dfc5136cb2d53f646971fbbeccee8ec726f8443b06c4e29cff3850a81cf`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: properties, witness. Outputs/bindings: row.
Calls/effect boundaries: properties.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[0].value::Call

Source: `infra/agentinfra/evidence.py:140`; AST `cfc44988c9eee6b889a9cd1904c25a36fd996cfff31f76532863112311509526`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: properties, witness. Outputs/bindings: (none).
Calls/effect boundaries: properties.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[1]::Expr

Source: `infra/agentinfra/evidence.py:141`; AST `068bd8ec1770e0a1ea830da0f56964ecb8c6e3d07c077a2bb7ca45bb4d5a118f`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, row. Outputs/bindings: (none).
Calls/effect boundaries: require, row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[1].value::Call

Source: `infra/agentinfra/evidence.py:141`; AST `b9d1f44ec5e2bd57ca32a87878e6cf9a91e9b676524e27a9808a5c387ce79910`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, row. Outputs/bindings: (none).
Calls/effect boundaries: require, row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[1].value.args[0].left::Call

Source: `infra/agentinfra/evidence.py:141`; AST `133827c6985e23650f6e3c8f21916694f50c70ccde4fb02b8d4f8f5bc3278b30`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row. Outputs/bindings: (none).
Calls/effect boundaries: row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[2]::Assign

Source: `infra/agentinfra/evidence.py:142`; AST `6e9701650c9ee0957271bbb4e9e052bba985d6b54ca9905d9045a5d9e8c4a1cb`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: re, row. Outputs/bindings: location.
Calls/effect boundaries: re.fullmatch, row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[2].value::Call

Source: `infra/agentinfra/evidence.py:142`; AST `62e70bf61b1fa57b82f69447fa194bfb68bffa47731d9ea8b8d87114332a42a3`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re, row. Outputs/bindings: (none).
Calls/effect boundaries: re.fullmatch, row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[2].value.args[1]::Call

Source: `infra/agentinfra/evidence.py:142`; AST `55d67da988036a292ee7f67fa87366a11399528c56d3a171e15a77758562753d`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row. Outputs/bindings: (none).
Calls/effect boundaries: row.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[3]::Expr

Source: `infra/agentinfra/evidence.py:143`; AST `ea54dc14ea7a68202fe220c83a95c1ef1a084410f2b88844d3eefbcbe2a98a71`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: location, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[3].value::Call

Source: `infra/agentinfra/evidence.py:143`; AST `313a5ba0ebb3b61dcddc16da3b1458358d4e7e0c9d8b998803d043bded45af9b`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: location, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[4]::Assign

Source: `infra/agentinfra/evidence.py:144`; AST `8c230d8f17abb54392a64560b87cc8f4a4115dba2ccc9aa2caf53d298a12dff3`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, location. Outputs/bindings: actual.
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[4].value::Call

Source: `infra/agentinfra/evidence.py:144`; AST `4477dbdf4e121e4f9cb656ad66aaa7aa5c84c7897d9507c5335b2f724b027602`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, location. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[5]::Assign

Source: `infra/agentinfra/evidence.py:146`; AST `68b6ebf701edf5c474d53e84eb62ef047d241385e1de4361709b55e4ba06a61d`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: obligation, root. Outputs/bindings: manifest_root.
Calls/effect boundaries: obligation.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[5].value.value.right::Call

Source: `infra/agentinfra/evidence.py:146`; AST `94f2d35bc9df1e595e42888181d2b0a52cb928808a0dc031e182369f66732863`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: obligation. Outputs/bindings: (none).
Calls/effect boundaries: obligation.get.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].value.value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[6]::Assign

Source: `infra/agentinfra/evidence.py:147`; AST `01ec14d5e721bccf7787df520c557f5a4e6a777bf87ea3688529817e0cd279f0`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: actual, manifest_root, root. Outputs/bindings: candidates.
Calls/effect boundaries: actual.is_absolute.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[6].value.test::Call

Source: `infra/agentinfra/evidence.py:147`; AST `9d49711554b9e93085ead4996602b7a6f9b3ba2dc1d0b7d780936a8a4f96dbbe`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: actual. Outputs/bindings: (none).
Calls/effect boundaries: actual.is_absolute.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[6].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[7]::Expr

Source: `infra/agentinfra/evidence.py:148`; AST `bfd982ec5f100a201ca6910b91812a45cb3e691e07217da049449a41f1b2bfd4`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidates, int, location, p, require, root, witness. Outputs/bindings: p.
Calls/effect boundaries: (root / witness['file']).resolve, int, p.resolve, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[7].value::Call

Source: `infra/agentinfra/evidence.py:148`; AST `c6965462cfb199c6014cf5872eae58a2b1207023d35df19e5d6b1830540e350f`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidates, int, location, p, require, root, witness. Outputs/bindings: p.
Calls/effect boundaries: (root / witness['file']).resolve, int, p.resolve, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[7].value.args[0].values[0].left::Call

Source: `infra/agentinfra/evidence.py:148`; AST `d228b7785971d4d90c555b19ab0d68af1c615d4240fec0b8f8eaa6f93f572a56`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, witness. Outputs/bindings: (none).
Calls/effect boundaries: (root / witness['file']).resolve.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[7].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[7].value.args[0].values[0].comparators[0]::SetComp

Source: `infra/agentinfra/evidence.py:148`; AST `00ee9109cad4e1c42c48bd951bc356c72fc264fb9d3fc84865f8d29ed0c5998c`.

Rust module: `infra::agentinfra::evidence`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: candidates, p. Outputs/bindings: p.
Calls/effect boundaries: p.resolve.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered SetComp evaluation at root.body[11].body[5].body[7].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[7].value.args[0].values[0].comparators[0].elt::Call

Source: `infra/agentinfra/evidence.py:148`; AST `a3ffa2b755523fc92066faf5b28922c57bb2971d1c1c71e228be26019623d604`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.resolve.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[7].value.args[0].values[0].comparators[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[5].body[7].value.args[0].values[1].left::Call

Source: `infra/agentinfra/evidence.py:149`; AST `2b0d42663eac444e6e5d0a1a7893e020ad33436c2974115c25d8f552f58158d4`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, location. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[7].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::classified::root.body[11].body[6]::Return

Source: `infra/agentinfra/evidence.py:150`; AST `334d41cf60d33801b3b7c4f22d59207a02346bfe305862d10291bce610b172e2`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: scope. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12]::FunctionDef

Source: `infra/agentinfra/evidence.py:153`; AST `e4fbc541aa82979e0f154f72b7e73404aa7759c5c4d22cd03813d746d7c2b856`.

Rust module: `infra::agentinfra::evidence`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, cache_key, command, confined_path, counts, current_receipt, digest, exact_keys, int, len, list, manifest, observation, out, profile, prose, re, read, receipt, receipts, record, require, root, rows, s, scenarios, set, successful, type, value. Outputs/bindings: cache_key, command, counts, observation, out, receipt, receipts, record, rows, s, scenarios, successful, value.
Calls/effect boundaries: all, confined_path, current_receipt, digest, exact_keys, int, len, prose, re.findall, re.search, read, require, rows.append, set, successful.update, type.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[0]::Expr

Source: `infra/agentinfra/evidence.py:154`; AST `d25f34b73d7181f9267a905519fbf6b8666cbbc5b433720ec627d2b2fab9b7cc`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[1]::ImportFrom

Source: `infra/agentinfra/evidence.py:155`; AST `b220687befa27ec1712e3119a9820102c7041681cf42733ab5784bb9bea6085f`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[2]::Assign

Source: `infra/agentinfra/evidence.py:156`; AST `567adfa380a10fdfb2a6f9df3c18365b087eef7160ff9f6f785ff1ecbd432fd7`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, manifest, read, root. Outputs/bindings: value.
Calls/effect boundaries: confined_path, read.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[2].value::Call

Source: `infra/agentinfra/evidence.py:156`; AST `29cc51acee4655d03334762b2c1b8e2acb7f5640b772ac4325ea7b68e911025c`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, manifest, read, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[2].value.args[0]::Call

Source: `infra/agentinfra/evidence.py:156`; AST `ad2e214a5b2c2cd30ce438762ddb010dff8704c7232cb5eb489dedb01b601e67`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, manifest, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[3]::Expr

Source: `infra/agentinfra/evidence.py:157`; AST `3ccc84a82211cb879c58b66ee6f24de3fcee3eb873473105cfb5eae5cbe28149`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exact_keys, value. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[3].value::Call

Source: `infra/agentinfra/evidence.py:157`; AST `2cc075d2ee460bfa7d05ab4bf9e903a42ba77e78f88a4a422b90a0fadb6f583e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exact_keys, value. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[4]::Expr

Source: `infra/agentinfra/evidence.py:158`; AST `b12c9040f1ffbaeafe95fa92ac6503d8f911c0b08af9d6108c0e0d337f02cccf`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, list, require, type, value. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[4].value::Call

Source: `infra/agentinfra/evidence.py:158`; AST `77677747ab2b3871644c6c7d6114fdeaf3eaabb4070a623d1f0f1b293621509e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, list, require, type, value. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[4].value.args[0].values[1].left::Call

Source: `infra/agentinfra/evidence.py:158`; AST `83baffc14b2c85ba97c7b125b58cad72b3b07ed8c07c5e308d985765714c4279`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, value. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[4].value.args[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:158`; AST `5d793e7c92d96e005279a122942765c23a0708c80215f30750f2375a1c6060f4`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, value. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value.args[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[5]::Assign

Source: `infra/agentinfra/evidence.py:159`; AST `930f294e6e01b98d7f3df797fbe91f21f79126860ec495b62f4f48db2af7487c`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: receipts, rows.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6]::For

Source: `infra/agentinfra/evidence.py:160`; AST `82511779bcaf787350e026f1e61df30009af24efafafeca0b6767e3b4d49bcc6`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: all, cache_key, command, counts, current_receipt, digest, exact_keys, int, len, list, observation, out, profile, prose, re, receipt, receipts, record, require, root, rows, s, scenarios, set, successful, type, value. Outputs/bindings: cache_key, command, counts, observation, out, receipt, record, s, scenarios, successful.
Calls/effect boundaries: all, current_receipt, digest, exact_keys, int, len, prose, re.findall, re.search, require, rows.append, set, successful.update, type.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[12].body[6]; no call, error or mutation may be omitted. Iteration: record in value['records']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[0]::Expr

Source: `infra/agentinfra/evidence.py:161`; AST `f5a9e870b4c7b68adb60d70a0bffa33f9654f5329f3f41f4d756feb8290c8c34`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exact_keys, record. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[0].value::Call

Source: `infra/agentinfra/evidence.py:161`; AST `e0fdf5bb41c44894c271ec6d1ea8da5aa9a8299135e3ed99445cc7520c077c2e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exact_keys, record. Outputs/bindings: (none).
Calls/effect boundaries: exact_keys.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[1]::Expr

Source: `infra/agentinfra/evidence.py:162`; AST `d1e8e7d1eef5311e98ec41f0b159bd6b839ea0d8b2fc8d36ffd84b1258ef518f`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prose, record. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[1].value::Call

Source: `infra/agentinfra/evidence.py:162`; AST `08a57ec79a2f7c11e28b3e4e487089f5207b3966fa0796b4786250b79d9b5f87`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: prose, record. Outputs/bindings: (none).
Calls/effect boundaries: prose.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[2]::Assign

Source: `infra/agentinfra/evidence.py:163`; AST `af332794f90fc96f87e89534c06b86044e6dcb72eb2b95078ce9de8267fe414d`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: observation.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[3]::Assign

Source: `infra/agentinfra/evidence.py:164`; AST `4852206c18411b9f6e13689b496f8e99db05e381a40db8954f20e882510a3279`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, observation. Outputs/bindings: cache_key.
Calls/effect boundaries: digest.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[3].value::Call

Source: `infra/agentinfra/evidence.py:164`; AST `1af2dcd5f19d85a8db08951a0b972298a6efa0e6a519bf5bdfb56892001b494c`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, observation. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4]::If

Source: `infra/agentinfra/evidence.py:165`; AST `9c2beef649532d69e0faa237e9e6faf0638cd2a9ae66c8d98a100797cb018f14`.

Rust module: `infra::agentinfra::evidence`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: cache_key, command, counts, current_receipt, int, len, observation, out, profile, re, receipt, receipts, require, root, scenarios, set, successful. Outputs/bindings: command, counts, out, receipt, scenarios, successful.
Calls/effect boundaries: current_receipt, int, len, re.findall, re.search, require, set, successful.update.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered If evaluation at root.body[12].body[6].body[4]; no call, error or mutation may be omitted. Condition: cache_key not in receipts
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[0]::Assign

Source: `infra/agentinfra/evidence.py:166`; AST `dc32d4d42b5fafab157995147abfcc1fef36d57783a44300d94accd224269136`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current_receipt, observation, profile, root. Outputs/bindings: receipt.
Calls/effect boundaries: current_receipt.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[0].value::Call

Source: `infra/agentinfra/evidence.py:166`; AST `22eed144b3d8644062c4aa47b7d2c31fb5dc2b718f013110e89b2028840fd76f`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current_receipt, observation, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: current_receipt.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[1]::Expr

Source: `infra/agentinfra/evidence.py:167`; AST `cb1cdfe4861fa15eed78a582044d568245a3ce040543c487c2da0d77b0782375`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[1].value::Call

Source: `infra/agentinfra/evidence.py:167`; AST `5e571d682affa40e193055b26c6ea8eb0996f9041c8f2365a96b8a6aaae6c912`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[2]::Expr

Source: `infra/agentinfra/evidence.py:168`; AST `ec2e9d0cd6f036d40a0bc21f217e85458c03ebfa39edbf3af185e81a1337388d`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[2].value::Call

Source: `infra/agentinfra/evidence.py:168`; AST `8bb1026efdefbaecd26d9005644a93a1fbd9498ba2900e3cdeb289481b054978`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[3]::Assign

Source: `infra/agentinfra/evidence.py:169`; AST `5b4353ebf3f36c91baaefd5abcca5bd246e61a5f367bc9ba0e049899f1f3bfe3`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: set. Outputs/bindings: successful.
Calls/effect boundaries: set.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[3].value::Call

Source: `infra/agentinfra/evidence.py:169`; AST `838cdcc98951e8453a6f9eabf156b2a00af54241b1675173b0420d161d1cb68b`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4]::For

Source: `infra/agentinfra/evidence.py:170`; AST `3d47a1b9050571793ac01f4bd3d61fb654f7b02ecc93e1afb65c37ae685086b2`.

Rust module: `infra::agentinfra::evidence`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: command, counts, int, len, out, re, receipt, require, scenarios, successful. Outputs/bindings: command, counts, out, scenarios.
Calls/effect boundaries: int, len, re.findall, re.search, require, successful.update.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered For evaluation at root.body[12].body[6].body[4].body[4]; no call, error or mutation may be omitted. Iteration: command in receipt['commands']
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[0]::Assign

Source: `infra/agentinfra/evidence.py:171`; AST `6c6c37245cd65ffd9ee42ef82f844aebeaece6331db12198d80b6a827f6edabc`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: command. Outputs/bindings: out.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[4].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[1]::Assign

Source: `infra/agentinfra/evidence.py:172`; AST `62d2605ace9cd641692163c32256d6e40ba2285eda9c3853ea692e07d28b1c2e`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: out, re. Outputs/bindings: scenarios.
Calls/effect boundaries: re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[4].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[1].value::Call

Source: `infra/agentinfra/evidence.py:172`; AST `3c63e71bae01beedfa9fab2e946934416e14839d13de3320f50ff169a1eb6887`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: out, re. Outputs/bindings: (none).
Calls/effect boundaries: re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[2]::Assign

Source: `infra/agentinfra/evidence.py:173`; AST `3e3cbd169ab1eb9c247b5fc53e884c459ea57de4b4f7c048f5e523301b79999f`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: out, re. Outputs/bindings: counts.
Calls/effect boundaries: re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[4].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[2].value::Call

Source: `infra/agentinfra/evidence.py:173`; AST `983de697d915513ca834b242ae573dfbc80a43ec92f056e3f44ea719bfc368bf`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: out, re. Outputs/bindings: (none).
Calls/effect boundaries: re.findall.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[3]::Expr

Source: `infra/agentinfra/evidence.py:174`; AST `eebbf065c2b5816d08e4efdfcd51c91e01181d1044169ed1a7d623857827e3b0`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: counts, int, len, out, re, require, scenarios. Outputs/bindings: (none).
Calls/effect boundaries: int, len, re.search, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[4].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[3].value::Call

Source: `infra/agentinfra/evidence.py:174`; AST `236c453fa709d3ec07cdff3dd80908e885052db322f9444a561df5f47d5db486`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: counts, int, len, out, re, require, scenarios. Outputs/bindings: (none).
Calls/effect boundaries: int, len, re.search, require.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[3].value.args[0].values[0].left::Call

Source: `infra/agentinfra/evidence.py:174`; AST `08cd92311e8303975a9d5df9d470eab1eb227f5c58684e32b3dab591055e7cfd`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: counts, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[4].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[3].value.args[0].values[1].left::Call

Source: `infra/agentinfra/evidence.py:174`; AST `9a28540dc745600aa8970e64e7e924afcbb2d56ff05b0c19fd89e30a605cd45e`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: counts, int. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[4].body[3].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[3].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/evidence.py:174`; AST `36f14006dc9d124e61a7fa06128e683fa49aeca2fcee812f016caa253fedbe3f`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, scenarios. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[4].body[3].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[3].value.args[0].values[2]::Call

Source: `infra/agentinfra/evidence.py:174`; AST `05e31858e83ff9150e638c4e3f992662ee3f1526b7fb9bbc73312842b633b08a`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: out, re. Outputs/bindings: (none).
Calls/effect boundaries: re.search.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[4].body[3].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[4]::Expr

Source: `infra/agentinfra/evidence.py:175`; AST `1315bc6578cb9dd537ada546cb09109ccad2a51c26c991c265f49fc8d06801fb`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: scenarios, successful. Outputs/bindings: (none).
Calls/effect boundaries: successful.update.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[4].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[4].body[4].value::Call

Source: `infra/agentinfra/evidence.py:175`; AST `4a0e10a79ebae06f3c261cc2adcb373dbe66e468c86faae99dd6c5f03b5e7234`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: scenarios, successful. Outputs/bindings: (none).
Calls/effect boundaries: successful.update.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[4].body[5]::Assign

Source: `infra/agentinfra/evidence.py:176`; AST `2d7c40f9964ef5bfab248c1ab720aee4ea9b3db3b6d59809c506df0bd5cd1295`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache_key, receipt, receipts, successful. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[5]::Assign

Source: `infra/agentinfra/evidence.py:177`; AST `eaa7e57d8a995d2d58b75a50c174b5dda930692cf901a80f3395dcae3325ffaa`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache_key, receipts. Outputs/bindings: receipt, successful.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[6]::Assign

Source: `infra/agentinfra/evidence.py:178`; AST `0771da6d97c64fd64f3b5c3e112c4838b0b38176743d4a8c99315e0dd47953c4`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: scenarios.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[7]::Expr

Source: `infra/agentinfra/evidence.py:179`; AST `964163e05439a8119947ed4618075cefed697adff39fd1f63d28e85c2a4670c5`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, list, require, s, scenarios, successful, type. Outputs/bindings: s.
Calls/effect boundaries: all, require, type.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[7].value::Call

Source: `infra/agentinfra/evidence.py:179`; AST `848c84afb0775bfe4c5cfd399590914366425054cc2dc2e313b7ebd3d3ef8de8`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, list, require, s, scenarios, successful, type. Outputs/bindings: s.
Calls/effect boundaries: all, require, type.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[7].value.args[0].values[0].left::Call

Source: `infra/agentinfra/evidence.py:179`; AST `02612840a230baf2344090ea923762c4f66fdeef191d7a4faced6ab140ea50f2`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: scenarios, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[7].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[7].value.args[0].values[2]::Call

Source: `infra/agentinfra/evidence.py:179`; AST `5f8fcc200b1091b4804a4dbf16c22c90d51841d2161f92f79032b4b25987fdd2`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, s, scenarios, successful. Outputs/bindings: s.
Calls/effect boundaries: all.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[7].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[7].value.args[0].values[2].args[0]::GeneratorExp

Source: `infra/agentinfra/evidence.py:179`; AST `b546d4a5c93dbb8165d3c41fe6d90d221efb9d24bbd3f6fc82cf639a4845c104`.

Rust module: `infra::agentinfra::evidence`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: s, scenarios, successful. Outputs/bindings: s.
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[6].body[7].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[8]::Expr

Source: `infra/agentinfra/evidence.py:180`; AST `e9f01f888377c67bc45b414daa4ebaea415320495f154ab77dcef2506507a97f`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, receipt, record, rows, scenarios. Outputs/bindings: (none).
Calls/effect boundaries: rows.append.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[6].body[8].value::Call

Source: `infra/agentinfra/evidence.py:180`; AST `b625313d2f2edfce89220f9398110f6417c130274a372fe445727e0e4e152ae1`.

Rust module: `infra::agentinfra::evidence`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, receipt, record, rows, scenarios. Outputs/bindings: (none).
Calls/effect boundaries: rows.append.
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/evidence.py::module::differential_cases::root.body[12].body[7]::Return

Source: `infra/agentinfra/evidence.py:183`; AST `e8d62c7bb685945ea0a81e6d4c73e7fe86bcf8b904a9d5c35c30d98b70af7c94`.

Rust module: `infra::agentinfra::evidence`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: rows. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: destiny, destiny_reuse, formal, pathlib, re, security.

Invariants: Preserve ordered Return evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
