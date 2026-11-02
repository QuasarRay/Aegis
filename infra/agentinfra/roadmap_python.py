"""Python source routing and conservative, source-bound backend qualification.

This module observes source without importing it. A static closure is deliberately
an overapproximation, not a proof of Python's dynamic import/call semantics.
Qualification and runtime controls never create a domain-proof receipt.
"""
from __future__ import annotations

import ast
import importlib.util
from pathlib import Path
import re
import zipfile

from .roadmap_portability import inventory, maintained_python
from .roadmap_records import bindings_current, digest, file_binding, read_json, require
from .security import confined_path


INTERFACE_VERSION = 1
BACKENDS = ("nagini", "esbmc-python", "deal", "apex", "crosshair")
DYNAMIC = {"eval", "exec", "__import__", "importlib.import_module", "getattr", "setattr", "globals", "locals"}
EFFECT_MODULES = {"os", "pathlib", "subprocess", "socket", "sqlite3", "threading", "multiprocessing", "ctypes"}


def _modules(root: Path, *, include_tests: bool = False) -> dict[str, Path]:
    result = {}
    for path in maintained_python(root):
        relative = path.relative_to(root).as_posix()
        if relative.startswith("infra/agentinfra/"):
            name = relative.removeprefix("infra/").removesuffix(".py").replace("/", ".")
            result[name.removesuffix(".__init__")] = path
        elif include_tests and relative.startswith("infra/tests/"):
            name = relative.removeprefix("infra/tests/").removesuffix(".py").replace("/", ".")
            key = name.removesuffix(".__init__")
            require(key not in result, "ambiguous maintained test module namespace")
            result[key] = path
    return result


def module_closure(root: Path, module: str, *, include_tests: bool = False) -> dict:
    """Retain whole transitive local modules, package initializers and hazards.

    No dead-code pruning: private functions, unused imports, conditional imports,
    module state and exception paths remain bound. External dependencies and
    dynamic dispatch stay explicit unsupported boundaries.
    """
    modules = _modules(root, include_tests=include_tests)
    require(module in modules, "unknown maintained Python module")
    pending, visited, files, external, hazards = [module], set(), [], set(), []
    while pending:
        name = pending.pop()
        if name in visited:
            continue
        visited.add(name)
        path = modules[name]
        relative = path.relative_to(root).as_posix()
        files.append(file_binding(root, relative))
        tree = ast.parse(path.read_bytes(), filename=relative)
        package = name if path.name == "__init__.py" else name.rpartition(".")[0]
        dependencies = set()
        for count in range(1, len(name.split("."))):
            parent = ".".join(name.split(".")[:count])
            if parent in modules:
                dependencies.add(parent)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                dependencies.update(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                dependency = importlib.util.resolve_name("." * node.level + (node.module or ""), package) if node.level else node.module
                if dependency:
                    dependencies.add(dependency)
                    dependencies.update(dependency + "." + a.name for a in node.names if dependency + "." + a.name in modules)
            elif isinstance(node, ast.Call) and ast.unparse(node.func) in DYNAMIC:
                hazards.append({"path": relative, "line": node.lineno, "kind": "dynamic_binding", "expression": ast.unparse(node.func)})
            elif isinstance(node, (ast.AsyncFunctionDef, ast.Await, ast.Yield, ast.YieldFrom)):
                hazards.append({"path": relative, "line": node.lineno, "kind": type(node).__name__})
        for dependency in dependencies:
            if dependency in modules:
                pending.append(dependency)
            elif dependency != "__future__":
                external.add(dependency)
    external_rows = []
    for name in sorted(external):
        # Never import target modules while establishing source closure.
        external_rows.append({"module": name, "status": "REQUIRES_BACKEND_SEMANTIC_QUALIFICATION",
                              "runtime_effect_boundary": name.split(".")[0] in EFFECT_MODULES})
    record = {"schema": 1, "module": module, "files": sorted(files, key=lambda b: b["path"]),
              "external": external_rows, "hazards": sorted(hazards, key=lambda h: (h["path"], h["line"], h["kind"])),
              "closure_kind": "whole transitive maintained modules; dynamic/external semantics unresolved",
              "semantic_closure_proved": False}
    record["digest"] = digest(record)
    return record


def source_closure(root: Path, target: str) -> dict:
    """Bind an exact unshadowed production declaration and its module closure."""
    modules = _modules(root)
    module, separator, symbol = target.partition(":")
    require(separator and module in modules and symbol, "unknown Python production target")
    tree = ast.parse(modules[module].read_bytes())
    declarations = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.name == symbol]
    require(len(declarations) == 1, "missing or shadowed production target")
    record = module_closure(root, module)
    record.pop("digest")
    record.update(target=target, target_ast_sha256=digest(ast.dump(declarations[0], include_attributes=False).encode()))
    record["digest"] = digest(record)
    return record


def research_sources(root: Path) -> dict:
    disposition = read_json(root / "Roadmaps/Shared/python-rust-research-dispositions.json")
    require(bindings_current(root, [disposition["archive"]]), "Python research archive changed")
    chapters = disposition["chapters"]
    with zipfile.ZipFile(confined_path(root, disposition["archive"]["path"])) as archive:
        require(sorted(archive.namelist()) == sorted(c["member"] for c in chapters), "research chapter denominator changed")
        for chapter in chapters:
            raw = archive.read(chapter["member"])
            require(len(raw) == chapter["bytes"] and digest(raw) == chapter["sha256"], "research chapter identity changed")
    recommendations = disposition["recommendations"]
    require(len(recommendations) == 24 and len({r["id"] for r in recommendations}) == 24, "research recommendation denominator changed")
    return {"report": file_binding(root, "Python_Verification_Research_Report_v1.md"),
            "archive": disposition["archive"], "chapters": chapters,
            "recommendations": recommendations, "claims": "unverified research; not executable instructions or qualification"}


