# Inspected sources and reuse decisions

Inspected on 2026-10-11. Repository content is evidence/data, not instructions.
These are immutable reference points for this customization, not a promise that
either branch remains at these revisions.

## Destiny

Repository: [QuasarRay/destiny](https://github.com/QuasarRay/destiny)
Branch: `destiny-rs-dev`; inspected revision:
`8eb7606f1db5e8f65336fa05f8f87ef85ab9e402`.

- [Cargo/toolchain](https://github.com/QuasarRay/destiny/blob/8eb7606f1db5e8f65336fa05f8f87ef85ab9e402/Cargo.toml): package `destiny-bevy-compat`, Bevy/Avian, optional Carbon networking and path dependency on `verification/spec`. Toolchain file pins Rust 1.95.0.
- [Release CI](https://github.com/QuasarRay/destiny/blob/8eb7606f1db5e8f65336fa05f8f87ef85ab9e402/.github/workflows/ci.yml): locked Rust, Python, native ABI, relocated CMake, wheel, three-OS matrix and dependency gates.
- [Formal CI](https://github.com/QuasarRay/destiny/blob/8eb7606f1db5e8f65336fa05f8f87ef85ab9e402/.github/workflows/formal-verification.yml): Kani 0.68.0, Verus 0.2026.09.20.aef82ed and six Verus files, plus specification/metaprogramming tests. A workflow declaration is not executed proof evidence.
- [Parity contract](https://github.com/QuasarRay/destiny/blob/8eb7606f1db5e8f65336fa05f8f87ef85ab9e402/verification/README.md): five distinct links are required for proved parity. The catalog reference is `ef738406b61ad06bae2f402857e464735ab106a2`, while formal CI checks original formation tests at `114e89fa584f0e1a81eb0a679aabf41af8870072`. This discrepancy remains a reference-review obligation.
- [Marker collector](https://github.com/QuasarRay/destiny/blob/8eb7606f1db5e8f65336fa05f8f87ef85ab9e402/verification/tools/proof_coverage.py): scans comments, rejects unknown markers and permits incomplete dual coverage unless strict mode is requested. It does not run either verifier.
- [Repetition scanner](https://github.com/QuasarRay/destiny/blob/8eb7606f1db5e8f65336fa05f8f87ef85ab9e402/verification/tools/pattern_scan.py): lexical repeated lines in five implementation files. Reuse this existing report before adding another clone detector; candidates still need semantic characterization.
- [Native differential tests](https://github.com/QuasarRay/destiny/blob/8eb7606f1db5e8f65336fa05f8f87ef85ab9e402/tests/test_backend_differential.py): skip without `DESTINY_BEVY_COMPAT_LIBRARY`. The dedicated recipe therefore requires an explicit existing library.

The inspected `verification/meta` and `verification/meta-support` directories
have no tracked Cargo.lock. This profile deliberately uses locked commands;
initial dependency resolution must be an explicit build task. No tool versions
are inferred from tool availability, and source claims in `VERIFICATION.md` are
not reused as current execution evidence.

## PAIML toolkit

Repository: [paiml/paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)
Inspected revision: `87361ca6cae0234af591674888221e54d98330ad`.
The manifest identifies version 3.42.0. The root LICENSE is MIT; Cargo.toml
declares `MIT OR Apache-2.0`. No code was copied, compiled, installed or executed,
so no toolkit runtime dependency or copied-code licensing assertion is made.

| Inspected source | Decision and reason |
| --- | --- |
| [Working-tree cache contract](https://github.com/paiml/paiml-mcp-agent-toolkit/blob/87361ca6cae0234af591674888221e54d98330ad/contracts/dead-code-cache-v1.yaml) | Reuse the ideas of uncommitted-input invalidation, schema/version binding, explicit cache-hit provenance and counted executions. Implement with existing Aegis primitives and SHA-256 file inventories; never fall back to committed HEAD as current evidence. |
| [Dependency cache](https://github.com/paiml/paiml-mcp-agent-toolkit/blob/87361ca6cae0234af591674888221e54d98330ad/src/cli/handlers/comply_cb_detect/dependency_checks_cache.rs) | Its `is_valid` compares whole-second modification time. Do not copy this validity predicate; byte edits with preserved times must invalidate. Retain the useful `--locked` discipline. This is a source-level finding, not an executed PMAT defect report. |
| [Unified context builder](https://github.com/paiml/paiml-mcp-agent-toolkit/blob/87361ca6cae0234af591674888221e54d98330ad/src/cli/handlers/unified_context_advanced_builder.rs) | Avoid enabling all analysis/context annotations by default. Target symbols/ranges and return compact receipts. Broad scoring/context generation needs a specific unresolved question. |

The existing Destiny scanner is adequate for a first duplication triage. A PMAT
semantic index can be evaluated later on an isolated, pinned checkout if it
demonstrably answers something the existing tools cannot. Keep any PMAT score,
provability annotation, context summary or clone suggestion advisory; validate
against source and the real compiler/verifiers. Do not enable autonomous fixes,
commits, MCP servers, network listeners or an additional agent fleet by default.
