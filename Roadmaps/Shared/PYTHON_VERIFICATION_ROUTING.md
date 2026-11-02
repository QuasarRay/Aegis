# Python production-verification routing

This decision consumes both the original supplied Python report and the later `python_rust_formal_verification_research_fixed.zip`. The user explicitly does not guarantee the archive's claims. Retain its recovery notes, original report, citations and every chapter unchanged. Research rankings and example commands are candidate inputs, not accepted tool capabilities or execution recipes.

## Route each actual obligation

1. Inventory the maintained production function and its full import/call/state closure. Bind the Aegis requirement, original-test closure where applicable, production source/AST digest, interpreter version, inputs, outputs, exceptions, mutations and ownership boundaries. Use the complete Python inventory; selecting easy functions does not remove difficult required obligations.
2. Classify the actual semantics: pure arithmetic/Boolean logic; containers and mutation; object/alias/exception behavior; serialization/FFI boundaries; or filesystem/process/native transport. Separate pure domain rules from necessary runtime integration tests without replacing production logic with an unused model.
3. Try a qualified deductive route for the supported production subset. Nagini remains a primary candidate. Evaluate Deal/deal-solver for small supported pure functions as a complementary candidate. Backend qualification must establish actual code ingestion, language/version support, assumptions, reproducibility, counterexamples and the strength of the result before acceptance.
4. Use a qualified ESBMC Python route when its supported semantics and explicit bounds faithfully represent the required domain. Distinguish exhaustive finite-domain evidence from bounded bug finding. Never choose smaller ranges merely to obtain success.
5. Treat Apex as a bounded qualification experiment for supported pure code and proof-review workflow. Its Lean result cannot stand in for production Python proof when source/model correspondence is supported only by sampled fidelity. Require an accepted semantic translation/linkage argument and backend qualification; otherwise retain the result as model evidence. Keep its automatic fuzzing and TLA+ routes disabled under the adopted phase policy. Use deterministic mode or the controlling Codex agent; do not launch a second model process or another provider.
6. Use CrossHair with explicit contracts for counterexamples when justified and authorized. Runtime contract checks, Hypothesis, type checkers, fuzzing, sampled equivalence and a no-counterexample result do not satisfy a required domain-proof gate.
7. Investigate applicable supported alternatives, then prepare a specific human engineering packet for unresolved semantics. Record attempted route, exact limitation, counterexamples, required behavior and proposed repair. Continue independent work. No unsupported result, tool skip, absent result or unresolved decision becomes completion.

## Qualification record and promotion gate

For each selected backend, record executable/package/source hash, interpreter and solver versions, supported operations, actual production target/import closure, specification origin and semantic review, numeric/container/exception assumptions, bounds, assertion and reachability identities, complete result/log artifacts, counterexamples, trusted translation boundary and qualification fixtures. Include both successful and deliberately failing actual production examples. Ensure tool skipping, unsupported constructs, stale imports, empty properties and missing covers are rejected.

Promotion requires a current reviewed qualification record for the exact backend/configuration and an evidence adapter that preserves its actual result strength. The package's admitted proof-backend names do not themselves qualify an installation. Additional candidate names remain outside the proof-acceptance path until A09 implements and qualifies their adapter. No newly suggested backend receives proof credit in this delivery.

The decision matrix is maintained in `python-backends.json`. A09 must record a per-obligation route and every unresolved coverage gap. A13 cannot complete until all required Python domain obligations are accepted; report recommendations to verify only easy or critical subsets do not amend that denominator.

## Primary-source checks on the later archive

The Apex repository calls the tool a research prototype. It distinguishes Lean-model proof, bounded model checking, fuzzing and gaps; its proof verdict also involves sampled comparison with the real implementation. That is insufficient by itself to establish Python/model equivalence under this roadmap. Its optional provider invocation also needs explicit single-agent/Codex controls. See the [Apex repository and verdict definitions](https://github.com/hyperionaidev/apex).

Deal documents restricted pure-function support, possible unsupported skips, and limitations involving mutation. Qualify the exact supported production kernel and reject skipped cases. The documented command is `python3 -m deal prove`, so the report's shorthand is not an executable recipe. See [Deal verification documentation](https://deal.readthedocs.io/basic/verification.html).

Certora's announcement concerns Solidity, with Rust described as forthcoming; it supplies no qualified Python route. Keep AutoProver outside current Python acceptance. See [the vendor announcement](https://www.certora.com/blog/autoprover-agentic-formal-verification).

The archive's “strongest”/“most mature” ranking, easy-install claims, universal multilingual composition claims and example verdicts are not adopted. Prusti/Verus/Creusot do not replace the user-selected Kani-first Rust policy. Separate Python/Rust checks also do not prove a composed FFI boundary: explicitly preserve value representation, errors, lifetime, aliasing, serialization and cross-language call/return contracts.

## A09 executable qualification groundwork

The fixed `python.route`, `python.toolchain` and `python.qualify` recipes run through the existing typed work, native owner, lease, reservation and process supervisor. `scripts/roadmap_python.py` implements these producers. Retrieved commands and JSON cannot supply executable argv. The selected Nagini 1.3.1 wheel, complete wheel dependency closure and Temurin 17 JRE are pinned by URL, byte length and SHA-256 in `python-toolchains.json`. Installation is private to `.aegis/toolchains`; host packages and system networking are not changed.

`python.route` retains both reports, all 13 archive members, 24 recommendation decisions, every maintained Python behavioral unit, the complete Aegis domain-obligation denominator and static original-test locations. An unassigned production target or dynamic fixture occurrence is explicitly unresolved. Whole transitive local modules and package initializers remain in the candidate closure, including private and unused code. Static closure does not certify dynamic dispatch or external module semantics.

The qualification harnesses in `verification/roadmap/python` import unchanged `agentinfra.roadmap_policy` production functions. The positive harness preserves the fixed budget/completion examples in `DomainPolicyTests.test_budgets_and_completion`; the negative control deliberately reverses the first assertion. These fixed examples establish neither full input quantification nor accepted original-test translation. A parse, type or import error in the negative control does not count as detecting the false assertion.

The initial adapter classifies raw Nagini observations conservatively and retains full logs. It does not implement an accepted domain-proof producer. Both the shared evidence audit and standalone verification audit reject Python proof claims until a source-bound execution/result adapter and its supported production semantics are qualified. Changing a matrix status or supplying a successful-looking `PROVED` JSON cannot grant proof credit. ESBMC/Deal qualification and the other retained routes remain A09 responsibilities. No required domain obligation is closed by this groundwork.
