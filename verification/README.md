# Controller deductive verification

`control.rs` is a Verus model with executable reservation and decision functions,
plus deductive lemmas. It has no admitted obligations, external bodies or weakened
verification settings. `scripts/check_formal.py` uses `--no-cheating`, one verifier
thread, exact positive result counts, a pinned version and a 60-second total budget.
It checks the input and selected tool-distribution hashes before and after execution,
reserves attempts durably, and writes a complete bounded receipt under `.aegis/`.

| Invariant | Entry points |
| --- | --- |
| Successful reservations increase both counters without overflow and stay within their declared maxima; rejected inputs do not reserve. | `reserve`, `may_reserve` |
| Exhausted attempts/time cannot reserve again. | `exhausted_budget_cannot_reserve` |
| A prior/interrupted attempt requires diagnosis; restart cannot erase consumed work. | `restart_does_not_refund` |
| Report reuse requires matching source, recipe, tools and environment, a deterministic successful result, and no proof request. | `reuse_report` |
| Scoped success requires fresh, unchanged, declared, exact, positive inventory with no failure, timeout, truncation or errors. | `accept_scoped`, `scoped_success` |
| Cache hits and zero-obligation output cannot discharge a proof. | `cached_result_cannot_discharge_proof`, `vacuous_result_cannot_discharge_proof` |
| Completion requires a nonempty set of checked obligations. | `all_checked` |
| Selecting the same obligation twice adds no new work. | `duplicate_selection_is_idempotent` |

The executable functions and lemmas produce ten checked Verus obligations with the
toolchain in `toolchain.json`. This pin is for the controller model. Destiny's reviewed
CI has a separate, newer Verus pin in `modules/destiny/profile.toml`; one cannot stand in
for the other. A toolchain change requires explicit review and a fresh observation.

## Abstraction and trusted boundary

The Python runner currently implements the corresponding policy independently. There
is **no proved refinement from Python to this Rust model**, and the Rust functions are
not called by the Python runtime. In particular, the model does not prove filesystem
atomicity, concurrency, subprocess isolation, receipt authentication, parser completeness,
source hashing or the truth of externally supplied Boolean observations. The ledger must
really be persisted before launch for the restart argument to apply. Plan-set idempotence
does not by itself prove the Python dependency traversal complete.

Verus, its Rust toolchain, Z3, vstd and its trusted specifications form the proof toolchain.
The receipt records selected distribution components, not an attestation of every dynamic
library, operating-system service or compiler dependency. Controller regression checks
exercise the real public interface and error paths separately; they do not close these
formal correspondence gaps. Likewise, this model establishes nothing about Destiny's
physics, networking, FFI, original engine, or Rust/Python semantic equivalence.
