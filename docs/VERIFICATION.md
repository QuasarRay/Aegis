# Verification record for the Destiny customization

Observed on 2026-10-11, against Destiny `destiny-rs-dev` at
`8eb7606f1db5e8f65336fa05f8f87ef85ab9e402`. Source inspection and controller execution
are separate from actual target proof execution.

| Check | Observed result | Scope |
| --- | --- | --- |
| `python scripts/check_formal.py --verus /opt/verus/verus` | 10 verified, 0 errors; `CHECKED_MODEL` | Controller Verus model only, with `--no-cheating` and exact count validation. |
| `python scripts/selftest.py` | 57 cases, 55 passed, 2 skipped | Operational controller regressions, including actual CLI/process/file paths; host-specific skipped cases are not passes. |
| Python parsing and TOML/JSON validation | Passed | Current source/configuration syntax. |
| Active source migration scan | No obsolete development-method mandates or dependencies found | Includes policies, code, templates and distribution surfaces; Git history is retained. |
| Pinned symbol provenance | All five verbatim symbols match their recorded SHA-256 values | Aegis branch reuse; adapted/retained primitives are identified separately. |
| `plan --changed src/runtime.rs` | 16 ordered recipes, 4 manual operational gates | Conservative selection only; does not execute the matrix. |
| `run proof-markers` | Fresh observation succeeded; second call `REUSED`, `executed: false` | Annotation inventory, not proof. |
| `run repetition` | Succeeded; output truncation explicitly reported | Existing lexical report; full-stream digest and bounded excerpt retained. |
| Scoped Kani formation invocation | `UNAVAILABLE`: cargo-kani missing | No Kani proof was executed or counted as passing. |
| Target Verus invocation | `UNAVAILABLE`: pinned version differs | Installed `0.2026.09.13.671956e`; Destiny requires `0.2026.09.20.aef82ed`. |

The marker inventory reports 509 original obligations, 109 Kani-marked, 107
Verus-marked, 107 marked in both and 400 missing both markers. These counts do
not establish proof success, proof completeness or the absence of other proof work.

Raw records: [model execution](evidence/controller-model.json),
[controller regressions](evidence/controller-regressions.txt),
[target CLI observations](evidence/target-observations.json),
[marker receipt](evidence/target-proof-markers.json), and
[repetition receipt](evidence/target-repetition.json).

The model was checked with Verus `0.2026.09.13.671956e`, Rust toolchain `1.98.1`
and Z3 `4.16.0`. Runtime executable and selected distribution identities are in the
receipt. This is distinct from Destiny's reviewed Rust 1.95.0 / Kani 0.68.0 / Verus
0.2026.09.20.aef82ed configuration. No tool download or silent version substitution
was performed for target proofs.

[The proof boundary](../verification/README.md) explicitly leaves Python-to-model
refinement, filesystem/process soundness and complete Destiny parity unproved.
The original-reference catalog/formation-CI discrepancy remains an explicit review
obligation. No native build, platform matrix, wheel install or real Carbon deployment
was claimed by this customization's local checks.
