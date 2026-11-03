"""Source-bound Python obligation and original-fixture catalogs.

AST locations and real runtime witnesses are separate evidence channels. These
records preserve complete source files and unresolved semantic interpretation;
they never manufacture a translated contract or accept a domain-proof result.
"""
from __future__ import annotations

import ast
from pathlib import Path
import re

from .roadmap_policy import SEMANTIC_FIELDS
from .roadmap_python import module_closure, source_closure
from .roadmap_records import bindings_current, digest, file_binding, read_json, require
from .security import confined_path


INTERFACE_VERSION = 1
HOOKS = {"setUp", "tearDown", "setUpClass", "tearDownClass", "asyncSetUp", "asyncTearDown"}


def _role(path: str) -> str:
    if path.startswith("infra/tests/"):
        return "original_test"
    if path.startswith("verification/roadmap/"):
        return "qualification_or_verification_harness"
    return "maintained_production_tooling"


def _node(node: ast.AST) -> dict:
    record = {"kind": type(node).__name__, "span": [node.lineno, node.end_lineno],
              "ast_sha256": digest(ast.dump(node, include_attributes=False).encode())}
    if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
        record["declared_name"] = node.name
    else:
        record["expression"] = ast.unparse(node)
    return record


def fixture_catalog(root: Path, locations: list[dict]) -> tuple[dict, dict]:
    """Bind entire fixtures, local inherited helpers and transitive source imports.

    External bases, dynamic lookup and runtime-dependent fixture values remain
    explicit unresolved semantics. Method names alone are never fixture IDs.
    """
    sources, closures, rows = {}, {}, {}
    for location in locations:
        relative = location["source"]["path"]
        if relative not in sources:
            require(bindings_current(root, [location["source"]]), "original fixture source changed")
            path = root / relative
            tree = ast.parse(path.read_bytes(), filename=relative)
            module = relative.removeprefix("infra/tests/").removesuffix(".py").replace("/", ".")
            closure = module_closure(root, module, include_tests=True)
            closures[closure["digest"]] = closure
            sources[relative] = (tree, closure)
        tree, closure = sources[relative]
        classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        matches = [(cls, method) for cls in classes if cls.name == location["fixture"] for method in cls.body
                   if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)) and method.name == location["test"] and
                   [method.lineno, method.end_lineno] == location["span"]]
        require(len(matches) == 1, "fixture source occurrence is missing or ambiguous")
        cls, method = matches[0]
        require(_node(method)["ast_sha256"] == location["ast_sha256"], "original method body identity differs")
        fixture_nodes, external_bases, unresolved, pending = [], [], [], [cls]
        seen = set()
        while pending:
            current = pending.pop()
            key = (current.lineno, current.end_lineno)
            if key in seen:
                continue
            seen.add(key)
            fixture_nodes.append(current)
            for base in current.bases:
                local = [c for c in classes if isinstance(base, ast.Name) and c.name == base.id]
                if local:
                    pending.extend(local)
                    if len(local) != 1:
                        unresolved.append({"kind": "ambiguous_local_base", "name": ast.unparse(base)})
                else:
                    external_bases.append(ast.unparse(base))
        methods = [n for c in fixture_nodes for n in c.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        calls = sorted([n for n in ast.walk(method) if isinstance(n, ast.Call)], key=lambda n: (n.lineno, n.col_offset))
        assertions = [_node(n) for n in ast.walk(method) if isinstance(n, ast.Assert) or isinstance(n, ast.Call) and
                      (ast.unparse(n.func).startswith("self.assert") or ast.unparse(n.func) == "self.fail")]
        quantifiers = [_node(n) for n in ast.walk(method) if isinstance(n, (ast.For, ast.While, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)) or
                       isinstance(n, ast.Call) and ast.unparse(n.func) == "self.subTest"]
        effects = [_node(n) for n in ast.walk(method) if isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.Delete, ast.Raise, ast.Await))]
        hooks = [_node(n) for n in methods if n.name in HOOKS]
        helpers = [_node(n) for n in methods if not n.name.startswith("test") and n.name not in HOOKS]
        module_hooks = [_node(n) for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name in {"setUpModule", "tearDownModule"}]
        fields = {field: {"source_status": "SOURCE_BOUND_REQUIRES_SEMANTIC_INTERPRETATION", "whole_fixture_source": location["source"]}
                  for field in SEMANTIC_FIELDS}
        fields["fixture_setup"].update(hooks=[h for h in hooks if h["declared_name"] in {"setUp", "setUpClass", "asyncSetUp"}], module_hooks=module_hooks)
        fields["fixture_teardown"].update(hooks=[h for h in hooks if h["declared_name"] in {"tearDown", "tearDownClass", "asyncTearDown"}], module_hooks=module_hooks)
        fields["helpers"]["definitions"] = helpers
        fields["call_order"]["calls_in_source_order"] = [_node(n) for n in calls]
        fields["assertions"]["nodes"] = assertions
        fields["quantification"].update(nodes=quantifiers, interpretation="original source loops/subtests; no invented universal quantification")
        fields["effects"]["nodes"] = effects
        fields["exceptions"]["nodes"] = [a for a in assertions if "assertRaises" in a["expression"]] + [_node(n) for n in ast.walk(method) if isinstance(n, (ast.Try, ast.TryStar, ast.ExceptHandler))]
        fields["tolerances"]["nodes"] = [a for a in assertions if "AlmostEqual" in a["expression"] or "delta=" in a["expression"] or "places=" in a["expression"]]
        fields["configuration"]["decorators"] = [ast.unparse(n) for n in [*cls.decorator_list, *method.decorator_list]]
        fields["identity"]["nodes"] = [_node(n) for n in ast.walk(method) if isinstance(n, ast.Compare) and any(isinstance(op, (ast.Is, ast.IsNot)) for op in n.ops)]
        fields["inputs"]["arguments"] = ast.dump(method.args, include_attributes=False)
        fields["numeric_semantics"]["required_behavior"] = "Preserve Python unbounded integers, exact bool/type checks, floats, configured tolerances and exceptions as actually used; no finite-bound substitution"
        record = {"schema": 1, "location": location, "source_closure": closure["digest"],
                  "fixture_definitions": [_node(n) for n in sorted(fixture_nodes, key=lambda n: n.lineno)],
                  "external_bases": sorted(set(external_bases)), "unresolved": unresolved,
                  "semantic_source_fields": fields, "runtime_id": relative.removeprefix("infra/tests/").removesuffix(".py").replace("/", ".") + "." + cls.name + "." + method.name,
                  "status": "SOURCE_BOUND_RUNTIME_AND_TRANSLATION_REVIEW_REQUIRED", "domain_proof": False}
        record["digest"] = digest(record)
        rows[location["id"]] = record
    return rows, closures


