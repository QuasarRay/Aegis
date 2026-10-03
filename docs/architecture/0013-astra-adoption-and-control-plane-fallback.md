# ADR 0013: Astra adoption path and safe control-plane fallback

## Status

Accepted as the integration boundary for the GitLab/Aegis architecture.

## Problem

The GitLab/Dagger/Rails architecture adds useful supervision and self-hosting capabilities, but an agent should not spend a large context window rediscovering the architecture before it can repair or continue formalization. The new control plane must also avoid making GitLab availability a prerequisite for work that the previous Python/PostgreSQL/Git/GitHub architecture could perform.

## Decision

`scripts/control_plane.py` is the bounded adoption and failover entrypoint.

The default `AEGIS_CONTROL_PLANE_MODE=auto` behaves as follows:

1. If a GitLab URL is configured, probe GitLab `/-/readiness?all=1`.
2. If GitLab and its dependent services are ready, select the GitLab Rails/MCP/Dagger control plane.
3. If GitLab is unconfigured or the readiness/delegation path fails, select the existing legacy controller.
4. Do not fork roadmap, evidence, PostgreSQL, `.aegis/`, or `.metarocq/` state when switching modes.

Explicit `gitlab` mode is fail-closed: it does not silently fall back. Explicit `legacy` mode does not contact GitLab.

## What may fail over

These are orchestration/availability failures and may use the legacy controller:

- GitLab web/Rails unavailable;
- GitLab MCP unavailable;
- GitLab CI delegation unavailable;
- Dagger/GitLab runner unavailable when an equivalent legacy controller operation exists;
- GitHub bridge unavailable (GitLab itself remains primary when healthy).

## What may never fail open

These remain hard blocks in every mode:

- PostgreSQL/event persistence failure;
- irreversible-record publication/recovery failure;
- Git commit/remote identity mismatch;
- source/roadmap identity mismatch;
- HOL4/Rocq/Kani/independent replay failure;
- missing formal theorem;
- closed `metatheory-verified` implementation gate;
- provider/model authorization requirement not independently established.

Fallback is therefore a control-plane substitution, not a trust-policy substitution.

## Shared state

Both modes consume the same machine-readable roadmap and evidence. The legacy path is the existing `pipelines/bootstrap.py` + PostgreSQL + Git publication controller. The GitLab path adds supervision, MCP, Rails UI, GitLab CI and Dagger around the same project contracts.

No GitLab-only database row, UI flag, Dagger success, GitHub status or fallback decision can mark a formal task complete.

## Astra adoption protocol

Astra should not begin by rereading the PR stack. The required sequence is:

```sh
python3 -B scripts/control_plane.py review
python3 -B scripts/control_plane.py diagnose
python3 -B scripts/control_plane.py adopt
```

The first command returns the bounded machine-readable context. The second identifies only failing architecture checks. The third returns the selected control plane and exact continuation interface.

If a check fails, inspect that check's named files only. Historical PRs and unchanged source are reference material, not mandatory context.

## CI fallback

The GitHub bridge workflow attempts exact-SHA delegation to the self-hosted GitLab control plane. If GitLab is reachable but delegation fails, the workflow validates the existing legacy bootstrap controller and reports a degraded fallback. It does not claim GitLab succeeded.

This is intended to keep repository development available during a GitLab fault while making the degraded state explicit.

## Recovery

Returning from legacy to GitLab requires no state migration: repair GitLab, rerun `control_plane.py select`, and continue against the same committed roadmap/evidence. If shared state changed while in legacy mode, GitLab sees that state through the repository/PostgreSQL integration rather than importing a separate fallback database.
