# Behavioral Law Protocol (Karpal-inspired)

A law is an implementation-independent invariant of externally observable behavior. Laws are stronger
than example tests: implementations may change, but the law should remain true unless the contract itself
changes deliberately.

## Law anatomy

Every project law should name:

- stable unique ID;
- behavior/invariant in plain language;
- observation boundary (public API, CLI, FFI, process, file format, protocol, etc.);
- falsifier: what observable result would disprove it;
- severity (`hard` by default);
- optional tags;
- reproducible command or comparison where possible.

The built-in runner supports `file_exists`, `file_contains`, `file_not_contains`, `regex`, `command`,
`json_command`, `command_sequence`, and `differential_json`. Complex properties should normally live in
project-owned test binaries/scripts and be invoked by a `command` law so the generic framework does not
learn project internals.

`command_sequence` is for lifecycle/state-transition contracts. `differential_json` is for comparing a
replacement against an authoritative oracle on selected observable fields.

## Integrity rules

- Law definitions and acceptance tests are read-only specifications during implementation.
- Never weaken, skip, rename, filter, monkey-patch, or special-case them to manufacture a pass.
- Production behavior must not inspect law IDs, test names, call stacks, fixture names, or harness markers.
- Test-only code must not substitute for the production path being claimed.
- The runner hashes law definition files before and after execution and fails if they change.
- Commands run with common test-identifying environment variables removed where practical.
- Hidden-test mindset: a fix must generalize to new inputs, orderings, counts, timing, and state histories.

## Project laws

Put project-specific TOML law files under `.agents/laws/project/` (normally committed) or pass explicit
law paths to `agentctl law run`. Law definitions are trusted project code because command laws may execute
programs; review new or externally supplied law files before running them.

Prefer laws at stable boundaries. A scheduler law should say that a completed task cannot become runnable
again, not that an internal vector has a particular length. A compatibility law should compare public
outputs or semantics, not private representations.

## Python law helpers

For project-owned Python law suites, import `agentinfra.lawlib` (or place `.agents/infra` on `PYTHONPATH`).
Its stdlib-only helpers cover determinism, idempotence, round trips, commutativity, associativity,
monotonicity, conservation, differential equivalence and invariant-preserving action sequences. These helpers
do not mock production behavior; callers pass real boundary functions/adapters. Deterministic generated cases
should record their seed and failing counterexample in normal project test output.
