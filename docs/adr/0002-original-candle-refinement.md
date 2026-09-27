# ADR-0002 — Original Candle is the final checker

Status: accepted architecture; semantic bridge and checker adapter OPEN.
Supersedes any interpretation of Kani/Verus success as final equivalence.

## Stakeholders and concerns

The solo supervisor needs a reproducible proof about the actual Rust implementation.
Implementing agents need to reuse upstream machinery without inventing another
specification. The user's ultimate checker is Original Candle, guided by the
ITP 2022 paper pinned in ADR-0001. This record uses ISO/IEC/IEEE 42010 concepts;
it is not a certification of conformance to that standard.

## Authority and semantic view

The original HOL4 theory files remain byte-identical. Aegis indexes their named
Definition blocks; it neither parses the complete language nor interprets HOL.
The Candle executable instead exposes its HOL Light frontend and kernel interface.
Loading an original HOL4 Script.sml into that frontend is not an established route.
Any import, encoding or generated bridge must preserve the original syntax and
semantics as the shared contract, with a checked correspondence theorem. A Rust
model written independently in a prover does not establish this correspondence.

Final verification must connect: exact Rust source and its semantics; original HOL4
contract interpreted by its original tooling; a correspondence checked in Original
Candle; complete refinement including error and state behavior; explicit assumptions
and termination; original Candle replay bound to the implementation and checker.
Machine-code correctness is a further claim requiring a compiler connection.

## Reuse and construction view

The pinned CakeML/candle commit exposes `candle/kernel.ml`, `candle/compute.ml`,
`candle/insulate.py`, `candle.sh` and `build-instructions.sh`. Hash-checked copies
and the upstream license are in `contracts/candle/reuse/`. `Kernel.compute` returns
a theorem for reduced cval expressions; it is not a Rust parser or Rust compiler.
Its characteristic equations require exact shape and order. Reuse this primitive
for applicable certificate computation instead of hand-building a redundant engine.
The insulate generator emits CakeML API bindings; reuse it for that purpose, not
as an alleged Rust generator. The CakeML HOL4 monadic translator already generates
CakeML kernel code with supporting proofs; it does not generate Rust.

Every batch must record separate proof replay, metaprogramming and code-generation
assessments for pinned Original Candle. If the assessment says a facility saves
cost, the executable plan validator requires its use. Deferral needs a reason;
free text cannot prove the reason true, so supervisors inspect it. Prefer existing
Rust generators and Kani/Verus macros when applicable. Handwritten glue is allowed
when no reliable reuse/generation fits or direct code uses fewer credits.

## Verification and trust view

Kani checks registered bounded properties of the actual crate. It prevents local
mistakes and provides reproducible regression evidence, but cannot discharge the
unbounded bridge. The current coordinator always reports final refinement OPEN
and full Candle completion false. It accepts no agent-authored proof-success flag.
There is deliberately no adapter that treats exit zero, theorem-looking stdout,
a new axiom or an unrelated theorem as Rust verification. Before enabling final
closure, add and review an adapter with complete statement, source, dependencies,
axiom accounting, checker identity, and independently replayable proof artifacts.

No original Candle executable or complete Rust refinement proof was built as part
of this Aegis specialization. Building the upstream shell script would download an
unpinned compiler archive; qualify and hash that artifact first in a separate
checkpoint. The pinned README also references old compute filenames absent at
that revision; use the checked-in `candle/compute.ml` interface above.

## Alternatives and correspondence

A fresh Rust verifier or specification rewrite would add semantic and maintenance
burden. Blind replay of HOL4 files through Candle would hide an unsupported interface.
A Kani-only completion gate would prove too little. Reusing the original contract,
existing generation and original Candle final checking is the chosen route; the
missing bridge is a blocking proof obligation, not an implicit trusted assumption.

Each checkpoint binds the selected HOL symbols, reuse decision, actual source
snapshot, Kani evidence and this unresolved final-checker route. Update this ADR
and the authority manifest together when reviewed bridge evidence becomes available.
