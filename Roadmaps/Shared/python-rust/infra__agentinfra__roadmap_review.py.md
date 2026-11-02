# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 113. Inventory digest: `a958fe70c200240e176ccceb0a46fa04e08685a75ece919ab5280e9d00fb8159`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_review.py::module::root::Module

Source: `infra/agentinfra/roadmap_review.py:1`; AST `e83cbac8165075e02c883060fd7c0d78695fcf6b58a432f08d8712ce10bfe20f`.

Rust module: `infra::agentinfra::roadmap_review`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, STAGES, all, binding, bindings_current, bool, campaign_authorized, canonical, confined_path, content, decision, dict, digest, evidence, field, finding, findings, history, html, ident, k, len, list, packet, path, pieces, require, result, root, set, sorted, stage, state, str. Outputs/bindings: STAGES, binding, content, field, finding, history, ident, k, path, pieces, result.
Calls/effect boundaries: '\n'.join, all, bindings_current, bool, canonical, canonical(packet.get(field, 'NOT_SUPPLIED')).decode, confined_path, content.encode, decision.get, dict, digest, finding.get, html.escape, len, packet.get, path.read_text, pieces.append, require, result.setdefault, set, sorted, state.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_review.py:1`; AST `29576d3cdb8dd48aa7cc1274c04042b051868dc84fd15e07cf51589a1987a345`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_review.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_review.py:4`; AST `32039d9ad9a016b386309feff2a29eef4a120a02242b2161a1158157d3827d8b`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_review.py:5`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_review.py:7`; AST `90667013d879502f9a26720d3046dc1d0ae3c038defb37ca97439fd74e854917`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_review.py:8`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::root.body[6]::Assign

Source: `infra/agentinfra/roadmap_review.py:11`; AST `5bc121a68750c3a13fff4f6f1e0b3ace86bb6cad87505304d9192e1acb36906a`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: STAGES.
Calls/effect boundaries: (none).
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7]::FunctionDef

Source: `infra/agentinfra/roadmap_review.py:14`; AST `27b17e4bc57746418e63dffd84d16df7c7eeaaf07c095c8d345862b234385190`.

Rust module: `infra::agentinfra::roadmap_review`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, binding, bindings_current, canonical, confined_path, content, dict, digest, field, html, len, packet, path, pieces, require, root, str. Outputs/bindings: binding, content, field, path, pieces.
Calls/effect boundaries: '\n'.join, bindings_current, canonical, canonical(packet.get(field, 'NOT_SUPPLIED')).decode, confined_path, content.encode, digest, html.escape, len, packet.get, path.read_text, pieces.append, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_review.py:15`; AST `97db6f14b2e8ce41a722b2f8ac7258f1a522aef0ffaa6f3f2a46ace4d6032e72`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: packet, require. Outputs/bindings: (none).
Calls/effect boundaries: packet.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_review.py:15`; AST `25640c2dcc8615a7b0a2fc5b77e391eb43acbf2af0f8027ff506d3ae677d9201`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet, require. Outputs/bindings: (none).
Calls/effect boundaries: packet.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_review.py:15`; AST `a330d28aec4fa7c7b9d1a6f603b25d0dc129c74b3fecb6c5d9bd008b7c6d1aaf`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[1]::Expr

Source: `infra/agentinfra/roadmap_review.py:16`; AST `9a25b9c8130bd05e40437abfd8b94b07efe99401ad5b4a3bb289ff770a33c5d1`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, packet, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, packet.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[1].value::Call

