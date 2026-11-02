# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 219. Inventory digest: `151bab9d15b0cdafc5fa864645a7835e71ddae97c13165695562bffc12794ea1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/coverage.py::module::root::Module

Source: `infra/agentinfra/coverage.py:1`; AST `1339c7626186ad0ad9a690d578dc093cbb20ea76062522e64d1c4c4514fb095a`.

Rust module: `infra::agentinfra::coverage`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: LANES, a, all, any, assertion, bool, c, confined_path, d, declared, dependency, dict, document, found, identity, index, int, inventory, inventory_path, isinstance, lane, len, levels, lines, list, load_json, original, original_cases, p, path, proofs, property_name, r, record, require, requirements, residual, reviewed, root, rows, rust, set, sha256_file, source, str, type. Outputs/bindings: LANES, a, assertion, c, d, declared, dependency, document, found, identity, index, inventory, inventory_path, lane, levels, lines, original, original_cases, p, path, r, record, requirements, residual, reviewed, rust, source.
Calls/effect boundaries: all, any, assertion.get, assertion['rule'].strip, bool, confined_path, dependency.get, dependency['relation'].strip, document.get, inventory.get, inventory_path.read_text, inventory_path.stat, isinstance, len, load_json, p.get, p.get('assertion_locations', {}).get, path.exists, path.read_text, path.stat, property_name, r['relation'].strip, record.get, record['execution_review'].strip, record['reference_review'].strip, record['required_obligations'].values, require, rust.get, set, set(r['assertion_properties']).issubset, sha256_file, source.read_text, source.read_text().splitlines, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::root.body[0]::Expr

Source: `infra/agentinfra/coverage.py:1`; AST `a103b00ef32ec5eadc6ad7125f4154835af7f04306a77665c6ed43b733e3fe5d`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::root.body[1]::Import

Source: `infra/agentinfra/coverage.py:2`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/coverage.py:3`; AST `6af63389e56de12581c260caf6303d1a9dc6fd9f1017e14e5b28653ebac1d166`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/coverage.py:4`; AST `74cec6df97530979bb0cb0be45097b409e88e7221caa19e2b1280902b92cd7c8`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/coverage.py:5`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/coverage.py:6`; AST `e456569099f8fa56244a81c6525e3b7d23eb6fec49bd0b141f3aab195a2e97d1`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::root.body[6]::Assign

Source: `infra/agentinfra/coverage.py:8`; AST `394423ff79e6638e61d7762c45ce762160dc85252014a522eaad78b7603271aa`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: LANES.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7]::FunctionDef

Source: `infra/agentinfra/coverage.py:11`; AST `466d082011fb999465aa05a4642bcca7ae7a4b25bd9c3bf66d6d0ebd9c560490`.

Rust module: `infra::agentinfra::coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: LANES, a, all, assertion, bool, c, confined_path, d, declared, dependency, dict, document, found, identity, index, int, inventory, inventory_path, isinstance, lane, len, lines, list, load_json, original, original_cases, p, path, property_name, r, record, require, requirements, residual, root, rows, rust, set, sha256_file, source, str, type. Outputs/bindings: a, assertion, c, d, declared, dependency, document, found, identity, index, inventory, inventory_path, lane, lines, original, original_cases, p, path, r, record, requirements, residual, rust, source.
Calls/effect boundaries: all, assertion.get, assertion['rule'].strip, bool, confined_path, dependency.get, dependency['relation'].strip, document.get, inventory.get, inventory_path.read_text, inventory_path.stat, isinstance, len, load_json, path.exists, path.read_text, path.stat, property_name, r['relation'].strip, record.get, record['execution_review'].strip, record['reference_review'].strip, record['required_obligations'].values, require, rust.get, set, sha256_file, source.read_text, source.read_text().splitlines, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[0]::Assign

Source: `infra/agentinfra/coverage.py:12`; AST `3d8c8a2d7687baf3f26ce5a09e9791adc10c57b0adc91cab147d58b9962ce57d`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[0].value::Call

Source: `infra/agentinfra/coverage.py:12`; AST `4895aa79a1b260a5c73b2551062e562bd41e35ccbf4dca7f289508acce98a425`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[1]::If

Source: `infra/agentinfra/coverage.py:13`; AST `7482ba787b9047f5257a77ceff815c1e420c561c8fb0f1f993d982e942b04c17`.

Rust module: `infra::agentinfra::coverage`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered If evaluation at root.body[7].body[1]; no call, error or mutation may be omitted. Condition: not path.exists()
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[1].test.operand::Call

Source: `infra/agentinfra/coverage.py:13`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].test.operand; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[1].body[0]::Return

Source: `infra/agentinfra/coverage.py:14`; AST `99539d16b3c55a78e0ab0338d294ed31e812ad2d3fb18d6983c893234f79bcb3`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Return evaluation at root.body[7].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[2]::Expr

Source: `infra/agentinfra/coverage.py:15`; AST `5911b5191fbc0290a12e935ab84504d46284fb71abb7becb8febff54ba11f494`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, require. Outputs/bindings: (none).
Calls/effect boundaries: path.stat, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[2].value::Call

Source: `infra/agentinfra/coverage.py:15`; AST `abf7ef7b638ce9170e1864985b3f8bc7374e789b3a1038c16f232193058663c4`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, require. Outputs/bindings: (none).
Calls/effect boundaries: path.stat, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[2].value.args[0].left.value::Call

Source: `infra/agentinfra/coverage.py:15`; AST `4ad13a92d4c0491c8737b8fcfacd38c225911ac2f24bdb5ec5c2f1fd76d4a178`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[3]::Assign

Source: `infra/agentinfra/coverage.py:16`; AST `b10d755ce9959eb92bb0a44ac3f8df4de0ea7cb8adbbb3685e6ad02c1a2e2cdc`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: load_json, path. Outputs/bindings: document.
Calls/effect boundaries: load_json, path.read_text.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[3].value::Call

Source: `infra/agentinfra/coverage.py:16`; AST `30814c43de501d3d01acd51e21e30ba71ad1182f9ac92cd239bd4c026c01ef85`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_json, path. Outputs/bindings: (none).
Calls/effect boundaries: load_json, path.read_text.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[3].value.args[0]::Call

Source: `infra/agentinfra/coverage.py:16`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[4]::Expr

Source: `infra/agentinfra/coverage.py:17`; AST `56c4697df10b7f39f65a1cbd7e75df2601959e555a0a33b4e5e4954fa0fa2f5c`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: document, require, rows. Outputs/bindings: (none).
Calls/effect boundaries: document.get, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[4].value::Call

Source: `infra/agentinfra/coverage.py:17`; AST `7d192c655c8c9eceb8e8f0a674ee29b30c492b2627a35e96d9200f50be05ac56`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: document, require, rows. Outputs/bindings: (none).
Calls/effect boundaries: document.get, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[4].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:17`; AST `1cfbac0739ac4bde8f59b01e04eeba2e834351d7a96059d947faf208e5be4b71`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: document. Outputs/bindings: (none).
Calls/effect boundaries: document.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[4].value.args[0].values[1].left::Call

Source: `infra/agentinfra/coverage.py:17`; AST `4942bfdcb776a058b45882696690b33335395228576c080e1a02d1de5771e32e`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: document. Outputs/bindings: (none).
Calls/effect boundaries: document.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[5]::Expr

Source: `infra/agentinfra/coverage.py:19`; AST `906da1424626152eecdc3ef912f5b4665adac7cded68e4bb45be5fc95e7ffe35`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: document, list, require, type. Outputs/bindings: (none).
Calls/effect boundaries: document.get, require, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[5].value::Call

Source: `infra/agentinfra/coverage.py:19`; AST `615add9d3ef3feeecfaaf340ee8122183dd766986a896d168b6ad6f02d15e2f4`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: document, list, require, type. Outputs/bindings: (none).
Calls/effect boundaries: document.get, require, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[5].value.args[0].left::Call

