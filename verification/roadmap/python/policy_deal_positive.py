"""Exact six fixed cases from test_roadmap.py::DomainPolicyTests::test_budgets_and_completion.

This imports maintained production bodies. It is an unqualified ingestion trial,
not a full-domain harness or an approved original-to-contract translation.
"""
from agentinfra.roadmap_policy import all_satisfied, cgp_eligible, may_reserve


def original_budget_and_completion() -> None:
    allowed = may_reserve(2, 3, 4, 9)
    assert allowed
    over = may_reserve(2, 3, 5, 9)
    assert not over
    boolean = may_reserve(True, 0, 1, 9)
    assert not boolean
    empty = all_satisfied([], [])
    assert not empty
    incomplete = all_satisfied(["impl", "proof"], ["impl"])
    assert not incomplete
    modernize = cgp_eligible(dict(Aegis="PROJECT_COMPLETE", Blue="PROJECT_COMPLETE", Destiny="DOMAIN_VERIFIED"))
    assert not modernize
