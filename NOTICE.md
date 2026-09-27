# Reused sources

The original Aegis source at commit
`01060f8d731e0e9082a555bc23f47810aa9eec51` is the starting point. Its atomic
filesystem, process, locking, transaction, path and Codex configuration code is
reused rather than reimplemented.

`contracts/candle/upstream/` contains byte-identical CakeML source and its BSD
license. The original paths, revisions and hashes are in `authority.json`.
These are the same pinned mathematical files used by the Candle-rs foundation.

The Candle paper is linked and attributed in ADR-0001. It is the ultimate
scientific reference, not a transferred correctness proof for this framework.

Kani and Verus are external tools. Prefer their original macros, models,
libraries, qualification examples and supported tooling to locally invented
boilerplate; retain their notices when code is copied into the target project.