Source: `infra/agentinfra/coverage.py:19`; AST `479a223d60eaa6beff2ad11b1e0875941b2e7e7847aeaf0a8cc904302564e591`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: document, type. Outputs/bindings: (none).
Calls/effect boundaries: document.get, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[5].value.args[0].left.args[0]::Call

Source: `infra/agentinfra/coverage.py:19`; AST `dec030bcad2a293716a292f782dd03640707cdd44da20e22ec1236ad0add5fd2`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: document. Outputs/bindings: (none).
Calls/effect boundaries: document.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[6]::Assign

Source: `infra/agentinfra/coverage.py:20`; AST `6cc0b94146fe0f30b7563602a32d1ea7b06a4c617353b62c0e532f8752b4dc57`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r, rows. Outputs/bindings: index, r.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[6].value::DictComp

Source: `infra/agentinfra/coverage.py:20`; AST `1a9655c3f2b84680d3d99c2c512c6f5eae568c18af69a4d87fa85f82fc8972a2`.

Rust module: `infra::agentinfra::coverage`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: r, rows. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered DictComp evaluation at root.body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[7]::Assign

Source: `infra/agentinfra/coverage.py:21`; AST `0d12cdf52c63b02887211792d663c789c4f538f1a5172647312e2b0c52fc1b1b`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, root. Outputs/bindings: inventory_path.
Calls/effect boundaries: confined_path.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[7].value::Call

Source: `infra/agentinfra/coverage.py:21`; AST `27fb3f14af59dfb689031e165ca05d4e6499d54568fb613eb6dfa605689cf2c4`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[8]::Expr

Source: `infra/agentinfra/coverage.py:22`; AST `34642492974eb496220731636afe5738207967bfcf3ded898593a0f599e22be9`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory_path, require. Outputs/bindings: (none).
Calls/effect boundaries: inventory_path.stat, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[8]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[8].value::Call

Source: `infra/agentinfra/coverage.py:22`; AST `7adb2fae158325b693794e049003e4bcc70920f1507c977120edb18bce1c846a`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory_path, require. Outputs/bindings: (none).
Calls/effect boundaries: inventory_path.stat, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[8].value.args[0].left.value::Call

Source: `infra/agentinfra/coverage.py:22`; AST `ddbf506e20d71f7ac2e57543162836d14799ce084b98677d8cfcf7584fa3096f`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory_path. Outputs/bindings: (none).
Calls/effect boundaries: inventory_path.stat.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[8].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[9]::Assign

Source: `infra/agentinfra/coverage.py:23`; AST `3e45c885a24e3526ef6204b0f3ac6c18ee85a426dfa31979f831d296c16861d3`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory_path, load_json. Outputs/bindings: inventory.
Calls/effect boundaries: inventory_path.read_text, load_json.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[9]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[9].value::Call

Source: `infra/agentinfra/coverage.py:23`; AST `70cbab16bf5bec76d6c0e7ad8648e1d3e0104a8ad341e9df9ba4d3e7b3d672bd`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory_path, load_json. Outputs/bindings: (none).
Calls/effect boundaries: inventory_path.read_text, load_json.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[9].value.args[0]::Call

Source: `infra/agentinfra/coverage.py:23`; AST `765d73c7cb9abbd165f3e9f223dd12f9b59de684b4a07ea66d37687deaf2ada7`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory_path. Outputs/bindings: (none).
Calls/effect boundaries: inventory_path.read_text.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[9].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[10]::Expr

Source: `infra/agentinfra/coverage.py:24`; AST `d9533a66cda87af3287e2d892c09897f5b5fc513f2a8810328cd8ab6a1104868`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, inventory, require, root, rows, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, inventory.get, require, sha256_file.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[10]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[10].value::Call

Source: `infra/agentinfra/coverage.py:24`; AST `742f6835cb42860cbc28355b5d79978dab673a6b26412c6c221b7bbf57efa48e`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, inventory, require, root, rows, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, inventory.get, require, sha256_file.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[10].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:24`; AST `5e6f6d7380bd0b0efdce5548fa669cb21f66d979e71f11f1e91e682c00624ed3`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory. Outputs/bindings: (none).
Calls/effect boundaries: inventory.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[10].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[10].value.args[0].values[1].left::Call

Source: `infra/agentinfra/coverage.py:25`; AST `88deaf34c240e00c2811eef57e3c11a5176cdeef3368f3fe2ecfbc6e380b6516`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory. Outputs/bindings: (none).
Calls/effect boundaries: inventory.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[10].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[10].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/coverage.py:25`; AST `6b6e3dc1d10a45e3d081a6a2b6daf4eea359c111b5e60a1857b9f54916ae78f1`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, sha256_file.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[10].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[10].value.args[0].values[1].comparators[0].args[0]::Call

Source: `infra/agentinfra/coverage.py:25`; AST `d1dae6c09a4737c00dad32494c0bfeb0041be63af3e8a598ba29935b4727024f`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[10].value.args[0].values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[11]::Assign

Source: `infra/agentinfra/coverage.py:27`; AST `8ca279e5e2e112566f57fa977dad1b959cd316a48a05a1eb386ed8a4162a6b67`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, inventory. Outputs/bindings: c, original_cases.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[11]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[11].value::DictComp

Source: `infra/agentinfra/coverage.py:27`; AST `c1cf85226cdfeb87f1cb013dc530a19643033e050301194533c16148a0ec3560`.

Rust module: `infra::agentinfra::coverage`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: c, inventory. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered DictComp evaluation at root.body[7].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[12]::Expr

Source: `infra/agentinfra/coverage.py:28`; AST `aa063d5303e020dea9a8d3d44224d0a818505448b12cbd89fa3327f2fe476873`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index, inventory, len, original_cases, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[12]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[12].value::Call

Source: `infra/agentinfra/coverage.py:28`; AST `44fa69b7bfd130ff915c6b8523282de306b0c1ed9c9331cec82584576228aa63`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: index, inventory, len, original_cases, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[12].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:28`; AST `5009b17b695b8484b116691c6b24efc4a1d8f818eb10c8da290c03300f603c03`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, original_cases. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[12].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[12].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/coverage.py:28`; AST `6126e2cf057fae7a0c2671e4e3716bd3a32bfe88b49fbfc5c7e5e686468690bf`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[12].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[12].value.args[0].values[1].left::Call

