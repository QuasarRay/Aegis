use vstd::prelude::*;

verus! {

// Deductive control model, not a claim of refinement to the Python runtime.
// The authority for booleans representing external observations is outside this model.
pub open spec fn may_reserve(
    attempts: int, max_attempts: int, spent: int, total: int,
    request: int, diagnosed: bool,
) -> bool {
    0 <= attempts < max_attempts
    && 0 <= spent <= total
    && 0 < request <= total - spent
    && (attempts == 0 || diagnosed)
}

pub fn reserve(
    attempts: u64, max_attempts: u64, spent: u64, total: u64,
    request: u64, diagnosed: bool,
) -> (r: Option<(u64, u64)>)
    ensures
        match r {
            Some((next_attempts, next_spent)) =>
                may_reserve(attempts as int, max_attempts as int, spent as int,
                            total as int, request as int, diagnosed)
                && next_attempts as int == attempts as int + 1
                && next_spent as int == spent as int + request as int
                && next_attempts <= max_attempts && next_spent <= total,
            None => !may_reserve(attempts as int, max_attempts as int, spent as int,
                                 total as int, request as int, diagnosed),
        },
{
    if attempts >= max_attempts || spent > total || request == 0
        || request > total - spent || (attempts > 0 && !diagnosed) {
        None
    } else {
        Some((attempts + 1, spent + request))
    }
}

pub proof fn exhausted_budget_cannot_reserve(
    attempts: int, maximum: int, spent: int, total: int, request: int, diagnosed: bool,
)
    requires attempts >= maximum || spent == total,
    ensures !may_reserve(attempts, maximum, spent, total, request, diagnosed),
{}

pub proof fn restart_does_not_refund(
    attempts: int, maximum: int, spent: int, total: int, request: int,
)
    requires attempts > 0,
    ensures !may_reserve(attempts, maximum, spent, total, request, false),
{}

pub fn reuse_report(
    same_source: bool, same_recipe: bool, same_tools: bool, same_environment: bool,
    deterministic: bool, success: bool, proof_requested: bool,
) -> (reuse: bool)
    ensures reuse == (same_source && same_recipe && same_tools && same_environment
                       && deterministic && success && !proof_requested),
{
    same_source && same_recipe && same_tools && same_environment
        && deterministic && success && !proof_requested
}

pub open spec fn scoped_success(
    formal_method: bool, fresh: bool, unchanged: bool, exact_entry: bool,
    declared_scope: bool, exited_ok: bool, timed_out: bool, truncated: bool,
    expected: int, observed: int, errors: int,
) -> bool {
    formal_method && fresh && unchanged && exact_entry && declared_scope
        && exited_ok && !timed_out && !truncated && expected > 0
        && observed == expected && errors == 0
}

pub fn accept_scoped(
    formal_method: bool, fresh: bool, unchanged: bool, exact_entry: bool,
    declared_scope: bool, exited_ok: bool, timed_out: bool, truncated: bool,
    expected: u64, observed: u64, errors: u64,
) -> (accepted: bool)
    ensures accepted == scoped_success(
        formal_method, fresh, unchanged, exact_entry, declared_scope, exited_ok,
        timed_out, truncated, expected as int, observed as int, errors as int),
{
    formal_method && fresh && unchanged && exact_entry && declared_scope
        && exited_ok && !timed_out && !truncated && expected > 0
        && observed == expected && errors == 0
}

pub proof fn cached_result_cannot_discharge_proof(
    formal_method: bool, unchanged: bool, exact_entry: bool, declared_scope: bool,
    exited_ok: bool, timed_out: bool, truncated: bool, expected: int, observed: int, errors: int,
)
    ensures !scoped_success(formal_method, false, unchanged, exact_entry, declared_scope,
                            exited_ok, timed_out, truncated, expected, observed, errors),
{}

pub proof fn vacuous_result_cannot_discharge_proof(
    formal_method: bool, fresh: bool, unchanged: bool, exact_entry: bool, declared_scope: bool,
    exited_ok: bool, timed_out: bool, truncated: bool, observed: int, errors: int,
)
    ensures !scoped_success(formal_method, fresh, unchanged, exact_entry, declared_scope,
                            exited_ok, timed_out, truncated, 0, observed, errors),
{}

pub fn all_checked(flags: &Vec<bool>) -> (r: bool)
    ensures r == (flags@.len() > 0 && forall|i: int| 0 <= i < flags@.len() ==> flags@[i]),
{
    if flags.len() == 0 { return false; }
    let mut i: usize = 0;
    while i < flags.len()
        invariant
            0 <= i <= flags.len(),
            flags.len() > 0,
            forall|j: int| 0 <= j < i ==> flags@[j],
        decreases flags.len() - i,
    {
        if !flags[i] { return false; }
        i = i + 1;
    }
    true
}

pub proof fn duplicate_selection_is_idempotent(selected: Set<int>, obligation: int)
    ensures selected.insert(obligation).insert(obligation) =~= selected.insert(obligation),
{}

} // verus!