Source: `infra/agentinfra/roadmap_review.py:16`; AST `2119de4b04f139322601817dcafa26dd39516474de240fdc902b4b5e0c6ed547`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, packet, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, packet.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:16`; AST `da7553f21e0896d5efb9856eac005577d841cd44f4d5721e94fbd4daa6d8b564`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, packet, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, packet.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[1].value.args[0].args[1]::Call

Source: `infra/agentinfra/roadmap_review.py:16`; AST `0edf6b08e61f5c754addc76dc753651ef618a0e36e92b825e7ee81699d21bf27`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[2]::Assign

Source: `infra/agentinfra/roadmap_review.py:17`; AST `b300172048a0834527f9ea30ae2b7412e0cd681a0f8926806487830136970851`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, packet. Outputs/bindings: pieces.
Calls/effect boundaries: digest.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[2].value.elts[4].values[1].value::Call

Source: `infra/agentinfra/roadmap_review.py:21`; AST `d611aad9a9dc53f0313a7dfede14788818618d6fe3dfd8a304073fee9626c685`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, packet. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].value.elts[4].values[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3]::For

Source: `infra/agentinfra/roadmap_review.py:22`; AST `278dbb0eeae7925b1795c022cb2c0c3f688105d139d9f4da618fd7b653e6dcdd`.

Rust module: `infra::agentinfra::roadmap_review`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, confined_path, content, html, len, packet, path, pieces, require, root. Outputs/bindings: binding, content, path.
Calls/effect boundaries: confined_path, content.encode, html.escape, len, path.read_text, pieces.append, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered For evaluation at root.body[7].body[3]; no call, error or mutation may be omitted. Iteration: binding in packet['inputs']
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_review.py:23`; AST `a5ea970cb68c88517e7e08f46baafbcdf656b2fb86353fdc4a22720940ffb9b9`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, confined_path, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_review.py:23`; AST `e93e7f2e055f15c3c8a83d6679f6cba3cc79f2c763673a69522794ba24c465f4`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_review.py:24`; AST `c69ac8f7fc31ec2a943849c7c1fd82976b98a169e1a56377e6e55142bc36a0a3`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: content.
Calls/effect boundaries: path.read_text.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_review.py:24`; AST `d7d2b1d3f5b3313cd24906b00f77863075a83ccc502a11ff12b073fd43d10854`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap_review.py:25`; AST `571d7a43f4ef68c68e8f382c7ad2a4f5fab156ab1fe72f21f7acb81099df6014`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: content, len, require. Outputs/bindings: (none).
Calls/effect boundaries: content.encode, len, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_review.py:25`; AST `4d3257c8dfc74586593ae5f320658556327678ae8a42225407b67488a7a68908`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content, len, require. Outputs/bindings: (none).
Calls/effect boundaries: content.encode, len, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_review.py:25`; AST `87009a06c42c936e419415306577bd7ff5f5cce2278545822fac3817e5ddaf30`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content, len. Outputs/bindings: (none).
Calls/effect boundaries: content.encode, len.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[2].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:25`; AST `afb1628361c96c3ef5d11385774759e83fdc9a907c70bbd3cbb4a6a834ad4563`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content. Outputs/bindings: (none).
Calls/effect boundaries: content.encode.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[2].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[3]::Expr

Source: `infra/agentinfra/roadmap_review.py:26`; AST `17481087a556ac481a990f4b1e31d29dda9511bd92cd601dd0aae8f4c2e7cef4`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, content, html, pieces. Outputs/bindings: (none).
Calls/effect boundaries: html.escape, pieces.append.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[3].value::Call

Source: `infra/agentinfra/roadmap_review.py:26`; AST `c1f3737a249eac899368aed4a9cb18b7665190ebd34b5dad09b35af987d7e3d6`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, content, html, pieces. Outputs/bindings: (none).
Calls/effect boundaries: html.escape, pieces.append.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[3].value.args[0].values[1].value::Call

Source: `infra/agentinfra/roadmap_review.py:26`; AST `b824f60b83638c10e270d6ba0b239ade395a5e5112c7dea41d3ac2056a577b72`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, html. Outputs/bindings: (none).
Calls/effect boundaries: html.escape.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[3].value.args[0].values[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[3].body[3].value.args[0].values[5].value::Call

Source: `infra/agentinfra/roadmap_review.py:26`; AST `3bbf4e3db82b156aa843a3c9916b2949acb3845399fed4404120f5f08c550c48`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: content, html. Outputs/bindings: (none).
Calls/effect boundaries: html.escape.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[3].value.args[0].values[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[4]::For

Source: `infra/agentinfra/roadmap_review.py:27`; AST `c7b6a0528055a99c9214c328a174fa9b10178bc908f6d46f217bd5259e15e654`.

Rust module: `infra::agentinfra::roadmap_review`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: canonical, field, html, packet, pieces. Outputs/bindings: field.
Calls/effect boundaries: canonical, canonical(packet.get(field, 'NOT_SUPPLIED')).decode, html.escape, packet.get, pieces.append.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered For evaluation at root.body[7].body[4]; no call, error or mutation may be omitted. Iteration: field in ('original_test', 'semantics', 'harness', 'production_path', 'assumptions', 'bounds', 'assertions', 'covers', 'counterexamples', 'changes', 'outcomes')
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_review.py:29`; AST `2c26df33ced34e23d87bb7143bb160494eb9acf2ddeb1d4e94afd054b78c6741`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, field, html, packet, pieces. Outputs/bindings: (none).
Calls/effect boundaries: canonical, canonical(packet.get(field, 'NOT_SUPPLIED')).decode, html.escape, packet.get, pieces.append.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_review.py:29`; AST `e17388fbace6f0bee3f5656cad1875701cd2b69eed3904b3342624c6121b1b8e`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, field, html, packet, pieces. Outputs/bindings: (none).
Calls/effect boundaries: canonical, canonical(packet.get(field, 'NOT_SUPPLIED')).decode, html.escape, packet.get, pieces.append.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[4].body[0].value.args[0].values[3].value::Call

Source: `infra/agentinfra/roadmap_review.py:29`; AST `ca92a8a2f11f7db0aea999ed49f345baf096377b5f6b6b02334ae942a3277457`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, field, html, packet. Outputs/bindings: (none).
Calls/effect boundaries: canonical, canonical(packet.get(field, 'NOT_SUPPLIED')).decode, html.escape, packet.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[0].value.args[0].values[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[4].body[0].value.args[0].values[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:29`; AST `954907b1ab926f7d42f848bcb1dc1e4652d3a8f6657d61969c4806792f8498b4`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, field, packet. Outputs/bindings: (none).
Calls/effect boundaries: canonical, canonical(packet.get(field, 'NOT_SUPPLIED')).decode, packet.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[0].value.args[0].values[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[4].body[0].value.args[0].values[3].value.args[0].func.value::Call

Source: `infra/agentinfra/roadmap_review.py:29`; AST `cc5919d3da555f7e9cebc6904b4aa3ba2bde592bc8ff77a32bae38d75f8d9cb3`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, field, packet. Outputs/bindings: (none).
Calls/effect boundaries: canonical, packet.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[0].value.args[0].values[3].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[4].body[0].value.args[0].values[3].value.args[0].func.value.args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:29`; AST `5018a536da6cc82ba073a6ba84d9705bc261f60343453da519a6d5b38b52721a`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[0].value.args[0].values[3].value.args[0].func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[5]::Expr

Source: `infra/agentinfra/roadmap_review.py:30`; AST `e871392e160ccc484cbd79ba05cb4acc02cefa85c88989d7026f0c0bfbeaacd9`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pieces. Outputs/bindings: (none).
Calls/effect boundaries: pieces.append.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[5].value::Call

Source: `infra/agentinfra/roadmap_review.py:30`; AST `36ca358585562a87d69000a34536611c790acda805263850458f9287fff34148`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pieces. Outputs/bindings: (none).
Calls/effect boundaries: pieces.append.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[6]::Return

Source: `infra/agentinfra/roadmap_review.py:31`; AST `217acbf760a20e52a788160d38f15e1482d9aec68946e6d69a91fc5496955801`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pieces. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::render_packet::root.body[7].body[6].value::Call

Source: `infra/agentinfra/roadmap_review.py:31`; AST `d2151ad2f9db507851ce7e786324bfbab7afdb5d73c0e86b3ee03011d06f496d`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pieces. Outputs/bindings: (none).
Calls/effect boundaries: '\n'.join.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8]::FunctionDef

Source: `infra/agentinfra/roadmap_review.py:34`; AST `ececc5d4433635a2eb12403a912a6f621a8cc70d7aada79157d5d2d02a018d84`.

Rust module: `infra::agentinfra::roadmap_review`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bool, decision, dict, digest, packet, require, set. Outputs/bindings: (none).
Calls/effect boundaries: bool, decision.get, digest, packet.get, require, set.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[0]::Expr

Source: `infra/agentinfra/roadmap_review.py:35`; AST `e2834583603855c1efac3ee11c2b6f15e4e4e218d22b7a1a67010c730fdb4038`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: decision, require. Outputs/bindings: (none).
Calls/effect boundaries: decision.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_review.py:35`; AST `ac20cd64f3853f00b9afa0917fa148ae6c925fb000a81adebd65367ee1434da9`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision, require. Outputs/bindings: (none).
Calls/effect boundaries: decision.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_review.py:35`; AST `a260952d24f2b406fd0d54dd7d43253eae11173c213161664834febf20f51d7f`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision. Outputs/bindings: (none).
Calls/effect boundaries: decision.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[1]::Expr

Source: `infra/agentinfra/roadmap_review.py:36`; AST `3286767e331be81f555b96976e5a4143c9ba33da55d4e48115e76aed8ca55c6f`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: decision, digest, packet, require. Outputs/bindings: (none).
Calls/effect boundaries: decision.get, digest, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[1].value::Call

Source: `infra/agentinfra/roadmap_review.py:36`; AST `7e38c1a2bcb2ebc44588a05d71c09eba34df71696b0cf2a367b2bc41d060fdcc`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision, digest, packet, require. Outputs/bindings: (none).
Calls/effect boundaries: decision.get, digest, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_review.py:36`; AST `245b8ea9b292c14e2a6518ecd1d08adc2a15b7bde5a2c30e4c273848921367bf`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision. Outputs/bindings: (none).
Calls/effect boundaries: decision.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[1].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_review.py:36`; AST `d611aad9a9dc53f0313a7dfede14788818618d6fe3dfd8a304073fee9626c685`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, packet. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[1].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[2]::Expr

Source: `infra/agentinfra/roadmap_review.py:37`; AST `4a41c5d061eb8486f87babb2902c7d9b28bfc17a3da29b1121ffc7f5d506e767`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: decision, require. Outputs/bindings: (none).
Calls/effect boundaries: decision.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[2].value::Call

Source: `infra/agentinfra/roadmap_review.py:37`; AST `9da6ee811262a828a192e2a2129365b30996025d0a0cf664de25bac24bd04453`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision, require. Outputs/bindings: (none).
Calls/effect boundaries: decision.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_review.py:37`; AST `6613a47e3263753ccfd2060fcde8cc8ed5529fcf94590c534c1269fc6f9cd9f1`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision. Outputs/bindings: (none).
Calls/effect boundaries: decision.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[3]::Expr

Source: `infra/agentinfra/roadmap_review.py:38`; AST `298c35052a1a35831b00f824ecc49beb17be7ea98a147cddc2ef562d90d8c25a`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, decision, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, decision.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[3].value::Call

Source: `infra/agentinfra/roadmap_review.py:38`; AST `b3ad4aced2b437db95cd7d95a381bd7c10182f4b99de7800b026fcda41405209`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, decision, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, decision.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[3].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_review.py:38`; AST `9f29dfebad5dd204d5772acce4ed262a518891ad06aa0969fd8ebbbcdb1b6e1f`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, decision. Outputs/bindings: (none).
Calls/effect boundaries: bool, decision.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[3].value.args[0].values[0].args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:38`; AST `6885287f948f7a1572bff875e0cb3e4ff76c8217cc7f70792e59afe8fe25c78d`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision. Outputs/bindings: (none).
Calls/effect boundaries: decision.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[3].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_review.py:38`; AST `2714cc5f0792ecd55acc1cdb6f6f45c4a60c88d55c8272237777496c32bdcb2b`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, decision. Outputs/bindings: (none).
Calls/effect boundaries: bool, decision.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[3].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:38`; AST `3e96dd0e23174efb1a30a6ef0ce91f3fef26da3fe83a52cf4df12111e1950b64`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision. Outputs/bindings: (none).
Calls/effect boundaries: decision.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[3].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_review.py:39`; AST `0953ab497e7e2016c9844b9eded9bc30a7a45b24038cd516da72dc18636e9af6`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, decision. Outputs/bindings: (none).
Calls/effect boundaries: bool, decision.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[3].value.args[0].values[2].args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:39`; AST `babf5e5e5deebb29d53242a72e11e635e786b61f7efe441276872d9c9cfbfecc`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision. Outputs/bindings: (none).
Calls/effect boundaries: decision.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[4]::Expr

Source: `infra/agentinfra/roadmap_review.py:40`; AST `895f8a5ed573383209de35e5af8af9f905389c051b9b17d16f763061d48066bc`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: decision, packet, require, set. Outputs/bindings: (none).
Calls/effect boundaries: packet.get, require, set.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[4].value::Call

Source: `infra/agentinfra/roadmap_review.py:40`; AST `b2470000acd902ef657b4fad422bbb4a48b685cabfe748fed9b69257921fb3b5`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision, packet, require, set. Outputs/bindings: (none).
Calls/effect boundaries: packet.get, require, set.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[4].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_review.py:40`; AST `504b2eb36fadfed9c445ffcc3da19c631e7056be629cc4895c9a76e15a9c6a44`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet. Outputs/bindings: (none).
Calls/effect boundaries: packet.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[4].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_review.py:40`; AST `0b178597b3ce860862da92e1b5267b37175f5d613240961f3b8dd8fb381bd12e`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: decision, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::validate_decision::root.body[8].body[4].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_review.py:40`; AST `b3d5ffa4ee0b58d323d028e39f30c40db3109a7dada7494398d8ce9d6c8adb2e`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: packet, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9]::FunctionDef

Source: `infra/agentinfra/roadmap_review.py:44`; AST `9def943356e50cb4283a4b0d3d385319ac5c3e9682b1251c438b038a63e4f1c2`.

Rust module: `infra::agentinfra::roadmap_review`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: STAGES, bool, campaign_authorized, dict, evidence, history, len, list, require, stage, state, str. Outputs/bindings: history.
Calls/effect boundaries: bool, dict, len, require, state.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[0]::Expr

Source: `infra/agentinfra/roadmap_review.py:45`; AST `e65b39d5e2de04813454101d5bac878e19b97879dd57eeb7def8b490251f8505`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: campaign_authorized, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[0].value::Call

Source: `infra/agentinfra/roadmap_review.py:45`; AST `468e3f7f532d10da95bd579c53a3e9f2e85e72ab78d8088b3d24a255ea1caa76`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: campaign_authorized, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[1]::Expr

Source: `infra/agentinfra/roadmap_review.py:46`; AST `ec9b11ea1993efaf7635c942ffe433149e35c24301115d8322bfd8bb496ac755`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, state. Outputs/bindings: (none).
Calls/effect boundaries: require, state.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[1].value::Call

Source: `infra/agentinfra/roadmap_review.py:46`; AST `4da4b360a28e8bcc52ec48056a060132bd69bd99877725ae66fd9c7c77db3cef`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, state. Outputs/bindings: (none).
Calls/effect boundaries: require, state.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_review.py:46`; AST `e3d16e1edd2313a98028a536dbf7d28c6dac3f2a79679ed02ce9a6bf83d0fc26`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[2]::Assign

Source: `infra/agentinfra/roadmap_review.py:47`; AST `f70f2c30d0cc97c7284cce174fff8e76ce5a7ecfdb6355a2433e16227abb73e1`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: history.
Calls/effect boundaries: state.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[2].value::Call

Source: `infra/agentinfra/roadmap_review.py:47`; AST `a590fea8263805a900237f975cbf6e5a00a8c203251b5f457acfafd2e5dcf4e1`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[3]::Expr

Source: `infra/agentinfra/roadmap_review.py:48`; AST `0e60661f520c27b10304f3cb65a79a95c3564d504920063196ca4b1de2ed62ce`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: STAGES, history, len, require, stage. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[3].value::Call

Source: `infra/agentinfra/roadmap_review.py:48`; AST `567903c45b1d2b6e5e28e6d96b4693c91d47873fb5bd8422591db58d3c10826c`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: STAGES, history, len, require, stage. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[3].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_review.py:48`; AST `8fd7f23e8ca1b1f62232eca3c2d445e52b36e10342fab14469e18a9030cabbf0`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: history, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[3].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_review.py:48`; AST `883177fde3e94703fe36d5a0abcf7d40d6c6b861285d5e1c3fda2b220fbfe880`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: STAGES, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[3].value.args[0].values[1].left.slice::Call

Source: `infra/agentinfra/roadmap_review.py:48`; AST `8fd7f23e8ca1b1f62232eca3c2d445e52b36e10342fab14469e18a9030cabbf0`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: history, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].value.args[0].values[1].left.slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[4]::Expr

