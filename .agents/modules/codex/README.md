# Codex Infrastructure Module

This optional adapter turns host-independent Aegis invariants into Codex configuration and custom roles.
It is not required by the core framework.

## Install

Dry run first:

`python .agents/modules/codex/install.py`

Apply:

`python .agents/modules/codex/install.py --apply`

Then run:

`python .agents/modules/codex/verify.py`

The installer manages project-local `.codex/config.toml` plus `.codex/agents/aegis-*.toml`. It preserves
unrelated configuration and fails closed on conflicting managed values or unmanaged role-file collisions.
Backups live under ignored `.agents/runtime/backups/`.

## Effective-runtime verification

Static verification proves only file configuration. After installing into a real Codex environment,
inspect the live parent and spawned-child metadata. Confirm `gpt-5.6-sol`, `max`, selected role profile,
expected sandbox, and one-child behavior. Treat inability to observe a property as *unverified*, not as a
pass. Current Codex versions may differ in how custom-agent profiles are selected/applied, especially
between multi-agent backends and CLI/Desktop builds.

## Uninstall safely

Preview: `python .agents/modules/codex/uninstall.py`

Apply: `python .agents/modules/codex/uninstall.py --apply`

Uninstall uses the local install journal and exact post-install hashes. If any managed Codex file was
changed after installation, it refuses to overwrite it rather than guessing how to merge backwards.

## V1 / V2 concurrency

Current Codex has two multi-agent backends with different concurrency configuration. Aegis does not force-enable V2 because released clients have had V2 regressions. The installed config sets the V2 session capacity to **2 total threads** (root + one child) without changing the V2 enabled flag. The host-independent Aegis lease remains the cross-backend source of truth and children are explicitly forbidden to delegate. Verify the live backend and effective limit after starting a fresh Codex session.
