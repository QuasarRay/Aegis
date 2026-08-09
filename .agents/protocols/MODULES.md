# Module Protocol

Agent/environment-specific behavior is isolated below `.agents/modules/<id>/` or project-local
`.agents/local-modules/<id>/`. The host-independent core does not import or execute module code merely
because a module exists.

Each module has `module.toml` with `[module]` metadata, policy paths, optional detection hints, and optional
explicit installer/verifier argv commands. `agentctl module list/show` performs metadata-only discovery.
`agentctl module install/verify <id>` executes only the action explicitly declared by that manifest and only
because the parent requested it.

## Composition

Built-in module IDs must be unique. A project-local module may replace a built-in module only by using the
same ID **and** explicitly declaring `module.replaces = "<id>"`; accidental duplicate IDs fail closed. Core
hard invariants cannot be weakened by any replacement. This makes agent-specific modules composable without
silent shadowing.

A host module should provide, as applicable: detection, policy, configuration template, effective-runtime
verification instructions, bounded child-role mapping, and safe transactional install/uninstall behavior.
An environment module should describe when it improves correctness/cost and how to detect it.

Keep recovery-critical core infrastructure stdlib-only. Optional extension modules may depend on richer
packages such as `mcpyrate` or `unpythonic`, but absence of those packages must not prevent state recovery,
law execution, framework audit, or module discovery.

Create a new project-local adapter skeleton with `agentctl module scaffold <id> --kind <kind>`. Scaffolded
modules are metadata + policy only; executable actions remain opt-in additions declared in the manifest.
