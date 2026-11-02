# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 170. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/security.py::module::root::Module

Source: `infra/agentinfra/security.py:1`; AST `673bcce749022e0435a11d120d3179ea497c6959737db1bccca0044da0509b6e`.

Rust module: `infra::agentinfra::security`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: FileNotFoundError, Mapping, Path, RuntimeError, SECRET_NAME, SECRET_VALUE_PATTERNS, SecurityError, TEST_DETECTION_NAME, ValueError, absolute, allow, allow_root, attributes, bool, candidate, current, dict, env, exc, extra, getattr, info, int, is_path_redirect, isinstance, key, lexical_relative, match, mode, must_exist, object, os, out, part, path, pattern, raw, re, redact_text, reject_symlinks, rel, reparse_attribute, resolved, root, stat, str, supplied_root, text, value, values. Outputs/bindings: SECRET_NAME, SECRET_VALUE_PATTERNS, TEST_DETECTION_NAME, absolute, allow, attributes, candidate, current, env, info, key, lexical_relative, mode, out, part, pattern, raw, rel, reparse_attribute, resolved, root, supplied_root, text, value.
Calls/effect boundaries: Path, Path(root).absolute, Path(root).resolve, SECRET_NAME.search, SecurityError, TEST_DETECTION_NAME.search, absolute.exists, absolute.relative_to, absolute.resolve, bool, candidate.absolute, candidate.absolute().relative_to, candidate.parent.resolve, env.pop, extra.items, getattr, int, is_path_redirect, isinstance, key.upper, match.group, os.environ.items, os.lstat, path.exists, path.is_symlink, path.stat, pattern.sub, raw.is_absolute, re.compile, redact_text, resolved.relative_to, stat.S_IMODE, stat.S_ISLNK, str, values.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[0]::ImportFrom

Source: `infra/agentinfra/security.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[1]::Import

Source: `infra/agentinfra/security.py:3`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[2]::Import

Source: `infra/agentinfra/security.py:4`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[3]::Import

Source: `infra/agentinfra/security.py:5`; AST `c22b5a111acc3bea9e5136e41e207f1f95083e90d861516ce34d682526721c86`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/security.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/security.py:7`; AST `04bc9827c95492db50079159f63cd3f6c18d5a158b04f9b9c591d7b22975b383`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[6]::Assign

Source: `infra/agentinfra/security.py:10`; AST `ff327ff99520621777edd1cf5a2c6406d5164c4222d4d33dd4cccd6a8368d7ca`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: re. Outputs/bindings: SECRET_NAME.
Calls/effect boundaries: re.compile.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[6].value::Call

Source: `infra/agentinfra/security.py:10`; AST `4781f81459886f6802db05ac3be90c776bdf563e76d15e9d78329adb2032b41e`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re. Outputs/bindings: (none).
Calls/effect boundaries: re.compile.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[7]::Assign

Source: `infra/agentinfra/security.py:11`; AST `e495c6000d38f5c628a8cf4ff88a1a6044fa661457f519e2661be82f673f100e`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: re. Outputs/bindings: TEST_DETECTION_NAME.
Calls/effect boundaries: re.compile.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[7].value::Call

Source: `infra/agentinfra/security.py:11`; AST `08e6150f52c4a2c1aa79efadf29e95d6c2f484472a5f2ee4cdf192e0946c97cd`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re. Outputs/bindings: (none).
Calls/effect boundaries: re.compile.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[8]::Assign

Source: `infra/agentinfra/security.py:14`; AST `0695994d823c1effa115bf59686711d908b96a2e5c8dd00a4f8cb6e129e63cf1`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: re. Outputs/bindings: SECRET_VALUE_PATTERNS.
Calls/effect boundaries: re.compile.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[8].value.elts[0]::Call

Source: `infra/agentinfra/security.py:15`; AST `8b62a14b3d58bf22da88363ab6dbedf344d0e058b40eeff7f05a1de75da246f5`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re. Outputs/bindings: (none).
Calls/effect boundaries: re.compile.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[8].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[8].value.elts[1]::Call

Source: `infra/agentinfra/security.py:16`; AST `7fa1b4e20d3cda6699871935f892ddc1c133fb8d23bd6491c42dbba2a86bcc8c`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re. Outputs/bindings: (none).
Calls/effect boundaries: re.compile.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[8].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::root.body[8].value.elts[2]::Call

Source: `infra/agentinfra/security.py:17`; AST `adb9943a0db3f42d54258fe00283c4bb60a654e16a2c7251bcba8cf49daf3c04`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: re. Outputs/bindings: (none).
Calls/effect boundaries: re.compile.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[8].value.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::SecurityError::root.body[9]::ClassDef

Source: `infra/agentinfra/security.py:21`; AST `2df738a6f7e1b77ff189544f0a5ed04972cc48879b367f974190793989f7c7a0`.

Rust module: `infra::agentinfra::security`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered ClassDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::SecurityError::root.body[9].body[0]::Pass

Source: `infra/agentinfra/security.py:22`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Pass evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10]::FunctionDef

Source: `infra/agentinfra/security.py:25`; AST `7bd13068c51998edbd37b1b3d17b252f1e87d4aaa3275a091a04ec35d9120103`.