def runtime_bindings(root: Path, fixtures: dict, details: dict | None) -> dict:
    """Reconcile a validated producer's observations without semantic promotion."""
    by_id = {}
    for key, fixture in fixtures.items():
        by_id.setdefault(fixture["runtime_id"], []).append(key)
    actual_rows = details.get("occurrences", []) if details else []
    require(len(actual_rows) == len({r["id"] for r in actual_rows}), "duplicate runtime original-test occurrences")
    observations = {r["id"]: r for r in actual_rows}
    source_files = {b["path"]: b for b in details.get("source_files", [])} if details else {}
    rows = {}
    for key, fixture in fixtures.items():
        actual = observations.get(fixture["runtime_id"])
        source = fixture["location"]["source"]
        if len(by_id[fixture["runtime_id"]]) != 1:
            status = "AMBIGUOUS_RUNTIME_SOURCE_OCCURRENCE"
        elif source_files.get(source["path"]) != source or not bindings_current(root, [source]):
            status = "MISSING_OR_STALE_EXECUTED_SOURCE"
        elif not actual:
            status = "MISSING_RUNTIME_OCCURRENCE"
        else:
            status = "OBSERVED_" + actual["outcome"] + "_RUNTIME_ONLY"
        rows[key] = {"runtime_id": fixture["runtime_id"], "status": status, "observation": actual,
                     "fixture_semantics": fixture["digest"], "domain_proof": False}
    return {"fixtures": rows, "unmatched_runtime_ids": sorted(set(observations) - set(by_id)),
            "original_test_translation_review": "NOT_GRANTED", "domain_proof": False}


