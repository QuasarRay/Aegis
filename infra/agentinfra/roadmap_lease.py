"""One fenced workspace lease, composing existing atomic writes and process locks.

The qualified native transport supplies session observations. A dead local
process alone never proves a remote/native turn stopped.
"""
from __future__ import annotations

import os
import socket
from pathlib import Path
import uuid

from .atomic import atomic_write_json
from .locks import FileLock, _pid_alive, _process_identity
from .roadmap_records import read_json, require


class WorkspaceLease:
    def __init__(self, coordination_root: Path):
        self.root = coordination_root.resolve()
        self.path = self.root / ".aegis/coordination/lease.json"
        self.lock_path = self.path.with_suffix(".lock")

    def read(self) -> dict:
        if not self.path.exists(): return {"schema": 1, "generation": 0, "active": None, "history": []}
        state = read_json(self.path)
        require(state.get("schema") == 1 and type(state.get("generation")) is int, "unknown/corrupt workspace lease")
        return state

    def acquire(self, session: str, operation: str, *, pid: int | None = None) -> dict:
        require(bool(session) and bool(operation), "native session and work identity required")
        pid = os.getpid() if pid is None else pid
        identity = _process_identity(pid)
        require(identity is not None and _pid_alive(pid, identity), "process creation identity cannot be established")
        lock = FileLock(self.lock_path, "workspace lease transaction"); lock.acquire()
        try:
            state = self.read()
            require(state["active"] is None, "active or unresolved native owner blocks transfer")
            state["generation"] += 1
            active = {"fence": state["generation"], "nonce": uuid.uuid4().hex, "session": session,
                      "operation": operation, "pid": pid, "process_identity": identity, "host": socket.gethostname()}
            state["active"] = active
            atomic_write_json(self.path, state, root=self.root, mode=0o600)
            return active
        finally: lock.release()

    def assert_owner(self, owner: dict) -> None:
        require(self.read()["active"] == owner, "stale fencing generation or owner identity")
        require(owner["host"] == socket.gethostname() and _pid_alive(owner["pid"], owner["process_identity"]), "owner process not established")
        if owner.get("boot_identity") is not None:
            from .roadmap_native import inspect_process
            require(inspect_process(owner) == "LIVE", "owner belongs to another boot or unknown process epoch")

    def qualify(self, owner: dict) -> dict:
        self.assert_owner(owner)
        from .roadmap_native import observe_native_owner
        observation = observe_native_owner(self.root, owner)
        self.assert_owner(owner)
        return observation

    def release_observed(self, owner: dict, *, recovery: bool = False) -> None:
        observation = self.qualify(owner)
        require(observation["status"] == "idle" and observation["goal"]["status"] != "active",
                "active, auto-continuing or ambiguous native ownership prohibits transfer")
        self.release(owner, {"session": owner["session"], "status": "idle", "producer": "qualified_codex_transport",
                             "observation_digest": observation["digest"]}, recovery=recovery)

    def release(self, owner: dict, native_observation: dict, *, recovery: bool = False) -> None:
        canonical = self.root / ".aegis/project.json"
        binding = read_json(canonical).get("execution", {}).get("native_binding", {}) if canonical.exists() else {}
        if binding.get("thread_id") == owner["session"] and binding.get("native_accounting_preserved") is True:
            # Legacy fixtures may supply transport observations. An adopted
            # production Goal must always be checked against the actual service.
            from .roadmap_native import observe_native_owner
            observed = observe_native_owner(self.root, owner)
            require(observed["status"] == "idle" and observed["goal"]["status"] != "active",
                    "active or auto-continuing native Goal prohibits lease release")
        lock = FileLock(self.lock_path, "workspace lease release"); lock.acquire()
        try:
            state = self.read(); require(state["active"] == owner, "stale lease cannot release current owner")
            require(native_observation.get("session") == owner["session"] and
                    native_observation.get("status") in {"idle", "completed", "cancelled"} and
                    native_observation.get("producer") == "qualified_codex_transport",
                    "native turn termination must be observed before transfer")
            if recovery:
                require(owner["host"] == socket.gethostname() and
                        not _pid_alive(owner["pid"], owner["process_identity"]), "recovery cannot displace a live or unknown process")
            state["history"].append({"owner": owner, "observation": native_observation, "recovery": recovery})
            state["active"] = None
            atomic_write_json(self.path, state, root=self.root, mode=0o600)
        finally: lock.release()
