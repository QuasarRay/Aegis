# Aegis GitLab Runtime Instructions

These rules specialize the repository root `AGENTS.md`.

- GitLab CE/FOSS is the only Rails application. Never create a second Rails app, authentication system, session store, or parallel web database.
- Keep the exact GitLab host revision and anchored files pinned in `gitlab/runtime.lock.json`; fail closed on drift.
- Human supervision UI and MCP must be read-only by default and derive facts from MetaRocq-rs/Aegis evidence. Process success is not formal proof.
- Reuse GitLab authorization and MCP infrastructure. Aegis capability policy is additional defense, not a substitute for GitLab authorization.
- Preserve the `metatheory-verified` implementation gate.
- Generate UI/API surfaces from stable machine-readable Aegis schemas where practical; avoid duplicate frontend state machines.
