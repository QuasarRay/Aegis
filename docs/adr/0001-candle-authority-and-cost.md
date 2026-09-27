# ADR-0001: Specialize Aegis for Candle specification obligations

Status: accepted by the requested branch redesign; implementation is incremental.
Architecture entity: Aegis's Candle-rs development coordinator.

## Stakeholders and concerns

The solo supervisor needs independently rerunnable evidence and durable progress.
The proof engineer needs the exact original HOL contract. The implementing agent
needs small, stable context and low token/credit cost. The future prover user needs
sound theorem construction and observable compatibility.

## Authority and views

The ultimate scientific and architectural reference is [Candle: A Verified
Implementation of HOL Light](https://doi.org/10.4230/LIPIcs.ITP.2022.3), ITP 2022,
by Abrahamsson, Myreen, Kumar and Sewell. Sections 2–5 distinguish kernel/value
invariants, protected theorem output, interactive execution safety and compilation.
The original end-to-end result applies to the original system; a Rust port needs
its own checked connection.

The mathematical-contract view uses the original HOL4 files without a new syntax
or independently redefined semantics. `contracts/candle/authority.json` pins their
source revision, Git blob and SHA-256. HOL4 remains their interpreter. Aegis only
indexes and binds source identities; it does not interpret HOL or prove Rust
refinement. Any paper/source discrepancy blocks the affected obligation.

The work view is: bind named obligations, inspect reuse/generation candidates,
implement, collect relevant evidence, publish a stacked checkpoint. OPEN replaces
the prerequisite of manufacturing a failing test. The evidence view distinguishes
implementation, auxiliary examples, bounded Kani results and unbounded refinement.

## Alternatives and rationale

Keeping the generic TDD engine behind a profile switch leaves hidden mandatory
gates, large contexts and two competing authority systems. Renaming RED to OPEN
without changing execution predicates preserves the same problem. This branch
therefore replaces the TDD coordinator while reusing Aegis's existing process,
filesystem, transaction and locking primitives. Generic infrastructure checks
remain useful when they exercise retained behavior; their historical count is
not a completion gate for Candle work.

No optional performance, readability, idiomaticness or concurrency campaign is
required. Verification budgets and content-bound result reuse control repeated
cost. A reliable direct implementation may cost less than new metaprogramming;
the reuse decision must record that tradeoff before authoring it.

## Correspondence and consequences

Each task names pinned HOL definitions and a reuse decision. Every proof result
names the source, verifier, bounds and obligation inventory. Each completed batch
has a remote commit and stacked PR; publication may preserve failed proof work.
Generated instruction copies and distributions must agree with their source.

This uses ISO/IEC/IEEE 42010 architecture-description concepts, without asserting
certification or complete standard conformance. Policy files, adapters and local
receipts remain untrusted against an agent that controls the same OS account.
Independent checkout, rerun and human review remain necessary.

## Open obligations

The complete HOL4 environment and Rust refinement bridge are not provided by this
coordinator. Pinning three source theories is not whole-system specification
coverage. Model selection must be confirmed by the host; configuration alone
does not prove effective routing. Old task receipts must not be imported as new
specification evidence.
