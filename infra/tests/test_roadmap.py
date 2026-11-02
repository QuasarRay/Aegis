from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.roadmap import compile_roadmaps, audit_evidence, packet, project_into_record, FENCE
from agentinfra.roadmap_records import ContractError, canonical, digest, file_binding, loads, read_json, validate
from agentinfra.roadmap_policy import (SEMANTIC_FIELDS, authorize, correspondence_errors, proof_errors,
                                     semantic_identity, goal_transition, may_reserve, all_satisfied, cgp_eligible)
from agentinfra.roadmap_runtime import BudgetLedger
from agentinfra.roadmap_codex import bind_goal, bind_plan, CodexReader
from agentinfra.roadmap_review import render_packet, validate_decision, advance_review, adjudicate_findings, STAGES
from agentinfra.roadmap_portability import inventory
from agentinfra.roadmap_knowledge import retrieve
from agentinfra.locks import FileLock, LockError
from agentinfra.roadmap_lease import WorkspaceLease
from agentinfra.roadmap_verification import reconcile_original_tests, reconcile_native_transition
from agentinfra.roadmap_scope import validate_write_scope


class CompilerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_temp = tempfile.TemporaryDirectory()
        cls.base = Path(cls.base_temp.name)
        shutil.copytree(ROOT / "Roadmaps", cls.base / "Roadmaps", ignore=shutil.ignore_patterns("python-rust"))
        sources = read_json(ROOT / "Roadmaps/Shared/sources.json")
        # Small fixture retains every authoritative text; binary corpus stays a separate ingestion concern.
        sources["files"] = [s for s in sources["files"] if s["path"].lower().endswith(".md")]
        for source in sources["files"]:
            p = cls.base / source["path"]; p.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / source["path"], p)
        (cls.base / "Roadmaps/Shared/sources.json").write_bytes(canonical(sources))

    @classmethod
    def tearDownClass(cls): cls.base_temp.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name)
        shutil.copytree(self.base, self.root, dirs_exist_ok=True)

    def tearDown(self): self.temp.cleanup()

    def edit_json(self, name, edit):
        path = self.root / "Roadmaps/Shared" / name; value = read_json(path)
        edit(value); path.write_bytes(canonical(value))

    def edit_contract(self, ident, edit):
        project = {"A": "Aegis", "B": "Blue", "D": "Destiny"}[ident[0]]
        path = next((self.root / "Roadmaps" / project).glob(ident[1:] + "-*.md"))
        text = path.read_text(); block = FENCE.search(text); item = loads(block[1]); edit(item)
        path.write_text(text[:block.start()] + "```aegis-milestone\n" + json.dumps(item) + "\n```" + text[block.end():])

    def test_determinism_packets_and_empty_evidence(self):
        c = compile_roadmaps(self.root); self.assertEqual(c, compile_roadmaps(self.root)); self.assertEqual(len(c["milestones"]), 40)
        a = audit_evidence(self.root, c, dict(schema=1, compiled_digest=c["digest"], receipts=[]))
        for ident in c["order"]:
            self.assertNotEqual(a["milestones"][ident]["state"], "SATISFIED")
            self.assertEqual(packet(c, a, ident)["contract"]["id"], ident)

    def test_source_edits_rejected(self):
        with (self.root / "Blue_Prompt.md").open("a") as stream: stream.write("changed")
        with self.assertRaisesRegex(ContractError, "source authority changed"): compile_roadmaps(self.root)

    def test_missing_and_duplicate_requirements(self):
        self.edit_json("requirements.json", lambda x: x["requirements"].pop(0))
        with self.assertRaises(ContractError): compile_roadmaps(self.root)

    def test_duplicate_requirement(self):
        self.edit_json("requirements.json", lambda x: x["requirements"].append(x["requirements"][0]))
        with self.assertRaisesRegex(ContractError, "duplicate requirement"): compile_roadmaps(self.root)

    def test_cycle(self):
        self.edit_contract("A00", lambda x: x["dependencies"].append("A01"))
        with self.assertRaisesRegex(ContractError, "cycle"): compile_roadmaps(self.root)

    def test_unknown_dependency(self):
        self.edit_contract("A00", lambda x: x["dependencies"].append("Z99"))
        with self.assertRaisesRegex(ContractError, "missing dependency"): compile_roadmaps(self.root)

    def test_unknown_recipe(self):
        self.edit_contract("A00", lambda x: x["checks"].append("retrieved.shell"))
        with self.assertRaisesRegex(ContractError, "undeclared"): compile_roadmaps(self.root)

    def test_recipe_injection(self):
        self.edit_json("registry.json", lambda x: x["recipes"]["roadmap.validate"].update(argv=["python", "-c", "raise Exception()"] ))
        with self.assertRaisesRegex(ContractError, "unreviewed"): compile_roadmaps(self.root)

    def test_formal_gate_cannot_block_implementation(self):
        self.edit_contract("B03", lambda x: x["gates"].append("full_domain_proof"))
        with self.assertRaisesRegex(ContractError, "formal campaign"): compile_roadmaps(self.root)

    def test_early_cgp_dependency_rejected(self):
        self.edit_contract("A14", lambda x: x["dependencies"].remove("D11"))
        with self.assertRaisesRegex(ContractError, "global CGP"): compile_roadmaps(self.root)

    def test_provider_and_reasoning_downgrades(self):
        self.edit_json("policy.json", lambda x: x.update(provider="other"))
        with self.assertRaisesRegex(ContractError, "CODEX_ONLY"): compile_roadmaps(self.root)

    def test_capability_provider_must_be_a_dependency(self):
        self.edit_contract("A01", lambda x: x["consumes"][0].update(provider="A09"))
        with self.assertRaisesRegex(ContractError, "capability"): compile_roadmaps(self.root)

    def test_scope_protects_originals_and_declares_owned_paths(self):
        c=compile_roadmaps(self.root)["milestones"]["A01"]
        validate_write_scope(self.root,c,["infra/agentinfra/new.py"])
        for path in ["AGENTS.MD","Roadmaps/Blue/AGENTS.MD","../escape","unowned/file.py"]:
            with self.subTest(path=path),self.assertRaises((ContractError,ValueError)):
                validate_write_scope(self.root,c,[path])

    def test_unknown_schema(self):
        self.edit_contract("A00", lambda x: x.update(schema=2))
        with self.assertRaisesRegex(ContractError, "constant"): compile_roadmaps(self.root)

    def test_projection_preserves_record_and_cas(self):
        p = self.root / "queue.json"; p.write_text('{"existing":"keep","failures":[1]}')
        old = digest(p.read_bytes()); project_into_record(self.root, "queue.json", {"milestones": {}}, old)
        self.assertEqual(read_json(p)["failures"], [1])
        with self.assertRaisesRegex(ContractError, "changed"): project_into_record(self.root, "queue.json", {}, old)

    def test_stale_and_mixed_candidate_evidence(self):
        c = compile_roadmaps(self.root); contract = c["milestones"]["A00"]; b = file_binding(self.root, "AGENTS.MD")
        receipts = [dict(schema=1,id=g,milestone="A00",gate=g,producer="owned-fixture",candidate="candidate",contract_digest=digest(contract),inputs=[b],artifacts=[b],command=[],configuration={},outcome="PASS",scope="production",limits=["fixture only"],logs=[b]) for g in contract["gates"]]
        for receipt in receipts:
            if receipt["gate"] == "implemented_outputs":
                receipt["configuration"] = dict(outputs=contract["outputs"], implementation_units=contract["implementation_units"])
        def audit(): return audit_evidence(self.root,c,dict(schema=1,compiled_digest=c["digest"],receipts=receipts))["milestones"]["A00"]
        self.assertEqual(audit()["state"], "SATISFIED")
        receipts[0]["candidate"]="other"; self.assertIn("ONE_COHERENT_CANDIDATE",audit()["missing_gates"])
        receipts[0]["candidate"]="candidate"; receipts[0]["artifacts"][0] = dict(b,sha256="0"*64)
        self.assertIn(receipts[0]["gate"],audit()["missing_gates"])

    def test_changed_input_invalidates_previously_compiled_audit(self):
        c=compile_roadmaps(self.root)
        p=self.root/"Roadmaps/Aegis/GOAL.md";p.write_text(p.read_text()+"changed launcher\n")
        with self.assertRaisesRegex(ContractError,"stale"):
            audit_evidence(self.root,c,dict(schema=1,compiled_digest=c["digest"],receipts=[]))


