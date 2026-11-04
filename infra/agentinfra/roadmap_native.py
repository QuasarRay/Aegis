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
from .roadmap_records import bindings_current, digest, read_json, require
from .security import confined_path


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


def _reader_executable(root: Path, installed: dict, running_path: str, running_sha256: str,
                       process_executable: str) -> dict:
    """Use the kernel-retained active binary only with its prior exact pin."""
    deleted = running_path.endswith(" (deleted)")
    original_path = running_path.removesuffix(" (deleted)")
    require(Path(original_path).resolve() == Path(installed["path"]).resolve(),
            "active-host executable path differs from the installed native authority")
    if not deleted:
        require(running_sha256 == installed["sha256"], "active-host executable bytes differ from installed native authority")
        return {"path": installed["path"], "sha256": running_sha256, "route": "installed_active_host"}
    from .roadmap_project import ProjectAdapter
    record = ProjectAdapter(root).read()
    binding = record.get("native_protocol")
    require(binding and bindings_current(root, [binding]), "retained native executable requires its unchanged prior protocol export")
    expected = {"path": str(Path(original_path).resolve()), "sha256": running_sha256}
    for index, candidate in enumerate([binding, *reversed(record.get("native_protocol_history", []))]):
        if not bindings_current(root, [candidate]):
            continue
        manifest = read_json(confined_path(root, candidate["path"], must_exist=True))
        valid = (manifest.get("schema") == 1 and manifest.get("kind") == "installed_codex_protocol_export" and
                 manifest.get("digest") == digest({k: v for k, v in manifest.items() if k != "digest"}) and
                 manifest.get("files") and bindings_current(root, manifest["files"]))
        require(index != 0 or valid, "retained active-host bytes/protocol do not match their prior exact native authority")
        if valid and manifest.get("executable") == expected:
            return {"path": process_executable, "sha256": running_sha256,
                    "route": "kernel_retained_pinned_active_host", "prior_protocol": candidate}
    require(False, "retained active-host bytes/protocol do not match their prior exact native authority")


def observe_native_owner(root: Path, owner: dict) -> dict:
    require(owner.get("host") == socket.gethostname() and
            _pid_alive(owner.get("pid", 0), owner.get("process_identity")), "native owner process is not established")
    from .roadmap_protocol import native_executable
    installed = native_executable()
    owner_executable = Path(f"/proc/{owner['pid']}/exe")
    require(owner_executable.exists(), "active-host executable handle is unavailable")
    running_path = os.readlink(owner_executable)
    route = _reader_executable(root, installed, running_path, digest(owner_executable.read_bytes()), str(owner_executable))
    require(_pid_alive(owner["pid"], owner["process_identity"]), "active-host creation identity changed during executable qualification")
    with CodexReader(executable=route["path"], experimental=True) as client:
        goal = client.call("thread/goal/get", {"threadId": owner["session"]})["goal"]
        thread = client.call("thread/read", {"threadId": owner["session"], "includeTurns": False})["thread"]
        executable = {"path": client.executable, "sha256": digest(Path(client.executable).read_bytes())}
        require(executable["sha256"] == route["sha256"], "native reader bytes changed during active-host observation")
    require(thread.get("id") == owner["session"] and goal and goal.get("threadId") == owner["session"],
            "native Goal/thread identity mismatch")
    require(Path(thread["cwd"]).resolve() == root.resolve(), "native chat belongs to another workspace")
    require(owner_executable.exists() and owner_executable.resolve() == Path(executable["path"]).resolve(),
            "active-host owner must be the observed native executable")
    require(_pid_alive(owner["pid"], owner["process_identity"]) and
            digest(owner_executable.read_bytes()) == route["sha256"], "active-host identity/bytes changed during native observation")
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
              "executable_route": route, "installed_executable": installed,
              "limits": ["Service/journal provenance is an explicit local trust boundary",
                         "notLoaded is observer-local and is never treated as idle",
                         "No inference, native Goal mutation or model rerouting is performed"]}
    result["digest"] = digest(result)
    return result


def _read_transport_binding(root: Path, protocol: dict, native: dict) -> dict:
    """Bind an installed reader to a fresh owned host observation.

    The caller obtains ``native`` directly from WorkspaceLease.qualify, never
    from a supplied observation file. Its existing observer verifies the live
    process and retained executable. This binding keeps both authorities visible
    when an atomic package update leaves the active host on its prior bytes.
    """
    from .roadmap_protocol import assert_protocol
    assert_protocol(root, protocol)
    require(native.get("digest") == digest({k: v for k, v in native.items() if k != "digest"}),
            "owned native observation changed before read-transport binding")
    installed = protocol["executable"]; active = native["executable"]
    route = native.get("executable_route")
    if active != installed:
        require(native.get("kind") == "codex_active_host_observation" and
                native.get("producer") == "agentinfra.roadmap_native.observe_native_owner" and
                native.get("installed_executable") == installed and route and
                route.get("route") == "kernel_retained_pinned_active_host" and
                route.get("path") == active["path"] == f"/proc/{native['owner_process']['pid']}/exe" and
                route.get("sha256") == active["sha256"] and route.get("prior_protocol") and
                bindings_current(root, [route["prior_protocol"]]),
                "read transport requires the verified pinned retained native host")
        previous = read_json(confined_path(root, route["prior_protocol"]["path"], must_exist=True))
        require(previous.get("kind") == "installed_codex_protocol_export" and previous.get("schema") == 1 and
                previous.get("digest") == digest({k: v for k, v in previous.items() if k != "digest"}) and
                previous.get("executable") == {"path": installed["path"], "sha256": active["sha256"]} and
                previous.get("files") and bindings_current(root, previous["files"]),
                "retained native read binding lost its exact prior executable/protocol pin")
    return {"schema": 1, "kind": "installed_reader_owned_host_binding", "installed_transport": installed,
            "active_host": active, "active_host_route": route,
            "owned_observation_digest": native["digest"],
            "limits": ["Fresh cooperating native observer is the process/host provenance boundary",
                       "Separate reader and host pins do not migrate the active process or qualify managed inference"]}
