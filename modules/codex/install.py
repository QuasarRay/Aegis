from pathlib import Path
import sys
FRAMEWORK=Path(__file__).resolve().parents[2]
ROOT=FRAMEWORK.parent if FRAMEWORK.name==".agents" else FRAMEWORK
sys.path.insert(0,str(FRAMEWORK/"infra"))
from agentinfra.codex_config import install, ConfigError
apply="--apply" in sys.argv
try:
    print(install(ROOT,dry_run=not apply))
except ConfigError as e:
    print(f"error: {e}",file=sys.stderr);raise SystemExit(2)
