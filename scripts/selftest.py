from pathlib import Path
import subprocess,sys
framework=Path(__file__).resolve().parents[1]
raise SystemExit(subprocess.call([sys.executable,"-B","-m","unittest","discover","-s",str(framework/"infra/tests"),"-q"]))
