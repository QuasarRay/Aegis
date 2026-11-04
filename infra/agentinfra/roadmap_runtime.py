"""Durable local reservations and fixed-recipe execution; no model inference."""
from __future__ import annotations

import os
import time
from pathlib import Path

from .atomic import atomic_write_json
from .locks import FileLock
from .process import run_process
from .roadmap_records import bindings_current, digest, file_binding, read_json, require
from .security import confined_path
from .roadmap_lease import WorkspaceLease


def retry_limits(root: Path, milestone: str, recipe: str, max_attempts: int, total_seconds: int, *, candidate: str | None = None) -> dict:
    """Read a scoped user amendment through the existing canonical record owner."""
    from .roadmap_project import ProjectAdapter
    adapter = ProjectAdapter(root)
    if not adapter.profile.path().exists():
        return {"max_attempts": max_attempts, "total_seconds": total_seconds}
    record = adapter.read()
    execution = record.get("execution", {})
    native = execution.get("native_binding", {})
    work_id = digest({"recipe": recipe, "root": str(root.resolve()), "native_thread": native.get("thread_id"),
                      "project": "Aegis", "milestone": milestone})
    binding = execution.get("budget_amendments", {}).get(work_id)
    if not binding:
        return {"max_attempts": max_attempts, "total_seconds": total_seconds}
    require(bindings_current(root, [binding]), "user retry amendment changed")
    amendment = read_json(confined_path(root, binding["path"]))
    require(amendment.get("schema") == 1 and amendment.get("kind") == "user_authorized_single_retry" and
            amendment.get("work_id") == work_id and amendment.get("recipe") == recipe and
            amendment.get("milestone") == milestone and amendment.get("native_thread") == native.get("thread_id") and
            amendment.get("goal_created_at") == native.get("observation", {}).get("createdAt") and
            amendment.get("objective") == native.get("objective"), "retry amendment escaped its adopted Goal/work unit")
    source = amendment.get("source", {})
    require(source.get("role") == "user" and source.get("content") and source.get("question_item_id") and
            source.get("observed_native_turn"), "retry amendment lacks explicit user provenance")
    require(amendment.get("base_limits") == {"max_attempts": max_attempts, "total_seconds": total_seconds} and
            amendment.get("preserve_attempt_lineage") is True and amendment.get("domain_proof") is False,
            "retry amendment changed its base limits or evidence strength")
    limits = amendment.get("limits", {})
    extra = amendment.get("additional_seconds")
    require(type(extra) is int and 0 < extra <= 900 and limits == {
            "max_attempts": max_attempts + 1, "total_seconds": total_seconds + extra}, "retry amendment must add exactly one bounded attempt")
    dependencies = amendment.get("dependencies", [])
    prior = amendment.get("prior_attempts", [])
    ledger = BudgetLedger(root).read()["attempts"]
    rows = {a["id"]: a for a in ledger}
    fields = ("id", "work_id", "inputs", "status", "reserved_seconds", "generation")
    require(prior and all(p.get("work_id") == work_id and p.get("status") in {"FAILED", "INTERRUPTED"} and
            p["id"] in rows and p == {k: rows[p["id"]].get(k) for k in fields} for p in prior),
            "retry amendment lost or rewrote failed attempt history")
    generation = prior[-1]["generation"]
    retained = amendment.get("retained_history")
    if retained is not None:
        history = [a for a in ledger if a["work_id"] == work_id]
        require(retained and len(retained) >= len(prior) and
                retained == [{k: a.get(k) for k in fields} for a in history[:len(retained)]] and
                retained[-len(prior):] == prior, "retry amendment lost or rewrote retained attempt history")
    current = [a for a in ledger if a["work_id"] == work_id and a.get("generation") == generation]
    require([a["id"] for a in current[:len(prior)]] == [a["id"] for a in prior] and
            len(current) <= limits["max_attempts"] and all(a.get("generation") == generation for a in prior),
            "retry amendment cannot reset or replace its original generation")
    if any(a["work_id"] == work_id and a.get("generation", 1) > generation for a in ledger):
        return {"max_attempts": max_attempts, "total_seconds": total_seconds}
    if candidate is not None and len(current) > len(prior) and current[-1]["status"] == "SUCCESS":
        spec_binding = current[-1].get("operation", {}).get("spec")
        require(spec_binding and bindings_current(root, [spec_binding]), "consumed retry lacks its immutable successful specification")
        completed = read_json(confined_path(root, spec_binding["path"]))
        require(completed.get("digest") == current[-1]["inputs"] == digest({k: v for k, v in completed.items() if k != "digest"}),
                "consumed retry specification changed")
        if completed.get("candidate") != candidate:
            return {"max_attempts": max_attempts, "total_seconds": total_seconds}
    require(dependencies and bindings_current(root, dependencies), "retry amendment inputs changed; renewed user scope required")
    return dict(limits, authorization=binding, dependencies=dependencies)


