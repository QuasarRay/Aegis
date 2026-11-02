# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 47. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/destiny_reuse.py::module::root::Module

Source: `infra/agentinfra/destiny_reuse.py:1`; AST `7dc50f23ae8f3b04d3d7932a1b8570763bacb477388ea1accda9c8e72df0d595`.

Rust module: `infra::agentinfra::destiny_reuse`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, ValueError, bytes, condition, data, harnesses, hashlib, isinstance, items, json, k, message, o, out, re, require, result, s, set, statuses, str, summaries, unique, v, value. Outputs/bindings: data, harnesses, k, out, result, statuses, summaries, v.
Calls/effect boundaries: ContractError, hashlib.sha256, hashlib.sha256(data).hexdigest, isinstance, json.dumps, json.dumps(value, sort_keys=True, separators=(',', ':')).encode, json.loads, out.count, re.findall, require, set, str.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::root.body[0]::Expr

Source: `infra/agentinfra/destiny_reuse.py:1`; AST `5e40e30cee64d1b5b84c22608d6f317d257e8e67a93df9c7976f488182ee38b4`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::root.body[1]::Import

Source: `infra/agentinfra/destiny_reuse.py:8`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::root.body[2]::Import

Source: `infra/agentinfra/destiny_reuse.py:9`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::root.body[3]::Import

Source: `infra/agentinfra/destiny_reuse.py:10`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::ContractError::root.body[4]::ClassDef

Source: `infra/agentinfra/destiny_reuse.py:13`; AST `20ae71d452c076a448e2abd03254a17e5d196bb532756531049d3642b96038f2`.

Rust module: `infra::agentinfra::destiny_reuse`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered ClassDef evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::ContractError::root.body[4].body[0]::Pass

Source: `infra/agentinfra/destiny_reuse.py:14`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Pass evaluation at root.body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::require::root.body[5]::FunctionDef

Source: `infra/agentinfra/destiny_reuse.py:17`; AST `15de08501a9cdb8a8a877465a00e9762fc00c8781aebc9267ecffa4fc5f3702e`.

Rust module: `infra::agentinfra::destiny_reuse`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, condition, message. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered FunctionDef evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::require::root.body[5].body[0]::If

Source: `infra/agentinfra/destiny_reuse.py:18`; AST `7eeeae7604dac282df7e6c5c3a98abf8a50bed3c6994b82bc3846c9f1c20c36e`.

Rust module: `infra::agentinfra::destiny_reuse`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ContractError, condition, message. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered If evaluation at root.body[5].body[0]; no call, error or mutation may be omitted. Condition: not condition
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::require::root.body[5].body[0].body[0]::Raise

Source: `infra/agentinfra/destiny_reuse.py:19`; AST `af6adc52e897a2e8a94f8a9b57898f3ff891bc1661ec52b6f5436d3300880f88`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError, message. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Raise evaluation at root.body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::require::root.body[5].body[0].body[0].exc::Call

Source: `infra/agentinfra/destiny_reuse.py:19`; AST `31cc39de2cb7708f97fb63a897e031342373423f025a4b3beea3b38042ba6887`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, message. Outputs/bindings: (none).
Calls/effect boundaries: ContractError.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::digest::root.body[6]::FunctionDef

Source: `infra/agentinfra/destiny_reuse.py:22`; AST `d7a3d4ad6406e8fbe664870fc4525bff848816c53413e410d9cb257b09585ce6`.

Rust module: `infra::agentinfra::destiny_reuse`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bytes, data, hashlib, isinstance, json, value. Outputs/bindings: data.
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest, isinstance, json.dumps, json.dumps(value, sort_keys=True, separators=(',', ':')).encode.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::digest::root.body[6].body[0]::Assign

Source: `infra/agentinfra/destiny_reuse.py:23`; AST `3c3faf374fa77a3cd64d95759a97447b064eba659d677e149d47a3b3eaf76206`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bytes, isinstance, json, value. Outputs/bindings: data.
Calls/effect boundaries: isinstance, json.dumps, json.dumps(value, sort_keys=True, separators=(',', ':')).encode.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::digest::root.body[6].body[0].value.test::Call

Source: `infra/agentinfra/destiny_reuse.py:23`; AST `952dcdc341aac4b7e1e87d815b76208592c95357e11ef0b8e2924bfc076856be`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bytes, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].value.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::digest::root.body[6].body[0].value.orelse::Call

Source: `infra/agentinfra/destiny_reuse.py:23`; AST `c76c621e2016502de3e69a8f40c6578df80d75022992ba8d439f2a13d53944aa`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, json.dumps(value, sort_keys=True, separators=(',', ':')).encode.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::digest::root.body[6].body[0].value.orelse.func.value::Call

Source: `infra/agentinfra/destiny_reuse.py:23`; AST `09abc8aa34faf81fba519d57c705122b211855fb6dea174b8f2fc306e30c1c9d`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].value.orelse.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::digest::root.body[6].body[1]::Return

