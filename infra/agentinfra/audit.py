"""Cheap structural checks; focused regression tests are a separate explicit run."""
import ast
from pathlib import Path
import tomllib

from .contracts import load_authority
from .release_source import validate_version_consistency
from .security import confined_path


def audit_source(framework):
    failures = []
    contract = load_authority(framework)
    version = validate_version_consistency(framework)
    if not version["ok"]:
        failures.append({"version": version["mismatches"]})
    source = framework / "infra/agentinfra"
    retired = {"tdd_runtime", "unittest_observer", "state_store", "state_machine", "assurance",
               "falsification_runtime", "final_audit_runtime", "review_runtime"}
    for path in source.glob("*.py"):
        if path.stem in retired:
            failures.append(f"Retired execution machinery present: {path.name}")
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.level and node.module:
                if not (source / (node.module.replace(".", "/") + ".py")).exists():
                    failures.append(f"Broken local import in {path.name}: {node.module}")
    with (framework / "modules/codex/config/managed.toml").open("rb") as stream:
        model = tomllib.load(stream)
    if model.get("model") != "gpt-6-astra" or model.get("agents", {}).get("default_subagent_model") != "gpt-6-astra":
        failures.append("Model configuration drift")
    root_instructions = (framework / "AGENTS.md").read_bytes()
    # Audit source/distribution directories without entering build or runtime output.
    import os
    for directory, names, files in os.walk(framework, followlinks=False):
        names[:] = sorted(n for n in names if n not in {".git", ".aegis", "dist", "target", "__pycache__"})
        for name in names:
            confined_path(framework, (Path(directory) / name).relative_to(framework))
        if not files and not names:
            continue
        relative = (Path(directory) / "AGENTS.md").relative_to(framework)
        path = confined_path(framework, relative)
        if not path.is_file() or path.read_bytes() != root_instructions:
            failures.append(f"Missing/divergent instructions: {relative}")
    return {"ok": not failures, "failures": failures, "contract_definitions": len(contract["catalog"]),
            "version": version["version"], "claim": "Structural audit only; no Candle refinement proof"}