Rust module: `infra::agentinfra::security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileNotFoundError, Path, attributes, bool, getattr, info, int, os, path, reparse_attribute, stat. Outputs/bindings: attributes, info, reparse_attribute.
Calls/effect boundaries: bool, getattr, int, os.lstat, path.is_symlink, stat.S_ISLNK.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[0]::Expr

Source: `infra/agentinfra/security.py:26`; AST `a75849aeb71b3b62d34ceadd103a2600ad3d77ac7f2e0c4e904cac97b816a441`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[1]::If

Source: `infra/agentinfra/security.py:37`; AST `7b936a7209cd1e9c22cbf1b205ff7975f41b7908cd593cbd887b87dc89e215c8`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_symlink.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[10].body[1]; no call, error or mutation may be omitted. Condition: path.is_symlink()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[1].test::Call

Source: `infra/agentinfra/security.py:37`; AST `59b1c604985dcd3e66bb0b7ae49c367ee9372b6c297d22636b1ad06e54b90bcc`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_symlink.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[1].body[0]::Return

Source: `infra/agentinfra/security.py:38`; AST `4a8ef490a01d3017cb999fbea58c2adfb60a40ad736e0d23eceb176a236b14c3`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Return evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[2]::If

Source: `infra/agentinfra/security.py:39`; AST `d8b0db979366ab19d231d718e249a54c170af94edcbd0679a1ff74571f6f5ea2`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[10].body[2]; no call, error or mutation may be omitted. Condition: os.name != 'nt'
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[2].body[0]::Return

Source: `infra/agentinfra/security.py:40`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Return evaluation at root.body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[3]::Try

Source: `infra/agentinfra/security.py:41`; AST `98faf6c2b9c8c3eb66a58f42a89b874f29bf4688d5fd9555afd2b41e090ae3c9`.

Rust module: `infra::agentinfra::security`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: FileNotFoundError, os, path. Outputs/bindings: info.
Calls/effect boundaries: os.lstat.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Try evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[3].body[0]::Assign

Source: `infra/agentinfra/security.py:42`; AST `1837751366672eb3e6f16469659928407c973ab4e0ac87be8f052fba6b4ace9c`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, path. Outputs/bindings: info.
Calls/effect boundaries: os.lstat.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[3].body[0].value::Call

Source: `infra/agentinfra/security.py:42`; AST `c71c6b2664f4933900c9b94cabeec29d3d4346c8d0d93d14b9729b50a35b210a`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, path. Outputs/bindings: (none).
Calls/effect boundaries: os.lstat.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[3].handlers[0]::ExceptHandler

Source: `infra/agentinfra/security.py:43`; AST `2a03f313767a87d04b28459e72bd48f4a4f82ac3ef3733dbb2cd6803249e0170`.

Rust module: `infra::agentinfra::security`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: FileNotFoundError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[10].body[3].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[3].handlers[0].body[0]::Return

Source: `infra/agentinfra/security.py:44`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Return evaluation at root.body[10].body[3].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[4]::Assign

Source: `infra/agentinfra/security.py:45`; AST `c68195334ce9b042494cc5c001b95f78869c07e5255c3d074eab3f84624272c2`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: getattr, info, int. Outputs/bindings: attributes.
Calls/effect boundaries: getattr, int.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[4].value::Call

Source: `infra/agentinfra/security.py:45`; AST `1d13b981cdc442069d0b1ac5795f653eebd4f0efe8f79ed8e1cdd1e29d980aab`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, info, int. Outputs/bindings: (none).
Calls/effect boundaries: getattr, int.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[4].value.args[0]::Call

Source: `infra/agentinfra/security.py:45`; AST `8c437135f724eb101d66967b27fde7827922d79316f181540008cd45b7e31bc1`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, info. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[5]::Assign

Source: `infra/agentinfra/security.py:46`; AST `7ee1406c7edb5fc4f9e2425debf873a47628a1fe79f200e48773dcf4325fa1a9`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: getattr, int, stat. Outputs/bindings: reparse_attribute.
Calls/effect boundaries: getattr, int.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[5].value::Call

Source: `infra/agentinfra/security.py:46`; AST `d87b4d4e1611d4c24e035215be9ec30c5c5d2c833e5ba8dff0273d72d4dbce3e`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, int, stat. Outputs/bindings: (none).
Calls/effect boundaries: getattr, int.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[5].value.args[0]::Call

Source: `infra/agentinfra/security.py:46`; AST `51ca90a505c2dda2c39c6655416b725f8e92314dfd0fcd7003a0cbb258bb3798`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, stat. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[6]::Return

Source: `infra/agentinfra/security.py:47`; AST `ecf6ac9cfefe0dac149ef98217eab6fe18f1f5203890d8b80785b4b614b3fe25`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attributes, bool, info, reparse_attribute, stat. Outputs/bindings: (none).
Calls/effect boundaries: bool, stat.S_ISLNK.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Return evaluation at root.body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[6].value.values[0]::Call

Source: `infra/agentinfra/security.py:47`; AST `4cd1f232533c29fd29a651a734784c00ddadd3c7f4b4f9af0e0849058eadddb9`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info, stat. Outputs/bindings: (none).
Calls/effect boundaries: stat.S_ISLNK.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::is_path_redirect::root.body[10].body[6].value.values[1]::Call

Source: `infra/agentinfra/security.py:47`; AST `aa810ba87bcf5840b500ea0ffd906865c59bfa1216ff412f28df288e95595259`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attributes, bool, reparse_attribute. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11]::FunctionDef

Source: `infra/agentinfra/security.py:50`; AST `0c8c37ce8187114865387652e0b3a183ca09f2496cb320a9610cd698d4760f54`.

Rust module: `infra::agentinfra::security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: SECRET_VALUE_PATTERNS, match, pattern, str, text, value. Outputs/bindings: pattern, text.
Calls/effect boundaries: match.group, pattern.sub.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[0]::Assign

Source: `infra/agentinfra/security.py:51`; AST `475672d40f17faa0b5c73a751b59494b787af951e04db9aa3671b3037d2419ee`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: text.
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[1]::For

Source: `infra/agentinfra/security.py:52`; AST `805990163ded74f78e245222c59e2978aa9bc2c9cdc77117ba76b42c226468a0`.

Rust module: `infra::agentinfra::security`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: SECRET_VALUE_PATTERNS, match, pattern, text. Outputs/bindings: pattern, text.
Calls/effect boundaries: match.group, pattern.sub.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered For evaluation at root.body[11].body[1]; no call, error or mutation may be omitted. Iteration: pattern in SECRET_VALUE_PATTERNS
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[1].body[0]::If

Source: `infra/agentinfra/security.py:53`; AST `5aac57548889779b9cf9aeb1f9469b7139f1db94b3d230a663fdceccfdc8b139`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: match, pattern, text. Outputs/bindings: text.
Calls/effect boundaries: match.group, pattern.sub.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[11].body[1].body[0]; no call, error or mutation may be omitted. Condition: pattern.groups
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[1].body[0].body[0]::Assign

