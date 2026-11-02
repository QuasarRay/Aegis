"""Original fixed budget/completion examples against unchanged production imports.

Origin: infra/tests/test_roadmap.py, DomainPolicyTests.test_budgets_and_completion.
This is an ingestion/qualification fixture. It does not quantify the full domain
and has no accepted original-to-harness semantic translation review.
"""
from nagini_contracts.contracts import Assert
from agentinfra.roadmap_policy import all_satisfied, cgp_eligible, may_reserve


def original_budget_and_completion() -> None:
    allowed = may_reserve(2, 3, 4, 9)
    Assert(allowed)
    over = may_reserve(2, 3, 5, 9)
    Assert(not over)
    boolean = may_reserve(True, 0, 1, 9)
    Assert(not boolean)
    empty = all_satisfied([], [])
    Assert(not empty)
    incomplete = all_satisfied(["impl", "proof"], ["impl"])
    Assert(not incomplete)
    modernize = cgp_eligible(dict(Aegis="PROJECT_COMPLETE", Blue="PROJECT_COMPLETE", Destiny="DOMAIN_VERIFIED"))
    Assert(not modernize)
