"""Typed sequential work over the canonical project record and existing ledger.

Specifications are derived from reviewed recipe implementations. JSON or prose
cannot supply argv. Local tool execution confers no domain-proof credit.
"""
from __future__ import annotations

from dataclasses import asdict
import importlib.util
import os
from pathlib import Path
import sys
import sysconfig
import time

from .atomic import atomic_write_json
from .locks import FileLock
from .process import observe_process, run_process
from .roadmap import FIXED_RECIPES, compile_roadmaps
from .roadmap_inventory import GitInventory
from .roadmap_lease import WorkspaceLease
from .roadmap_native import inspect_process, process_handle
from .roadmap_portability import ROOTS, maintained_python
from .roadmap_project import ProjectAdapter
from .roadmap_records import bindings_current, digest, file_binding, read_json, require, validate_record
from .roadmap_runtime import BudgetLedger, recipe_scope, retry_limits
from .roadmap_persistence import policy_binding, recovery_packet, retained_history
from .security import confined_path, minimal_subprocess_env


INTERFACE_VERSION = 1
PROJECT_RECIPES = {"production.build", "original.tests", "source.reconcile", "native.protocol", "native.acceptance",
                   "python.route", "python.toolchain", "python.qualify"}


def selected_work_milestones(compiled: dict, record: dict, through: str) -> list[str]:
    """Retain accepted work and the real dependency closure, including ready forks.

    Historical projection state chooses which responsibilities must be reviewed
    again; it grants no current acceptance. Every selected output/gate still
    requires current artifacts, actual recipes and the normal evidence audit.
    """
    scope = record["execution"]["scope"]
    require(through in scope, "work is outside the adopted scope")
    selected = {m for m in scope if record.get("aegis_roadmap_projection", {}).get("milestones", {}).get(m, {}).get("state") == "SATISFIED"}
    selected.add(through)
    pending = list(selected)
    while pending:
        milestone = pending.pop()
        for dependency in compiled["milestones"][milestone]["dependencies"]:
            require(dependency in scope, "dependency is outside the adopted project scope")
            if dependency not in selected:
                selected.add(dependency)
                pending.append(dependency)
    return [m for m in compiled["order"] if m in selected]


def toolchain() -> dict:
    modules = {}
    for name in ("compileall", "py_compile", "unittest", "json", "subprocess"):
        spec = importlib.util.find_spec(name)
        require(spec is not None and spec.origin and Path(spec.origin).is_file(), "Python runtime module unavailable")
        modules[name] = {"path": spec.origin, "sha256": digest(Path(spec.origin).read_bytes())}
    stdlib = Path(sysconfig.get_path("stdlib"))
    runtime = []
    for directory, names, files in os.walk(stdlib):
        names[:] = sorted(n for n in names if n not in {"site-packages", "__pycache__"})
        for name in sorted(files):
            path = Path(directory) / name
            if path.suffix in {".py", ".so", ".pyd", ".dll"}:
                runtime.append({"path": str(path), "sha256": digest(path.read_bytes())})
    library = Path(sysconfig.get_config_var("LIBDIR") or "") / (sysconfig.get_config_var("LDLIBRARY") or "")
    return {"executable": str(Path(sys.executable).resolve()), "sha256": digest(Path(sys.executable).read_bytes()),
            "version": sys.version, "cache_tag": sys.implementation.cache_tag, "platform": sys.platform,
            "modules": modules, "stdlib": runtime,
            "python_library": {"path": str(library), "sha256": digest(library.read_bytes())} if library.is_file() else None}


