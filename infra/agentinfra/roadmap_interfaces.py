"""Read-only versioned module/API observations and structural compatibility.

The AST reader does not import target modules or execute retrieved source.
Signatures and schema structure are one evidence channel. Actual behavior,
effects and recovery still require unchanged original tests and domain proof.
"""
from __future__ import annotations

import ast
import importlib.util
from pathlib import Path
import sys

from .roadmap_inventory import GitInventory
from .roadmap_records import KEYWORDS, digest, file_binding, read_json, require
from .security import confined_path


INTERFACE_VERSION = 1
LAYERS = {
    "policy": {"roadmap_policy", "roadmap_scope", "governance", "security"},
    "execution": {"roadmap_runtime", "roadmap_work", "roadmap_lease", "roadmap_download", "roadmap_mirrors", "process", "locks", "atomic", "transaction"},
    "profiles": {"roadmap_project"},
    "evidence": {"roadmap_records", "roadmap_acceptance", "roadmap_verification", "roadmap_python", "roadmap_python_catalog", "evidence", "verus_evidence", "coverage", "formal"},
    "source": {"roadmap_inventory", "roadmap_portability", "roadmap_interfaces", "catalog", "context_cache"},
    "native": {"roadmap_codex", "roadmap_native", "roadmap_protocol", "roadmap_native_adapter", "roadmap_managed"},
    "knowledge": {"roadmap_knowledge"},
    "review": {"roadmap_review"},
    "entrypoint": {"cli", "roadmap_cli", "__main__"},
    "compiler": {"roadmap"},
    "legacy_destiny": {"destiny", "destiny_reuse", "paths"},
    "package": {"__init__"},
}


def _signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> dict:
    return {"kind": type(node).__name__, "parameters": ast.dump(node.args, include_attributes=False),
            "returns": ast.unparse(node.returns) if node.returns else None,
            "decorators": [ast.unparse(d) for d in node.decorator_list]}


def _public(name: str, *, method: bool = False) -> bool:
    return not name.startswith("_") or (method and name.startswith("__") and name.endswith("__"))


def _exports(tree: ast.Module) -> dict:
    exports = {}

    def visit(statements: list[ast.AST], guards: tuple[str, ...] = ()) -> None:
        for node in statements:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if _public(node.name):
                    exports.setdefault(node.name, []).append(dict(_signature(node), declaration_guards=list(guards)))
            elif isinstance(node, ast.ClassDef):
                if not _public(node.name):
                    continue
                methods = {}
                for method in node.body:
                    if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)) and _public(method.name, method=True):
                        methods.setdefault(method.name, []).append(_signature(method))
                fields = [{"name": n.target.id, "annotation": ast.unparse(n.annotation),
                           "default": ast.unparse(n.value) if n.value else None}
                          for n in node.body if isinstance(n, ast.AnnAssign) and
                          isinstance(n.target, ast.Name) and _public(n.target.id)]
                exports.setdefault(node.name, []).append({"kind": "ClassDef", "bases": [ast.unparse(n) for n in node.bases],
                                      "decorators": [ast.unparse(n) for n in node.decorator_list],
                                      "fields": fields, "methods": methods, "declaration_guards": list(guards)})
            else:
                # Retain conditional/module-level declarations without treating
                # a nested local function as another public module export.
                predicates = {key: ast.dump(getattr(node, key), include_attributes=False)
                              for key in ("test", "iter", "target", "type", "pattern", "guard")
                              if isinstance(getattr(node, key, None), ast.AST)}
                for field, value in ast.iter_fields(node):
                    context = guards + (f"{type(node).__name__}.{field}:{predicates}",)
                    if isinstance(value, list):
                        visit([n for n in value if isinstance(n, (ast.stmt, ast.ExceptHandler, ast.match_case))], context)
                    elif isinstance(value, (ast.stmt, ast.ExceptHandler, ast.match_case)):
                        visit([value], context)

    visit(tree.body)
    return exports


def _module(raw: bytes, path: str) -> dict:
    tree = ast.parse(raw, filename=path)
    compile(tree, path, "exec")
    key = path.removeprefix("infra/agentinfra/").removesuffix(".py").replace("/", ".")
    owners = [layer for layer, names in LAYERS.items() if key in names]
    require(len(owners) == 1, f"module responsibility is missing or ambiguous: {path}")
    name = "agentinfra" if key == "__init__" else "agentinfra." + key.removesuffix(".__init__")
    package = name if key.endswith("__init__") else name.rpartition(".")[0]
    dependencies = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            dependency = importlib.util.resolve_name("." * node.level + (node.module or ""), package) if node.level else node.module
            if dependency:
                dependencies.add(dependency)
        elif isinstance(node, ast.Import):
            dependencies.update(n.name for n in node.names)
    constants = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in {"INTERFACE_VERSION", "__version__"}:
                    constants[target.id] = ast.literal_eval(node.value)
    return {"module": name, "path": path, "layer": owners[0], "source_sha256": digest(raw),
            "exports": _exports(tree), "imports": sorted(dependencies), "declared_versions": constants}


