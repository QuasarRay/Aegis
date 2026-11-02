# Evidence and verification contract

The roadmap package is validated by compiler checks, negative scenarios and runtime tests. Those checks do not formally verify Aegis or establish Carbon implementation completion. Product proof and integration work remains in A08–A13, B09–B10 and D10–D11.

## Carbon semantic identity

The evidence chain is **original test → semantic contract → harness representation → actual production path → verifier result**. Every link has an identity and review status. Preserve the complete fixture closure: setup, teardown, constants, generated inputs, ranges, quantification, helper implementations, imported assertion behavior, call order, state transitions, partial effects, expected values, exceptions and failure conditions. Preserve widths, overflow, narrowing, NaN, signed zero, ordering, identity, aliasing, lifecycle, rounding and original tolerances.

Each occurrence is fixture-, parameter- and configuration-qualified. Duplicate method names do not merge tests. Fixed scenarios remain fixed; generalizations are additional obligations. A stronger-looking property, approximate tolerance, altered setup or narrowed domain cannot replace an original case. Source review and identical declared semantic records do not independently prove arbitrary program equivalence: extraction adequacy and harness-to-production linkage require their own evidence.

Classify concurrency-focused tests using actual assertions and dependencies. Retain applicable unchanged original concurrency tests. Mixed domain/concurrency cases retain their domain obligations. Formal concurrency and performance campaigns are deferred.

## Rust backend qualification

Kani recipes select exact harnesses and bind current production bodies, dependencies, generator inputs, compiler configuration and toolchain. Require the intended assertions and relevant successful reachability witnesses. Reject absent results, failed assertions, unsupported operations, model-only targets, incomplete unwinding, timeout, truncation, interrupted execution and stale inputs. Preserve counterexamples and all introduced assumptions/bounds. An assumption that excludes a valid original input invalidates semantic identity.

Bolero/Kani still invokes Kani. Its explicit validity coverage and bounded byte generation must match the original input domain. It cannot provide an escape from unsupported Kani semantics. Inspect the pinned [engine](https://github.com/camshaft/bolero/blob/master/lib/bolero-kani/src/lib.rs) and [invocation](https://github.com/camshaft/bolero/blob/master/bin/cargo-bolero/src/kani.rs); record limits per obligation rather than assuming the current upstream representation.

After applicable supported routes have been investigated, retain unresolved obligations and request a specific human engineering decision. Continue independent work. Human intervention cannot label a failed solver result as proof or silently remove a required responsibility.

## Python report disposition

The supplied `Python_Verification_Research_Report_v1.md` has arrived and is pinned unchanged. Backend **selection recommendations** below are adopted for qualification. Actual production proof qualification remains open; the current interpreter is Python 3.14 and compatibility must be demonstrated rather than inferred from report claims.

| Candidate | Disposition | Qualification needed |
|---|---|---|
| Nagini | Primary deductive candidate for suitable typed production kernels | Pin a supported Python/toolchain version; validate actual functions, exceptions, aliasing, containers, loops, contracts and Viper trust boundary. The maintained changelog reports Python 3.9–3.12 support, so the report's broader interpreter claim is not accepted without evidence. |
| ESBMC Python frontend | Complementary bounded candidate | Pin frontend/build flags, actual production imports, integer/object semantics, bounds and counterexamples. Establish whether each claim is exhaustive within a declared finite domain or only bounded bug finding. The documented frontend invokes `esbmc file.py`; unverified report commands are not executable recipes. |
| CrossHair | Contract exploration and counterexample diagnosis | Import actual side-effect-bounded production kernels with explicit contracts. No counterexample found is not unrestricted proof; a success cannot satisfy `full_domain_proof`. |
| PyVeritas | Deferred from acceptance-critical path | LLM-produced translation introduces semantic/provenance and cost obligations. Reconsider only after independent source-to-target equivalence and measurable benefit. |
| Dafny-of-Python | Research only | Qualify translator support, source linkage and unsupported features before any proof credit. A translated Dafny model alone is not proof of maintained Python. |

Primary sources used to assess these claims: [Nagini](https://github.com/marcoeilers/nagini), [Nagini changelog](https://github.com/marcoeilers/nagini/blob/master/CHANGELOG.md), [ESBMC Python frontend](https://github.com/esbmc/esbmc/blob/master/src/python-frontend/README.md), [CrossHair contracts](https://crosshair.readthedocs.io/en/latest/contracts.html). These are qualification inputs; pin exact versions at A09 before execution. No backend is installed or proved merely by appearing in this table.

The shared interface records production target, original/requirement origin, semantic domain, assumptions, bounds, backend/version, assertions, reachability, command, result and limitations. Refactor only when production behavior is preserved; do not create an easier duplicate model and call it production verification. The included finite production-policy harness exercises actual policy functions and explicitly reports runtime evidence only.

## Aegis domain obligations

1. Missing required obligations prevent milestone completion.
2. Implementation receipts cannot satisfy domain proof gates.
3. Scope amendments cannot silently remove source responsibilities.
4. Duplicate operations cannot receive another reservation without distinct authorized work.
5. Restart cannot erase spent attempts, failures or uncertain operations.
6. Reuse requires the complete relevant input identity.
7. Changed semantic inputs invalidate human review.
8. Canonical many-to-one source/target ownership fails correspondence.
9. Unsupported or diagnostic backend results cannot become proofs.
10. Rejected or unknown native transitions cannot confirm completion.
11. Unauthorized policy/model/reasoning downgrades cannot enable dispatch.
12. CGP modernization cannot start before the three-project barrier.

Formal checks must state exactly which pure production rules and domains they establish. Runtime tests remain necessary for filesystem atomicity, process supervision, locks, recovery, native transport, installed artifact identity and concurrency. Formal model results cannot substitute for these actual integration checks.

## Acceptance strength and coherent candidate

Keep source review, structural reconciliation, compilation, original-test execution, reviewed translation identity, mechanically established properties, packaging and publication separate. A receipt binds semantic inputs and actual outputs; the producer/parser and human provenance are explicit trust boundaries, not self-authenticating strings.

Carbon completion requires complete source/body/configuration coverage, bidirectional object/relationship correspondence, every actual implementation responsibility, production builds, installed/loaded identities, full applicable original-test execution, accepted test-to-harness identity, current production-linked domain proofs, concurrency original-test acceptance, no unresolved required human decision, reproducible packages, portable-core boundaries, accurate architecture, verified publication and canonical/native closure. All evidence must describe the same accepted candidate.

## Later supplied Python/Rust archive

The user supplied a recovered archive without guaranteeing its claims. [Python verification routing](PYTHON_VERIFICATION_ROUTING.md) records the resulting obligation-by-obligation procedure, primary-source corrections and backend qualification gates. [Archive dispositions](python-rust-research-dispositions.json) retain all 13 members and 24 explicit recommendations. Nagini/ESBMC remain qualification candidates; Deal is a complementary candidate; Apex is a bounded experiment with an explicit production-translation barrier. No new backend is qualified by this research update.