Source: `infra/agentinfra/security.py:54`; AST `117dd536d5c2ddc09f45f2d46c4ee2b6d927981782981e69ad10ed43d6ddb4b5`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: match, pattern, text. Outputs/bindings: text.
Calls/effect boundaries: match.group, pattern.sub.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/security.py:54`; AST `367888ecf46d7e5e10516dd0c66791c9cfc06028f8e4df5bd62b3ba250eb6fa7`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: match, pattern, text. Outputs/bindings: (none).
Calls/effect boundaries: match.group, pattern.sub.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[1].body[0].body[0].value.args[0]::Lambda

Source: `infra/agentinfra/security.py:54`; AST `0067f98e1fe72bf74a73b7a918def3f402b10ef49f6735ba65156cff2824097f`.

Rust module: `infra::agentinfra::security`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: match. Outputs/bindings: (none).
Calls/effect boundaries: match.group.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Lambda evaluation at root.body[11].body[1].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[1].body[0].body[0].value.args[0].body.left::Call

Source: `infra/agentinfra/security.py:54`; AST `58882b4861698257f0d45873338173193c11189bdbd97121c39fe80fe9dd5650`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: match. Outputs/bindings: (none).
Calls/effect boundaries: match.group.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[0].body[0].value.args[0].body.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[1].body[0].orelse[0]::Assign

Source: `infra/agentinfra/security.py:56`; AST `0c4cdf609819ee59fa50f3b0c2d32f4cf685a5b3c8ac7c6f1db33d217c79755e`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pattern, text. Outputs/bindings: text.
Calls/effect boundaries: pattern.sub.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[1].body[0].orelse[0].value::Call

Source: `infra/agentinfra/security.py:56`; AST `66f924d2005ef4ab386fccf41969f9a64c3ec5b574b1d6a172195f01026e0c5f`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pattern, text. Outputs/bindings: (none).
Calls/effect boundaries: pattern.sub.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[0].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_text::root.body[11].body[2]::Return

Source: `infra/agentinfra/security.py:57`; AST `59affc0a76fe14b6d067c38e827181776717f3fdec012ef6688ad9f3620d09f8`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Return evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12]::FunctionDef

Source: `infra/agentinfra/security.py:60`; AST `aff0946de5212f2836c9a09599f79bfe17ddf8839f79baf8a62adea3e20c8bdc`.

Rust module: `infra::agentinfra::security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Mapping, SECRET_NAME, dict, isinstance, key, object, out, redact_text, str, value, values. Outputs/bindings: key, out, value.
Calls/effect boundaries: SECRET_NAME.search, isinstance, redact_text, str, values.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[0]::AnnAssign

Source: `infra/agentinfra/security.py:61`; AST `1efa57e45782f67fb8acfc21684ae367c83cc049351cacdac7562f008eb07c60`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, object, str. Outputs/bindings: out.
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered AnnAssign evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1]::For

Source: `infra/agentinfra/security.py:62`; AST `2ac704c0fa67a738904eb4ea06965b5f1010d5e0dff8af99cfd1d172c09b4a56`.

Rust module: `infra::agentinfra::security`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: SECRET_NAME, isinstance, key, out, redact_text, str, value, values. Outputs/bindings: key, value.
Calls/effect boundaries: SECRET_NAME.search, isinstance, redact_text, str, values.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered For evaluation at root.body[12].body[1]; no call, error or mutation may be omitted. Iteration: (key, value) in values.items()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].iter::Call

Source: `infra/agentinfra/security.py:62`; AST `58b17beeca91d68195f6c986bde5554c25ae79243d51bf18f34d1e40380276bd`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: values. Outputs/bindings: (none).
Calls/effect boundaries: values.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0]::If

Source: `infra/agentinfra/security.py:63`; AST `db2e37133cdf8a6e24839246998b4188c6e3b65f568f95caa819f0cf2f3d5458`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SECRET_NAME, isinstance, key, out, redact_text, str, value. Outputs/bindings: (none).
Calls/effect boundaries: SECRET_NAME.search, isinstance, redact_text, str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted. Condition: SECRET_NAME.search(str(key))
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].test::Call

Source: `infra/agentinfra/security.py:63`; AST `fd8be4e350afa29cd610069222c3aa0f6fddcdb4f20d6f59abd0273c36e07a63`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SECRET_NAME, key, str. Outputs/bindings: (none).
Calls/effect boundaries: SECRET_NAME.search, str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].test.args[0]::Call

Source: `infra/agentinfra/security.py:63`; AST `9fa2a35533437c0274affe76a7b1619b3e9ef75a1bdae6f73cc29c25b992a17c`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].test.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].body[0]::Assign

Source: `infra/agentinfra/security.py:64`; AST `c75dc3489fb6abe77b2ebe658941dc7f785532050c2dbe966cf2d592b230493f`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, out, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].body[0].targets[0].slice::Call

Source: `infra/agentinfra/security.py:64`; AST `9fa2a35533437c0274affe76a7b1619b3e9ef75a1bdae6f73cc29c25b992a17c`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].body[0].targets[0].slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].orelse[0]::If

Source: `infra/agentinfra/security.py:65`; AST `8be0417d2345add3de9ab551f649e34b29dd24f9db3a66a27c701f992f4579fd`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: isinstance, key, out, redact_text, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, redact_text, str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[12].body[1].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: isinstance(value, str)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].orelse[0].test::Call

Source: `infra/agentinfra/security.py:65`; AST `f0937843eac35cb846ed896776839197deebad579475d870c722a45446739540`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, str, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].orelse[0].body[0]::Assign

Source: `infra/agentinfra/security.py:66`; AST `370820b1baa3637c1297f1d5ccf97dce85c36c4bdbefa8129050bd9398a83ae6`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, out, redact_text, str, value. Outputs/bindings: (none).
Calls/effect boundaries: redact_text, str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].orelse[0].body[0].targets[0].slice::Call

