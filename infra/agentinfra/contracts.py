"""Candle contracts are original HOL4 source references, never test definitions."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

from .security import confined_path

FRAMEWORK = Path(__file__).resolve().parents[2]
IDENT = re.compile(r"[a-z][a-z0-9_-]{0,63}\Z")
RUST_PATH = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*\Z")
METHODS = {"kani", "verus"}


class ContractError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ContractError(message)


def digest(value):
    data = value if isinstance(value, bytes) else json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    def unique(items):
        result = {}
        for k, v in items:
            require(k not in result, f"duplicate JSON key: {k}")
            result[k] = v
        return result
    return json.loads(Path(path).read_text(), object_pairs_hook=unique,
                      parse_constant=lambda s: require(False, f"non-finite JSON: {s}"))


def keys(obj, expected, label):
    require(type(obj) is dict and set(obj) == set(expected.split()), f"{label}: expected fields {expected}")


def nonempty(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label} must be nonempty")
    return value


def relative(value):
    nonempty(value, "path")
    p = Path(value)
    require(not p.is_absolute() and p.as_posix() == value and all(x not in {".", "..", ""} for x in value.split("/")), "noncanonical relative path")
    require(p.parts[0] not in {".git", ".aegis", "target"} and not value.startswith(".candle/evidence/"), "path is runtime/output, not an input")
    return value


def git(root, *args):
    p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, timeout=30, check=False)
    require(p.returncode == 0, f"git {args[0]} failed: {p.stderr.decode(errors='replace')[:300]}")
    return p.stdout


def authority():
    return read_json(FRAMEWORK / "contracts/authority.json")


def authority_digest():
    return digest((FRAMEWORK / "contracts/authority.json").read_bytes())


def validate_plan(plan):
    keys(plan, "schema task authority_sha256 paper_sections reuse adr remote obligations", "plan")
    require(type(plan["schema"]) is int and plan["schema"] == 1, "unsupported plan schema")
    require(isinstance(plan["task"], str) and IDENT.fullmatch(plan["task"]), "invalid task id")
    require(plan["authority_sha256"] == authority_digest(), "authority lock differs; resolve original-source changes explicitly")
    require(type(plan["paper_sections"]) is list and len(plan["paper_sections"]) > 0, "paper sections required")
    for section in plan["paper_sections"]:
        nonempty(section, "paper section")
    relative(plan["adr"])
    reuse = plan["reuse"]
    keys(reuse, "strategy sources license reason generator", "reuse decision")
    require(reuse["strategy"] in {"reuse", "generate", "handwrite"}, "unknown reuse strategy")
    for field in ("license", "reason"):
        nonempty(reuse[field], f"reuse.{field}")
    require(type(reuse["sources"]) is list, "reuse.sources must be a list")
    for source in reuse["sources"]:
        nonempty(source, "reuse source")
    require(reuse["sources"] or reuse["strategy"] == "handwrite", "reuse/generation requires provenance")
    require(type(reuse["generator"]) is list and all(isinstance(a, str) and a for a in reuse["generator"]), "generator must be argv")
    require(reuse["strategy"] != "generate" or reuse["generator"], "generation requires a reproducible recipe")
    # The justification is a reviewable decision, not a machine-verifiable cost claim.
    keys(plan["remote"], "repository base", "remote")
    require(re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", plan["remote"]["repository"] or ""), "invalid GitHub repository")
    require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_./-]*", plan["remote"]["base"] or ""), "invalid base branch")
    require(type(plan["obligations"]) is list and plan["obligations"], "nonempty obligation set required")
    anchors = {s["path"] for s in authority()["specifications"]}
    ids = set()
    for o in plan["obligations"]:
        keys(o, "id anchor symbol statement rust_paths method entry expected_checks assumptions limits", "obligation")
        require(isinstance(o["id"], str) and IDENT.fullmatch(o["id"]) and o["id"] not in ids, "invalid/duplicate obligation id")
        ids.add(o["id"])
        require(o["anchor"] in anchors, "obligation needs an original specification anchor")
        require(isinstance(o["symbol"], str) and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_']*", o["symbol"]), "invalid HOL4 symbol")
        nonempty(o["statement"], "refinement statement")
        require(type(o["rust_paths"]) is list and o["rust_paths"] and len(set(o["rust_paths"])) == len(o["rust_paths"]), "nonempty unique Rust input paths required")
        for p in o["rust_paths"]:
            relative(p)
            require(p.endswith(".rs"), "Rust obligations must name Rust files")
        require(o["method"] in METHODS, "only Kani/Verus evidence adapters are supported")
        require(type(o["expected_checks"]) is int and o["expected_checks"] > 0, "expected_checks must be positive")
        if o["method"] == "kani":
            require(isinstance(o["entry"], str) and RUST_PATH.fullmatch(o["entry"]), "invalid exact Kani harness")
            require(o["expected_checks"] == 1, "each Kani obligation binds one exact harness")
        else:
            require(o["entry"] in o["rust_paths"], "Verus entry must be a declared Rust input")
        for field in ("assumptions", "limits"):
            require(type(o[field]) is list and o[field], f"explicit {field} required (use 'none known' only if justified)")
            for item in o[field]:
                nonempty(item, field)
    require("REPLACE:" not in json.dumps(plan), "template placeholders must be resolved before binding")
    return plan


def verify_references(plan, roots):
    lock = authority()
    require(set(roots) == {r["id"] for r in lock["repositories"]}, "both pinned original repositories required")
    for ref in lock["repositories"]:
        root = Path(roots[ref["id"]]).resolve(strict=True)
        require(git(root, "rev-parse", "HEAD").decode().strip() == ref["commit"], f"wrong {ref['id']} revision")
        require(not git(root, "status", "--porcelain", "--untracked-files=all"), f"{ref['id']} reference checkout is dirty")
    for spec in lock["specifications"]:
        root = Path(roots[spec["repository"]])
        path = confined_path(root, spec["path"], must_exist=True)
        require(digest(path.read_bytes()) == spec["sha256"], f"original specification bytes changed: {spec['path']}")
        require(git(root, "rev-parse", f"HEAD:{spec['path']}").decode().strip() == spec["git_blob"], "original blob mismatch")
    for o in plan["obligations"]:
        content = confined_path(Path(roots["cakeml"]), o["anchor"], must_exist=True).read_text()
        require(re.search(r"(?:Definition|Theorem)\s+" + re.escape(o["symbol"]) + r"\b", content), f"HOL4 symbol absent: {o['symbol']}")
    return {r["id"]: r["commit"] for r in lock["repositories"]}


def source_snapshot(root):
    root = Path(root).resolve(strict=True)
    require(Path(git(root, "rev-parse", "--show-toplevel").decode().strip()).resolve() == root, "root must be repository root")
    names = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard").decode().split("\0")
    entries = {}
    for name in sorted(set(names) - {""}):
        if name.startswith((".aegis/", ".candle/evidence/")):
            continue
        p = confined_path(root, name, must_exist=True)
        require(p.is_file(), f"input is not a regular file (submodules require an explicit binding): {name}")
        entries[name] = {"sha256": digest(p.read_bytes()), "executable": bool(p.stat().st_mode & 0o111)}
    return {"digest": digest(entries), "entries": entries}


def framework_digest():
    files = {}
    for folder in ("infra/agentinfra", "contracts"):
        for p in sorted((FRAMEWORK / folder).rglob("*")):
            if p.is_file() and "__pycache__" not in p.parts:
                files[p.relative_to(FRAMEWORK).as_posix()] = digest(p.read_bytes())
    return digest(files)
