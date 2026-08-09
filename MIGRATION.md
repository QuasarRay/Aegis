# Migration / Upgrade

Aegis is designed to compose with existing repositories rather than overwrite them.

## Replacing an older generic `.agents` framework

1. Preserve the old directory until its project-specific additions are identified.
2. Copy the new `.agents/` tree without copying `.agents/runtime/` state between unrelated projects.
3. Move project-specific policies/laws/modules into `.agents/project.md`, `.agents/laws/project/`, or `.agents/local-modules/` as appropriate.
4. Use `python .agents/bootstrap/install.py` for a dry-run root `AGENTS.md` merge; then rerun with `--apply`.
5. Run `python .agents/bin/agentctl.py manifest verify`, `audit`, and `law run`.
6. Install/verify host adapters explicitly (for example `module install codex --apply` then `module verify codex`).

Do not blindly delete an older framework when it may contain user-authored project overlays, law definitions, host configuration, evidence, or runtime state. Aegis installers fail closed on managed-block/config drift rather than guessing.

## Host adapter upgrades

Host APIs evolve independently. Re-run static adapter verification after framework updates and validate the effective host runtime in a fresh session before relying on enforcement claims. Static configuration is never treated as proof of live model, reasoning-effort, sandbox, or concurrency behavior.
