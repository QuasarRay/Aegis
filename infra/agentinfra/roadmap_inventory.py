"""Current authority, Git and component inventory for the A00 responsibility.

Snapshots retain every ref/tree and every tracked or untracked nonignored file.
Historical Python bodies are inspected once per Git blob. Their declaration
inventory is structural evidence; a candidate remains pending semantic review.
"""
from __future__ import annotations

import ast
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import time

from .process import run_process
from .roadmap import compile_roadmaps
from .roadmap_records import canonical, digest, loads, read_json, require
from .roadmap_project import ProjectAdapter
from .security import confined_path, minimal_subprocess_env
from .transaction import Mutation


class GitInventory:
    """Bounded reads of exact Git metadata and immutable source objects."""

    def __init__(self, root: Path, *, deadline: float | None = None):
        self.root = root.resolve()
        self.deadline = time.monotonic() + 600 if deadline is None else deadline
        self.executable = shutil.which("git")
        require(self.executable is not None, "Git is required for an authority inventory")

    def read(self, *arguments: str) -> str:
        remaining = self.deadline - time.monotonic()
        require(remaining > 0, "authority inventory exceeded its finite time budget")
        result = run_process([self.executable, *arguments], cwd=self.root,
                             timeout=min(30, remaining), capture_limit=16_000_000)
        require(result.returncode == 0 and not result.timed_out and
                not result.stdout_truncated and not result.stderr_truncated,
                f"Git inventory command failed or exceeded bounds: {arguments[0]}")
        # Process logs redact secrets. Never silently inventory altered metadata.
        require(digest(result.stdout.encode()) == result.stdout_sha256,
                "Git inventory metadata was redacted or not exact UTF-8")
        return result.stdout

    def blob(self, oid: str) -> bytes:
        require(len(oid) in {40, 64} and all(c in "0123456789abcdef" for c in oid),
                "invalid Git object identity")
        # Keep source bytes out of redacted logs, preserve encoding declarations,
        # and bound memory independently of the size of an old branch's blob.
        with tempfile.TemporaryFile() as output:
            remaining = self.deadline - time.monotonic()
            require(remaining > 0, "authority inventory exceeded its finite time budget")
            result = subprocess.run([self.executable, "cat-file", "blob", oid],
                                    cwd=self.root, stdout=output, stderr=subprocess.PIPE,
                                    timeout=min(30, remaining), env=minimal_subprocess_env())
            require(result.returncode == 0, "Git source blob could not be read")
            require(output.tell() <= 8_000_000, "source blob exceeds inspection bound")
            output.seek(0)
            return output.read()

    def refs(self) -> list[dict]:
        text = self.read("for-each-ref", "--format=%(refname)%00%(objectname)%00%(tree)",
                         "refs/heads", "refs/remotes")
        refs = []
        for line in text.splitlines():
            name, commit, tree = line.split("\0")
            require(bool(tree), f"branch does not identify a commit tree: {name}")
            refs.append({"ref": name, "commit": commit, "tree": tree})
        require(bool(refs), "no branch authorities found")
        return refs

    def tree(self, oid: str) -> list[dict]:
        entries = []
        for item in self.read("ls-tree", "-rz", "--full-tree", oid).split("\0"):
            if item:
                header, path = item.split("\t", 1)
                mode, kind, blob = header.split()
                entries.append({"path": path, "mode": mode, "type": kind, "oid": blob})
        return entries

    def remote_heads(self) -> list[dict]:
        return [{"ref": line.split("\t")[1], "commit": line.split("\t")[0]}
                for line in self.read("ls-remote", "--heads", "origin").splitlines()]

    def worktree(self, *, dirty_only: bool = False) -> dict:
        staged = {}
        for item in self.read("ls-files", "--stage", "-z").split("\0"):
            if not item:
                continue
            header, name = item.split("\t", 1)
            mode, oid, stage = header.split()
            staged.setdefault(name, []).append({"mode": mode, "oid": oid, "stage": stage})
        untracked = set(filter(None, self.read(
            "ls-files", "--others", "--exclude-standard", "-z").split("\0")))
        selected = set(staged)
        if dirty_only:
            selected = set(filter(None, self.read("diff", "--name-only", "--no-renames", "-z", "HEAD").split("\0")))
            selected.update(filter(None, self.read("diff", "--cached", "--name-only", "--no-renames", "-z", "HEAD").split("\0")))
        names = sorted(selected | untracked)
        files = []
        for name in names:
            path = self.root / name
            # A symlink's own bytes are source; its destination is never read.
            confined_path(self.root, path.parent, allow_root=True)
            entry = {"path": name, "index": staged.get(name, [])}
            if path.is_symlink():
                entry.update(kind="symlink", sha256=digest(os.fsencode(os.readlink(path))))
            elif not path.exists():
                entry.update(kind="missing")
            elif path.is_file():
                entry.update(kind="file", sha256=digest(path.read_bytes()),
                             executable=bool(path.stat().st_mode & stat.S_IXUSR))
            elif path.is_dir() and any(s["mode"] == "160000" for s in entry["index"]):
                nested = GitInventory(path, deadline=self.deadline)
                # An uninitialized gitlink is a retained reference, not a checkout.
                if (path / ".git").exists():
                    # The commit owns unchanged reference bytes; changed and
                    # untracked bytes need their own identities, including
                    # edits that leave the porcelain status text unchanged.
                    entry.update(kind="gitlink", checkout=nested.worktree(dirty_only=True))
                else:
                    entry.update(kind="uninitialized_gitlink")
            else:
                require(False, f"unsupported source file kind: {name}")
            files.append(entry)
        branch = self.read("rev-parse", "--abbrev-ref", "HEAD").strip()
        return {"branch": None if branch == "HEAD" else branch,
                "head": self.read("rev-parse", "HEAD").strip(),
                "status": self.read("status", "--porcelain=v1", "-z", "--untracked-files=all"),
                "files": files}


