# Formal-contract migration

This specialized branch adopts the contract-oriented architecture introduced in
`candle/02-contract-runtime` and the stricter evidence/budgeting work through
`metarocq/13-target-adoption`. It replaces the previous general-purpose acceptance
controller and its development-method mandates, policy compiler, catalogs, templates,
installer and duplicated release mirror. Obsolete command entry points no longer exist.
Their implementation remains recoverable in Git at main `01060f8d731e0e9082a555bc23f47810aa9eec51`.

The source checkout is the distribution. Run its CLI against an explicit Destiny root;
no application directory, active .agents tree or host configuration is installed or edited.
Do not run old deployment commands against this version. This avoids distributing a
stale second copy of the retired policies. Runtime state uses .aegis/destiny; old Aegis
acceptance records are not imported or promoted into new proof evidence.

Reusable atomic writes, confinement, process capture, locks and context storage remain.
Their relevant regression checks remain as diagnostics. The new authority is a declared
specification plus actual scoped verification, with fail-closed source/tool binding.
Public decisions capture premises, reuse analysis and proof limits without storing private
reasoning. The change does not weaken Destiny's own CI or alter its source code.

This is a local integrity and economy controller, not a security sandbox. A malicious
same-user process can edit both inputs and receipts; hash seals are not signatures.
TOCTOU and generated-tool dependencies remain operational trust boundaries. Untrusted
repositories must be inspected before executing their build scripts. Full system parity,
FFI safety, foreign implementations and the adequacy of a specification require their
own correspondence obligations. Never infer them from an exit code or a local model.
