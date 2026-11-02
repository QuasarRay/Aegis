"""Assemble implementation receipts from actual ledger runs and scoped review.

This producer deliberately cannot confer formal proof or project completion.
Output adequacy remains an explicit source-review trust boundary; command and
artifact identities, complete tests and current input freshness are checked.
"""
from __future__ import annotations

from pathlib import Path

from .roadmap import audit_evidence, compile_roadmaps
from .roadmap_codex import bind_goal
from .roadmap_interfaces import compare_interfaces, observe_interfaces
from .roadmap_inventory import GitInventory
from .roadmap_portability import artifacts, check, inventory
from .roadmap_project import ProjectAdapter
from .roadmap_records import bindings_current, digest, file_binding, read_json, require, validate_record
from .roadmap_runtime import BudgetLedger
from .roadmap_work import _immutable, materialize, qualify_execution, selected_work_milestones, validate_tool_receipt
from .security import confined_path


INTERFACE_VERSION = 1


def _unique(bindings: list[dict]) -> list[dict]:
    by_path = {}
    for binding in bindings:
        require(binding["path"] not in by_path or by_path[binding["path"]] == binding, "conflicting artifact bindings")
        by_path[binding["path"]] = binding
    return [by_path[p] for p in sorted(by_path)]


def unchanged_originals(root: Path, baseline: str) -> dict:
    git = GitInventory(root)
    commit = git.read("rev-parse", "--verify", "--end-of-options", baseline + "^{commit}").strip()
    expected = []
    for entry in git.tree(commit):
        if entry["path"].startswith("infra/tests/") and entry["path"].endswith(".py"):
            require(entry["type"] == "blob" and entry["mode"] != "120000", "original test is not a source-owned file")
            binding = {"path": entry["path"], "sha256": digest(git.blob(entry["oid"]))}
            require(bindings_current(root, [binding]), "applicable original test bytes were changed or removed")
            expected.append(binding)
    require(bool(expected), "original test denominator is empty")
    return {"baseline_commit": commit, "unchanged_source_files": expected}


def assemble_implementation(root: Path, review_path: str, through: str) -> dict:
    return _assemble(root, review_path, through, complete_current=True)


def refresh_implementation_dependencies(root: Path, review_path: str, through: str) -> dict:
    """Refresh accepted dependencies while the current implementation stays open."""
    return _assemble(root, review_path, through, complete_current=False)


