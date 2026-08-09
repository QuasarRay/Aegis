# Executable Infrastructure

`agentinfra` is a Python 3.11+ stdlib-only control plane. It deliberately does not depend on the
project's virtual environment packages.

Use `.agents/bin/agentctl.py` rather than installing the package. The package metadata exists for
optional editable development/testing.

Core functions: atomic state, stale-safe locks, hardened task transitions, acceptance gates,
evidence ledger, content freshness cache, module discovery, law execution, shell choice, manifest
verification and framework audit.

## Long-task bookkeeping

`agentctl task list` enumerates canonical tasks. `task decision-add` records durable decisions with optional
evidence IDs. `subagent close` requires an outcome and summary and stores the completed handoff in the task
state before releasing the global child lease.