Source: `infra/agentinfra/security.py:66`; AST `9fa2a35533437c0274affe76a7b1619b3e9ef75a1bdae6f73cc29c25b992a17c`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].orelse[0].body[0].targets[0].slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/security.py:66`; AST `5372a1f191b9d0fa06266b4614a043b019d982e2133d56566441f2af8ec8e819`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: redact_text, value. Outputs/bindings: (none).
Calls/effect boundaries: redact_text.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].orelse[0].orelse[0]::Assign

Source: `infra/agentinfra/security.py:68`; AST `5653c03a1ee01bace773891c5abca8a429ba09f0eb5254b7d140fd43e9943721`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: key, out, str, value. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[0].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[1].body[0].orelse[0].orelse[0].targets[0].slice::Call

Source: `infra/agentinfra/security.py:68`; AST `9fa2a35533437c0274affe76a7b1619b3e9ef75a1bdae6f73cc29c25b992a17c`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].orelse[0].orelse[0].targets[0].slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::redact_mapping::root.body[12].body[2]::Return

Source: `infra/agentinfra/security.py:69`; AST `b6962c41f3a8739966bfd4ad2b2f495b4148be3c2f293d4445f963bf3ff579cd`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: out. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Return evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13]::FunctionDef

Source: `infra/agentinfra/security.py:72`; AST `cfe82632044247586740d98e2bb9a969a650973b9f4cf85e93a101cdeb9f8300`.

Rust module: `infra::agentinfra::security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Mapping, SECRET_NAME, SecurityError, TEST_DETECTION_NAME, allow, dict, env, extra, key, os, str, value. Outputs/bindings: allow, env, key, value.
Calls/effect boundaries: SECRET_NAME.search, SecurityError, TEST_DETECTION_NAME.search, env.pop, extra.items, key.upper, os.environ.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[0]::Assign

Source: `infra/agentinfra/security.py:73`; AST `16dd5a6a388e5a38eb4e551e1c564f0471e6b4f5bbe3bfcaf3ed6f73cd7cc842`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: allow.
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[1]::Assign

Source: `infra/agentinfra/security.py:88`; AST `53806a4a158e776a887e70677e49c6a0b4b209e15215d5fcacf2de6f14755b8c`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SECRET_NAME, allow, key, os, value. Outputs/bindings: env, key, value.
Calls/effect boundaries: SECRET_NAME.search, key.upper, os.environ.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[1].value::DictComp

Source: `infra/agentinfra/security.py:88`; AST `c2eed71b4c9007bfef80c75e713d5643940b069989a8831acdcc9a225c4c3d6e`.

Rust module: `infra::agentinfra::security`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: SECRET_NAME, allow, key, os, value. Outputs/bindings: key, value.
Calls/effect boundaries: SECRET_NAME.search, key.upper, os.environ.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered DictComp evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[1].value.generators[0].iter::Call

Source: `infra/agentinfra/security.py:88`; AST `d265912a044c9a5ebe83f8e7b94215d82f8fc6eb9cdc8323f80f7202aad017c5`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.environ.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[1].value.generators[0].ifs[0].values[0].left::Call

Source: `infra/agentinfra/security.py:88`; AST `e083dc42e68f29bcaad566470f4a2b02cbc7d8b47deeaea63c531201aa9560d7`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: key. Outputs/bindings: (none).
Calls/effect boundaries: key.upper.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.generators[0].ifs[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[1].value.generators[0].ifs[0].values[1].operand::Call

Source: `infra/agentinfra/security.py:88`; AST `555dc6bbbefb46dab5b6da7f93a290f508db481b25526dd373d0c3118a91b520`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SECRET_NAME, key. Outputs/bindings: (none).
Calls/effect boundaries: SECRET_NAME.search.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.generators[0].ifs[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2]::If

Source: `infra/agentinfra/security.py:89`; AST `a66c3bbfcee7d8f173c392164e148a87f0e47d35a0cf493724d5efa5a988d631`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SECRET_NAME, SecurityError, TEST_DETECTION_NAME, env, extra, key, value. Outputs/bindings: key, value.
Calls/effect boundaries: SECRET_NAME.search, SecurityError, TEST_DETECTION_NAME.search, extra.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[2]; no call, error or mutation may be omitted. Condition: extra
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0]::For

Source: `infra/agentinfra/security.py:90`; AST `25ae464b2e523743da5481d7bbac243ab9d5cabc84ea1b82d4100dcb06b8cff0`.

Rust module: `infra::agentinfra::security`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: SECRET_NAME, SecurityError, TEST_DETECTION_NAME, env, extra, key, value. Outputs/bindings: key, value.
Calls/effect boundaries: SECRET_NAME.search, SecurityError, TEST_DETECTION_NAME.search, extra.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered For evaluation at root.body[13].body[2].body[0]; no call, error or mutation may be omitted. Iteration: (key, value) in extra.items()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0].iter::Call

Source: `infra/agentinfra/security.py:90`; AST `32d6a8e86c7a778fa645c9f7000f387dac12c2d8022cf967a86f1a1edceb60f7`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: extra. Outputs/bindings: (none).
Calls/effect boundaries: extra.items.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0].body[0]::If

Source: `infra/agentinfra/security.py:91`; AST `e3e5c780a4b909f49ce6e3bd27305bf25ba579b09dc979ad58173cfd92413a23`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SECRET_NAME, SecurityError, key. Outputs/bindings: (none).
Calls/effect boundaries: SECRET_NAME.search, SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[2].body[0].body[0]; no call, error or mutation may be omitted. Condition: SECRET_NAME.search(key)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0].body[0].test::Call

Source: `infra/agentinfra/security.py:91`; AST `555dc6bbbefb46dab5b6da7f93a290f508db481b25526dd373d0c3118a91b520`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SECRET_NAME, key. Outputs/bindings: (none).
Calls/effect boundaries: SECRET_NAME.search.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0].body[0].body[0]::Raise

Source: `infra/agentinfra/security.py:92`; AST `8c3148cbb85b0888cc3356e738c9a55e5bfca87b064922c043ef2ac85472ccf0`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, key. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[2].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0].body[0].body[0].exc::Call

Source: `infra/agentinfra/security.py:92`; AST `c3d095c30cf32eacc709f33d1b40660e383a8c4c84eccad61b966e831687152e`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, key. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0].body[1]::If

Source: `infra/agentinfra/security.py:93`; AST `345d2335df08a3bea270b0e64ff1e60069405a28fa603b35f705a177bfb57c8b`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: TEST_DETECTION_NAME, key. Outputs/bindings: (none).
Calls/effect boundaries: TEST_DETECTION_NAME.search.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[2].body[0].body[1]; no call, error or mutation may be omitted. Condition: TEST_DETECTION_NAME.search(key)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0].body[1].test::Call

