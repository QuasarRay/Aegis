"""Deterministic roadmap-package validation; never claims product completion."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.roadmap import compile_roadmaps, audit_evidence, packet
from agentinfra.roadmap_knowledge import validate_skills
from agentinfra.roadmap_records import require


def validate_package(root: Path) -> dict:
    first = compile_roadmaps(root)
    second = compile_roadmaps(root)
    require(first == second, "compiler is nondeterministic")
    audit = audit_evidence(root, first, {"schema": 1, "compiled_digest": first["digest"], "receipts": []})
    for ident in first["order"]:
        require(audit["milestones"][ident]["state"] != "SATISFIED", "empty evidence granted product credit")
        packet(first, audit, ident)
    skills = validate_skills(root)
    return {"schema": 1, "status": "PASS", "scope": "roadmap package compiler and packaging",
            "milestones": len(first["milestones"]), "requirements": len(first["requirements"]),
            "skills": skills["skills"], "compiled_digest": first["digest"], "product_completion": False}


if __name__ == "__main__":
    print(json.dumps(validate_package(ROOT), indent=2, sort_keys=True))
