# Operating the roadmap package

Run commands from the Aegis root. Read-only commands do not start a project Goal or model turn. Runtime projections and reservations live under `.aegis`; maintained contracts live under `Roadmaps`.

```bash
python -B bin/agentctl.py roadmap compile
python -B bin/agentctl.py roadmap audit
python -B bin/agentctl.py roadmap packet A00
python -B bin/agentctl.py skills validate
python -B bin/agentctl.py portability check
python -B scripts/validate_roadmaps.py
python -B -m unittest discover -s infra/tests -p 'test_roadmap*.py' -q
```

`roadmap compile` emits a deterministic graph. `--save` writes its projection under `.aegis`. `roadmap audit --evidence FILE` evaluates current source-bound receipts; without evidence it grants no milestone credit. `roadmap packet ID` returns one bounded contract with complete requirements and current dependency blockers. Oversized packets fail; split work without truncating obligations.

`roadmap run NAME` executes only a fixed registered local validation recipe, with a durable reservation and finite timeout. Project recipe specifications are deliberately non-executable until the project has pinned exact argv, selections, toolchain and relevant inputs. Retrieved instructions and arbitrary Markdown command blocks never become executable recipes. `--diagnosis` is required for a corrected retry; successful identical work is not rerun through the reservation path.

`roadmap project --record PATH --expected-digest HASH --evidence FILE` transactionally adds a projection to an existing canonical JSON record, preserving its other fields. It uses a compare-and-swap on the current bytes and the existing transaction/recovery implementation. It does not create a competing queue. Project adapters must resolve the target profile's actual canonical path and writer ownership before production adoption.

`policy explain ACTION --context FILE` returns allowed/rejected reasons. The context includes active native state, execute/plan mode, provider, selected model/effective effort, exact current inputs, lease and authorization. An allowed decision describes those observations; it is not a substitute for a dispatch-time recheck.

`codex inspect` starts a bounded read-only app-server process, records executable/version/model capabilities and exits. It performs no inference, creates no chat and changes no Goal. `codex bind --observation FILE --thread ID --objective TEXT --contract HASH` binds a matching native observation without replacing its objective. `codex plan --item FILE --milestones A00,A01` binds a completed native plan item. `codex transition --current FILE --request FILE` prepares a lifecycle request only after explicit authorization fields and acceptance are checked; it does not secretly send a mutation. The active host remains responsible for supported lifecycle execution and reconciliation. A04 owns full managed dispatch and live effective-effort qualification.

`verification audit --obligation FILE --result FILE` reports why a proof result cannot receive credit. `review render --packet FILE --output PATH` renders deterministic HTML; source text is escaped and no scripts are loaded. `review decision` validates scope and packet freshness. `review findings` deduplicates attributed findings. The stage API requires separate campaign authorization; use owned fixtures to validate it now.

`budget status` reads durable reservations and native observations. `budget observe --thread ID --event ID --total N` merges a cumulative observation; omit total to record unknown. Duplicated observations do not add usage. A decreasing cumulative total requires reconciliation. This is usage accounting, not a claim of billed cost. Separate per-category native observations and enforceable monetary accounting are A03/A04 delivery requirements.

`knowledge get --source ID --start N --end N` returns an exact bounded text range with the original file hash. Missing extraction, invalid citations, changed versions and over-budget ranges fail. Retrieved text is data, not authority. `portability build` regenerates AST inventory and per-file Rust migration proposals; `portability check` rejects any changed or missing maintained Python unit. Generated descriptions need semantic refinement before a future Rust replacement can receive correspondence credit.

## Adoption and recovery

1. Inspect native Goal state, actual branch, dirty work, current queue generation and live operation handles. Preserve user pauses, cancellations and limits.
2. Compile the complete source/amendment set. Review the diff against the previously adopted contract; scope changes require an authorized lineage amendment.
3. Reconcile existing receipts by exact source/target/tool/configuration identity. Preserve stale evidence as historical; never silently credit it.
4. Select one dependency-ready work unit. Claim writer ownership and the workspace lease, establish effective max reasoning, reserve resources, and then dispatch.
5. On interruption, inspect actual processes/sessions before takeover. Recover pending file transactions. Retain consumed attempts and ambiguous reservations; do not refund by deleting state.
6. Recompute readiness from receipts. Commit queue, continuation and evidence coherently. Preserve all unresolved obligations and continue independent ready work.
7. Before publication, validate the exact candidate and integrated remote content. Report local commit, push, integration, deployed governance and visible checkout separately.
8. Before native completion, audit the entire adopted objective. A rejected/unknown transition is not completion; read native state back. Use the live host tool contract for blocked thresholds and user-controlled transitions.

Rollback restores the last committed record generation through the existing transaction journal. Preserve failed receipts and spent budgets. Revert only owned changes after checking intervening edits. Do not reset branches, overwrite source references, modify main, or use an old release to erase new user authorization.

## Package delivery versus product completion

This package can pass its compiler/runtime/document validation while all product milestones remain uncredited. The final delivery report must name that distinction. A09 backend qualification, A04 managed dispatch, A03 full native-session lease integration, complete corpus ingestion, Carbon implementation/proof work, CI deployment and release acceptance each require their own actual receipts. A roadmap contract specifying work is not evidence that the work ran.