def _assemble(root: Path, review_path: str, through: str, *, complete_current: bool) -> dict:
    root = root.resolve()
    compiled = compile_roadmaps(root)
    adapter = ProjectAdapter(root)
    current = adapter.read()
    require(current["continuation"]["milestone"] == through, "acceptance must close the current adopted work unit")
    owner, native, _, _ = qualify_execution(root, compiled, through, "roadmap.validate")
    attempts = BudgetLedger(root).read()["attempts"]
    require(not any(a["status"] == "RESERVED" for a in attempts), "unresolved operations prevent acceptance")
    runs = {}
    selected = selected_work_milestones(compiled, current, through)
    if not complete_current:
        selected = [m for m in selected if m != through]
        require(bool(selected), "partial implementation has no accepted dependency scope to refresh")
    names = list(dict.fromkeys(["roadmap.validate", "production.build", "original.tests", "source.reconcile",
                               *[name for m in selected for name in compiled["milestones"][m]["checks"]]]))
    for name in names:
        spec = materialize(root, compiled, through, name)
        matches = [a for a in attempts if a["status"] == "SUCCESS" and a["inputs"] == spec["digest"]
                   and a.get("operation", {}).get("spec_digest") == spec["digest"]]
        require(bool(matches), f"no successful current materialized {name} operation")
        receipt = matches[-1]["receipt"]
        validate_tool_receipt(root, spec, receipt)
        require(bindings_current(root, receipt["artifacts"]), "successful operation artifacts became stale")
        require(receipt["returncode"] == 0 and receipt["timed_out"] is False and receipt["truncated"] is False,
                "operation lacks a complete successful result")
        runs[name] = {"attempt": matches[-1]["id"], "receipt": receipt, "spec": spec}
    candidate = runs["production.build"]["receipt"]["candidate"]
    require(all(r["receipt"]["candidate"] == candidate for r in runs.values()), "operation candidates differ")
    review_binding = file_binding(root, review_path)
    review = read_json(confined_path(root, review_path))
    require(review.get("candidate") == candidate and review.get("decision") == "accept_implementation" and
            bool(review.get("reviewer")) and bool(review.get("rationale")) and not review.get("unresolved_required_findings", []),
            "current scoped implementation review is missing or unresolved")
    scope = current["execution"]["scope"]
    require(through in scope, "milestone is outside adopted scope")
    require(set(review.get("milestones", {})) == set(selected), "review omits or adds an ancestor responsibility")
    if not complete_current:
        partial = review.get("partial_current", {})
        require(partial.get("milestone") == through and partial.get("open_responsibilities") and partial.get("rationale"),
                "unfinished current work must preserve its explicit open responsibilities")
    originals = unchanged_originals(root, review["original_tests_baseline"])
    test_details = next(b for b in runs["original.tests"]["receipt"]["artifacts"] if b["path"].endswith("/details.json"))
    tests = read_json(confined_path(root, test_details["path"]))
    require(tests.get("accepted") is True and tests["candidate"] == candidate, "complete original tests were not accepted")
    passing = {case["id"] for case in tests["occurrences"] if case["outcome"] == "PASS"}
    require(set(b["path"] for b in originals["unchanged_source_files"]) <= set(b["path"] for b in tests["source_files"]),
            "executed test source inventory omits original tests")
    mapping = inventory(root)
    check(root, mapping)
    _, generated = artifacts(mapping)
    migration_bindings = [file_binding(root, "Roadmaps/Shared/python-rust/" + path) for path in generated]
    migration_index = file_binding(root, "Roadmaps/Shared/python-rust/inventory.json")
    generation = digest({"review": review_binding, "runs": {name: {"attempt": run["attempt"],
                          "inputs": run["receipt"]["inputs"], "artifacts": run["receipt"]["artifacts"]}
                          for name, run in runs.items()}})
    base = f".aegis/roadmaps/work/{candidate}/acceptance/{through}/{generation}"
    interfaces = _immutable(root, base + "/interfaces.json", observe_interfaces(root))
    compatibility = compare_interfaces(root, review["original_tests_baseline"])
    require(compatibility["structural_compatible"], "public API/record changes require explicit compatibility disposition")
    compatibility_binding = _immutable(root, base + "/compatibility.json", compatibility)
    originals_binding = _immutable(root, base + "/original-sources.json", originals)
    compiled_binding = _immutable(root, base + "/compiled.json", compiled)
    native_binding = _immutable(root, base + "/native-" + native["digest"] + ".json", native)
    all_inputs = _unique([*runs["production.build"]["spec"]["inputs"], *migration_bindings])
    common = [compiled_binding, review_binding, originals_binding, interfaces, compatibility_binding,
              *[b for name, run in runs.items() if name not in {"roadmap.validate", "production.build", "original.tests", "source.reconcile"}
                for b in run["receipt"]["artifacts"]]]
    receipts = []
    for milestone in selected:
        contract = compiled["milestones"][milestone]
        require(set(contract["gates"]) == {"source_correspondence", "implemented_outputs", "production_build", "applicable_original_tests"},
                "this assembler cannot certify domain proof, packaging or final completion gates")
        observed = review["milestones"][milestone]
        require(set(observed.get("outputs", {})) == set(contract["outputs"]) and
                set(observed.get("implementation_units", {})) == set(contract["implementation_units"]),
                "review omits an explicit output or implementation unit")
        reviewed_artifacts = []
        for item in [*observed["outputs"].values(), *observed["implementation_units"].values()]:
            require(item.get("rationale") and item.get("artifacts") and item.get("tests") and
                    set(item["tests"]) <= passing and bindings_current(root, item["artifacts"]),
                    "output/unit lacks current reviewed artifacts and passing runtime evidence")
            reviewed_artifacts.extend(item["artifacts"])
        for gate, name in (("source_correspondence", "source.reconcile"), ("implemented_outputs", "roadmap.validate"),
                           ("production_build", "production.build"), ("applicable_original_tests", "original.tests")):
            run = runs[name]
            receipt = {"schema": 1, "id": f"{milestone}-{gate}-{candidate}-{generation}", "milestone": milestone, "gate": gate,
                "producer": "agentinfra.roadmap_acceptance.assemble_implementation", "candidate": candidate,
                "contract_digest": digest(contract), "inputs": all_inputs,
                "artifacts": _unique([*common, *reviewed_artifacts, *run["receipt"]["artifacts"]]),
                "command": [], "configuration": {"outputs": contract["outputs"], "implementation_units": contract["implementation_units"],
                    "actual_argv": run["spec"]["argv"], "ledger_attempt": run["attempt"], "execution_milestone": through,
                    "acceptance_generation": generation, "required_recipe_attempts": {n: r["attempt"] for n, r in runs.items()},
                    "evidence_strength": "source review, structural reconciliation and source-host runtime acceptance",
                    "original_sources": originals_binding, "domain_proof": False, "installed_artifact_acceptance": False},
                "outcome": "PASS", "scope": "production", "limits": ["Output adequacy is a scoped source-review trust boundary",
                    "No domain proof or installed artifact, package, release or native Goal completion credit"],
                "logs": [b for b in run["receipt"]["artifacts"] if b["path"].endswith("/result.json")]}
            validate_record(root, "EvidenceReceipt", receipt)
            receipts.append(receipt)
    evidence = {"schema": 1, "compiled_digest": compiled["digest"], "receipts": receipts}
    audit = audit_evidence(root, compiled, evidence)
    require(all(audit["milestones"][m]["state"] == "SATISFIED" for m in selected), "current acceptance audit failed")
    evidence_binding = _immutable(root, base + "/evidence.json", evidence)
    _immutable(root, base + "/audit.json", audit)
    current = adapter.read()
    execution = dict(current["execution"])
    prior_binding = execution["native_binding"]
    execution["binding_history"] = [*execution.get("binding_history", []), prior_binding]
    execution["native_binding"] = bind_goal(native["goal"], thread_id=owner["session"],
                                             objective=prior_binding["objective"], contract_hash=compiled["digest"])
    execution["native_turn_configuration"] = {k: native[k] for k in ("model", "effort", "mode")}
    history = list(current.get("acceptance_history", []))
    if current.get("roadmap_evidence") and current["roadmap_evidence"] != evidence_binding:
        history.append(current["roadmap_evidence"])
    adapter.update({"execution": execution, "roadmap_evidence": evidence_binding, "acceptance_history": history,
                    "aegis_roadmap_projection": audit, "module_interfaces": interfaces,
                    "compatibility_observation": compatibility_binding,
                    "python_rust_correspondence": migration_index, "implementation_review": review_binding,
                    "partial_current_work": review.get("partial_current") if not complete_current else None},
                   expected_digest=digest(adapter.profile.path().read_bytes()))
    return {"candidate": candidate, "accepted_milestones": selected, "evidence": evidence_binding,
            "domain_proof": False, "native_goal_completed": False, "native_observation": native_binding,
            "work_milestone": through, "work_milestone_complete": complete_current}