Source: `infra/agentinfra/security.py:93`; AST `ae67fa56051b2a5281fc8a9473ccfa3ef9b8ae7729aacc3337afaaaed5661f90`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TEST_DETECTION_NAME, key. Outputs/bindings: (none).
Calls/effect boundaries: TEST_DETECTION_NAME.search.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0].body[1].body[0]::Continue

Source: `infra/agentinfra/security.py:94`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Continue evaluation at root.body[13].body[2].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[2].body[0].body[2]::Assign

Source: `infra/agentinfra/security.py:95`; AST `6073ef6d43f2fb4c016ca1f313241a372d9cb76ce1ab8922a5753f0bb687e7c7`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, key, value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[3]::Assign

Source: `infra/agentinfra/security.py:96`; AST `23e2c22832153178a701c14940a4c0d08e60e5867ec74a580efc74923ee8f8ba`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[4]::Assign

Source: `infra/agentinfra/security.py:97`; AST `5661a8f04571d3d57156f737d637e60635cd465394313a1908e79b0a443d5cc1`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[5]::Assign

Source: `infra/agentinfra/security.py:98`; AST `2ba84a9aa2f12640dd91c0c42a38a64726abb4a8f960326e6ce4baff65084da8`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[6]::Expr

Source: `infra/agentinfra/security.py:99`; AST `d49292957843b56b87ed1994ab2dcceadb421240c49a36b055c14856dcd6338e`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env. Outputs/bindings: (none).
Calls/effect boundaries: env.pop.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[6].value::Call

Source: `infra/agentinfra/security.py:99`; AST `052c11d2b42fb5c79f8092474fa78cc2ebb94b90c92b1463bb3cce2af2430f1b`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env. Outputs/bindings: (none).
Calls/effect boundaries: env.pop.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[7]::Expr

Source: `infra/agentinfra/security.py:100`; AST `b1c7fa91ddd3d1d3331e490a541cf23ce7b3885c52ffcf8c00e8b308bd6bb4f2`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env. Outputs/bindings: (none).
Calls/effect boundaries: env.pop.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[7].value::Call

Source: `infra/agentinfra/security.py:100`; AST `bc7f5aee7d05255b416145d651fddf47dfbad17ac5f9a0f87c41a34c549fb900`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env. Outputs/bindings: (none).
Calls/effect boundaries: env.pop.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::minimal_subprocess_env::root.body[13].body[8]::Return

Source: `infra/agentinfra/security.py:101`; AST `cd7cdf1b560fffaa519e13385426d375bedd995902203af681096abeec2eeec3`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Return evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14]::FunctionDef

Source: `infra/agentinfra/security.py:104`; AST `035d82bfec903b53a1bb4a07af585e0118a6d9cb9a5937685cc2865f23c987a1`.

Rust module: `infra::agentinfra::security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, SecurityError, ValueError, absolute, allow_root, bool, candidate, current, exc, is_path_redirect, lexical_relative, must_exist, part, raw, reject_symlinks, rel, resolved, root, str, supplied_root, value. Outputs/bindings: absolute, candidate, current, lexical_relative, part, raw, rel, resolved, root, supplied_root.
Calls/effect boundaries: Path, Path(root).absolute, Path(root).resolve, SecurityError, absolute.exists, absolute.relative_to, absolute.resolve, candidate.absolute, candidate.absolute().relative_to, candidate.parent.resolve, is_path_redirect, raw.is_absolute, resolved.relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[0]::Assign

Source: `infra/agentinfra/security.py:112`; AST `03cd3d4ef65cb355d9f4a0ec20f0912d797d942dd3450b8c96803467ae0c5d1e`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, root. Outputs/bindings: supplied_root.
Calls/effect boundaries: Path, Path(root).absolute.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[0].value::Call

Source: `infra/agentinfra/security.py:112`; AST `3eebbf736e68d2d295cdba37607062033a5419b81d2ced5b3f4e341f2d5a6dcc`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(root).absolute.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[0].value.func.value::Call

Source: `infra/agentinfra/security.py:112`; AST `89ee07422ba048597dbd9de6548decd194db771e3b0860cd61470bfeb6374e17`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[1]::Assign

Source: `infra/agentinfra/security.py:113`; AST `2a3be91b550b6a6298e54ac8b21e74dcfa327683f188e0d2f817dbab3c8180de`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, root. Outputs/bindings: root.
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[1].value::Call

Source: `infra/agentinfra/security.py:113`; AST `c730489059afc3f4aef1c52b1968dce819ad8d18695e9c28c3f4518931ce9791`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(root).resolve.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[1].value.func.value::Call

Source: `infra/agentinfra/security.py:113`; AST `89ee07422ba048597dbd9de6548decd194db771e3b0860cd61470bfeb6374e17`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, root. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[2]::Assign

Source: `infra/agentinfra/security.py:114`; AST `cc38df8f32d8947d05cc36215148b5323bf8e7dff14651c7bcda4e205f6b38cc`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, value. Outputs/bindings: raw.
Calls/effect boundaries: Path.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[2].value::Call

Source: `infra/agentinfra/security.py:114`; AST `5f0281d99485aea7f5de192477181f069d9072f512cd7586af0b70660a137bb2`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, value. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[3]::If

Source: `infra/agentinfra/security.py:115`; AST `a88c2b239abb92d333ee847cedc4efca29844c6cd4a1b6d969d5e3eb737d7af8`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, raw, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[3]; no call, error or mutation may be omitted. Condition: '..' in raw.parts
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[3].body[0]::Raise

Source: `infra/agentinfra/security.py:116`; AST `dfe31ce50ca6dd54fcaf38aadae577be6ae5aa18de6a60c7bbcfd55a03ebf199`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[3].body[0].exc::Call

Source: `infra/agentinfra/security.py:116`; AST `e1cbf15fc0b4ecf8b94d9b52d133004719007ec87b4388167f6f0dcfb0ccf438`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[4]::Assign

Source: `infra/agentinfra/security.py:117`; AST `9a1cbd8966bf39b92a29d26cff48434c14d00f89e6a796c3643997fe030bb6a9`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw, supplied_root. Outputs/bindings: candidate.
Calls/effect boundaries: raw.is_absolute.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[4].value.test::Call

Source: `infra/agentinfra/security.py:117`; AST `988e0b836d3be7a8bdd28c2d328869df6f375964196e0741a1384f9a809835e5`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.is_absolute.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5]::If

Source: `infra/agentinfra/security.py:118`; AST `612900042793dece7b7380afa7ade1f2298b7a30f672924d88e70e6729072df4`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, ValueError, candidate, current, is_path_redirect, lexical_relative, part, reject_symlinks, supplied_root. Outputs/bindings: current, lexical_relative, part.
Calls/effect boundaries: SecurityError, candidate.absolute, candidate.absolute().relative_to, is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[5]; no call, error or mutation may be omitted. Condition: reject_symlinks
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[0]::Try

Source: `infra/agentinfra/security.py:119`; AST `5a13fc49d80b3f00fa6672441dbd1cb3f4b18cfb221070a8d53002e93a32b06f`.

Rust module: `infra::agentinfra::security`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ValueError, candidate, supplied_root. Outputs/bindings: lexical_relative.
Calls/effect boundaries: candidate.absolute, candidate.absolute().relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Try evaluation at root.body[14].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[0].body[0]::Assign

Source: `infra/agentinfra/security.py:120`; AST `da47e8c036cae52b43f89dcd4ec238708dfd9780e5bbcbcf5e9edaff2bbb1033`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, supplied_root. Outputs/bindings: lexical_relative.
Calls/effect boundaries: candidate.absolute, candidate.absolute().relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[0].body[0].value::Call

Source: `infra/agentinfra/security.py:120`; AST `a8cc4e8799d75ecaad241b55a5a91223a6c90911b85518b07e708be5c9c2120e`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, supplied_root. Outputs/bindings: (none).
Calls/effect boundaries: candidate.absolute, candidate.absolute().relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[0].body[0].value.func.value::Call

Source: `infra/agentinfra/security.py:120`; AST `ddceaeafa337d658529684b30e389d6d0263f5236014a8429d70d7ad46426aa2`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate. Outputs/bindings: (none).
Calls/effect boundaries: candidate.absolute.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/security.py:121`; AST `8e6f24ab037cd562c5f52dc9fb02b58a56c6166039a69bf5086d676f7a06b76d`.