def inspect_python(raw: bytes, filename: str) -> dict:
    """Compile and enumerate all bodies, including nested and unused definitions."""
    try:
        tree = ast.parse(raw, filename=filename)
        compile(tree, filename, "exec")
    except (SyntaxError, UnicodeError, ValueError) as exc:
        return {"status": "UNSUPPORTED_BY_CURRENT_INTERPRETER", "error": type(exc).__name__,
                "line": getattr(exc, "lineno", None), "semantic_acceptance": False}
    definitions = []

    def visit(node: ast.AST, owner: str, route: str) -> None:
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            owner = owner + "::" + node.name
            definitions.append({"owner": owner, "route": route, "kind": type(node).__name__,
                                "lines": [node.lineno, node.end_lineno],
                                "ast_sha256": digest(ast.dump(node, include_attributes=False).encode())})
        for field, value in ast.iter_fields(node):
            if isinstance(value, ast.AST):
                visit(value, owner, route + "." + field)
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    if isinstance(child, ast.AST):
                        visit(child, owner, f"{route}.{field}[{index}]")

    visit(tree, "module", "root")
    return {"status": "STRUCTURALLY_INSPECTED", "definitions": definitions,
            "ast_sha256": digest(ast.dump(tree, include_attributes=False).encode()),
            "semantic_acceptance": False}


def authority_inventory(root: Path, *, remote: bool = False) -> dict:
    root = root.resolve()
    compiled = compile_roadmaps(root)
    git = GitInventory(root)
    refs, worktree = git.refs(), git.worktree()
    heads = git.remote_heads() if remote else None
    trees = {oid: git.tree(oid) for oid in sorted({r["tree"] for r in refs})}
    head_tree = git.read("rev-parse", "HEAD^{tree}").strip()
    if head_tree not in trees:
        trees[head_tree] = git.tree(head_tree)
    current_blobs = {e["path"]: e["oid"] for e in trees[head_tree] if e["type"] == "blob"}
    components = {}
    for tree_id, entries in trees.items():
        for entry in entries:
            if entry["type"] != "blob" or entry["mode"] == "120000" or not entry["path"].endswith(".py"):
                continue
            oid = entry["oid"]
            if oid not in components:
                raw = git.blob(oid)
                components[oid] = {"oid": oid, "sha256": digest(raw), "paths": [], "trees": [],
                                   "inspection": inspect_python(raw, entry["path"])}
            item = components[oid]
            if entry["path"] not in item["paths"]:
                item["paths"].append(entry["path"])
            if tree_id not in item["trees"]:
                item["trees"].append(tree_id)
    for item in components.values():
        item["paths"].sort()
        item["trees"].sort()
        item["current_paths"] = [p for p in item["paths"] if current_blobs.get(p) == item["oid"]]
        item["disposition"] = ("PRESERVE_CURRENT_IMPLEMENTATION" if item["current_paths"]
                               else "RETAIN_PENDING_SEMANTIC_REVIEW_BEFORE_REUSE")
    working_components = []
    for file in worktree["files"]:
        if file["kind"] == "file" and file["path"].endswith(".py"):
            raw = confined_path(root, file["path"], must_exist=True).read_bytes()
            require(digest(raw) == file["sha256"], "working source changed during body inspection")
            working_components.append({"path": file["path"], "sha256": file["sha256"],
                                       "inspection": inspect_python(raw, file["path"])})
    missing = [] if heads is None else [h for h in heads if not any(
        r["ref"] == "refs/remotes/origin/" + h["ref"].removeprefix("refs/heads/") and
        r["commit"] == h["commit"] for r in refs)]
    require(refs == git.refs() and worktree == git.worktree(),
            "source, index or branch authorities changed during inventory")
    if remote:
        require(heads == git.remote_heads(), "remote heads changed during inventory")
    require(compiled == compile_roadmaps(root), "roadmap authorities changed during inventory")
    record = {"schema": 1, "kind": "aegis_authority_inventory", "compiled_digest": compiled["digest"],
              "git": {"version": git.read("--version").strip(),
                      "executable_sha256": digest(Path(git.executable).read_bytes())},
              "python": {"version": sys.version, "executable_sha256": digest(Path(sys.executable).read_bytes())},
              "authorities": read_json(root / "Roadmaps/Shared/sources.json")["files"],
              "requirements": read_json(root / "Roadmaps/Shared/requirements.json")["requirements"],
              "refs": refs, "trees": trees, "components": [components[k] for k in sorted(components)],
              "worktree": worktree, "working_components": working_components,
              "remote_heads": heads, "unreconciled_remote_heads": missing,
              "preservation": {"source_mutations": [], "branch_mutations": [],
                               "historical_evidence": "retained under its original lineage",
                               "reuse_rule": "Review a candidate body and its dependencies before replacing a current component"},
              "limitations": ["Structural inspection is not semantic acceptance or domain proof",
                              "Reference gitlinks retain their own source and verification obligations",
                              "Python symlink references remain tree entries and are not treated as independent source bodies",
                              "Ignored runtime state is owned by its existing canonical record and budget ledger"]}
    record["digest"] = digest(record)
    return record