Source: `infra/agentinfra/destiny_reuse.py:24`; AST `9d1d3a819632ba7b5eb6687385ba1bc6b610232a0087e7fc3e68d636a2fc5c37`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Return evaluation at root.body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::digest::root.body[6].body[1].value::Call

Source: `infra/agentinfra/destiny_reuse.py:24`; AST `ec988457fe103b959d993a11b804009071d8c43f7cb3ec64f12df05099c74d63`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(data).hexdigest.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::digest::root.body[6].body[1].value.func.value::Call

Source: `infra/agentinfra/destiny_reuse.py:24`; AST `08f31cedb8064eb17f9167928d61fe53346b78450a1fe6d6c7076f027285d627`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::root.body[7]::FunctionDef

Source: `infra/agentinfra/destiny_reuse.py:27`; AST `c40e4b53923ea88507eb205372fafd883d0adf82daa0e6f7760cd55dde724e6b`.

Rust module: `infra::agentinfra::destiny_reuse`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: data, items, json, k, require, result, s, unique, v. Outputs/bindings: k, result, v.
Calls/effect boundaries: json.loads, require.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::unique::root.body[7].body[0]::FunctionDef

Source: `infra/agentinfra/destiny_reuse.py:28`; AST `a0b9cb35ade3bc6c705d9c103c771918bda657d61e53e78ee8cc6844f642f256`.

Rust module: `infra::agentinfra::destiny_reuse`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: items, k, require, result, v. Outputs/bindings: k, result, v.
Calls/effect boundaries: require.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::unique::root.body[7].body[0].body[0]::Assign

Source: `infra/agentinfra/destiny_reuse.py:29`; AST `2c435ecac12c985901bb8025f4efe5e5ad7e200542d8b36f3e0370612550a391`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: result.
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::unique::root.body[7].body[0].body[1]::For

Source: `infra/agentinfra/destiny_reuse.py:30`; AST `199f7c2d3e983a7e7356688eb7cb58ae19fc4b5b589106bd2c27e58ce228b9cd`.

Rust module: `infra::agentinfra::destiny_reuse`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: items, k, require, result, v. Outputs/bindings: k, v.
Calls/effect boundaries: require.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered For evaluation at root.body[7].body[0].body[1]; no call, error or mutation may be omitted. Iteration: (k, v) in items
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::unique::root.body[7].body[0].body[1].body[0]::Expr

Source: `infra/agentinfra/destiny_reuse.py:31`; AST `5ccc56900738da3f05633d2201160763c5776b85e7d90acc4aa5e9d5a8b77945`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: k, require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::unique::root.body[7].body[0].body[1].body[0].value::Call

Source: `infra/agentinfra/destiny_reuse.py:31`; AST `bbd04315af966055dad7bb18da45cc01f42efc69a50af33edeb49a7341e25cf8`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: k, require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::unique::root.body[7].body[0].body[1].body[1]::Assign

Source: `infra/agentinfra/destiny_reuse.py:32`; AST `d5d9ec85aa471cdcdbe3ba7012f9c7197694b047dbc384105b7078e3554b6257`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: k, result, v. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::unique::root.body[7].body[0].body[2]::Return

Source: `infra/agentinfra/destiny_reuse.py:33`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Return evaluation at root.body[7].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::root.body[7].body[1]::Return

Source: `infra/agentinfra/destiny_reuse.py:34`; AST `ec6e8cd8ba2a244aef96f67dd5a3120d023a2b1c58845676bb615c1316c960e3`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, json, require, s, unique. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, require.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Return evaluation at root.body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::root.body[7].body[1].value::Call

Source: `infra/agentinfra/destiny_reuse.py:34`; AST `9e343f976d6cf8636ee556598f293d5ebfecb83638e977210bcd1b773d17d70b`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, json, require, s, unique. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, require.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::root.body[7].body[1].value.keywords[1].value::Lambda

Source: `infra/agentinfra/destiny_reuse.py:35`; AST `d2380c588f889a18d154b3f05680c0828a9124bf4574579f0edb3dbca1b58377`.

Rust module: `infra::agentinfra::destiny_reuse`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: require, s. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Lambda evaluation at root.body[7].body[1].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::load_json::root.body[7].body[1].value.keywords[1].value.body::Call

Source: `infra/agentinfra/destiny_reuse.py:35`; AST `4bf8314f050c59e4b7cf8ca0a81fccaa26b09662cbc106f1b6551ddc0059f027`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, s. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].value.keywords[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8]::FunctionDef

Source: `infra/agentinfra/destiny_reuse.py:38`; AST `ce3342e53ccc8bdc769487d041116a41956a02becc5061f447d0c94edf5a87b6`.

Rust module: `infra::agentinfra::destiny_reuse`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: harnesses, o, out, re, result, set, statuses, str, summaries. Outputs/bindings: harnesses, out, statuses, summaries.
Calls/effect boundaries: out.count, re.findall, set, str.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered FunctionDef evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[0]::If

