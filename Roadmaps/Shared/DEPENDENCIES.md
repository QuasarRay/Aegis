# Cross-project dependency and execution order

This deterministic preference order prioritizes implementation closure before comprehensive proof closure. Dependencies and current capability receipts still govern readiness; early proof can proceed when a concrete benefit is recorded. A blocked unit does not remove responsibilities or prevent independent ready work.

| Order | Milestone | Required capabilities | Phase |
|---|---|---|---|
| 1 | [A00](../Aegis/00-authority-branch-inventory-and-preservation.md) |  | implementation |
| 2 | [A01](../Aegis/01-policy-transition-and-roadmap-compiler.md) | authority_inventory (A00) | implementation |
| 3 | [A02](../Aegis/02-modular-hybrid-controller.md) | roadmap_compiler (A01) | implementation |
| 4 | [A03](../Aegis/03-durable-execution-deduplication-and-budgets.md) | hybrid_interfaces (A02) | implementation |
| 5 | [A04](../Aegis/04-native-codex-integration.md) | durable_execution (A03) | implementation |
| 6 | [A05](../Aegis/05-source-inventory-and-correspondence.md) | native_codex (A04) | implementation |
| 7 | [B00](../Blue/00-source-authority-and-full-inventory.md) | durable_execution (A03); source_correspondence (A05) | implementation |
| 8 | [B01](../Blue/01-unified-build-and-early-feasibility.md) | blue_inventory (B00); native_codex (A04) | implementation |
| 9 | [B02](../Blue/02-complete-canonical-vertical-path.md) | blue_build_routes (B01); source_correspondence (A05) | implementation |
| 10 | [D00](../Destiny/00-authority-and-existing-work-reconciliation.md) | durable_execution (A03); source_correspondence (A05) | implementation |
| 11 | [D01](../Destiny/01-current-blue-and-shared-runtime-integration.md) | destiny_inventory (D00); blue_vertical_runtime (B02) | implementation |
| 12 | [D02](../Destiny/02-canonical-objects-and-lifecycle.md) | destiny_blue_integration (D01) | implementation |
| 13 | [A06](../Aegis/06-knowledge-corpus-and-skills.md) | source_correspondence (A05) | implementation |
| 14 | [A07](../Aegis/07-macro-and-generation-support.md) | source_correspondence (A05) | implementation |
| 15 | [B03](../Blue/03-object-model-exposure-and-lifetime.md) | blue_vertical_runtime (B02) | implementation |
| 16 | [B04](../Blue/04-scheduling-time-events-and-task-context.md) | blue_vertical_runtime (B02) | implementation |
| 17 | [D03](../Destiny/03-numeric-state-time-and-geometry.md) | destiny_objects (D02) | implementation |
| 18 | [D04](../Destiny/04-forces-collisions-and-spatial-organization.md) | destiny_numeric_geometry (D03) | implementation |
| 19 | [B05](../Blue/05-streams-paths-and-external-i-o.md) | blue_vertical_runtime (B02) | implementation |
| 20 | [B06](../Blue/06-resources-persistence-and-structured-data.md) | blue_object_lifecycle (B03); blue_scheduling (B04); blue_io (B05) | implementation |
| 21 | [D05](../Destiny/05-movement-modes-and-transitions.md) | destiny_numeric_geometry (D03); destiny_physics_spatial (D04) | implementation |
| 22 | [D06](../Destiny/06-visibility-proximity-and-notifications.md) | destiny_objects (D02); destiny_physics_spatial (D04) | implementation |
| 23 | [D07](../Destiny/07-mutation-persistence-and-temporal-behavior.md) | destiny_numeric_geometry (D03); destiny_modes (D05); destiny_visibility_events (D06); blue_resources_formats (B06) | implementation |
| 24 | [B07](../Blue/07-remaining-production-closure.md) | blue_object_lifecycle (B03); blue_scheduling (B04); blue_io (B05); blue_resources_formats (B06) | implementation |
| 25 | [D08](../Destiny/08-client-server-and-host-closure.md) | destiny_modes (D05); destiny_visibility_events (D06); destiny_temporal_formats (D07); blue_scheduling (B04); blue_io (B05) | implementation |
| 26 | [A12](../Aegis/12-ci-deployment-and-self-development.md) | durable_execution (A03); knowledge_skills (A06) | implementation |
| 27 | [B08](../Blue/08-integrated-implementation-acceptance.md) | blue_production_closure (B07); release_pipeline (A12) | implementation |
| 28 | [D09](../Destiny/09-complete-implementation-acceptance.md) | destiny_host_closure (D08); blue_implementation_ready (B08); release_pipeline (A12) | implementation |
| 29 | [A08](../Aegis/08-rust-verification-infrastructure.md) | source_correspondence (A05) | implementation |
| 30 | [A09](../Aegis/09-python-verification-integration.md) | hybrid_interfaces (A02) | implementation |
| 31 | [A10](../Aegis/10-human-proof-supervision.md) | knowledge_skills (A06); rust_verification (A08) | implementation |
| 32 | [A11](../Aegis/11-generic-review-and-flaw-documentation-engine.md) | knowledge_skills (A06); human_review (A10) | implementation |
| 33 | [A13](../Aegis/13-aegis-domain-verification-and-completion.md) | macro_generation (A07); rust_verification (A08); python_verification (A09); human_review (A10); review_engine (A11); release_pipeline (A12) | completion |
| 34 | [B09](../Blue/09-exact-domain-verification.md) | blue_implementation_ready (B08); rust_verification (A08); human_review (A10) | verification |
| 35 | [B10](../Blue/10-final-acceptance-documentation-and-publication.md) | blue_domain_verified (B09); release_pipeline (A12) | completion |
| 36 | [D10](../Destiny/10-exact-domain-verification.md) | destiny_implementation_ready (D09); rust_verification (A08); human_review (A10) | verification |
| 37 | [D11](../Destiny/11-final-acceptance-and-publication.md) | destiny_domain_verified (D10); blue_complete (B10); release_pipeline (A12) | completion |
| 38 | [A14](../Aegis/14-pervasive-cgp-modernization.md) | aegis_complete (A13); blue_complete (B10); destiny_complete (D11) | modernization |
| 39 | [B11](../Blue/11-pervasive-cgp-modernization.md) | aegis_complete (A13); blue_complete (B10); destiny_complete (D11) | modernization |
| 40 | [D12](../Destiny/12-pervasive-cgp-modernization.md) | aegis_complete (A13); blue_complete (B10); destiny_complete (D11) | modernization |
