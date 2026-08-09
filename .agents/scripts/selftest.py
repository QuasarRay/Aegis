from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
cmd=[sys.executable,str(root/".agents"/"bin"/"agentctl.py"),"law","run"]
raise SystemExit(subprocess.call(cmd,cwd=root))