def save_inventory(root: Path, record: dict) -> dict:
    """CAS-update the registered canonical record and immutable snapshot together."""
    root = root.resolve()
    require(record.get("schema") == 1 and record.get("kind") == "aegis_authority_inventory" and
            digest({k: v for k, v in record.items() if k != "digest"}) == record.get("digest"),
            "invalid authority snapshot identity")
    compiled = compile_roadmaps(root)
    require(compiled["digest"] == record["compiled_digest"], "authority snapshot became stale")
    git = GitInventory(root)
    require(git.refs() == record["refs"] and git.worktree() == record["worktree"],
            "source or branches changed before authority snapshot publication")
    if record["remote_heads"] is not None:
        require(git.remote_heads() == record["remote_heads"], "remote heads changed before authority snapshot publication")
    adapter = ProjectAdapter(root, profiles=compiled["projects"])
    path = adapter.profile.path()
    before = path.read_bytes() if path.exists() else None
    current = loads(before.decode()) if before is not None else {"schema": 1, "project": "Aegis"}
    require(current.get("schema") == 1 and current.get("project") == "Aegis",
            "unknown canonical Aegis record; explicit migration required")
    relative = f".aegis/roadmaps/authority/{record['digest']}.json"
    snapshot = confined_path(root, relative)
    raw = canonical(record) + b"\n"
    require(not snapshot.exists() or snapshot.read_bytes() == raw, "immutable inventory snapshot collision")
    binding = {"path": relative, "sha256": digest(raw)}
    if current.get("authority_inventory") == binding:
        return {"status": "REUSED", "inventory": binding, "record": str(path)}
    adapter.update({"authority_inventory": binding}, allow_create=True,
                   expected_digest=digest(before) if before is not None else None,
                   artifacts=(Mutation(snapshot, raw, expected_exists=snapshot.exists(),
                                       expected_sha256=digest(raw) if snapshot.exists() else None),))
    return {"status": "RECORDED", "inventory": binding, "record": str(path)}


def reconcile_inventory(root: Path, record: dict) -> dict:
    """Reproduce the complete denominator instead of trusting snapshot counts."""
    current = authority_inventory(root, remote=record.get("remote_heads") is not None)
    require(current == record, "authority inventory differs from current sources, branches or configuration")
    require(not record["unreconciled_remote_heads"], "remote branches require fetch and inspection")
    require(all(c["inspection"]["status"] == "STRUCTURALLY_INSPECTED"
                for c in record["working_components"]), "current Python body cannot be compiled and inventoried")
    return {"schema": 1, "status": "RECONCILED", "inventory_digest": record["digest"],
            "requirements": len(record["requirements"]), "refs": len(record["refs"]),
            "trees": len(record["trees"]), "historical_python_blobs": len(record["components"]),
            "current_python_files": len(record["working_components"]),
            "domain_proof": False, "semantic_acceptance_of_historical_candidates": False}
