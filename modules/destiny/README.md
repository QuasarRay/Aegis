# Destiny utilities

Use `python bin/destinyctl.py --project /absolute/destiny PATH_COMMAND` from this
Aegis checkout. See the root README for a complete cycle. No files are installed in Destiny.

| Command | Purpose |
| --- | --- |
| `plan --base REF` | Include committed, staged, unstaged, untracked and deleted paths; select a deduplicated prerequisite order. |
| `plan --changed PATH` | Explicit change selection; repeat for multiple paths. Unknown paths select the full matrix. |
| `plan --release` | Show all recipes and manual operational gates without executing them. |
| `context PATH --start N --lines N` | Return a bounded redacted excerpt, or UNCHANGED with its source digest. |
| `run NAME` | Run exactly one reviewed recipe; preserve a bounded output receipt. |
| `bind PATH` | Validate and bind a complete formal plan to current source and controller identities. |
| `verify ID` | Execute one declared obligation freshly, with its assumptions and scope. |
| `audit` | Report checked, missing, failed and stale obligations for the current binding. |

`run kani --harness NAME` selects one exact harness. `run verus --entry FILE
--expected-checks N` requires an entry already present in the profile and a positive
reviewed inventory count. These low-level commands produce observations; use a complete
formal plan to bind them to public invariants and correspondence assumptions.

Default source excerpts are 12 KB, capped at 64 KB. Each captured output stream is
bounded at 16 KB, with a full-stream digest. Timeouts and at most two attempts are
reserved durably before work. Repeating an attempt requires `--fresh --reason TEXT`;
changing only a prose diagnosis does not invalidate an exhausted execution identity.
The two cheap source reports are memoized; verification itself is never memoized.

Cargo is offline and rustup auto-install is disabled by default. `--allow-network`
explicitly changes that environment. Tools and external references must be supplied
and match the profile; missing native libraries and mismatched original revisions
fail before execution. Tool probes consume the declared budget. Host-generated caches
and build outputs are not authenticated; treat receipts as local integrity records.

For formal plans, replace every template marker and use paths relative to the target.
Bind after the implementation is ready for verification. Any source, plan, profile,
controller or verifier change requires a new binding/observation. Preserve proof files
and the completed plan in Git; .aegis state is rebuildable local bookkeeping.

Locks, budgets and context receipts are scoped to one checkout. Keep one canonical task
owner; separate clones need separate coordination and do not share these local counters.
