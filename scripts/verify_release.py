"""Read-only verification of a generated deployment artifact."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "infra"))
from agentinfra.release_source import verify_deployment_tree

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
result = verify_deployment_tree(args.destination)
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["ok"] else 1)