def authorize_single_retry(root: Path, compiled: dict, milestone: str, recipe: str, *,
                           user_authorized: bool, source: dict, dependencies: list[dict]) -> dict:
    """Record user scope for the exhausted latest generation, retaining history.

    The controlling Goal alone never authorizes another attempt.
    """
    from .roadmap_project import ProjectAdapter
    require(user_authorized and source.get("role") == "user" and source.get("content") and
            source.get("question_item_id") and source.get("observed_native_turn"), "explicit observed user retry authorization required")
    adapter = ProjectAdapter(root)
    record_digest = digest(adapter.profile.path().read_bytes())
    record = adapter.read()
    require(digest(adapter.profile.path().read_bytes()) == record_digest, "canonical record changed while reading retry authority")
    execution = record["execution"]
    observation = WorkspaceLease(root).qualify(execution["workspace_lease"])
    require(observation["turn_id"] == source["observed_native_turn"] and observation["goal"]["status"] == "active",
            "retry authorization must be recorded in the observed active native turn")
    work_id, inherited = recipe_scope(root, compiled, recipe, milestone, BudgetLedger(root))
    require(not inherited and work_id not in execution.get("budget_amendments", {}), "retry amendment already exists or has unresolved inherited accounting")
    contract = compiled["milestones"][milestone]
    require(recipe in contract["checks"] and dependencies and bindings_current(root, dependencies), "retry dependencies/scope are not current")
    seconds = min(compiled["recipes"][recipe]["max_seconds"], contract["budget_policy"]["max_seconds_per_recipe"])
    attempts = min(compiled["recipes"][recipe]["max_attempts"], contract["budget_policy"]["max_attempts"])
    history = [a for a in BudgetLedger(root).read()["attempts"] if a["work_id"] == work_id]
    generation = history[-1].get("generation", 1) if history else None
    prior = [a for a in history if a.get("generation", 1) == generation]
    require(type(generation) is int and generation > 0 and
            all(a["status"] in {"SUCCESS", "FAILED", "INTERRUPTED"} and
                a.get("generation", 1) <= generation for a in history) and
            len(prior) == attempts and all(a["status"] in {"FAILED", "INTERRUPTED"} and
            a.get("generation", 1) == prior[-1].get("generation", 1) for a in prior) and
            sum(a["reserved_seconds"] for a in prior) == 1800, "single retry requires intact exhausted failed history")
    native = execution["native_binding"]
    require(observation["goal"]["threadId"] == native["thread_id"] and observation["goal"]["objective"] == native["objective"] and
            observation["goal"]["createdAt"] == native["observation"]["createdAt"], "retry authorization cannot replace the native Goal")
    fields = ("id", "work_id", "inputs", "status", "reserved_seconds", "generation")
    amendment = {"schema": 1, "kind": "user_authorized_single_retry", "work_id": work_id, "recipe": recipe,
                 "milestone": milestone, "native_thread": native["thread_id"], "objective": native["objective"],
                 "goal_created_at": native["observation"]["createdAt"], "source": source, "dependencies": dependencies,
                 "base_limits": {"max_attempts": attempts, "total_seconds": 1800},
                 "limits": {"max_attempts": attempts + 1, "total_seconds": 1800 + seconds}, "additional_seconds": seconds,
                 "prior_attempts": [{k: a.get(k) for k in fields} for a in prior],
                 "retained_history": [{k: a.get(k) for k in fields} for a in history],
                 "preserve_attempt_lineage": True, "domain_proof": False}
    relative = ".aegis/roadmaps/authorizations/" + digest(amendment) + ".json"
    atomic_write_json(confined_path(root, relative), amendment, root=root, mode=0o600)
    execution = dict(execution, budget_amendments=dict(execution.get("budget_amendments", {}), **{work_id: file_binding(root, relative)}))
    adapter.update({"execution": execution}, expected_digest=record_digest)
    return amendment