Source: `infra/agentinfra/roadmap_review.py:49`; AST `92371926ee3f984a8e87fa370feb8db39914220556eda5c49138ef3c602d2965`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, evidence, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[4].value::Call

Source: `infra/agentinfra/roadmap_review.py:49`; AST `746ededbb0b30a742860194480e46d3144c033207a9a948fe4e1a6eac73aa12c`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, evidence, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:49`; AST `08987c720604a3403ee05ee9a9dc01d0a5d7c9e17bd06edc2b02b0a7339bc375`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, evidence. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[5]::Return

Source: `infra/agentinfra/roadmap_review.py:50`; AST `a728bd508cb63586034a43521e05f989d2714fe911478f6a693b31bbef584ba2`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, evidence, history, stage, state. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::advance_review::root.body[9].body[5].value::Call

Source: `infra/agentinfra/roadmap_review.py:50`; AST `5904d100f1c58052f646f1a845eacd232352c16ec28c97aa6a9bed6bdc029f1c`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, evidence, history, stage, state. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10]::FunctionDef

Source: `infra/agentinfra/roadmap_review.py:53`; AST `c576378bf5f571b2b8d6de291444212d5807ae3b0df0718debf62a2a5d48115c`.

Rust module: `infra::agentinfra::roadmap_review`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, all, bindings_current, bool, dict, digest, finding, findings, ident, k, list, require, result, root, sorted. Outputs/bindings: finding, ident, k, result.
Calls/effect boundaries: all, bindings_current, bool, dict, digest, finding.get, require, result.setdefault, sorted.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_review.py:54`; AST `2c435ecac12c985901bb8025f4efe5e5ad7e200542d8b36f3e0370612550a391`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: result.
Calls/effect boundaries: (none).
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1]::For

