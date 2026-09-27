"""Small specification-driven CLI; legacy TDD commands are intentionally absent."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from . import candle
from .contracts import load_authority
from .paths import framework_dir, find_root


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("doctor", "audit", "selftest", "status", "spec", "verify", "prepare-checkpoint"):
        commands.add_parser(name)
    begin = commands.add_parser("begin")
    begin.add_argument("plan", type=Path)
    write = commands.add_parser("authorize-write")
    write.add_argument("path")
    checkpoint = commands.add_parser("checkpoint")
    checkpoint.add_argument("--pr", required=True)
    package = commands.add_parser("package")
    package.add_argument("destination", type=Path)
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve(strict=True) if args.root else find_root()
        framework = framework_dir(root)
        if args.command in {"doctor", "audit"}:
            from .audit import audit_source
            result = audit_source(framework)
        elif args.command == "selftest":
            import subprocess
            return subprocess.call([sys.executable, "-B", "-m", "unittest", "discover", "-s",
                                    str(framework / "infra/tests"), "-q"], cwd=root)
        elif args.command == "spec":
            result = load_authority(framework)
        elif args.command == "begin":
            result = candle.begin(root, json.loads(args.plan.read_text()), framework)
        elif args.command == "authorize-write":
            result = candle.authorize_write(root, args.path, framework)
        elif args.command == "verify":
            result = candle.verify(root, framework)
        elif args.command == "prepare-checkpoint":
            result = candle.prepare_checkpoint(root, framework)
        elif args.command == "checkpoint":
            result = candle.checkpoint(root, args.pr, framework)
        elif args.command == "status":
            result = candle.status(root, framework)
        else:
            from .release_source import build_deployment_tree
            result = build_deployment_tree(framework, args.destination)
        print(json.dumps(result, indent=2))
        if args.command == "verify":
            return 0 if result["result"]["status"] == "BOUNDED_PASS" else 1
        return 0 if result.get("ok", True) else 1
    except (OSError, ValueError, RuntimeError, KeyError, TypeError) as error:
        print(json.dumps({"ok": False, "error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
