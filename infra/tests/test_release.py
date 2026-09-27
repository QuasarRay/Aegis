"""Release manifests cannot authorize reads outside their artifact or hide drift."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agentinfra.release_source import verify_deployment_tree


class ReleaseManifest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = Path(__file__).resolve().parents[2]
        entries = []
        for name in ['VERSION','README.md','framework.toml','infra/pyproject.toml','modules/codex/module.toml']:
            out = self.root / '.agents' / name
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes((source / name).read_bytes())
            entries.append((name,out.read_bytes()))
        entries.sort()
        manifest = ''.join(hashlib.sha256(data).hexdigest()+'  .agents/'+name+'\n' for name,data in entries).encode()
        self.manifest = self.root / '.agents/MANIFEST.sha256'
        self.manifest.write_bytes(manifest)
        content = b''.join(n.encode()+b'\0'+str(len(d)).encode()+b'\0'+d for n,d in entries)
        self.release = {'schema':2,'version':'5.0.0','manifest_sha256':hashlib.sha256(manifest).hexdigest(),'content_sha256':hashlib.sha256(content).hexdigest()}
        self.write_release()

    def write_release(self):
        (self.root / 'RELEASE.json').write_text(json.dumps(self.release))

    def test_valid_minimal_artifact_and_content_digest(self):
        self.assertTrue(verify_deployment_tree(self.root)['ok'])
        self.release['content_sha256'] = '0'*64
        self.write_release()
        self.assertFalse(verify_deployment_tree(self.root)['ok'])

    def test_duplicate_and_parent_traversal_rejected_even_with_updated_manifest_hash(self):
        original = self.manifest.read_bytes()
        for addition in [original.splitlines(keepends=True)[0], b'0'*64+b'  .agents/../outside\n']:
            data = original + addition
            self.manifest.write_bytes(data)
            self.release['manifest_sha256'] = hashlib.sha256(data).hexdigest()
            self.write_release()
            self.assertFalse(verify_deployment_tree(self.root)['ok'])

    def test_redirected_payload_rejected(self):
        path = self.root / '.agents/VERSION'
        out = self.root / 'outside'
        shutil.move(path, out)
        path.symlink_to(out)
        self.assertFalse(verify_deployment_tree(self.root)['ok'])

    def test_extra_and_missing_files_rejected(self):
        extra = self.root / '.agents/unmanifested'
        extra.write_text('hidden input')
        self.assertFalse(verify_deployment_tree(self.root)['ok'])
        extra.unlink()
        (self.root / '.agents/VERSION').unlink()
        self.assertFalse(verify_deployment_tree(self.root)['ok'])