class DomainPolicyTests(unittest.TestCase):
    def test_strict_records(self):
        for bad in ('{"a":1,"a":2}', '{"n":NaN}'):
            with self.assertRaises(ContractError): loads(bad)
        with self.assertRaises(ContractError): validate(True, {"type":"integer"})
        with self.assertRaises(ContractError): validate({}, {"unevaluatedProperties":False})

    def test_budgets_and_completion(self):
        self.assertTrue(may_reserve(2,3,4,9)); self.assertFalse(may_reserve(2,3,5,9)); self.assertFalse(may_reserve(True,0,1,9))
        self.assertFalse(all_satisfied([],[])); self.assertFalse(all_satisfied(["impl","proof"],["impl"]))
        self.assertFalse(cgp_eligible(dict(Aegis="PROJECT_COMPLETE",Blue="PROJECT_COMPLETE",Destiny="DOMAIN_VERIFIED")))

    def test_exact_semantics_detect_each_weakened_field(self):
        original={k:["exact source behavior"] for k in SEMANTIC_FIELDS}
        self.assertTrue(semantic_identity(original,copy.deepcopy(original)))
        for field in SEMANTIC_FIELDS:
            with self.subTest(field=field):
                changed=copy.deepcopy(original); changed[field]=[]; self.assertFalse(semantic_identity(original,changed))

    def test_correspondence_bijection_and_relationships(self):
        groups=[dict(source_id="S1",target_id="T1",production_bindings=["actual.rs:1"],members=["method"],required_relationships=["base"],implemented_relationships=["base"])]
        self.assertEqual(correspondence_errors(["S1"],groups),[])
        self.assertTrue(correspondence_errors(["S1","S2"],groups))
        self.assertTrue(correspondence_errors(["S1","S2"],groups+[dict(groups[0],source_id="S2")]))
        groups[0]["implemented_relationships"]=[]; self.assertTrue(correspondence_errors(["S1"],groups))

    def test_proof_strength_and_freshness(self):
        obligation=dict(obligation_id="fixture::test[config]",candidate="C",production_digest="P",contract_digest="S",assertions=["A"],covers=["reached"],assumptions=[],bounds={"domain":"original"},toolchain={"kani":"pin"},backend="kani",origin="aegis_requirement")
        result=dict(obligation,status="PROVED",executed=True,timed_out=False,truncated=False,unsupported=False,unwind_incomplete=False,model_only=False,assertions={"A":"SUCCESS"},covers={"reached":"SUCCESS"})
        self.assertEqual(proof_errors(obligation,result),[])
        mutations=[dict(status="INTERRUPTED"),dict(backend="crosshair"),dict(covers={}),dict(assertions={"A":"FAILURE"}),dict(production_digest="old"),dict(candidate="other"),dict(bounds={"narrowed":True})]
        mutations += [{k:True} for k in ("timed_out","truncated","unsupported","unwind_incomplete","model_only")]
        for change in mutations:
            with self.subTest(change=change): self.assertTrue(proof_errors(obligation,dict(result,**change)))

    def test_plan_scope_effort_and_campaign_gates(self):
        context=dict(provider="codex",mode="execute",authorized=True,goal_status="active",requested_effort="max",accepted_effort="max",effective_effort="max",selected_model="selected",observed_model="selected",active_agents=1,lease_valid=True,expected_inputs="X",current_inputs="X")
        self.assertTrue(authorize("implement",context)["allowed"])
        for change in (dict(mode="plan"),dict(effective_effort=None),dict(active_agents=2),dict(goal_status="paused"),dict(authorized=False),dict(current_inputs="Y"),dict(observed_model="rerouted"),dict(monetary_cap=5)):
            with self.subTest(change=change): self.assertFalse(authorize("implement",dict(context,**change))["allowed"])
        self.assertFalse(authorize("review_campaign",context)["allowed"])
        self.assertFalse(authorize("cgp",context)["allowed"])