def _actual_test_details(root: Path, compiled: dict, candidate: str) -> tuple[dict | None, dict | None, list[dict]]:
    # Reuse the existing materializer/ledger/result validator. A convenient JSON
    # with PASS strings cannot become an executed original-test observation.
    from .roadmap_runtime import BudgetLedger
    from .roadmap_work import validate_tool_receipt
    # The outer named recipe supplies the current materialized candidate. Do
    # not recompute its host configuration inside the isolated recipe HOME.
    attempts = [a for a in BudgetLedger(root).read()["attempts"] if a["status"] == "SUCCESS" and
                a.get("receipt", {}).get("recipe") == "original.tests" and a["receipt"].get("candidate") == candidate]
    if not attempts:
        return None, None, []
    attempt = attempts[-1]
    binding = attempt.get("operation", {}).get("spec")
    require(binding and bindings_current(root, [binding]), "executed original-test specification is missing or changed")
    spec = read_json(root / binding["path"])
    spec_inputs = {b["path"]: b for b in spec["inputs"]}
    if (spec.get("candidate") != candidate or spec.get("contract_digest") != compiled["digest"] or
            any(spec_inputs.get(b["path"]) != b for b in compiled["inputs"]) or not bindings_current(root, spec["inputs"])):
        return None, None, []
    receipt = attempt["receipt"]
    require(receipt["inputs"] == spec["digest"] == attempt["inputs"], "runtime fixture operation identity differs")
    validate_tool_receipt(root, spec, receipt)
    bindings = [b for b in receipt["artifacts"] if b["path"].endswith("/details.json")]
    require(len(bindings) == 1, "original-test producer has no unique detail artifact")
    details = read_json(root / bindings[0]["path"])
    require(details.get("candidate") == candidate and details.get("accepted") is True, "runtime fixture producer is not accepted for this candidate")
    dependencies = {}
    for item in [binding, *receipt["artifacts"]]:
        require(item["path"] not in dependencies or dependencies[item["path"]] == item, "runtime receipt dependency identity conflicts")
        dependencies[item["path"]] = item
    return details, bindings[0], sorted(dependencies.values(), key=lambda b: b["path"])


def test_receipt_dependencies(root: Path, compiled: dict, candidate: str) -> list[dict]:
    """Bind runtime witnesses into the existing route work specification/cache."""
    return _actual_test_details(root, compiled, candidate)[2]


