"""Durable local reservations and fixed-recipe execution; no model inference."""
from __future__ import annotations

import os
import time
from pathlib import Path

from .atomic import atomic_write_json
from .locks import FileLock
from .process import run_process
from .roadmap_records import bindings_current, digest, read_json, require
from .security import confined_path


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
                total_seconds: int = 1800, diagnosis: str | None = None) -> dict:
        require(bool(work_id) and bool(inputs), "work and input identities required")
        require(type(seconds) is int and 0 < seconds <= total_seconds, "invalid finite reservation")
        require(type(max_attempts) is int and max_attempts > 0, "invalid attempt limit")
        lock = FileLock(self.lock, "roadmap budget reservation")
        lock.acquire()
        try:
            record = self.read()
            prior = [a for a in record["attempts"] if a["work_id"] == work_id]
            require(not any(a["status"] == "RESERVED" for a in prior), "existing operation requires recovery, not redispatch")
            require(not any(a["status"] == "SUCCESS" and a["inputs"] == inputs for a in prior), "matching successful work already exists")
            require(len(prior) < max_attempts, "durable attempt limit exhausted")
            require(sum(a["reserved_seconds"] for a in prior) + seconds <= total_seconds, "durable time limit exhausted")
            if prior:
                require(bool(diagnosis and diagnosis.strip()), "retry requires diagnosis")
                require(prior[-1]["inputs"] != inputs, "unchanged failed inputs cannot retry")
            attempt = {"id": digest({"work": work_id, "inputs": inputs, "ordinal": len(prior) + 1}),
                       "work_id": work_id, "inputs": inputs, "reserved_seconds": seconds,
                       "status": "RESERVED", "diagnosis": diagnosis, "pid": os.getpid(),
                       "created_ns": time.time_ns()}
            record["attempts"].append(attempt)
            atomic_write_json(self.path, record, root=self.root, mode=0o600)
            return attempt
        finally:
            lock.release()

    def close(self, ident: str, outcome: str, receipt: dict) -> None:
        require(outcome in {"SUCCESS", "FAILED", "INTERRUPTED"}, "unknown terminal outcome")
        lock = FileLock(self.lock, "roadmap budget reconciliation")
        lock.acquire()
        try:
            record = self.read()
            matches = [a for a in record["attempts"] if a["id"] == ident]
            require(len(matches) == 1 and matches[0]["status"] == "RESERVED", "unknown or already terminal attempt")
            matches[0].update(status=outcome, receipt=receipt)
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


def run_recipe(root: Path, compiled: dict, name: str, *, diagnosis: str | None = None) -> dict:
    require(bindings_current(root, compiled["inputs"]), "compiled execution inputs became stale")
    require(name in compiled["recipes"], "undeclared recipe")
    recipe = compiled["recipes"][name]
    require(recipe["kind"] == "local_validation", "this recipe is a project execution specification, not an activated command")
    require(recipe["argv"] and recipe["argv"][0] == "python", "only fixed local Python validation recipes are supported")
    import sys
    argv = [sys.executable, "-B", *recipe["argv"][1:]]
    require(all(type(x) is str for x in argv), "invalid argv")
    work_id = digest({"recipe": name, "root": str(root.resolve())})
    inputs = digest({"compiled": compiled["digest"], "recipe": recipe})
    ledger = BudgetLedger(root)
    lease = FileLock(root / ".aegis/roadmaps/execution.lock", "single roadmap recipe execution")
    lease.acquire(timeout=0)
    try:
        attempt = ledger.reserve(work_id, inputs, recipe["max_seconds"],
                                 max_attempts=recipe["max_attempts"], diagnosis=diagnosis)
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
