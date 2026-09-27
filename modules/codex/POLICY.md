# Codex adapter policy

The intended model for the parent and any explicitly authorized child is
`gpt-6-astra`, with `max` reasoning. Configuration is not evidence of host routing.
Report actual host metadata or UNAVAILABLE; never silently substitute a model.

The workflow does not require or initiate delegation. Four optional roles remain:
researcher, implementer, verifier and adversarial reviewer. A user-authorized child
has a bounded assignment and cannot delegate. There is no legacy lease service.
The retained static adapter limits capacity where the host honors its configuration;
it is not a live concurrency guarantee. No parallelism campaign is required.

The ordinary Candle CLI does not install configuration. Existing install/uninstall
helpers are retained for explicit maintenance and recovery, preserve unrelated
settings, and reject conflicting managed values. Deployment authorization comes
from the user's task, not a blanket restriction on using those helpers.
