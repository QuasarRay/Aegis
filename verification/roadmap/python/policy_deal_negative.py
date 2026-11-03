"""Deliberately wrong original admitted-budget assertion; unsupported is not detection."""
from agentinfra.roadmap_policy import may_reserve


def deliberately_wrong_budget_assertion() -> None:
    allowed = may_reserve(2, 3, 4, 9)
    assert not allowed
