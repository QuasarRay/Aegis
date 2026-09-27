# Candle source router

Read this once; load only the active obligation's relevant context.

- `contracts/project-goals.md`: the user's goals.
- `contracts/candle/authority.json`: paper and exact original HOL identities.
- `core/candle-workflow.md`: implementation authority and evidence rules.
- `docs/adr/0001-candle-authority-and-cost.md`: architecture, trust and cost decisions.
- `templates/candle-batch.json`: reusable task plan.
- `protocols/CHECKPOINT.md`: durable stacked progress.
- `infra/agentinfra/contracts.py`: definition binding and reuse decisions.
- `infra/agentinfra/candle.py`: runtime, budgets, evidence and checkpoints.
- `infra/agentinfra/verification.py`: bounded Kani execution.
- `docs/retired-surfaces.json`: retired generic machinery and historical blobs.

Tests support evidence. Original mathematical files remain the shared contract.
Instruction copies are generated; do not reread them for duplicate context.
