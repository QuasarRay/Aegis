"""Synthetic acceptance regressions. These confer no Destiny proof credit."""
import copy
from pathlib import Path
import tempfile
import unittest

from agentinfra.destiny_reuse import digest
from agentinfra.verus_evidence import inventory, current_inventory, validate_symbol_mapping, validate_case_map

ENTRY='verification/verus/example.rs'
VIR='''(@ "verification/verus/example.rs:1:1: 1:70 (#0)" (Function
 :name (Fun :path example::transition) :owning_module example:: :mode Exec
 :attrs (FunctionAttrs :is_external_body false :exec_assume_termination false
 :exec_allows_no_decreases_clause false :is_async false)
 :body (@@ "src/transition.rs:1:1: 1:30 (#0)" (Block :body None))))
(arch_word_bits (ArchWordBits Either32Or64))
'''

class VerusInventoryTests(unittest.TestCase):
    def setUp(self):
        self.folder=tempfile.TemporaryDirectory()
        self.root=Path(self.folder.name)
        self.artifact='.aegis/destiny/verus-artifacts/run.vir'
        path=self.root/self.artifact;path.parent.mkdir(parents=True);path.write_text(VIR)
        self.actual=inventory(VIR,ENTRY)
        self.obligation={'entry':ENTRY,'expected_checks':1}
        self.command={'argv':['/pinned/verus','--crate-type=lib',ENTRY],'returncode':0,
            'stdout':'verification results:: 1 verified, 0 errors\n','stderr':'',
            'timed_out':False,'stdout_truncated':False,'stderr_truncated':False}
        self.receipt={'id':'verus','status':'OBSERVED_SUCCESS','returncode':0,'proof_output_checked':True,
            'identity':{'obligation':{'method':'verus',**self.obligation},'commands':[self.command['argv']]},
            'commands':[self.command], 'verus_inventory':{**self.actual,
                'artifact':self.artifact,'artifact_sha256':digest(path.read_bytes())}}
        self.mapping={'schema':1,'entry':ENTRY,'symbols':[{'symbol':'example::transition','mode':'Exec',
            'obligations':['derived-state'],'relation':'Changed state corresponds to the specification transition.',
            'review':'Original definition and actual shared production body reviewed.'}]}

    def tearDown(self):self.folder.cleanup()

    def test_real_body_is_not_confused_with_a_nested_body_none(self):
        value=current_inventory(self.root,self.receipt,self.obligation)
        self.assertEqual(validate_symbol_mapping(value,self.mapping),{'example::transition'})
        self.assertEqual(value['checked'][0]['body'],'src/transition.rs:1:1: 1:30 (#0)')

    def test_missing_or_unreferenced_or_unreviewed_theorem_is_rejected(self):
        for mutate in (
            lambda d:d.update(symbols=[]),
            lambda d:d['symbols'][0].update(symbol='example::unrelated'),
            lambda d:d['symbols'][0].update(obligations=[]),
            lambda d:d['symbols'][0].update(review=''),
        ):
            d=copy.deepcopy(self.mapping);mutate(d)
            with self.assertRaises(ValueError):validate_symbol_mapping(self.actual,d)

    def test_zero_wrong_count_failure_success_shaped_log_and_truncation_are_rejected(self):
        for mutate in (
            lambda r:r['commands'][0].update(stdout='verification results:: 0 verified, 0 errors\n'),
            lambda r:r['commands'][0].update(stdout='verification results:: 2 verified, 0 errors\n'),
            lambda r:r['commands'][0].update(returncode=1),
            lambda r:r['commands'][0].update(stdout='verification results:: 1 verified, 1 errors\n'),
            lambda r:r['commands'][0].update(stdout_truncated=True),
            lambda r:r['commands'][0].update(timed_out=True),
        ):
            r=copy.deepcopy(self.receipt);mutate(r)
            with self.assertRaises(ValueError):current_inventory(self.root,r,self.obligation)

    def test_missing_changed_or_incomplete_inventory_is_rejected(self):
        r=copy.deepcopy(self.receipt);r['verus_inventory']=None
        with self.assertRaises(ValueError):current_inventory(self.root,r,self.obligation)
        (self.root/self.artifact).write_text(VIR.replace('transition','changed'))
        with self.assertRaises(ValueError):current_inventory(self.root,self.receipt,self.obligation)
        with self.assertRaises(ValueError):inventory(VIR.split('(arch_word_bits')[0],ENTRY)

    def test_empty_external_and_unchecked_behavior_are_rejected(self):
        for text in (VIR.replace('example::transition','other::transition'),
                     VIR.replace(':is_external_body false',':is_external_body true'),
                     VIR.replace(':exec_assume_termination false',':exec_assume_termination true')):
            with self.assertRaises(ValueError):inventory(text,ENTRY)

    def test_qualified_catalog_join_rejects_omitted_case_and_assertion(self):
        catalog=[];cases=[];mapped=[]
        for i in range(531):
            j=i if i<509 else i-509
            source=f'source{j%34}.py';test=f'test_{j}';fixture='Test' if i<509 else 'SecondFixture'
            identity=f'{source}::{fixture}::{test}'
            assertion=f'{source}:{j+1}'
            authority={'id':identity,'source':source,'test':test,'original_commit':'pin','original_source_sha256':'hash'}
            catalog.append(authority)
            case={**authority,'assertion_ids':[assertion],'dependency_ids':[]}
            cases.append(case)
            mapped.append({**case,'assertion_mappings':[{'id':assertion}], 'dependency_mappings':[],
                'execution_obligation':{'required':True,'relation':'Original setup executes.'},
                'required_obligations':['derived-state'],'concurrency_relevance':'required_concurrency_obligation',
                'applicability_rationale':'Shared state accessed by admitted callers.'})
        source_inventory={'original_commit':'pin','cases':cases}
        value={'original_commit':'pin','cases':mapped,'obligations':{'derived-state':{}}}
        self.assertEqual(len(validate_case_map(catalog,source_inventory,value)),531)
        for mutation in ('omitted','assertion','ambiguous'):
            changed=copy.deepcopy(value)
            if mutation=='omitted':changed['cases'].pop()
            elif mutation=='assertion':changed['cases'][0]['assertion_mappings']=[]
            else:changed['cases'][509]['id']=changed['cases'][0]['id']
            with self.assertRaises(ValueError):validate_case_map(catalog,source_inventory,changed)

