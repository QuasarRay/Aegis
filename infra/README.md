# Controller runtime

Python 3.11+ standard library only. Run `python bin/agentctl.py --help` from the
source checkout. `destiny.py` owns plans, context, sequential execution and receipts;
`formal.py` binds public contracts and audits exact verifier observations. Shared atomic,
process, confinement and lock utilities are retained from Aegis rather than reimplemented.

`python scripts/selftest.py` exercises operational regressions. Formal control invariants
and their deductive proof entry point are in `verification/`; their scope is narrower than
Python implementation correctness and is documented there.
