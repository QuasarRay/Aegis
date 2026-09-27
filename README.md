# Aegis for Candle-rs

This branch replaces Aegis's general-purpose controller with a contract workflow for
[QuasarRay/Candle-rs](https://github.com/QuasarRay/Candle-rs). Original Candle mathematical
specifications are the application contract. The [ITP 2022 paper](https://doi.org/10.4230/LIPIcs.ITP.2022.3)
is the ultimate scientific reference. Rust implements the contract; tests do not define it.

The original theories retain their HOL4 syntax and semantics. Pin and use upstream
files directly. An agent-written restatement is not a replacement oracle. Kani and Verus
check declared Rust obligations; their result is scoped and does not inherit original
Candle's end-to-end soundness theorem. See [authority](contracts/README.md).

## Work cycle

Run the controller from a pinned source checkout; it is not a pip-distributed package.
Python 3.11+ and Git are sufficient for the controller. Install Kani/Verus separately
only for the selected obligation. This avoids expensive optional tool setup.

1. Inspect `contracts/authority.json`, the relevant original definition, and the paper
   section. Read one compact architecture decision, not the entire repository.
2. Copy `templates/candle-plan.json` to `.candle/plan.json` in Candle-rs. Replace every
   placeholder. Record code reuse, source license, generation recipe, or why handwriting
   is cheapest. Keep one bounded set of obligations and explicit assumptions.
3. Add `.aegis/` and Rust build output to the target's `.gitignore`. Keep `.candle/plan.json`,
   `.candle/evidence/`, source, proof harnesses and architecture decisions tracked.
4. Bind the plan, implement in Rust, run selected verification, commit all work and
   evidence, push a branch and open a PR. Record its checkpoint before the next cycle.
   A blocked proof can be saved; it cannot be declared successful.

```python
# Run from a checkout with Aegis/infra on PYTHONPATH.
from pathlib import Path
from agentinfra.candle import Candle

work = Candle(Path("/work/Candle-rs"))
work.freeze(".candle/plan.json", {
    "candle": "/references/candle", "cakeml": "/references/cakeml",
})
print(work.brief())                 # generated, bounded work packet
# Implement/reuse/generate Rust and its correspondence obligations here.
print(work.verify(timeout=120))     # real tool invocation, bounded output
# Commit, push, and create the PR through the GitHub connector or existing tooling.
print(work.checkpoint(pr=123))      # live remote SHA + PR base/head check
print(work.audit())                # scoped evidence, never universal soundness
```

CLI equivalents are available via `python bin/agentctl.py --root /work/Candle-rs --help`.
Aegis never commits unrelated files, merges a PR, or configures branch protection on
its own. The checkpoint is a gate on the next managed cycle. Use small cycles; a crash
before publishing can still lose local work. GitHub commits preserve the source, plan
and evidence. After a fresh checkout, bind the same plan and rerun relevant checks;
local bookkeeping is not treated as externally authenticated proof.

## Cost and supervision

Reuse Aegis's atomic writes, process capture, path checks and locks. Generate repeated
briefs, instruction routing and proof work inventories from one contract. Select only
Kani harnesses or Verus entry files needed by the current obligation. No failing-test
precondition, readability or idiomaticness gate, performance campaign, concurrency
redesign, mandatory agent fan-out, or response-speed optimization exists in this branch.

Read [the architecture](docs/architecture/0001-candle-contract-control-plane.md),
[supervision boundaries](docs/SUPERVISION.md), and [migration](MIGRATION.md).
Run `python scripts/selftest.py` to check the controller and its negative cases.
`python scripts/generate.py --check` detects generated-file drift. These regression
checks are observations about Aegis, not the authority for Candle behavior.
