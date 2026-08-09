# Aegis Framework 0.0.1

A project-independent coding-agent operating framework with a small host-neutral policy core, executable
state/evidence/law infrastructure, and optional host/environment adapters.

Design targets:

- **Max reasoning by default** for parent and subagents;
- save credits through fewer calls, sequential delegation, bounded fresh contexts, local caching and less
  rework—not by silently reducing reasoning effort;
- globally one active child and no nested delegation;
- hardened parent-owned workflow state and evidence-backed claims;
- Karpal-inspired behavioral law testing at production boundaries;
- content-hash context freshness to avoid redundant model/network reads;
- modular host adapters (`codex`, `xonsh`, optional Python metaprogramming, project-local modules);
- preservation of user work, test integrity and truthful validation.

The executable core uses only the Python standard library so recovery and verification remain portable.
Optional `mcpyrate`/`unpythonic` extensions may build richer DSLs without becoming a bootstrap dependency.

Start with repository-root `AGENTS.md`, then `.agents/INDEX.md`. Use
`python .agents/bin/agentctl.py doctor` to inspect capabilities and `... law run` for framework/project laws.

## Safe installation into an existing repository

If the target already has a root `AGENTS.md`, copy `.agents/` first and preview the generic bootstrap merge:

```text
python .agents/bootstrap/install.py
python .agents/bootstrap/install.py --apply
```

Do not overwrite an existing root instruction file by blindly extracting the packaged root `AGENTS.md`.
The bootstrap installer manages only a delimited Aegis block and preserves unrelated instructions. See
`.agents/bootstrap/README.md`.

## Executable control plane

`agentctl` provides task-state transitions, evidence, acceptance gates, risks, sequential child leases,
context freshness, shell selection, behavioral laws, module discovery/actions, framework integrity and Codex
adapter management. The recovery-critical core is Python 3.11+ stdlib-only.

For project-owned Python law suites, `.agents/infra/agentinfra/lawlib.py` supplies compact helpers for
idempotence, determinism, round trips, commutativity, associativity, monotonicity, conservation,
differential behavior and state-sequence invariants.

## Adapter philosophy

Host-specific enforcement belongs in modules rather than the generic core. The Codex module pins
`gpt-5.6-sol` + `max`, accounts for current V1/V2 multi-agent differences, installs role profiles
transactionally, and requires effective-runtime verification. The Xonsh module provides a first-class mixed
Python/subprocess interactive surface when that reduces quoting, glue and repeated tool calls. Optional
metaprogramming remains outside the bootstrap dependency set.