Source: `infra/agentinfra/coverage.py:28`; AST `520bd523349251d1f17f40d21b2a36d79efa1d4637cd56e8205e6702e29b0111`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original_cases, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[12].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[12].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/coverage.py:28`; AST `a6fb4d710933481a34eb34396be9972b93186ccf054fcedde0ce0750e22b580c`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: index, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[12].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[13]::Assign

Source: `infra/agentinfra/coverage.py:30`; AST `472a2592dd4ebe1a90ae2d4f66c0be2099239220097bf4fc6215a365ccec64e9`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: found.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[13]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14]::For

Source: `infra/agentinfra/coverage.py:31`; AST `f330403a03af1cfafeaa70b77ce4413ef4dc7e10b6bcfda78bd8ef7375ebde36`.

Rust module: `infra::agentinfra::coverage`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: LANES, a, all, assertion, bool, confined_path, d, declared, dependency, dict, document, found, identity, index, int, isinstance, lane, len, lines, list, original, original_cases, p, property_name, r, record, require, requirements, residual, root, rust, set, source, str, type. Outputs/bindings: a, assertion, d, declared, dependency, identity, lane, lines, original, p, r, record, requirements, residual, rust, source.
Calls/effect boundaries: all, assertion.get, assertion['rule'].strip, bool, confined_path, dependency.get, dependency['relation'].strip, isinstance, len, property_name, r['relation'].strip, record.get, record['execution_review'].strip, record['reference_review'].strip, record['required_obligations'].values, require, rust.get, set, source.read_text, source.read_text().splitlines, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered For evaluation at root.body[7].body[14]; no call, error or mutation may be omitted. Iteration: record in document['cases']
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[0]::Assign

Source: `infra/agentinfra/coverage.py:32`; AST `2523605e4d769049892fa0d54a06a39ccbd32142782c2375a53c19250f623274`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: identity.
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[0].value::Call

Source: `infra/agentinfra/coverage.py:32`; AST `28567771d249b5724c790ba932816f34017d8632795bc389bf0731cac4e7e5aa`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[1]::Expr

Source: `infra/agentinfra/coverage.py:33`; AST `dbd141c8e3dbfe69c3438afb47498c7b9db58e54350940856ffca76f00bd23c2`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: found, identity, index, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[1].value::Call

Source: `infra/agentinfra/coverage.py:33`; AST `bb0ca9831f790d6e4fa78b49179b57d85400c8b27cdef4181af498e00142e37b`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: found, identity, index, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[2]::Expr

Source: `infra/agentinfra/coverage.py:34`; AST `3718cdedc5b59784661900e17748982cd882e951ea1cdf3bbe7f465f6f4427db`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identity, index, record, require. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[2].value::Call

Source: `infra/agentinfra/coverage.py:34`; AST `3506e003f52b356cd857d62684d69d2f5b93edbe5b05a3a3501f86e5050db11a`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity, index, record, require. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[2].value.args[0].left::Call

Source: `infra/agentinfra/coverage.py:34`; AST `abbb54c8fcbdbe870a796907eb62a56738e08417b48087273c33317dc17ee849`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[3]::Expr

Source: `infra/agentinfra/coverage.py:35`; AST `2f6a1ff2a0cc93dbeeb58b3caa41739abf5443573c1f00be8a1884e591e4550a`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, require. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[3].value::Call

Source: `infra/agentinfra/coverage.py:35`; AST `6b7ddfb32e27853b9b5dbf39f795cbcd6609a7c583a4d22a84bb02a84ca8e955`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, require. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[3].value.args[0].left::Call

Source: `infra/agentinfra/coverage.py:35`; AST `817ddc2032f92ca05ecb174fe8b2f469383ee3a7c1d1098bc52dc2cbd9a4a5f5`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[4]::Assign

Source: `infra/agentinfra/coverage.py:37`; AST `e80a7cbd532fc89beca5f45f1c5cfde0015d210952d63ae54e676a0dbe12e941`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identity, original_cases. Outputs/bindings: original.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[5]::Expr

Source: `infra/agentinfra/coverage.py:38`; AST `2d9c870bb7397ac066c0be43fa06c8baf55bcfe424bf10554a3e768138dd67ba`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original, record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[5].value::Call

Source: `infra/agentinfra/coverage.py:38`; AST `e91bb3cbd22d61fa02fd0925dce10a1364e928f7feaee237729f550c40626a12`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original, record, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6]::If

Source: `infra/agentinfra/coverage.py:39`; AST `99c2134505b59c717f117b64a2edd29612a5ecd96b02758d65b9a7a42e85e82f`.

Rust module: `infra::agentinfra::coverage`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, assertion, bool, confined_path, d, dependency, int, isinstance, len, lines, list, original, property_name, record, require, root, rust, set, source, str, type. Outputs/bindings: a, assertion, d, dependency, lines, rust, source.
Calls/effect boundaries: assertion.get, assertion['rule'].strip, bool, confined_path, dependency.get, dependency['relation'].strip, isinstance, len, property_name, record.get, record['execution_review'].strip, record['reference_review'].strip, require, rust.get, set, source.read_text, source.read_text().splitlines, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered If evaluation at root.body[7].body[14].body[6]; no call, error or mutation may be omitted. Condition: record.get('rust_translation_reviewed') is True
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].test.left::Call

Source: `infra/agentinfra/coverage.py:39`; AST `2847f34976d64e25b134aba4d73d07f6f89018112beca16c645352b53073488c`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].test.left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[0]::Expr

Source: `infra/agentinfra/coverage.py:40`; AST `a578b75e9b72fa71f80307977cefda59b499624993c40e410e5b57ed6870c894`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[0].value::Call

Source: `infra/agentinfra/coverage.py:40`; AST `72119969b6aef44d16ce33b09523783924eca811fcd34d71b2188c4889dcdc13`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[1]::Expr

Source: `infra/agentinfra/coverage.py:41`; AST `74e78049662a3ed3457287b29b1c1cc3ae4d67750f21d7a7343ffd2cb74941ae`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, len, list, original, record, require, set, type. Outputs/bindings: a.
Calls/effect boundaries: len, record.get, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[1].value::Call

Source: `infra/agentinfra/coverage.py:41`; AST `1159d62d64d69111b8c198a2c183e0c38d93dbc307b8aa033a0ad29db3e8b64e`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, len, list, original, record, require, set, type. Outputs/bindings: a.
Calls/effect boundaries: len, record.get, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:41`; AST `bee1994d1e0d8c39be0ef17d5b9daa5ff26b6ffaed47ad742cdc6e330343bbd0`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[1].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/coverage.py:41`; AST `2755517f7d0c9cf5e394ac4b218d4def790d76977109964fca2479ab61e1885f`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[1].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/coverage.py:42`; AST `26a5605edef7e21255950806dbb3d06e2282e3f416f6ee5661a4ef170193d55c`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[1].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/coverage.py:42`; AST `17d0f8cd708e01d994d2cabf96a442b7b1db161e604fdcf133a6720b92b41c36`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, len, record. Outputs/bindings: a.
Calls/effect boundaries: len.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[1].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[1].value.args[0].values[1].comparators[0].args[0]::SetComp

Source: `infra/agentinfra/coverage.py:42`; AST `3e661d5372fd9224bbb0fa9beef2ae1b027c3b58c9a5124ac3822744b3dc9c1d`.

Rust module: `infra::agentinfra::coverage`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: a, record. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered SetComp evaluation at root.body[7].body[14].body[6].body[1].value.args[0].values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[1].value.args[0].values[2].left::SetComp

Source: `infra/agentinfra/coverage.py:43`; AST `3e661d5372fd9224bbb0fa9beef2ae1b027c3b58c9a5124ac3822744b3dc9c1d`.

Rust module: `infra::agentinfra::coverage`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: a, record. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered SetComp evaluation at root.body[7].body[14].body[6].body[1].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[1].value.args[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/coverage.py:43`; AST `502c367d3bb0c7b517ea5d43aebb9fcfe7207187c77829f10c3f65bd7e497546`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[1].value.args[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[2]::Expr

Source: `infra/agentinfra/coverage.py:45`; AST `64b675a01ef7e28000a286ae11aaa66b92269ea54787c293058f2433f34dc034`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: d, len, list, original, record, require, set, type. Outputs/bindings: d.
Calls/effect boundaries: len, record.get, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[2].value::Call

Source: `infra/agentinfra/coverage.py:45`; AST `6df82b8beb41a9ccd49364aeb8e4ced89128b7e14897d5a122f130eb69f153b4`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: d, len, list, original, record, require, set, type. Outputs/bindings: d.
Calls/effect boundaries: len, record.get, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:45`; AST `ae34e6f9fa4cfbceb8849a9b84112fbc7b61b277c7d10b66c20289646ec31b08`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[2].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/coverage.py:45`; AST `7d4b3f291e00ae7af1886661a7d1e51392007d0f26752d6fe6c8d321a7b0f6ed`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[2].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[2].value.args[0].values[1].left::SetComp

Source: `infra/agentinfra/coverage.py:46`; AST `39e0c4f9ee02ed7bf633b845a6650b99067a1573d524c671cfc7d454c3ab62b6`.

Rust module: `infra::agentinfra::coverage`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: d, record. Outputs/bindings: d.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered SetComp evaluation at root.body[7].body[14].body[6].body[2].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[2].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/coverage.py:46`; AST `612e14c786dbedbf2928f258a009cf6c70ef3773b9c175919ffcba45e2ea484d`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[2].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[2].value.args[0].values[2].left::Call

Source: `infra/agentinfra/coverage.py:47`; AST `c144c5adc275e8b8b09d1e71159fec432afce0dc8b331f6b3d7705f152f37fdd`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[2].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[2].value.args[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/coverage.py:47`; AST `83d9c69e9d0d598819316bdfd5d75b441078bd903249022aa2aa5ffdb648160a`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, original. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[2].value.args[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[3]::Expr

Source: `infra/agentinfra/coverage.py:49`; AST `ca3d4e93387bfe153cdd11040045836a19fdfdc28dbbb71324c4665e5d2acff6`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, isinstance, record, require, str. Outputs/bindings: (none).
Calls/effect boundaries: bool, isinstance, record.get, record['execution_review'].strip, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[3].value::Call

Source: `infra/agentinfra/coverage.py:49`; AST `1308db4ff3dce5d102a2c170a1638a65471528a159facc5111b8fe28c0cd0300`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, isinstance, record, require, str. Outputs/bindings: (none).
Calls/effect boundaries: bool, isinstance, record.get, record['execution_review'].strip, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[3].value.args[0].values[0]::Call

Source: `infra/agentinfra/coverage.py:49`; AST `506cee82ae4600ecb12a01da23c91794a86607e34f39e1b14f08c4eb6214ba8a`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, record, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[3].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[3].value.args[0].values[0].args[0]::Call

Source: `infra/agentinfra/coverage.py:49`; AST `35def1d80c35ab7438b83615a49d61bea261ee7a35b15ea731bcb9a5693f0273`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[3].value.args[0].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[3].value.args[0].values[1]::Call

Source: `infra/agentinfra/coverage.py:49`; AST `3af002bb2276608571124d3f6a88ae051c6b166ea50f2c33ea470102501dc53f`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, record. Outputs/bindings: (none).
Calls/effect boundaries: bool, record['execution_review'].strip.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[3].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[3].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/coverage.py:49`; AST `d2536b956ec6b2e3a256306433c7483ff6c5cb2e756b3ec36223111cf90cde04`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record['execution_review'].strip.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[3].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[4]::Expr

Source: `infra/agentinfra/coverage.py:51`; AST `acfca44d0c5ac6e6d0646578f8d0207a1600bf976b120b12fa772680fd2ef0a6`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, isinstance, record, require, str. Outputs/bindings: (none).
Calls/effect boundaries: bool, isinstance, record.get, record['reference_review'].strip, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[4].value::Call

Source: `infra/agentinfra/coverage.py:51`; AST `e9ed292f2ca99f9fef6d0b9d00b8662f12eb6e626a6ac2c17a0a14dde2e95eaa`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, isinstance, record, require, str. Outputs/bindings: (none).
Calls/effect boundaries: bool, isinstance, record.get, record['reference_review'].strip, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[4].value.args[0].values[0]::Call

Source: `infra/agentinfra/coverage.py:51`; AST `cdc4d7992dcc773d3804d8891bc65910ddc3df971e211d5d0ed9762586d65f21`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, record, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[4].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[4].value.args[0].values[0].args[0]::Call

Source: `infra/agentinfra/coverage.py:51`; AST `b7fe60537b7f7d0994f2a2bd07d4441a6a4c0a81c81cb1a9d2a6d744cac2c12d`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[4].value.args[0].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[4].value.args[0].values[1]::Call

Source: `infra/agentinfra/coverage.py:51`; AST `e5ae80d292b7dc1baefb411e4fe7e1b4cee9b241192f2651164999e8d261a8d8`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, record. Outputs/bindings: (none).
Calls/effect boundaries: bool, record['reference_review'].strip.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[4].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[4].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/coverage.py:51`; AST `a56bb6b0a71eff7b1b9b217fdd28b744a859a7fbf0e7bcd7872cb3a5b671147b`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record['reference_review'].strip.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[4].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5]::For

Source: `infra/agentinfra/coverage.py:53`; AST `d68f9d82c3d98fb8fa6006ee565329313edaa12717b8dbc7001b41de9dfd1fdd`.

Rust module: `infra::agentinfra::coverage`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: assertion, bool, confined_path, int, isinstance, len, lines, list, property_name, record, require, root, rust, source, str, type. Outputs/bindings: assertion, lines, rust, source.
Calls/effect boundaries: assertion.get, assertion['rule'].strip, bool, confined_path, isinstance, len, property_name, require, rust.get, source.read_text, source.read_text().splitlines, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered For evaluation at root.body[7].body[14].body[6].body[5]; no call, error or mutation may be omitted. Iteration: assertion in record['assertions']
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[0]::Expr

Source: `infra/agentinfra/coverage.py:54`; AST `43832baab8e5b6c291b728be4100a78f418ec0532619aa2eda2b0f8357eaea00`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertion, bool, isinstance, require, str. Outputs/bindings: (none).
Calls/effect boundaries: assertion.get, assertion['rule'].strip, bool, isinstance, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[0].value::Call

Source: `infra/agentinfra/coverage.py:54`; AST `9650e36f6217b61ca04e298c00e7c26ad3f7084997ef45c0302e741e863359ef`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion, bool, isinstance, require, str. Outputs/bindings: (none).
Calls/effect boundaries: assertion.get, assertion['rule'].strip, bool, isinstance, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/coverage.py:54`; AST `50ab5fec7abf97fd2a17c7c51a14b517857308325afc7c8c1b37b5ffd3869473`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: assertion.get, isinstance.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[0].value.args[0].values[0].args[0]::Call

Source: `infra/agentinfra/coverage.py:54`; AST `94028e9444edd05d547f5d9b4cf880bf15e1111cb98527997539b98dda02b088`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion. Outputs/bindings: (none).
Calls/effect boundaries: assertion.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[0].value.args[0].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/coverage.py:54`; AST `e07429f5bb5484e57893422390d7e1b6a134a2dee8e7f0ce9b24eebdabca5d9a`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion, bool. Outputs/bindings: (none).
Calls/effect boundaries: assertion['rule'].strip, bool.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[0].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/coverage.py:54`; AST `88a8815ef098a82de9eaa5bb3f7d3a76c51c69889768e8dd2a03629b1df1fda1`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion. Outputs/bindings: (none).
Calls/effect boundaries: assertion['rule'].strip.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[0].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[1]::Expr

Source: `infra/agentinfra/coverage.py:55`; AST `b012113815692b040c00c2ad6cc946b14d964c23ae637a2d5774293f29c01982`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assertion, list, require, type. Outputs/bindings: (none).
Calls/effect boundaries: assertion.get, require, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[1].value::Call

Source: `infra/agentinfra/coverage.py:55`; AST `b623267ed9af09067a7e73e3981a8a43d2be3acb35ad0df01dc3b98b9d8ff0c2`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion, list, require, type. Outputs/bindings: (none).
Calls/effect boundaries: assertion.get, require, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:55`; AST `6c0d980a5d25c8077c1d5b377e28fd10a56a4dc94d47942f80a4a8e305d139ba`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion, type. Outputs/bindings: (none).
Calls/effect boundaries: assertion.get, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[1].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/coverage.py:55`; AST `c8070de5cd38a4e40ed47b1331686de703f3abcc4e001b6d1c472c48da6c329d`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion. Outputs/bindings: (none).
Calls/effect boundaries: assertion.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[1].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2]::For

Source: `infra/agentinfra/coverage.py:56`; AST `be37e67d50a0938f223c69a245ecf767a152732e4de0ec778f1e115cc10e9180`.

Rust module: `infra::agentinfra::coverage`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: assertion, confined_path, int, isinstance, len, lines, property_name, require, root, rust, source, str, type. Outputs/bindings: lines, rust, source.
Calls/effect boundaries: confined_path, isinstance, len, property_name, require, rust.get, source.read_text, source.read_text().splitlines, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered For evaluation at root.body[7].body[14].body[6].body[5].body[2]; no call, error or mutation may be omitted. Iteration: rust in assertion['rust_assertions']
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[0]::Assign

Source: `infra/agentinfra/coverage.py:57`; AST `4574b212c6f03377965d20cb1338c9f0c45394269420594113207de6c473b4c0`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, root, rust. Outputs/bindings: source.
Calls/effect boundaries: confined_path.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[14].body[6].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[0].value::Call

Source: `infra/agentinfra/coverage.py:57`; AST `4103114217c3fae0274ca46678f77f9263b03932193d385b5c54ecc2d543ccb1`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, rust. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[1]::Assign

Source: `infra/agentinfra/coverage.py:58`; AST `0ad9164db0597c1d08c45f917734c0498d26339d7103e9b38a54bc2aa7572000`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: source. Outputs/bindings: lines.
Calls/effect boundaries: source.read_text, source.read_text().splitlines.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[14].body[6].body[5].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[1].value::Call

Source: `infra/agentinfra/coverage.py:58`; AST `b45fc3d58380a6263a4cf8dc25f4a7d6f2db8a7c7124323b1a21f671cb6037ed`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.read_text, source.read_text().splitlines.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[1].value.func.value::Call

Source: `infra/agentinfra/coverage.py:58`; AST `6c1e5441d9f3a8009a1291ac3a347c9696b9950e44674d6a3088f82b392bb8dc`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.read_text.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[2]::Expr

Source: `infra/agentinfra/coverage.py:59`; AST `b8587211e78ed9285902cd6584dec9ee91ef1c4d1a0ed301a8a7042baa796407`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, len, lines, require, rust, type. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[5].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[2].value::Call

Source: `infra/agentinfra/coverage.py:59`; AST `2cdc56ae83078cc8b5accec6ae97abe6c951347c823f8a071173ee8c2301b0b2`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, len, lines, require, rust, type. Outputs/bindings: (none).
Calls/effect boundaries: len, require, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:59`; AST `bdbdb72684db48d443c1062dd1df50a20a22433b50a2b4590597941f8f6070b2`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: rust, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[2].value.args[0].values[1].comparators[1]::Call

Source: `infra/agentinfra/coverage.py:59`; AST `07afbb7a385f382c1b40fcda6b6f7e9c91706969b1e8ab06f90f28b01f56b98a`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, lines. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[2].value.args[0].values[1].comparators[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[3]::Expr

Source: `infra/agentinfra/coverage.py:61`; AST `1f0820863fa89780b1f555d19e33ddcaa57cfda0f1f4e9c7b29f84ef43809aaf`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isinstance, property_name, require, rust, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, property_name, require, rust.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[5].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[3].value::Call

Source: `infra/agentinfra/coverage.py:61`; AST `84e1d837c4ad8726506449b40248b75a55d3f77e48f85cc66ab22e17a684d32f`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, property_name, require, rust, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, property_name, require, rust.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[0]::Call

Source: `infra/agentinfra/coverage.py:61`; AST `1943f7092cc7fe3da93fe91ab8481b2871d30038350ddf22a9fc49f78a81e096`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, rust, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, rust.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[0].args[0]::Call

Source: `infra/agentinfra/coverage.py:61`; AST `562301baaf5dc5ee747368ace3c81824efe1bf3b1918b0c0f33ea2f452537bba`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: rust. Outputs/bindings: (none).
Calls/effect boundaries: rust.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[1]::Call

Source: `infra/agentinfra/coverage.py:61`; AST `253d496e59a1fda271cffb032797e4cf58b78dbdbfa10115bfd11110a429d398`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, rust, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, rust.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/coverage.py:61`; AST `6f5479dd41d2cb6c45589624ed928073f441937c8bac76ac33e8aaf596250145`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: rust. Outputs/bindings: (none).
Calls/effect boundaries: rust.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[2]::Call

Source: `infra/agentinfra/coverage.py:62`; AST `91b412e125a97553e8f2c8a567d938bc6d586c70b0f7cfd9d2c75f5b7d21493c`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, rust, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, rust.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[2].args[0]::Call

Source: `infra/agentinfra/coverage.py:62`; AST `e558337e3ca4a5e47ec0506bc69669babf828e81b2b45a2cecbdb1729ef2141f`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: rust. Outputs/bindings: (none).
Calls/effect boundaries: rust.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[3]::Call

Source: `infra/agentinfra/coverage.py:63`; AST `5ca0f43e15a4a06e3092eb24d820f873432ab67754daf1a812c45991327714b8`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: property_name, rust. Outputs/bindings: (none).
Calls/effect boundaries: property_name.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[5].body[2].body[3].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[6]::For

Source: `infra/agentinfra/coverage.py:65`; AST `fc732d459ab269ddce7d25f75792f3b720f5ed6b96f2fe39ccfde7295ac5a3a2`.

Rust module: `infra::agentinfra::coverage`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: bool, dependency, isinstance, record, require, str. Outputs/bindings: dependency.
Calls/effect boundaries: bool, dependency.get, dependency['relation'].strip, isinstance, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered For evaluation at root.body[7].body[14].body[6].body[6]; no call, error or mutation may be omitted. Iteration: dependency in record['dependency_mappings']
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[6].body[0]::Expr

Source: `infra/agentinfra/coverage.py:66`; AST `58c8054febfcc27465fcc3bc17f23efb2d29c664b63e05404df3fe6218c3c872`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, dependency, isinstance, require, str. Outputs/bindings: (none).
Calls/effect boundaries: bool, dependency.get, dependency['relation'].strip, isinstance, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[6].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[6].body[0].value::Call

Source: `infra/agentinfra/coverage.py:66`; AST `59cbd73dc72da655dd1ea4408da85242799bf8e5084d56f5b601536cc4bdf5c4`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, dependency, isinstance, require, str. Outputs/bindings: (none).
Calls/effect boundaries: bool, dependency.get, dependency['relation'].strip, isinstance, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[6].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/coverage.py:66`; AST `b97c752c3d23fd60540930bbcf96cc59e59fa7ce508f3d35f9c20c2c575d5e63`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: dependency.get, isinstance.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[6].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[6].body[0].value.args[0].values[0].args[0]::Call

Source: `infra/agentinfra/coverage.py:66`; AST `d4d157935edc3765a05b0f1ea7a25060c297d0fb73221d1a810c08decf9997cf`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependency.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[6].body[0].value.args[0].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[6].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/coverage.py:66`; AST `f55a9bd7c2da403f2d17412eeb6111f714f61a8a8c12e6e3c9c8964ed2c384c7`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, dependency. Outputs/bindings: (none).
Calls/effect boundaries: bool, dependency['relation'].strip.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[6].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[6].body[6].body[0].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/coverage.py:66`; AST `791737e22e320fd9213a9f448dae6788664b73d7d827aa5991317ef04cadb185`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependency['relation'].strip.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[6].body[6].body[0].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[7]::Expr

Source: `infra/agentinfra/coverage.py:67`; AST `682ead144e3398b04e776a6f9f09baca45e0708faeab886cf41655aab7c2cefd`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LANES, dict, record, require, set, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[7].value::Call

Source: `infra/agentinfra/coverage.py:67`; AST `b56b244e37a032ae94754454fd4c2c9c5a5555901919c66caa8757d42b6b6db3`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LANES, dict, record, require, set, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[7].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:67`; AST `a3da54027950a1a6bc208f2747818552a76094b06bd9e51295729d8c3c9732f5`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[7].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[7].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/coverage.py:67`; AST `401a520b88a437c6692c302e289438a6acaf3e2580f26e0a04093b44db9b1444`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[7].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[7].value.args[0].values[1].left::Call

Source: `infra/agentinfra/coverage.py:67`; AST `b94f4caf33be6976a166032ffb620c427b3b1053b5531ef145ca6e118c040eed`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[7].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[7].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/coverage.py:67`; AST `3172f8e77809f58cbe9f174d8af8daf5748046ff76ac67d4d12638f7130b9add`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LANES, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[7].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8]::For

Source: `infra/agentinfra/coverage.py:69`; AST `3a9723264045c8889395feddfae11ed0d9aa65ce33584a4f21ccec908d294845`.

Rust module: `infra::agentinfra::coverage`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: LANES, all, dict, isinstance, lane, len, list, p, property_name, r, record, require, requirements, set, str, type. Outputs/bindings: lane, p, r, requirements.
Calls/effect boundaries: all, isinstance, len, property_name, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered For evaluation at root.body[7].body[14].body[8]; no call, error or mutation may be omitted. Iteration: lane in LANES
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[0]::Assign

Source: `infra/agentinfra/coverage.py:70`; AST `b94f27249426aa26b2a6e9a6d7423ad6eb1401f28e103031483b9fee5b92f719`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lane, record. Outputs/bindings: requirements.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[14].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1]::Expr

Source: `infra/agentinfra/coverage.py:71`; AST `1191e034c573b2fd86c296d7f9f0af5cf70f0096e376adc8e437d86b02b4ad2e`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, dict, isinstance, list, p, property_name, r, require, requirements, set, str, type. Outputs/bindings: p, r.
Calls/effect boundaries: all, isinstance, property_name, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value::Call

Source: `infra/agentinfra/coverage.py:71`; AST `950f99efb6e1fdbddc3ab5ca11cc48a5ac08e34cdc885a04e2f0e524d9cf4be5`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, dict, isinstance, list, p, property_name, r, require, requirements, set, str, type. Outputs/bindings: p, r.
Calls/effect boundaries: all, isinstance, property_name, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:71`; AST `e3e64147eac9e19fcd1ed16b8579138422182dc0f573912f8d8171c407368edb`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: requirements, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1]::Call

Source: `infra/agentinfra/coverage.py:71`; AST `9c800b0bb50d6aba00c149bb2dc2af2229f87db1ed5a584cb7cd75464a6c99ea`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, dict, isinstance, list, p, property_name, r, requirements, set, str, type. Outputs/bindings: p, r.
Calls/effect boundaries: all, isinstance, property_name, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/coverage.py:71`; AST `9bdcddaa350f246f75ee0f261b277b21d0396bc8f44806adde65fcbfcbb9f663`.

Rust module: `infra::agentinfra::coverage`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: all, dict, isinstance, list, p, property_name, r, requirements, set, str, type. Outputs/bindings: p, r.
Calls/effect boundaries: all, isinstance, property_name, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[0].left::Call

Source: `infra/agentinfra/coverage.py:72`; AST `cdeb224e42d837c9c38268bd923f897130d790b564e7c75c4123dd06ccfe64eb`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[1].left::Call

Source: `infra/agentinfra/coverage.py:72`; AST `461abfbc1b5e31c7525f751d19b6007da7988df985251d12dd6d55416dce506c`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[2]::Call

Source: `infra/agentinfra/coverage.py:73`; AST `d998972fc3543f6ff400afce2bae1da4e9e8eb7ce3c284654b9d09b85f1288b4`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, r, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[3]::Call

Source: `infra/agentinfra/coverage.py:73`; AST `e391f58129d78574f6fd1eb52f7fee79287bb848145a02688bd43e707b39f30d`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, r, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[4].left::Call

Source: `infra/agentinfra/coverage.py:74`; AST `4028c54b9cb78c0a977164f8c30b0ab72aa82e6bc12339c481101e6ed1e77ae5`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[4].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[6]::Call

Source: `infra/agentinfra/coverage.py:75`; AST `f1c3d63ae98e9c97eab5a6f9122ae31362a1236a820faafc8796bfcbf576a690`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, p, property_name, r. Outputs/bindings: p.
Calls/effect boundaries: all, property_name.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[6]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[6].args[0]::GeneratorExp

Source: `infra/agentinfra/coverage.py:75`; AST `1111c3ec6c96063e404e1391be749a3255dad6c7f0fd2f239fdd199a62be9fb8`.

Rust module: `infra::agentinfra::coverage`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: p, property_name, r. Outputs/bindings: p.
Calls/effect boundaries: property_name.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[6].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[6].args[0].elt::Call

Source: `infra/agentinfra/coverage.py:75`; AST `c112d2f59cd487bae8118938514e330cde7bafd377f7b78537261a73b88b1ade`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, property_name. Outputs/bindings: (none).
Calls/effect boundaries: property_name.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[1].value.args[0].values[1].args[0].elt.values[6].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[2]::Expr

Source: `infra/agentinfra/coverage.py:77`; AST `d1f659072cdb59169f6a3fbc24b19c0610cb80bd9d1b8f852b026c9196ec3122`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, r, require, requirements. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[2].value::Call

Source: `infra/agentinfra/coverage.py:77`; AST `650584d86058c5141e1323f16e370a8559e153b593f260ad3994251b5722cee2`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, r, require, requirements. Outputs/bindings: r.
Calls/effect boundaries: len, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[2].value.args[0].left::Call

Source: `infra/agentinfra/coverage.py:77`; AST `b439bc46998c1bdb1c86a8832bcfefc2a98550a90b17c5467baa9bef678067f4`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, requirements. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[2].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/coverage.py:77`; AST `9048f7d11bdada9befc1caa705fd92320f47fc23a2c58cfa3d896da7985b10b3`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, r, requirements. Outputs/bindings: r.
Calls/effect boundaries: len.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[8].body[2].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[8].body[2].value.args[0].comparators[0].args[0]::SetComp

Source: `infra/agentinfra/coverage.py:77`; AST `8d2511137e4ab2fec0ab23d6758a1555da7cfcc03c7f5a98a0cd6c7e0b717053`.

Rust module: `infra::agentinfra::coverage`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: r, requirements. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered SetComp evaluation at root.body[7].body[14].body[8].body[2].value.args[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[9]::If

Source: `infra/agentinfra/coverage.py:78`; AST `0a262278d0cc616259dad93d28581653f2f9e0bf424f4ac22ed99c757b029121`.

Rust module: `infra::agentinfra::coverage`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, all, declared, p, r, record, require, requirements. Outputs/bindings: a, declared, p, r, requirements.
Calls/effect boundaries: all, record.get, record['required_obligations'].values, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered If evaluation at root.body[7].body[14].body[9]; no call, error or mutation may be omitted. Condition: record.get('rust_translation_reviewed') is True
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[9].test.left::Call

Source: `infra/agentinfra/coverage.py:78`; AST `2847f34976d64e25b134aba4d73d07f6f89018112beca16c645352b53073488c`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[9].test.left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[9].body[0]::Assign

Source: `infra/agentinfra/coverage.py:79`; AST `bb6d9b454f198834424816ae14c3b06bd7f3e4338989244709f3e6e9bb82dd46`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p, r, record, requirements. Outputs/bindings: declared, p, r, requirements.
Calls/effect boundaries: record['required_obligations'].values.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[14].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[9].body[0].value::SetComp

Source: `infra/agentinfra/coverage.py:79`; AST `b1a965d1fad337212d5ebfa5de58285e726f6ee5dc781e4dccee3fe9554badf6`.

Rust module: `infra::agentinfra::coverage`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: p, r, record, requirements. Outputs/bindings: p, r, requirements.
Calls/effect boundaries: record['required_obligations'].values.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered SetComp evaluation at root.body[7].body[14].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[9].body[0].value.generators[0].iter::Call

Source: `infra/agentinfra/coverage.py:79`; AST `ea929b8d49da1093138dbac19e60a81e892830161cf9c3b3333d9a2854b8f4a0`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record['required_obligations'].values.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[9].body[0].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[9].body[1]::Expr

Source: `infra/agentinfra/coverage.py:81`; AST `5def2834b4267b65bb2a5808789c97d5159af6e4dccd64becc9fb9992e61b16a`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, all, declared, r, record, require. Outputs/bindings: a, r.
Calls/effect boundaries: all, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[9].body[1].value::Call

Source: `infra/agentinfra/coverage.py:81`; AST `3c55285c3d22bdadbd0bd93291677571ae3c2498b6532356ca4b326a9fd64967`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, declared, r, record, require. Outputs/bindings: a, r.
Calls/effect boundaries: all, require.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[9].body[1].value.args[0]::Call

Source: `infra/agentinfra/coverage.py:81`; AST `65336d0b419427f1ebf04f24c3d9435d883edc1f159fdcb12d614e9e53eb26ec`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, declared, r, record. Outputs/bindings: a, r.
Calls/effect boundaries: all.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[9].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[9].body[1].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/coverage.py:81`; AST `37639a38209abc52f420018ceff78ec26a11e15f419a71acc12d4095276ede34`.

Rust module: `infra::agentinfra::coverage`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, declared, r, record. Outputs/bindings: a, r.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[7].body[14].body[9].body[1].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[10]::Assign

Source: `infra/agentinfra/coverage.py:83`; AST `144438807c8d3d752e697f9eff9b1d17fc10105ac85ac8d0b67473ca3f6363c9`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: residual.
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[14].body[10]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[10].value::Call

Source: `infra/agentinfra/coverage.py:83`; AST `ffea64d9a06d360d9f500abfabb8923adc0ecc35d2b4398c0f60793a7bce5efd`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11]::Expr

Source: `infra/agentinfra/coverage.py:84`; AST `060ca00868f776a88044a4eca2740198b8e8f45ee09600cc665bcc30cb70f20c`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LANES, all, bool, dict, isinstance, list, r, require, residual, set, str, type. Outputs/bindings: r.
Calls/effect boundaries: all, bool, isinstance, r['relation'].strip, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[14].body[11]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11].value::Call

Source: `infra/agentinfra/coverage.py:84`; AST `d1f2fb4caebf34ff2c75dec07153a0148a02ad5d505525bd83633b9c0a98b464`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LANES, all, bool, dict, isinstance, list, r, require, residual, set, str, type. Outputs/bindings: r.
Calls/effect boundaries: all, bool, isinstance, r['relation'].strip, require, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11].value.args[0].values[0].left::Call

Source: `infra/agentinfra/coverage.py:84`; AST `2b1db6b1049306c5b60f469e07af0710e383370875ee201e74abedc1479b74bf`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: residual, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[11].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11].value.args[0].values[1]::Call

Source: `infra/agentinfra/coverage.py:84`; AST `b15cf3c7b0a3560513a9366ee0d090dbfeb23fe5bb4822459059930170c8b069`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LANES, all, bool, dict, isinstance, r, residual, set, str, type. Outputs/bindings: r.
Calls/effect boundaries: all, bool, isinstance, r['relation'].strip, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[11].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11].value.args[0].values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/coverage.py:84`; AST `a6953286f9760ecd1c0f0f387ebee103a798f8512a16171f533fd9bd7b7ce0ac`.

Rust module: `infra::agentinfra::coverage`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: LANES, bool, dict, isinstance, r, residual, set, str, type. Outputs/bindings: r.
Calls/effect boundaries: bool, isinstance, r['relation'].strip, set, type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[7].body[14].body[11].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[0].left::Call

Source: `infra/agentinfra/coverage.py:84`; AST `cdeb224e42d837c9c38268bd923f897130d790b564e7c75c4123dd06ccfe64eb`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[1].left::Call

Source: `infra/agentinfra/coverage.py:84`; AST `461abfbc1b5e31c7525f751d19b6007da7988df985251d12dd6d55416dce506c`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[3]::Call

Source: `infra/agentinfra/coverage.py:85`; AST `b7ef2e5a67301b9e72cec6b55b219aab9fd43e08b06476a9ae6c9a571df08cef`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, r, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[4]::Call

Source: `infra/agentinfra/coverage.py:85`; AST `3831d948dfd452cf47e1977b49032e3c642d868667794530b096fdb039853d2f`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, r. Outputs/bindings: (none).
Calls/effect boundaries: bool, r['relation'].strip.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[4]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[4].args[0]::Call

Source: `infra/agentinfra/coverage.py:85`; AST `5b971d52582e869a9f5dcf71d1228754f96b5e35318d401f2d196251ec0f5627`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r['relation'].strip.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[7].body[14].body[11].value.args[0].values[1].args[0].elt.values[4].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[14].body[12]::Assign

Source: `infra/agentinfra/coverage.py:87`; AST `db08dfb5f482dc5c1c4e61e92b02560b7085c3c88f6194cd8b45f4433324c379`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: found, identity, record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[14].body[12]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::mappings::root.body[7].body[15]::Return

Source: `infra/agentinfra/coverage.py:88`; AST `fe941c9ac15d564629ac31572e64dfe1ba8d1c0e98af5cb5e6dbf3ee4f82cf76`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: found. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Return evaluation at root.body[7].body[15]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8]::FunctionDef

Source: `infra/agentinfra/coverage.py:91`; AST `c7e46f595467badf7a7f377b9a2eef097483931e93596d433971f26d90a3766f`.

Rust module: `infra::agentinfra::coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: LANES, a, all, any, assertion, bool, lane, levels, p, proofs, r, record, requirements, residual, reviewed, set. Outputs/bindings: a, assertion, lane, levels, p, r, requirements, residual, reviewed.
Calls/effect boundaries: all, any, assertion.get, bool, p.get, p.get('assertion_locations', {}).get, record.get, set, set(r['assertion_properties']).issubset.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[0]::If

Source: `infra/agentinfra/coverage.py:92`; AST `dfbf78d06b44100bcd0a90a102279b22ae51cfef358e40b6c23e5e7190b64c8c`.

Rust module: `infra::agentinfra::coverage`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LANES, lane, record. Outputs/bindings: lane.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered If evaluation at root.body[8].body[0]; no call, error or mutation may be omitted. Condition: record is None
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[0].body[0]::Return

Source: `infra/agentinfra/coverage.py:93`; AST `95f32469644445978bf37e797c2e1c71baab2ff949c0e90bc39b97204e93a14c`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LANES, lane. Outputs/bindings: lane.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Return evaluation at root.body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[0].body[0].value::DictComp

Source: `infra/agentinfra/coverage.py:93`; AST `d37dd85e740edc3d8289f464c575c9ad442d8718a8c8c3583373cf7007549348`.

Rust module: `infra::agentinfra::coverage`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: LANES, lane. Outputs/bindings: lane.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered DictComp evaluation at root.body[8].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[1]::Assign

Source: `infra/agentinfra/coverage.py:94`; AST `6d797ca7fe3a68666278b9872cf06618c90871ae10600863132b4abff5d1d56d`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: levels.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2]::For

Source: `infra/agentinfra/coverage.py:95`; AST `5c3d0856cb3e96f886f485cb04c94949518e18feb544a6abb69f6db46fd8e300`.

Rust module: `infra::agentinfra::coverage`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: LANES, a, all, any, assertion, bool, lane, levels, p, proofs, r, record, requirements, residual, reviewed, set. Outputs/bindings: a, assertion, lane, p, r, requirements, residual, reviewed.
Calls/effect boundaries: all, any, assertion.get, bool, p.get, p.get('assertion_locations', {}).get, record.get, set, set(r['assertion_properties']).issubset.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered For evaluation at root.body[8].body[2]; no call, error or mutation may be omitted. Iteration: lane in LANES
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[0]::Assign

Source: `infra/agentinfra/coverage.py:96`; AST `b94f27249426aa26b2a6e9a6d7423ad6eb1401f28e103031483b9fee5b92f719`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lane, record. Outputs/bindings: requirements.
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[1]::Assign

Source: `infra/agentinfra/coverage.py:98`; AST `87b8fc6482fbafe4d6b7ea3396584eaefac97a0d8f203dd2f33e97475cc42471`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: reviewed.
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[1].value.left::Call

Source: `infra/agentinfra/coverage.py:98`; AST `2847f34976d64e25b134aba4d73d07f6f89018112beca16c645352b53073488c`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[2]::Assign

Source: `infra/agentinfra/coverage.py:99`; AST `28d115d94c65f939c800c0a8a701cb1cdc389527a7093b76644d2681a340fd06`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, lane, r, record. Outputs/bindings: r, residual.
Calls/effect boundaries: any, record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[2].value::Call

Source: `infra/agentinfra/coverage.py:99`; AST `904b55523f8eb8fbcde18a55be3afb31d7d3e13105ecfb5fa397bbca2a362726`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, lane, r, record. Outputs/bindings: r.
Calls/effect boundaries: any, record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[2].value.args[0]::GeneratorExp

Source: `infra/agentinfra/coverage.py:99`; AST `e2e2868caf72fa256851db5b7a73c2b141c6e6dab800ba0ee5ac83cdcaa36f6d`.

Rust module: `infra::agentinfra::coverage`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: lane, r, record. Outputs/bindings: r.
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[2].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[2].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/coverage.py:99`; AST `ffea64d9a06d360d9f500abfabb8923adc0ecc35d2b4398c0f60793a7bce5efd`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[2].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3]::Assign

