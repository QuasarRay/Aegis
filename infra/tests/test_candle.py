"""Adversarial coordinator regressions; mocked tools below are not proof evidence."""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agentinfra import candle
from agentinfra.contracts import ContractError, file_digest, load_authority, validate_plan
from agentinfra.kani_report import validate_kani_report
from agentinfra.security import SecurityError
from agentinfra.transaction import FileTransaction
from agentinfra.verification import proof_manifest

FRAMEWORK = Path(__file__).resolve().parents[2]


def sample_plan():
    return json.loads((FRAMEWORK / 'templates/candle-batch.json').read_text())


class Workflow(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.plan = sample_plan()
        self.plan['scope'].append('Cargo.toml')
        for name, data in {
            '.gitignore': '.aegis/\ntarget/\n',
            'AGENTS.md': 'Canonical fixture instructions\n',
            'src/lib.rs': '// unimplemented\n',
            'src/proofs.rs': '#[kani::proof]\n#[kani::unwind(2)]\nfn variable_roundtrip() {}\n',
            'docs/adr/type-variables.md': '# Decision\nExisting generator reused.\n',
            'Cargo.toml': '[package]\nname="fixture"\nversion="0.0.0"\n',
        }.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(data)
        self.contract = load_authority(FRAMEWORK)
        for entry in self.contract['authority']['files']:
            if entry['local'].endswith('.sml'):
                out = self.root / 'spec/upstream' / Path(entry['local']).name
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(FRAMEWORK / entry['local'], out)
        self.manifest = {'kani_version':'0.68.0', 'bounded_properties':[{
            'harness':'variable_roundtrip', 'domain':'fixture only', 'unwind':2,
            'upstream':['mk_vartype_def']}]}
        (self.root / 'spec/obligations.json').write_text(json.dumps(self.manifest))
        self.git('init', '-q', '-b', 'master')
        self.git('config', 'user.name', 'Aegis fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')
        self.git('remote', 'add', 'origin', 'https://github.com/QuasarRay/Candle-rs.git')
        self.base = self.git('rev-parse', 'HEAD')
        self.git('update-ref', 'refs/remotes/origin/master', self.base)
        self.git('switch', '-qc', self.plan['branch'])

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.PIPE).decode().strip()

    def begin(self):
        return candle.begin(self.root, self.plan, FRAMEWORK)

    def verify_missing(self):
        with patch('agentinfra.candle.version', return_value={'available':False}):
            return candle.verify(self.root, FRAMEWORK)

    def prepared(self):
        self.begin()
        self.verify_missing()
        return candle.prepare_checkpoint(self.root, FRAMEWORK)

    def remote_fixture(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'checkpoint')
        head = self.git('rev-parse', 'HEAD')
        repo = {'full_name':'QuasarRay/Candle-rs'}
        response = {'state':'open', 'merged':False, 'draft':True,
                    'head':{'sha':head, 'ref':self.plan['branch'], 'repo':repo},
                    'base':{'sha':self.base, 'ref':'master', 'repo':repo}}
        actual = candle.git
        def git_with_remote(root, *args):
            if args[0] == 'ls-remote':
                return head + '\trefs/heads/' + self.plan['branch']
            return actual(root, *args)
        return response, git_with_remote

    def test_open_obligation_authorizes_implementation_without_failing_test(self):
        result = self.begin()
        self.assertFalse(result['baseline_execution_required'])
        self.assertTrue(candle.authorize_write(self.root, 'src/lib.rs', FRAMEWORK)['authorized'])
        self.assertFalse(candle.status(self.root, FRAMEWORK)['full_candle_completion'])

    def test_another_batch_requires_remote_checkpoint(self):
        self.begin()
        with self.assertRaisesRegex(ContractError, 'stacked PR'):
            self.begin()

    def test_unknown_contract_and_cost_saving_candle_deferral_rejected(self):
        bad = copy.deepcopy(self.plan)
        bad['obligations'] = ['invented::spec']
        with self.assertRaises(ContractError):
            validate_plan(bad, self.contract)
        bad = copy.deepcopy(self.plan)
        bad['reuse']['original_candle']['metaprogramming']['saves_cost'] = True
        with self.assertRaisesRegex(ContractError, 'Use Original Candle'):
            validate_plan(bad, self.contract)
        del bad['reuse']['original_candle']
        with self.assertRaises(ContractError):
            validate_plan(bad, self.contract)

    def test_protected_and_untracked_output_scope_rejected(self):
        for name in ['../out', 'target/proofs.rs', '.agents/a.py', 'spec/upstream/x', 'x/AGENTS.md']:
            with self.subTest(name=name):
                bad = copy.deepcopy(self.plan)
                bad['scope'].append(name)
                with self.assertRaises(ContractError):
                    validate_plan(bad, self.contract)

    def test_out_of_scope_changes_and_symlinks_detected(self):
        self.begin()
        (self.root / 'surprise').write_text('unplanned')
        with self.assertRaisesRegex(ContractError, 'Out-of-scope'):
            candle.authorize_write(self.root, 'src/lib.rs', FRAMEWORK)
        (self.root / 'surprise').unlink()
        (self.root / 'src/lib.rs').unlink()
        (self.root / 'src/lib.rs').symlink_to(self.root / 'Cargo.toml')
        with self.assertRaises(SecurityError):
            candle.source_snapshot(self.root)

    def test_contract_bytes_and_harness_bounds_checked(self):
        self.assertEqual(len(proof_manifest(self.root, self.plan, self.contract)['bounded_properties']), 1)
        (self.root / 'src/proofs.rs').write_text('#[kani::proof]\n#[kani::unwind(3)]\nfn variable_roundtrip() {}')
        with self.assertRaisesRegex(ContractError, 'unwind'):
            proof_manifest(self.root, self.plan, self.contract)

    def test_missing_inputs_record_open_instead_of_proof(self):
        self.begin()
        (self.root / 'src/proofs.rs').write_text('// missing')
        result = self.verify_missing()
        self.assertEqual(result['result']['status'], 'OPEN')
        self.assertTrue(result['dirty'])
        self.assertEqual(result['refinement'], 'OPEN')

    def test_budget_and_identical_failure_cache(self):
        self.plan['budget']['verifier_runs'] = 1
        self.begin()
        first = self.verify_missing()
        self.assertEqual(first['result']['status'], 'UNAVAILABLE')
        self.assertTrue(self.verify_missing()['cached'])
        (self.root / 'src/lib.rs').write_text('// next source')
        with self.assertRaisesRegex(ContractError, 'budget exhausted'):
            self.verify_missing()

    def test_raw_export_cache_tampering_rejected(self):
        self.begin()
        def fake_run(root, plan, manifest, export):
            export.write_text('{"fixture":true}')
            return {'status':'FAILED', 'report_path':export.relative_to(root).as_posix(), 'report_sha256':file_digest(export)}
        with patch('agentinfra.candle.version', return_value={'available':True}), patch('agentinfra.candle.run_kani', side_effect=fake_run):
            result = candle.verify(self.root, FRAMEWORK)
            (self.root / result['result']['report_path']).write_text('changed')
            with self.assertRaisesRegex(ContractError, 'raw verifier export changed'):
                candle.verify(self.root, FRAMEWORK)

    def test_source_mutated_by_checker_cannot_pass(self):
        self.begin()
        def mutate(*args):
            (self.root / 'src/lib.rs').write_text('// changed during verification')
            return {'status':'BOUNDED_PASS'}
        with patch('agentinfra.candle.version', return_value={'available':True}), patch('agentinfra.candle.run_kani', side_effect=mutate):
            result = candle.verify(self.root, FRAMEWORK)
        self.assertEqual(result['result']['status'], 'STALE')

    def test_attempt_charged_before_checker_crash(self):
        self.begin()
        with patch('agentinfra.candle.version', return_value={'available':True}), patch('agentinfra.candle.run_kani', side_effect=RuntimeError('checker crash')):
            result = candle.verify(self.root, FRAMEWORK)
            self.assertEqual(result['result']['status'], 'FAILED')
        self.assertEqual(len(candle.read_state(self.root)['active']['attempts']), 1)

    def test_missing_manifest_is_persisted_as_open(self):
        self.begin()
        (self.root / 'spec/obligations.json').unlink()
        self.assertEqual(self.verify_missing()['result']['status'], 'OPEN')

    def test_interrupted_process_can_checkpoint_without_forging_a_result(self):
        self.begin()
        with patch('agentinfra.candle.version', return_value={'available':True}), patch('agentinfra.candle.run_kani', side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                candle.verify(self.root, FRAMEWORK)
        result = candle.prepare_checkpoint(self.root, FRAMEWORK)
        self.assertEqual(result['results'][0]['status'], 'INTERRUPTED')

    def test_packet_preserves_evidence_and_freezes_implementation(self):
        result = self.prepared()
        directory = self.root / result['directory']
        self.assertTrue((directory / 'summary.json').is_file())
        self.assertEqual((directory / 'AGENTS.md').read_bytes(), (self.root / 'AGENTS.md').read_bytes())
        self.assertEqual(len(list(directory.glob('*.json'))), 2)
        with self.assertRaisesRegex(ContractError, 'frozen'):
            candle.authorize_write(self.root, 'src/lib.rs', FRAMEWORK)
        with self.assertRaisesRegex(ContractError, 'frozen'):
            candle.verify(self.root, FRAMEWORK)

    def test_packet_write_failure_rolls_back_and_allows_retry(self):
        self.begin()
        self.verify_missing()
        def fault(stage, journal):
            if stage == 'after_destination':
                raise OSError('injected packet failure')
        def failing_transaction(*args, **kwargs):
            return FileTransaction(*args, **kwargs, fault=fault)
        with patch('agentinfra.candle.FileTransaction', side_effect=failing_transaction):
            with self.assertRaisesRegex(OSError, 'injected packet failure'):
                candle.prepare_checkpoint(self.root, FRAMEWORK)
        self.assertNotIn('packet', candle.read_state(self.root)['active'])
        candle.prepare_checkpoint(self.root, FRAMEWORK)
        self.assertIn('packet', candle.read_state(self.root)['active'])

    def test_missing_architecture_record_cannot_create_partial_packet(self):
        self.begin()
        self.verify_missing()
        (self.root / self.plan['architecture_record']).unlink()
        with self.assertRaises((ContractError, SecurityError)):
            candle.prepare_checkpoint(self.root, FRAMEWORK)
        self.assertFalse((self.root / 'supervision').exists())

    def test_remote_mismatch_rejected_and_exact_draft_checkpoint_unlocks_next_batch(self):
        self.prepared()
        response, git_with_remote = self.remote_fixture()
        response['draft'] = False
        with patch('agentinfra.candle.github_pr', return_value=response), patch('agentinfra.candle.git', side_effect=git_with_remote):
            with self.assertRaisesRegex(ContractError, 'expected open draft'):
                candle.checkpoint(self.root, 'https://github.com/QuasarRay/Candle-rs/pull/1', FRAMEWORK)
            response['draft'] = True
            result = candle.checkpoint(self.root, 'https://github.com/QuasarRay/Candle-rs/pull/1', FRAMEWORK)
        self.assertEqual(result['refinement'], 'OPEN')
        self.assertIsNone(candle.read_state(self.root)['active'])
        self.git('update-ref', 'refs/remotes/origin/' + self.plan['branch'], result['head'])
        self.plan['base_branch'] = self.plan['branch']
        self.plan['branch'] = 'codex/next'
        self.plan['id'] = 'next'
        self.git('switch', '-qc', 'codex/next')
        self.begin()

    def test_post_packet_implementation_change_is_rejected(self):
        self.prepared()
        (self.root / 'src/lib.rs').write_text('// drift')
        self.git('add', '.')
        self.git('commit', '-qm', 'drift')
        with self.assertRaisesRegex(ContractError, 'changed after checkpoint'):
            candle.checkpoint(self.root, 'https://github.com/QuasarRay/Candle-rs/pull/1', FRAMEWORK)

    def test_corrupt_state_is_rejected(self):
        self.begin()
        path = self.root / '.aegis/candle/state.json'
        state = json.loads(path.read_text())
        state['active']['phase'] = 'COMPLETE'
        path.write_text(json.dumps(state))
        with self.assertRaisesRegex(ContractError, 'integrity'):
            candle.read_state(self.root)


class ReportInventory(unittest.TestCase):
    def test_omitted_duplicate_unreachable_and_failed_assertions_fail(self):
        manifest = {'kani_version':'0.68.0', 'bounded_properties':[{'harness':'x'}]}
        report = {'metadata':{'kani_version':'0.68.0'}, 'harness_metadata':[{
            'pretty_name':'proofs::x', 'attributes':{'kind':'Proof','should_panic':False}}],
            'verification_results':{'summary':{'total_harnesses':1,'executed':1,'status':'completed','successful':1,'failed':0},
             'results':[{'harness_id':'proofs::x','status':'Success','duration_ms':1,
             'checks':[{'category':'assertion','function':'proofs::x','status':'Success'}]}]}}
        self.assertTrue(validate_kani_report(report, manifest)['passed'])
        for mutation in ['omitted','duplicate','unreachable','failed','version']:
            bad = copy.deepcopy(report)
            results = bad['verification_results']['results']
            if mutation == 'omitted': results.clear()
            elif mutation == 'duplicate': results.append(copy.deepcopy(results[0]))
            elif mutation == 'version': bad['metadata']['kani_version'] = 'unqualified'
            else: results[0]['checks'][0]['status'] = 'Unreachable' if mutation == 'unreachable' else 'Failure'
            with self.subTest(mutation=mutation):
                self.assertFalse(validate_kani_report(bad, manifest)['passed'])