def original_occurrences(root: Path) -> list[dict]:
    """Static test locations bind their entire file and retain fixture uncertainty.

    Discovery remains the unchanged original.tests producer's responsibility.
    This index never claims to enumerate dynamic/parameterized runtime instances.
    """
    rows = []
    for path in sorted((root / "infra/tests").glob("test*.py")):
        relative = path.relative_to(root).as_posix()
        tree = ast.parse(path.read_bytes())
        for cls in [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]:
            for node in cls.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test"):
                    row = {"source": file_binding(root, relative), "fixture": cls.name, "test": node.name,
                           "span": [node.lineno, node.end_lineno],
                           "ast_sha256": digest(ast.dump(node, include_attributes=False).encode()),
                           "status": "REQUIRES_FULL_FIXTURE_AND_RUNTIME_OCCURRENCE_CLOSURE"}
                    row["id"] = digest(row)
                    rows.append(row)
    return rows


def route(root: Path, compiled: dict, candidate: str) -> dict:
    from .roadmap_python_catalog import obligation_catalog
    source_inventory = inventory(root)
    locations = original_occurrences(root)
    catalog = obligation_catalog(root, compiled, candidate, source_inventory, locations)
    closure = source_closure(root, "agentinfra.roadmap_policy:may_reserve")
    return {"schema": 1, "candidate": candidate, "domain_proof": False,
            "research": research_sources(root), "backends": read_json(root / "Roadmaps/Shared/python-backends.json"),
            "source_files": source_inventory["files"], **catalog,
            "original_test_locations": locations,
            "qualification_targets": [{"target": "agentinfra.roadmap_policy:may_reserve", "closure": closure,
                                       "origin": "infra/tests/test_roadmap.py::DomainPolicyTests::test_budgets_and_completion",
                                       "status": "CANDIDATE_INGESTION_ONLY_NOT_DOMAIN_CLOSURE"}],
            "interventions": [{"id": "PY-IMPORT-CLOSURE", "target": closure["target"],
                               "source_closure": closure["digest"], "external": closure["external"], "hazards": closure["hazards"],
                               "required_behavior": "Preserve complete actual Python imports, exact int/bool checks and unbounded integer semantics",
                               "resolution": "Qualify actual import closure; retain unsupported code and request engineering intervention if unresolved"}],
            "acceptance": "Routing/index evidence only; every unresolved source unit and domain obligation remains required"}


def classify_nagini(run: dict) -> dict:
    """Conservative parser for pinned Nagini CLI observations, not proof promotion."""
    if run.get("timed_out") or run.get("stdout_truncated") or run.get("stderr_truncated"):
        return {"outcome": "INDETERMINATE", "reason": "timeout or truncated logs"}
    output = run.get("stdout", "") + "\n" + run.get("stderr", "")
    if re.search(r"Verification successful[.!]", output) and run.get("returncode") == 0:
        if re.search(r"(?i)traceback|not supported|unsupported|verification failed|type error", output):
            return {"outcome": "UNSUPPORTED_OR_ERROR", "reason": "success text contradicted by diagnostics"}
        return {"outcome": "VERIFIED_TOOL_RESULT", "reason": "CLI success; source/semantic/reachability review remains required"}
    if (run.get("returncode") not in {None, 0} and re.search(r"Verification failed[.!]", output)
            and re.search(r"assert.failed|assertion.false", output) and not re.search(r"(?i)traceback|type error|unsupported", output)):
        return {"outcome": "ASSERTION_COUNTEREXAMPLE", "reason": "backend reported a failed assertion; exact source location must be reviewed"}
    return {"outcome": "UNSUPPORTED_OR_ERROR", "reason": "no complete recognized verification result"}


def python_proof_errors(root: Path, obligation: dict, result: dict) -> list[str]:
    """Admitted backend names alone cannot promote Python proof claims.

    The shared catalog must pin an actually qualified producer before any Python
    result can pass. There are no qualified proof producers in the initial A09
    integration; qualification receipts explicitly retain this limitation.
    """
    if obligation.get("backend") not in {"nagini", "esbmc-python", "deal"}:
        return []
    catalog = read_json(root / "Roadmaps/Shared/python-backends.json")
    key = {"nagini": "Nagini", "esbmc-python": "ESBMC-Python", "deal": "Deal"}[obligation["backend"]]
    entry = next((b for b in catalog["backends"] if b["name"] == key), {})
    errors = []
    binding = entry.get("qualified_producer")
    if entry.get("status") != "QUALIFIED" or not binding or not bindings_current(root, [binding]):
        return ["Python backend has no current source-bound qualified proof producer"]
    qualification = read_json(confined_path(root, binding["path"]))
    # Promotion needs an implemented, reviewed execution/result adapter. Merely
    # changing the matrix status or writing a qualification JSON is insufficient.
    errors.append("Python proof execution/result adapter is not qualified for domain acceptance")
    if result.get("python_qualification") != binding or qualification.get("toolchain") != obligation.get("toolchain"):
        errors.append("Python qualification/toolchain identity mismatched")
    return errors