def _qualification_evidence(root: Path) -> tuple[dict, dict | None, list[dict]]:
    """Retain actual ledger evidence without making a historical run current proof.

    The canonical pointer selects an observation, not an approved backend. All
    immutable artifacts must agree with its original supervisor/specification.
    Changed source/tool files remain explicit stale observations, never proof.
    """
    from .roadmap_project import ProjectAdapter
    from .roadmap_runtime import BudgetLedger
    from .roadmap_work import validate_tool_receipt
    if not (root / ".aegis/project.json").is_file():
        return {"status": "NOT_ATTEMPTED", "domain_proof": False}, None, []
    binding = ProjectAdapter(root).read().get("python_qualification_observation")
    if not binding:
        return {"status": "NOT_ATTEMPTED", "domain_proof": False}, None, []
    require(bindings_current(root, [binding]), "canonical Python qualification observation changed")
    attempts = BudgetLedger(root).read()["attempts"]
    matches = [a for a in attempts if a["status"] == "SUCCESS" and a.get("receipt", {}).get("recipe") == "python.qualify" and
               binding in a["receipt"].get("artifacts", [])]
    require(len(matches) == 1, "Python qualification lacks a unique actual ledger producer")
    attempt = matches[0]
    spec_binding = attempt.get("operation", {}).get("spec")
    require(spec_binding and bindings_current(root, [spec_binding]), "qualification specification changed or is missing")
    spec = read_json(confined_path(root, spec_binding["path"]))
    receipt = attempt["receipt"]
    details = read_json(confined_path(root, binding["path"]))
    require(spec.get("digest") == attempt["inputs"] == receipt["inputs"] == digest({k: v for k, v in spec.items() if k != "digest"}) and
            spec.get("recipe") == "python.qualify" and spec.get("project") == "Aegis" and
            spec.get("selection", {}).get("kind") == "actual_python_source_qualification" and
            spec["selection"].get("action") == "qualify" and spec["selection"].get("domain_proof") is False,
            "qualification operation identity/producer differs")
    require(details.get("schema") == 1 and details.get("action") == "qualify" and details.get("backend") == "nagini" and
            details.get("candidate") == spec.get("candidate") == receipt.get("candidate") and details.get("domain_proof") is False,
            "qualification details escaped their dispatched producer")
    tool_binding = details.get("toolchain")
    require(tool_binding and tool_binding == spec["selection"].get("toolchain") and
            bindings_current(root, [tool_binding]), "qualification toolchain provenance is missing or changed")
    toolchain = read_json(confined_path(root, tool_binding["path"]))
    require(toolchain.get("status") == "INSTALLED_NOT_QUALIFIED" and toolchain.get("files"), "qualification lacks its installed toolchain manifest")
    invoked = spec.get("argv", [None])[0]
    require(isinstance(invoked, str) and Path(invoked).is_absolute() and
            str(Path(invoked).resolve()) == spec["toolchain"]["executable"], "qualification interpreter differs from its pinned executable identity")
    expected_argv = [invoked, "-B", "scripts/roadmap_python.py", "qualify", "--output",
                     spec["target"]["output"] + "/details.json", "--candidate", spec["candidate"], "--toolchain", tool_binding["path"]]
    require(spec.get("argv") == expected_argv and receipt.get("argv") == expected_argv and
            binding["path"] == spec["target"]["output"] + "/" + spec["digest"] + "/details.json",
            "qualification did not use the fixed source-owned driver/output")
    original = details.get("original")
    production = details.get("production", {})
    require(original and production.get("target") and production.get("files") and
            production.get("digest") == digest({k: v for k, v in production.items() if k != "digest"}),
            "qualification lacks complete original/production source identity")
    expected = [binding, spec_binding, tool_binding, original, *receipt["artifacts"], *production["files"], *toolchain["files"]]
    dependencies, stale = {}, []
    for item in expected:
        path = confined_path(root, item["path"])
        observed = file_binding(root, item["path"]) if path.is_file() else None
        if observed != item:
            stale.append({"expected": item, "observed": observed})
        if observed:
            require(item["path"] not in dependencies or dependencies[item["path"]] == observed, "qualification dependency identity conflicts")
            dependencies[item["path"]] = observed
    record = {"status": "RETAINED_ACTUAL_QUALIFICATION_OBSERVATION", "attempt": attempt["id"],
              "observation": binding, "specification": spec_binding, "producer_candidate": spec["candidate"],
              "recorded_status": details.get("status"), "domain_proof": False, "backend_qualified": False,
              "producer_interpreter": {k: spec["toolchain"].get(k) for k in ("executable", "sha256", "version", "platform")},
              "retained_attempt_ids": [a["id"] for a in attempts if a["work_id"] == attempt["work_id"]],
              "producer_inputs_current": bindings_current(root, spec["inputs"]), "stale_bindings": stale}
    if stale:
        record["status"] = "STALE_QUALIFICATION_ARTIFACTS_NO_CURRENT_CREDIT"
        return record, None, sorted(dependencies.values(), key=lambda b: b["path"])
    validate_tool_receipt(root, spec, receipt)
    require(receipt["returncode"] == 0 and receipt["timed_out"] is False and receipt["truncated"] is False,
            "qualification producer did not complete its observation")
    record["production_closure_current"] = production == source_closure(root, production["target"])
    if not record["production_closure_current"]:
        record["status"] = "STALE_PRODUCTION_CLOSURE_NO_CURRENT_CREDIT"
        return record, None, sorted(dependencies.values(), key=lambda b: b["path"])
    return record, details, sorted(dependencies.values(), key=lambda b: b["path"])


def qualification_receipt_dependencies(root: Path) -> list[dict]:
    """Make a changed real backend observation invalidate the route cache."""
    return _qualification_evidence(root)[2]


def qualification_lineage_digest(root: Path) -> str:
    """Bind displayed attempt ancestry even when the canonical result is unchanged."""
    return digest(_qualification_evidence(root)[0].get("retained_attempt_ids", []))


