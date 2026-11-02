# Branch and component reuse

Snapshot: 2026-11-02. See [machine inventory](branch-inventory.json) for all 31 local/tracking refs, 27 live remote heads, 26 unique trees and 131 unique Python component blobs. Identical blobs are inspected once. Original commits and main remain untouched.

- `infra/agentinfra/atomic.py`: reuse unchanged. Retain working durable atomic writes. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/transaction.py`: reuse unchanged. Retain working journaled compare-and-swap transactions and recovery. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/locks.py`: reuse unchanged. Retain working nonce and process-identity locks. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/process.py`: reuse unchanged. Retain working bounded process-group supervision. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/security.py`: reuse unchanged. Retain working confined paths. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/context_cache.py`: reuse unchanged. Retain working bounded context receipts. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/catalog.py`: reuse unchanged. Retain working fixture-qualified source catalog. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/formal.py`: reuse unchanged. Retain working exact existing verification runner. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/evidence.py`: reuse unchanged. Retain working existing evidence parser. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/verus_evidence.py`: reuse unchanged. Retain working historical verifier parser without mandatory adoption. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/coverage.py`: reuse unchanged. Retain working source/evidence coverage. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/destiny_reuse.py`: reuse unchanged. Retain working branch/source reuse. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/destiny.py`: reuse unchanged. Retain working legacy CLI behavior under compatibility dispatch. New roadmap modules compose these facilities; old acceptance semantics stay scoped.
- `infra/agentinfra/governance.py`: reuse unchanged. Retain working deployment write boundaries. New roadmap modules compose these facilities; old acceptance semantics stay scoped.

`cli.py` is adapted through family dispatch. New modules extend policy, roadmap, native observations, knowledge, review and migration documentation. Historical Candle/MetaRocq/Destiny branches are retained by exact commit and component hashes; they are not silently adopted as universal policy. Their AST signatures are inventoried for bounded future reuse. A00 must inspect any candidate body before superseding a working component. This snapshot does not claim semantic acceptance of all branch variants.