Source: `infra/agentinfra/coverage.py:100`; AST `6ea3d464d8aeebce63f8b6d8ac3ba8ebc63eb125e6478c3a2f31f1f1a0ac7ac5`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, all, any, assertion, bool, lane, levels, p, proofs, r, record, requirements, residual, reviewed, set. Outputs/bindings: a, assertion, p, r.
Calls/effect boundaries: all, any, assertion.get, bool, p.get, p.get('assertion_locations', {}).get, record.get, set, set(r['assertion_properties']).issubset.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[2]::Call

Source: `infra/agentinfra/coverage.py:100`; AST `84bb2cf0d7e6703edda158ed7cd6e8d74ff067f745ebbff3db3ba49835e6639a`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, requirements. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3]::Call

Source: `infra/agentinfra/coverage.py:100`; AST `ff49547cb69bab7ebff1ead445e4a2dc6f729410b166902562582c9f72bf4d59`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, any, assertion, lane, p, proofs, r, record, requirements, set. Outputs/bindings: a, assertion, p, r.
Calls/effect boundaries: all, any, assertion.get, p.get, p.get('assertion_locations', {}).get, record.get, set, set(r['assertion_properties']).issubset.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0]::GeneratorExp

Source: `infra/agentinfra/coverage.py:100`; AST `a754addae9d7efde3472ec30566d581cafa77ab9b7a3a3368bd210e69c6bce50`.

