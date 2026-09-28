"""HOL4/hol4-mcp orchestration.

hol4-mcp is an editing/proof-navigation aid.  Acceptance is always a direct
HOL4 kernel build via Holmake; MCP output is never promoted to proof evidence.
"""
from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import os
import shutil

from .contracts import FRAMEWORK, digest, read_json, require
from .process import run_process
from .security import confined_path


def pins():
    lock = read_json(FRAMEWORK / "contracts/toolchain.json")
    return {
        "hol4_repo": lock["hol4_repo"],
        "hol4_commit": lock["hol4_commit"],
        "hol4_mcp_repo": lock["hol4_mcp_repo"],
        "hol4_mcp_commit": lock["hol4_mcp_commit"],
        "hol4_mcp_version": lock["hol4_mcp_version"],
    }


def hol4_home() -> Path:
    value = os.environ.get("HOLDIR")
    require(bool(value), "HOLDIR must point at the pinned HOL4 checkout")
    home = Path(value).resolve(strict=True)
    require((home / "bin/Holmake").is_file(), "HOLDIR has no built bin/Holmake")
    return home


def executable_identity(path: Path) -> dict:
    path = path.resolve(strict=True)
    return {"path": str(path), "sha256": digest(path.read_bytes())}


def identity() -> dict:
    mcp = shutil.which("hol4-mcp")
    require(mcp is not None, "required tool unavailable: hol4-mcp")
    return {
        "pins": pins(),
        "Holmake": executable_identity(hol4_home() / "bin/Holmake"),
        "hol4-mcp": executable_identity(Path(mcp)),
    }


def tactictoe_cache(root: Path) -> Path:
    root = Path(root).resolve(strict=True)
    cache = confined_path(root, ".aegis/tactictoe-cache")
    cache.mkdir(parents=True, exist_ok=True)
    return cache


def environment(root: Path) -> dict[str, str]:
    return {
        "HOLDIR": str(hol4_home()),
        "HOL4_TACTICTOE_CACHE": str(tactictoe_cache(root)),
        **({"HOME": os.environ["HOME"]} if "HOME" in os.environ else {}),
    }


def mcp_stdio_config(root: Path) -> dict:
    """Configuration consumable by an MCP client; not verification evidence."""
    mcp = shutil.which("hol4-mcp")
    require(mcp is not None, "required tool unavailable: hol4-mcp")
    return {
        "command": str(Path(mcp).resolve(strict=True)),
        "args": ["--transport", "stdio"],
        "env": {
            "HOLDIR": str(hol4_home()),
            "HOL4_TACTICTOE_CACHE": str(tactictoe_cache(root)),
        },
        "identity": identity(),
        "claim": "orchestration only; final acceptance requires direct Holmake",
    }


def holmake(root: Path, workdir: str = ".", timeout: int = 600) -> dict:
    """Run the trusted acceptance boundary directly, bypassing hol4-mcp."""
    root = Path(root).resolve(strict=True)
    cwd = confined_path(root, workdir, must_exist=True)
    require(cwd.is_dir(), "HOL4 workdir is not a directory")
    before = identity()
    result = run_process(
        [str(hol4_home() / "bin/Holmake"), "--qof"],
        cwd=cwd,
        timeout=timeout,
        env=environment(root),
    )
    require(identity() == before, "HOL4 or hol4-mcp executable changed during verification")
    checked = (
        result.returncode == 0
        and not result.timed_out
        and not result.stdout_truncated
        and not result.stderr_truncated
    )
    return {
        "status": "CHECKED" if checked else "FAILED",
        "tool_identity": before,
        "execution": asdict(result),
        "claim": "direct HOL4 kernel build; hol4-mcp is outside the trusted acceptance path",
    }
