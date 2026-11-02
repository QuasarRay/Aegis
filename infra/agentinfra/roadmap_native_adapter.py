"""Observed Goal/Plan adapters over pinned read-only native contracts.

Native Goal writes stay with an explicitly supplied host lifecycle callback.
These adapters never create/resume chats, start inference or replace objectives.
Only final persisted Plan text, lifecycle/configuration metadata and hashes are
retained; reasoning payloads and arbitrary tool output are not copied.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from .roadmap import audit_evidence, compile_roadmaps
from .roadmap_codex import CodexReader, CodexRpcError, bind_goal, bind_plan
from .roadmap_lease import WorkspaceLease
from .roadmap_policy import goal_transition
from .roadmap_project import ProjectAdapter
from .roadmap_protocol import assert_protocol
from .roadmap_records import ContractError, bindings_current, digest, read_json, require, validate_record
from .roadmap_verification import reconcile_native_transition
from .security import confined_path


INTERFACE_VERSION = 1
READ_CONTRACTS = {
    "model/list": "ModelList", "collaborationMode/list": "CollaborationModeList",
    "thread/read": "ThreadRead", "thread/list": "ThreadList", "thread/goal/get": "ThreadGoalGet",
    "thread/turns/list": "ThreadTurnsList", "thread/items/list": "ThreadItemsList",
}


class NativeRpc:
    """Bounded metadata/history reads with actual request/reply provenance."""
    def __init__(self, root: Path, protocol: dict):
        self.root = root.resolve()
        self.protocol = protocol
        self.calls = []
        self.client = None
        self.event_state = None
        self.event_cursor = 0

    def watch(self, native_observation: dict) -> None:
        self.event_state = NativeEventState(native_observation["session"], native_observation["model"])
        self.event_state.turn_id = native_observation["turn_id"]
        self.event_state.status = "inProgress" if native_observation["status"] == "active" else "UNKNOWN"

    def __enter__(self):
        assert_protocol(self.root, self.protocol)
        self.client = CodexReader(executable=self.protocol["executable"]["path"], experimental=True)
        self.client.__enter__()
        self.calls.append({"method": "initialize", "status": "OBSERVED", "response_digest": digest(self.client.initialization),
                           "request_contract": self.protocol["selected"]["InitializeParams"],
                           "response_contract": self.protocol["selected"]["InitializeResponse"],
                           "observed_at": datetime.now(timezone.utc).isoformat()})
        return self

    def __exit__(self, *args):
        if self.client is not None:
            self.client.__exit__(*args)

    def call(self, method: str, params: dict) -> dict:
        require(method in READ_CONTRACTS and self.client is not None, "native adapter refuses unqualified/mutating method")
        assert_protocol(self.root, self.protocol)
        prefix = READ_CONTRACTS[method]
        request_schema = read_json(confined_path(self.root, self.protocol["selected"][prefix + "Params"]["path"]))
        require(set(params) <= set(request_schema.get("properties", {})) and
                set(request_schema.get("required", [])) <= set(params), "request differs from installed native contract")
        for key in ("threadId", "turnId"):
            if key in params:
                require(type(params[key]) is str and 0 < len(params[key]) <= 128, "invalid native thread/turn identity")
        if method == "thread/read":
            require(params.get("includeTurns") is False, "full history must use bounded item pagination")
        if "limit" in params:
            require(type(params["limit"]) is int and 1 <= params["limit"] <= 20, "native read page must be bounded")
        if "cursor" in params:
            require(type(params["cursor"]) is str and 0 < len(params["cursor"]) <= 4000, "invalid opaque cursor")
        if method == "thread/turns/list":
            require(params.get("itemsView") == "notLoaded", "turn metadata cannot hydrate unrelated item contents")
        if method == "thread/items/list":
            require(bool(params.get("turnId")), "Plan item reads require an explicit source turn")
        observed = {"method": method, "request_digest": digest(params), "observed_at": datetime.now(timezone.utc).isoformat(),
                    "request_contract": self.protocol["selected"][prefix + "Params"],
                    "response_contract": self.protocol["selected"][prefix + "Response"]}
        try:
            reply = self.client.call(method, params)
        except CodexRpcError as error:
            observed.update(status="REJECTED", error_code=error.code, message=error.message)
            self.calls.append(observed)
            raise
        except (TimeoutError, OSError):
            observed.update(status="UNKNOWN")
            self.calls.append(observed)
            raise
        response_schema = read_json(confined_path(self.root, observed["response_contract"]["path"]))
        if not isinstance(reply, dict) or not set(response_schema.get("required", [])) <= set(reply):
            observed.update(status="INVALID_NATIVE_REPLY", response_digest=digest(reply))
            self.calls.append(observed)
            raise ContractError("native reply omits required contract fields")
        if self.event_state is not None:
            selected_events = {"turn/started", "turn/completed", "item/started", "item/completed", "item/plan/delta",
                               "turn/plan/updated", "model/rerouted", "thread/tokenUsage/updated"}
            for event in self.client.events[self.event_cursor:]:
                if event.get("method") in selected_events and event.get("params", {}).get("threadId") == self.event_state.thread_id:
                    self.event_state.consume(event)
            self.event_cursor = len(self.client.events)
            if self.event_state.blockers:
                observed.update(status="OBSERVED_POLICY_REFUSED", response_digest=digest(reply), blockers=list(self.event_state.blockers))
                self.calls.append(observed)
                raise ContractError("native stream reported rerouting or an unqualified observation")
        observed.update(status="OBSERVED", response_digest=digest(reply))
        self.calls.append(observed)
        return reply

    def turns(self, thread_id: str) -> list[dict]:
        turns, cursor, seen = [], None, set()
        for _ in range(20):
            params = {"threadId": thread_id, "itemsView": "notLoaded", "limit": 20, "sortDirection": "desc"}
            if cursor:
                params["cursor"] = cursor
            reply = self.call("thread/turns/list", params)
            for turn in reply["data"]:
                require(turn["id"] not in seen, "duplicate native turn identity")
                seen.add(turn["id"])
                turns.append({"id": turn["id"], "status": turn["status"],
                              "error_class": (turn.get("error") or {}).get("codexErrorInfo")})
            cursor = reply.get("nextCursor")
            if not cursor:
                return turns
        raise ContractError("native turn history exceeds bounded discovery; select a narrower source")


def observe_goal(root: Path, rpc: NativeRpc, compiled: dict, previous: dict) -> dict:
    goal = rpc.call("thread/goal/get", {"threadId": previous["thread_id"]})["goal"]
    require(isinstance(goal, dict), "native Goal is cleared; preserve its prior identity and accounting")
    binding = bind_goal(goal, thread_id=previous["thread_id"], objective=previous["objective"], contract_hash=compiled["digest"])
    created = previous.get("observation", {}).get("createdAt")
    require(created is None or type(created) is int and type(goal.get("createdAt")) is int and goal["createdAt"] == created,
            "native Goal was replaced/recreated")
    for key in ("tokensUsed", "timeUsedSeconds"):
        old = previous.get("observation", {}).get(key)
        new = goal.get(key)
        require(type(new) is int and new >= 0 and (old is None or new >= old), "native accounting decreased or became unknown")
    validate_record(root, "GoalBinding", binding)
    return binding


def observe_plan(root: Path, rpc: NativeRpc, source: dict, compiled: dict, milestones: list[str]) -> dict:
    thread_id, turn_id, item_id = (source[k] for k in ("thread_id", "turn_id", "item_id"))
    thread = rpc.call("thread/read", {"threadId": thread_id, "includeTurns": False})["thread"]
    require(thread["id"] == thread_id and Path(thread["cwd"]).resolve() == root.resolve(), "native Plan belongs to another workspace")
    turns = rpc.turns(thread_id)
    require(any(t["id"] == turn_id and t["status"] == "completed" for t in turns), "native Plan source turn is not completed")
    cursor, seen = None, set()
    for _ in range(40):
        params = {"threadId": thread_id, "turnId": turn_id, "limit": 4, "sortDirection": "desc"}
        if cursor:
            params["cursor"] = cursor
        reply = rpc.call("thread/items/list", params)
        for entry in reply["data"]:
            require(entry["turnId"] == turn_id, "native item escaped its selected source turn")
            item = entry["item"]
            require(item["id"] not in seen, "duplicate native item identity")
            seen.add(item["id"])
            if item["id"] != item_id:
                continue
            require(item.get("type") == "plan" and type(item.get("text")) is str and item["text"],
                    "selected source is not a completed native Plan item")
            # Match the actual maintained adopted authority, byte for byte.
            # Prose from an unrelated chat cannot be relabeled as this plan.
            authority = source["adopted_source"]
            require(bindings_current(root, [authority]) and digest(item["text"].encode()) == source["text_sha256"] == authority["sha256"] and
                    item["text"].encode() == confined_path(root, authority["path"]).read_bytes(), "native Plan differs from the adopted source authority")
            binding = bind_plan(item, milestones, compiled)
            validate_record(root, "PlanBinding", binding)
            return {"schema": INTERFACE_VERSION, "binding": binding, "source": source,
                    "source_thread": {"id": thread_id, "cwd": thread["cwd"]}, "source_turn_status": "completed",
                    "item": {"type": "plan", "id": item_id, "text": item["text"]},
                    "turn_observations": turns, "producer": "installed_native_read_transport",
                    "limits": ["Persisted completed Plan item and exact adopted authority; no new model turn",
                               "Mapping the plan preserves current amendments and does not activate a Goal"]}
        cursor = reply.get("nextCursor")
        if not cursor:
            break
    raise ContractError("required native Plan item is absent from the bounded selected source turn")


def capability_snapshot(root: Path, rpc: NativeRpc, native: dict) -> dict:
    models, cursor = [], None
    for _ in range(20):
        reply = rpc.call("model/list", {"cursor": cursor} if cursor else {})
        models.extend(reply["data"])
        cursor = reply.get("nextCursor")
        if not cursor:
            break
    require(not cursor, "native model catalog pagination exceeded bound")
    selected = [m for m in models if m.get("model") == native["model"]]
    require(len(selected) == 1 and any(e["reasoningEffort"] == "max" for e in selected[0]["supportedReasoningEfforts"]),
            "selected native model has no advertised max effort")
    modes = rpc.call("collaborationMode/list", {})["data"]
    require(native["effort"] == "max" and native["mode"] == "default" and native["caller_is_descendant"],
            "actual active-host reasoning/mode/ancestry not established")
    value = {"schema": 1, "provider": "codex", "requested_effort": "max", "accepted_effort": native["effort"],
             "effective_effort": native["effort"], "observed_at": datetime.now(timezone.utc).isoformat(),
             "transport": "installed stdio read transport plus active-host metadata observation",
             "versions": {"executable": rpc.protocol["executable"], "protocol_digest": rpc.protocol["digest"],
                          "selected_model": native["model"], "native_turn_id": native["turn_id"],
                          "configuration_origin": native["metadata"]["context"]["origin"],
                          "collaboration_modes": modes, "selected_model_catalog": selected[0],
                          "effective_effort_boundary": "verified native turn configuration",
                          "event_feed": "read-only observer; managed inference stream is not subscribed or dispatched",
                          "goal_writes": "host lifecycle callback required; no live Goal mutation exercised",
                          "managed_adapter": {"read_rpc": "EXERCISED", "goal_mutation_transport": "REQUIRED_NOT_IMPLEMENTED",
                                              "turn_lifecycle": "REQUIRED_NOT_IMPLEMENTED"},
                          "managed_inference": "not dispatched by this active-host adapter"},
             "operations": sorted({c["method"] for c in rpc.calls if c["status"] == "OBSERVED"})}
    validate_record(root, "CapabilitySnapshot", value)
    return value


class NativeGoalAdapter:
    """Prepare and reconcile host lifecycle operations with one authorization path."""
    def __init__(self, root: Path, protocol: dict):
        self.root = root.resolve()
        self.protocol = protocol

    def prepare(self, action: str, *, user_authorized: bool, token_budget: int | None = None) -> dict:
        record = ProjectAdapter(self.root).read()
        compiled = compile_roadmaps(self.root)
        owner = record["execution"]["workspace_lease"]
        observation = WorkspaceLease(self.root).qualify(owner)
        require(observation["caller_is_descendant"], "native lifecycle action lacks its owned host process")
        if action in {"complete", "resume"}:
            require(observation["effort"] == "max" and observation["mode"] == "default" and
                    observation["model"] == record["execution"]["native_turn_configuration"]["model"],
                    "native completion/activation lacks its execution mode/model/reasoning")
        with NativeRpc(self.root, self.protocol) as rpc:
            rpc.watch(observation)
            binding = observe_goal(self.root, rpc, compiled, record["execution"]["native_binding"])
            calls = list(rpc.calls)
        acceptance = False
        evidence_binding = record.get("roadmap_evidence")
        if action == "complete":
            require(evidence_binding and bindings_current(self.root, [evidence_binding]), "current full-objective acceptance is missing")
            evidence = read_json(confined_path(self.root, evidence_binding["path"]))
            audit = audit_evidence(self.root, compiled, evidence)
            scope = record["execution"]["scope"]
            require(scope and all(audit["milestones"][m]["state"] == "SATISFIED" for m in scope),
                    "the full adopted native objective is not complete")
            domain_required = any("full_domain_proof" in compiled["milestones"][m]["gates"] for m in scope)
            required = {p["id"] for p in record.get("pending_proof_obligations", [])
                        if domain_required and p["id"].split("-", 1)[0] in scope}
            actual = {p["obligation"]["obligation_id"] for receipt in evidence["receipts"]
                      if receipt["gate"] == "full_domain_proof" and receipt["outcome"] == "PASS" for p in receipt.get("proofs", [])}
            require(required <= actual, "pending required domain obligations prohibit native completion")
            acceptance = True
        current = dict(binding["observation"], thread_id=binding["thread_id"])
        requested = {"action": action, "thread_id": binding["thread_id"], "objective": binding["objective"]}
        if token_budget is not None:
            schema = read_json(confined_path(self.root, self.protocol["selected"]["ThreadGoalSetParams"]["path"]))
            require(schema["properties"]["tokenBudget"].get("format") == "int64" and type(token_budget) is int and
                    0 < token_budget <= 2 ** 63 - 1, "token budget is outside the installed native integer domain")
            requested["token_budget"] = token_budget
        request = goal_transition(current, requested, user_authorized=user_authorized, acceptance=acceptance)
        require("objective" not in request["params"], "native lifecycle must never resend/replace the objective")
        result = {"schema": INTERFACE_VERSION, "action": action, "binding": binding, "request": request,
                  "owner": owner, "contract_digest": compiled["digest"], "evidence": evidence_binding if acceptance else None,
                  "authorization": "explicit host authorization required again at dispatch", "read_observations": calls}
        result["digest"] = digest(result)
        return result

    def dispatch(self, prepared: dict, host_transition: Callable[[dict], dict], *, user_authorized: bool,
                 authorization_id: str, host_identity: dict, diagnosis: str | None = None) -> dict:
        from .roadmap_native import process_handle
        from .roadmap_runtime import BudgetLedger
        from .roadmap_work import _immutable
        import os
        import time

        require(digest({k: v for k, v in prepared.items() if k != "digest"}) == prepared.get("digest"), "prepared native request was changed")
        require(user_authorized and bool(authorization_id) and host_identity.get("provider") == "codex" and
                host_identity.get("transport") and host_identity.get("identity"), "identified authorized host lifecycle callback required")
        token_budget = prepared["request"]["params"].get("tokenBudget")
        fresh = self.prepare(prepared["action"], user_authorized=user_authorized, token_budget=token_budget)
        require(fresh["request"] == prepared["request"] and fresh["owner"] == prepared["owner"] and
                fresh["contract_digest"] == prepared["contract_digest"] and fresh["evidence"] == prepared["evidence"],
                "native lifecycle inputs changed before host dispatch")
        ledger = BudgetLedger(self.root)
        current_record = ProjectAdapter(self.root).read()
        prior = current_record["execution"].get("native_transition")
        require(not prior or prior["state"] in {"SUCCESS", "FAILED"}, "unresolved native transition requires read-back recovery")
        semantic = {k: fresh[k] for k in ("action", "request", "owner", "contract_digest", "evidence")}
        semantic.update(protocol_digest=self.protocol["digest"], previous_goal_status=fresh["binding"]["observation"]["status"],
                        authorization_id=authorization_id, host_identity=host_identity)
        identity = digest(semantic)
        base = f".aegis/roadmaps/native-transitions/{identity}"
        prep_binding = _immutable(self.root, base + "/preparation-" + fresh["digest"] + ".json", fresh)
        operation = {"state": "PREPARED", "spec_digest": identity, "runner": process_handle(os.getpid()),
                     "owner": fresh["owner"], "child": None, "transport": "explicit_host_lifecycle_callback",
                     "native_thread": fresh["binding"]["thread_id"], "preparation": prep_binding,
                     "kind": "native_lifecycle_control", "authorization_id": authorization_id}
        attempt = ledger.reserve_control(digest({"native_goal": fresh["binding"]["thread_id"], "action": fresh["action"],
                                                "authorization_id": authorization_id}), identity, 60, operation,
                                         user_authorized=user_authorized, diagnosis=diagnosis)
        require(not attempt.get("reused"), "identical native transition is already successful; inspect native state instead of redispatching")
        adapter = ProjectAdapter(self.root)
        current_record = adapter.read()
        execution = dict(current_record["execution"])
        if prior:
            execution["native_transition_history"] = [*execution.get("native_transition_history", []), prior]
        execution["native_transition"] = {"state": "PREPARED", "attempt": attempt["id"], "preparation": prep_binding}
        adapter.update({"execution": execution}, expected_digest=digest(adapter.profile.path().read_bytes()))
        operation.update(state="RUNNING", dispatched_ns=time.time_ns())
        ledger.journal(attempt["id"], operation)
        response = None
        unknown = None
        try:
            response = host_transition(fresh["request"])
        except (TimeoutError, OSError) as exc:
            unknown = type(exc).__name__
        with NativeRpc(self.root, self.protocol) as rpc:
            after = rpc.call("thread/goal/get", {"threadId": fresh["binding"]["thread_id"]})["goal"]
            reads = list(rpc.calls)
        desired = {"complete": "complete", "pause": "paused", "resume": "active"}.get(prepared["action"])
        if desired:
            reconciliation = reconcile_native_transition(fresh["binding"]["observation"], response, after, desired)
        elif prepared["action"] == "clear":
            reconciliation = {"confirmed": after is None, "scope": "explicitly authorized clear; previous accounting remains in prepared binding"}
        else:
            before = fresh["binding"]["observation"]
            reconciliation = _budget_readback(before, response, after, token_budget, fresh["contract_digest"])
        result = {"schema": INTERFACE_VERSION, "request_digest": fresh["digest"], "response": response,
                "observation_error": unknown, "after": after, "reconciliation": reconciliation, "read_observations": reads}
        result_binding = _immutable(self.root, base + "/result-" + digest(result) + ".json", result)
        terminal = "SUCCESS" if reconciliation["confirmed"] else "FAILED" if response and response.get("error") else "UNKNOWN"
        if terminal != "UNKNOWN":
            ledger.close(attempt["id"], terminal, {"artifacts": [prep_binding, result_binding], "native_reconciliation": reconciliation,
                                                  "unknown_usage": True})
        current_record = adapter.read(); execution = dict(current_record["execution"])
        execution["native_transition"] = {"state": terminal, "attempt": attempt["id"], "preparation": prep_binding, "result": result_binding}
        adapter.update({"execution": execution}, expected_digest=digest(adapter.profile.path().read_bytes()))
        return dict(result, attempt=attempt["id"], state=terminal, result_binding=result_binding)

    def recover(self) -> dict:
        """Reobserve the same native Goal; an unchanged/unknown state never retries."""
        from .roadmap_runtime import BudgetLedger
        from .roadmap_work import _immutable

        adapter = ProjectAdapter(self.root)
        record = adapter.read()
        transition = record["execution"].get("native_transition")
        require(transition and transition["state"] not in {"SUCCESS", "FAILED"}, "no unresolved native transition")
        require(bindings_current(self.root, [transition["preparation"]]), "native preparation evidence changed")
        prepared = read_json(confined_path(self.root, transition["preparation"]["path"]))
        with NativeRpc(self.root, self.protocol) as rpc:
            after = rpc.call("thread/goal/get", {"threadId": prepared["binding"]["thread_id"]})["goal"]
        desired = {"complete": "complete", "pause": "paused", "resume": "active"}.get(prepared["action"])
        before = prepared["binding"]["observation"]
        if desired:
            result = reconcile_native_transition(before, None, after, desired)
        elif prepared["action"] == "clear":
            result = {"confirmed": after is None}
        else:
            result = _budget_readback(before, None, after, prepared["request"]["params"]["tokenBudget"], prepared["contract_digest"])
        observation = {"schema": INTERFACE_VERSION, "after": after, "reconciliation": result,
                       "scope": "read-back of the same uncertain native transition; no redispatch"}
        binding = _immutable(self.root, str(Path(transition["preparation"]["path"]).parent / ("recovery-" + digest(observation) + ".json")), observation)
        if result["confirmed"]:
            BudgetLedger(self.root).close(transition["attempt"], "SUCCESS", {"artifacts": [transition["preparation"], binding],
                                         "native_reconciliation": result, "unknown_usage": True})
            execution = dict(record["execution"])
            execution["native_transition"] = dict(transition, state="SUCCESS", recovery=binding)
            adapter.update({"execution": execution}, expected_digest=digest(adapter.profile.path().read_bytes()))
        return dict(observation, state="SUCCESS" if result["confirmed"] else "UNKNOWN", artifact=binding)


def _budget_readback(before: dict, response: dict | None, after: dict | None, budget: int, contract_digest: str) -> dict:
    try:
        require(isinstance(after, dict), "native Goal missing after budget request")
        bind_goal(after, thread_id=before["threadId"], objective=before["objective"], contract_hash=contract_digest)
        result = reconcile_native_transition(before, response, after, after["status"])
        result["confirmed"] = result["confirmed"] and after.get("tokenBudget") == budget
        return result
    except ContractError as error:
        return {"confirmed": False, "reasons": [str(error)]}


class NativeEventState:
    """Finite public-notification projection; deltas never become final Plans."""
    def __init__(self, thread_id: str, selected_model: str):
        require(bool(thread_id) and bool(selected_model), "native event owner/model required")
        self.thread_id = thread_id
        self.selected_model = selected_model
        self.turn_id = None
        self.status = "UNKNOWN"
        self.plans = {}
        self.usage = None
        self.blockers = []
        self.observed = []

    def consume(self, notification: dict) -> None:
        method, params = notification["method"], notification["params"]
        require(params.get("threadId") == self.thread_id, "native notification belongs to another chat")
        origin = {"method": method, "sha256": digest(notification)}
        if origin in self.observed:
            return
        require(len(self.observed) < 10000, "native notification packet exceeds its observation bound")
        if method == "turn/started":
            require(self.status != "inProgress" or params["turn"]["id"] == self.turn_id, "overlapping native model turns prohibited")
            self.turn_id = params["turn"]["id"]
            self.status = "inProgress"
            self.plans = {}
        elif method == "model/rerouted":
            require(params.get("turnId") == self.turn_id, "model routing belongs to another or unknown turn")
            if params.get("toModel") != self.selected_model or params.get("fromModel") != self.selected_model:
                self.blockers.append("MODEL_REROUTED_OR_UNEXPECTED_SOURCE")
        elif method == "thread/tokenUsage/updated":
            total = params["tokenUsage"]["total"]
            require(total and all(type(v) is int and v >= 0 for v in total.values()), "invalid cumulative native usage")
            if self.usage is not None:
                require(set(total) == set(self.usage) and all(total[k] >= self.usage[k] for k in total), "native token series decreased or changed shape")
            self.usage = dict(total)
        else:
            require(params.get("turnId", params.get("turn", {}).get("id")) == self.turn_id,
                    "native notification belongs to another or unknown turn")
            if method == "turn/completed":
                require(params["turn"]["status"] in {"completed", "interrupted", "failed"}, "native turn is not terminal")
                self.status = params["turn"]["status"]
            elif method == "item/completed" and params["item"].get("type") == "plan":
                item = params["item"]
                require(bool(item.get("id")) and type(item.get("text")) is str and bool(item["text"]), "empty completed native Plan")
                final = {k: item[k] for k in ("type", "id", "text")}
                require(item["id"] not in self.plans or self.plans[item["id"]] == final, "conflicting final native Plan item")
                self.plans[item["id"]] = final
            elif method == "turn/plan/updated":
                require(type(params.get("plan")) is list and all(type(p.get("step")) is str and p["step"] and
                        p.get("status") in {"pending", "inProgress", "completed"} for p in params["plan"]),
                        "invalid native plan-step update")
            elif method not in {"item/started", "item/completed", "item/plan/delta", "turn/plan/updated"}:
                self.blockers.append("UNQUALIFIED_NATIVE_NOTIFICATION")
        self.observed.append(origin)
