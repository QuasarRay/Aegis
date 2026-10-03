"""Qualify Z3 proof reconstruction and reject contaminated theorem objects."""
from pathlib import Path
import json
import os
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra"))

from agentinfra.contracts import digest, require
from agentinfra.hol4 import executable_identity, holmake, mcp_stdio_config, mcp_smoke


SCRIPT = r"""open HolKernel boolLib bossLib integerTheory;
val _ = new_theory "AegisHol4Smoke";

val goal = ``!x y:int. (2*x <= 2*y /\ y < x+1) ==> (x = y)``;
val reconstructed = prove (goal, HolSmtLib.Z3_TAC);

(* DISK_THM is HOL4's loaded-theory bookkeeping marker, not an SMT oracle.
   Match the pinned Sanity default; do not trust its mutable allow lists. *)
fun acceptable expected th =
  let val (oracles, axioms) = Tag.dest_tag (Thm.tag th)
  in null (Thm.hyp th) andalso aconv (Thm.concl th) expected
     andalso List.all (fn name => name = "DISK_THM") oracles
     andalso null axioms
  end;
val _ = if acceptable goal reconstructed then ()
        else raise Fail "reconstructed theorem failed scope/tag inspection";
val _ = if acceptable goal (mk_oracle_thm "AegisRejectedProbe" ([], goal))
        orelse acceptable goal (ASSUME goal) orelse acceptable goal TRUTH
        then raise Fail "theorem inspection accepted a negative control" else ();
val _ = save_thm ("integer_interval", reconstructed);

val _ = export_theory();
val out = TextIO.openOut "inspection.json";
val _ = TextIO.output (out,
  "{\"theorem\":\"AegisHol4Smoke.integer_interval\",\"goal_checked\":true,\"hypotheses\":0,\"non_disk_oracles\":0,\"local_axioms\":0,\"negative_controls\":3}\n");
val _ = TextIO.closeOut out;
"""


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="aegis-hol4-") as td:
        root = Path(td)
        (root / ".aegis").mkdir()
        theory = root / "theory"
        theory.mkdir()
        (theory / "AegisHol4SmokeScript.sml").write_text(SCRIPT)
        (theory / "Holmakefile").write_text("INCLUDES = $(HOLDIR)/src/integer $(HOLDIR)/src/HolSmt\n")
        solver = Path(os.environ["HOL4_Z3_EXECUTABLE"])
        solver_before = executable_identity(solver)
        result = holmake(root, "theory", timeout=600)
        require(executable_identity(solver) == solver_before, "Z3 executable changed during replay")
        inspected = None
        artifacts = {}
        if result["status"] == "CHECKED":
            inspected = json.loads((theory / "inspection.json").read_text())
            require(inspected == {"theorem": "AegisHol4Smoke.integer_interval", "goal_checked": True,
                    "hypotheses": 0, "non_disk_oracles": 0, "local_axioms": 0, "negative_controls": 3},
                    "unexpected theorem inspection result")
            for name in ("AegisHol4SmokeTheory.sml", "AegisHol4SmokeTheory.sig"):
                data = (theory / name).read_bytes()
                require(bool(data), "theory export is empty")
                artifacts[name] = digest(data)
        config = None
        try:
            config = mcp_stdio_config(root)
            mcp = mcp_smoke(root)
        except Exception as exc:
            # Preserve the direct replay observation even if the optional
            # navigation service is broken. Overall qualification still fails.
            mcp = {"status": "FAILED", "reason": str(exc), "claim": "MCP discovery only"}
        output = ROOT / ".aegis/hol4-qualification.json"
        output.parent.mkdir(exist_ok=True)
        output.write_text(json.dumps({
            "claim": "Z3/HOL4 reconstruction and inspection qualification only; not MetaRocq refinement",
            "script_sha256": digest(SCRIPT.encode()), "z3": solver_before,
            "inspection": inspected, "exports": artifacts,
            "mcp": config,
            "mcp_smoke": mcp,
            "holmake": result,
        }, indent=2) + "\n")
        print(json.dumps({"status": result["status"], "claim": result["claim"]}))
        return 0 if result["status"] == "CHECKED" and mcp["status"] == "READY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
