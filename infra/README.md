# Candle coordinator

Python 3.11+ and the standard library suffice. No mandatory Hypothesis dependency
remains. `bin/agentctl.py --help` lists the current interface; legacy lifecycle
commands are absent.

Existing Aegis filesystem/process/transaction primitives retain focused regression
checks. The coordinator binds original HOL definitions, reuse decisions, scope,
checker budgets and durable PRs. `kani_report.py` is reused from Candle-rs with its
license notice. Infrastructure tests are maintenance evidence, not a prerequisite
for implementing every Candle definition or proof of theorem-prover equivalence.
