import json, os, shutil, subprocess, tempfile, unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from agentinfra.state_store import StateStore
from agentinfra.state_machine import TransitionError
from agentinfra.evidence import _append_verified_observation, append_evidence, load_evidence, rollback_last_evidence
from agentinfra.workspace import workspace_fingerprint

class TestState(unittest.TestCase):
    def setUp(self):
        self.td=tempfile.TemporaryDirectory();self.root=Path(self.td.name);(self.root/".agents"/"runtime").mkdir(parents=True)
        self.s=StateStore(self.root)
    def tearDown(self):self.td.cleanup()
    def _precheck(self):
        self.s.transition("PRECHECK","start")
        for k in ["instructions_discovered","project_overlay_checked","acceptance_defined","workspace_inspected"]:
            self.s.mutate(lambda t,k=k:t["precheck"].__setitem__(k,True))
        self.s.mutate(lambda t:t["precheck"].__setitem__("workspace_snapshot",workspace_fingerprint(self.root)))
        return self.s.transition("TRIAGE","ready")
    def test_precheck_fails_closed(self):
        self.s.create("x",mode="write");self.s.transition("PRECHECK","start")
        with self.assertRaises(TransitionError):self.s.transition("TRIAGE","too soon")
    def test_valid_precheck(self):
        self.s.create("x",mode="write");self._precheck();self.assertEqual(self.s.load()["state"],"TRIAGE")
    def test_transition_history_is_atomic_state(self):
        self.s.create("x");self.s.transition("PRECHECK","start");t=self.s.load()
        self.assertEqual(t["transitions"][-1]["to"],"PRECHECK")
        self.assertFalse((self.root/".agents"/"runtime"/"tasks"/t["id"]/"transitions.jsonl").exists())
    def test_blocked_only_resumes_previous_state(self):
        self.s.create("x");self.s.transition("PRECHECK","start");self.s.transition("BLOCKED","external")
        with self.assertRaises(TransitionError):self.s.transition("IMPLEMENT","skip")
        self.assertEqual(self.s.transition("PRECHECK","resume")["state"],"PRECHECK")
    def test_implementation_invalidates_stale_proof(self):
        self.s.create("x");self._precheck();self.s.transition("IMPLEMENT","work")
        def proven(t):
            t["verification_evidence"]=["E-old"];t["verification_epoch"]=t["change_epoch"]
            t["gates"]=[{"id":"G1","description":"proof gate","status":"PROVEN","evidence":["E-old"]},{"id":"G2","description":"waived gate","status":"WAIVED","evidence":[],"waiver_reason":"not applicable","waiver_authority":"policy:test-policy"}]
            t["final_audit_complete"]=True;t["final_audit_workspace"]={"available":False}
        self.s.mutate(proven)
        epoch=self.s.load()["change_epoch"]
        self.s.transition("DIAGNOSE","issue");self.s.transition("IMPLEMENT","fix")
        t=self.s.load();self.assertFalse(t["final_audit_complete"]);self.assertNotIn("final_audit_workspace",t)
        self.assertEqual(t["verification_evidence"],[]);self.assertIsNone(t["verification_epoch"]);self.assertEqual(t["change_epoch"],epoch+1)
        self.assertEqual(t["gates"][0]["status"],"OPEN");self.assertEqual(t["gates"][0]["evidence"],[])
        self.assertEqual(t["gates"][1]["status"],"WAIVED")

    def test_final_audit_requires_resolved_gates_and_critical_risks(self):
        self.s.create("x");self._precheck();self.s.transition("IMPLEMENT","work");self.s.transition("VERIFY","verify")
        task=self.s.load();rec=_append_verified_observation(self.root/".agents"/"runtime"/"tasks"/task["id"],"observation","current verified observation",task_id=task["id"],change_epoch=task["change_epoch"],task_revision=task["revision"],workspace=workspace_fingerprint(self.root),gate_ids=["G1"])
        def setup(t):
            t["verification_evidence"]=[rec["id"]];t["verification_epoch"]=t["change_epoch"];t["evidence_head"]=rec["record_sha256"]
            t["gates"]=[{"id":"G1","description":"current proof","status":"OPEN","evidence":[]}]
            t["risks"]=[{"id":"R1","description":"critical risk","severity":"critical","status":"open"}]
        self.s.mutate(setup)
        with self.assertRaises(TransitionError):self.s.transition("FINAL_AUDIT","too soon")
        def resolve_gate(t):
            t["gates"][0]["status"]="PROVEN";t["gates"][0]["evidence"]=[rec["id"]]
        self.s.mutate(resolve_gate)
        with self.assertRaises(TransitionError):self.s.transition("FINAL_AUDIT","risk still open")
        def resolve_risk(t):
            t["risks"][0]["status"]="resolved";t["risks"][0]["resolution"]="verified mitigation"
        self.s.mutate(resolve_risk)
        self.assertEqual(self.s.transition("FINAL_AUDIT","ready")["state"],"FINAL_AUDIT")

    def test_finalize_rejects_evidence_from_prior_epoch_even_if_state_is_tampered(self):
        task=self.s.create("x");td=self.root/".agents"/"runtime"/"tasks"/task["id"]
        old=append_evidence(td,"test","old proof",change_epoch=0)
        path=td/"state.json";forged=json.loads(path.read_text());forged["state"]="FINAL_AUDIT";forged["change_epoch"]=1;forged["verification_epoch"]=1;forged["verification_evidence"]=[old["id"]];forged["gates"]=[{"id":"G1","description":"gate","status":"PROVEN","evidence":[old["id"]]}];forged["final_audit_complete"]=True;path.write_text(json.dumps(forged))
        with self.assertRaisesRegex(RuntimeError,"state (?:schema|integrity)"):
            self.s.transition("FINALIZE","must reject forged stale proof")

    def test_failed_state_save_rolls_back_its_evidence_append(self):
        task=self.s.create("x")
        td=self.root/".agents"/"runtime"/"tasks"/task["id"]
        attached={}
        def mutate_with_bad_state(state):
            record=append_evidence(td,"test","must roll back",task_revision=state["revision"],lock_held=True)
            attached["record"]=record
            state["evidence_head"]=record["record_sha256"]
            state["title"]="illegal immutable rewrite"
        def rollback():
            record=attached.get("record")
            if record:
                rollback_last_evidence(td,record["record_sha256"],lock_held=True)
        with self.assertRaisesRegex(RuntimeError,"immutable task field changed"):
            self.s.mutate(mutate_with_bad_state,hold_evidence_lock=True,on_failure=rollback)
        self.assertEqual(load_evidence(td),[])
        current=self.s.load()
        self.assertEqual(current["revision"],0)
        self.assertIsNone(current["evidence_head"])

    def test_unbound_direct_append_blocks_canonical_state_mutation(self):
        task=self.s.create("x")
        td=self.root/".agents"/"runtime"/"tasks"/task["id"]
        append_evidence(td,"test","orphan")
        with self.assertRaisesRegex(RuntimeError,"evidence head is not the verified ledger head"):
            self.s.mutate(lambda state:state["precheck"].__setitem__("x",True))

    def test_critical_gate_cannot_be_waived_by_a_caller_supplied_policy_string(self):
        self.s.create("x")
        self.s.mutate(lambda state:state["gates"].append({
            "id":"G1","description":"critical proof","severity":"critical",
            "status":"OPEN","evidence":[],"created_revision":state["revision"]+1,
        }))
        def forge_waiver(state):
            state["gates"][0].update({
                "status":"WAIVED","waiver_reason":"caller says so",
                "waiver_authority":"policy:caller-controlled",
            })
        with self.assertRaisesRegex(RuntimeError,"critical acceptance gates cannot be waived"):
            self.s.mutate(forge_waiver)

    def test_finalized_load_fails_closed_after_workspace_mutation(self):
        self.s.create("x",mode="write",risk="low")
        self._precheck()
        self.s.transition("IMPLEMENT","work")
        self.s.transition("VERIFY","verify")
        task=self.s.load()
        td=self.root/".agents"/"runtime"/"tasks"/task["id"]
        record=_append_verified_observation(
            td,"observation","current proof",
            task_id=task["id"],change_epoch=task["change_epoch"],task_revision=task["revision"],
            workspace=workspace_fingerprint(self.root),gate_ids=["G1"],
        )
        def bind(state):
            state["evidence_head"]=record["record_sha256"]
            state["verification_evidence"]=[record["id"]]
            state["verification_epoch"]=state["change_epoch"]
            state["gates"]=[{
                "id":"G1","description":"proof","severity":"high","status":"PROVEN",
                "evidence":[record["id"]],"created_revision":0,
            }]
        self.s.mutate(bind)
        self.s.transition("FINAL_AUDIT","ready")
        self.s.audit_complete()
        finalized=self.s.transition("FINALIZE","done")
        self.assertEqual(finalized["state"],"FINALIZE")
        with self.assertRaisesRegex(RuntimeError,"terminal task state FINALIZE rejects evidence append"):
            append_evidence(td,"observation","must not append",task_id=task["id"],change_epoch=task["change_epoch"])
        self.assertEqual(self.s.load()["state"],"FINALIZE")
        (self.root/"post-finalize.txt").write_text("changed",encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError,"workspace no longer matches"):
            self.s.load()

    def test_state_and_current_anchor_rollback_is_rejected_by_anchor_history(self):
        task=self.s.create("rollback")
        state_path=self.root/".agents"/"runtime"/"tasks"/task["id"]/"state.json"
        anchor_path=self.root/".agents"/"persistent"/"task-anchors"/f"{task['id']}.json"
        old_state=state_path.read_bytes();old_anchor=anchor_path.read_bytes()
        self.s.mutate(lambda state:state["precheck"].__setitem__("newer",True))
        state_path.write_bytes(old_state);anchor_path.write_bytes(old_anchor)
        with self.assertRaisesRegex(RuntimeError,"anchor history"):
            self.s.load(task["id"])

    def test_gate_and_risk_history_cannot_be_deleted_or_replaced(self):
        self.s.create("append-only claims")
        self.s.mutate(lambda state:(
            state["gates"].append({"id":"G1","description":"real gate","severity":"high","status":"OPEN","evidence":[],"created_revision":state["revision"]+1}),
            state["risks"].append({"id":"R1","description":"real risk","severity":"high","status":"open"}),
        ))
        with self.assertRaisesRegex(RuntimeError,"gate history cannot be deleted"):
            self.s.mutate(lambda state:state.__setitem__("gates",[{"id":"Gfake","description":"replacement","severity":"low","status":"OPEN","evidence":[],"created_revision":state["revision"]+1}]))
        with self.assertRaisesRegex(RuntimeError,"risk history cannot be deleted"):
            self.s.mutate(lambda state:state.__setitem__("risks",[]))

    def test_proven_gate_requires_nonempty_evidence(self):
        self.s.create("empty proof")
        with self.assertRaisesRegex(RuntimeError,"proven acceptance gate requires evidence"):
            self.s.mutate(lambda state:state["gates"].append({"id":"G1","description":"fake","severity":"low","status":"PROVEN","evidence":[],"created_revision":state["revision"]+1}))

    @unittest.skipUnless(os.name == "nt", "Windows junction behavior")
    def test_runtime_junction_cannot_redirect_state_reads_outside_project(self):
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as od:
            root=Path(td);outside=Path(od);(root/".agents"/"runtime").mkdir(parents=True)
            store=StateStore(root);task=store.create("junction")
            runtime=root/".agents"/"runtime";target=outside/"redirected-runtime"
            shutil.copytree(runtime,target);shutil.rmtree(runtime)
            result=subprocess.run(["cmd.exe","/d","/c","mklink","/J",str(runtime),str(target)],capture_output=True,text=True)
            if result.returncode:
                self.skipTest("host cannot create a directory junction")
            try:
                with self.assertRaisesRegex(RuntimeError,"(?:escapes root|redirected control path)"):
                    StateStore(root).load(task["id"])
            finally:
                runtime.rmdir()
