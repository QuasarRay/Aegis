# Aegis for Destiny Rust

This branch specializes Aegis for [Destiny's destiny-rs-dev branch](https://github.com/QuasarRay/destiny/tree/destiny-rs-dev),
inspected at `8eb7606f1db5e8f65336fa05f8f87ef85ab9e402`. Its acceptance scope is four capabilities:

1. Preserve all **531 original occurrences**, identified as `source::fixture::test`.
2. Bind exact Kani evidence to the pinned version, harness, source and proof-input digests;
   reject stale, cached, incomplete and vacuous observations, and report missing tools as `UNAVAILABLE`.
3. Keep mapping, specification proof, production Rust refinement proof and runtime differential evidence separate.
4. Write a machine-readable work queue with existing evidence, semantic families, gaps and blockers.

Development uses specifications, explicit invariants and formal verification. It retains
Max reasoning and saves work through small packets, source reuse, exact proof selection
and durable attempt limits. These controls do not meter or cap provider token billing.

## Start from the queue

Python 3.11+ and Git suffice. Run these commands from this checkout; `agentctl.py` and
`destinyctl.py` expose the same interface. The target Git repository must contain the
pinned original commit, or supply `--original /path/to/local/reference` to catalog/queue/harness.
No reference code is executed and no repository or verifier is downloaded automatically.

```sh
python -B bin/destinyctl.py --project /work/destiny queue
python -B bin/destinyctl.py --project /work/destiny catalog --query formation --limit 8
python -B bin/destinyctl.py --project /work/destiny harness \
  --case 'python/destiny/test/test_ball.py::BallTest::test_free_formation_slot'
```

`queue` writes `.aegis/destiny/work-queue.json` and prints only a compact summary.
All 531 identities are derived from the original source at
`ef738406b61ad06bae2f402857e464735ab106a2`. The catalog's semantic inventory is pinned:
dropping an occurrence fails validation. The previous collector reduced these to
509 unqualified keys. A legacy marker shared by several fixtures cannot discharge any
of those individual obligations; new markers use `// original-case: source::fixture::test`.

`harness` automatically extracts the selected original method/body, fixture setup,
inheritance and available helper dependencies. It records exact original file hashes,
assertion lines, existing candidates and unresolved dependencies. Python extraction uses
ASTs; C++ extraction handles the pinned GoogleTest declarations and balanced bodies.
Imports, macros and dynamic semantics still need source review. Assertions are never
silently truncated to fit a packet.

Only one work item may be open. Packets default to 12 KB; unchanged requests reuse the
saved packet. After implementation, reuse or a blocker, record the decision:

```sh
python -B bin/destinyctl.py --project /work/destiny harness-close \
  --outcome implemented --note 'Record the actual harness path and remaining gaps here.'
```

Closing a work item records progress. It does not establish proof.

## Bind and check one obligation

Copy [the formal plan template](modules/destiny/formal-plan.json) into the target and
replace every placeholder after reviewing the original behavior and actual Rust call path.
The template starts at specification assurance; the existing formation harness must be
reviewed and supplied with real assertion identities and reachability evidence before use.

```sh
python -B bin/destinyctl.py --project /work/destiny bind .destiny/plan.json
python -B bin/destinyctl.py --project /work/destiny verify formation-slot --budget-seconds 120
python -B bin/destinyctl.py --project /work/destiny audit
python -B bin/destinyctl.py --project /work/destiny queue
```

Kani must be **0.68.0**. A scoped invocation uses an exact fully qualified harness,
regular property output and a forced rebuild. It requires a successful behavioral
assertion and a satisfied cover witness; failed, unreachable, undetermined, truncated
or empty output gets no proof credit. Assumptions and bounds remain part of the claim.
The cover witness must exercise the relevant scenario after its domain restrictions.
The initial scoped time allowance is 120 seconds, with at most two attempts per identical
input. Retrying requires a recorded diagnosis. A broad verifier run requires `--full-suite`.

Every classified obligation declares its original identities, assertion property IDs,
source-located reachability witnesses and reviewed relation. Production refinement also
requires a satisfied witness inside the bound production `src/` implementation.
Use the actual Cargo manifest containing that harness. Merely importing production source
or running a specification-only harness cannot satisfy that requirement. Review must
check that the relational assertions constrain the real implementation without substituting
stubs or a separate model. Aegis checks evidence integrity and scope; it cannot infer
semantic adequacy from Rust syntax or from a user's prose declaration.

## Interpret the evidence

| Queue field | Meaning |
| --- | --- |
| `mapped_or_marked` | An unambiguous source marker or declared case mapping exists. |
| `spec_proved` | A current exact Kani observation discharged the declared specification scope. |
| `production_rust_refinement_proved` | Current Kani evidence discharged the reviewed relation and located production reachability witnesses. |
| `runtime_differential_evidence` | Reviewed original-case/scenario mappings have current successful native execution receipts. |

The fields are independent. `uncovered` means production refinement evidence is absent.
Earlier bindings remain visible; stale bindings carry blockers and get no proof credit.
Unclassified older proofs are retained in `unmapped_proofs` for review. No marker count,
compiler exit code, cached report or runtime comparison is promoted into refinement proof.
Missing evidence is a gap, not evidence that no proof exists elsewhere.

Runtime receipt mappings can be consumed with `queue --differential .aegis/destiny/runtime.json`;
see [the command and schema guide](modules/destiny/README.md). Semantic families are
advisory classifications by source/name. The catalog and formation CI cite different
original revisions; correspondence between those authorities must remain explicit.

All 25 Aegis, 33 Destiny and 85 PMAT branch heads were inventoried. The implementation
reuses inspected Candle/MetaRocq helpers and the existing atomic, locking and process
utilities. HOL4, MetaRocq and other specialized work is recorded at its sibling-branch pins.
See [branch review](modules/destiny/BRANCH_REVIEW.md), [reuse provenance](modules/destiny/reuse-provenance.json)
and [focused validation](docs/VERIFICATION.md). The historical controller model has no
proved refinement to Python and establishes no Destiny theorem. No further Aegis-wide
verification campaign is required for this customization's four-capability finish line.