def materialize(root: Path, compiled: dict, milestone: str, recipe: str, *, recovery: dict | None = None) -> dict:
    root = root.resolve()
    require(compiled == compile_roadmaps(root), "compiled authorities/source namespace changed")
    require(milestone in compiled["milestones"] and compiled["milestones"][milestone]["project"] == "Aegis",
            "only the adopted Aegis project recipes are qualified")
    contract = compiled["milestones"][milestone]
    inherited = []
    if recipe not in contract["checks"]:
        record = ProjectAdapter(root).read()
        inherited = [m for m in selected_work_milestones(compiled, record, milestone) if recipe in compiled["milestones"][m]["checks"]]
    require((recipe in contract["checks"] or inherited) and recipe in compiled["recipes"], "recipe outside the milestone contract")
    require(recipe in FIXED_RECIPES or recipe in PROJECT_RECIPES, "project recipe has no qualified implementation")
    inputs = {b["path"]: b for b in compiled["inputs"]}
    for path in maintained_python(root):
        inputs[path.relative_to(root).as_posix()] = file_binding(root, path.relative_to(root).as_posix())
    for name in ("framework.toml",):
        inputs[name] = file_binding(root, name)
    environment = minimal_subprocess_env()
    # The process supervisor supplies a fresh isolated HOME; no ambient Python
    # import path may redirect these source-owned recipes to another package.
    require(not environment.get("PYTHONHOME") and not environment.get("PYTHONPATH") and
            not environment.get("VIRTUAL_ENV"), "ambient Python routing requires explicit qualification")
    config = {"environment": environment, "isolated_home": True, "capture_bytes_per_stream": 4_000_000,
              "installed_artifact_acceptance": False, "source_roots": list(ROOTS)}
    tools = toolchain()
    if int(milestone[1:]) >= 4:
        from .roadmap_protocol import native_executable
        tools["codex"] = native_executable()
        execution = ProjectAdapter(root).read()["execution"]
        config["native"] = {"selected_model": execution["native_turn_configuration"]["model"],
                            "requested_effort": "max", "plan_source": execution.get("native_plan_source"),
                            "state_home": str(Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex").resolve())}
    candidate = digest({"compiled": compiled["digest"], "inputs": sorted(inputs.values(), key=lambda b: b["path"]),
                        "toolchain": tools, "configuration": config})
    output = f".aegis/roadmaps/work/{candidate}/{recipe}"
    selection = {"kind": "registered_local_validation"}
    if recipe in FIXED_RECIPES:
        argv = [sys.executable, *FIXED_RECIPES[recipe][1:]]
    elif recipe in {"python.route", "python.toolchain", "python.qualify"}:
        require(milestone == "A09" or "A09" in inherited, "Python qualification requires its adopted A09 capability lineage")
        action = recipe.removeprefix("python.")
        argv = [sys.executable, "-B", "scripts/roadmap_python.py", action, "--output", output + "/details.json", "--candidate", candidate]
        selection = {"kind": "actual_python_source_qualification", "action": action, "domain_proof": False}
        if recipe in {"python.toolchain", "python.qualify"}:
            from .roadmap_python import qualification_backend
            backend = qualification_backend(root)
            selection["backend"] = backend
            if backend != "nagini":
                argv.extend(["--backend", backend])
        if recipe == "python.route":
            from .roadmap_python_catalog import test_receipt_dependencies, qualification_receipt_dependencies, qualification_lineage_digest
            dependencies = test_receipt_dependencies(root, compiled, candidate)
            for dependency in dependencies:
                inputs[dependency["path"]] = dependency
            selection["original_test_dependencies"] = dependencies
            qualification_dependencies = qualification_receipt_dependencies(root)
            for dependency in qualification_dependencies:
                inputs[dependency["path"]] = dependency
            selection["qualification_dependencies"] = qualification_dependencies
            selection["qualification_lineage_digest"] = qualification_lineage_digest(root)
        if recipe == "python.qualify":
            from .roadmap_python import backend_observation_key
            binding = ProjectAdapter(root).read().get(backend_observation_key(backend, "toolchain"))
            require(binding and bindings_current(root, [binding]), "current isolated Python toolchain observation required")
            observed = read_json(confined_path(root, binding["path"]))
            require(observed.get("status") == "INSTALLED_NOT_QUALIFIED" and bindings_current(root, observed["files"]), "isolated Python toolchain is missing or changed")
            if backend == "esbmc-python":
                from .roadmap_python import esbmc_link_state
                links = esbmc_link_state(root, observed)
                require(all(x["safe"] and x["observed"] == x["expected"] for x in links), "ESBMC release symlink changed")
                selection["toolchain_link_state"] = links
            for dependency in [binding, *observed["files"]]:
                inputs[dependency["path"]] = dependency
            argv.extend(["--toolchain", binding["path"]])
            selection["toolchain"] = binding
    elif recipe == "native.protocol":
        require(milestone == "A04" or "A04" in inherited, "native protocol export requires its adopted capability lineage")
        argv = [tools["codex"]["path"], "app-server", "generate-json-schema", "--experimental", "--out", output + "/export"]
        selection = {"kind": "installed_native_protocol", "executable": tools["codex"], "experimental": True}
    elif recipe == "native.acceptance":
        require(milestone == "A04" or "A04" in inherited, "native transport acceptance requires its adopted capability lineage")
        record = ProjectAdapter(root).read()
        binding = record.get("native_protocol")
        require(binding and bindings_current(root, [binding]), "qualified current native protocol export required")
        protocol = read_json(confined_path(root, binding["path"]))
        require(protocol["executable"] == tools["codex"] and config["native"]["plan_source"], "native protocol/Plan source is mismatched or missing")
        for dependency in [binding, *protocol["files"]]:
            inputs[dependency["path"]] = dependency
        argv = [sys.executable, "-B", "scripts/roadmap_native.py", "acceptance", "--protocol", binding["path"],
                "--output", output + "/details.json", "--candidate", candidate]
        selection = {"kind": "real_read_transport_and_active_host", "protocol": binding,
                     "thread_id": record["execution"]["native_binding"]["thread_id"],
                     "objective": record["execution"]["native_binding"]["objective"],
                     "goal_created_at": record["execution"]["native_binding"]["observation"].get("createdAt")}
    elif recipe == "production.build":
        argv = [sys.executable, "-B", "-X", f"pycache_prefix={output}/pycache", "-m", "compileall", "-q", "-f",
                "--invalidation-mode=checked-hash", *ROOTS]
        selection = {"kind": "checked_hash_bytecode", "roots": list(ROOTS),
                     "production": [b for b in inputs.values() if b["path"].endswith(".py") and
                                    not b["path"].startswith("infra/tests/")]}
    else:
        argv = [sys.executable, "-B", "scripts/roadmap_acceptance.py",
                "tests" if recipe == "original.tests" else "source", "--output", output + "/details.json",
                "--candidate", candidate]
        selection = {"kind": "complete_unittest_discovery", "start": "infra/tests", "pattern": "test*.py",
                     "files": [b for b in inputs.values() if b["path"].startswith("infra/tests/")]} if recipe == "original.tests" else {
                         "kind": "all_branch_source_reconciliation", "refs": GitInventory(root).refs(),
                         "worktree": GitInventory(root).worktree(), "remote_heads": GitInventory(root).remote_heads()}
    persistent = compiled.get("policy", {}).get("execution_policy") is not None
    spec = {"schema": INTERFACE_VERSION, "project": "Aegis", "recipe": recipe, "candidate": candidate,
            "contract_digest": compiled["digest"], "inputs": sorted(inputs.values(), key=lambda b: b["path"]),
            "target": {"root": str(root), "output": output, "acceptance": "source-host runtime only"},
            "argv": argv, "selection": selection, "toolchain": tools, "configuration": config,
            "max_seconds": None if persistent else min(compiled["recipes"][recipe]["max_seconds"], contract["budget_policy"]["max_seconds_per_recipe"]),
            "max_attempts": None if persistent else min(compiled["recipes"][recipe]["max_attempts"], contract["budget_policy"]["max_attempts"])}
    spec["execution_environment"] = dict(environment)
    limits = ({"max_attempts": None, "total_seconds": None} if persistent else
              retry_limits(root, milestone, recipe, spec["max_attempts"], 1800, candidate=candidate))
    spec.update(max_attempts=limits["max_attempts"], total_seconds=limits["total_seconds"])
    if persistent:
        spec.update(execution_mode="persistent_unlimited", execution_policy=policy_binding(root))
    if "authorization" in limits:
        spec["budget_authorization"] = limits["authorization"]
        for dependency in [limits["authorization"], *limits["dependencies"]]:
            inputs[dependency["path"]] = dependency
        spec["inputs"] = sorted(inputs.values(), key=lambda b: b["path"])
    if recipe == "native.acceptance":
        # Preserve the existing native state location. The Python HOME remains
        # isolated by the supervisor; no credential value is read or copied.
        spec["execution_environment"]["CODEX_HOME"] = config["native"]["state_home"]
    spec["digest"] = digest(spec)
    if recovery is not None:
        require(persistent and bindings_current(root, [recovery]), "recovery requires current persistent policy/evidence")
        # Keep each attempt's stage outputs immutable, including retries with
        # unchanged semantic inputs. The existing work/ancestry identity stays.
        base_digest, old_output = spec["digest"], spec["target"]["output"]
        new_output = old_output + "/recovery-" + digest(recovery)
        spec["target"] = dict(spec["target"], output=new_output)
        spec["argv"] = [a.replace(old_output + "/", new_output + "/") for a in spec["argv"]]
        spec["inputs"] = sorted({b["path"]: b for b in [*spec["inputs"], recovery]}.values(), key=lambda b: b["path"])
        spec.update(recovery_base_digest=base_digest, recovery=recovery)
        spec["digest"] = digest({k: v for k, v in spec.items() if k != "digest"})
    return spec


def _immutable(root: Path, relative: str, record: dict) -> dict:
    path = confined_path(root, relative)
    if path.exists():
        require(read_json(path) == record, "immutable operation artifact changed")
    else:
        atomic_write_json(path, record, root=root, mode=0o600)
    return file_binding(root, relative)


def _save_unit(adapter: ProjectAdapter, unit: dict) -> None:
    validate_record(adapter.root, "WorkUnit", unit)
    record = adapter.read()
    units = dict(record.get("work_units", {}))
    previous = units.get(unit["work_id"])
    if previous and previous != unit:
        history = list(previous["continuation"].get("history", []))
        snapshot = dict(previous, continuation={k: v for k, v in previous["continuation"].items() if k != "history"})
        unit["continuation"]["history"] = [*history, snapshot]
    units[unit["work_id"]] = unit
    adapter.update({"work_units": units}, expected_digest=digest(adapter.profile.path().read_bytes()))


def qualify_execution(root: Path, compiled: dict, milestone: str, recipe: str) -> tuple[dict, dict, str, tuple[str, ...]]:
    adapter = ProjectAdapter(root)
    record = adapter.read()
    execution = record["execution"]
    work_id, inherited = recipe_scope(root, compiled, recipe, milestone, BudgetLedger(root))
    owner = execution["workspace_lease"]
    observation = WorkspaceLease(root).qualify(owner)
    binding = execution["native_binding"]
    require(observation["goal"]["objective"] == binding["objective"] and
            observation["goal"]["threadId"] == binding["thread_id"] and observation["goal"]["status"] == "active",
            "current native Goal differs from the adopted active objective")
    for field in ("tokensUsed", "timeUsedSeconds"):
        require(type(observation["goal"].get(field)) is int and
                observation["goal"][field] >= binding.get("observation", {}).get(field, 0),
                "native accounting cannot decrease at dispatch")
    require(observation["goal"].get("createdAt") == binding.get("observation", {}).get("createdAt"),
            "native Goal was replaced/recreated")
    require(observation["caller_is_descendant"] and observation["status"] == "active" and
            observation["mode"] == "default" and observation["effort"] == "max" and
            observation["model"] == execution["native_turn_configuration"]["model"],
            "active-host mode/model/effective max reasoning not established")
    require(execution.get("monetary_cap") is None, "requested monetary cap cannot be enforced with unknown billing")
    ledger = BudgetLedger(root)
    goal = observation["goal"]
    ledger.observe_usage(owner["session"], digest(goal), goal.get("tokensUsed"))
    usage = observation["metadata"].get("usage")
    if usage and usage.get("totals"):
        ledger.observe_categories(owner["session"], usage["origin"]["sha256"], usage["totals"], usage["origin"])
    return owner, observation, work_id, inherited


def operation_state(operation: dict) -> dict:
    """Observe actual creation handles. Neither timeout nor a lock is terminal."""
    runner = inspect_process(operation.get("runner", {}))
    child_handle = operation.get("child")
    child = inspect_process(child_handle) if child_handle else "UNKNOWN"
    group = "UNKNOWN"
    if child == "PREVIOUS_BOOT":
        group = "GONE_PREVIOUS_BOOT"
    elif os.name == "posix" and child_handle and child_handle.get("host") == operation.get("runner", {}).get("host"):
        # A reused group ID is ambiguous, never a target for termination.
        if child in {"GONE", "LIVE"}:
            try:
                os.killpg(child_handle["pid"], 0)
                group = "LIVE"
            except ProcessLookupError:
                group = "GONE"
            except PermissionError:
                pass
    return {"runner": runner, "child": child, "process_group": group,
            "safe_interruption": runner in {"GONE", "REUSED_PID", "PREVIOUS_BOOT"} and
                child in {"GONE", "PREVIOUS_BOOT"} and group in {"GONE", "GONE_PREVIOUS_BOOT"}}


def validate_tool_receipt(root: Path, spec: dict, receipt: dict) -> None:
    require(receipt.get("inputs") == spec["digest"] and receipt.get("candidate") == spec["candidate"] and
            receipt.get("argv") == spec["argv"] and receipt.get("domain_proof") is False and
            receipt.get("installed_artifact_acceptance") is False and bindings_current(root, receipt.get("artifacts", [])),
            "tool receipt input/artifact identity is stale or mismatched")
    logs = [b for b in receipt["artifacts"] if b["path"].endswith("/result.json")]
    require(len(logs) == 1, "tool receipt requires one actual supervisor result")
    result = read_json(confined_path(root, logs[0]["path"]))
    require(result["argv"] == spec["argv"] and result["cwd"] == str(root.resolve()) and
            all(result[field] == receipt[field] for field in ("returncode", "timed_out", "stdout", "stderr")) and
            receipt["truncated"] == (result["stdout_truncated"] or result["stderr_truncated"]) and
            receipt["tool_microseconds"] == int(result["duration_seconds"] * 1_000_000),
            "tool receipt contradicts the actual supervisor result")


def current_success(root: Path, compiled: dict, milestone: str, recipe: str, attempts: list[dict]) -> dict:
    """Resolve a current success, including an isolated, evidenced recovery."""
    base = materialize(root, compiled, milestone, recipe)
    matches = []
    for attempt in attempts:
        if attempt["status"] != "SUCCESS":
            continue
        if attempt["inputs"] == base["digest"]:
            spec = base
        elif (attempt.get("semantic_inputs") == base["digest"] and attempt.get("recovery") and
              bindings_current(root, [attempt["recovery"]])):
            spec = materialize(root, compiled, milestone, recipe, recovery=attempt["recovery"])
        else:
            continue
        if attempt["inputs"] == spec["digest"] == attempt.get("operation", {}).get("spec_digest"):
            validate_tool_receipt(root, spec, attempt["receipt"])
            matches.append({"attempt": attempt["id"], "spec": spec, "receipt": attempt["receipt"]})
    require(bool(matches), f"no successful current materialized {recipe} operation")
    return matches[-1]


def recover_operation(root: Path, ident: str) -> dict:
    ledger = BudgetLedger(root)
    matches = [a for a in ledger.read()["attempts"] if a["id"] == ident]
    require(len(matches) == 1, "unknown durable operation")
    attempt = matches[0]
    if attempt["status"] != "RESERVED":
        return {"status": attempt["status"], "attempt": ident, "already_terminal": True}
    operation = attempt.get("operation", {})
    observed = operation_state(operation)
    if observed["safe_interruption"]:
        receipt_path = operation.get("receipt_path")
        if receipt_path and confined_path(root, receipt_path).exists():
            receipt = read_json(confined_path(root, receipt_path))
            if (receipt.get("inputs") == attempt["inputs"] and receipt.get("domain_proof") is False and
                    bindings_current(root, receipt.get("artifacts", [])) and bindings_current(root, [operation["spec"]])):
                spec = read_json(confined_path(root, operation["spec"]["path"]))
                if (spec.get("digest") == attempt["inputs"] == digest({k: v for k, v in spec.items() if k != "digest"}) and
                        bindings_current(root, spec["inputs"]) and receipt.get("argv") == spec["argv"]):
                    validate_tool_receipt(root, spec, receipt)
                    outcome = "SUCCESS" if receipt["returncode"] == 0 and not receipt["timed_out"] and not receipt["truncated"] else "FAILED"
                    ledger.close(ident, outcome, receipt)
                    return {"status": outcome, "attempt": ident, "observed": observed, "completed_result_recovered": True}
        ledger.close(ident, "INTERRUPTED", {"recovery": observed, "unknown_usage": True,
                                           "reason": "verified runner, child and process group are gone"})
        return {"status": "INTERRUPTED", "attempt": ident, "observed": observed}
    return {"status": "UNRESOLVED", "attempt": ident, "observed": observed,
            "next_action": "reobserve these same handles; do not redispatch or refund the reservation"}


def run_work(root: Path, compiled: dict, milestone: str, recipe: str, *, diagnosis: str | None = None,
             recovery: dict | None = None) -> dict:
    root = root.resolve()
    lock = FileLock(root / ".aegis/roadmaps/execution.lock", "single canonical roadmap work unit")
    lock.acquire(timeout=0)
    try:
        owner, observation, work_id, inherited = qualify_execution(root, compiled, milestone, recipe)
        ledger = BudgetLedger(root)
        spec = materialize(root, compiled, milestone, recipe)
        previous = [a for a in ledger.read()["attempts"] if a["work_id"] == work_id]
        if recovery is None and previous and previous[-1]["status"] == "SUCCESS" and previous[-1].get("semantic_inputs") == spec["digest"]:
            # A successful recovered operation is still reusable for the same
            # source/selection. Its old recovery decision is provenance only.
            recovery = previous[-1].get("recovery")
        if recovery:
            spec = materialize(root, compiled, milestone, recipe, recovery=recovery)
        directory = spec["target"]["output"] + "/" + spec["digest"]
        spec_binding = _immutable(root, directory + "/spec.json", spec)
        native_binding = _immutable(root, directory + "/native-" + observation["digest"] + ".json", observation)
        adapter = ProjectAdapter(root)
        owners = [m for m in selected_work_milestones(compiled, adapter.read(), milestone)
                  if recipe in compiled["milestones"][m]["checks"]] if recipe not in compiled["milestones"][milestone]["checks"] else [milestone]
        unit = {"schema": 1, "work_id": work_id, "contract_digest": compiled["digest"],
                "source_responsibility": list(dict.fromkeys(r for m in [milestone, *owners] for r in compiled["milestones"][m]["requirements"])),
                "inputs": spec["inputs"], "writer": owner["session"] + ":" + str(owner["fence"]),
                "allowed_actions": [recipe], "continuation": {"milestone": milestone, "spec": spec_binding,
                    "native": native_binding, "status": "PREPARED", "domain_proof": False,
                    "implementation_units": compiled["milestones"][milestone].get("implementation_units", []),
                    "check_owners": owners}}
        adapter = ProjectAdapter(root)
        _save_unit(adapter, unit)
        operation = {"state": "PREPARED", "spec_digest": spec["digest"], "spec": spec_binding,
                     "runner": process_handle(os.getpid()), "owner": owner, "child": None,
                     "native_turn_id": observation["turn_id"], "prepared_ns": time.time_ns(),
                     "receipt_path": directory + "/receipt.json"}
        if spec.get("budget_authorization"):
            operation["budget_authorization"] = spec["budget_authorization"]
        if spec.get("execution_policy"):
            operation["execution_policy"] = spec["execution_policy"]
            operation["semantic_inputs"] = spec.get("recovery_base_digest", spec["digest"])
        if recovery:
            operation["recovery"] = recovery
        previous = [a for a in ledger.read()["attempts"] if a["work_id"] == work_id]
        if previous and previous[-1]["status"] == "SUCCESS" and previous[-1]["inputs"] != spec["digest"]:
            operation["supersedes_success"] = previous[-1]["id"]
        attempt = ledger.reserve_operation(work_id, spec["digest"], spec["max_seconds"], operation, max_attempts=spec["max_attempts"],
                                 total_seconds=spec["total_seconds"],
                                 diagnosis=diagnosis, inherited_attempt_ids=inherited,
                                 persistent_policy=spec.get("execution_policy"), recovery=recovery)
        if attempt.get("reused"):
            validate_tool_receipt(root, spec, attempt["receipt"])
            unit["continuation"].update(status="REUSED", attempt=attempt["id"], receipt=attempt["receipt"])
            _save_unit(adapter, unit)
            return dict(attempt["receipt"], reused=True, attempt=attempt["id"])
        unit["continuation"].update(status="RESERVED", attempt=attempt["id"], reservation=ledger.reservation_record(attempt["id"]))
        _save_unit(adapter, unit)

        def started(proc):
            operation.update(state="RUNNING", child=process_handle(proc.pid), dispatched_ns=time.time_ns())
            ledger.journal(attempt["id"], dict(operation))

        spawn_attempted = False
        try:
            WorkspaceLease(root).assert_owner(owner)
            current_tools = toolchain()
            if "codex" in spec["toolchain"]:
                from .roadmap_protocol import native_executable
                current_tools["codex"] = native_executable()
            require(bindings_current(root, spec["inputs"]) and spec["toolchain"] == current_tools, "dispatch inputs changed")
            dispatch_owner, dispatch_native, _, _ = qualify_execution(root, compiled, milestone, recipe)
            require(dispatch_owner == owner and dispatch_native["turn_id"] == observation["turn_id"],
                    "native owner or turn changed before dispatch")
            spawn_attempted = True
            with observe_process(started):
                result = run_process(spec["argv"], cwd=root, timeout=spec["max_seconds"],
                                     env=spec["execution_environment"], capture_limit=4_000_000,
                                     output_directory=confined_path(root, directory + "/logs"))
            log = _immutable(root, directory + "/result.json", asdict(result))
            observed = operation_state(operation)
            require(observed["child"] == "GONE" and observed["process_group"] == "GONE",
                    "supervisor returned but descendants/creation handles remain live or unknown")
            WorkspaceLease(root).assert_owner(owner)
            require(materialize(root, compile_roadmaps(root), milestone, recipe, recovery=recovery) == spec,
                    "operation semantic inputs changed")
            artifacts = [spec_binding, log]
            for raw_path, size, sha in ((result.stdout_path, result.stdout_bytes, result.stdout_sha256),
                                        (result.stderr_path, result.stderr_bytes, result.stderr_sha256)):
                if raw_path:
                    binding = file_binding(root, Path(raw_path).relative_to(root).as_posix())
                    require(binding["sha256"] == sha and Path(raw_path).stat().st_size == size,
                            "complete process archive differs from the captured stream")
                    artifacts.append(binding)
            if recipe == "native.protocol" and result.returncode == 0 and not result.timed_out:
                from .roadmap_protocol import export_manifest
                manifest = export_manifest(root, spec["target"]["output"] + "/export", spec["selection"]["executable"])
                binding = _immutable(root, directory + "/protocol.json", manifest)
                artifacts.extend([binding, *manifest["files"]])
                adapter.update({"native_protocol": binding}, expected_digest=digest(adapter.profile.path().read_bytes()))
            details = confined_path(root, spec["target"]["output"] + "/details.json")
            if details.exists():
                details_record = read_json(details)
                details_binding = _immutable(root, directory + "/details.json", details_record)
                artifacts.append(details_binding)
                require(details_record.get("candidate") == spec["candidate"] and details_record.get("domain_proof") is False,
                        "acceptance detail identity differs from the dispatched candidate")
                if recipe == "source.reconcile":
                    artifacts.append(details_record["snapshot"]["inventory"])
                if recipe in {"python.route", "python.toolchain", "python.qualify"}:
                    dependencies = details_record.get("artifacts", [])
                    require(not dependencies or bindings_current(root, dependencies), "Python observation artifacts changed")
                    artifacts.extend(dependencies)
                    if recipe == "python.toolchain" and result.returncode == 0:
                        require(details_record.get("status") == "INSTALLED_NOT_QUALIFIED" and
                                bindings_current(root, details_record["files"]), "isolated Python installation is incomplete")
                        artifacts.extend(details_record["files"])
                        from .roadmap_python import backend_observation_key
                        backend = spec["selection"]["backend"]
                        require(details_record.get("backend", "nagini") == backend, "installed backend differs from its fixed selection")
                        adapter.update({backend_observation_key(backend, "toolchain"): details_binding}, expected_digest=digest(adapter.profile.path().read_bytes()))
                    elif recipe == "python.route" and result.returncode == 0:
                        require(details_record.get("runtime_test_dependencies", []) == spec["selection"]["original_test_dependencies"],
                                "Python route used runtime witnesses outside its materialized inputs")
                        require(details_record.get("qualification_dependencies", []) == spec["selection"]["qualification_dependencies"],
                                "Python route used backend observations outside its materialized inputs")
                        require(details_record.get("qualification_lineage_digest") == spec["selection"]["qualification_lineage_digest"],
                                "Python route used qualification ancestry outside its materialized inputs")
                        adapter.update({"python_verification_routes": details_binding}, expected_digest=digest(adapter.profile.path().read_bytes()))
                    elif recipe == "python.qualify" and result.returncode == 0:
                        from .roadmap_python import backend_observation_key
                        backend = spec["selection"]["backend"]
                        require(details_record.get("backend") == backend, "qualification backend differs from its fixed selection")
                        adapter.update({backend_observation_key(backend, "qualification"): details_binding}, expected_digest=digest(adapter.profile.path().read_bytes()))
                if recipe == "native.acceptance":
                    require(details_record.get("accepted") is True, "native transport qualification is incomplete")
                    require(bindings_current(root, details_record.get("artifacts", [])), "native observation artifacts changed")
                    artifacts.extend(details_record["artifacts"])
                    update = {"native_transport_acceptance": details_binding, "native_capability_snapshot": details_record["capability_snapshot"],
                              "native_plan_observation": details_record["plan_observation"]}
                    current_record = adapter.read(); execution = dict(current_record["execution"])
                    execution["native_plan_binding"] = details_record["plan_binding"]
                    execution["plan_limitation"] = "Bound completed native Plan is byte-identical to the adopted source; managed inference/live Goal writes are separate qualified host capabilities."
                    update["execution"] = execution
                    adapter.update(update, expected_digest=digest(adapter.profile.path().read_bytes()))
            if recipe == "production.build":
                import importlib.util as bytecode
                for source in spec["selection"]["production"]:
                    absolute = str(root / source["path"])
                    path = root / spec["target"]["output"] / "pycache" / (absolute.lstrip("/").removesuffix(".py") + "." + sys.implementation.cache_tag + ".pyc")
                    raw = path.read_bytes()
                    require(raw[:4] == bytecode.MAGIC_NUMBER and int.from_bytes(raw[4:8], "little") == 3 and
                            raw[8:16] == bytecode.source_hash((root / source["path"]).read_bytes()),
                            "production bytecode does not bind current checked-hash source")
                    artifacts.append(file_binding(root, path.relative_to(root).as_posix()))
            receipt = {"schema": 1, "recipe": recipe, "inputs": spec["digest"], "candidate": spec["candidate"],
                       "argv": spec["argv"], "returncode": result.returncode, "timed_out": result.timed_out,
                       "truncated": result.stdout_truncated or result.stderr_truncated,
                       "stdout": result.stdout, "stderr": result.stderr, "artifacts": artifacts,
                       "tool_microseconds": int(result.duration_seconds * 1_000_000),
                       "domain_proof": False, "installed_artifact_acceptance": False}
            _immutable(root, directory + "/receipt.json", receipt)
            ok = receipt["returncode"] == 0 and not receipt["timed_out"] and not receipt["truncated"]
            ledger.close(attempt["id"], "SUCCESS" if ok else "FAILED", receipt)
            unit["continuation"].update(status="SUCCESS" if ok else "FAILED", receipt=receipt,
                                        reservation=ledger.reservation_record(attempt["id"]))
            if not ok and spec.get("execution_policy"):
                history = retained_history(ledger.read()["attempts"], work_id, inherited)
                unit["continuation"]["recovery_required"] = recovery_packet(work_id, operation["semantic_inputs"], history)
            _save_unit(adapter, unit)
            return dict(receipt, attempt=attempt["id"], reused=False)
        except BaseException as exc:
            observed = operation_state(operation)
            # Unknown/live descendants keep their reservation. A crash between
            # spawn and handle persistence also remains unknown on recovery.
            if not spawn_attempted or observed["child"] == "GONE" and observed["process_group"] == "GONE":
                if any(a["id"] == attempt["id"] and a["status"] == "RESERVED" for a in ledger.read()["attempts"]):
                    ledger.close(attempt["id"], "INTERRUPTED", {"error_type": type(exc).__name__,
                                 "observed": observed, "unknown_usage": True})
                    unit["continuation"].update(status="INTERRUPTED", reservation=ledger.reservation_record(attempt["id"]))
                    if spec.get("execution_policy"):
                        history = retained_history(ledger.read()["attempts"], work_id, inherited)
                        unit["continuation"]["recovery_required"] = recovery_packet(work_id, operation["semantic_inputs"], history)
                    _save_unit(adapter, unit)
            raise
    finally:
        lock.release()
