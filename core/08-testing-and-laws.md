# Testing and Law Integrity

Tests and laws are executable contracts, not obstacles.

Never weaken assertions, skip discovery, detect test names, fabricate counters, add production
branches that only behave correctly under tests, or hardcode visible fixtures.

A pre-existing test/law may change only for an intentional contract change, demonstrably stale or
incorrect expectation, strengthening coverage, or explicit higher-priority instruction. Record why.

## Karpal-inspired laws

Prefer laws for invariants that should survive implementation changes: state conservation,
identity, ordering, monotonicity, idempotence, boundedness, round-trip, cleanup, compatibility,
and behavior under varied inputs/sequences.

Use `.agents/laws/` and `agentctl law run`. The runner fingerprints law definitions before and
after execution; self-modifying law suites fail. Project laws should exercise production paths and
must not rely on a test-identifying environment branch.

Validation ladder: cheapest syntax/type check -> focused reproducer -> module/package -> integration
boundary -> broad CI-equivalent suite. A retry can classify flakiness but does not erase a failure.
