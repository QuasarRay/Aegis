"""AST-complete Python behavioral inventory and explicit Rust migration proposals."""
from __future__ import annotations

import ast
import json
from pathlib import Path

from .locks import FileLock
from .roadmap_records import ContractError, bindings_current, canonical, digest, loads, read_json, require
from .security import confined_path
from .transaction import FileTransaction, Mutation, TransactionError, recover_named_transactions


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
    raw_overrides = overrides_path.read_bytes() if overrides_path.exists() else None
    overrides = loads(raw_overrides.decode()) if raw_overrides is not None else {"schema": 1, "units": {}}
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
    record = {"schema": 1, "coverage": "all maintained files, definitions, statements and designated expression/handler blocks",
              "files": files, "units": units, "digest": digest({"files": files, "units": units}),
              "configuration": {"overrides_sha256": digest(raw_overrides) if raw_overrides is not None else None}}
    assert_sources(root, record)
    return record


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


def shards(record: dict, max_bytes: int = 262144) -> tuple[dict, dict[str, dict]]:
    """Stable per-source shards bounded by actual canonical UTF-8 file bytes."""
    require(type(max_bytes) is int and max_bytes > 0, "invalid inventory shard budget")
    parts, pending, ordinals = {}, [], {}
    group = None
    overhead = len(canonical({"schema": 1, "units": []})) + 1
    size = overhead

    def flush() -> None:
        nonlocal pending, size
        if not pending:
            return
        ordinal = ordinals.get(group, 0)
        name = f"units-{digest(group.encode())}-{ordinal:04}.json"
        value = {"schema": 1, "units": pending}
        require(name not in parts and len(canonical(value)) + 1 <= max_bytes,
                "inventory shard identity or byte bound violated")
        parts[name] = value
        ordinals[group] = ordinal + 1
        pending, size = [], overhead

    for unit in record["units"]:
        owner = unit.get("file", "")
        require(isinstance(owner, str), "invalid Python source owner")
        if owner != group:
            flush()
            group = owner
        length = len(canonical(unit))
        require(overhead + length <= max_bytes, "single behavioral entry exceeds shard budget; refine representation without dropping semantics")
        if pending and size + length + 1 > max_bytes:
            flush()
        size += length + (1 if pending else 0)
        pending.append(unit)
    flush()
    index = {"schema": 1, "kind": "sharded_python_rust_inventory", "coverage": record["coverage"],
             "layout": "source_shards_v1", "encoding": "canonical_utf8_json_lf", "shard_max_bytes": max_bytes,
             "files": record["files"], "unit_count": len(record["units"]), "digest": record["digest"],
             "shards": [{"path": "units/" + name, "digest": digest(value), "count": len(value["units"]),
                         "sha256": digest(canonical(value) + b"\n"), "bytes": len(canonical(value)) + 1}
                        for name, value in parts.items()]}
    return index, parts


def assert_sources(root: Path, record: dict) -> None:
    require([p.relative_to(root).as_posix() for p in maintained_python(root)] == [f["path"] for f in record["files"]]
            and (not record["files"] or bindings_current(root, record["files"])),
            "Python source namespace or bytes changed during generation")
    path = root / "Roadmaps/Shared/python-rust-overrides.json"
    expected = record.get("configuration", {}).get("overrides_sha256")
    require((digest(path.read_bytes()) if path.exists() else None) == expected,
            "Python/Rust override configuration changed during generation")


def file_record(record: dict, source: dict) -> dict:
    units = [u for u in record["units"] if u["file"] == source["path"]]
    return dict(record, files=[source], units=units, digest=digest({"files": [source], "units": units}))


def _document_path(source: str) -> str:
    return source.replace("/", "__") + ".md"


def artifacts(record: dict) -> tuple[dict, dict[str, bytes]]:
    index, parts = shards(record)
    output = {"units/" + name: canonical(value) + b"\n" for name, value in parts.items()}
    documents = []
    for source in record["files"]:
        path = _document_path(source["path"])
        require(path not in output, "Python correspondence document path collision")
        raw = markdown(file_record(record, source)).encode()
        output[path] = raw
        documents.append({"path": path, "source": source["path"], "sha256": digest(raw)})
    index["documents"] = documents
    index["configuration"] = record.get("configuration", {})
    output["inventory.json"] = canonical(index) + b"\n"
    return index, output


