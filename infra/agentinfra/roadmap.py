"""Compile literate milestones into deterministic, evidence-derived projections."""
from __future__ import annotations

import re
from pathlib import Path

from .atomic import atomic_write_json
from .roadmap_records import (bindings_current, canonical, digest, loads, read_json,
                              require, validate_record)
from .security import confined_path
from .transaction import FileTransaction, Mutation
from .roadmap_policy import proof_errors


FENCE = re.compile(r"^```aegis-milestone\s*\n(.*?)^```\s*$", re.M | re.S)
FIXED_RECIPES = {
    "roadmap.validate": ["python", "-B", "scripts/validate_roadmaps.py"],
    "roadmap.tests": ["python", "-B", "-m", "unittest", "discover", "-s", "infra/tests", "-p", "test_roadmap*.py", "-q"],
    "aegis.selftest": ["python", "-B", "scripts/selftest.py"],
}
GATES = {"source_correspondence", "implemented_outputs", "production_build", "applicable_original_tests",
         "full_domain_proof", "architecture", "package_identity", "publication", "operational_closure", "current_global_barrier"}


def compile_roadmaps(root: Path) -> dict:
    root = root.resolve()
    shared = root / "Roadmaps/Shared"
    registry = read_json(shared / "registry.json")
    require(registry.get("schema") == 1, "unknown registry version")
    policy = read_json(shared / "policy.json")
    require(policy.get("schema") == 1 and policy.get("provider") == "codex", "CODEX_ONLY policy required")
    require(policy.get("reasoning") == "max" and policy.get("max_active_agents") == 1, "reasoning/agent policy weakened")
    require(policy.get("initial_strategy") == "implementation_first" and policy.get("domain_proofs_at_completion") is True,
            "phase verification policy weakened")
    require(policy.get("flaw_campaign") == "deferred" and policy.get("cgp_requires_all_projects_complete") is True,
            "deferred phase policy weakened")
    from .roadmap_mirrors import POLICY_PATH, read_download_policy
    require(policy.get("artifact_download_policy") == POLICY_PATH, "reviewed mirror delivery policy required")
    delivery = read_download_policy(root)
    require(all(delivery.get(k, "missing") is None for k in
                ("overall_job_deadline", "max_sources_per_artifact", "max_addresses_per_source", "source_timeout_seconds")),
            "persistent delivery reintroduced source/address/transfer lifetime ceilings")
    from .roadmap_persistence import POLICY_PATH as EXECUTION_POLICY_PATH, read_execution_policy
    require(policy.get("execution_policy") == EXECUTION_POLICY_PATH and "AM20" in policy.get("amendments", {}),
            "adopted persistent execution policy required")
    read_execution_policy(root)
    sources = read_json(shared / "sources.json")
    mandatory_sources = {"AGENTS.MD", "Blue_Prompt.md", "Destiny_Prompt.md", "Roadmaps/Shared/ADOPTED_PLAN.md"}
    source_names = [s["path"] for s in sources["files"]]
    require(len(source_names) == len(set(source_names)) and mandatory_sources <= set(source_names), "source authority denominator missing/duplicated")
    for source in sources["files"]:
        require(bindings_current(root, [source]), f"source authority changed: {source['path']}")
    requirements = read_json(shared / "requirements.json")["requirements"]
    for requirement in requirements:
        path = confined_path(root, requirement["source"], must_exist=True)
        lines = path.read_text().splitlines()
        start, end = requirement["lines"]
        require(0 < start <= end <= len(lines), "invalid requirement source location")
        require(digest("\n".join(lines[start-1:end]).encode()) == requirement["sha256"], "requirement source excerpt changed")
    for source in ("Blue_Prompt.md", "Destiny_Prompt.md"):
        covered_lines = set()
        for r in requirements:
            if r["source"] == source:
                covered_lines.update(range(r["lines"][0], r["lines"][1] + 1))
        require(covered_lines == set(range(1, len((root / source).read_text().splitlines()) + 1)), f"source requirements omitted: {source}")
    requirement_ids = [r["id"] for r in requirements]
    require(len(set(requirement_ids)) == len(requirement_ids), "duplicate requirement IDs")
    amendments = set(registry["amendments"])
    require(amendments == set(policy["amendments"]) and amendments <= set(requirement_ids), "missing adopted amendments")
    require({f"ROOT-{n:02}" for n in range(1, 20)} <= set(requirement_ids), "root requirements omitted")
    for prefix, count in (("BLUE-A", 14), ("BLUE-U", 22), ("DESTINY-A", 15)):
        require({f"{prefix}{n:02}" for n in range(1, count + 1)} <= set(requirement_ids), "named acceptance requirements omitted")
    recipes = registry["recipes"]
    for name, recipe in recipes.items():
        require(recipe.get("kind") in {"local_validation", "project_specification"}, "unknown recipe class")
        require(recipe.get("execution_mode") == "persistent_unlimited" and
                recipe.get("max_seconds", "missing") is None and recipe.get("max_attempts", "missing") is None,
                "recipe reintroduced an Aegis attempt/time ceiling")
        if recipe["kind"] == "local_validation":
            require(name in FIXED_RECIPES and recipe["argv"] == FIXED_RECIPES[name], "unreviewed executable recipe")
    milestones = {}
    input_bindings = list(sources["files"])
    for project, profile in registry["projects"].items():
        validate_record(root, "ProjectProfile", profile)
        paths = sorted((root / "Roadmaps" / project).glob("[0-9][0-9]-*.md"))
        require(len(paths) == len(profile["milestones"]), f"{project}: missing or extra milestone files")
        for path in paths:
            raw = path.read_bytes()
            blocks = FENCE.findall(raw.decode("utf-8"))
            require(len(blocks) == 1, f"{path}: exactly one milestone contract required")
            item = loads(blocks[0])
            validate_record(root, "MilestoneContract", item)
            budget = item["budget_policy"]
            require(budget.get("execution_mode") == "persistent_unlimited" and
                    budget.get("max_attempts", "missing") is None and
                    budget.get("max_seconds_per_recipe", "missing") is None and
                    "AM20" in item["amendments"] and "AM20" in item["requirements"],
                    "milestone reintroduced an Aegis attempt/time ceiling")
            ident = item["id"]
            require(ident not in milestones, f"duplicate milestone {ident}")
            require(item["project"] == project and ident in profile["milestones"], f"wrong project owner: {ident}")
            require(set(item["requirements"]) <= set(requirement_ids), f"{ident}: unknown requirement")
            require(set(item["amendments"]) <= amendments, f"{ident}: unknown amendment")
            require(set(item["checks"]) <= set(recipes), f"{ident}: undeclared execution recipe")
            require(set(item["gates"]) <= GATES, f"{ident}: unknown evidence gate")
            require(item["phase"] != "implementation" or "full_domain_proof" not in item["gates"],
                    f"{ident}: formal campaign blocks implementation")
            if item["phase"] == "modernization":
                require(set(item["dependencies"]) >= set(registry["completion_milestones"]), f"{ident}: missing global CGP barrier")
            for artifact in item["references"]:
                require(confined_path(root, artifact, must_exist=True).is_file(), f"missing reference: {artifact}")
            milestones[ident] = dict(item, document=path.relative_to(root).as_posix())
            input_bindings.append({"path": path.relative_to(root).as_posix(), "sha256": digest(raw)})
    covered = set().union(*(set(m["requirements"]) for m in milestones.values()))
    require(covered == set(requirement_ids), f"requirements without milestones: {set(requirement_ids) - covered}")
    for requirement in requirements:
        require(requirement["milestones"] and set(requirement["milestones"]) <= set(milestones), "requirement references missing milestone")
        for ident in requirement["milestones"]:
            require(requirement["id"] in milestones[ident]["requirements"], f"asymmetric requirement mapping: {requirement['id']}")
    order, active, seen = [], set(), set()

    def visit(ident: str) -> None:
        require(ident in milestones, f"missing dependency: {ident}")
        require(ident not in active, f"dependency cycle at {ident}")
        if ident in seen:
            return
        active.add(ident)
        for dependency in sorted(milestones[ident]["dependencies"]):
            visit(dependency)
        active.remove(ident)
        seen.add(ident)
        order.append(ident)

    priority = registry.get("execution_priority", [])
    require(len(priority) == len(milestones) and set(priority) == set(milestones), "execution priority must preserve every milestone exactly once")
    for ident in priority:
        visit(ident)
    providers = {}
    obligations = []
    for ident, milestone in milestones.items():
        for capability in milestone["provides"]:
            require(capability not in providers, "duplicate capability provider")
            providers[capability] = ident
        obligations.extend(p["id"] for p in milestone["proof_obligations"])
    require(len(obligations) == len(set(obligations)), "duplicate proof obligation identity")
    for milestone in milestones.values():
        require({c["provider"] for c in milestone["consumes"]} == set(milestone["dependencies"]), "capability prerequisites missing or undeclared")
        for consume in milestone["consumes"]:
            require(providers.get(consume["capability"]) == consume["provider"], "capability provider mismatch")
    project_docs = {root / "Roadmaps" / p / name for p in registry["projects"] for name in ("README.md", "GOAL.md")}
    for path in sorted(set(shared.glob("*.json")) | set(shared.glob("*.md")) | set((shared / "codex-protocol").glob("*.json")) |
                       set((root / "infra").rglob("*.py")) | set((root / "scripts").glob("*.py")) |
                       set((root / "bin").glob("*.py")) | set((root / "verification/roadmap").glob("*.py")) |
                       set((shared / "ci").glob("*.py")) | set((shared / "skills").rglob("SKILL.md")) | project_docs):
        input_bindings.append({"path": path.relative_to(root).as_posix(), "sha256": digest(path.read_bytes())})
    result = {"schema": 1, "kind": "compiled_roadmap_projection", "policy": policy,
              "projects": registry["projects"], "recipes": recipes, "milestones": milestones,
              "order": order, "requirements": requirement_ids, "inputs": input_bindings,
              "completion_claim": "ROADMAP_PACKAGE_ONLY; product milestones require their own evidence"}
    result["digest"] = digest(result)
    return result


