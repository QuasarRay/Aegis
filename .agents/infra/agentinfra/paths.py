from __future__ import annotations
from pathlib import Path

def find_root(start: Path | None = None) -> Path:
    p = (start or Path.cwd()).resolve()
    for candidate in (p, *p.parents):
        if (candidate / ".agents" / "framework.toml").is_file():
            return candidate
    raise FileNotFoundError("could not find repository containing .agents/framework.toml")

def agents_dir(root: Path) -> Path: return root / ".agents"
def runtime_dir(root: Path) -> Path: return agents_dir(root) / "runtime"
def tasks_dir(root: Path) -> Path: return runtime_dir(root) / "tasks"
def persistent_dir(root: Path) -> Path: return agents_dir(root) / "persistent"
def install_state_dir(root: Path) -> Path: return persistent_dir(root) / "install-state"