class BudgetLedger:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.path = confined_path(self.root, ".aegis/roadmaps/reservations.json")
        self.lock = self.path.with_suffix(".lock")

    def read(self) -> dict:
        if not self.path.exists():
            return {"schema": 1, "attempts": [], "usage": {}}
        record = read_json(self.path)
        require(record.get("schema") == 1 and isinstance(record.get("attempts"), list)
                and isinstance(record.get("usage"), dict), "unsupported/corrupt budget ledger")
        return record

    def reserve(self, work_id: str, inputs: str, seconds: int, *, max_attempts: int = 2,
                total_seconds: int = 1800, diagnosis: str | None = None,
                inherited_attempt_ids: tuple[str, ...] = ()) -> dict:
        return self._reserve(work_id, inputs, seconds, max_attempts=max_attempts, total_seconds=total_seconds,
                             diagnosis=diagnosis, inherited_attempt_ids=inherited_attempt_ids)

    def reserve_operation(self, work_id: str, inputs: str, seconds: int, operation: dict, *,
                          max_attempts: int = 2, total_seconds: int = 1800, diagnosis: str | None = None,
                          inherited_attempt_ids: tuple[str, ...] = ()) -> dict:
        return self._reserve(work_id, inputs, seconds, max_attempts=max_attempts, total_seconds=total_seconds,
                             diagnosis=diagnosis, inherited_attempt_ids=inherited_attempt_ids, operation=operation)

    def reserve_control(self, work_id: str, inputs: str, seconds: int, operation: dict, *,
                        user_authorized: bool, diagnosis: str | None = None) -> dict:
        require(user_authorized and operation.get("kind") == "native_lifecycle_control" and
                operation.get("native_thread") and operation.get("authorization_id"), "explicit native control authorization required")
        return self._reserve(work_id, inputs, seconds, max_attempts=2, total_seconds=120,
                             diagnosis=diagnosis, operation=operation, native_control=True)

    def _reserve(self, work_id: str, inputs: str, seconds: int, *, max_attempts: int = 2,
                 total_seconds: int = 1800, diagnosis: str | None = None,
                 inherited_attempt_ids: tuple[str, ...] = (), operation: dict | None = None,
                 native_control: bool = False) -> dict:
        require(bool(work_id) and bool(inputs), "work and input identities required")
        require(type(seconds) is int and 0 < seconds <= total_seconds, "invalid finite reservation")
        require(type(max_attempts) is int and max_attempts > 0, "invalid attempt limit")
        lock = FileLock(self.lock, "roadmap budget reservation")
        lock.acquire()
        try:
            record = self.read()
            def blocks(candidate: dict) -> bool:
                if candidate["status"] != "RESERVED": return False
                parent = candidate.get("operation", {})
                if native_control: return parent.get("kind") == "native_lifecycle_control"
                if (operation and operation.get("parent_native_attempt") == candidate["id"] and
                        operation.get("kind") == "deterministic_recipe" and
                        parent.get("kind") == "native_model_turn" and operation.get("owner") == parent.get("owner") and
                        parent.get("child") and parent.get("turn_id")):
                    from .roadmap_native import inspect_process, is_process_ancestor
                    return not (inspect_process(parent["child"]) == "LIVE" and is_process_ancestor(parent["child"]["pid"]))
                return True
            require(not any(blocks(a) for a in record["attempts"]),
                    "existing workspace operation requires recovery, not redispatch")
            by_id = {a["id"]: a for a in record["attempts"]}
            require(len(by_id) == len(record["attempts"]), "duplicate durable attempt identity")
            selected = {a["id"] for a in record["attempts"] if a["work_id"] == work_id}
            selected.update(inherited_attempt_ids)
            pending = list(selected)
            while pending:
                ident = pending.pop()
                require(ident in by_id, "inherited attempt is missing from the durable ledger")
                for ancestor in by_id[ident].get("inherited_attempt_ids", []):
                    if ancestor not in selected:
                        selected.add(ancestor)
                        pending.append(ancestor)
            prior = [a for a in record["attempts"] if a["id"] in selected]
            bounded_prior = prior
            generation = 1
            generation_parent = None
            if operation is not None:
                require(operation.get("spec_digest") == inputs and operation.get("runner") and
                        operation.get("state") == "PREPARED", "bound operation journal required before dispatch")
                reusable = [a for a in record["attempts"] if a["status"] == "SUCCESS" and a["inputs"] == inputs
                            and a.get("operation", {}).get("spec_digest") == inputs]
                for successful in reversed(reusable):
                    receipt = successful.get("receipt", {})
                    if bindings_current(self.root, receipt.get("artifacts", [])):
                        if successful.get("operation", {}).get("kind") == "native_model_turn":
                            from .roadmap_managed import validate_native_turn_receipt
                            try:
                                saved_spec = read_json(confined_path(self.root, successful["operation"]["spec"]["path"]))
                                validate_native_turn_receipt(self.root, saved_spec, receipt, current_outputs=True)
                            except ValueError:
                                continue
                        successful.setdefault("reuse_consumers", [])
                        if work_id not in successful["reuse_consumers"]:
                            successful["reuse_consumers"].append(work_id)
                        atomic_write_json(self.path, record, root=self.root, mode=0o600)
                        return dict(successful, reused=True)
                if not native_control and prior:
                    generation = prior[-1].get("generation", 1)
                    supersedes = operation.get("supersedes_success")
                    if supersedes:
                        previous = prior[-1]
                        require(previous["id"] == supersedes and previous["status"] == "SUCCESS" and
                                previous["inputs"] != inputs, "new target generation requires the latest successful operation")
                        spec_binding = previous.get("operation", {}).get("spec")
                        require(spec_binding and bindings_current(self.root, [spec_binding]), "successful generation lacks its original specification")
                        spec = read_json(confined_path(self.root, spec_binding["path"]))
                        require(spec.get("digest") == previous["inputs"] == digest({k: v for k, v in spec.items() if k != "digest"}),
                                "successful generation specification identity changed")
                        if spec.get("kind") == "managed_native_turn":
                            from .roadmap_managed import validate_native_turn_receipt
                            validate_native_turn_receipt(self.root, spec, previous["receipt"])
                        else:
                            from .roadmap_work import validate_tool_receipt
                            validate_tool_receipt(self.root, spec, previous["receipt"])
                            require(previous["receipt"]["returncode"] == 0 and not previous["receipt"]["timed_out"] and
                                    not previous["receipt"]["truncated"], "new generation cannot supersede unsuccessful work")
                        generation += 1
                        generation_parent = supersedes
                        bounded_prior = []
                    else:
                        require(prior[-1]["status"] != "SUCCESS" or prior[-1]["inputs"] == inputs,
                                "changed successful target requires explicit generation lineage")
                        bounded_prior = [a for a in prior if a.get("generation", 1) == generation]
            require(not any(a["status"] == "RESERVED" for a in prior), "existing operation requires recovery, not redispatch")
            require(not any(a["status"] == "SUCCESS" and a["inputs"] == inputs for a in prior), "matching successful work already exists")
            require(len(bounded_prior) < max_attempts, "durable attempt limit exhausted")
            require(sum(a["reserved_seconds"] for a in bounded_prior) + seconds <= total_seconds, "durable time limit exhausted")
            if bounded_prior:
                require(bool(diagnosis and diagnosis.strip()), "retry requires diagnosis")
                require(bounded_prior[-1]["inputs"] != inputs, "unchanged failed inputs cannot retry")
            attempt = {"id": digest({"work": work_id, "inputs": inputs, "ordinal": len(prior) + 1}),
                       "work_id": work_id, "inputs": inputs, "reserved_seconds": seconds,
                       "status": "RESERVED", "diagnosis": diagnosis, "pid": os.getpid(),
                       "created_ns": time.time_ns()}
            if selected:
                attempt["inherited_attempt_ids"] = sorted(selected)
            if operation is not None:
                attempt["operation"] = operation
                attempt.update(generation=generation, generation_parent=generation_parent,
                               attempt_in_generation=len(bounded_prior) + 1)
            record["attempts"].append(attempt)
            atomic_write_json(self.path, record, root=self.root, mode=0o600)
            return attempt
        finally:
            lock.release()

    def journal(self, ident: str, operation: dict) -> dict:
        """CAS-like advancement of this ledger's existing nonterminal operation."""
        lock = FileLock(self.lock, "roadmap operation observation"); lock.acquire()
        try:
            record = self.read()
            matches = [a for a in record["attempts"] if a["id"] == ident]
            require(len(matches) == 1 and matches[0]["status"] == "RESERVED", "operation is not reserved")
            attempt = matches[0]
            old = attempt.get("operation", {})
            require(operation.get("state") == "RUNNING" and old.get("state") in {"PREPARED", "RUNNING"},
                    "operation journal only advances a prepared/running dispatch")
            require(old.get("spec_digest") == operation.get("spec_digest") and
                    old.get("runner") == operation.get("runner") and old.get("owner") == operation.get("owner"),
                    "operation identity/owner cannot change")
            require(old.get("child") is None or old["child"] == operation.get("child"),
                    "observed child creation identity cannot change")
            attempt["operation"] = operation
            atomic_write_json(self.path, record, root=self.root, mode=0o600)
            return attempt
        finally:
            lock.release()

    def observe_categories(self, thread_id: str, event_id: str, totals: dict, origin: dict) -> dict:
        """Reconcile one native session series, separately from Goal accounting.

        Cached input is part of input; reasoning output is part of output. These
        categories are never added together to manufacture tokens or billing.
        """
        fields = {"input_tokens", "cached_input_tokens", "cache_write_input_tokens", "output_tokens",
                  "reasoning_output_tokens", "total_tokens"}
        require(bool(thread_id) and bool(event_id) and bool(origin) and set(totals) <= fields,
                "native category observation identity/fields required")
        require(all(v is None or type(v) is int and v >= 0 for v in totals.values()), "invalid native token category")
        sample = {"totals": {k: totals.get(k) for k in sorted(fields)}, "origin": origin}
        lock = FileLock(self.lock, "native category reconciliation"); lock.acquire()
        try:
            record = self.read()
            series = record["usage"].setdefault("native-session:" + thread_id,
                     {"kind": "native_session_cumulative", "thread_id": thread_id,
                      "totals": {k: None for k in sorted(fields)}, "events": {}})
            if event_id in series["events"]:
                require(series["events"][event_id] == sample, "conflicting duplicate native category event")
                return series
            for field, value in sample["totals"].items():
                previous = series["totals"][field]
                require(value is None or previous is None or value >= previous,
                        "decreasing native category requires reconciliation")
            series["events"][event_id] = sample
            for field, value in sample["totals"].items():
                if value is not None:
                    series["totals"][field] = value
            atomic_write_json(self.path, record, root=self.root, mode=0o600)
            return series
        finally:
            lock.release()

    def metrics(self) -> dict:
        record = self.read()
        attempts = record["attempts"]
        measured = [a["receipt"]["tool_microseconds"] for a in attempts
                    if type(a.get("receipt", {}).get("tool_microseconds")) is int]
        return {"schema": 1, "attempts": len(attempts),
                "outcomes": {s: sum(a["status"] == s for a in attempts)
                             for s in ("RESERVED", "SUCCESS", "FAILED", "INTERRUPTED")},
                "reserved_seconds": sum(a["reserved_seconds"] for a in attempts),
                "observed_tool_microseconds": sum(measured) if measured else None,
                "tool_time_unknown_attempts": len(attempts) - len(measured),
                "reuse_consumers": sum(len(a.get("reuse_consumers", [])) for a in attempts),
                "native_series": {k: {f: v for f, v in s.items() if f != "events"} for k, s in record["usage"].items()},
                "ci_microseconds": None, "storage_bytes": None, "price_estimate": None, "billed_amount": None,
                "limits": ["No observed prices or billing; no enforceable monetary cap",
                           "Goal totals and native session categories are separate cumulative series",
                           "Historical reservations remain consumed; unknown measurements are not zero"]}

    def reservation_record(self, ident: str) -> dict:
        """Version-one quota record; consumed is allocation, not measured time."""
        from .roadmap_records import validate_record
        matches = [a for a in self.read()["attempts"] if a["id"] == ident]
        require(len(matches) == 1, "unknown reservation")
        attempt = matches[0]
        value = {"schema": 1, "id": ident, "work_id": attempt["work_id"], "inputs": attempt["inputs"],
                 "reserved": attempt["reserved_seconds"], "consumed": attempt["reserved_seconds"],
                 "unknown_usage": type(attempt.get("receipt", {}).get("tool_microseconds")) is not int,
                 "attempt": attempt.get("attempt_in_generation", len(attempt.get("inherited_attempt_ids", [])) + 1), "status": attempt["status"],
                 "reconciliation": "Seconds of irrevocable attempt allocation; consumed allocation is not observed runtime or billing. Actual microseconds are separate, unknown when unavailable."}
        validate_record(self.root, "BudgetReservation", value)
        return value

    def close(self, ident: str, outcome: str, receipt: dict) -> None:
        require(outcome in {"SUCCESS", "FAILED", "INTERRUPTED"}, "unknown terminal outcome")
        lock = FileLock(self.lock, "roadmap budget reconciliation")
        lock.acquire()
        try:
            record = self.read()
            matches = [a for a in record["attempts"] if a["id"] == ident]
            require(len(matches) == 1 and matches[0]["status"] == "RESERVED", "unknown or already terminal attempt")
            matches[0].update(status=outcome, receipt=receipt)
            if "operation" in matches[0]:
                matches[0]["operation"]["state"] = outcome
                matches[0]["operation"]["closed_ns"] = time.time_ns()
            atomic_write_json(self.path, record, root=self.root, mode=0o600)
        finally:
            lock.release()

    def observe_usage(self, thread_id: str, event_id: str, total: int | None) -> dict:
        require(bool(thread_id) and bool(event_id), "native usage identity required")
        require(total is None or (type(total) is int and total >= 0), "invalid cumulative usage")
        lock = FileLock(self.lock, "native usage reconciliation")
        lock.acquire()
        try:
            record = self.read()
            usage = record["usage"].setdefault(thread_id, {"total": None, "events": {}})
            if event_id in usage["events"]:
                require(usage["events"][event_id] == total, "conflicting duplicate usage event")
                return dict(usage)
            if total is not None and usage["total"] is not None:
                require(total >= usage["total"], "native accounting reset or out-of-order event requires reconciliation")
            usage["events"][event_id] = total
            if total is not None:
                usage["total"] = total
            atomic_write_json(self.path, record, root=self.root, mode=0o600)
            return dict(usage)
        finally:
            lock.release()


