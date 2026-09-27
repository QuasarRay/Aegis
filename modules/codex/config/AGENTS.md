Project Goals:

1. Reimplement Candle in Rust and formally verify its source code Rust implementation to behave identically to the intended specification.

2. Create Supervision Infrastructure so for Human Engineers to be capable of independently verify what untrusted AI Agents implemented.

3. Use metaprogramming to the fullest potential.

4. Initially sacrifice performance optimization and code readability and idiomaticness in favor of reliability, faster development cycles, and preventing wasted credits/tokens

5. prefer code reuse over implementing from scratch. Reuse Boilerplate from the source codes of Verus and Kani to prevent tokens/credits from being wasted, and to accelerate development cycles.

6. prefer machine generated code over direct implementation.

7. use strong ISO Architecture Description Records to reduce token/credit of AI agents from being wasted, and make it possible for a solo human engineer to efficiently supervise a project scope larger than what is normally done by solo developers.

8. this AGENTS.md file should exist at every directory in the project repository.

9. Reuse mathematical specifications from Original Candle, while Rust implements those specifications. Also allow the scientific paper of Candle to guide you in the process of developing the Rust implementation. Treat the Original Candle's mathematical specifications as shared contract between Original Candle and Candle-rs. Both projects should understand the exact same specification files exactly in the same way and the same manner. therefore, the specifications share syntax as well as semantics.

10. use Kani to prevent mistakes from happening from the first time, prevent repeating a mistake that has been made, and as a means of human supervision. Also prevent progress from being lost by making stackable pull requests incrementally. Turn my github account into your workspace.

The Original Candle Github Repository: "https://github.com/CakeML/candle.git"

Target Project Repository: "https://github.com/QuasarRay/Candle-rs.git"

## Aegis Candle branch working agreement

- This branch specializes Aegis for Candle-rs. Read INDEX.md, contracts/candle/authority.json
  and the relevant ADR. The Candle paper is the ultimate scientific/architectural
  reference; the original, byte-identical HOL4 files are the mathematical contract.
  Resolve any disagreement explicitly; never silently redefine either authority.
- Work from named original HOL definitions. An unimplemented obligation is OPEN;
  no failing test, property-testing campaign or RED/GREEN chronology is needed to
  authorize implementation. Auxiliary tests may diagnose and prevent regression.
- Record reuse candidates first: upstream Candle/CakeML, Kani, Verus and existing
  Rust components. Prefer copying compatible licensed code or reliable generation.
  Handwritten code requires a recorded reason: no suitable reusable source, no
  reliable generation, or lower expected token/credit cost. Do not implement a
  generator where a smaller direct implementation costs less.
- Ultimately check Rust-to-contract refinement in Original Candle itself. Every
  batch must assess its proof replay, theorem-producing computation and code
  generation at the pinned revision; use them when they save tokens/credits.
  HOL4 scripts and Candle's HOL Light frontend are distinct interfaces. Preserve
  the original specification bytes and prove any semantic bridge. A generated
  model, printed theorem, added axiom or successful process exit is not evidence
  that the actual Rust source refines those specifications. Keep the final claim
  OPEN until Rust semantics, contract correspondence, assumptions and original
  Candle replay are independently checked against the exact implementation.
- Use GPT 6 Astra (gpt-6-astra). Do not silently select another model. Model
  configuration expresses intent; report actual host capability accurately.
- Minimize tokens, credits, repeated context and redundant checks. No mandatory
  readability, idiom, performance, concurrency, benchmark or cosmetic campaigns.
  Retain correctness and evidence integrity. Add concurrency only when the actual
  Candle contract requires it, not as a generic engineering preference.
- Reuse bounded process capture, path confinement, atomic writes and locks already
  in Aegis. Kani checks actual Rust under declared bounds. A timeout, unavailable
  checker or missing result stays unresolved. Tests and bounded checks cannot
  establish unbounded HOL refinement or machine-code soundness.
- Preserve work in small commits and stacked draft PRs. Before another obligation
  batch, publish the current checkpoint even when a proof remains incomplete.
  Record the parent branch, remote commit and PR. Never merge or force-push without
  explicit authorization. Keep unproved claims visible in checkpoint descriptions.
- Record architecture decisions using ISO/IEC/IEEE 42010 concepts: stakeholders,
  concerns, views, correspondence, alternatives, rationale, trust and open gaps.
- Root AGENTS.md is canonical; generate identical copies in every source directory.
  Git metadata and ignored build/runtime output are excluded. Existing upstream
  specification bytes and license notices must remain unchanged.
- No automatic delegation. If authorized and useful, allow only one child at a time
  with a bounded context, no nested delegation, and a checkpoint before handoff.
- This framework is an auditable coordinator, not an operating-system sandbox or
  a proof checker for its own reports. Never claim execution or proof from an
  agent-authored success flag. Report actual commands, identities, results and gaps.
