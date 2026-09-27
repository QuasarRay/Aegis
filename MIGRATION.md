# Migration to the Candle-only branch

This coordinator replacement is intentionally incompatible with the generic
lifecycle. Old test chronology receipts, policy packs and historical test-count
catalogs are not specification evidence. Their source remains in Git;
`docs/retired-surfaces.json` identifies retired files.

Preserve work in a remote draft PR first. Deploy a reviewed package in a separate
setup commit. Select `gpt-6-astra`, merge the working agreement into target goals,
generate directory instructions, ignore `.aegis/` and `target/`, and start a clean
branch exactly at the intended remote base. Bind a new plan to original HOL names.

Runtime state uses `.aegis/candle/`; legacy `.aegis/tasks/` is untouched and never
automatically imported. Durable evidence packets live in committed
`supervision/checkpoints/<batch>/`. Failed Kani obligations remain unresolved.

Package generation does not install governance into a live project. Codex adapter
installation is a separate explicit maintenance operation that preserves unrelated
configuration. Static model settings do not establish effective host routing.