Rust module: `infra::agentinfra::coverage`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, all, any, assertion, lane, p, proofs, r, record, requirements, set. Outputs/bindings: a, assertion, p, r.
Calls/effect boundaries: all, any, assertion.get, p.get, p.get('assertion_locations', {}).get, record.get, set, set(r['assertion_properties']).issubset.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[2].body[3].value.values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt::Call

Source: `infra/agentinfra/coverage.py:100`; AST `2ffc09e63eb58cbbe3afe7721bbdc843b433a32790aae32da8db5c91ce0a8c59`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, any, assertion, lane, p, proofs, r, record, set. Outputs/bindings: a, assertion, p.
Calls/effect boundaries: all, any, assertion.get, p.get, p.get('assertion_locations', {}).get, record.get, set, set(r['assertion_properties']).issubset.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0]::GeneratorExp

Source: `infra/agentinfra/coverage.py:100`; AST `05fcc06a941b56f2df71d746dfa80ea3eeaf4aaf89e181dfdb5da804702f6eab`.

Rust module: `infra::agentinfra::coverage`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, all, assertion, lane, p, proofs, r, record, set. Outputs/bindings: a, assertion, p.
Calls/effect boundaries: all, assertion.get, p.get, p.get('assertion_locations', {}).get, record.get, set, set(r['assertion_properties']).issubset.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[0].left::Call

