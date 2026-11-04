"""Owned stdio/native-journal fixtures for the sequential managed controller.

The pinned fixture executable is Python. No test creates a Codex chat, changes
a live Goal, starts inference or confers native/domain qualification.
"""
from __future__ import annotations

import contextlib
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.atomic import atomic_write_json
from agentinfra.roadmap_codex import bind_goal
from agentinfra.roadmap_lease import WorkspaceLease
from agentinfra.roadmap_managed import ManagedTurnRunner
from agentinfra.roadmap_native_adapter import NativeGoalAdapter
from agentinfra.roadmap_native import process_handle
from agentinfra.roadmap_project import ProjectAdapter
from agentinfra.roadmap_protocol import REQUIRED_SCHEMAS, export_manifest
from agentinfra.roadmap_records import ContractError, digest, file_binding, read_json
from agentinfra.roadmap_runtime import BudgetLedger
from agentinfra.transaction import FileTransaction, Mutation
from agentinfra.roadmap_records import canonical


SERVER = r'''
import json,os,sys
from pathlib import Path
root=Path.cwd(); state_path=root/'native-state.json'; journal=root/'native.jsonl'
def save(s): state_path.write_text(json.dumps(s))
def event(kind,payload):
    with journal.open('a') as f: f.write(json.dumps({'type':kind,'payload':payload})+'\n')
def context(s,ident):
    event('turn_context',{'turn_id':ident,'model':s.get('effective_model','M'),'effort':s.get('effective_effort','max'),
          'cwd':str(root),'collaboration_mode':{'mode':s.get('effective_mode','default')}})
def thread(s):
    return {'id':'T','cwd':str(root),'path':str(journal),'model':s.get('effective_model','M'),
            'reasoningEffort':s.get('effective_effort','max'),'status':{'type':'notLoaded'}}
def send(x): print(json.dumps(x),flush=True)
for line in sys.stdin:
    m=json.loads(line)
    if 'id' not in m: continue
    s=json.loads(state_path.read_text()); method=m['method']; p=m['params']
    s['traffic'].append({'method':method,'params':p,'pid':os.getpid()});save(s)
    result={}
    if method=='initialize': pass
    elif method=='model/list':
        result={'data':[{'model':'M','id':'M','supportedReasoningEfforts':[{'reasoningEffort':s.get('catalog_effort','max')}]}],'nextCursor':None}
    elif method=='thread/goal/get': result={'goal':s['goal']}
    elif method=='thread/read': result={'thread':thread(s)}
    elif method=='thread/turns/list': result={'data':s['turns'],'nextCursor':None}
    elif method=='thread/resume':
        result={'thread':thread(s),'cwd':str(root),'model':s.get('accepted_model','M'),'modelProvider':'fixture',
          'reasoningEffort':s.get('accepted_effort','max'),'approvalPolicy':'never','approvalsReviewer':'user','sandbox':{'type':'readOnly'},
          'collaborationMode':{'mode':s.get('accepted_mode','default'),'settings':{'model':s.get('accepted_model','M'),
              'reasoning_effort':s.get('accepted_effort','max'),'developer_instructions':None}}}
    elif method=='turn/start':
        r=json.loads((root/'.aegis/project.json').read_text()); t=r['execution']['managed_turn']
        a=next(a for a in json.loads((root/'.aegis/roadmaps/reservations.json').read_text())['attempts'] if a['id']==t['attempt'])
        assert a['status']=='RESERVED' and a['operation']['start_sent'] and a['operation']['child']['pid']==os.getpid()
        assert p['model']=='M' and p['effort']=='max' and p['collaborationMode']['settings']['reasoning_effort']=='max'
        if s.get('reject_start'):
            send({'id':m['id'],'error':{'code':-32602,'message':'token=fixture-sensitive-value'}});continue
        ident='N'+str(len(s['turns'])); s['current']=ident
        turn={'id':ident,'status':'inProgress','items':[],'error':None};s['turns'].insert(0,turn)
        s['goal']['tokensUsed']+=10; context(s,ident); event('event_msg',{'type':'task_started','turn_id':ident});save(s)
        if s.get('drop_start'): break
        send({'id':m['id'],'result':{'turn':turn}})
        send({'method':'turn/started','params':{'threadId':'T','turn':turn}})
        if s.get('usage'):
            usage={'method':'thread/tokenUsage/updated','params':{'threadId':'T','turnId':ident,'tokenUsage':{'total':
                {'inputTokens':100,'cachedInputTokens':20,'outputTokens':50,'reasoningOutputTokens':10,'totalTokens':150}}}}
            send(usage);send(usage)
        if s.get('reroute'):
            send({'method':'model/rerouted','params':{'threadId':'T','turnId':ident,'fromModel':'M','toModel':'other','reason':'highRiskCyberActivity'}})
            event('event_msg',{'type':'model_rerouted','turn_id':ident,'from_model':'M','to_model':'other'})
        if s.get('scope_drift'):
            send({'method':'turn/plan/updated','params':{'threadId':'T','turnId':ident,'plan':[{'step':'A14 begin modernization','status':'inProgress'}]}})
        if s.get('approval'):
            send({'id':'approval-1','method':'item/commandExecution/requestApproval','params':{'threadId':'T','turnId':ident,'command':'private fixture body'}})
        if s.get('complete'):
            s['turns'][0]['status']='completed';save(s);event('event_msg',{'type':'task_complete','turn_id':ident})
            send({'method':'turn/completed','params':{'threadId':'T','turn':s['turns'][0]}})
        continue
    elif method=='turn/steer':
        assert p['expectedTurnId']==s['current']
        if s.get('steer_unknown'):
            print('{malformed}',flush=True);continue
        result={'turnId':s['current']}
    elif method=='turn/interrupt':
        assert p['turnId']==s['current']
        if not s.get('ack_only'):
            s['turns'][0]['status']='interrupted';save(s);event('event_msg',{'type':'turn_aborted','turn_id':s['current']})
            send({'method':'turn/completed','params':{'threadId':'T','turn':s['turns'][0]}})
    else:
        send({'id':m['id'],'error':{'code':-32601,'message':'fixture refuses unknown method'}});continue
    send({'id':m['id'],'result':result})
'''


class ManagedTurnTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name)
        shared = self.root/'Roadmaps/Shared';shared.mkdir(parents=True)
        for name in ['registry.json','records.schema.json']: shutil.copyfile(ROOT/'Roadmaps/Shared'/name,shared/name)
        (self.root/'framework.toml').write_text('fixture = true\n')
        (self.root/'infra/agentinfra').mkdir(parents=True);(self.root/'infra/agentinfra/fixture.py').write_text('VALUE = 1\n')
        self.exe={'path':str(Path(sys.executable).resolve()),'sha256':digest(Path(sys.executable).read_bytes())}
        export=self.root/'export/v2';export.mkdir(parents=True)
        params={'ThreadResume':['threadId','excludeTurns'],'TurnStart':['threadId','input','clientUserMessageId','model','effort','collaborationMode','parentTurnId'],
                'TurnSteer':['threadId','expectedTurnId','input','clientUserMessageId'],'TurnInterrupt':['threadId','turnId'],
                'ThreadGoalGet':['threadId'],'ThreadRead':['threadId','includeTurns'],'ThreadTurnsList':['threadId','itemsView','limit','sortDirection','cursor'],
                'ModelList':['limit','cursor']}
        responses={'ThreadResume':['thread','cwd','model','modelProvider','approvalPolicy','approvalsReviewer','sandbox'],
                   'TurnStart':['turn'],'TurnSteer':['turnId'],'ThreadGoalGet':['goal'],'ThreadRead':['thread'],
                   'ThreadTurnsList':['data'],'ModelList':['data']}
        for name in REQUIRED_SCHEMAS:
            stem=name.removesuffix('.json');value={'type':'object','properties':{},'required':[]}
            if stem.endswith('Params'):
                prefix=stem.removesuffix('Params');value['properties']={k:{} for k in params.get(prefix,[])}
                if prefix!='ModelList' and prefix in params: value['required']=['threadId']
            if stem.endswith('Response'):value['required']=responses.get(stem.removesuffix('Response'),[])
            if stem in ['ThreadTurnsListResponse','ThreadItemsListResponse']:
                value['definitions']={'Turn':{'type':'object'},'ThreadItem':{'oneOf':[]}}
            atomic_write_json(export/name,value,root=self.root)
        with patch('agentinfra.roadmap_protocol.native_executable',return_value=self.exe):
            self.protocol=export_manifest(self.root,'export',self.exe)
        atomic_write_json(self.root/'protocol.json',self.protocol,root=self.root)
        (self.root/'app-server').write_text(SERVER)
        self.owner=WorkspaceLease(self.root).acquire('T','managed turn fixture')
        self.owner.update(process_handle(os.getpid()))
        lease=WorkspaceLease(self.root);state=lease.read();state['active']=self.owner;atomic_write_json(lease.path,state,root=self.root)
        parent=dict(self.owner,pid=99999999,process_identity='proc-start:0')
        self.goal={'threadId':'T','objective':'whole objective','status':'active','createdAt':1,'tokensUsed':100,'timeUsedSeconds':10,'tokenBudget':None}
        binding=bind_goal(self.goal,thread_id='T',objective=self.goal['objective'],contract_hash='c'*64)
        self.adapter=ProjectAdapter(self.root);self.adapter.update({'execution':{'workspace_lease':self.owner,'native_binding':binding,
            'native_turn_configuration':{'model':'M','effort':'max','mode':'default'},'scope':['A04'],'integration_path':'managed_app_server',
            'managed_runner':{'runner':process_handle(os.getpid()),'server':None,'authorization_id':'adoption','adoption':{'parent':parent},'protocol_digest':self.protocol['digest'],
                              'state_home':str(Path(os.environ.get('CODEX_HOME') or Path.home()/'.codex').resolve())}},
            'continuation':{'milestone':'A04'},'native_protocol':file_binding(self.root,'protocol.json')},expected_digest=None,allow_create=True)
        self.compiled={'digest':'c'*64,'inputs':[file_binding(self.root,'Roadmaps/Shared/records.schema.json')],
            'milestones':{'A04':{'dependencies':[],'implementation_units':['native controller'],'budget_policy':{'max_seconds_per_recipe':900,'max_attempts':2}}}}
        self.state_path=self.root/'native-state.json';self.save({'goal':self.goal,'turns':[{'id':'P','status':'completed','error':None}], 'traffic':[]})
        self.journal=self.root/'native.jsonl'
        self.journal.write_text(json.dumps({'type':'session_meta','payload':{'id':'T'}})+'\n')
        self.context('P');self.event('event_msg',{'type':'task_complete','turn_id':'P'})
        self.runner=ManagedTurnRunner(self.root,self.protocol)

    def tearDown(self):
        if self.runner.client is not None:self.runner.close()
        self.temp.cleanup()

    def save(self,s): self.state_path.write_text(json.dumps(s))
    def state(self): return read_json(self.state_path)
    def event(self,kind,payload):
        with self.journal.open('a') as f:f.write(json.dumps({'type':kind,'payload':payload})+'\n')
    def context(self,ident,effort='max'):
        self.event('turn_context',{'turn_id':ident,'model':'M','effort':effort,'cwd':str(self.root),'collaboration_mode':{'mode':'default'}})
    def fixture(self):
        stack=contextlib.ExitStack();stack.enter_context(contextlib.chdir(self.root))
        stack.enter_context(patch('agentinfra.roadmap_protocol.native_executable',return_value=self.exe))
        stack.enter_context(patch('agentinfra.roadmap_managed.compile_roadmaps',return_value=self.compiled))
        stack.enter_context(patch('agentinfra.roadmap_managed.audit_evidence',return_value={'milestones':{'A04':{'state':'READY'}}}))
        return stack
    def configure(self,**fields): s=self.state();s.update(fields);self.save(s)
    def start(self,role='executor',authorization='user-work'):
        spec=self.runner.prepare('perform owned native fixture work',role=role,authorization_id=authorization)
        return self.runner.start(spec,user_authorized=True)
    def observe(self,result):
        for _ in range(4):
            if result['state'] in ['SUCCESS','FAILED','INTERRUPTED']:return result
            result=self.runner.poll(0.1)
        return result

    def test_real_stdio_turn_is_reserved_before_dispatch_and_terminal_native_evidence_closes_it(self):
        self.configure(complete=True)
        with self.fixture(): result=self.observe(self.start())
        self.assertEqual(result['state'],'SUCCESS')
        a=BudgetLedger(self.root).read()['attempts'][0];self.assertEqual(a['operation']['turn_id'],'N1')
        self.assertEqual(a['operation']['child']['pid'],next(x['pid'] for x in self.state()['traffic'] if x['method']=='turn/start'))
        self.assertEqual(a['status'],'SUCCESS');self.assertEqual(len(self.adapter.read()['work_units']),1)
        self.assertTrue(a['operation']['effective_configuration']['confirmed'])
        self.assertFalse(a['receipt']['domain_proof'])

    def test_sequential_specialist_and_reviewer_reuse_one_owned_server_and_max_policy(self):
        self.configure(complete=True)
        with self.fixture():
            self.assertEqual(self.observe(self.start('specialist','specialist-work'))['state'],'SUCCESS')
            self.assertEqual(self.observe(self.start('reviewer','review-work'))['state'],'SUCCESS')
        requests=[x for x in self.state()['traffic'] if x['method']=='turn/start']
        self.assertEqual(len(requests),2);self.assertEqual(requests[0]['pid'],requests[1]['pid'])
        self.assertEqual(requests[0]['params']['parentTurnId'],'P');self.assertEqual(requests[1]['params']['parentTurnId'],'N1')
        self.assertTrue(all(x['params']['model']=='M' and x['params']['effort']=='max' for x in requests))

    def test_active_native_handle_blocks_another_turn_and_keeps_original_reservation(self):
        with self.fixture():
            self.assertEqual(self.start()['state'],'RUNNING')
            with self.assertRaisesRegex(ContractError,'requires observation'):
                self.start(authorization='second-work')
        self.assertEqual(len([x for x in self.state()['traffic'] if x['method']=='turn/start']),1)
        self.assertEqual(BudgetLedger(self.root).read()['attempts'][0]['status'],'RESERVED')

    def test_steering_targets_same_turn_and_duplicate_authorization_never_resends(self):
        with self.fixture():
            self.start();control=self.runner.steer('focus on the owned input',user_authorized=True,authorization_id='steer-1')
            self.assertEqual(control['state'],'ACKNOWLEDGED')
            with self.assertRaisesRegex(ContractError,'already attempted'):
                self.runner.steer('focus on the owned input',user_authorized=True,authorization_id='steer-1')
        requests=[x for x in self.state()['traffic'] if x['method']=='turn/steer'];self.assertEqual(len(requests),1)
        self.assertEqual(requests[0]['params']['expectedTurnId'],'N1')

    def test_interrupt_ack_is_not_termination_and_delayed_native_end_is_required(self):
        self.configure(ack_only=True)
        with self.fixture():
            self.start();self.runner.interrupt(user_authorized=True,authorization_id='stop-1')
            self.assertEqual(self.runner.recover()['state'],'RUNNING')
            self.assertEqual(BudgetLedger(self.root).read()['attempts'][0]['status'],'RESERVED')
            s=self.state();s['turns'][0]['status']='interrupted';self.save(s);self.event('event_msg',{'type':'turn_aborted','turn_id':'N1'})
            self.assertEqual(self.runner.recover()['state'],'INTERRUPTED')

    def test_actual_native_interruption_remains_distinct_from_success(self):
        with self.fixture():
            self.start();self.runner.interrupt(user_authorized=True,authorization_id='stop-1');result=self.runner.recover()
        self.assertEqual(result['state'],'INTERRUPTED');self.assertEqual(result['native_status'],'interrupted')

    def test_dropped_start_response_and_local_exit_do_not_prove_native_termination(self):
        self.configure(drop_start=True)
        with self.fixture():
            result=self.start();self.runner.close()
            self.assertEqual(result['state'],'UNKNOWN')
            self.assertEqual(self.runner.recover()['state'],'UNKNOWN')
            with self.assertRaisesRegex(ContractError,'requires observation'):self.start(authorization='new-work')
        self.assertEqual(BudgetLedger(self.root).read()['attempts'][0]['status'],'RESERVED')

    def test_observed_effort_downgrade_cannot_pass_native_turn(self):
        with self.fixture():
            self.assertEqual(self.start()['state'],'RUNNING')
            s=self.state();s['turns'][0]['status']='completed';s['effective_effort']='medium';self.save(s)
            self.context('N1',effort='medium');self.event('event_msg',{'type':'task_complete','turn_id':'N1'})
            result=self.runner.recover()
        self.assertEqual(result['state'],'FAILED')

    def test_unaccepted_model_or_plan_mode_refuses_model_dispatch(self):
        self.configure(accepted_mode='plan')
        with self.fixture():result=self.start()
        self.assertEqual(result['state'],'FAILED');self.assertFalse(any(x['method']=='turn/start' for x in self.state()['traffic']))

    def test_surfaced_rerouting_and_out_of_scope_plan_do_not_receive_success(self):
        self.configure(complete=True,reroute=True,scope_drift=True)
        with self.fixture():result=self.observe(self.start())
        self.assertEqual(result['state'],'FAILED')
        operation=BudgetLedger(self.root).read()['attempts'][0]['operation']
        self.assertIn('NATIVE_PLAN_SCOPE_DRIFT',operation['event_projection']['blockers'])
        self.assertIn('MODEL_REROUTED_OR_UNEXPECTED_SOURCE',operation['event_projection']['blockers'])

    def test_native_usage_duplicate_snapshots_are_not_added_to_goal_or_session_totals(self):
        self.configure(complete=True,usage=True)
        with self.fixture():self.assertEqual(self.observe(self.start())['state'],'SUCCESS')
        usage=BudgetLedger(self.root).read()['usage']
        self.assertEqual(usage['native-session:T']['totals']['total_tokens'],150)
        self.assertEqual(usage['T']['total'],110)

    def test_user_action_request_is_retained_without_copying_private_command_body(self):
        self.configure(approval=True)
        with self.fixture():result=self.start()
        self.assertEqual(result['state'],'AWAITING_USER_ACTION')
        self.assertNotIn('private fixture body',json.dumps(BudgetLedger(self.root).read()))
        self.assertEqual(result['required_user_action'][0]['id'],'approval-1')

    def test_rejected_start_closes_failed_with_native_error_code_and_no_token_reset(self):
        self.configure(reject_start=True)
        with self.fixture():result=self.start()
        self.assertEqual(result['state'],'FAILED');self.assertEqual(self.state()['goal']['tokensUsed'],100)
        a=BudgetLedger(self.root).read()['attempts'][0];self.assertEqual(a['operation']['start_error']['code'],-32602)
        self.assertNotIn('fixture-sensitive-value',json.dumps(a))

    def test_unknown_steering_does_not_redispatch_and_completed_output_is_not_credited(self):
        self.configure(steer_unknown=True)
        with self.fixture():
            self.start();self.assertEqual(self.runner.steer('new input',user_authorized=True,authorization_id='unknown-steer')['state'],'UNKNOWN')
            with self.assertRaisesRegex(ContractError,'already attempted'):
                self.runner.steer('new input',user_authorized=True,authorization_id='unknown-steer')
            s=self.state();s['turns'][0]['status']='completed';self.save(s);self.event('event_msg',{'type':'task_complete','turn_id':'N1'})
            self.assertEqual(self.runner.recover()['state'],'FAILED')

    def test_source_change_between_prepare_and_dispatch_refuses_reservation(self):
        with self.fixture():
            spec=self.runner.prepare('work',role='executor',authorization_id='user-input')
            (self.root/'infra/agentinfra/fixture.py').write_text('VALUE = 2\n')
            with self.assertRaisesRegex(ContractError,'changed before dispatch'):self.runner.start(spec,user_authorized=True)
        self.assertEqual(BudgetLedger(self.root).read()['attempts'],[])

    def test_native_state_routing_change_cannot_start_another_connection(self):
        with self.fixture():
            spec=self.runner.prepare('work',role='executor',authorization_id='user-input')
            with patch.dict(os.environ,{'CODEX_HOME':str(self.root/'different-native-state')}):
                with self.assertRaisesRegex(ContractError,'state routing changed'):self.runner.start(spec,user_authorized=True)
        self.assertEqual(BudgetLedger(self.root).read()['attempts'],[])

    def test_native_pause_and_unapproved_work_refuse_new_dispatch(self):
        s=self.state();s['goal']['status']='paused';self.save(s)
        with self.fixture():
            spec=self.runner.prepare('work',role='reviewer',authorization_id='user-input')
            with self.assertRaises(ContractError):self.runner.start(spec,user_authorized=False)
            with self.assertRaisesRegex(ContractError,'active parent or unqualified'):self.runner.start(spec,user_authorized=True)
        self.assertEqual(BudgetLedger(self.root).read()['attempts'],[])

    def test_actual_active_parent_process_cannot_be_adopted(self):
        with self.fixture():
            with self.assertRaisesRegex(ContractError,'parent process prohibits'):
                self.adapter.adopt_managed_runner(self.protocol,user_authorized=True,authorization_id='adopt')
        self.assertEqual(WorkspaceLease(self.root).read()['active'],self.owner)

    def retired_driver(self):
        atomic_write_json(self.root/'fixture-compiled.json',self.compiled,root=self.root)
        code=r'''
import json,os,sys
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,sys.argv[1])
from agentinfra.atomic import atomic_write_json
from agentinfra.roadmap_native import process_handle
from agentinfra.roadmap_managed import ManagedTurnRunner
from agentinfra.roadmap_records import read_json
from agentinfra.roadmap_records import canonical,digest
from agentinfra.transaction import FileTransaction,Mutation
root=Path.cwd(); p=read_json(root/'.aegis/project.json'); lease=read_json(root/'.aegis/coordination/lease.json')
before=(root/'.aegis/project.json').read_bytes();lease_before=(root/'.aegis/coordination/lease.json').read_bytes()
# Seed this owned fixture with the actual short-lived driver process.
owner=dict(p['execution']['workspace_lease'],**process_handle(os.getpid()))
p['execution']['workspace_lease']=owner;p['execution']['managed_runner']['runner']=process_handle(os.getpid());lease['active']=owner
FileTransaction(root,[Mutation(root/'.aegis/project.json',canonical(p)+b'\n',expected_exists=True,expected_sha256=digest(before)),
 Mutation(root/'.aegis/coordination/lease.json',canonical(lease)+b'\n',expected_exists=True,expected_sha256=digest(lease_before))],
 state_dir=root/'.aegis/state/transactions',name='aegis-authority-inventory').commit()
protocol=read_json(root/'protocol.json');compiled=read_json(root/'fixture-compiled.json')
with patch('agentinfra.roadmap_protocol.native_executable',return_value=protocol['executable']),patch('agentinfra.roadmap_managed.compile_roadmaps',return_value=compiled),patch('agentinfra.roadmap_managed.audit_evidence',return_value={'milestones':{'A04':{'state':'READY'}}}):
 r=ManagedTurnRunner(root,protocol);s=r.prepare('owned work',role='executor',authorization_id='retired-driver')
 print(json.dumps(r.start(s,user_authorized=True)));r.close()
'''
        process=subprocess.run([sys.executable,'-B','-c',code,str(ROOT/'infra')],cwd=self.root,capture_output=True,text=True,timeout=20)
        self.assertEqual(process.returncode,0,process.stderr)
        return json.loads(process.stdout)

    def test_retired_real_driver_stays_unknown_until_original_native_turn_ends(self):
        result=self.retired_driver();self.assertEqual(result['state'],'RUNNING')
        with self.fixture():
            self.assertEqual(self.runner.recover()['state'],'UNKNOWN')
            self.assertEqual(BudgetLedger(self.root).read()['attempts'][0]['status'],'RESERVED')
            s=self.state();s['turns'][0]['status']='completed';self.save(s);self.event('event_msg',{'type':'task_complete','turn_id':'N1'})
            recovered=self.runner.recover()
        self.assertEqual(recovered['state'],'SUCCESS');self.assertTrue(recovered['retired_owner_reconciled'])
        self.assertEqual(len([t for t in self.state()['traffic'] if t['method']=='turn/start']),1)
        self.assertNotEqual(self.adapter.read()['execution']['workspace_lease']['pid'],os.getpid())

    def test_explicit_adoption_after_retirement_preserves_pause_and_fences_same_goal(self):
        self.retired_driver();s=self.state();s['turns'][0]['status']='completed';self.save(s);self.event('event_msg',{'type':'task_complete','turn_id':'N1'})
        with self.fixture():
            self.runner.recover()
            with self.assertRaisesRegex(ContractError,'auto-continuing'):self.adapter.adopt_managed_runner(self.protocol,user_authorized=True,authorization_id='adopt')
            s=self.state();s['goal']['status']='paused';self.save(s)
            adopted=self.adapter.adopt_managed_runner(self.protocol,user_authorized=True,authorization_id='adopt')
        self.assertEqual(adopted['owner']['pid'],os.getpid());self.assertEqual(adopted['owner']['fence'],2)
        p=self.adapter.read();self.assertEqual(p['execution']['native_binding']['observation']['status'],'paused')
        self.assertEqual(p['execution']['native_binding']['observation']['createdAt'],1)
        self.assertEqual(p['execution']['native_binding']['observation']['tokensUsed'],110)
        self.assertEqual(p['execution']['native_binding']['objective'],'whole objective')
        self.assertEqual(len([t for t in self.state()['traffic'] if t['method']=='turn/start']),1)

    def completed_retired_driver(self):
        self.retired_driver();s=self.state();s['turns'][0]['status']='completed';self.save(s)
        self.event('event_msg',{'type':'task_complete','turn_id':'N1'})
        return self.runner.recover()

    def test_retired_goal_control_recovery_repairs_projection_without_transferring_owner(self):
        with self.fixture():
            self.assertEqual(self.completed_retired_driver()['state'],'SUCCESS')
            record=self.adapter.read();owner=record['execution']['workspace_lease'];before=self.adapter.profile.path().read_bytes()
            prepared={'schema':1,'action':'pause','binding':record['execution']['native_binding'],'owner':owner,'contract_digest':'c'*64,
                      'request':{'method':'thread/goal/set','params':{'threadId':'T','origin':'user','status':'paused'}}}
            prepared['digest']=digest(prepared);path=self.root/'.aegis/fixture-control-preparation.json';atomic_write_json(path,prepared,root=self.root)
            binding=file_binding(self.root,'.aegis/fixture-control-preparation.json')
            operation={'state':'PREPARED','kind':'native_lifecycle_control','spec_digest':prepared['digest'],'runner':owner,'owner':owner,
                       'child':None,'native_thread':'T','authorization_id':'old-user-pause','preparation':binding,'transport':'explicit_host_lifecycle_callback'}
            attempt=BudgetLedger(self.root).reserve_control('old-pause',prepared['digest'],30,operation,user_authorized=True)
            record['execution']['native_transition']={'state':'UNKNOWN','attempt':attempt['id'],'preparation':binding}
            FileTransaction(self.root,[Mutation(self.adapter.profile.path(),canonical(record)+b'\n',expected_exists=True,expected_sha256=digest(before))],
                            state_dir=self.root/'.aegis/state/transactions',name='aegis-authority-inventory').commit()
            s=self.state();s['goal']['status']='paused';self.save(s)
            recovered=NativeGoalAdapter(self.root,self.protocol).recover()
        self.assertEqual(recovered['state'],'SUCCESS');self.assertEqual(self.adapter.read()['execution']['workspace_lease'],owner)
        self.assertEqual(self.adapter.read()['execution']['native_transition']['state'],'SUCCESS')

    def test_active_host_rebind_retires_managed_route_after_real_driver_termination(self):
        with self.fixture():
            self.assertEqual(self.completed_retired_driver()['state'],'SUCCESS')
            observation={'caller_is_descendant':True,'status':'active','goal':self.state()['goal'],'model':'M','effort':'max','mode':'default'}
            with patch('agentinfra.roadmap_native.observe_native_owner',return_value=observation):
                rebound=self.adapter.rebind_native_process(os.getpid())
        p=self.adapter.read();self.assertEqual(rebound['owner']['pid'],os.getpid())
        self.assertEqual(p['execution']['integration_path'],'active_host');self.assertNotIn('managed_runner',p['execution'])
        self.assertEqual(len(p['execution']['managed_runner_history']),1)

    def test_only_verified_model_child_may_nest_deterministic_work(self):
        ledger=BudgetLedger(self.root)
        model_op={'state':'PREPARED','kind':'native_model_turn','runner':process_handle(os.getpid()),'owner':self.owner,'child':None,'spec_digest':'model'}
        parent=ledger.reserve_operation('model','model',30,model_op)
        model_op.update(state='RUNNING',child=process_handle(os.getpid()),turn_id='N1');ledger.journal(parent['id'],model_op)
        child={'state':'PREPARED','kind':'deterministic_recipe','runner':process_handle(os.getpid()),'owner':self.owner,'child':None,
               'spec_digest':'tool','parent_native_attempt':parent['id']}
        tool=ledger.reserve_operation('tool','tool',10,child)
        self.assertEqual(len([a for a in ledger.read()['attempts'] if a['status']=='RESERVED']),2)
        ledger.close(tool['id'],'SUCCESS',{})
        with self.assertRaises(ContractError):ledger.reserve('unowned','other',10)
        invalid=dict(child,spec_digest='other',kind='native_model_turn')
        with self.assertRaises(ContractError):ledger.reserve_operation('overlap','other',10,invalid)
        ledger.close(parent['id'],'INTERRUPTED',{})


if __name__=='__main__':unittest.main()
