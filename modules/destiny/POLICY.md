# Destiny formal development contract

The customization is complete when it preserves the 531 fixture-qualified originals,
checks exact current Kani evidence, separates the four assurance levels and emits the
machine-readable work queue. Stop Aegis infrastructure work at that boundary. Do not
launch an Aegis-wide campaign as a prerequisite for implementing a Destiny harness.

## Authority and obligations

Use Destiny's original behavioral definitions, engine-independent Rust specification,
representation adapters and named correspondence obligations. The target reference is
recorded in `contracts/destiny.json`; it is not a proof result. Preserve the distinction
between Specified, ImplementationMissing, ProofMissing and KnownMismatch in Destiny's
own verification inventory. Resolve an authority discrepancy explicitly, not by choosing
the reference that happens to make verification succeed.

For each change, record a precise invariant, relevant original/specification definitions,
implementation paths, selected exact Kani harness or counted Verus entry, assumptions,
known bounds and unproved correspondence. Inspect existing equivalents before implementing.
Extract fixtures and case bodies automatically from the pinned original Git blobs.
Never invent fixture names, merge repeated test names, or use ambiguous legacy markers
to cover multiple fixtures. Preserve every original assertion and its setup dependencies.
Record reuse/license decisions and a generator recipe when generation is appropriate.
Then implement, bind the actual source and run the selected proof obligation. A failed
obligation requires diagnosis; do not weaken it to pass. Incomplete work remains explicit.

Proved parity needs all of: the original rule, specification, representation adapter,
concrete implementation proof and applicable deductive refinement. Differential observations
can expose gaps across native/Python/engine boundaries but cannot establish universal
correspondence. Marker coverage, compilation, lints and runtime regressions are diagnostics.
A parser accepting success output does not prove a specification is sufficient.

## Work economy

- Consult the pinned branch inventory and context ledger before re-reading repositories.
- Keep Max reasoning; bound the work packet, source excerpts and public decision record.
- Select a single exact obligation. Plans deduplicate dependencies and are conservative
  for unknown paths. Do not launch all recipes just because a plan lists them.
- Reuse deterministic report receipts only when source, tool, recipe and environment
  identities match. Display reuse explicitly; never turn it into fresh proof evidence.
- Reserve attempt/time budget before executing. Two attempts per identical input are the
  default limit; a repeated or interrupted run requires a diagnosis. No automatic reset.
- Formal runs are always fresh. A source or tool change invalidates the observation.
- Do not install tools or enable network use implicitly. No provider API calls, external
  service fleet, automatic fan-out or speculative performance campaign are needed.

## Execution and claims

The `bind`, `verify`, `audit` workflow is fail-closed for missing evidence and changed
inputs. `CHECKED_SCOPED` means exactly the declared, non-vacuous verifier inventory at
the recorded source/tool identities. It is not an attestation of end-to-end soundness.
Read and retain the actual assumptions, unwind bounds, trusted externals and proof limits.

The native differential recipe requires a real library because a skipped native path
is not success. Operational release recipes preserve Destiny's platform, packaging and
transport diagnostics; one local host cannot certify their entire matrix. Never suppress
a failure or skipped boundary by relabelling it as verified.

Production refinement credit additionally requires exact successful relational assertions
and a satisfied, source-located cover witness in the bound production implementation.
Review the actual call path, adapters and assumptions; a specification harness or an
unused production import does not establish production refinement. Runtime comparisons
have their own evidence field and cannot discharge a formal obligation.