Source: `infra/agentinfra/roadmap_review.py:55`; AST `469f751b9aeac1293af010879b7b8465b30179568e06f758c178f413bd8a4097`.

Rust module: `infra::agentinfra::roadmap_review`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: all, bindings_current, bool, dict, digest, finding, findings, ident, k, require, result, root. Outputs/bindings: finding, ident, k.
Calls/effect boundaries: all, bindings_current, bool, dict, digest, finding.get, require, result.setdefault.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered For evaluation at root.body[10].body[1]; no call, error or mutation may be omitted. Iteration: finding in findings
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_review.py:56`; AST `1bc3df198e95fb2b2c54c783ebcfb260fc1d59c5be13ac5042390b2561050c8e`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: finding, require. Outputs/bindings: (none).
Calls/effect boundaries: finding.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_review.py:56`; AST `0fce8c5817340a3c91e1a3044c39d67fe27b6434d07e964e05fb93caa66c33e3`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: finding, require. Outputs/bindings: (none).
Calls/effect boundaries: finding.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_review.py:56`; AST `542c2952f37d71de1d8fe41cf91872ab33fbf05de47734f1f8c8cdba40ccae54`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: finding. Outputs/bindings: (none).
Calls/effect boundaries: finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[1]::Expr

Source: `infra/agentinfra/roadmap_review.py:57`; AST `5a201f8fc27a3efa126255a5245f3ff75bb3fa4ad75f1d79894bbf481231240b`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, finding, k, require. Outputs/bindings: k.
Calls/effect boundaries: all, finding.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_review.py:57`; AST `641c7f90fa4556ee771f15905a5b1693210b6ac0232319f642e1ca814e8ff54f`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, finding, k, require. Outputs/bindings: k.
Calls/effect boundaries: all, finding.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:57`; AST `a7a6694c8304b3b2671a82f357e8f58f2c12708df32cc4e94e2da5e332cb9692`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, finding, k. Outputs/bindings: k.
Calls/effect boundaries: all, finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[1].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_review.py:57`; AST `f70edd6e3e70052d4bfbeff44a155717aa9401b372f37d463f88db939d51a04e`.

