# Destiny utilities

Use `python bin/destinyctl.py --project /absolute/destiny PATH_COMMAND` from this
Aegis checkout. See the root README for a complete cycle. No files are installed in Destiny.

| Command | Purpose |
| --- | --- |
| `queue [--differential PATH]` | Write all 531 fixture-qualified obligations, independent assurance fields, existing proofs, families, gaps and blockers. |
| `catalog --query TEXT --limit 8` | Search a bounded slice of qualified identities; ambiguous legacy markers are exposed separately. |
| `harness --case SOURCE::FIXTURE::TEST` | Extract the actual fixture, setup, case and available dependencies from pinned original source. |
| `harness-close --outcome implemented\|reuse\|blocked --note TEXT` | Record the current work item's decision before opening another. No proof credit. |
| `plan --base REF` | Include committed, staged, unstaged, untracked and deleted paths; select a deduplicated prerequisite order. |
| `plan --changed PATH` | Explicit change selection; repeat for multiple paths. Unknown paths select the full matrix. |
| `plan --release` | Show all recipes and manual operational gates without executing them. |
| `context PATH --start N --lines N` | Return a bounded redacted excerpt, or UNCHANGED with its source digest. |
| `run NAME` | Run exactly one reviewed recipe; preserve a bounded output receipt. |
| `bind PATH` | Validate and bind a complete formal plan to current source and controller identities. |
| `verify ID` | Execute one declared obligation freshly, with its assumptions and scope. |
| `audit` | Report checked, missing, failed and stale obligations for the current binding. |

`run kani --harness NAME --proof-input FILE` selects one exact harness and binds its
source digest. `--manifest PATH/Cargo.toml` selects its actual crate (default:
`verification/kani/Cargo.toml`). `run verus --entry FILE
--expected-checks N` requires an entry already present in the profile and a positive
reviewed inventory count. These low-level commands produce observations; use a complete
formal plan to bind them to public invariants and correspondence assumptions.

Default source excerpts are 12 KB, capped at 64 KB. Each captured output stream is
bounded at 16 KB, with a full-stream digest. Timeouts and at most two attempts are
reserved durably before work. Repeating an attempt requires `--fresh --reason TEXT`;
changing only a prose diagnosis does not invalidate an exhausted execution identity.
The two cheap source reports are memoized; verification itself is never memoized.
Scoped Kani/Verus runs reserve 120 seconds. Unscoped verifier runs require `--full-suite`.
An unchanged harness packet is returned by reference. Reopening a closed case or rereading
the same packet requires `--fresh --reason`; one explicit packet reread is allowed.

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

## Evidence schema

An obligation may have an `evidence` object with exactly these fields:

- `kind`: `spec_proved` or `production_rust_refinement_proved`.
- `original_cases`: nonempty distinct fixture-qualified identities from the pinned catalog.
- `assertion_properties`: exact Kani property IDs ending in `.assertion.NUMBER`, all successful.
- `reachability`: nonempty objects `{ "property": "FUNCTION.cover.NUMBER", "file": "SOURCE", "line": 123 }`, all satisfied at those bound source locations.
- `relation`: the precise original/specification/implementation correspondence claimed.
- `review`: the review of original assertions, setup, domains, assumptions, bounds, witness placement and real production linkage.

Production refinement requires a reachability witness in a declared production `src/`
file. Include every relevant adapter and harness in `proof_inputs` and the actual
production files in `implementation`. The plan's optional `manifest` selects the crate
with that harness. Older plans without `evidence` remain unclassified; the queue never
guesses their assurance level. `CHECKED_SCOPED` always retains declared assumptions/limits.

Kani parsing follows [the pinned CLI](https://github.com/model-checking/kani/blob/kani-0.68.0/kani-driver/src/args/mod.rs)
and [the pinned output parser](https://github.com/model-checking/kani/blob/kani-0.68.0/kani-driver/src/cbmc_output_parser.rs).
The strict reader requires a satisfied cover in addition to successful assertions;
see [Kani reachability semantics](https://model-checking.github.io/kani/verification-results.html).

A runtime mapping file has this form (replace the sample receipt, scenario and rationale):

```json
{
  "schema": 1,
  "records": [{
    "case": "python/destiny/test/test_ball.py::BallTest::test_free_formation_slot",
    "observation": {
      "status": "OBSERVED_SUCCESS",
      "executed": true,
      "id": "native-differential",
      "key": "COPY_FROM_ACTUAL_RUN_RESULT",
      "receipt": ".aegis/destiny/receipts/COPY_ACTUAL_RECEIPT.json"
    },
    "scenarios": ["COPY_EXACT_VERBOSE_SCENARIO_NAME (module.Class.method)"],
    "rationale": "REPLACE_with_reviewed_original_to_runtime_scenario_correspondence"
  }]
}
```

Only actual `native-differential` or `original-formations` receipts qualify. Their source,
tool, controller, environment and external native library hashes must still match.
Every selected scenario must have run successfully; zero-case, skipped and truncated
executions are rejected. A runtime mapping remains reviewed scenario evidence, with
the reference revision discrepancy recorded in the authority; it cannot establish
universal parity or set either proof field. Store the mapping under `.aegis/` so its
creation does not change the source identity in the receipt.

The queue's `source_identity` binds the target snapshot. Regenerate after source changes;
do not treat a saved queue as a new proof observation. `semantic_family` is a routing aid,
and `gaps`, per-item `blockers`, global `blockers`, `tools` and `unmapped_proofs` preserve
incomplete or unusable evidence without silently dropping obligations.
