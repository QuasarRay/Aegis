"""AST-complete Python behavioral inventory and explicit Rust migration proposals."""
from __future__ import annotations

import ast
from pathlib import Path

from .roadmap_records import digest, read_json, require


ROOTS = ("infra", "bin", "scripts", "verification/roadmap", "Roadmaps/Shared/ci")
PATTERNS = {
    "Module": "Rust module; explicit initialization function for module-level effects; no hidden import-time mutation",
    "ClassDef": "Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods",
    "FunctionDef": "fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order",
    "AsyncFunctionDef": "async fn with explicit cancellation/lifetime contract; preserve suspension and observable completion",
    "If": "if/else with explicit Python truth-value conversion and unchanged branch order",
    "For": "for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics",
    "AsyncFor": "async stream loop with explicit normal-exhaustion, cancellation and else semantics",
    "While": "while with explicit truth conversion and a normal-exhaustion flag for loop else",
    "Try": "Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone",
    "TryStar": "typed exception-group partition/recombination; preserve simultaneous subgroup handling and propagation",
    "ExceptHandler": "match on source error enum preserving exception subtype matching and binding cleanup",
    "With": "scoped resource guard plus explicit enter/exit and exception-suppression result",
    "AsyncWith": "async enter/exit protocol with explicit awaited cleanup and cancellation outcomes",
    "Match": "match plus guards preserving Python structural pattern and binding semantics",
    "match_case": "ordered match arm with explicit guard and bound-name lifetime",
    "ListComp": "iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope",
    "SetComp": "source-compatible ordered evaluation into a set; preserve equality/hash behavior",
    "DictComp": "ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement",
    "GeneratorExp": "lazy iterator with captured environment and explicit exhaustion/error lifetime",
    "Lambda": "closure with explicit captures; preserve Python late binding and argument defaults",
    "Call": "typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors",
}
BLOCKS = tuple(getattr(ast, n) for n in PATTERNS if hasattr(ast, n))


def maintained_python(root: Path) -> list[Path]:
    return sorted({p for name in ROOTS for p in (root / name).rglob("*.py")
                   if "__pycache__" not in p.parts and not p.is_symlink()})