def qualification_reports(root: Path, candidate: str, catalog: dict) -> dict:
    """Join actual backend diagnostics to complete source and fixture identities.

    These are engineering packets. Even matching source closure and a successful
    CLI result cannot approve a semantic translation, reachability or proof.
    """
    from .roadmap_python import classify_nagini
    observation, details, dependencies = _qualification_evidence(root)
    observation["same_code_candidate"] = observation.get("producer_candidate") == candidate
    packets, runs = [], []
    if details:
        toolchain = read_json(confined_path(root, details["toolchain"]["path"]))
        controls = details.get("runs", [])
        require(len(controls) == 2 and [r.get("intent") for r in controls] == ["positive", "deliberately_wrong_assertion"],
                "qualification omitted, duplicated or reordered its positive/negative controls")
        closure = details["production"]
        closure_files = {b["path"]: b for b in closure["files"]}
        fixture_ids = [key for key, fixture in catalog["fixture_semantics"].items() if
                       fixture["location"]["source"] == details["original"] and
                       fixture["location"]["fixture"] == "DomainPolicyTests" and
                       fixture["location"]["test"] == "test_budgets_and_completion"]
        affected = [row["id"] for row in catalog["obligations"] if set(closure_files) & {b["path"] for b in row["source_bindings"]} or
                    set(fixture_ids) & set(row["original_fixture_ids"])]
        for control, name in zip(controls, ("policy_positive.py", "policy_negative.py"), strict=True):
            fixture = control["fixture"]
            require(fixture["path"] == "verification/roadmap/python/" + name and bindings_current(root, [fixture, control["result"]]) and
                    fixture in details["artifacts"] and control["result"] in details["artifacts"], "qualification control source/result changed")
            raw = read_json(confined_path(root, control["result"]["path"]))
            prefix = [toolchain["python"], "-B", toolchain["nagini"]]
            require(raw.get("argv") in (prefix + [str(root / fixture["path"])],
                    prefix + ["--mypy-path", str(root / "infra"), str(root / fixture["path"])]) and raw.get("cwd") == str(root.resolve()),
                    "qualification control did not ingest its actual fixture through the pinned console")
            classification = classify_nagini(raw)
            tree = ast.parse(confined_path(root, fixture["path"]).read_bytes())
            assertions = [_node(n) for n in ast.walk(tree) if isinstance(n, ast.Call) and ast.unparse(n.func) == "Assert"]
            row = {"intent": control["intent"], "fixture": fixture, "result": control["result"],
                   "recorded_classification": control["classification"], "classification": classification,
                   "assertion_source_nodes": assertions, "assertion_reachability": "NOT_ESTABLISHED",
                   "negative_control_identity_review": "NOT_GRANTED", "domain_proof": False}
            runs.append(row)
            diagnostics = []
            for channel in ("stdout", "stderr"):
                for number, text in enumerate(raw.get(channel, "").splitlines(), 1):
                    match = re.fullmatch(r"Type error: (.+) \(([A-Za-z_][\w.]*)@(\d+)\.(\d+)\)", text)
                    if not match:
                        continue
                    message, module, line, column = match.groups()
                    relative = "infra/" + module.replace(".", "/") + ".py"
                    source = closure_files.get(relative)
                    identities = [u["id"] for u in catalog["production_targets"].values() if source and u["source"] == source and
                                  u["span"][0] <= int(line) <= u["span"][1]]
                    diagnostics.append({"message": message, "module": module, "line": int(line), "column": int(column),
                                        "log": control["result"], "channel": channel, "log_line": number,
                                        "source": source, "containing_declaration_ids": identities,
                                        "source_identity_status": "CURRENT_CLOSURE_LOCATION" if source and identities else "UNRESOLVED_LOCATION"})
            if classification["outcome"] != "VERIFIED_TOOL_RESULT" or control["intent"] != "positive":
                packet = {"kind": "python_backend_engineering_intervention", "backend": details["backend"],
                          "observation": observation["observation"], "producer_attempt": observation["attempt"],
                          "producer_candidate": observation["producer_candidate"], "route_candidate": candidate,
                          "target": closure["target"], "production_closure": closure, "control": row,
                          "diagnostics": diagnostics, "original_fixture_ids": fixture_ids,
                          "potentially_affected_obligation_ids": affected, "domain_proof": False,
                          "status": "UNRESOLVED_ENGINEERING_AND_SEMANTIC_REVIEW_REQUIRED",
                          "required_behavior": "Preserve the complete maintained module/import/state closure, unchanged original fixtures, exact int/bool discrimination and unbounded Python integer semantics.",
                          "required_actions": ["Resolve actual type/translation support without deleting unused production bodies, substituting stubs/models or reducing required input domains.",
                                               "Qualify faithful ESBMC/Deal alternatives against the same production/source/original denominator and record unsupported cases.",
                                               "Review exact original-to-harness semantics, assertion identities and reachability before any backend or proof promotion."],
                          "semantic_translation_approved": False, "backend_qualified": False}
                packet["id"] = digest(packet)
                packets.append(packet)
    return {"qualification_observations": [dict(observation, runs=runs)], "qualification_dependencies": dependencies,
            "qualification_lineage_digest": digest(observation.get("retained_attempt_ids", [])),
            "qualification_interventions": packets, "qualification_acceptance": "Actual or stale diagnostic observations only; no backend, translation, reachability or domain-proof approval"}


