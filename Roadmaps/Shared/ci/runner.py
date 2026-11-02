"""Shared local/GitLab Dagger recipe. Requires a qualified pinned runner/image."""
from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from importlib.metadata import version

ENGINE = "0.21.11"
ROOT = Path(__file__).resolve().parents[3]
CHECKS = [
    ["python", "-B", "scripts/validate_roadmaps.py"],
    ["python", "-B", "-m", "unittest", "discover", "-s", "infra/tests", "-p", "test_roadmap*.py", "-q"],
    ["python", "-B", "bin/agentctl.py", "portability", "check"],
    ["python", "-B", "verification/roadmap/policy_harness.py"],
]


async def run() -> None:
    import dagger
    observed = subprocess.run(["dagger", "version"], capture_output=True, text=True, check=True, timeout=10).stdout
    if not re.search(r"\bv" + re.escape(ENGINE) + r"\b", observed) or version("dagger-io") != ENGINE:
        raise RuntimeError("Dagger engine/SDK differs from the accepted recipe pin")
    image = os.environ.get("AEGIS_CI_PYTHON_IMAGE", "")
    if not re.fullmatch(r"[^\s]+@sha256:[a-f0-9]{64}", image):
        raise RuntimeError("AEGIS_CI_PYTHON_IMAGE must be a qualified immutable Python 3.14 image digest")
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        source = client.host().directory(str(ROOT), exclude=[".git", ".aegis", "**/__pycache__"])
        container = client.container().from_(image).with_directory("/src", source).with_workdir("/src")
        results = []
        for argv in CHECKS:
            container = container.with_exec(argv)
            results.append({"argv": argv, "stdout": await container.stdout()})
        path = ROOT / ".aegis/ci/roadmap.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"schema": 1, "engine": ENGINE, "image": image,
                                   "results": results, "scope": "roadmap package only"}, indent=2) + "\n")


if __name__ == "__main__":
    asyncio.run(run())
