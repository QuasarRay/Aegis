# Package validation and evidence limits

`scripts/validate_roadmaps.py` compiles the complete package twice, checks deterministic output, verifies pinned inputs and requirement coverage, creates bounded packets for every milestone, checks skill packaging and confirms that empty evidence grants no product completion. `infra/tests/test_roadmap.py` supplies positive and negative fixtures for the enforcement functions. The existing full self-test suite supplies additional atomic-write, process, lock, transaction and legacy-controller regressions.

| Required scenario | Executable coverage |
|---|---|
| Missing/duplicate source entities, target owners, relationships | `test_correspondence_bijection_and_relationships` |
| Missing fixture, duplicate name, parameter/configuration occurrence | `test_fixture_and_configuration_denominator` |
| Changed assertions, tolerance, teardown, quantification, narrowed domain | `test_exact_semantics_detect_each_weakened_field`; `test_proof_strength_and_freshness` |
| Vacuous, stale, truncated, interrupted, model-only or unsupported proof | `test_proof_strength_and_freshness`; existing exact evidence-parser tests |
| Changed source/generator/dependency inputs and installed artifacts | `test_source_edits_rejected`; `test_stale_and_mixed_candidate_evidence`; original-test artifact reconciliation |
| Goal replacement, accounting reset, pauses/clear and ambiguous completion | `test_native_identity_pause_clear_and_accounting`; `test_native_completion_requires_confirmed_readback` |
| Plan mode, scope expansion, protected source writes | `test_plan_scope_effort_and_campaign_gates`; `test_native_plan_scope_and_transport_boundary`; `test_scope_protects_originals_and_declares_owned_paths` |
| Reasoning downgrade, unobserved setting, model rerouting | `test_plan_scope_effort_and_campaign_gates` |
| Duplicate dispatch, interrupted reservation, stale fence, partial writes | reservation and workspace-fencing tests; existing transaction/recovery suite |
| Lost/duplicate/cumulative/unavailable usage | `test_cumulative_usage_unknown_duplicates_and_resets` |
| Stale or out-of-scope human approval | `test_review_escaping_staleness_and_scoped_decision` |
| Retrieved instructions attempting to change policy or execute commands | `test_recipe_injection`; escaped review sources; exact corpus authority labels |
| Missing corpus/extraction, wrong citations and version mismatch | `test_corpus_exact_citations_versions_and_budget`; corpus manifest explicitly retains pending sources |
| Python blocks absent from Rust migration map | `test_python_behavior_inventory_changes_and_blocks`; complete `portability check` |
| CI/receipt credited to the wrong tree or package | same-candidate artifact checks and original-test loaded identity reconciliation; A12 still requires real GitLab qualification |
| Early CGP phase | `test_early_cgp_dependency_rejected`; `test_budgets_and_completion`; policy harness global barrier cases |
| Cycles, unknown schemas/recipes and denominator removal | compiler negative scenarios |

Tests establish the behavior of the declared controls on their tested inputs. They do not authenticate arbitrary producer claims, prove extraction adequacy, establish all filesystem/transport behaviors, verify Carbon, or replace the future production-linked formal campaign. The included finite Python policy harness imports actual production functions and reports runtime evidence only.

The package's Dagger recipe is pinned and executable on a provisioned qualified runner. Local Python checks and generated protocol schemas do not count as a Dagger/GitLab run, live managed dispatch, deployed `.agents`, or product publication. Record those outcomes only when executed.