Rust module: `infra::agentinfra::roadmap_review`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: finding, k. Outputs/bindings: k.
Calls/effect boundaries: finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[10].body[1].body[1].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[1].value.args[0].args[0].elt::Call

Source: `infra/agentinfra/roadmap_review.py:57`; AST `5dfe41f4b7035c8bda03901ae0cdc3554604e75d176b474e9712423cd6540f90`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: finding, k. Outputs/bindings: (none).
Calls/effect boundaries: finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[1].value.args[0].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_review.py:58`; AST `f9766db08565bf750ec4b4ea6e5ac9b32436faa78811fad49c8cd319c9bc7085`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, finding, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, finding.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_review.py:58`; AST `2f263c189117e454c17729ff8308fbaf60d860111cbc6d0de73e816c0c06f009`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, finding, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, finding.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:58`; AST `239c013f5fafebfdc62e4466e29c904940c6a5db26493f5de4e11d2d5f39ea43`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, finding, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[2].value.args[0].args[1]::Call

Source: `infra/agentinfra/roadmap_review.py:58`; AST `e31623868eeafb7452c596dadaaafaf114c9c1d86ef2a63e4a6feb3cd157a128`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: finding. Outputs/bindings: (none).
Calls/effect boundaries: finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[3]::If

Source: `infra/agentinfra/roadmap_review.py:59`; AST `08450db3aefb0fdee824f83712b0ccf874439e9cef9e86c8d33f8036c3adb40d`.

Rust module: `infra::agentinfra::roadmap_review`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: bool, finding, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, finding.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered If evaluation at root.body[10].body[1].body[3]; no call, error or mutation may be omitted. Condition: finding['classification'] == 'confirmed'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_review.py:60`; AST `af5a681ba214c1f2b9e3eece10a7f88b36896c6a4e833946f21047c12cae6148`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, finding, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, finding.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_review.py:60`; AST `7bd98317ef41b5d5bbac0258cb0a6226e7a3858755898c7bff2cccbfd8d24a91`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, finding, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, finding.get, require.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[3].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:60`; AST `4c81cf9b2f47bd4616c9fe2b2b2dc8728f24f41499373b3209e426fbb9aed298`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, finding. Outputs/bindings: (none).
Calls/effect boundaries: bool, finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[3].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[3].body[0].value.args[0].args[0]::Call

