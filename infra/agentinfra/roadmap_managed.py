"""Sequential native turns on an explicitly adopted existing Codex chat.

This controller never creates chats, changes Goals or runs a Goal-continuation
loop. A caller explicitly adopts, prepares, starts and observes one turn. Native
termination, process identity, source identity and effective settings are separate
observations. A lost connection never grants another model dispatch.
"""
from __future__ import annotations

from datetime import datetime, timezone
import os
import re
from pathlib import Path
import time
import uuid

from .locks import FileLock
from .roadmap import audit_evidence, compile_roadmaps
from .roadmap_codex import CodexReader, CodexRpcError
from .roadmap_lease import WorkspaceLease
from .roadmap_native import inspect_process, is_process_ancestor, process_handle, read_session_metadata
from .roadmap_native_adapter import NativeEventState, NativeRpc, READ_CONTRACTS, observe_goal, _bind_observed_goal
from .roadmap_policy import authorize
from .roadmap_portability import maintained_python
from .roadmap_project import AEGIS_RECORD_WRITER, ProjectAdapter
from .roadmap_protocol import assert_protocol
from .roadmap_records import ContractError, bindings_current, canonical, digest, file_binding, read_json, require, validate_record
from .roadmap_runtime import BudgetLedger
from .roadmap_work import _immutable
from .security import confined_path
from .transaction import FileTransaction, Mutation


INTERFACE_VERSION = 1
CONTRACTS = {"thread/resume": "ThreadResume", "turn/start": "TurnStart",
             "turn/steer": "TurnSteer", "turn/interrupt": "TurnInterrupt"}
PUBLIC_EVENTS = {"turn/started", "turn/completed", "item/started", "item/completed", "item/plan/delta",
                 "turn/plan/updated", "model/rerouted", "thread/tokenUsage/updated"}
TERMINAL = {"completed", "failed", "interrupted"}
RETIRED = {"GONE", "REUSED_PID", "PREVIOUS_BOOT"}


