# Aegis for Candle-rs

Implement the user's Candle-rs objective. The authoritative scientific reference is
*Candle: A Verified Implementation of HOL Light*, ITP 2022,
DOI 10.4230/LIPIcs.ITP.2022.3. Read `contracts/authority.json` and the relevant
obligation before changing behavior. Original HOL4 specification files are the
shared application contract; preserve their bytes, syntax, semantics, and assumptions.
The paper guides interpretation. If paper, pinned sources, and intended behavior
conflict, record the discrepancy; do not invent a replacement specification.

- Implement Candle in Rust, proving refinement of the original specifications.
  Kani checks bounded Rust obligations; Verus can establish deductive obligations.
  Neither a test nor a successful process exit alone proves semantic equivalence.
- Use existing code first, reliable generation second. Handwrite only if reuse or
  generation is unavailable or demonstrably costs more. Record source, license,
  generation recipe, and the reason once per work item. Reuse Verus/Kani boilerplate.
- Prefer metaprogramming that removes repeated implementation and proof work.
- Do not require RED/GREEN cycles, failing tests before edits, or test-first timing.
  Mathematical contracts determine correctness. Retain useful counterexamples.
- Spend tokens on correctness, coverage, and human supervision. Do not impose
  readability, idiomaticness, performance, output-speed, or concurrency work.
- Configure requested model `gpt-6-astra` (GPT 6 Astra); report host limitations
  truthfully. Configuration is not evidence of the model that actually ran.
- Keep small ISO/IEC/IEEE 42010-informed architecture decision records with concerns,
  alternatives, decision, consequences, contract links, and unresolved assumptions.
- Preserve unrelated work. Never fabricate verification, approval, or remote state.
- Commit and publish a stackable PR after each bounded development cycle, including
  blocked work. Verify remote commit and PR head before starting the next cycle.
  Record base/head/parent PR and exact evidence so another engineer can resume.
- Human engineers must be able to rerun checks independently. Hashes detect changes;
  they do not make agent-authored claims trustworthy. Keep the trust boundary explicit.
- Generate AGENTS.md in every tracked source directory. Do not copy instructions into
  external reference checkouts, Git internals, build products, or runtime state.

`docs/architecture/0001-candle-contract-control-plane.md` defines the branch redesign.
The previous general-purpose TDD controller is being replaced, not carried forward
as a second optional workflow. No automatic delegation is required.