def obligation_catalog(root: Path, compiled: dict, candidate: str, source_inventory: dict, locations: list[dict]) -> dict:
    policy_path = "Roadmaps/Shared/python-obligation-bindings.json"
    policy = read_json(root / policy_path)
    contracts = {m: c for m, c in compiled["milestones"].items() if c["project"] == "Aegis" and c["phase"] != "modernization"}
    require(policy.get("schema") == 1 and set(policy["milestones"]) == set(contracts), "Python source-binding milestone denominator changed")
    fixtures, closures = fixture_catalog(root, locations)
    details, runtime_receipt, runtime_dependencies = _actual_test_details(root, compiled, candidate)
    shared_targets = {target: source_closure(root, target) for target in policy["denominator_targets"]}
    closures.update({value["digest"]: value for value in shared_targets.values()})
    file_bindings = {b["path"]: b for b in source_inventory["files"]}
    scope_files = {}
    for milestone, scope in policy["milestones"].items():
        selected = set()
        for module in scope["production_modules"]:
            relative = "infra/" + module.replace(".", "/") + ".py"
            if module == "agentinfra":
                relative = "infra/agentinfra/__init__.py"
            require(relative in file_bindings, "configured existing Python production module is missing: " + module)
            selected.add(relative)
        for pattern in scope["maintained_source_patterns"]:
            selected.update(p.relative_to(root).as_posix() for p in root.glob(pattern) if p.is_file() and p.relative_to(root).as_posix() in file_bindings)
        scope_files[milestone] = selected
    rows = []
    for milestone, contract in contracts.items():
        for obligation in contract["proof_obligations"]:
            suffix = obligation["id"].removeprefix(milestone + "-")
            require(suffix in {"O01", "O02"} or milestone == "A13" and suffix == "O03", "unrouted required domain obligation")
            files = scope_files[milestone] if suffix != "O02" else {b["path"] for c in shared_targets.values() for b in c["files"]}
            targets = [u for u in source_inventory["units"] if u["file"] in files and u["kind"] in {"FunctionDef", "AsyncFunctionDef", "ClassDef"}]
            original_ids = [key for key, f in fixtures.items() if milestone == "A13" and suffix == "O03" or files & {b["path"] for b in closures[f["source_closure"]]["files"]}]
            rows.append({"id": obligation["id"], "milestone": milestone, "statement": obligation["statement"], "origin": obligation["origin"],
                         "source_requirement_ids": contract["requirements"], "milestone_contract_digest": digest(contract),
                         "source_bindings": [dict(file_bindings[p], source_role=_role(p)) for p in sorted(files)],
                         "production_sources": [file_bindings[p] for p in sorted(files) if _role(p) == "maintained_production_tooling"],
                         "verification_sources": [file_bindings[p] for p in sorted(files) if _role(p) == "qualification_or_verification_harness"],
                         "production_target_ids": [u["id"] for u in targets if _role(u["file"]) == "maintained_production_tooling"],
                         "verification_target_ids": [u["id"] for u in targets if _role(u["file"]) == "qualification_or_verification_harness"],
                         "original_fixture_ids": original_ids, "denominator_rule_targets": list(shared_targets) if suffix == "O02" else [],
                         "backend_candidates": ["nagini", "esbmc-python", "deal"], "qualified_backend": None,
                         "retained_implementation_gaps": policy["milestones"][milestone]["retained_implementation_gaps"],
                         "status": "SOURCE_BOUND_SEMANTIC_CONTRACT_AND_BACKEND_QUALIFICATION_REQUIRED" if files else "UNIMPLEMENTED_REQUIRED_TARGET_RETAINED",
                         "required_action": "Review complete linked production/fixture semantics, explicit domains, assertions and reachability; execute a qualified source-bound backend without omitting remaining source responsibilities"})
    file_obligations = {}
    for row in rows:
        paths = {b["path"] for b in row["source_bindings"]} | {fixtures[key]["location"]["source"]["path"] for key in row["original_fixture_ids"]}
        for path in paths:
            file_obligations.setdefault(path, set()).add(row["id"])
    units = []
    for unit in source_inventory["units"]:
        related = sorted(file_obligations.get(unit["file"], set()))
        require("A13-O03" in related, "maintained Python source unit escaped the global completion denominator")
        units.append({"id": unit["id"], "file": unit["file"], "source_sha256": unit["source_sha256"], "ast_sha256": unit["ast_sha256"],
                      "span": unit["span"], "kind": unit["kind"], "source_role": _role(unit["file"]), "related_obligation_ids": related,
                      "status": "SOURCE_LINKED_DOMAIN_CLASSIFICATION_AND_PROOF_REMAIN_REQUIRED"})
    declarations = {u["id"]: {"id": u["id"], "source": file_bindings[u["file"]], "ast_sha256": u["ast_sha256"], "source_role": _role(u["file"]),
                         "span": u["span"], "kind": u["kind"], "calls": u["calls"],
                         "effect_node_count": len(u["effects"]), "status": "ACTUAL_DECLARATION_SEMANTICS_NOT_QUALIFIED",
                         "backend_routes": {"nagini": "DEDUCTIVE_CANDIDATE_ACTUAL_OPERATIONS_AND_IMPORTS_UNQUALIFIED",
                                            "esbmc-python": "BOUNDED_CANDIDATE_REQUIRES_SOURCE_FAITHFUL_DOMAIN_AND_NUMERIC_BOUNDS",
                                            "deal": "COMPLEMENTARY_CANDIDATE_REQUIRES_ACTUAL_PURE_SUPPORTED_FUNCTION"}}
               for u in source_inventory["units"] if u["kind"] in {"FunctionDef", "AsyncFunctionDef", "ClassDef"} and not u["file"].startswith("infra/tests/")}
    targets = {key: value for key, value in declarations.items() if value["source_role"] == "maintained_production_tooling"}
    verification_targets = {key: value for key, value in declarations.items() if value["source_role"] == "qualification_or_verification_harness"}
    expected = [o["id"] for contract in contracts.values() for o in contract["proof_obligations"]]
    require(expected and len(expected) == len(set(expected)) and sorted(expected) == sorted(r["id"] for r in rows),
            "required Python obligation denominator is empty, duplicated or incomplete")
    require(all(set(r["production_target_ids"]) <= set(targets) for r in rows), "obligation refers to an unbound production declaration")
    require(all(set(r["verification_target_ids"]) <= set(verification_targets) for r in rows), "obligation refers to an unbound verification declaration")
    return {"binding_policy": file_binding(root, policy_path), "obligations": rows, "source_units": units, "production_targets": targets,
            "verification_targets": verification_targets,
            "fixture_semantics": fixtures, "closure_catalog": closures, "runtime_test_receipt": runtime_receipt,
            "runtime_test_dependencies": runtime_dependencies,
            "runtime_fixture_bindings": runtime_bindings(root, fixtures, details), "domain_proof": False,
            "source_binding_limit": "Complete referenced source files retained; static call/import links overapproximate behavior. External bases, dynamic dispatch and full semantic interpretation still require qualification/review."}