def recipe_scope(root: Path, compiled: dict, name: str, milestone: str,
                 ledger: BudgetLedger) -> tuple[str, tuple[str, ...]]:
    """Bind local validation to the adopted native execution, retaining old attempts.

    The old fixed runner had no chat identity. Its attempts within this Goal's
    lifetime are retained as ancestors. Earlier authoring Goals stay in their
    own lineage. This is local tool accounting, not managed model dispatch.
    """
    require(milestone in compiled["milestones"] and compiled["milestones"][milestone]["project"] == "Aegis",
            "local recipe scope must name an Aegis milestone")
    path = confined_path(root, compiled["projects"]["Aegis"]["canonical_record"], must_exist=True)
    record = read_json(path)
    execution = record.get("execution", {})
    binding = execution.get("native_binding", {})
    goal = binding.get("observation", {})
    thread = binding.get("thread_id")
    require(record.get("schema") == 1 and record.get("project") == "Aegis" and bool(thread),
            "adopted canonical native execution required")
    require(goal.get("threadId", goal.get("thread_id")) == thread and
            goal.get("objective") == binding.get("objective") and goal.get("status") == "active",
            "native execution identity is mismatched or inactive")
    require(milestone in execution.get("scope", []) and
            record.get("continuation", {}).get("milestone") == milestone,
            "recipe is outside the current adopted work unit")
    owner = execution.get("workspace_lease", {})
    require(owner.get("session") == thread, "recipe owner differs from the native execution")
    WorkspaceLease(root).assert_owner(owner)
    created = goal.get("createdAt")
    require(type(created) is int and created > 0, "native Goal lifetime must be observed for legacy attribution")
    continuation = record["continuation"]
    started = continuation.get("started_ns")
    if started is None and milestone == "A00":
        started = created * 1_000_000_000  # Preserve the bootstrap's known attribution boundary.
    require(type(started) is int and started >= created * 1_000_000_000,
            "current work-unit start must be observed for legacy attribution")
    legacy = digest({"recipe": name, "root": str(root.resolve())})
    inherited = tuple(a["id"] for a in ledger.read()["attempts"]
                      if a["work_id"] == legacy and a["created_ns"] >= started)
    work_id = digest({"recipe": name, "root": str(root.resolve()), "native_thread": thread,
                      "project": "Aegis", "milestone": milestone})
    return work_id, inherited