Source: `infra/agentinfra/destiny_reuse.py:39`; AST `983d22751d681b03dca204b474e9ad8f22e415fcd248b2e2c063fe758b911f70`.

Rust module: `infra::agentinfra::destiny_reuse`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered If evaluation at root.body[8].body[0]; no call, error or mutation may be omitted. Condition: result.returncode or result.timed_out or result.stdout_truncated or result.stderr_truncated
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[0].body[0]::Return

Source: `infra/agentinfra/destiny_reuse.py:40`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Return evaluation at root.body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[1]::Assign

Source: `infra/agentinfra/destiny_reuse.py:41`; AST `4bdec47ef94ed43f84c0155f36b195e77438ef4c17ca187dec7292bbc8e66f6c`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: out.
Calls/effect boundaries: (none).
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[2]::If

Source: `infra/agentinfra/destiny_reuse.py:42`; AST `c38773222ffb87c82ef93337d8a5dfefbaa9133af414294797a83e5de60e0e5e`.

Rust module: `infra::agentinfra::destiny_reuse`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: harnesses, o, out, re, set, statuses. Outputs/bindings: harnesses, statuses.
Calls/effect boundaries: out.count, re.findall, set.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered If evaluation at root.body[8].body[2]; no call, error or mutation may be omitted. Condition: o['method'] == 'kani'
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[2].body[0]::Assign

Source: `infra/agentinfra/destiny_reuse.py:43`; AST `c431c85aeeb086b50aa2506acfe07d826e0751bdb7b2c1d9cebba1f3a412a7d1`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: out, re. Outputs/bindings: harnesses.
Calls/effect boundaries: re.findall.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[2].body[0].value::Call

Source: `infra/agentinfra/destiny_reuse.py:43`; AST `a4106be24320cd7a38a4d083ae57e4c515b0dc6a27b3953ce48cc832aef0394f`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: out, re. Outputs/bindings: (none).
Calls/effect boundaries: re.findall.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[2].body[1]::Assign

Source: `infra/agentinfra/destiny_reuse.py:44`; AST `c78b6da57400f94f8131fd939eff570c59cd2d92b28f64eda17110e2bef62116`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: out, re. Outputs/bindings: statuses.
Calls/effect boundaries: re.findall.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[2].body[1].value::Call

Source: `infra/agentinfra/destiny_reuse.py:44`; AST `510b9cce0c9e9742e81c98b72c7b2d4619d425e3b5de0a3c78473096627dd299`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: out, re. Outputs/bindings: (none).
Calls/effect boundaries: re.findall.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[2].body[2]::Return

Source: `infra/agentinfra/destiny_reuse.py:45`; AST `1bfc1de8572355d4ae932812361961ebc9453a8b6a32d0ce865314a38a097c71`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: harnesses, o, out, set, statuses. Outputs/bindings: (none).
Calls/effect boundaries: out.count, set.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Return evaluation at root.body[8].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[2].body[2].value.values[1].left::Call

Source: `infra/agentinfra/destiny_reuse.py:45`; AST `4dbb0c875912d7dea338edb6434df3f7851f249177ee7203d2697e999bf33918`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: out. Outputs/bindings: (none).
Calls/effect boundaries: out.count.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[2].value.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[2].body[2].value.values[3].left::Call

Source: `infra/agentinfra/destiny_reuse.py:46`; AST `7e47ec3e5d44cfdc3f8d502abf7c4e4875d54905747485a39fcba7dad5def1ed`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, statuses. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[8].body[2].body[2].value.values[3].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[3]::Assign

Source: `infra/agentinfra/destiny_reuse.py:49`; AST `9c6c7d02659a315b17a2dbf9979e41ed75d7cf862d0530e5ede73287b77fefb3`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: out, re. Outputs/bindings: summaries.
Calls/effect boundaries: re.findall.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Assign evaluation at root.body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[3].value::Call

Source: `infra/agentinfra/destiny_reuse.py:49`; AST `17d2e251e6df3eb2e4cfef8b93d6c1fd0a56c2bcbcda0f240d64301b26aaf2f9`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: out, re. Outputs/bindings: (none).
Calls/effect boundaries: re.findall.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[4]::Return

Source: `infra/agentinfra/destiny_reuse.py:50`; AST `78686362a5ef6e14ae80a977690fde80322db069960bd324c707c6024a7d9b33`.

Rust module: `infra::agentinfra::destiny_reuse`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: o, str, summaries. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Return evaluation at root.body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/destiny_reuse.py::module::checked_output::root.body[8].body[4].value.comparators[0].elts[0].elts[0]::Call

Source: `infra/agentinfra/destiny_reuse.py:50`; AST `615288f8ecaf0af05116f20e702f3eb8b051507a5dae489f5638f7052ad4d91b`.

Rust module: `infra::agentinfra::destiny_reuse`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: o, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: hashlib, json, re.

Invariants: Preserve ordered Call evaluation at root.body[8].body[4].value.comparators[0].elts[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; regex; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
