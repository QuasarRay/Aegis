# Aegis Framework 5.0.0

This `candle-rs` specialization coordinates the Rust implementation of Candle.
The [Candle paper](https://doi.org/10.4230/LIPIcs.ITP.2022.3) is the ultimate
scientific/architectural reference. Original, byte-identical HOL4 files provide
the mathematical contract; their interpretation stays in HOL4. See
[ADR-0001](docs/adr/0001-candle-authority-and-cost.md).

Implementation starts from an OPEN specification obligation and a reuse/generation
decision. No failing test, property-testing campaign or RED/GREEN chronology is
required. Auxiliary checks remain useful evidence.

## Source maintenance

Python 3.11+ and Git suffice on CachyOS. Runtime dependencies are standard library only.

```sh
python3 -B scripts/sync_agents.py
python3 -B bin/agentctl.py --root . audit
python3 -B scripts/selftest.py
python3 -B bin/agentctl.py --root . package dist/candle-release
python3 -B scripts/verify_release.py dist/candle-release
```

The package builder reuses Aegis's filesystem transactions. Review the generated
`dist/candle-release/.agents/` and commit it in the target before starting a batch.
Merge its working agreement into the target's canonical goals and generate the
target's instruction copies in that separate setup commit. Root `AGENTS.md` is
canonical within this source package. Do not reread identical copies for context.

## Candle implementation loop

In Candle-rs, ignore `.aegis/` and `target/`, commit setup changes and fetch the
base. Adapt [the plan template](templates/candle-batch.json), including its branch,
exact file scope, original HOL definitions and honest reuse assessment. Store the
plan outside tracked source until `begin` binds it.

```sh
git switch -c codex/candle-types origin/master
python3 -B .agents/bin/agentctl.py --root . begin /path/to/batch.json
python3 -B .agents/bin/agentctl.py --root . authorize-write src/lib.rs
# Implement/generate the registered slice, reusing existing code first.
python3 -B .agents/bin/agentctl.py --root . verify
python3 -B .agents/bin/agentctl.py --root . prepare-checkpoint
# Commit implementation and supervision/checkpoints/<batch>/, push, open draft PR.
python3 -B .agents/bin/agentctl.py --root . checkpoint --pr https://github.com/QuasarRay/Candle-rs/pull/NUMBER
python3 -B .agents/bin/agentctl.py --root . status
```

The next batch starts from the preceding recorded remote branch. Aegis does not
make paid model calls, commit, push, create PRs, merge or force-push automatically.
The agent performs the authorized GitHub actions through its available integration;
Aegis reads GitHub PR metadata and the remote ref to verify the exact checkpoint.
A local commit alone is insufficient. Failed proofs can be checkpointed honestly.

## Evidence and limits

Kani 0.68.0 runs the actual target crate and registered harnesses. The collector
checks exact result inventory, source identity, bounds and successful assertions.
Missing, timed-out and stale results remain non-passing. Identical attempts reuse
content-bound results; source, plan, policy or reported tool-version changes
invalidate that key. Budgets prevent indefinite identical retries.

BOUNDED_PASS does not close unbounded HOL refinement. **Original Candle itself is
the required final proof checker.** Each plan must assess its proof replay,
metaprogramming and generation facilities and use them when they save cost.
The Rust semantics bridge, HOL4-to-Candle correspondence, complete refinement
statement and reproducible original Candle replay remain OPEN. See
[ADR-0002](docs/adr/0002-original-candle-refinement.md). Aegis
cannot pronounce Candle complete, and the coordinator is not formally verified.
Reuse Kani/Verus's original macros, models and libraries in the target project.

Local hash seals are not signatures against an agent with the same OS account.
Managed APIs check scope and integrity; external tools can bypass them. A supervisor
must review and rerun from a separately trusted checkout/toolchain. The Git-visible
snapshot does not attest undeclared external compiler inputs. Public GitHub is
currently the checkpoint backend; private repository authentication and automatic
stack retargeting are not implemented.

No generic readability, idiom, benchmark, performance, concurrency, stress-test or
delegation campaign is mandatory. The selected model is `gpt-6-astra`; configuration
intent and actual host routing remain separate claims.
