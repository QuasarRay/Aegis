from pathlib import Path
import sys,json
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/"infra"))
from agentinfra.audit import audit_source
result=audit_source(root)
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["ok"] else 1)
