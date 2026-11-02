"""Finite runtime checks of actual production policy functions.

These are useful executable qualification fixtures, not a formal proof result.
Selected Python verifiers must qualify these imports and their semantic domains.
"""
from itertools import product
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.roadmap_policy import all_satisfied, may_reserve, cgp_eligible


def finite_policy_checks() -> int:
    checked = 0
    for used, reserved, requested, limit in product(range(-1, 6), repeat=4):
        allowed = may_reserve(used, reserved, requested, limit)
        assert not allowed or min(used, reserved, limit) >= 0
        assert not allowed or requested > 0 and used + reserved + requested <= limit
        checked += 1
    for states in product(("PROJECT_COMPLETE", "IMPLEMENTATION_READY", "DOMAIN_VERIFIED", "UNKNOWN"), repeat=3):
        mapping = dict(zip(("Aegis", "Blue", "Destiny"), states))
        assert cgp_eligible(mapping) == all(x == "PROJECT_COMPLETE" for x in states)
        checked += 1
    assert not all_satisfied([], [])
    assert not all_satisfied(["implementation", "proof"], ["implementation"])
    return checked + 2


if __name__ == "__main__":
    print(f"{finite_policy_checks()} finite production-policy runtime scenarios passed; FORMAL_PROOF_NOT_RUN")
