"""Bounded, fresh deductive verification of the controller model."""
from argparse import ArgumentParser
from dataclasses import asdict
from pathlib import Path
import json
import os
import shutil
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.atomic import atomic_write_json
from agentinfra.destiny import load_profile, matches_version, reserve_attempt
from agentinfra.destiny_reuse import checked_output, digest, load_json, require
from agentinfra.context_cache import sha256_file
from agentinfra.locks import FileLock
from agentinfra.process import run_process
from agentinfra.security import confined_path


def verify(args):
    pin_path = ROOT / "verification/toolchain.json"
    pin = load_json(pin_path.read_text())
    found = shutil.which(args.verus)
    require(found is not None, "UNAVAILABLE: Verus executable missing")
    verus = Path(found).resolve(strict=True)
    source = confined_path(ROOT, pin["entry"], must_exist=True)
    tools = [verus, verus.parent / "rust_verify", verus.parent / "z3", verus.parent / "vstd.vir",
             verus.parent / "libvstd.rlib", verus.parent / "libverus_builtin.rlib"]
    # Include available platform-specific macro libraries used during verification.
    tools.extend(sorted(verus.parent.glob("*verus*macros.*")))
    require(all(p.is_file() for p in tools), "UNAVAILABLE: incomplete Verus distribution")

    def identity():
        return {"source": sha256_file(source), "pin": sha256_file(pin_path),
                "runner": sha256_file(Path(__file__)),
                "tools": {str(p): sha256_file(p) for p in tools},
                "helpers": {p.name: sha256_file(p) for p in sorted((ROOT / "infra/agentinfra").glob("*.py"))}}

    env = {k: os.environ[k] for k in ("HOME", "CARGO_HOME", "RUSTUP_HOME", "RUSTUP_TOOLCHAIN") if k in os.environ}
    env.update({"RUSTUP_AUTO_INSTALL": "0", "CARGO_NET_OFFLINE": "true", "NO_COLOR": "1",
                "VERUS_Z3_PATH": str(verus.parent / "z3")})
    lock = FileLock(ROOT / ".aegis/formal-controller/run.lock", "controller-model-verification")
    lock.acquire(timeout=0)
    try:
        before = identity()
        key = digest({"controller_model": before, "environment": env})
        require(reserve_attempt(ROOT, load_profile(), key, pin["timeout_seconds"], args.reason), "BUDGET_EXCEEDED: identical model attempt limit reached")
        started = time.monotonic()
        outputs = []
        for argv, version in (([str(verus), "--version"], pin["verus"]),
                              ([str(verus.parent / "z3"), "--version"], pin["z3"])):
            remaining = pin["timeout_seconds"] - (time.monotonic() - started)
            require(remaining > 0, "TIMEOUT: model probe budget exhausted")
            result = run_process(argv, cwd=ROOT, env=env, timeout=min(10, remaining), capture_limit=4000)
            outputs.append(asdict(result))
            require(result.returncode == 0 and not result.timed_out and not result.stdout_truncated
                    and not result.stderr_truncated and matches_version(version, result.stdout + result.stderr),
                    "UNAVAILABLE: pinned controller-model verifier/solver version differs")
        remaining = pin["timeout_seconds"] - (time.monotonic() - started)
        require(remaining > 0, "TIMEOUT: model verification budget exhausted")
        result = run_process([str(verus), "--crate-type=lib", "--no-cheating", "--num-threads", "1", str(source)],
                             cwd=ROOT, env=env, timeout=remaining, capture_limit=16_000)
        require(identity() == before, "INPUTS_CHANGED: model or tool distribution changed during verification")
        passed = checked_output({"method": "verus", "expected_checks": pin["expected_checks"]}, result)
        record = {"schema": 1, "status": "CHECKED_MODEL" if passed else "FAILED", "identity": before,
                  "environment": env, "probes": outputs, "execution": asdict(result),
                  "expected_checks": pin["expected_checks"], "claim": pin["scope"]}
        record["sha256"] = digest(record)
        receipt = ROOT / ".aegis/formal-controller" / (record["sha256"] + ".json")
        atomic_write_json(receipt, record)
        return {"status": record["status"], "receipt": str(receipt), "checks": pin["expected_checks"], "claim": pin["scope"]}
    finally:
        lock.release()


if __name__ == "__main__":
    p = ArgumentParser(description=__doc__)
    p.add_argument("--verus", default="verus")
    p.add_argument("--reason", help="diagnosis for another attempt with identical inputs")
    args = p.parse_args()
    try:
        result = verify(args)
    except (OSError, ValueError, RuntimeError, KeyError, TypeError) as exc:
        result = {"status": "ERROR", "reason": str(exc)}
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "CHECKED_MODEL" else 1)