def audit_evidence(root: Path, compiled: dict, evidence: dict) -> dict:
    """Evaluate supplied, source-bound receipts, never Markdown checkboxes.

    Receipt producer trust and semantic adequacy remain explicit reviewed boundaries.
    This function cannot authenticate arbitrary user-created proof claims.
    """
    require(evidence.get("schema") == 1, "unsupported evidence envelope")
    require(bindings_current(root, compiled["inputs"]), "compiled source/tool/configuration inputs became stale")
    require(evidence.get("compiled_digest") == compiled["digest"], "evidence belongs to another roadmap")
    receipts = evidence.get("receipts", [])
    require(isinstance(receipts, list), "receipts must be a list")
    ids = [r.get("id") for r in receipts]
    require(len(ids) == len(set(ids)), "duplicate receipt IDs")
    by_milestone = {}
    for receipt in receipts:
        validate_record(root, "EvidenceReceipt", receipt)
        require(receipt["milestone"] in compiled["milestones"], "receipt has unknown milestone")
        by_milestone.setdefault(receipt["milestone"], []).append(receipt)
    result = {}
    for ident in compiled["order"]:
        contract = compiled["milestones"][ident]
        accepted = []
        candidates = set()
        rejected = []
        for receipt in by_milestone.get(ident, []):
            require(receipt["gate"] in contract["gates"], "receipt claims an undeclared milestone gate")
            good = (receipt["outcome"] == "PASS" and receipt["scope"] == "production"
                    and receipt["contract_digest"] == digest(contract)
                    and bindings_current(root, receipt["inputs"])
                    and bindings_current(root, receipt["artifacts"])
                    and bindings_current(root, receipt["logs"]))
            if receipt["gate"] == "implemented_outputs":
                good = (good and sorted(receipt["configuration"].get("outputs", [])) == sorted(contract["outputs"])
                        and sorted(receipt["configuration"].get("implementation_units", [])) == sorted(contract["implementation_units"]))
            if receipt["gate"] == "full_domain_proof":
                proofs = receipt.get("proofs", [])
                required = receipt["configuration"].get("required_obligation_ids", [])
                actual = [p.get("obligation", {}).get("obligation_id") for p in proofs]
                minimum = {p["id"] for p in contract["proof_obligations"]}
                good = (good and bool(required) and minimum <= set(required)
                        and len(required) == len(set(required)) and sorted(actual) == sorted(required))
                for proof in proofs:
                    obligation, result_proof = proof.get("obligation", {}), proof.get("result", {})
                    validate_record(root, "ProofObligation", obligation)
                    from .roadmap_python import python_proof_errors
                    good = (good and not proof_errors(obligation, result_proof)
                            and not python_proof_errors(root, obligation, result_proof)
                            and obligation["candidate"] == receipt["candidate"]
                            and bindings_current(root, obligation["source"]))
            if good:
                accepted.append(receipt["gate"])
                candidates.add(receipt["candidate"])
            else:
                rejected.append(receipt["id"])
        missing = sorted(set(contract["gates"]) - set(accepted))
        dependencies = [d for d in contract["dependencies"] if result[d]["state"] != "SATISFIED"]
        if len(candidates) > 1:
            missing.append("ONE_COHERENT_CANDIDATE")
        if missing or dependencies:
            state = "BLOCKED" if dependencies else "READY"
        else:
            state = "SATISFIED"
        result[ident] = {"state": state, "missing_gates": missing,
                         "dependency_blockers": dependencies, "rejected_receipts": rejected}
    return {"schema": 1, "compiled_digest": compiled["digest"], "milestones": result,
            "trust_boundary": "source-bound receipt validation; not independent proof of semantic adequacy"}


