# Codex adapter

Optional GPT 6 Astra configuration for the Candle workflow. See POLICY.md.
`python3 modules/codex/verify.py` checks managed source and any existing project
configuration. It does not prove effective live model selection or sandboxing.

The retained install/uninstall helpers use Aegis filesystem transactions and
recovery metadata under `.aegis/state/install-state`. Invoke them only for an
explicit configuration task. The Candle CLI does not discover or auto-install
modules. No deleted lease, TDD or generic role service is required.