def _schema_vocabulary(schema: dict) -> None:
    require(isinstance(schema, dict) and not set(schema) - KEYWORDS, "unsupported interface schema vocabulary")
    for collection in ("$defs", "properties"):
        for child in schema.get(collection, {}).values():
            _schema_vocabulary(child)
    for key in ("items", "additionalProperties"):
        if isinstance(schema.get(key), dict):
            _schema_vocabulary(schema[key])
    for child in schema.get("anyOf", []):
        _schema_vocabulary(child)


def observe_interfaces(root: Path) -> dict:
    root = root.resolve()
    paths = sorted((root / "infra/agentinfra").rglob("*.py"))
    require(bool(paths), "empty production module denominator")
    modules = [_module(confined_path(root, path, must_exist=True).read_bytes(), path.relative_to(root).as_posix()) for path in paths]
    package = next(m for m in modules if m["module"] == "agentinfra")
    require(type(package["declared_versions"].get("INTERFACE_VERSION")) is int and
            package["declared_versions"]["INTERFACE_VERSION"] == INTERFACE_VERSION,
            "unsupported or unversioned current module interface")
    schema_binding = file_binding(root, "Roadmaps/Shared/records.schema.json")
    schemas = read_json(root / "Roadmaps/Shared/records.schema.json")
    _schema_vocabulary(schemas)
    for name, definition in schemas["$defs"].items():
        version = definition.get("properties", {}).get("schema", {}).get("const")
        require(type(version) is int and version == 1,
                f"unsupported record interface version: {name}")
    for module in modules:
        require(file_binding(root, module["path"])["sha256"] == module["source_sha256"],
                "module bytes changed during interface observation")
    require(paths == sorted((root / "infra/agentinfra").rglob("*.py")), "module namespace changed during interface observation")
    require(schema_binding == file_binding(root, "Roadmaps/Shared/records.schema.json"),
            "record protocol changed during interface observation")
    result = {"schema": INTERFACE_VERSION, "kind": "module_interface_observation", "modules": modules,
              "toolchain": {"python": sys.version, "executable_sha256": digest(Path(sys.executable).read_bytes())},
              "record_protocols": schemas["$defs"],
              "schema_binding": schema_binding,
              "limits": ["AST-declared source-owned public APIs, including lifecycle methods; no target imports executed",
                         "Structural interfaces do not establish behavioral compatibility or domain correctness",
                         "Complete private and unused body coverage belongs to the Python/Rust source inventory"]}
    result["digest"] = digest(result)
    return result


def _compatible(previous: list[dict], current: list[dict]) -> bool:
    if len(previous) != len(current):
        return False
    for before, after in zip(previous, current):
        if before.get("kind") != "ClassDef":
            if before != after:
                return False
        else:
            if {k: v for k, v in before.items() if k != "methods"} != {k: v for k, v in after.items() if k != "methods"}:
                return False
            if any(after.get("methods", {}).get(name) != methods for name, methods in before["methods"].items()):
                return False
    return True


def compare_interfaces(root: Path, baseline_ref: str) -> dict:
    current = observe_interfaces(root)
    git = GitInventory(root)
    baseline = git.read("rev-parse", "--verify", "--end-of-options", baseline_ref + "^{commit}").strip()
    old = {}
    for entry in git.tree(baseline):
        if entry["path"].startswith("infra/agentinfra/") and entry["path"].endswith(".py") and entry["type"] == "blob":
            require(entry["mode"] != "120000", "baseline interface symlink needs explicit source ownership")
            value = _module(git.blob(entry["oid"]), entry["path"])
            old[value["module"]] = value
    require(bool(old), "empty baseline module denominator")
    now = {m["module"]: m for m in current["modules"]}
    changes = []
    for name, module in old.items():
        if name not in now:
            changes.append({"module": name, "change": "removed_module"})
            continue
        for exported, signature in module["exports"].items():
            candidate = now[name]["exports"].get(exported)
            if candidate is None:
                changes.append({"module": name, "export": exported, "change": "removed_export"})
            elif not _compatible(signature, candidate):
                changes.append({"module": name, "export": exported, "change": "changed_signature_or_class_shape"})
    old_schemas = git.blob(git.read("rev-parse", baseline + ":Roadmaps/Shared/records.schema.json").strip())
    from .roadmap_records import loads
    previous_protocols = loads(old_schemas.decode())["$defs"]
    for name, schema in previous_protocols.items():
        if current["record_protocols"].get(name) != schema:
            changes.append({"record": name, "change": "changed_serialized_record_contract"})
    return {"schema": INTERFACE_VERSION, "kind": "structural_compatibility_observation", "baseline_commit": baseline,
            "current_interface_digest": current["digest"], "baseline_modules": len(old),
            "current_modules": len(now), "structural_compatible": not changes, "changes": changes,
            "added_modules": sorted(set(now) - set(old)), "domain_proof": False,
            "limits": current["limits"]}
