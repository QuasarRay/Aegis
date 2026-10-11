#!/usr/bin/env python3
"""Destiny utilities from a pinned Aegis source checkout."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "infra"))
from agentinfra.destiny import main

if __name__ == "__main__":
    raise SystemExit(main())