Rust module: `infra::agentinfra::security`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ValueError. Outputs/bindings: lexical_relative.
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[14].body[5].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[0].handlers[0].body[0]::Assign

Source: `infra/agentinfra/security.py:122`; AST `1e2b1358337353f4972db7aec0c2e9fcc1f43e46f7a46c2cd66587f3ef044965`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: lexical_relative.
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[1]::If

Source: `infra/agentinfra/security.py:123`; AST `b381a48e2dbab05f4a5ca4ac9d3ac0d10ea2d585857fa01f700ca6ead61d01e3`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, current, is_path_redirect, lexical_relative, part, supplied_root. Outputs/bindings: current, part.
Calls/effect boundaries: SecurityError, is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[5].body[1]; no call, error or mutation may be omitted. Condition: lexical_relative is not None
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[1].body[0]::Assign

Source: `infra/agentinfra/security.py:124`; AST `4dd82b83da125613b846b72fc3dbff58ee2d43f6cc722db4c95b0ee89b28c619`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: supplied_root. Outputs/bindings: current.
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[1].body[1]::For

Source: `infra/agentinfra/security.py:125`; AST `d05ede69659ca39ddc265efa073aad81b0f99fbcbca28f8a6d66e9b2a5397eea`.

Rust module: `infra::agentinfra::security`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: SecurityError, current, is_path_redirect, lexical_relative, part. Outputs/bindings: current, part.
Calls/effect boundaries: SecurityError, is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered For evaluation at root.body[14].body[5].body[1].body[1]; no call, error or mutation may be omitted. Iteration: part in lexical_relative.parts
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[1].body[1].body[0]::Assign

Source: `infra/agentinfra/security.py:126`; AST `9f303b47c2b05fc0da78630751f6b3dc79ae61ee6da8a1dd85b853c47d6c1978`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, part. Outputs/bindings: current.
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[5].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[1].body[1].body[1]::If

Source: `infra/agentinfra/security.py:127`; AST `65c270f71a035f399c2cbe7be6d1c53310aaf5c02a71e3dba18d46589e36b02d`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, current, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError, is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[5].body[1].body[1].body[1]; no call, error or mutation may be omitted. Condition: is_path_redirect(current)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[1].body[1].body[1].test::Call

Source: `infra/agentinfra/security.py:127`; AST `40016ece3accb20f8c991e15dbde33edb0976b624a9765bc08db3981c15afe10`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[1].body[1].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[1].body[1].body[1].body[0]::Raise

Source: `infra/agentinfra/security.py:128`; AST `7eb758f9ce8fc2dfe9b7112d6af2252371e96d3f93586533fb0db497c3db4f1c`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, current. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[5].body[1].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[5].body[1].body[1].body[1].body[0].exc::Call

Source: `infra/agentinfra/security.py:128`; AST `355ca43cfd5ef7ddb7bef929d14a6ebb344a9ea9526ad04bf00fcc69827e8958`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, current. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[1].body[1].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[6]::Assign

Source: `infra/agentinfra/security.py:129`; AST `e8d9c5042f1c8d310c7a5d4d5cda31dc9d5e45b0aa9d69b4c47f30c43b924a03`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate. Outputs/bindings: absolute.
Calls/effect boundaries: candidate.parent.resolve.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[6].value.left::Call

Source: `infra/agentinfra/security.py:129`; AST `816865b7ac8fbb50b64c521dbb56b1a62b5348247859df0ba2968f97fbdcaaef`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate. Outputs/bindings: (none).
Calls/effect boundaries: candidate.parent.resolve.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[7]::Try

Source: `infra/agentinfra/security.py:130`; AST `f308b2117cc16266827551fe80f2412386909cde1879c148d4d8958c2ca5c2e0`.

Rust module: `infra::agentinfra::security`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: SecurityError, ValueError, absolute, exc, root, value. Outputs/bindings: rel.
Calls/effect boundaries: SecurityError, absolute.relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Try evaluation at root.body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[7].body[0]::Assign

Source: `infra/agentinfra/security.py:131`; AST `85492968ebd1e2c4e0fbaa096b2888b67feb448311a9f0e2a44f503008d43d3f`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: absolute, root. Outputs/bindings: rel.
Calls/effect boundaries: absolute.relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[7].body[0].value::Call

