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

    def release(self, owner: dict, native_observation: dict, *, recovery: bool = False) -> None:
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
