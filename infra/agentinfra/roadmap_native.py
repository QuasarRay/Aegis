"""Read-only active-host Codex observations for execution fencing and usage.

The native service and its local append-only event journal are trust boundaries.
An observer-local notLoaded status never proves another server's turn ended.
Only lifecycle, configuration and usage metadata are retained, not message text.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import socket

from .locks import _pid_alive, _process_identity
from .roadmap_codex import CodexReader
from .roadmap_records import digest, require


INTERFACE_VERSION = 1


def process_handle(pid: int) -> dict:
    identity = _process_identity(pid)
    require(identity is not None and _pid_alive(pid, identity), "process creation identity cannot be established")
    boot = Path("/proc/sys/kernel/random/boot_id")
    return {"pid": pid, "process_identity": identity, "host": socket.gethostname(),
            "boot_identity": digest(boot.read_bytes()) if boot.exists() else None}


def inspect_process(handle: dict) -> str:
    if handle.get("host") != socket.gethostname() or not handle.get("process_identity"):
        return "UNKNOWN"
    boot = Path("/proc/sys/kernel/random/boot_id")
    if handle.get("boot_identity") is not None:
        if not boot.exists():
            return "UNKNOWN"
        if digest(boot.read_bytes()) != handle["boot_identity"]:
            return "PREVIOUS_BOOT"
    pid = handle.get("pid")
    if type(pid) is not int or pid <= 0:
        return "UNKNOWN"
    current = _process_identity(pid)
    if current is None:
        return "UNKNOWN" if _pid_alive(pid) else "GONE"
    return "LIVE" if current == handle["process_identity"] else "REUSED_PID"


def is_process_ancestor(pid: int) -> bool:
    current = os.getpid()
    for _ in range(128):
        if current == pid:
            return True
        path = Path(f"/proc/{current}/status")
        if not path.exists():
            return False
        fields = path.read_text().splitlines()
        parent = int(next(line.split(":", 1)[1].strip() for line in fields if line.startswith("PPid:")))
        if parent <= 0 or parent == current:
            return False
        current = parent
    return False


def read_session_metadata(path: Path, thread_id: str) -> dict:
    session = None
    context = None
    lifecycle = None
    usage = None
    routing = []
    with path.open("rb") as stream:
        while True:
            offset = stream.tell()
            raw = stream.readline(8_000_001)
            if not raw:
                break
            require(len(raw) <= 8_000_000 and raw.endswith(b"\n"), "incomplete or oversized native event; retain unknown ownership")
            event = json.loads(raw)
            kind = event.get("type")
            payload = event.get("payload", {})
            origin = {"path": str(path), "offset": offset, "bytes": len(raw), "sha256": digest(raw),
                      "timestamp": event.get("timestamp")}
            if kind == "session_meta":
                session = {"id": payload.get("id"), "origin": origin}
            elif kind == "turn_context":
                if context is None or context.get("turn_id") != payload.get("turn_id"):
                    routing = []
                context = {"model": payload.get("model"), "effort": payload.get("effort"),
                           "turn_id": payload.get("turn_id"),
                           "mode": payload.get("collaboration_mode", {}).get("mode"),
                           "cwd": payload.get("cwd"), "origin": origin}
            elif kind == "event_msg":
                event_kind = payload.get("type")
                if event_kind in {"task_started", "task_complete", "turn_aborted"}:
                    lifecycle = {"kind": event_kind, "turn_id": payload.get("turn_id"), "origin": origin}
                elif event_kind == "token_count" and payload.get("info"):
                    usage = {"totals": payload["info"].get("total_token_usage"), "origin": origin}
                elif event_kind == "model_rerouted":
                    routing.append({"turn_id": payload.get("turn_id"), "from_model": payload.get("from_model"),
                                    "to_model": payload.get("to_model"), "origin": origin})
    require(session and session["id"] == thread_id, "native journal belongs to another chat")
    require(context and lifecycle and lifecycle.get("turn_id"), "native turn state is not established")
    return {"session": session, "context": context, "lifecycle": lifecycle, "usage": usage, "routing": routing}


def observe_native_owner(root: Path, owner: dict) -> dict:
    require(owner.get("host") == socket.gethostname() and
            _pid_alive(owner.get("pid", 0), owner.get("process_identity")), "native owner process is not established")
    with CodexReader(experimental=True) as client:
        goal = client.call("thread/goal/get", {"threadId": owner["session"]})["goal"]
        thread = client.call("thread/read", {"threadId": owner["session"], "includeTurns": False})["thread"]
        executable = {"path": client.executable, "sha256": digest(Path(client.executable).read_bytes())}
    require(thread.get("id") == owner["session"] and goal and goal.get("threadId") == owner["session"],
            "native Goal/thread identity mismatch")
    require(Path(thread["cwd"]).resolve() == root.resolve(), "native chat belongs to another workspace")
    owner_executable = Path(f"/proc/{owner['pid']}/exe")
    require(owner_executable.exists() and owner_executable.resolve() == Path(executable["path"]).resolve(),
            "active-host owner must be the observed native executable")
    metadata = read_session_metadata(Path(thread["path"]), owner["session"])
    context = metadata["context"]
    require(not metadata["routing"], "native journal reports a model reroute")
    require(context.get("turn_id") == metadata["lifecycle"]["turn_id"],
            "effective configuration is not bound to the observed native turn")
    require(thread.get("model") == context["model"] and thread.get("reasoningEffort") == context["effort"],
            "native model/effort observations disagree")
    state = "active" if metadata["lifecycle"]["kind"] == "task_started" else "idle"
    result = {"schema": INTERFACE_VERSION, "kind": "codex_active_host_observation",
              "producer": "agentinfra.roadmap_native.observe_native_owner", "session": owner["session"],
              "status": state, "goal": goal, "model": context["model"], "effort": context["effort"],
              "mode": context["mode"], "turn_id": metadata["lifecycle"]["turn_id"],
              "owner_process": process_handle(owner["pid"]), "caller_is_descendant": is_process_ancestor(owner["pid"]),
              "observer_server_status": thread.get("status"), "executable": executable, "metadata": metadata,
              "limits": ["Service/journal provenance is an explicit local trust boundary",
                         "notLoaded is observer-local and is never treated as idle",
                         "No inference, native Goal mutation or model rerouting is performed"]}
    result["digest"] = digest(result)
    return result
