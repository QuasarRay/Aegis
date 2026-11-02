"""Observed Goal/Plan adapters and authorized managed Goal lifecycle transport.

Goal writes share one policy, journal and ledger across host and managed paths.
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


class _ManagedGoalClient(CodexReader):
    """One prepared Goal request; no thread loading or model-turn methods."""
    ALLOWED = CodexReader.ALLOWED | {"thread/goal/set", "thread/goal/clear"}

    def __init__(self, root: Path, protocol: dict, request: dict, on_started: Callable[[dict], None]):
        super().__init__(executable=protocol["executable"]["path"], experimental=True)
        self.root = root
        self.protocol = protocol
        self.request = request
        self.on_started = on_started
        self.sent = False
        self.observations = []

    def _started(self) -> None:
        from .roadmap_native import process_handle
        self.on_started(process_handle(self.proc.pid))
        executable = Path(f"/proc/{self.proc.pid}/exe")
        require(executable.exists() and executable.resolve() == Path(self.executable).resolve() and
                digest(executable.read_bytes()) == self.protocol["executable"]["sha256"],
                "managed server process is not the pinned installed executable")

    def call(self, method: str, params: dict) -> dict:
        if method not in {"thread/goal/set", "thread/goal/clear"}:
            return super().call(method, params)
        require(not self.sent and {"method": method, "params": params} == self.request,
                "managed Goal transport permits its single prepared lifecycle request only")
        assert_protocol(self.root, self.protocol)
        prefix = "ThreadGoalSet" if method == "thread/goal/set" else "ThreadGoalClear"
        request_contract = self.protocol["selected"][prefix + "Params"]
        response_contract = self.protocol["selected"][prefix + "Response"]
        schema = read_json(confined_path(self.root, request_contract["path"]))
        require(set(params) <= set(schema.get("properties", {})) and
                set(schema.get("required", [])) <= set(params) and "objective" not in params,
                "managed lifecycle request differs from installed native contract")
        require(type(params.get("threadId")) is str and 0 < len(params["threadId"]) <= 128 and
                params.get("origin") in {"user", "automatic"}, "native Goal identity/provenance required")
        allowed = {"threadId", "origin", "status", "tokenBudget"} if method == "thread/goal/set" else {"threadId", "origin"}
        require(set(params) <= allowed, "managed lifecycle request contains an unqualified field")
        if "tokenBudget" in params:
            require(type(params["tokenBudget"]) is int and 0 < params["tokenBudget"] <= 2 ** 63 - 1,
                    "native token budget must preserve its positive int64 domain")
        observed = {"method": method, "request_digest": digest(params), "request_contract": request_contract,
                    "response_contract": response_contract, "observed_at": datetime.now(timezone.utc).isoformat()}
        self.sent = True  # An uncertain write must never be repeated on this connection.
        try:
            reply = super().call(method, params)
        except CodexRpcError as error:
            self.observations.append(dict(observed, status="REJECTED", error_code=error.code, message=error.message))
            raise
        except (TimeoutError, OSError, ContractError, ValueError):
            self.observations.append(dict(observed, status="UNKNOWN"))
            raise
        response_schema = read_json(confined_path(self.root, response_contract["path"]))
        if not isinstance(reply, dict) or not set(response_schema.get("required", [])) <= set(reply):
            self.observations.append(dict(observed, status="INVALID_NATIVE_REPLY", response_digest=digest(reply)))
            raise ContractError("managed native reply omits required contract fields")
        self.observations.append(dict(observed, status="OBSERVED", response_digest=digest(reply)))
        return reply


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
                          "goal_writes": "shared authorized host callback or managed stdio sender; no live Goal mutation exercised",
                          "managed_adapter": {"read_rpc": "EXERCISED", "goal_mutation_transport": "IMPLEMENTED_NOT_LIVE_QUALIFIED",
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
        return self._dispatch(prepared, host_transition, user_authorized=user_authorized,
                              authorization_id=authorization_id, host_identity=host_identity, diagnosis=diagnosis)

    def dispatch_managed(self, prepared: dict, *, user_authorized: bool,
                         authorization_id: str, diagnosis: str | None = None) -> dict:
        """Send the same audited request over the pinned installed stdio server.

        This is an explicit lifecycle operation, not a Goal-continuation loop.
        It cannot create a chat, load a thread, dispatch inference or change the
        objective. Live qualification still requires an authorized user action.
        """
        identity = {"provider": "codex", "transport": "managed_app_server_stdio_goal",
                    "identity": {"executable": self.protocol["executable"], "protocol_digest": self.protocol["digest"]}}
        return self._dispatch(prepared, None, user_authorized=user_authorized,
                              authorization_id=authorization_id, host_identity=identity, diagnosis=diagnosis, managed=True)

    def _dispatch(self, prepared: dict, host_transition: Callable[[dict], dict] | None, *, user_authorized: bool,
                  authorization_id: str, host_identity: dict, diagnosis: str | None, managed: bool = False) -> dict:
        from .roadmap_native import process_handle
        from .roadmap_runtime import BudgetLedger
        from .roadmap_work import _immutable
        import os
        import time

        require(digest({k: v for k, v in prepared.items() if k != "digest"}) == prepared.get("digest"), "prepared native request was changed")
        require(user_authorized and bool(authorization_id) and host_identity.get("provider") == "codex" and
                host_identity.get("transport") and host_identity.get("identity"), "identified authorized host lifecycle callback required")
        require(managed or callable(host_transition), "native host lifecycle callback required")
        if managed:
            assert_protocol(self.root, self.protocol)
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
                     "owner": fresh["owner"], "child": None, "transport": host_identity["transport"] if managed else "explicit_host_lifecycle_callback",
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
        transport = None
        dispatched = None

        def child_started(handle: dict) -> None:
            operation["child"] = handle
            ledger.journal(attempt["id"], operation)

        try:
            WorkspaceLease(self.root).assert_owner(fresh["owner"])
            if managed:
                transport = _ManagedGoalClient(self.root, self.protocol, fresh["request"], child_started)
                with transport as client:
                    # Reobserve on this connection immediately before the write.
                    # The native API has no compare-and-swap parameter; other
                    # noncooperating clients remain an explicit trust boundary.
                    current = client.call("thread/goal/get", {"threadId": fresh["binding"]["thread_id"]})["goal"]
                    valid = reconcile_native_transition(fresh["binding"]["observation"], None, current,
                                                        fresh["binding"]["observation"]["status"])
                    require(valid["confirmed"], "native Goal changed before managed lifecycle dispatch")
                    WorkspaceLease(self.root).assert_owner(fresh["owner"])
                    response = client.call(fresh["request"]["method"], fresh["request"]["params"])
            else:
                response = host_transition(fresh["request"])
        except CodexRpcError as exc:
            response = {"error": {"code": exc.code, "message": exc.message}, "method": exc.method}
        except Exception as exc:
            # A malformed reply, callback error or disconnect can follow an
            # applied mutation. Retain the reservation and reconcile readback.
            unknown = type(exc).__name__
        if transport is not None:
            dispatched = transport.sent
        if managed:
            operation["native_request_sent"] = dispatched if transport is not None else False
            ledger.journal(attempt["id"], operation)
        reply = {"schema": INTERFACE_VERSION, "request_digest": fresh["digest"], "response": response,
                 "observation_error": unknown, "managed_request_sent": dispatched,
                 "transport_observations": transport.observations if transport is not None else [],
                 "initialization_digest": digest(transport.initialization) if transport is not None and transport.initialization is not None else None}
        # Preserve an actual rejection/success reply before attempting readback.
        # An interrupted read must not turn a known reply into a missing one.
        reply_binding = _immutable(self.root, base + "/reply-" + digest(reply) + ".json", reply)
        operation["reply"] = reply_binding
        ledger.journal(attempt["id"], operation)
        current_record = adapter.read(); execution = dict(current_record["execution"])
        execution["native_transition"] = {"state": "AWAITING_READBACK", "attempt": attempt["id"],
                                          "preparation": prep_binding, "reply": reply_binding}
        adapter.update({"execution": execution}, expected_digest=digest(adapter.profile.path().read_bytes()))
        after, reads, read_error = self._readback(fresh)
        reconciliation = _reconcile_goal(fresh, response, after) if read_error is None else {
            "confirmed": False, "reasons": ["native readback is unknown"], "readback_error": read_error}
        result = {"schema": INTERFACE_VERSION, "request_digest": fresh["digest"], "response": response,
                  "observation_error": unknown, "after": after, "reconciliation": reconciliation,
                  "read_observations": reads, "reply": reply_binding}
        terminal = _transition_outcome(self.root, operation, reconciliation, response)
        result["state"] = terminal
        result_binding = _immutable(self.root, base + "/result-" + digest(result) + ".json", result)
        if terminal != "UNKNOWN":
            ledger.close(attempt["id"], terminal, {"artifacts": [prep_binding, reply_binding, result_binding], "native_reconciliation": reconciliation,
                                                  "unknown_usage": True})
        current_record = adapter.read(); execution = dict(current_record["execution"])
        execution["native_transition"] = {"state": terminal, "attempt": attempt["id"], "preparation": prep_binding,
                                          "reply": reply_binding, "result": result_binding}
        adapter.update({"execution": execution}, expected_digest=digest(adapter.profile.path().read_bytes()))
        return dict(result, attempt=attempt["id"], state=terminal, result_binding=result_binding)

    def _readback(self, prepared: dict) -> tuple[dict | None, list[dict], str | None]:
        rpc = None
        try:
            with NativeRpc(self.root, self.protocol) as rpc:
                after = rpc.call("thread/goal/get", {"threadId": prepared["binding"]["thread_id"]})["goal"]
                return after, list(rpc.calls), None
        except Exception as error:
            return None, list(rpc.calls) if rpc is not None else [], type(error).__name__

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
        matches = [a for a in BudgetLedger(self.root).read()["attempts"] if a["id"] == transition["attempt"]]
        require(len(matches) == 1, "native transition lost its durable reservation")
        attempt = matches[0]
        operation = attempt["operation"]
        require(operation["preparation"] == transition["preparation"] and
                operation["native_thread"] == prepared["binding"]["thread_id"], "native reservation lineage changed")
        response = None
        artifacts = [transition["preparation"]]
        reply_binding = transition.get("reply") or operation.get("reply")
        if reply_binding:
            require(not transition.get("reply") or not operation.get("reply") or transition["reply"] == operation["reply"],
                    "native reply journal disagrees with canonical transition")
            require(bindings_current(self.root, [reply_binding]), "native reply evidence changed")
            reply = read_json(confined_path(self.root, reply_binding["path"]))
            require(reply["request_digest"] == prepared["digest"], "native reply belongs to another preparation")
            response = reply["response"]
            artifacts.append(reply_binding)
        after, reads, read_error = self._readback(prepared)
        result = _reconcile_goal(prepared, response, after) if read_error is None else {
            "confirmed": False, "reasons": ["native readback is unknown"], "readback_error": read_error}
        state = _transition_outcome(self.root, operation, result, response)
        ledger_terminal = attempt["status"] in {"SUCCESS", "FAILED"}
        if ledger_terminal:
            require(bindings_current(self.root, attempt["receipt"].get("artifacts", [])) and
                    bool(attempt["receipt"].get("artifacts")), "terminal native receipt evidence changed")
            # A crash may happen after closing the ledger and before updating
            # the canonical projection. Preserve that observed operation result;
            # the fresh native state is still reported separately below.
            state = attempt["status"]
        observation = {"schema": INTERFACE_VERSION, "after": after, "reconciliation": result,
                       "response": response, "state": state, "read_observations": reads,
                       "ledger_already_terminal": ledger_terminal,
                       "scope": "read-back of the same uncertain native transition; no redispatch"}
        binding = _immutable(self.root, str(Path(transition["preparation"]["path"]).parent / ("recovery-" + digest(observation) + ".json")), observation)
        if state != "UNKNOWN":
            if not ledger_terminal:
                BudgetLedger(self.root).close(transition["attempt"], state, {"artifacts": [*artifacts, binding],
                                             "native_reconciliation": result, "unknown_usage": True})
            execution = dict(record["execution"])
            execution["native_transition"] = dict(transition, state=state, recovery=binding)
            if reply_binding:
                execution["native_transition"]["reply"] = reply_binding
            adapter.update({"execution": execution}, expected_digest=digest(adapter.profile.path().read_bytes()))
        return dict(observation, artifact=binding)


def _transition_outcome(root: Path, operation: dict, reconciliation: dict, response: dict | None) -> str:
    if operation.get("transport") == "managed_app_server_stdio_goal":
        if operation.get("child"):
            from .roadmap_native import inspect_process
            process_state = inspect_process(operation["child"])
            reconciliation["transport_process_state"] = process_state
            if process_state not in {"GONE", "REUSED_PID", "PREVIOUS_BOOT"}:
                return "UNKNOWN"
        if operation.get("native_request_sent") is False:
            reconciliation["request_not_dispatched"] = True
            reconciliation["confirmed"] = False
            return "FAILED"
    if isinstance(response, dict) and response.get("error"):
        return "FAILED"
    return "SUCCESS" if reconciliation["confirmed"] else "UNKNOWN"


def _reconcile_goal(prepared: dict, response: dict | None, after: dict | None) -> dict:
    desired = {"complete": "complete", "pause": "paused", "resume": "active"}.get(prepared["action"])
    before = prepared["binding"]["observation"]
    if desired:
        return reconcile_native_transition(before, response, after, desired)
    if prepared["action"] == "clear":
        return {"confirmed": after is None and not (isinstance(response, dict) and response.get("error")),
                "scope": "explicitly authorized clear; previous accounting remains in prepared binding"}
    return _budget_readback(before, response, after, prepared["request"]["params"]["tokenBudget"], prepared["contract_digest"])


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
