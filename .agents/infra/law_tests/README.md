# Comprehensive Aegis law suite

`traceability.json` is the canonical machine-readable mapping from every name in the immutable
`tests-to-impl/` specification to executable coverage. Release-source checkouts keep that
specification at the repository root and mirror it byte-for-byte under `.agents/tests-to-impl/` so
the signed release archive can execute the same completeness law after a clean extraction. It is generated deterministically by
`build_traceability.py`; generation is bookkeeping, not proof that a law passed.

The executable suite has three layers:

1. focused production-path tests under `infra/tests/`;
2. semantic family batteries under this directory;
3. an outer acceptance runner that records collection, start, completion, capability, outcome,
   oracle count, definition digests, and representative mutation results.

Exact-name adapters are permitted to share a family battery only when the registry marks the mapping as
a stronger equivalent and the battery exercises the named observable boundary.  A collected name with no
started/completed record, a zero-oracle result, an unexpected skip, or a changed specification/test digest
is an acceptance failure.

Capability and outcome are separate.  In particular, unavailable live Codex, Xonsh, optional Python-meta,
or foreign-platform probes are never reported as passing portable laws.
