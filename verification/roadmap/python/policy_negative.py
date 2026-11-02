"""Deliberately wrong assertion for the original admitted budget example.

The backend must actually reject this assertion. Parse/type/import failures are
unsupported qualification results and never count as detecting the false claim.
"""
from nagini_contracts.contracts import Assert
from agentinfra.roadmap_policy import may_reserve


def deliberately_wrong_budget_assertion() -> None:
    allowed = may_reserve(2, 3, 4, 9)
    Assert(not allowed)
