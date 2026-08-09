from __future__ import annotations

import argparse
import hashlib
import json
import stat
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".agents" / "infra"))

from agentinfra.atomic import atomic_write_bytes
from agentinfra.manifest import entries
from agentinfra.security import confined_path


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sync(root: Path, *, apply: bool = False, maintenance_authorized: bool = False) -> dict:
    root = root.resolve(strict=True)
    if apply and not maintenance_authorized:
        raise RuntimeError("release/install mirror synchronization requires explicit maintenance authorization")
    changed: list[str] = []
    checked = 0
    for installed_relative, _ in entries(root):
        installed = confined_path(root, installed_relative, must_exist=True, reject_symlinks=True)
        source_relative = Path(installed_relative).relative_to(".agents").as_posix()
        source = confined_path(root, source_relative, reject_symlinks=True)
        payload = installed.read_bytes()
        checked += 1
        if source.is_file() and digest(source.read_bytes()) == digest(payload):
            continue
        changed.append(source_relative)
        if apply:
            mode = stat.S_IMODE(installed.stat(follow_symlinks=False).st_mode)
            atomic_write_bytes(source, payload, root=root, mode=mode)
    remaining = []
    if apply:
        for installed_relative, _ in entries(root):
            installed = root / installed_relative
            source_relative = Path(installed_relative).relative_to(".agents").as_posix()
            source = root / source_relative
            if not source.is_file() or digest(source.read_bytes()) != digest(installed.read_bytes()):
                remaining.append(source_relative)
    return {"applied": apply, "checked": checked, "changed": changed, "remaining_mismatches": remaining}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Synchronize the immutable release-source mirror from .agents")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--maintenance-authorized", action="store_true")
    args = parser.parse_args(argv)
    result = sync(args.root, apply=args.apply, maintenance_authorized=args.maintenance_authorized)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["remaining_mismatches"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
