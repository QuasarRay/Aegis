"""Fixed Deal ingestion observer for unchanged production-import controls.

This executes the pinned solver API, not a rewritten production model. Imported
AST inference and module/state semantics remain unqualified trust boundaries.
"""
from __future__ import annotations

import argparse
import ast
import importlib.metadata
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra"))

from agentinfra.atomic import atomic_write_json
from agentinfra.roadmap_python import source_closure
from agentinfra.roadmap_records import digest, file_binding, require
from agentinfra.security import confined_path


def observe(root: Path, relative: str) -> dict:
    allowed = {"verification/roadmap/python/policy_deal_positive.py": "original_budget_and_completion",
               "verification/roadmap/python/policy_deal_negative.py": "deliberately_wrong_budget_assertion"}
    require(relative in allowed, "fixture is outside the fixed Deal qualification controls")
    path = confined_path(root, relative, must_exist=True)
    source = ast.parse(path.read_bytes(), filename=relative)
    assertions = [{"span": [n.lineno, n.end_lineno], "ast_sha256": digest(ast.dump(n, include_attributes=False).encode())}
                  for n in ast.walk(source) if isinstance(n, ast.Assert)]
    record = {"schema": 1, "backend": "deal", "status": "UNSUPPORTED_OR_UNQUALIFIED", "domain_proof": False,
              "fixture": file_binding(root, relative), "source_assertions": assertions, "solver_results": [],
              "constraints": [], "skips": [], "assertion_reachability": "NOT_ESTABLISHED",
              "production": source_closure(root, "agentinfra.roadmap_policy:may_reserve"),
              "semantic_limit": "Actual function ASTs are inferred from the maintained module. Whole module initialization/state, external imports, numeric/bool semantics and original assertion/translation identities remain unqualified."}
    try:
        import astroid
        import z3
        from deal_solver import Theorem
        from deal_solver._exceptions import UnsupportedError

        record["versions"] = {name: importlib.metadata.version(name) for name in ("deal", "deal-solver", "astroid", "z3-solver")}
        record["z3_runtime_version"] = z3.get_version_string()
        module = astroid.MANAGER.ast_from_file(str(path))
        record["ast_module_file"] = file_binding(root, Path(module.file).resolve().relative_to(root).as_posix())
        policy = root / "infra/agentinfra/roadmap_policy.py"
        declarations = {n.name: n for n in ast.parse(policy.read_bytes()).body if isinstance(n, ast.FunctionDef)}
        imports = [alias.name for node in source.body if isinstance(node, ast.ImportFrom) and
                   node.module == "agentinfra.roadmap_policy" for alias in node.names]
        inferred_imports = []
        for name in imports:
            uses = [n for n in module.nodes_of_class(astroid.nodes.Name) if n.name == name and
                    isinstance(n.parent, astroid.nodes.Call) and n.parent.func is n]
            require(uses, "production import has no actual call in the fixed fixture")
            for use in uses:
                inferred = [n for n in use.infer() if isinstance(n, astroid.nodes.FunctionDef)]
                require(len(inferred) == 1 and inferred[0].name == name and Path(inferred[0].root().file).resolve() == policy and
                        inferred[0].fromlineno == declarations[name].lineno and inferred[0].tolineno == declarations[name].end_lineno,
                        "Deal inference did not select the exact maintained production declaration")
                inferred_imports.append({"name": name, "call_span": [use.lineno, use.end_lineno],
                                         "source": file_binding(root, policy.relative_to(root).as_posix()),
                                         "declaration_span": [inferred[0].fromlineno, inferred[0].tolineno]})
        record["inferred_production_calls"] = inferred_imports

        class ObservedTheorem(Theorem):
            @staticmethod
            def get_contracts(func):
                if func.decorators and func.decorators.nodes:
                    raise UnsupportedError("unqualified contract decorators", func.name)
                return iter(())

            @property
            def constraints(self):
                for constraint in super().constraints:
                    formula = constraint.condition.expr.sexpr()
                    require(len(record["constraints"]) < 128 and len(formula.encode()) <= 409600,
                            "qualification observer resource bound exceeded; no result credit")
                    record["constraints"].append({"description": constraint.description, "smt": formula,
                                                   "smt_sha256": digest(formula.encode())})
                    yield constraint

            def _prove(self, solver, descr):
                result = Theorem._prove(solver=solver, descr=descr)
                record["solver_results"].append({"description": descr, "conclusion": result.conclusion.name,
                                                  "error": str(result.error) if result.error else None,
                                                  "example": str(result.example) if result.example else None})
                return result

        # The pinned Deal implementation converts seconds to Z3 milliseconds.
        # Z3's supported zero setting disables its wall-clock timeout.
        theorems = list(ObservedTheorem.from_astroid(module=module, timeout=0.0))
        require([t.name for t in theorems] == [allowed[relative]], "Deal omitted/added/reordered qualification functions")
        theorem = theorems[0]
        proof = theorem.prove()
        record.update(status="OBSERVED_UNQUALIFIED", function=theorem.name,
                      proof={"conclusion": proof.conclusion.name, "description": proof.description,
                             "error": str(proof.error) if proof.error else None,
                             "example": str(proof.example) if proof.example else None},
                      skips=[str(x) for x in theorem._context.skips])
    except Exception as exc:
        record["error"] = {"type": type(exc).__name__, "message": str(exc)}
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    record = observe(ROOT, args.fixture)
    atomic_write_json(confined_path(ROOT, args.output), record, root=ROOT, mode=0o600)
    print({"backend": "deal", "status": record["status"], "domain_proof": False,
           "error": record.get("error"), "proof": record.get("proof")})


if __name__ == "__main__":
    main()