def run_recipe(root: Path, compiled: dict, name: str, *, diagnosis: str | None = None,
               milestone: str | None = None) -> dict:
    if milestone is not None:
        from .roadmap_work import run_work
        return run_work(root, compiled, milestone, name, diagnosis=diagnosis)
    canonical_record = root / ".aegis/project.json"
    require(not canonical_record.exists() or not read_json(canonical_record).get("execution"),
            "adopted execution requires an explicit current milestone")
    require(bindings_current(root, compiled["inputs"]), "compiled execution inputs became stale")
    require(name in compiled["recipes"], "undeclared recipe")
    recipe = compiled["recipes"][name]
    require(recipe["kind"] == "local_validation", "this recipe is a project execution specification, not an activated command")
    require(recipe["argv"] and recipe["argv"][0] == "python", "only fixed local Python validation recipes are supported")
    import sys
    argv = [sys.executable, *recipe["argv"][1:]]
    require(all(type(x) is str for x in argv), "invalid argv")
    work_id = digest({"recipe": name, "root": str(root.resolve())})
    inputs = digest({"compiled": compiled["digest"], "recipe": recipe})
    ledger = BudgetLedger(root)
    inherited = ()
    if milestone is not None:
        work_id, inherited = recipe_scope(root, compiled, name, milestone, ledger)
    lease = FileLock(root / ".aegis/roadmaps/execution.lock", "single roadmap recipe execution")
    lease.acquire(timeout=0)
    try:
        attempt = ledger.reserve(work_id, inputs, recipe["max_seconds"],
                                 max_attempts=recipe["max_attempts"], diagnosis=diagnosis,
                                 inherited_attempt_ids=inherited)
        try:
            result = run_process(argv, cwd=root, timeout=recipe["max_seconds"], capture_limit=100_000)
            receipt = {"schema": 1, "recipe": name, "inputs": inputs, "argv": argv,
                       "returncode": result.returncode, "timed_out": result.timed_out,
                       "truncated": result.stdout_truncated or result.stderr_truncated,
                       "stdout": result.stdout, "stderr": result.stderr}
            ok = result.returncode == 0 and not result.timed_out and not receipt["truncated"]
        except BaseException as exc:
            ledger.close(attempt["id"], "INTERRUPTED", {"error_type": type(exc).__name__})
            raise
        ledger.close(attempt["id"], "SUCCESS" if ok else "FAILED", receipt)
        return receipt
    finally:
        lease.release()
