"""Bounded Codex stdio protocol transport and native observation bindings.

No method here creates a thread or starts a model turn. Live Goal mutations must
be invoked through the current host's authorized native lifecycle interface.
"""
from __future__ import annotations

import os
import select
import shutil
import subprocess
import time
from pathlib import Path

from .roadmap_records import ContractError, canonical, digest, loads, require
from .security import redact_text


class CodexRpcError(ContractError):
    """An actual error reply, distinct from timeout or an unobserved outcome."""
    def __init__(self, method: str, error: dict):
        self.method = method
        self.code = error.get("code")
        self.message = redact_text(str(error.get("message", "native request rejected")))[:2000]
        super().__init__(f"Codex protocol error: {self.code}: {self.message}")


class CodexReader:
    ALLOWED = {"initialize", "model/list", "thread/goal/get", "thread/read", "collaborationMode/list",
               "thread/list", "thread/turns/list", "thread/items/list"}

    def __init__(self, executable: str = "codex", timeout: float = 15, *, experimental: bool = False):
        require(0 < timeout <= 60, "protocol timeout must be finite and bounded")
        self.executable = shutil.which(executable)
        require(bool(self.executable), "Codex executable unavailable")
        self.timeout = timeout
        self.experimental = experimental
        self.proc = None
        self.buffer = b""
        self.next_id = 0
        self.events = []
        self.initialization = None

    def __enter__(self):
        self.proc = subprocess.Popen([self.executable, "app-server", "--listen", "stdio://"],
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.DEVNULL, bufsize=0)
        try:
            from . import __version__
            self.initialization = self.call("initialize", {"clientInfo": {"name": "aegis-roadmap", "title": "Aegis roadmap", "version": __version__},
                                     "capabilities": {"experimentalApi": self.experimental}})
            self.proc.stdin.write(canonical({"method": "initialized"}) + b"\n")
        except BaseException:
            self.__exit__()
            raise
        return self

    def call(self, method: str, params: dict) -> dict:
        require(method in self.ALLOWED, "read-only Codex adapter refuses this method")
        require(self.proc is not None, "Codex transport not initialized")
        self.next_id += 1
        ident = self.next_id
        self.proc.stdin.write(canonical({"id": ident, "method": method, "params": params}) + b"\n")
        deadline = time.monotonic() + self.timeout
        while time.monotonic() < deadline:
            if b"\n" in self.buffer:
                line, self.buffer = self.buffer.split(b"\n", 1)
                message = loads(line.decode())
                if message.get("id") == ident:
                    if "error" in message:
                        raise CodexRpcError(method, message["error"])
                    return message["result"]
                self.events.append(message)
                require(len(self.events) <= 1000, "too many unsolicited protocol events")
                continue
            ready, _, _ = select.select([self.proc.stdout], [], [], max(0, deadline - time.monotonic()))
            if ready:
                chunk = os.read(self.proc.stdout.fileno(), 65536)
                require(bool(chunk), "Codex transport closed before response")
                self.buffer += chunk
                require(len(self.buffer) <= 2_000_000, "oversized Codex protocol response")
        raise TimeoutError(f"Codex {method} exceeded {self.timeout}s")

    def __exit__(self, *_):
        if self.proc:
            try:
                self.proc.stdin.close()
            except BrokenPipeError:
                pass
            try:
                self.proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.proc.terminate()
                try:
                    self.proc.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    self.proc.kill()
                    self.proc.wait(timeout=2)
            self.proc.stdout.close()


def capabilities() -> dict:
    with CodexReader() as client:
        version = subprocess.run([client.executable, "--version"], capture_output=True, text=True, timeout=10, check=True).stdout.strip()
        models, cursor = [], None
        for _ in range(20):
            result = client.call("model/list", {"cursor": cursor} if cursor else {})
            models.extend({"id": m.get("id"), "model": m.get("model"),
                           "supported_efforts": m.get("supportedReasoningEfforts", [])} for m in result.get("data", []))
            cursor = result.get("nextCursor")
            if not cursor:
                break
        require(not cursor, "model catalog pagination exceeded bound")
        return {"schema": 1, "provider": "codex", "version": version,
                "executable_sha256": digest(Path(client.executable).read_bytes()),
                "models": models, "reasoning_requested": "max", "effective_reasoning": None,
                "tested_operations": ["initialize", "model/list"],
                "limit": "catalog discovery only; no inference, entitlement, Goal or Plan activation"}


def bind_goal(observation: dict, *, thread_id: str, objective: str, contract_hash: str) -> dict:
    goal = observation.get("goal", observation)
    require(goal.get("threadId", goal.get("thread_id")) == thread_id, "native Goal belongs to another chat")
    require(goal.get("objective") == objective and bool(objective), "native objective mismatch")
    require(goal.get("status") in {"active", "paused", "blocked", "complete", "budget_limited", "usage_limited", "budgetLimited", "usageLimited"}, "unknown native Goal state")
    require(len(contract_hash) == 64, "contract digest required")
    return {"schema": 1, "thread_id": thread_id, "objective": objective,
            "contract_digest": contract_hash, "observation": goal,
            "observation_digest": digest(observation), "native_accounting_preserved": True}


def bind_plan(plan: dict, milestone_ids: list[str], compiled: dict) -> dict:
    require(bool(plan.get("id")) and plan.get("type") == "plan" and bool(plan.get("text")), "completed native plan item required")
    require(milestone_ids and len(set(milestone_ids)) == len(milestone_ids), "empty or duplicate milestone mapping")
    require(set(milestone_ids) <= set(compiled["milestones"]), "plan references unknown scope")
    return {"schema": 1, "native_item_digest": digest(plan), "native_item_id": plan["id"],
            "compiled_digest": compiled["digest"], "milestones": milestone_ids,
            "activation": "requires native execution authorization"}


def read_native_goal(thread_id: str) -> dict:
    require(bool(thread_id), "actual native thread identity required")
    with CodexReader(experimental=True) as client:
        return client.call("thread/goal/get", {"threadId": thread_id})