class RuntimeAndReviewTests(unittest.TestCase):
    def setUp(self): self.temp=tempfile.TemporaryDirectory(); self.root=Path(self.temp.name)
    def tearDown(self): self.temp.cleanup()

    def test_reservation_restart_does_not_refund_or_duplicate(self):
        ledger=BudgetLedger(self.root); first=ledger.reserve("work","inputs1",10)
        with self.assertRaisesRegex(ContractError,"recovery"): BudgetLedger(self.root).reserve("work","inputs1",10)
        ledger.close(first["id"],"INTERRUPTED",{"handle":"uncertain"})
        with self.assertRaises(ContractError): ledger.reserve("work","inputs1",10,diagnosis="interrupted")
        with self.assertRaises(ContractError): ledger.reserve("work","inputs2",10)
        second=ledger.reserve("work","inputs2",10,diagnosis="fixed exact missing input"); ledger.close(second["id"],"SUCCESS",{})
        with self.assertRaises(ContractError): ledger.reserve("work","inputs3",10,diagnosis="another")
        self.assertEqual(len(BudgetLedger(self.root).read()["attempts"]),2)

    def test_cumulative_usage_unknown_duplicates_and_resets(self):
        ledger=BudgetLedger(self.root)
        self.assertIsNone(ledger.observe_usage("T","unknown",None)["total"])
        ledger.observe_usage("T","event1",12); ledger.observe_usage("T","event1",12)
        self.assertEqual(ledger.observe_usage("T","event2",15)["total"],15)
        with self.assertRaises(ContractError): ledger.observe_usage("T","event1",13)
        with self.assertRaises(ContractError): ledger.observe_usage("T","reset",1)

    def test_live_owner_excludes_duplicate_dispatch(self):
        a=FileLock(self.root/"lease","fixture"); b=FileLock(self.root/"lease","fixture")
        a.acquire()
        try:
            with self.assertRaises(LockError): b.acquire(timeout=0)
        finally: a.release()

    def test_native_identity_pause_clear_and_accounting(self):
        goal=dict(thread_id="T",objective="whole project",status="active",tokensUsed=300)
        binding=bind_goal(goal,thread_id="T",objective="whole project",contract_hash="a"*64)
        self.assertEqual(binding["observation"]["tokensUsed"],300)
        for requested in (dict(thread_id="X",action="complete"),dict(thread_id="T",action="complete",objective="subset")):
            with self.assertRaises(ContractError): goal_transition(goal,requested,user_authorized=True,acceptance=True)
        with self.assertRaises(ContractError): goal_transition(goal,dict(thread_id="T",action="complete"),user_authorized=True)
        prepared=goal_transition(goal,dict(thread_id="T",action="complete"),user_authorized=True,acceptance=True)
        self.assertNotIn("objective",prepared["params"]); self.assertNotIn("tokenBudget",prepared["params"])
        for action in ("pause","clear","budget"):
            with self.assertRaises(ContractError): goal_transition(goal,dict(thread_id="T",action=action),user_authorized=False)
        self.assertEqual(goal_transition(goal,dict(thread_id="T",action="pause"),user_authorized=True)["params"]["status"],"paused")
        self.assertEqual(goal_transition(goal,dict(thread_id="T",action="clear"),user_authorized=True)["method"],"thread/goal/clear")

    def test_native_plan_scope_and_transport_boundary(self):
        plan=dict(id="P",type="plan",text="A00 authority")
        self.assertEqual(bind_plan(plan,["A00"],dict(digest="x",milestones={"A00":{}}))["milestones"],["A00"])
        with self.assertRaises(ContractError): bind_plan(plan,["A01"],dict(digest="x",milestones={"A00":{}}))
        reader=object.__new__(CodexReader)
        with self.assertRaisesRegex(ContractError,"read-only"): reader.call("turn/start",{})

    def test_native_completion_requires_confirmed_readback(self):
        before=dict(threadId="T",objective="whole",status="active",tokensUsed=12,timeUsedSeconds=3)
        after=dict(before,status="complete",tokensUsed=15)
        self.assertFalse(reconcile_native_transition(before,{},None,"complete")["confirmed"])
        self.assertTrue(reconcile_native_transition(before,None,after,"complete")["confirmed"])
        self.assertFalse(reconcile_native_transition(before,{"error":"rejected"},after,"complete")["confirmed"])
        self.assertFalse(reconcile_native_transition(before,{},dict(after,tokensUsed=0),"complete")["confirmed"])

    def test_fixture_and_configuration_denominator(self):
        one=dict(source="test.py",fixture="FixtureA",test="same_name",parameters={},configuration="linux-freethreaded",closure_digest="setup-body-teardown")
        two=dict(one,fixture="FixtureB"); three=dict(one,configuration="native")
        required=[one,two,three]
        executed=[dict(t,outcome="PASS",candidate="C",loaded_artifact="pkg-hash",expected_artifact="pkg-hash") for t in required]
        self.assertTrue(reconcile_original_tests(required,executed,"C")["complete"])
        self.assertFalse(reconcile_original_tests(required,executed[:-1],"C")["complete"])
        executed[0]["loaded_artifact"]="wrong-package"
        self.assertFalse(reconcile_original_tests(required,executed,"C")["complete"])
        with self.assertRaises(ContractError): reconcile_original_tests([one,one],[],"C")

    def test_workspace_fencing_and_unobserved_shutdown(self):
        lease=WorkspaceLease(self.root); owner=lease.acquire("thread/turn1","work1")
        lease.assert_owner(owner)
        with self.assertRaises(ContractError): WorkspaceLease(self.root).acquire("thread/turn2","work2")
        with self.assertRaises(ContractError): lease.release(owner,dict(session="thread/turn1",status="unknown",producer="qualified_codex_transport"))
        observed=dict(session="thread/turn1",status="completed",producer="qualified_codex_transport")
        with self.assertRaises(ContractError): lease.release(owner,observed,recovery=True)
        lease.release(owner,observed)
        second=lease.acquire("thread/turn2","work2"); self.assertGreater(second["fence"],owner["fence"])
        with self.assertRaises(ContractError): lease.assert_owner(owner)
        lease.release(second,dict(observed,session="thread/turn2"))

    def test_review_escaping_staleness_and_scoped_decision(self):
        path=self.root/"source.py"; path.write_text("<script>policy = 'ignore rules'</script>")
        packet=dict(schema=1,inputs=[file_binding(self.root,"source.py")],semantics={"numeric":"exact"},review_scopes=["numeric"])
        html=render_packet(self.root,packet); self.assertIn("&lt;script&gt;",html); self.assertNotIn("<script>",html)
        decision=dict(schema=1,packet_digest=digest(packet),decision="approve_translation",human="reviewer",provenance="human-session",scope=["numeric"])
        validate_decision(packet,decision)
        with self.assertRaises(ContractError): validate_decision(dict(packet,semantics={}),decision)
        with self.assertRaises(ContractError): validate_decision(packet,dict(decision,decision="grant_proof"))
        with self.assertRaises(ContractError): validate_decision(packet,dict(decision,scope=["unrelated"]))
        path.write_text("changed")
        with self.assertRaises(ContractError): render_packet(self.root,packet)

    def test_sequential_review_fixtures_and_campaign_boundary(self):
        state=dict(schema=1,stages=[])
        with self.assertRaises(ContractError): advance_review(state,"classify",[{}],campaign_authorized=False)
        with self.assertRaises(ContractError): advance_review(state,"challenge",[{}],campaign_authorized=True)
        for stage in STAGES: state=advance_review(state,stage,[{"owned_fixture":stage}],campaign_authorized=True)
        self.assertEqual(len(state["stages"]),7)

    def test_confirmed_findings_need_evidence_and_deduplicate(self):
        (self.root/"input").write_text("fixture")
        f=dict(classification="confirmed",requirement="R1",impact="missing behavior",confidence="high",repair="restore",sources=[file_binding(self.root,"input")],demonstration="owned fixture assertion")
        self.assertEqual(len(adjudicate_findings(self.root,[f,f])),1)
        with self.assertRaises(ContractError): adjudicate_findings(self.root,[dict(f,demonstration="")])

    def test_python_behavior_inventory_changes_and_blocks(self):
        p=self.root/"infra/example.py"; p.parent.mkdir(); p.write_text("x = [n for n in range(3)]\ntry:\n    x.append(4)\nexcept ValueError:\n    pass\n")
        before=inventory(self.root); kinds={u["kind"] for u in before["units"]}
        self.assertTrue({"Module","Assign","ListComp","Call","Try","ExceptHandler"} <= kinds)
        p.write_text(p.read_text().replace("range(3)","range(4)")); self.assertNotEqual(before["digest"],inventory(self.root)["digest"])

    def test_corpus_exact_citations_versions_and_budget(self):
        (self.root/"text.md").write_text("first\nsecond\n")
        p=self.root/"Roadmaps/Shared/corpus.json"; p.parent.mkdir(parents=True)
        p.write_bytes(canonical(dict(sources=[dict(id="S",status="RETAINED_TEXT",binding=file_binding(self.root,"text.md"))])))
        self.assertEqual(retrieve(self.root,"S",2,2)["content"],"second")
        for start,end in ((0,1),(1,3)):
            with self.assertRaises(ContractError): retrieve(self.root,"S",start,end)
        with self.assertRaises(ContractError): retrieve(self.root,"S",1,2,max_bytes=2)
        (self.root/"text.md").write_text("new edition")
        with self.assertRaises(ContractError): retrieve(self.root,"S",1,1)


if __name__ == "__main__": unittest.main()
