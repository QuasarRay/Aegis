# Policy Router

Load only what the current task needs. The root `AGENTS.md` contains hard defaults; specialist policies add
precision without requiring every task to ingest the full framework.

## Always relevant for substantial work
- `core/00-charter.md`
- `core/01-max-reasoning-and-cost.md`
- `core/02-hardened-state-machine.md`
- `core/03-sequential-subagents.md`
- `core/04-context-cache-bandwidth.md`
- `core/05-evidence-claims.md`

## By task
- implementation/debugging: `core/06-execution-workflow.md`, `07-code-architecture-quality.md`, `12-failure-recovery.md`
- testing/compatibility: `core/08-testing-and-laws.md`, `protocols/LAW_TESTS.md`
- Git/worktrees/user changes: `core/09-git-workspace.md`
- commands/interactive work: `core/10-tools-and-shells.md`, `protocols/ENVIRONMENT_SELECTION.md`
- security/dependencies: `core/11-security-dependencies.md`
- performance: `core/13-performance.md`
- final response: `core/14-reporting.md`

## Bootstrap and executable infrastructure
- safe root-instruction merge/uninstall: `bootstrap/README.md`
- control-plane usage: `infra/README.md`
- upgrades from older framework copies: `MIGRATION.md`

## Protocols
- canonical task state: `protocols/STATE.md`
- subagent leases/handoffs: `protocols/SUBAGENT.md`
- behavioral laws: `protocols/LAW_TESTS.md` + `infra/agentinfra/lawlib.py`
- optional modules: `protocols/MODULES.md`
- shell selection: `protocols/ENVIRONMENT_SELECTION.md`

## Adapters
Read a module policy only when that host/environment is used. `modules/codex/` is the first enforced host
adapter; `modules/xonsh/` is an interactive environment adapter; `modules/python-meta/` is an optional
extension-authoring layer. Project-specific adapters belong under `.agents/local-modules/`.
