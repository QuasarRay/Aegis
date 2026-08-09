import tempfile,unittest,shutil
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from agentinfra.manifest import render, verify

SOURCE=Path(__file__).resolve().parents[3]

class TestManifest(unittest.TestCase):
    def test_project_extensions_do_not_invalidate_framework_manifest(self):
        with tempfile.TemporaryDirectory() as td:
            r=Path(td);shutil.copytree(SOURCE/'.agents',r/'.agents')
            (r/'.agents'/'MANIFEST.sha256').write_text(render(r))
            (r/'.agents'/'local-modules'/'x').mkdir(parents=True);(r/'.agents'/'local-modules'/'x'/'module.toml').write_text('[module]\nid="x"\n')
            (r/'.agents'/'laws'/'project').mkdir(parents=True,exist_ok=True);(r/'.agents'/'laws'/'project'/'x.toml').write_text('# local')
            (r/'.agents'/'project.md').write_text('# local')
            ok,detail=verify(r);self.assertTrue(ok,detail)