def _previous_artifacts(base: Path) -> dict[str, bytes]:
    path = base / "inventory.json"
    if not path.exists():
        return {}
    raw_index = path.read_bytes()
    index = loads(raw_index.decode())
    require(index.get("schema") == 1 and index.get("kind") == "sharded_python_rust_inventory",
            "unknown correspondence generation; explicit migration required")
    layout = index.get("layout")
    require(layout in {None, "source_shards_v1"}, "unsupported correspondence layout")
    owned, units = {"inventory.json": raw_index}, []
    for shard in index["shards"]:
        relative = shard["path"]
        require(relative.startswith("units/units-") and relative.endswith(".json") and relative not in owned,
                "invalid or duplicate owned inventory shard")
        raw = confined_path(base, relative, must_exist=True).read_bytes()
        value = loads(raw.decode())
        require(digest(value) == shard["digest"] and len(value["units"]) == shard["count"],
                "owned correspondence shard was edited; preserve and reconcile it before generation")
        expected = canonical(value) + b"\n" if layout else (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
        require(raw == expected, "owned correspondence shard bytes were edited")
        if layout:
            require(digest(raw) == shard["sha256"] and len(raw) == shard["bytes"] and
                    len(raw) <= index["shard_max_bytes"], "owned correspondence byte identity changed")
        units.extend(value["units"])
        owned[relative] = raw
    require(len(units) == index["unit_count"] and len({u["id"] for u in units}) == len(units) and
            digest({"files": index["files"], "units": units}) == index["digest"],
            "previous correspondence denominator is incomplete or duplicated")
    require({u["file"] for u in units} <= {f["path"] for f in index["files"]}, "unowned correspondence unit")
    previous = dict(index, units=units)
    for source in index["files"]:
        relative = _document_path(source["path"])
        require(relative not in owned, "previous correspondence document path collision")
        local = file_record(previous, source) if layout else dict(previous, files=[source], units=[u for u in units if u["file"] == source["path"]])
        expected = markdown(local).encode()
        raw = confined_path(base, relative, must_exist=True).read_bytes()
        require(raw == expected, "owned migration description was edited; preserve and reconcile it before generation")
        owned[relative] = raw
    return owned


def publish(root: Path, record: dict) -> dict:
    """CAS-publish owned artifacts with existing transaction recovery, index last."""
    root = root.resolve()
    base = root / "Roadmaps/Shared/python-rust"
    state = root / ".aegis/state/transactions"
    lock = FileLock(root / ".aegis/roadmaps/portability.lock", "correspondence generation")
    lock.acquire()
    try:
        recover_named_transactions(state, expected_root=root, names=["aegis-portability"])
        assert_sources(root, record)
        previous = _previous_artifacts(base)
        index, output = artifacts(record)
        mutations = []
        for relative in sorted(set(previous) | set(output)):
            if relative == "inventory.json":
                continue
            path = confined_path(root, base / relative)
            before = previous.get(relative)
            if before is None and path.exists():
                require(relative in output and path.read_bytes() == output[relative],
                        "unowned correspondence artifact conflicts with generation")
                before = path.read_bytes()
            after = output.get(relative)
            if before != after:
                mutations.append(Mutation(path, after, expected_exists=before is not None,
                                          expected_sha256=digest(before) if before is not None else None))
        old_index = previous.get("inventory.json")
        if old_index != output["inventory.json"]:
            mutations.append(Mutation(base / "inventory.json", output["inventory.json"],
                                      expected_exists=old_index is not None,
                                      expected_sha256=digest(old_index) if old_index is not None else None))
        assert_sources(root, record)
        if mutations:
            FileTransaction(root, mutations, state_dir=state, name="aegis-portability").commit()
        assert_sources(root, record)
        return {"files": len(record["files"]), "units": len(record["units"]), "shards": len(index["shards"]),
                "digest": record["digest"], "artifacts_changed": len(mutations),
                "status": "PUBLISHED" if mutations else "REUSED", "layout": index["layout"]}
    except TransactionError as exc:
        raise ContractError(f"correspondence transaction requires reconciliation: {exc}") from exc
    finally:
        lock.release()


def check(root: Path, record: dict) -> dict:
    assert_sources(root, record)
    _, expected = artifacts(record)
    base = root / "Roadmaps/Shared/python-rust"
    for relative, raw in expected.items():
        require(confined_path(root, base / relative, must_exist=True).read_bytes() == raw,
                "Python-to-Rust mapping is missing, stale or edited; regenerate and review changed blocks")
    assert_sources(root, record)
    return {"status": "CURRENT", "files": len(record["files"]), "units": len(record["units"])}