Source: `infra/agentinfra/security.py:131`; AST `b85564b5d2f31fd20d22a079c71b85630d2107a400bca227358c866a15a52ae9`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: absolute, root. Outputs/bindings: (none).
Calls/effect boundaries: absolute.relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[7].handlers[0]::ExceptHandler

Source: `infra/agentinfra/security.py:132`; AST `d30ee41359fac40f8cdcd03cf9f7bcf1539ec969b973d02b2b2426d9e74389a9`.

Rust module: `infra::agentinfra::security`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: SecurityError, ValueError, exc, root, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[14].body[7].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[7].handlers[0].body[0]::Raise

Source: `infra/agentinfra/security.py:133`; AST `d15fdc899120c38a581faf502b23a2b9c8f8ba63bf9fdf2b95055078184b85df`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, exc, root, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[7].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[7].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/security.py:133`; AST `093c5df5d44aef1092a7c0bdd2e9c54293d07c6dc2279273268620358c7bee39`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, root, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[8]::If

Source: `infra/agentinfra/security.py:134`; AST `4c14fef6ccc473941796792a6ec9a6bf3af9cbf921c8737c8315d25b09fe1932`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, allow_root, rel. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[8]; no call, error or mutation may be omitted. Condition: not allow_root and (not rel.parts)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[8].body[0]::Raise

Source: `infra/agentinfra/security.py:135`; AST `95186908b82ffcdfb134a4c28c71b682c66ed7f54da726b9258a149f90339908`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[8].body[0].exc::Call

Source: `infra/agentinfra/security.py:135`; AST `a48ccac6999af03e61fc2ebff989a12a727dfb24f93c04d38f2a20e49fa0f165`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[9]::Assign

Source: `infra/agentinfra/security.py:136`; AST `b9426148ac340985a146a215bf5bb038fda9ee75387032814947274ed11f0c17`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: current.
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[10]::For

Source: `infra/agentinfra/security.py:137`; AST `8f6b24eac3d29c771f9478d2a6e0dac6a49d09ac85933cb53dc0be1767f7e8a7`.

Rust module: `infra::agentinfra::security`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: SecurityError, current, is_path_redirect, part, reject_symlinks, rel. Outputs/bindings: current, part.
Calls/effect boundaries: SecurityError, is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered For evaluation at root.body[14].body[10]; no call, error or mutation may be omitted. Iteration: part in rel.parts
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[10].body[0]::If

Source: `infra/agentinfra/security.py:138`; AST `abadd7830cd0dad4084fb622d258a217ac55634e27ac6e5c79e6131a10f1035b`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, part. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[10].body[0]; no call, error or mutation may be omitted. Condition: part in {'', '.', '..'}
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[10].body[0].body[0]::Raise

Source: `infra/agentinfra/security.py:139`; AST `61f2f877a3d708620c06733747d4a45c260ca996f076f0fd8f9dc4d3caefd14a`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, part. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[10].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[10].body[0].body[0].exc::Call

Source: `infra/agentinfra/security.py:139`; AST `95396b67fff6b8db07c77743da5010f696b689c74ff0811b1bb1bf4c6fe89021`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, part. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[10].body[1]::Assign

Source: `infra/agentinfra/security.py:140`; AST `9f303b47c2b05fc0da78630751f6b3dc79ae61ee6da8a1dd85b853c47d6c1978`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, part. Outputs/bindings: current.
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[10].body[2]::If

Source: `infra/agentinfra/security.py:141`; AST `5603e6e2d649eea0906c4a3cd1adbe5cb5ad4bf36d0d5738175dc4b8bded7429`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, current, is_path_redirect, reject_symlinks. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError, is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[10].body[2]; no call, error or mutation may be omitted. Condition: reject_symlinks and is_path_redirect(current)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[10].body[2].test.values[1]::Call

Source: `infra/agentinfra/security.py:141`; AST `40016ece3accb20f8c991e15dbde33edb0976b624a9765bc08db3981c15afe10`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[2].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[10].body[2].body[0]::Raise

Source: `infra/agentinfra/security.py:142`; AST `7eb758f9ce8fc2dfe9b7112d6af2252371e96d3f93586533fb0db497c3db4f1c`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, current. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[10].body[2].body[0].exc::Call

Source: `infra/agentinfra/security.py:142`; AST `355ca43cfd5ef7ddb7bef929d14a6ebb344a9ea9526ad04bf00fcc69827e8958`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, current. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[11]::If

Source: `infra/agentinfra/security.py:143`; AST `b252a5cbb89f4d1fdcab6fdc1d35650c0736666b2b71d96519f9551116280373`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, absolute, must_exist. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError, absolute.exists.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[11]; no call, error or mutation may be omitted. Condition: must_exist and (not absolute.exists())
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[11].test.values[1].operand::Call

Source: `infra/agentinfra/security.py:143`; AST `738a78f60adde83a2ce8bccd78c30f09572c2a776d9ec5dbe60ecefc591a2490`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: absolute. Outputs/bindings: (none).
Calls/effect boundaries: absolute.exists.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[11].body[0]::Raise

Source: `infra/agentinfra/security.py:144`; AST `8a12a6bfcef07ddc32da219244af450dcc622de74d6dc589adc69fda7fb84633`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, absolute. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[11].body[0].exc::Call

Source: `infra/agentinfra/security.py:144`; AST `839655b15e4c1fe8a0177b199194394c42acd97d452d21a77794de538a11c705`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, absolute. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12]::If

Source: `infra/agentinfra/security.py:145`; AST `060a1719b972a4858bc78a2e273486cbca5283338943147f808597cbac711080`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, ValueError, absolute, exc, resolved, root, value. Outputs/bindings: resolved.
Calls/effect boundaries: SecurityError, absolute.exists, absolute.resolve, resolved.relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[12]; no call, error or mutation may be omitted. Condition: absolute.exists()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12].test::Call

Source: `infra/agentinfra/security.py:145`; AST `738a78f60adde83a2ce8bccd78c30f09572c2a776d9ec5dbe60ecefc591a2490`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: absolute. Outputs/bindings: (none).
Calls/effect boundaries: absolute.exists.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12].body[0]::Assign

Source: `infra/agentinfra/security.py:146`; AST `751f15b2de53cab98dd4e278db27ad4e10aabb4aee36b9053dd9ac716b41f72d`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: absolute. Outputs/bindings: resolved.
Calls/effect boundaries: absolute.resolve.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12].body[0].value::Call

Source: `infra/agentinfra/security.py:146`; AST `f3fb3d34ba79b32ad30783a7d28402a041d87626ba4d845cb258802558d32b02`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: absolute. Outputs/bindings: (none).
Calls/effect boundaries: absolute.resolve.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12].body[1]::Try

Source: `infra/agentinfra/security.py:147`; AST `699887e58b0aa4f720e1879141418b849fe5e1eb8a243d8308d870126165198c`.

Rust module: `infra::agentinfra::security`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: SecurityError, ValueError, exc, resolved, root, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError, resolved.relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Try evaluation at root.body[14].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12].body[1].body[0]::Expr

Source: `infra/agentinfra/security.py:148`; AST `eaa159ee80a0b5cc376ef4a565d60439c3498f9fd96c054f24e94170b72d1b55`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: resolved, root. Outputs/bindings: (none).
Calls/effect boundaries: resolved.relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12].body[1].body[0].value::Call

Source: `infra/agentinfra/security.py:148`; AST `4017b00ae78f32c4035748514303a40a6901b8b2f1117224493dac7e819e1243`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: resolved, root. Outputs/bindings: (none).
Calls/effect boundaries: resolved.relative_to.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/security.py:149`; AST `6748dfa890b5e2cb9b3e3832264ca290b7de0da72025c924215edf610399291a`.