Source: `infra/agentinfra/coverage.py:101`; AST `cf842fc63c9a2d0a7f444b1f58480c4e7e260b7de3fd40280e76128c1ace1c2c`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[1].left::Call

Source: `infra/agentinfra/coverage.py:101`; AST `272ddabf2aa8ae7305c05188402da2d1cf29183c33f0b44d999c3bb87ae0daa8`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[2].left::Call

Source: `infra/agentinfra/coverage.py:102`; AST `5568359b357f11f697a6db2027d3d4b4266164d201cc3aa32bb1190e3a0e4e81`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[2].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[3].left::Call

Source: `infra/agentinfra/coverage.py:102`; AST `1c86a34ea5522864a31a3bc1048e7c7c116744c8081eecf003c41c34746b5038`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[3].left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[4]::Call

Source: `infra/agentinfra/coverage.py:103`; AST `dcc91ddc7666b2014479e86ec3bddcee88bedd8862ad831b5325dab1e8fef195`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, r, set. Outputs/bindings: (none).
Calls/effect boundaries: p.get, set, set(r['assertion_properties']).issubset.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[4]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[4].func.value::Call

Source: `infra/agentinfra/coverage.py:103`; AST `4b8dbcc590f98d1820e91a408b416094d2f54667a9c6484514ed7c51713e894b`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[4].func.value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[4].args[0]::Call