def inventory(root: Path) -> dict:
    files, units = [], []
    overrides_path = root / "Roadmaps/Shared/python-rust-overrides.json"
    overrides = read_json(overrides_path) if overrides_path.exists() else {"schema": 1, "units": {}}
    require(overrides.get("schema") == 1, "unknown Python/Rust mapping override schema")
    for path in maintained_python(root):
        relative = path.relative_to(root).as_posix()
        raw = path.read_bytes()
        tree = ast.parse(raw, filename=relative)
        files.append({"path": relative, "sha256": digest(raw)})
        imports = sorted({n.module or "" for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)} |
                         {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names})

        def visit(node: ast.AST, owner: str, route: str) -> None:
            next_owner = owner
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                next_owner = owner + "::" + node.name
            if isinstance(node, BLOCKS) or isinstance(node, ast.stmt):
                kind = type(node).__name__
                names_in = sorted({n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)})
                names_out = sorted({n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)})
                calls = sorted({ast.unparse(n.func) for n in ast.walk(node) if isinstance(n, ast.Call)})
                proposal = PATTERNS.get(kind, "Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects")
                effects = sorted({ast.unparse(n) for n in ast.walk(node)
                                  if isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.Delete, ast.Raise,
                                                    ast.Return, ast.Yield, ast.YieldFrom, ast.Await))})
                libraries = {"serde_json": "json", "std::fs / std::path::PathBuf": "pathlib",
                             "std::process::Command with explicit process-group owner": "subprocess",
                             "std::sync plus OS file locks": "threading", "regex": "re",
                             "sha2": "hashlib", "std::time::Instant / SystemTime": "time",
                             "clap": "argparse", "rustpython_parser or validated Python AST bridge": "ast"}
                invariant = "Preserve ordered " + kind + " evaluation at " + route + "; no call, error or mutation may be omitted."
                if isinstance(node, (ast.If, ast.While)):
                    invariant += " Condition: " + ast.unparse(node.test)
                if isinstance(node, (ast.For, ast.AsyncFor)):
                    invariant += " Iteration: " + ast.unparse(node.target) + " in " + ast.unparse(node.iter)
                unit = {"id": f"{relative}::{next_owner}::{route}::{kind}", "file": relative,
                              "source_sha256": digest(raw), "ast_sha256": digest(ast.dump(node, include_attributes=False).encode()),
                              "span": [getattr(node, "lineno", 1), getattr(node, "end_lineno", len(raw.splitlines()))],
                              "kind": kind, "inputs": names_in, "outputs": names_out, "calls": calls,
                              "effects": effects, "invariants": [invariant],
                              "rust_libraries": [lib for lib, source in libraries.items() if source in imports],
                              "dependencies": imports, "rust_module": relative.removesuffix(".py").replace("/", "::"),
                              "rust_equivalent": proposal,
                              "numeric_contract": "Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding",
                              "ownership_contract": "Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases",
                              "error_contract": "Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum",
                              "verification_required": ["current Python tests", "actual production Python proof where applicable", "future Rust correspondence and affected test/proof replay"],
                              "unresolved": ["Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement"],
                              "status": "PROPOSED_EQUIVALENT_NOT_IMPLEMENTED_OR_PROVED"}
                override = overrides["units"].get(unit["id"])
                if override:
                    require(override.get("ast_sha256") == unit["ast_sha256"] and override.get("source_sha256") == unit["source_sha256"], "reviewed migration mapping became stale")
                    fields = {"rust_equivalent", "ownership_contract", "error_contract", "numeric_contract", "invariants", "unresolved", "rust_libraries"}
                    require(set(override) <= fields | {"ast_sha256", "source_sha256", "review"} and override.get("review"), "invalid migration refinement")
                    unit.update({k: v for k, v in override.items() if k in fields})
                    unit["review"] = override["review"]
                units.append(unit)
            for field, value in ast.iter_fields(node):
                if isinstance(value, ast.AST):
                    visit(value, next_owner, f"{route}.{field}")
                elif isinstance(value, list):
                    for i, child in enumerate(value):
                        if isinstance(child, ast.AST):
                            visit(child, next_owner, f"{route}.{field}[{i}]")
        visit(tree, "module", "root")
    require(len({u["id"] for u in units}) == len(units), "duplicate Python behavioral unit")
    require(set(overrides["units"]) <= {u["id"] for u in units}, "migration refinement references removed Python unit")
    return {"schema": 1, "coverage": "all maintained files, definitions, statements and designated expression/handler blocks",
            "files": files, "units": units, "digest": digest({"files": files, "units": units})}


def markdown(record: dict) -> str:
    lines = ["# Python to Rust behavioral correspondence", "",
             "Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.", "",
             f"Files: {len(record['files'])}. Behavioral units: {len(record['units'])}. Inventory digest: `{record['digest']}`.", "",
             "Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.", ""]
    for unit in record["units"]:
        lines.extend([f"## {unit['id']}", "", f"Source: `{unit['file']}:{unit['span'][0]}`; AST `{unit['ast_sha256']}`.", "",
                      f"Rust module: `{unit['rust_module']}`. {unit['rust_equivalent']}", "",
                      f"Inputs: {', '.join(unit['inputs']) or '(none)'}. Outputs/bindings: {', '.join(unit['outputs']) or '(none)' }.",
                      f"Calls/effect boundaries: {', '.join(unit['calls']) or '(none)' }.",
                      f"Dependencies: {', '.join(unit['dependencies']) or '(none)' }.", "",
                      "Invariants: " + "; ".join(unit["invariants"]),
                      "Rust library candidates: " + "; ".join(unit["rust_libraries"] or ["standard Rust constructs; qualify external boundaries"]),
                      "Unresolved: " + "; ".join(unit["unresolved"]), "",
                      unit["numeric_contract"], unit["ownership_contract"], unit["error_contract"], "",
                      "Required evidence: " + "; ".join(unit["verification_required"]) + ".", ""])
    return "\n".join(lines)