Rust module: `infra::agentinfra::security`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: SecurityError, ValueError, exc, root, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[14].body[12].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12].body[1].handlers[0].body[0]::Raise

Source: `infra/agentinfra/security.py:150`; AST `982f627e57a0d1a84044212fa59f4073abbd7828d85930ac4c995435000a2a29`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, exc, root, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[12].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[12].body[1].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/security.py:150`; AST `2e6b1b638629a4d180d726faec9764eefef639906e49512772fe2adefd3a3fc1`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, root, value. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[1].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::confined_path::root.body[14].body[13]::Return

Source: `infra/agentinfra/security.py:151`; AST `d410503600f545372f82c2fcfd703177c9f4839bc0d43836156024b894cfa295`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: absolute. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Return evaluation at root.body[14].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15]::FunctionDef

Source: `infra/agentinfra/security.py:154`; AST `6b4d1204fbedcfbd6575ca88dd80c5c138550d267cf8233819cc2c5118227860`.

Rust module: `infra::agentinfra::security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, SecurityError, is_path_redirect, mode, os, path, stat. Outputs/bindings: mode.
Calls/effect boundaries: SecurityError, is_path_redirect, path.exists, path.stat, stat.S_IMODE.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[0]::If

Source: `infra/agentinfra/security.py:155`; AST `540435e39e1acc2b25d14e1296483c4fffc741e828a6848cb33d57d8032302a9`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, is_path_redirect, path. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError, is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[15].body[0]; no call, error or mutation may be omitted. Condition: is_path_redirect(path)
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[0].test::Call

Source: `infra/agentinfra/security.py:155`; AST `d9cac03fb65b00711ae1083fa305b5510d29827fd7fb7d268ae3ec96200e726a`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: is_path_redirect, path. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[0].body[0]::Raise

Source: `infra/agentinfra/security.py:156`; AST `edef943d05b3a2dde5d6c5a7ecc7ca1db23ee267d827141f9d96e051033f68d2`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, path. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[15].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[0].body[0].exc::Call

Source: `infra/agentinfra/security.py:156`; AST `a40ea9202288f7993102bc55c479cc16b858d05049673e031d8572ba2696395e`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, path. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[1]::If

Source: `infra/agentinfra/security.py:157`; AST `deb1fcbb3f25f07b00c374a98a29f6b044ad921400f44297a473926c75c296d3`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, mode, os, path, stat. Outputs/bindings: mode.
Calls/effect boundaries: SecurityError, path.exists, path.stat, stat.S_IMODE.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[15].body[1]; no call, error or mutation may be omitted. Condition: os.name != 'nt' and path.exists()
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[1].test.values[1]::Call

Source: `infra/agentinfra/security.py:157`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[1].body[0]::Assign

Source: `infra/agentinfra/security.py:158`; AST `f8c87485c10eccd1fa2683b700162281e801102798926f80aa0ca94128ab2113`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, stat. Outputs/bindings: mode.
Calls/effect boundaries: path.stat, stat.S_IMODE.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[1].body[0].value::Call

Source: `infra/agentinfra/security.py:158`; AST `5000b3727d4a08bc08940fc09e3a239c8cae85b8ce1b1e370944035830d61bda`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, stat. Outputs/bindings: (none).
Calls/effect boundaries: path.stat, stat.S_IMODE.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[1].body[0].value.args[0].value::Call

Source: `infra/agentinfra/security.py:158`; AST `d0f2660d5c576e75c41493128e9ef73fd43d1401a0dd272c961864f7164b7698`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[1].body[1]::If

Source: `infra/agentinfra/security.py:159`; AST `1d7a3ddd625efb2a3888dfbc31d22d4262ef7d1b9798caa59deb0cc93137ebcb`.

Rust module: `infra::agentinfra::security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SecurityError, mode, path. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered If evaluation at root.body[15].body[1].body[1]; no call, error or mutation may be omitted. Condition: mode & 18
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[1].body[1].body[0]::Raise

Source: `infra/agentinfra/security.py:160`; AST `c02dc8cb0332d3635b59ca55888e1be61eb72eb2635029486a4e5eb9a53c80ab`.

Rust module: `infra::agentinfra::security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SecurityError, mode, path. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Raise evaluation at root.body[15].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/security.py::module::ensure_private_control_file::root.body[15].body[1].body[1].body[0].exc::Call

Source: `infra/agentinfra/security.py:160`; AST `e2ba3fb2fdd2a4bc43bb594257e8fc10fd2fa5def37b00e2ce4f8c483ab98f18`.

Rust module: `infra::agentinfra::security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, mode, path. Outputs/bindings: (none).
Calls/effect boundaries: SecurityError.
Dependencies: __future__, os, pathlib, re, stat, typing.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
