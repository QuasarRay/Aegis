# Verification record for the Destiny customization

## Final four-capability scope

Focused validation on 2026-10-11 preserved **531 catalog occurrences as 531 distinct
`source::fixture::test` identities**. Fixtures were joined to actual source at
`ef738406b61ad06bae2f402857e464735ab106a2`; the catalog's semantic inventory digest
is recorded in `contracts/destiny.json` and prevents silently dropping entries.

The generated queue for Destiny `8eb7606f1db5e8f65336fa05f8f87ef85ab9e402` contains
109 mapped/marked cases, 0 credited specification proofs, 0 credited production
refinement proofs and 0 supplied runtime differential records. All 531 consequently
remain uncovered at production-refinement assurance. These are available-evidence
counts, not a claim that the project has no proof work elsewhere.

Seventeen focused checks passed in 2.290 seconds. They covered fixture extraction and
duplicate preservation, exact Kani version/harness/property parsing, vacuity, assurance
separation, production witness location, harness digest changes, rejection of cached
results and skipped runtime scenarios, plus the existing stale-tool/source, verifier
count/version and durable retry boundaries. Synthetic verifier output in those checks
is explicitly a controller fixture and is never credited as a Destiny theorem.

Real source extraction produced a 6,471-byte Python formation packet including eight
original/setup/helper snippets, and a 3,884-byte C++ packet containing the selected
`RectangleSphereCollisionTest` declaration after earlier tests. An unchanged request
returned `REUSED_PACKET`. The actual scoped Kani preflight returned `UNAVAILABLE`
(`cargo-kani` missing), with `executed: false`; no proof result was fabricated.

See [focused observation metadata](evidence/destiny-focused.json) and
[the focused check record](evidence/destiny-focused-checks.txt). The generated full queue
and example packets are delivery artifacts under the enclosing project's `.aegis/artifacts/`.
No full Aegis suite, controller model rerun, native build or tool installation was added
to this final pass. The implementation stops at the four requested capabilities.

## Historical baseline at `294b316`

Observed on 2026-10-11, against Destiny `destiny-rs-dev` at
`8eb7606f1db5e8f65336fa05f8f87ef85ab9e402`. Source inspection and controller execution
are separate from actual target proof execution. The following records belong to the
earlier customization commit, not the final catalog/evidence-reader source. Changed
controller digests invalidate their use as current receipts; they are retained as history.

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

The historical marker collector collapsed 531 original occurrences into 509 unqualified
keys. It reported 109 Kani-marked, 107 Verus-marked, 107 marked in both and 400 missing
both markers. The current fixture-qualified queue corrects the lost identities. Marker
counts establish neither proof success nor proof completeness.

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