def _state_home() -> str:
    return str(Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex").resolve())


def _protocol(root: Path, protocol: dict) -> None:
    assert_protocol(root, protocol)
    require(all(prefix + suffix in protocol["selected"] for prefix in CONTRACTS.values()
                for suffix in ("Params", "Response")), "managed turn contracts are not pinned")


def _native(root: Path, protocol: dict, execution: dict) -> tuple[dict, dict, dict]:
    with NativeRpc(root, protocol) as rpc:
        binding = observe_goal(root, rpc, compile_roadmaps(root), execution["native_binding"])
        thread = rpc.call("thread/read", {"threadId": binding["thread_id"], "includeTurns": False})["thread"]
    require(thread["id"] == binding["thread_id"] and Path(thread["cwd"]).resolve() == root,
            "managed native chat belongs to another workspace")
    metadata = read_session_metadata(Path(thread["path"]), binding["thread_id"])
    require(metadata["context"]["turn_id"] == metadata["lifecycle"]["turn_id"], "native lifecycle/configuration disagree")
    return binding, thread, metadata


def adopt_managed_runner(adapter: ProjectAdapter, protocol: dict, *, user_authorized: bool, authorization_id: str) -> dict:
    """One transaction transfers a retired, natively idle parent to this driver.

    Requiring the former host process to be retired also prevents its automatic
    Goal continuation from overlapping this controller after an explicit resume.
    Existing pauses and limits stay in native state; adoption does not resume.
    """
    require(user_authorized and authorization_id and adapter.profile.project == "Aegis", "explicit managed adoption authorization required")
    root = adapter.root; _protocol(root, protocol); state_home = _state_home()
    lease = WorkspaceLease(root); lock = FileLock(lease.lock_path, "managed native ownership adoption"); lock.acquire()
    try:
        before = adapter.profile.path().read_bytes(); record = adapter.read(); execution = record["execution"]
        old = execution["workspace_lease"]; lease_before = lease.path.read_bytes(); state = lease.read()
        require(state["active"] == old, "canonical and workspace native owner disagree")
        require(inspect_process(old) in RETIRED, "active or unknown parent process prohibits managed handoff")
        require(not any(a["status"] == "RESERVED" for a in BudgetLedger(root).read()["attempts"]),
                "reconcile every existing operation handle before managed handoff")
        previous_server = execution.get("managed_runner", {}).get("server")
        require(not previous_server or inspect_process(previous_server) in RETIRED,
                "previous managed server remains live or unknown")
        binding, thread, metadata = _native(root, protocol, execution)
        require(metadata["lifecycle"]["kind"] in {"task_complete", "turn_aborted"} and
                binding["observation"]["status"] in {"paused", "blocked", "budget_limited", "usage_limited", "budgetLimited", "usageLimited"},
                "native parent is active, auto-continuing or not explicitly resumable")
        context = metadata["context"]; selected = execution["native_turn_configuration"]["model"]
        require(context["mode"] == "default" and context["effort"] == "max" and context["model"] == selected and
                thread.get("model") == selected and thread.get("reasoningEffort") == "max", "parent native mode/model/max effort is unqualified")
        require(inspect_process(old) in RETIRED, "parent process changed during managed handoff")
        require(_state_home() == state_home, "native state routing changed during adoption")
        handle = process_handle(os.getpid()); state["generation"] += 1
        owner = dict(old, **handle, fence=state["generation"], nonce=uuid.uuid4().hex)
        observation = {"schema": 1, "authorization_id": authorization_id, "parent": old,
                       "parent_native_context": context, "parent_native_lifecycle": metadata["lifecycle"],
                       "native_binding": binding, "protocol_digest": protocol["digest"], "replacement": owner}
        state["history"].append({"owner": old, "replacement": owner, "recovery": True, "observation": observation})
        state["active"] = owner
        execution["binding_history"] = [*execution.get("binding_history", []), execution["native_binding"]]
        execution.update(workspace_lease=owner, native_binding=binding, integration_path="managed_app_server",
                         managed_runner={"runner": handle, "server": None, "authorization_id": authorization_id,
                                         "adoption": observation, "protocol_digest": protocol["digest"]})
        execution["managed_runner"]["state_home"] = state_home
        record["canonical_writer_transaction_name"] = AEGIS_RECORD_WRITER
        FileTransaction(root, [Mutation(lease.path, canonical(state) + b"\n", expected_exists=True, expected_sha256=digest(lease_before)),
                               Mutation(adapter.profile.path(), canonical(record) + b"\n", expected_exists=True, expected_sha256=digest(before))],
                        state_dir=root / ".aegis/state/transactions", name=AEGIS_RECORD_WRITER).commit()
        return {"owner": owner, "observation": observation}
    finally:
        lock.release()


def observe_managed_owner(root: Path, owner: dict) -> dict:
    root = root.resolve(); record = ProjectAdapter(root).read(); execution = record["execution"]
    managed = execution.get("managed_runner", {})
    require(managed.get("state_home") == _state_home(), "managed native state routing changed")
    require(execution.get("integration_path") == "managed_app_server" and execution["workspace_lease"] == owner and
            managed.get("runner") == {k: owner[k] for k in ("pid", "process_identity", "host", "boot_identity")},
            "managed runner ownership is not established")
    WorkspaceLease(root).assert_owner(owner)
    require(inspect_process(managed["adoption"]["parent"]) in RETIRED, "original native parent is not retired")
    protocol_binding = record["native_protocol"]
    require(bindings_current(root, [protocol_binding]), "managed native protocol binding changed")
    protocol = read_json(confined_path(root, protocol_binding["path"])); _protocol(root, protocol)
    require(protocol["digest"] == managed["protocol_digest"], "managed protocol changed after adoption")
    binding, thread, metadata = _native(root, protocol, execution)
    server = managed.get("server")
    if server:
        server_state = inspect_process(server)
        require(server_state == "LIVE" or server_state in RETIRED and metadata["lifecycle"]["kind"] != "task_started",
                "managed native server or its outstanding turn is unobserved")
        if server_state == "LIVE": _loaded_executable(server, protocol)
    context = metadata["context"]
    require(not metadata.get("routing"), "native journal reports a model reroute")
    require(thread.get("model") == context["model"] and thread.get("reasoningEffort") == context["effort"],
            "managed service and native configuration disagree")
    result = {"schema": 1, "kind": "codex_managed_host_observation", "producer": "agentinfra.roadmap_managed.observe_managed_owner",
              "session": owner["session"], "status": "active" if metadata["lifecycle"]["kind"] == "task_started" else "idle",
              "goal": binding["observation"], "model": context["model"], "effort": context["effort"], "mode": context["mode"],
              "turn_id": context["turn_id"], "owner_process": process_handle(owner["pid"]),
              "caller_is_descendant": is_process_ancestor(owner["pid"]), "executable": protocol["executable"],
              "metadata": metadata, "observer_server_status": thread.get("status"),
              "limits": ["One explicitly adopted existing chat; no implicit chat creation or Goal activation",
                         "Service/journal and cooperating process provenance are explicit trust boundaries"]}
    result["digest"] = digest(result); return result


def _loaded_executable(handle: dict, protocol: dict) -> None:
    executable = Path(f"/proc/{handle['pid']}/exe")
    require(executable.exists() and executable.resolve() == Path(protocol["executable"]["path"]).resolve() and
            digest(executable.read_bytes()) == protocol["executable"]["sha256"], "managed process is not the pinned native executable")


def _source_inputs(root: Path, compiled: dict) -> list[dict]:
    inputs = {b["path"]: b for b in compiled["inputs"]}
    for path in maintained_python(root): inputs[path.relative_to(root).as_posix()] = file_binding(root, path.relative_to(root).as_posix())
    inputs["framework.toml"] = file_binding(root, "framework.toml")
    return sorted(inputs.values(), key=lambda b: b["path"])


class _TurnClient(CodexReader):
    ALLOWED = CodexReader.ALLOWED | set(CONTRACTS)

    def __init__(self, root: Path, protocol: dict, started):
        super().__init__(executable=protocol["executable"]["path"], experimental=True)
        self.root = root; self.protocol = protocol; self.started = started; self.calls = []

    def _started(self) -> None:
        handle = process_handle(self.proc.pid); self.started(handle); _loaded_executable(handle, self.protocol)

    def call(self, method: str, params: dict) -> dict:
        prefix = CONTRACTS.get(method) or READ_CONTRACTS.get(method)
        if prefix is None:
            return super().call(method, params)
        _protocol(self.root, self.protocol)
        request = self.protocol["selected"][prefix + "Params"]; response = self.protocol["selected"][prefix + "Response"]
        schema = read_json(confined_path(self.root, request["path"]))
        require(set(params) <= set(schema.get("properties", {})) and set(schema.get("required", [])) <= set(params),
                "managed request differs from installed native contract")
        provenance = {"method": method, "request_digest": digest(params), "request_contract": request,
                      "response_contract": response, "observed_at": datetime.now(timezone.utc).isoformat()}
        try:
            reply = super().call(method, params)
        except CodexRpcError as error:
            self.calls.append(dict(provenance, status="REJECTED", error_code=error.code, message=error.message)); raise
        except Exception:
            self.calls.append(dict(provenance, status="UNKNOWN")); raise
        schema = read_json(confined_path(self.root, response["path"]))
        require(isinstance(reply, dict) and set(schema.get("required", [])) <= set(reply), "managed reply omits native contract fields")
        self.calls.append(dict(provenance, status="OBSERVED", response_digest=digest(reply))); return reply


class ManagedTurnRunner:
    """Explicit single-turn controller; executor/specialist/reviewer share policy."""
    def __init__(self, root: Path, protocol: dict):
        self.root = root.resolve(); self.protocol = protocol; self.client = None; self.events = None
        self.attempt = None; self.operation = None; self.spec = None; self.started_monotonic = None
        self.call_cursor = 0

    def _record(self) -> tuple[ProjectAdapter, dict, dict]:
        adapter = ProjectAdapter(self.root); record = adapter.read(); execution = record["execution"]
        require(execution.get("integration_path") == "managed_app_server", "explicit managed ownership adoption is required")
        WorkspaceLease(self.root).assert_owner(execution["workspace_lease"])
        require(is_process_ancestor(execution["workspace_lease"]["pid"]), "caller is outside managed runner ownership")
        require(execution["managed_runner"]["protocol_digest"] == self.protocol["digest"], "managed protocol changed")
        require(execution["managed_runner"].get("state_home") == _state_home(), "managed native state routing changed")
        _protocol(self.root, self.protocol)
        return adapter, record, execution

    def prepare(self, text: str, *, role: str, authorization_id: str, seconds: int = 900) -> dict:
        _, record, execution = self._record(); compiled = compile_roadmaps(self.root)
        require(role in {"executor", "specialist", "reviewer"} and type(text) is str and text.strip() and
                len(text.encode()) <= 128000 and type(authorization_id) is str and 0 < len(authorization_id) <= 128,
                "bounded explicitly attributed native input/role required")
        milestone = record["continuation"]["milestone"]; contract = compiled["milestones"][milestone]
        require(milestone in execution["scope"] and type(seconds) is int and
                0 < seconds <= contract["budget_policy"]["max_seconds_per_recipe"], "turn exceeds adopted work scope or finite budget")
        require(execution.get("monetary_cap") is None, "managed native billing cap is not enforceable")
        evidence = record.get("roadmap_evidence")
        audit = audit_evidence(self.root, compiled, read_json(confined_path(self.root, evidence["path"])) if evidence and bindings_current(self.root, [evidence]) else None)
        require(all(audit["milestones"][m]["state"] == "SATISFIED" for m in contract["dependencies"]),
                "managed work dependencies lack current acceptance")
        spec = {"schema": 1, "kind": "managed_native_turn", "milestone": milestone, "role": role,
                "authorization_id": authorization_id, "owner": execution["workspace_lease"], "contract_digest": compiled["digest"],
                "inputs": _source_inputs(self.root, compiled), "protocol_digest": self.protocol["digest"],
                "state_home": execution["managed_runner"]["state_home"], "permission_policy": "inherit_native_chat",
                "selected_model": execution["native_turn_configuration"]["model"], "requested_effort": "max", "mode": "default",
                "thread_id": execution["native_binding"]["thread_id"], "objective": execution["native_binding"]["objective"],
                "goal_created_at": execution["native_binding"]["observation"]["createdAt"],
                "allowed_milestones": execution["scope"],
                "input": [{"type": "text", "text": text}], "max_seconds": seconds,
                "max_attempts": contract["budget_policy"]["max_attempts"], "source_responsibility": contract["implementation_units"]}
        spec["work_id"] = digest({k: spec[k] for k in ("thread_id", "milestone", "role", "authorization_id")})
        spec["digest"] = digest(spec); return spec

    def _persist(self, state: str, **extra) -> dict:
        adapter, record, execution = self._record()
        current = execution.get("managed_turn")
        if current and current["attempt"] != self.attempt["id"]:
            require(current["state"] in {"SUCCESS", "FAILED", "INTERRUPTED"}, "another native turn remains unresolved")
            execution["managed_turn_history"] = [*execution.get("managed_turn_history", []), current]
        execution["managed_turn"] = {"state": state, "attempt": self.attempt["id"], "spec": self.operation["spec"],
                                     "turn_id": self.operation.get("turn_id"), **extra}
        if self.operation.get("child"): execution["managed_runner"]["server"] = self.operation["child"]
        units = dict(record.get("work_units", {})); unit = {"schema": 1, "work_id": self.spec["work_id"],
            "contract_digest": self.spec["contract_digest"], "source_responsibility": self.spec["source_responsibility"],
            "inputs": self.spec["inputs"], "writer": AEGIS_RECORD_WRITER, "allowed_actions": ["managed.native.turn"],
            "continuation": {"state": state, "attempt": self.attempt["id"], "native_turn": self.operation.get("turn_id")}}
        validate_record(self.root, "WorkUnit", unit); units[unit["work_id"]] = unit
        adapter.update({"execution": execution, "work_units": units}, expected_digest=digest(adapter.profile.path().read_bytes()))
        return execution["managed_turn"]

    def start(self, spec: dict, *, user_authorized: bool, diagnosis: str | None = None) -> dict:
        require(user_authorized and spec.get("digest") == digest({k: v for k, v in spec.items() if k != "digest"}), "authorized unchanged native specification required")
        _, record, execution = self._record()
        require(spec == self.prepare(spec["input"][0]["text"], role=spec["role"], authorization_id=spec["authorization_id"], seconds=spec["max_seconds"]),
                "native source/contract/configuration changed before dispatch")
        prior = execution.get("managed_turn")
        require(not prior or prior["state"] in {"SUCCESS", "FAILED", "INTERRUPTED"}, "existing native turn requires observation/recovery")
        observation = WorkspaceLease(self.root).qualify(spec["owner"])
        expected = digest({"inputs": spec["inputs"], "contract": spec["contract_digest"]})
        decision = authorize("implement", {"provider": "codex", "mode": "execute" if observation["mode"] == "default" else "plan",
            "authorized": user_authorized, "goal_status": observation["goal"]["status"], "requested_effort": "max",
            "accepted_effort": observation["effort"], "effective_effort": observation["effort"],
            "selected_model": spec["selected_model"], "observed_model": observation["model"], "active_agents": 1,
            "lease_valid": True, "expected_inputs": expected, "current_inputs": expected})
        require(decision["allowed"] and observation["status"] == "idle", "active parent or unqualified managed execution policy")
        require(observation["goal"]["createdAt"] == spec["goal_created_at"] and observation["goal"]["objective"] == spec["objective"], "native Goal lineage changed")
        old_server = execution["managed_runner"].get("server")
        require(self.client is not None or not old_server or inspect_process(old_server) in RETIRED,
                "original native stream is live or unknown; starting a replacement is refused")
        self.spec = spec; self.events = NativeEventState(spec["thread_id"], spec["selected_model"])
        self.call_cursor = len(self.client.calls) if self.client is not None else 0
        base = f".aegis/roadmaps/native-turns/{spec['digest']}"
        binding = _immutable(self.root, base + "/spec.json", spec)
        self.operation = {"state": "PREPARED", "kind": "native_model_turn", "spec_digest": spec["digest"], "spec": binding,
            "runner": process_handle(os.getpid()), "owner": spec["owner"], "child": None, "native_thread": spec["thread_id"],
            "turn_id": None, "controls": [], "source_parent_turn": observation["turn_id"], "start_sent": False}
        ledger = BudgetLedger(self.root)
        prior_attempts = [a for a in ledger.read()["attempts"] if a["work_id"] == spec["work_id"]]
        if prior_attempts and prior_attempts[-1]["status"] == "SUCCESS" and prior_attempts[-1]["inputs"] != spec["digest"]:
            self.operation["supersedes_success"] = prior_attempts[-1]["id"]
        self.attempt = ledger.reserve_operation(spec["work_id"], spec["digest"], spec["max_seconds"], self.operation,
            max_attempts=spec["max_attempts"], total_seconds=spec["max_seconds"] * spec["max_attempts"], diagnosis=diagnosis)
        require(not self.attempt.get("reused"), "matching native turn is already successful; no redispatch")
        self._persist("PREPARED"); self.operation.update(state="RUNNING", started_ns=time.time_ns())
        ledger.journal(self.attempt["id"], self.operation); self.started_monotonic = time.monotonic()
        try:
            if self.client is None:
                self.client = _TurnClient(self.root, self.protocol, self._started); self.client.__enter__()
            else:
                self.operation["child"] = process_handle(self.client.proc.pid); ledger.journal(self.attempt["id"], self.operation)
            models, cursor = [], None
            for _ in range(20):
                page = self.client.call("model/list", {"limit": 20, **({"cursor": cursor} if cursor else {})})
                models.extend(page["data"]); cursor = page.get("nextCursor")
                if not cursor: break
            require(not cursor, "model catalog exceeds its qualified bound")
            selected = [m for m in models if m.get("model") == spec["selected_model"]]
            require(len(selected) == 1 and any(x["reasoningEffort"] == "max" for x in selected[0]["supportedReasoningEfforts"]), "selected model does not advertise max")
            self.operation["advertised_model_capability"] = {"model": selected[0]["model"], "entry_digest": digest(selected[0]),
                "supported_efforts": [x["reasoningEffort"] for x in selected[0]["supportedReasoningEfforts"]]}
            resumed = self.client.call("thread/resume", {"threadId": spec["thread_id"], "excludeTurns": True})
            mode = resumed.get("collaborationMode") or {}
            require(resumed["thread"]["id"] == spec["thread_id"] and resumed["thread"].get("status", {}).get("type") not in {"active", "systemError"} and Path(resumed["cwd"]).resolve() == self.root and
                    resumed["model"] == spec["selected_model"] and resumed.get("reasoningEffort") == "max" and mode.get("mode") == "default" and
                    mode.get("settings", {}).get("model") == spec["selected_model"] and mode.get("settings", {}).get("reasoning_effort") == "max",
                    "accepted native model/mode/max effort is unavailable or changed")
            self.operation["accepted_configuration"] = {"model": resumed["model"], "effort": resumed["reasoningEffort"], "mode": mode["mode"], "reply_digest": digest(resumed)}
            self.operation["accepted_configuration"].update({key: resumed.get(key) for key in
                ("modelProvider", "approvalPolicy", "approvalsReviewer", "sandbox", "activePermissionProfile", "serviceTier")})
            self._drain()
            require(self.events.status != "inProgress" and not self.events.blockers, "resumed native chat is already active or unqualified")
            fresh = WorkspaceLease(self.root).qualify(spec["owner"])
            require(fresh["status"] == "idle" and fresh["turn_id"] == self.operation["source_parent_turn"] and fresh["goal"]["status"] == "active" and fresh["mode"] == "default" and
                    fresh["model"] == spec["selected_model"] and fresh["effort"] == "max" and bindings_current(self.root, spec["inputs"]),
                    "native state or source changed immediately before model dispatch")
            self.operation["start_sent"] = True; ledger.journal(self.attempt["id"], self.operation)
            reply = self.client.call("turn/start", {"threadId": spec["thread_id"], "input": spec["input"],
                "clientUserMessageId": spec["authorization_id"], "model": spec["selected_model"], "effort": "max",
                **({"parentTurnId": self.operation["source_parent_turn"]} if spec["role"] != "executor" else {}),
                "collaborationMode": {"mode": "default", "settings": {"model": spec["selected_model"], "reasoning_effort": "max", "developer_instructions": None}}})
            turn = reply["turn"]; require(type(turn.get("id")) is str and turn["id"] and turn["status"] in TERMINAL | {"inProgress"}, "invalid native turn handle")
            self.operation["turn_id"] = turn["id"]; self.events.turn_id = turn["id"]; self.events.status = turn["status"]
            self.operation["start_reply"] = {"turn_id": turn["id"], "status": turn["status"], "sha256": digest(reply)}
        except CodexRpcError as error:
            self.operation["start_error"] = {"method": error.method, "code": error.code, "message": error.message}
        except Exception as error:
            self.operation["start_observation_error"] = type(error).__name__
        self._drain(); ledger.journal(self.attempt["id"], self.operation)
        if not self.operation["start_sent"] or self.operation.get("start_error", {}).get("method") == "turn/start":
            return self._finish("FAILED", native_status="not_started")
        self._persist("RUNNING" if self.operation.get("turn_id") else "UNKNOWN")
        return self.poll(0)

    def _started(self, handle: dict) -> None:
        self.operation["child"] = handle; BudgetLedger(self.root).journal(self.attempt["id"], self.operation); self._persist("PREPARED")

    def _drain(self) -> None:
        if self.client is None: return
        self.operation["rpc_observations"] = list(self.client.calls[self.call_cursor:])
        self.operation["initialization_digest"] = digest(self.client.initialization) if self.client.initialization is not None else None
        pending, self.client.events = self.client.events, []
        for message in pending: self._consume(message)

    def _consume(self, message: dict) -> None:
        method = message.get("method"); params = message.get("params", {})
        if not method: return
        if "id" in message:
            self.operation.setdefault("user_action_requests", []).append({"id": message["id"], "method": method, "sha256": digest(message)})
            require(len(self.operation["user_action_requests"]) <= 200, "native user-action request bound exceeded")
            return
        if params.get("threadId") != self.spec["thread_id"]: return
        if method == "turn/plan/updated":
            mapping = []
            for step in params.get("plan", []):
                names = sorted(set(re.findall(r"\b[ABD][0-9]{2}\b", step.get("step", ""))))
                mapping.append({"step_sha256": digest(step), "explicit_milestones": names})
                if not set(names) <= set(self.spec["allowed_milestones"]):
                    self.events.blockers.append("NATIVE_PLAN_SCOPE_DRIFT")
            self.operation["runtime_plan_mapping"] = {"steps": mapping,
                "limit": "Only explicit milestone IDs are mapped; descriptive steps do not replace the adopted Plan"}
        if method == "error":
            self.operation.setdefault("native_errors", []).append({"turn_id": params.get("turnId"),
                "will_retry": params.get("willRetry"), "sha256": digest(message),
                "contract": self.protocol["selected"].get("ErrorNotification")})
        if method in PUBLIC_EVENTS:
            try: self.events.consume(message)
            except Exception as error:
                self.events.blockers.append("INVALID_NATIVE_EVENT:" + type(error).__name__)
            if self.events.turn_id:
                require(not self.operation.get("turn_id") or self.operation["turn_id"] == self.events.turn_id, "native stream changed its owned turn")
                self.operation["turn_id"] = self.events.turn_id
            if method == "thread/tokenUsage/updated" and self.events.usage:
                mapping = {"inputTokens": "input_tokens", "cachedInputTokens": "cached_input_tokens", "outputTokens": "output_tokens",
                           "reasoningOutputTokens": "reasoning_output_tokens", "totalTokens": "total_tokens"}
                totals = {target: self.events.usage.get(source) for source, target in mapping.items()}
                BudgetLedger(self.root).observe_categories(self.spec["thread_id"], digest(message), totals,
                    {"transport": "owned_native_stdio_notification", "server": self.operation["child"], "notification_sha256": digest(message)})

    def poll(self, timeout: float = 1) -> dict:
        require(0 <= timeout <= 1 and self.attempt is not None, "poll requires an existing native operation and a bounded wait")
        self._record(); self._drain()
        if self.client is not None:
            try:
                for index in range(1000):
                    message = self.client._receive(timeout if index == 0 else 0)
                    if message is None: break
                    self._consume(message)
            except Exception as error:
                self.operation["stream_error"] = type(error).__name__
        self.operation["event_projection"] = {"turn_id": self.events.turn_id, "status": self.events.status,
            "plans": self.events.plans, "usage": self.events.usage, "blockers": self.events.blockers,
            "observed": self.events.observed}
        BudgetLedger(self.root).journal(self.attempt["id"], self.operation)
        if self.started_monotonic is not None and time.monotonic() - self.started_monotonic >= self.spec["max_seconds"]:
            self.operation["deadline_exceeded"] = True
            if not any(c["action"] == "interrupt" for c in self.operation["controls"]) and self.operation.get("turn_id"):
                self.interrupt(user_authorized=True, authorization_id="deadline:" + self.attempt["id"])
        return self.recover()

    def steer(self, text: str, *, user_authorized: bool, authorization_id: str) -> dict:
        require(type(text) is str and text.strip() and len(text.encode()) <= 128000, "bounded steering text required")
        observation = WorkspaceLease(self.root).qualify(self.spec["owner"])
        require(observation["goal"]["status"] == "active" and observation["mode"] == "default" and observation["effort"] == "max" and
                observation["model"] == self.spec["selected_model"], "steering production work requires current authorized execution settings")
        return self._control("steer", {"threadId": self.spec["thread_id"], "expectedTurnId": self.operation["turn_id"],
            "input": [{"type": "text", "text": text}], "clientUserMessageId": authorization_id}, user_authorized, authorization_id)

    def interrupt(self, *, user_authorized: bool, authorization_id: str) -> dict:
        return self._control("interrupt", {"threadId": self.spec["thread_id"], "turnId": self.operation["turn_id"]}, user_authorized, authorization_id)

    def _control(self, action: str, params: dict, user_authorized: bool, authorization_id: str) -> dict:
        self._record(); require(user_authorized and type(authorization_id) is str and 0 < len(authorization_id) <= 128 and
                               self.client is not None and self.operation.get("turn_id"), "explicit owned native control authorization/handle required")
        ledger = BudgetLedger(self.root); attempt = next(a for a in ledger.read()["attempts"] if a["id"] == self.attempt["id"])
        require(attempt["status"] == "RESERVED", "native turn is already terminal")
        require(not any(c["authorization_id"] == authorization_id for c in self.operation["controls"]), "native control already attempted; no redispatch")
        control = {"action": action, "authorization_id": authorization_id, "request": params, "state": "PREPARED"}
        self.operation["controls"].append(control); ledger.journal(self.attempt["id"], self.operation)
        try:
            reply = self.client.call("turn/" + action, params)
            require(action != "steer" or reply.get("turnId") == self.operation["turn_id"], "steering accepted another native turn")
            control.update(state="ACKNOWLEDGED", response_digest=digest(reply))
        except CodexRpcError as error:
            control.update(state="REJECTED", error_code=error.code, message=error.message)
        except Exception as error:
            control.update(state="UNKNOWN", observation_error=type(error).__name__)
        self._drain(); ledger.journal(self.attempt["id"], self.operation); self._persist("RUNNING", last_control=control)
        return control

    def recover(self) -> dict:
        """Read the original native handle. Never resume or start a replacement."""
        initial = ProjectAdapter(self.root).read()["execution"]
        if inspect_process(initial["workspace_lease"]) in RETIRED:
            return _recover_retired_turn(self.root, self.protocol)
        adapter, record, execution = self._record(); transition = execution.get("managed_turn")
        require(transition is not None, "no managed native turn exists")
        ledger = BudgetLedger(self.root); attempt = next(a for a in ledger.read()["attempts"] if a["id"] == transition["attempt"])
        operation = attempt["operation"]; require(bindings_current(self.root, [operation["spec"]]), "native specification evidence changed")
        self.attempt = attempt; self.operation = operation; self.spec = read_json(confined_path(self.root, operation["spec"]["path"]))
        if self.events is None:
            self.events = NativeEventState(self.spec["thread_id"], self.spec["selected_model"])
            projection = operation.get("event_projection", {})
            for attribute in ("turn_id", "status", "plans", "usage", "blockers", "observed"):
                if attribute in projection: setattr(self.events, attribute, projection[attribute])
        if attempt["status"] != "RESERVED":
            if transition["state"] != attempt["status"]:
                require(attempt.get("receipt") and bindings_current(self.root, attempt["receipt"].get("artifacts", [])), "terminal native receipt changed")
                self._persist(attempt["status"], result=attempt["receipt"]["result"])
            return {"state": attempt["status"], "attempt": attempt["id"], "already_terminal": True}
        turn_id = operation.get("turn_id"); native_status = None; outcome = None
        try:
            with NativeRpc(self.root, self.protocol) as rpc:
                goal = rpc.call("thread/goal/get", {"threadId": self.spec["thread_id"]})["goal"]
                binding = None
                try: binding = _bind_observed_goal(self.root, compile_roadmaps(self.root), execution["native_binding"], goal)
                except Exception as error: self.operation["goal_reconciliation_error"] = type(error).__name__
                turns = rpc.turns(self.spec["thread_id"])
                thread = rpc.call("thread/read", {"threadId": self.spec["thread_id"], "includeTurns": False})["thread"]
            ledger.observe_usage(self.spec["thread_id"], digest({"goal": goal}), binding["observation"]["tokensUsed"] if binding else None)
            require(not any(t["status"] == "inProgress" and t["id"] != turn_id for t in turns), "another native turn is active")
            native_status = next((t["status"] for t in turns if t["id"] == turn_id), None)
            metadata = read_session_metadata(Path(thread["path"]), self.spec["thread_id"])
            context = metadata["context"]
            effective = context["turn_id"] == turn_id and context["model"] == self.spec["selected_model"] and context["effort"] == "max" and context["mode"] == "default" and not metadata.get("routing")
            self.operation["effective_configuration"] = {"confirmed": effective, "native_context": context}
            self.operation["native_status"] = native_status
            self.operation["native_goal_observation"] = goal
            if native_status in TERMINAL:
                blockers = operation.get("event_projection", {}).get("blockers", [])
                controls_ok = all(c["state"] == "ACKNOWLEDGED" for c in operation["controls"]) and not operation.get("user_action_requests")
                outcome = "INTERRUPTED" if native_status == "interrupted" else "SUCCESS" if native_status == "completed" and effective and binding and controls_ok and not blockers and not operation.get("deadline_exceeded") else "FAILED"
        except Exception as error:
            self.operation["recovery_observation_error"] = type(error).__name__
        if outcome is not None:
            return self._finish(outcome, native_status=native_status)
        ledger.journal(attempt["id"], self.operation)
        state = "AWAITING_USER_ACTION" if operation.get("user_action_requests") else "RUNNING" if native_status == "inProgress" else "UNKNOWN"
        self._persist(state)
        return {"state": state, "attempt": attempt["id"], "native_turn_id": turn_id, "native_status": native_status,
                "required_user_action": operation.get("user_action_requests", []), "no_redispatch": True}

    def _finish(self, outcome: str, *, native_status: str) -> dict:
        result = {"schema": 1, "kind": "native_turn_observation", "spec_digest": self.spec["digest"],
            "attempt": self.attempt["id"], "outcome": outcome, "native_status": native_status,
            "operation": self.operation, "domain_proof": False, "installed_artifact_acceptance": False,
            "source_after": _source_inputs(self.root, compile_roadmaps(self.root)),
            "limits": ["Native turn lifecycle/configuration only; model output is not implementation acceptance",
                       "No Goal completion, source equivalence or domain proof is conferred"]}
        binding = _immutable(self.root, str(Path(self.operation["spec"]["path"]).parent / ("result-" + digest(result) + ".json")), result)
        self.operation["terminal_observation"] = binding
        BudgetLedger(self.root).journal(self.attempt["id"], self.operation)
        receipt = {"inputs": self.spec["digest"], "result": binding, "artifacts": [self.operation["spec"], binding],
                   "native_status": native_status, "native_turn_id": self.operation.get("turn_id"),
                   "domain_proof": False, "unknown_usage": not bool(self.operation.get("event_projection", {}).get("usage"))}
        BudgetLedger(self.root).close(self.attempt["id"], outcome, receipt); self._persist(outcome, result=binding)
        return {"state": outcome, "attempt": self.attempt["id"], "native_turn_id": self.operation.get("turn_id"), "native_status": native_status, "result": binding}

    def close(self) -> None:
        if self.client is not None:
            self.client.__exit__(); self.client = None
        # Exiting the transport is not native termination evidence. Its durable
        # turn reservation and workspace owner stay in place until recovery.


def validate_native_turn_receipt(root: Path, spec: dict, receipt: dict, *, current_outputs: bool = False) -> None:
    require(spec.get("kind") == "managed_native_turn" and receipt.get("inputs") == spec["digest"] and
            receipt.get("native_status") == "completed" and receipt.get("domain_proof") is False and
            bindings_current(root, receipt.get("artifacts", [])), "native success receipt is stale or incomplete")
    result = read_json(confined_path(root, receipt["result"]["path"]))
    require(result["spec_digest"] == spec["digest"] and result["outcome"] == "SUCCESS" and
            result["operation"]["effective_configuration"]["confirmed"] is True and
            result["operation"]["turn_id"] == receipt["native_turn_id"], "native receipt contradicts actual turn observations")
    require(not current_outputs or result.get("source_after") and bindings_current(root, result["source_after"]),
            "native turn's observed outputs changed; its lifecycle receipt cannot be reused")


def _recover_retired_turn(root: Path, protocol: dict) -> dict:
    """Reconcile a dead driver under the existing lease/transaction locks.

    No owner is displaced. A later explicit adoption must still pass all native
    idleness and process checks. Unknown handles and surviving tools stay open.
    """
    _protocol(root, protocol); adapter = ProjectAdapter(root); lease = WorkspaceLease(root)
    lock = FileLock(lease.lock_path, "retired managed native turn recovery"); lock.acquire()
    try:
        before = adapter.profile.path().read_bytes(); record = adapter.read(); execution = record["execution"]
        owner = execution["workspace_lease"]; managed = execution.get("managed_runner", {})
        require(managed.get("state_home") == _state_home(), "retired native state routing changed")
        require(execution.get("integration_path") == "managed_app_server" and lease.read()["active"] == owner and
                inspect_process(owner) in RETIRED, "retired managed ownership changed")
        transition = execution["managed_turn"]; ledger = BudgetLedger(root)
        attempt = next(a for a in ledger.read()["attempts"] if a["id"] == transition["attempt"])
        operation = attempt["operation"]; require(operation["owner"] == owner and bindings_current(root, [operation["spec"]]), "retired native reservation lineage changed")
        if attempt["status"] == "RESERVED":
            children = [a for a in ledger.read()["attempts"] if a["status"] == "RESERVED" and
                        a.get("operation", {}).get("parent_native_attempt") == attempt["id"]]
            server = operation.get("child") or managed.get("server")
            if children or not server or inspect_process(server) not in RETIRED or not operation.get("turn_id"):
                return {"state": "UNKNOWN", "attempt": attempt["id"], "reason": "native/process/child handles require further observation", "no_redispatch": True}
            try:
                with NativeRpc(root, protocol) as rpc:
                    turns = rpc.turns(operation["native_thread"])
                    thread = rpc.call("thread/read", {"threadId": operation["native_thread"], "includeTurns": False})["thread"]
                    goal = rpc.call("thread/goal/get", {"threadId": operation["native_thread"]})["goal"]
                native_status = next((t["status"] for t in turns if t["id"] == operation["turn_id"]), None)
                if native_status not in TERMINAL:
                    return {"state": "UNKNOWN", "attempt": attempt["id"], "native_status": native_status, "no_redispatch": True}
                spec = read_json(confined_path(root, operation["spec"]["path"]))
                metadata = read_session_metadata(Path(thread["path"]), operation["native_thread"]); context = metadata["context"]
                effective = context["turn_id"] == operation["turn_id"] and context["model"] == spec["selected_model"] and context["effort"] == "max" and context["mode"] == "default" and not metadata.get("routing")
                try: _bind_observed_goal(root, compile_roadmaps(root), execution["native_binding"], goal); goal_matches = True
                except Exception: goal_matches = False
                blockers = operation.get("event_projection", {}).get("blockers", [])
                outcome = "INTERRUPTED" if native_status == "interrupted" else "SUCCESS" if native_status == "completed" and effective and goal_matches and not blockers and not operation.get("user_action_requests") and all(c["state"] == "ACKNOWLEDGED" for c in operation["controls"]) else "FAILED"
                operation["effective_configuration"] = {"confirmed": effective, "native_context": context}
                result = {"schema": 1, "kind": "native_turn_observation", "spec_digest": spec["digest"], "attempt": attempt["id"],
                    "outcome": outcome, "native_status": native_status, "operation": operation,
                    "source_after": _source_inputs(root, compile_roadmaps(root)), "domain_proof": False,
                    "recovery": "retired runner and server; actual original native turn reobserved; no redispatch"}
                binding = _immutable(root, str(Path(operation["spec"]["path"]).parent / ("recovery-" + digest(result) + ".json")), result)
                ledger.close(attempt["id"], outcome, {"inputs": spec["digest"], "result": binding, "artifacts": [operation["spec"], binding],
                    "native_status": native_status, "native_turn_id": operation["turn_id"], "domain_proof": False, "unknown_usage": True})
                attempt = next(a for a in ledger.read()["attempts"] if a["id"] == attempt["id"])
            except (OSError, TimeoutError, ContractError, KeyError) as error:
                return {"state": "UNKNOWN", "attempt": attempt["id"], "observation_error": type(error).__name__, "no_redispatch": True}
        require(attempt["status"] in {"SUCCESS", "FAILED", "INTERRUPTED"} and
                bindings_current(root, attempt["receipt"]["artifacts"]), "terminal retired native receipt changed")
        execution["managed_turn"] = dict(transition, state=attempt["status"], result=attempt["receipt"]["result"])
        require(inspect_process(owner) in RETIRED and lease.read()["active"] == owner, "native owner changed during retired recovery")
        FileTransaction(root, [Mutation(adapter.profile.path(), canonical(record) + b"\n", expected_exists=True, expected_sha256=digest(before))],
            state_dir=root / ".aegis/state/transactions", name=AEGIS_RECORD_WRITER).commit()
        return {"state": attempt["status"], "attempt": attempt["id"], "retired_owner_reconciled": True, "no_redispatch": True}
    finally:
        lock.release()