def packet(compiled: dict, audit: dict, ident: str, max_bytes: int = 24_576) -> dict:
    require(ident in compiled["milestones"], "unknown work unit")
    require(type(max_bytes) is int and max_bytes > 0, "invalid packet budget")
    require(audit["compiled_digest"] == compiled["digest"], "stale audit")
    contract = compiled["milestones"][ident]
    work = {"schema": 1, "work_id": digest({"roadmap": compiled["digest"], "milestone": ident}),
            "contract": contract, "readiness": audit["milestones"][ident],
            "policy": compiled["policy"], "instructions": "Read the milestone document and listed references. No work is activated by this packet."}
    require(len(canonical(work)) <= max_bytes, "packet exceeds budget; split the work, never truncate requirements")
    return work


def project_into_record(root: Path, relative: str, audit: dict, expected_digest: str) -> dict:
    path = confined_path(root, relative, must_exist=True)
    raw = path.read_bytes()
    require(digest(raw) == expected_digest, "canonical record changed")
    record = loads(raw.decode())
    require(isinstance(record, dict), "canonical record is not an object")
    registry_path = root / "Roadmaps/Shared/registry.json"
    registry = read_json(registry_path) if registry_path.exists() else None
    if registry and path == confined_path(root, registry["projects"]["Aegis"]["canonical_record"]):
        from .roadmap_project import ProjectAdapter
        return ProjectAdapter(root, profiles=registry["projects"]).update(
            {"aegis_roadmap_projection": audit}, expected_digest=expected_digest)
    updated = dict(record, aegis_roadmap_projection=audit)
    return FileTransaction(root, [Mutation(path, canonical(updated) + b"\n", expected_sha256=expected_digest)],
                           state_dir=root / ".aegis/state/transactions", name="roadmap-projection").commit()


def save_compiled(root: Path, compiled: dict) -> Path:
    path = root / ".aegis/roadmaps/compiled.json"
    atomic_write_json(path, compiled, root=root)
    return path
