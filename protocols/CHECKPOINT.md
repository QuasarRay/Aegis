# Durable progress protocol

One active obligation batch is allowed. Original HOL definitions and the reuse
plan authorize implementation. Checker attempts are charged before execution;
a crashed attempt still consumes budget. Failures may be checkpointed honestly.

`prepare-checkpoint` retains the plan, source identities, results, available Kani
exports and captured command logs under `supervision/checkpoints/<batch>/`.
Commit the packet and implementation; push a new branch and open a draft PR onto
the preceding checkpoint branch. The first batch uses its explicit initial base.
`checkpoint --pr URL` checks GitHub metadata and `git ls-remote`.

A second batch is denied until progress exists remotely. No operation merges,
force-pushes, rewrites history or deletes user work. Same-user external tools can
bypass APIs; a coordinator is not an OS sandbox. Preserve the branch on interruption
and inspect `status`. Do not relabel edited local state as a proof. Recover from
a remote packet in a fresh checkout after independent review if necessary.
