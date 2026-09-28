"""Qualify Aegis' HOL4 acceptance adapter on a tiny theorem."""
from pathlib import Path
import json
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra"))

from agentinfra.hol4 import holmake, mcp_stdio_config


SCRIPT = r"""open HolKernel boolLib bossLib;
val _ = new_theory "AegisHol4Smoke";

Theorem identity:
  !p:bool. p ==> p
Proof
  simp[]
QED

val _ = export_theory();
"""


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="aegis-hol4-") as td:
        root = Path(td)
        (root / ".aegis").mkdir()
        theory = root / "theory"
        theory.mkdir()
        (theory / "AegisHol4SmokeScript.sml").write_text(SCRIPT)
        config = mcp_stdio_config(root)
        result = holmake(root, "theory", timeout=300)
        output = ROOT / ".aegis/hol4-qualification.json"
        output.parent.mkdir(exist_ok=True)
        output.write_text(json.dumps({
            "claim": "HOL4 adapter qualification only; not a Candle theorem",
            "mcp": config,
            "holmake": result,
        }, indent=2) + "\n")
        print(json.dumps({"status": result["status"], "claim": result["claim"]}))
        return 0 if result["status"] == "CHECKED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
