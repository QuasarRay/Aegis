from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .candle import Candle
from .contracts import ContractError, authority, authority_digest, read_json, validate_plan


def main(argv=None):
    parser = argparse.ArgumentParser(description="Candle original-specification work cycles; no test-order gates")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("authority")
    validate = commands.add_parser("validate")
    validate.add_argument("plan", type=Path)
    freeze = commands.add_parser("freeze")
    freeze.add_argument("plan", type=Path)
    freeze.add_argument("--candle", type=Path, required=True)
    freeze.add_argument("--cakeml", type=Path, required=True)
    commands.add_parser("brief")
    verify = commands.add_parser("verify")
    verify.add_argument("--timeout", type=int, default=120)
    checkpoint = commands.add_parser("checkpoint")
    checkpoint.add_argument("--pr", type=int, required=True)
    commands.add_parser("audit")
    args = parser.parse_args(argv)
    try:
        app = Candle(args.root)
        if args.command == "authority":
            out = {"digest": authority_digest(), **authority()}
        elif args.command == "validate":
            out = {"task": validate_plan(read_json(args.root / args.plan))["task"], "valid": True}
        elif args.command == "freeze":
            out = app.freeze(args.plan, {"candle": args.candle, "cakeml": args.cakeml})
        elif args.command == "verify":
            out = app.verify(args.timeout)
        elif args.command == "checkpoint":
            out = app.checkpoint(args.pr)
        else:
            out = getattr(app, args.command)()
        print(json.dumps(out, sort_keys=True, separators=(",", ":")))
        if args.command == "verify" and any(x["status"] != "CHECKED" for x in out["results"]):
            return 2
        return 0
    except (ContractError, OSError, ValueError, RuntimeError, KeyError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
