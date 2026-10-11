"""Operational controller regressions; deductive verification is check_formal.py."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
raise SystemExit(subprocess.run(
    [sys.executable, "-B", "-m", "unittest", "discover", "-s", "infra/tests", "-q"], cwd=root
).returncode)
