"""Fixed real native read-transport acceptance; creates no chat or model turn."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.atomic import atomic_write_json
from agentinfra.roadmap import compile_roadmaps
from agentinfra.roadmap_lease import WorkspaceLease
from agentinfra.roadmap_native_adapter import NativeGoalAdapter, NativeRpc, capability_snapshot, observe_goal, observe_plan
from agentinfra.roadmap_project import ProjectAdapter
from agentinfra.roadmap_records import ContractError, digest, file_binding, read_json, require
from agentinfra.security import confined_path


def collect(root: Path, protocol: dict, candidate: str, output: str) -> dict:
    record = ProjectAdapter(root).read()
    execution = record["execution"]
    compiled = compile_roadmaps(root)
    native = WorkspaceLease(root).qualify(execution["workspace_lease"])
    require(protocol["executable"]["sha256"] == native["executable"]["sha256"] and
            native["model"] == execution["native_turn_configuration"]["model"] and native["goal"]["status"] == "active",
            "real native host differs from the adopted execution")
    with NativeRpc(root, protocol) as rpc:
        rpc.watch(native)
        goal = observe_goal(root, rpc, compiled, execution["native_binding"])
        plan = observe_plan(root, rpc, execution["native_plan_source"], compiled, execution["scope"])
        root_turns = rpc.turns(goal["thread_id"])
        snapshot = capability_snapshot(root, rpc, native)
        calls = list(rpc.calls)
    try:
        NativeGoalAdapter(root, protocol).prepare("complete", user_authorized=True)
    except ContractError as refusal:
        completion_guard = {"refused": True, "reason": str(refusal), "scope": "actual incomplete adopted objective; no mutation sent"}
    else:
        raise ContractError("incomplete full objective unexpectedly permitted native completion")
    directory = Path(output).parent
    artifacts = {}
    for name, value in (("goal-binding", goal), ("plan-observation", plan), ("capability-snapshot", snapshot),
                        ("rpc-observations", {"schema": 1, "calls": calls, "root_turns": root_turns, "completion_guard": completion_guard}),
                        ("active-host", native)):
        path = directory / (name + "-" + digest(value) + ".json")
        target = confined_path(root, path)
        if target.exists():
            require(read_json(target) == value, "immutable native observation changed")
        else:
            atomic_write_json(target, value, root=root, mode=0o600)
        artifacts[name] = file_binding(root, path.as_posix())
    return {"schema": 1, "kind": "actual_native_read_transport_acceptance", "candidate": candidate, "accepted": True,
            "goal_binding": artifacts["goal-binding"], "plan_binding": plan["binding"],
            "plan_observation": artifacts["plan-observation"], "capability_snapshot": artifacts["capability-snapshot"],
            "artifacts": list(artifacts.values()), "domain_proof": False, "installed_native_executable": protocol["executable"],
            "limits": ["Real read RPCs and active-host observations; no new chat, model turn or live Goal mutation",
                       "Host lifecycle dispatch/recovery uses explicit callbacks and separate durable reservations",
                       "Native service, local journal and host callback are explicit provenance/authorization trust boundaries"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["acceptance"])
    parser.add_argument("--protocol", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--candidate", required=True)
    args = parser.parse_args()
    result = collect(ROOT, read_json(confined_path(ROOT, args.protocol)), args.candidate, args.output)
    atomic_write_json(confined_path(ROOT, args.output), result, root=ROOT, mode=0o600)
    print({"accepted": result["accepted"], "candidate": result["candidate"], "native_plan_item": result["plan_binding"]["native_item_id"],
           "domain_proof": False})


if __name__ == "__main__":
    main()