Source: `infra/agentinfra/roadmap_review.py:60`; AST `d0f7f9309a4c9c4f0a877410b84aa1f902b9cef27b9119f93a829788ca8e21d7`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: finding. Outputs/bindings: (none).
Calls/effect boundaries: finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[3].body[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[4]::Assign

Source: `infra/agentinfra/roadmap_review.py:61`; AST `b1d610e0a3ef1e39a219b4537562ab7b29530451a5c7cb9f2452832e16c9b9bc`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, finding. Outputs/bindings: ident.
Calls/effect boundaries: digest, finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[4].value::Call

Source: `infra/agentinfra/roadmap_review.py:61`; AST `08985d902f3f5ac946fb2118c780c48e691f2f1407289065b1c5afe23a11d577`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, finding. Outputs/bindings: (none).
Calls/effect boundaries: digest, finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[4].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_review.py:62`; AST `d0f7f9309a4c9c4f0a877410b84aa1f902b9cef27b9119f93a829788ca8e21d7`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: finding. Outputs/bindings: (none).
Calls/effect boundaries: finding.get.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[4].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[5]::Expr

Source: `infra/agentinfra/roadmap_review.py:63`; AST `60e918021296eaabee83ed8f67ea171cc7e1d650844a4dd1f2b4692ed902bf68`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, finding, ident, result. Outputs/bindings: (none).
Calls/effect boundaries: dict, result.setdefault.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[5].value::Call

Source: `infra/agentinfra/roadmap_review.py:63`; AST `2cf6e94a47eba72c67acdd2f730c923318dfdc05f2dd045a213d875e02d94eac`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, finding, ident, result. Outputs/bindings: (none).
Calls/effect boundaries: dict, result.setdefault.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[1].body[5].value.args[1]::Call

Source: `infra/agentinfra/roadmap_review.py:63`; AST `1aef31d88de705766129eecb0669921c0be5664ca248827aedc5d1e6f75d4f6f`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, finding, ident. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[5].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[2]::Return

Source: `infra/agentinfra/roadmap_review.py:64`; AST `b04d1183e40ab8facf9e7fe12e0ef1ab723343a62af9ee2dd9822e73db39dd98`.

Rust module: `infra::agentinfra::roadmap_review`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: k, result, sorted. Outputs/bindings: k.
Calls/effect boundaries: sorted.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Return evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[2].value::ListComp

Source: `infra/agentinfra/roadmap_review.py:64`; AST `a05965ea541be4f07b925ca1c1b2a136c2204febf10b75842cfd476bf6de3f58`.

Rust module: `infra::agentinfra::roadmap_review`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: k, result, sorted. Outputs/bindings: k.
Calls/effect boundaries: sorted.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered ListComp evaluation at root.body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_review.py::module::adjudicate_findings::root.body[10].body[2].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_review.py:64`; AST `86b51074d48d90fd6f01f51a310a7fa23e29764131eea529168156300a0d3346`.

Rust module: `infra::agentinfra::roadmap_review`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, html, pathlib, roadmap_records, security.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