Source: `infra/agentinfra/coverage.py:103`; AST `53e305ebd97955bfe5dc271c4ce7912bf184d34951f8c28879e15920887cbd23`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[4].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5]::Call

Source: `infra/agentinfra/coverage.py:104`; AST `05d60e68ff6c3c357db766f6af1bd8a1507d70cfd27fd4bd61eb941275d21a3d`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, all, assertion, p, r, record. Outputs/bindings: a, assertion.
Calls/effect boundaries: all, assertion.get, p.get, p.get('assertion_locations', {}).get, record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0]::GeneratorExp

Source: `infra/agentinfra/coverage.py:104`; AST `13ca7655aceb7cdf2e5eb1c35633a22a12dc0a49af0573a3405a18e85881c8be`.

Rust module: `infra::agentinfra::coverage`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, assertion, p, r, record. Outputs/bindings: a, assertion.
Calls/effect boundaries: assertion.get, p.get, p.get('assertion_locations', {}).get, record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0].elt.left::Call

Source: `infra/agentinfra/coverage.py:104`; AST `1dcacb3fcc0e17d6c9071ba3ce41d144949c4adb032e1b595d1e59077192e781`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, p. Outputs/bindings: (none).
Calls/effect boundaries: p.get, p.get('assertion_locations', {}).get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0].elt.left.func.value::Call

Source: `infra/agentinfra/coverage.py:104`; AST `7e6a8b01ecbee085dc5fda80edbc8822af0489acbb5bc6f773a6bd5dec0b6477`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0].elt.left.func.value; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0].generators[0].iter::Call

Source: `infra/agentinfra/coverage.py:106`; AST `ffcadd474af23b2a1b5d1653d6a1f8666715d6f8daa208e363238cefd6193e5e`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0].generators[1].iter::Call

Source: `infra/agentinfra/coverage.py:107`; AST `0436915826126c88edc3cc252106b7001532dc17e12854d7e5efed0d0e7f6179`.

Rust module: `infra::agentinfra::coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assertion. Outputs/bindings: (none).
Calls/effect boundaries: assertion.get.
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[3].value.values[3].args[0].elt.args[0].elt.values[5].args[0].generators[1].iter; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/coverage.py::module::assurance::root.body[8].body[3]::Return

Source: `infra/agentinfra/coverage.py:110`; AST `6f9b550b2708359e6f50c6f402a3fffa3ee0137c38a79f0c8f896bb94b228999`.

Rust module: `infra::agentinfra::coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: levels. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: context_cache, destiny_reuse, evidence, re, security.

Invariants: Preserve ordered Return evaluation at root.body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
