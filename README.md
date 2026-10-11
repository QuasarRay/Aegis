# Aegis for Destiny Rust

This branch specializes Aegis for [QuasarRay/destiny, destiny-rs-dev](https://github.com/QuasarRay/destiny/tree/destiny-rs-dev).
It uses specification and formal verification as the development contract, with bounded
context, durable attempt budgets, conservative dependency planning and explicit proof scope.
The target revision inspected is `8eb7606f1db5e8f65336fa05f8f87ef85ab9e402`.

The design reuses the formal workflow introduced on Aegis's Candle branches and hardened
on its MetaRocq branches. All 25 Aegis, 33 Destiny and 85 PMAT branch heads were inventoried;
relevant distinct implementations were compared. See [branch review](modules/destiny/BRANCH_REVIEW.md)
and [source provenance](modules/destiny/reuse-provenance.json). HOL4, MetaRocq, extraction,
TacticToe and supervision implementations remain available at their pinned sibling branches.
Destiny's existing Kani and Verus obligations are reused directly.

## Use from this checkout

Python 3.11+ and Git suffice for planning, context and binding. Verifiers are required
only when selected, must match Destiny's pins, and are never installed automatically.
Use either `bin/agentctl.py` or `bin/destinyctl.py`; they expose the same interface.

```sh
python bin/agentctl.py --project /work/destiny plan --base origin/destiny-rs-dev
python bin/agentctl.py --project /work/destiny context src/runtime.rs --start 100 --lines 80
python bin/agentctl.py --project /work/destiny run proof-markers
python bin/agentctl.py --project /work/destiny run repetition
```

Plans never execute commands. An unmapped change selects the complete matrix; a release
plan includes all operational checks. Each `run` invokes one named recipe, with finite
wall time, output and attempt budgets. Its prerequisites are displayed, not silently run.
Unchanged report inputs reuse a hash-bound receipt. Formal verification is never memoized.
These controls limit local work; they neither meter nor enforce provider token billing.

For a formal cycle, copy [the plan template](modules/destiny/formal-plan.json) into the
target checkout, replace every placeholder with real definitions and proof entries,
implement the obligation, then bind and verify the exact source:

```sh
python bin/agentctl.py --project /work/destiny bind .destiny/plan.json
python bin/agentctl.py --project /work/destiny verify formation-slot
python bin/agentctl.py --project /work/destiny audit
```

A binding records specification/implementation/harness identities, assumptions, limits
and reuse rationale. A changed input makes it stale. Only fresh, exact, non-vacuous
verifier output can yield `CHECKED_SCOPED`. That status concerns declared obligations;
it never certifies the completeness of their selection or end-to-end Destiny parity.
Missing or incorrect tool versions are `UNAVAILABLE`, not passed checks.

## Assurance and maintenance

[Destiny policy](modules/destiny/POLICY.md) defines correspondence boundaries; the existing
marker collector is an inventory, and a duplication scanner supplies candidates. Neither
is a proof. Native, Python, wheel and platform smoke/regression checks remain available
as operational diagnostics alongside the formal contract.

```sh
python scripts/check_formal.py --verus /opt/verus/verus
python scripts/selftest.py
```

The first command deductively checks [the controller model](verification/control.rs)
with its separately pinned toolchain and records source/tool/output identity. The second
exercises controller regression cases without any third-party Python dependency. The
model's abstraction boundary and the absence of a proved refinement to Python are explicit.
Neither command proves Destiny correct. See [migration](MIGRATION.md) and
[verification scope](verification/README.md) before interpreting results.

Actual observations and tool limitations are recorded in [the verification record](docs/VERIFICATION.md).
