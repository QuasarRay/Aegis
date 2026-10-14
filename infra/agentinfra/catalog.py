"""Bounded original-test packets for faithful, reuse-first Kani implementation.

Read original source as data from the catalog's immutable Git revision. Never
execute it or infer that a source marker proves correspondence.
"""
from __future__ import annotations

import ast
from collections import Counter
import json
from pathlib import Path
import re
import subprocess

from .atomic import atomic_write_json
from .destiny_reuse import digest, load_json, require
from .locks import FileLock
from .security import confined_path, minimal_subprocess_env

FRAMEWORK = Path(__file__).resolve().parents[2]
# Same catalog grammar as Destiny's existing proof_coverage.py, preserving duplicates.
FILE_RE = re.compile(r'file!\("([^"]+)"\s*=>\s*\[(.*?)\]\)', re.S)
STRING_RE = re.compile(r'"([^"]+)"')
MARKER = "// original-test: "
QUALIFIED_MARKER = "// original-case: "


def inventory(root):
    path = confined_path(root, "verification/spec/src/catalog.rs", must_exist=True)
    require(path.stat().st_size <= 256_000, "catalog exceeds bounded input size")
    rows = [(source, name) for source, body in FILE_RE.findall(path.read_text()) for name in STRING_RE.findall(body)]
    require(rows, "unrecognized or empty original-test catalog")
    return Counter(f"{source}::{name}" for source, name in rows)


def existing(root):
    found = {}
    base = confined_path(root, "verification/kani")
    for path in sorted(base.rglob("*.rs")):
        path = confined_path(root, path, must_exist=True)
        require(path.stat().st_size <= 512_000, "Kani source exceeds bounded index size")
        for number, line in enumerate(path.read_text().splitlines(), 1):
            prefix = next((p for p in (QUALIFIED_MARKER, MARKER) if line.strip().startswith(p)), None)
            if prefix:
                name = line.strip()[len(prefix):]
                found.setdefault(name, []).append({"path": path.relative_to(root).as_posix(), "line": number})
    return found


def search(root, args):
    require(1 <= args.limit <= 20 and args.offset >= 0, "limit must be 1..20 and offset nonnegative")
    rows, marked = qualified_index(root, getattr(args, "original", None)), existing(root)
    selected = []
    for row in rows:
        candidates, ambiguous = candidates_for(row, marked)
        if args.query.casefold() in row["id"].casefold() and (not args.unmarked or not candidates):
            selected.append({**row, "existing_kani_markers": candidates, "ambiguous_markers": ambiguous})
    return {"status": "CATALOG", "occurrences": len(rows), "qualified_identities": len({r["id"] for r in rows}),
            "matching_obligations": len(selected), "next_offset": args.offset + args.limit if args.offset + args.limit < len(selected) else None,
            "cases": selected[args.offset:args.offset + args.limit],
            "notice": "Each original fixture has its own identity. Ambiguous legacy markers discharge no fixture obligation."}


def qualify(counts, read_original):
    """Join every catalog occurrence to its actual fixture; fail if multiplicities differ."""
    result, used = [], set()
    for source in sorted({key.rsplit("::", 1)[0] for key in counts}):
        text = read_original(source)
        definitions = {}
        if source.endswith(".py"):
            tree = ast.parse(text, filename=source)
            for cls in tree.body:
                if isinstance(cls, ast.ClassDef):
                    for node in cls.body:
                        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            definitions.setdefault(node.name, []).append((cls.name, node.lineno))
        else:
            for match in re.finditer(r'\bTEST(?:_F|_P)?\s*\(\s*(\w+)\s*,\s*(\w+)\s*\)', text):
                definitions.setdefault(match[2], []).append((match[1], text.count("\n", 0, match.start()) + 1))
        for key, count in counts.items():
            path, name = key.rsplit("::", 1)
            if path != source:
                continue
            fixtures = definitions.get(name, [])
            require(len(fixtures) == count, f"catalog/source multiplicity differs for {key}: catalog {count}, source {len(fixtures)}")
            for fixture, line in fixtures:
                identity = f"{source}::{fixture}::{name}"
                require(identity not in used, f"duplicate qualified identity in original source: {identity}")
                used.add(identity)
                result.append({"id": identity, "source": source, "fixture": fixture, "test": name, "line": line,
                               "legacy_marker": key, "legacy_multiplicity": count, "original_source_sha256": digest(text.encode())})
    require(len(result) == sum(counts.values()), "an original occurrence was lost during fixture qualification")
    return sorted(result, key=lambda r: r["id"])


def qualified_index(root, original=None):
    from .destiny import state_path
    authority = load_json((FRAMEWORK / "contracts/destiny.json").read_text())
    revision = authority["original_catalog_commit"]
    counts = inventory(root)
    require(sum(counts.values()) == authority["original_occurrences"] and digest(dict(counts)) == authority["catalog_occurrences_sha256"],
            "catalog differs from the pinned 531 occurrences; review the authority before changing the inventory")
    catalog = confined_path(root, "verification/spec/src/catalog.rs", must_exist=True)
    key = digest({"catalog": digest(catalog.read_bytes()), "revision": revision, "reader": digest(Path(__file__).read_bytes())})
    path = state_path(root, f"catalog/{key}.json")
    if path.exists():
        cached = load_json(path.read_text())
        require(cached["key"] == key and digest(cached["rows"]) == cached["sha256"], "qualified catalog cache integrity differs")
        return cached["rows"]
    repo = (original or root).resolve(strict=True)
    rows = qualify(counts, lambda name: original_text(repo, revision, name))
    for row in rows:
        row["original_commit"] = revision
    atomic_write_json(path, {"key": key, "rows": rows, "sha256": digest(rows)})
    return rows


def candidates_for(row, marked):
    exact = marked.get(row["id"], [])
    legacy = marked.get(row["legacy_marker"], [])
    return (exact + legacy, []) if row["legacy_multiplicity"] == 1 else (exact, legacy)


def family(row):
    value = row["id"].lower()
    for label, terms in (
        ("formation", ("formation",)), ("network", ("network", "packet", "marshal")),
        ("callbacks", ("callback", "proximity", "sensor")), ("collision", ("collision", "collide", "miniball", "minicapsule")),
        ("geometry", ("vector", "aabb", "plane", "triangle", "boxshape")),
        ("evolution", ("/evolve/", "orbit", "warp", "goto", "follow")),
        ("spatial-queries", ("bubble", "range", "cone", "capsule")),
        ("lifecycle", ("add", "remove", "destroy", "clear", "construct")),
    ):
        if any(t in value for t in terms):
            return label
    return "ball-state"


def work_queue(root, profile, args):
    from .destiny import environment, source_snapshot, state_path
    from . import formal
    import shutil
    snapshot = source_snapshot(root, profile["checks"]["proof-markers"]["read_globs"])
    rows, marked = qualified_index(root, getattr(args, "original", None)), existing(root)
    from .coverage import assurance, mappings
    case_mappings = mappings(root, rows)
    proof_rows, blockers = formal.proof_inventory(root, profile)
    output = []
    for row in rows:
        mapped, ambiguous = candidates_for(row, marked)
        proofs = [p for p in proof_rows if row["id"] in p.get("original_cases", [])]
        reviewed_mapping = case_mappings.get(row["id"])
        levels = {"mapped_or_marked": bool(mapped or proofs),
                  **assurance(reviewed_mapping, proofs),
                  "runtime_differential_evidence": False}
        output.append({**row, "semantic_family": family(row), "family_basis": "source/name classification, advisory",
                       "assurance": levels, "uncovered": not levels["production_rust_refinement_proved"],
                       "existing_proofs": proofs, "marked_candidates": mapped, "ambiguous_candidates": ambiguous,
                       "assertion_mapping": reviewed_mapping,
                       "gaps": [level for level, present in levels.items() if not present],
                       "blockers": (["legacy marker does not identify a unique fixture"] if ambiguous else []) +
                                   [p.get("blocker") or p["status"] for p in proofs if p["status"] != "CHECKED_SCOPED"]})
    # Optional runtime evidence is consumed separately and never promoted to a proof lane.
    if getattr(args, "differential", None):
        from .evidence import differential_cases
        by_id = {r["id"]: r for r in output}
        for record in differential_cases(root, profile, args.differential):
            require(record["case"] in by_id, "runtime mapping is not a fixture-qualified catalog identity")
            row = by_id[record["case"]]
            row["assurance"]["runtime_differential_evidence"] = True
            row["runtime_evidence"] = row.get("runtime_evidence", []) + [record]
            row["gaps"] = [g for g in row["gaps"] if g != "runtime_differential_evidence"]
    kani_missing = [t for t in ("cargo", "cargo-kani", "rustc") if shutil.which(t, path=environment(root, False).get("PATH")) is None]
    tools = {"kani": {"pinned_version": profile["checks"]["kani"]["expect"][0],
                       "status": "UNAVAILABLE" if kani_missing else "NOT_CHECKED", "missing": kani_missing}}
    if kani_missing:
        blockers.append("UNAVAILABLE: missing " + ", ".join(kani_missing))
    require(source_snapshot(root, profile["checks"]["proof-markers"]["read_globs"]) == snapshot, "target changed during queue generation")
    document = {"schema": 1, "status": "WORK_QUEUE", "original_commit": rows[0]["original_commit"],
                "source_identity": snapshot, "tools": tools, "obligations": output, "blockers": blockers,
                "unmapped_proofs": [p for p in proof_rows if not p.get("original_cases")],
                "assurance_rule": "Proof levels describe declared, freshly checked scope. Mapping is not proof; differential execution is not refinement proof."}
    path = confined_path(root, args.output) if args.output else state_path(root, "work-queue.json")
    atomic_write_json(path, document)
    return {"status": "WORK_QUEUE", "path": str(path), "obligations": len(output),
            "qualified_identities": len({r["id"] for r in output}),
            "uncovered": sum(r["uncovered"] for r in output), "blockers": blockers,
            "assurance_counts": {k: sum(r["assurance"][k] for r in output) for k in output[0]["assurance"]}}


def original_text(repo, revision, name):
    from .destiny import git, relative_path
    require(relative_path(name) == name, "noncanonical original source path")
    size = int(git(repo, "--no-replace-objects", "cat-file", "-s", f"{revision}:{name}").strip())
    require(size <= 512_000, "original source exceeds bounded inspection size; split the source review")
    # The generic process logger redacts text. Source extraction must retain exact
    # bytes, including assertion literals; immutable blob size is checked first.
    result = subprocess.run(["git", "--no-replace-objects", "-C", str(repo), "cat-file", "blob", f"{revision}:{name}"],
                            capture_output=True, timeout=15, env=minimal_subprocess_env({"GIT_TERMINAL_PROMPT": "0"}))
    require(result.returncode == 0 and len(result.stdout) == size, "cannot read exact pinned original blob")
    return result.stdout.decode("utf-8")


def python_case(source, name, fixture, read_original, completed=()):
    """Extract exact methods plus local/common helper dependencies, without running Python."""
    texts, trees = {}, {}

    def module(path):
        if path not in trees:
            texts[path] = read_original(path)
            trees[path] = ast.parse(texts[path], filename=path)
        return trees[path]

    tree = module(source)
    choices = [(cls, node) for cls in tree.body if isinstance(cls, ast.ClassDef)
               for node in cls.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name]
    selected = [(cls, node) for cls, node in choices if cls.name == fixture] if fixture else [
        (cls, node) for cls, node in choices if cls.name not in completed][:1]
    if choices and not selected and fixture is None:
        return {"status": "WORK_ALREADY_RECORDED", "fixtures": [cls.name for cls, _ in choices]}
    if len(selected) != 1:
        return {"status": "SOURCE_MAPPING_REQUIRED", "fixtures": [{"fixture": cls.name, "line": n.lineno} for cls, n in choices]}
    cls, method = selected[0]
    snippets, pending, visited, queue = [], set(), set(), [(source, method, "original case")]
    fixture_chain = []
    methods = {}

    def classes(path, current, seen=None):
        seen = set() if seen is None else seen
        key = (path, current.name)
        if key in seen:
            return
        seen.add(key)
        fixture_chain.append({"source": path, "class": current.name, "line": current.lineno,
                              "bases": [ast.unparse(base) for base in current.bases]})
        for node in current.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                methods.setdefault(node.name, (path, node))
                if node.name in {"setUp", "tearDown", "setUpClass", "tearDownClass", "__init__"}:
                    queue.append((path, node, "fixture lifecycle"))
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                queue.append((path, node, "fixture constants"))
        for base in current.bases:
            label = ast.unparse(base)
            if label in {"unittest.TestCase", "object"}:
                continue
            target, symbol = path, label
            if label.startswith("helpers."):
                target, symbol = "python/destiny/test/helpers.py", label.split(".", 1)[1]
            match = [n for n in module(target).body if isinstance(n, ast.ClassDef) and n.name == symbol]
            if match:
                classes(target, match[0], seen)
            else:
                pending.add(f"Review fixture base {label} in {path}")

    classes(source, cls)
    while queue:
        path, node, purpose = queue.pop(0)
        key = (path, node.lineno, node.end_lineno)
        if key in visited:
            continue
        require(len(visited) < 32, "dependency packet exceeds 32 definitions; split the work item")
        visited.add(key)
        start = min([node.lineno, *[d.lineno for d in getattr(node, "decorator_list", [])]])
        snippets.append({"path": path, "start": start, "end": node.end_lineno, "purpose": purpose,
                         "text": "\n".join(texts[path].splitlines()[start - 1:node.end_lineno])})
        names = {n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
        parents = {child: parent for parent in ast.walk(node) for child in ast.iter_child_nodes(parent)}
        for candidate in module(path).body:
            symbols = {candidate.name} if isinstance(candidate, (ast.FunctionDef, ast.ClassDef)) else {
                n.id for target in getattr(candidate, "targets", []) for n in ast.walk(target) if isinstance(n, ast.Name)}
            if symbols & names:
                if isinstance(candidate, ast.ClassDef) and any(
                    item["source"] == path and item["class"] == candidate.name for item in fixture_chain
                ):
                    references = [n for n in ast.walk(node) if isinstance(n, ast.Name)
                                  and isinstance(n.ctx, ast.Load) and n.id == candidate.name]
                    # super(Fixture, self) names the already-resolved fixture
                    # chain. Copying its entire class would pull unrelated
                    # cases into this packet and repeat lifecycle/helpers. Keep
                    # all other class uses (construction/static dispatch) whole.
                    if references and all(isinstance(parents.get(n), ast.Call)
                        and isinstance(parents[n].func, ast.Name) and parents[n].func.id == "super"
                        and parents[n].args and parents[n].args[0] is n for n in references):
                        continue
                queue.append((path, candidate, "local dependency"))
        for n in ast.walk(node):
            if not isinstance(n, ast.Attribute) or not isinstance(n.value, ast.Name):
                continue
            if n.value.id == "helpers":
                helper = "python/destiny/test/helpers.py"
                matches = [c for c in module(helper).body if getattr(c, "name", None) == n.attr
                           or any(isinstance(t, ast.Name) and t.id == n.attr for t in getattr(c, "targets", []))]
                if matches:
                    queue.extend((helper, c, "original helper dependency") for c in matches)
                else:
                    pending.add(f"Resolve helpers.{n.attr}")
            elif n.value.id == "self" and n.attr in methods:
                dependency_path, dependency = methods[n.attr]
                queue.append((dependency_path, dependency, "fixture helper"))
    imports = {path: [ast.get_source_segment(texts[path], n) for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))]
               for path, tree in trees.items()}
    assertions = sorted({n.lineno for n in ast.walk(method) if isinstance(n, ast.Assert)
                         or isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr.startswith("assert")})
    return {"status": "EXTRACTED", "fixture": cls.name, "fixture_chain": fixture_chain,
            "matching_original_definitions": len(choices), "available_fixtures": [c.name for c, _ in choices],
            "assertion_lines": assertions, "snippets": snippets, "imports": imports,
            "dependency_review": sorted(pending), "original_files": {p: digest(t.encode()) for p, t in texts.items()},
            "boundary": "Static dependency selection is advisory. Review imports, dynamic dispatch, stateful defaults and inheritance before translation."}


def cpp_case(source, name, fixture, read_original, completed=()):
    text = read_original(source)
    require('R"' not in text, "raw C++ strings need explicit source review before packet extraction")
    # Preserve offsets while ignoring braces in comments and ordinary string/character literals.
    masked = re.sub(r'//[^\n]*|/\*.*?\*/|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'',
                    lambda m: "".join("\n" if c == "\n" else " " for c in m[0]), text, flags=re.S)
    matches = list(re.finditer(r'\b(TEST(?:_F|_P)?)\s*\(\s*(\w+)\s*,\s*' + re.escape(name) + r'\s*\)', masked))
    selected = [m for m in matches if m[2] == fixture] if fixture else [m for m in matches if m[2] not in completed][:1]
    if matches and not selected and fixture is None:
        return {"status": "WORK_ALREADY_RECORDED", "fixtures": [m[2] for m in matches]}
    if len(selected) != 1:
        return {"status": "SOURCE_MAPPING_REQUIRED", "fixtures": [{"fixture": m[2], "line": text.count("\n", 0, m.start()) + 1} for m in matches]}
    match = selected[0]
    begin = masked.find("{", match.end())
    require(begin >= 0, "C++ case body missing")
    depth, end = 1, begin + 1
    while depth and end < len(masked):
        depth += (masked[end] == "{") - (masked[end] == "}")
        end += 1
    require(depth == 0, "C++ case body is unbalanced")
    start_line, end_line = text.count("\n", 0, match.start()) + 1, text.count("\n", 0, end) + 1
    excerpt = text[match.start():end]
    first_test = re.search(r'\bTEST(?:_F|_P)?\s*\(', masked)
    preamble = text[:first_test.start()].rstrip() if first_test else ""
    snippets = [{"path": source, "start": start_line, "end": end_line, "purpose": "original case", "text": excerpt}]
    if preamble:
        snippets.append({"path": source, "start": 1, "end": preamble.count("\n") + 1,
                         "purpose": "original fixture/helper declarations and includes", "text": preamble})
    dependencies = []
    if match[1] != "TEST":
        pending, seen = [match[2]], set()
        while pending:
            fixture_name = pending.pop()
            if fixture_name in seen or fixture_name in {"testing::Test", "::testing::Test"}:
                continue
            seen.add(fixture_name)
            declaration = re.search(r'\b(?:class|struct)\s+' + re.escape(fixture_name) + r'\s*(?::([^;{]+))?\s*\{', masked)
            if not declaration:
                dependencies.append(f"Resolve external fixture base {fixture_name}")
                continue
            depth, stop = 1, declaration.end()
            while depth and stop < len(masked):
                depth += (masked[stop] == "{") - (masked[stop] == "}")
                stop += 1
            require(depth == 0, "C++ fixture is unbalanced")
            if stop < len(text) and text[stop] == ";":
                stop += 1
            if declaration.start() >= len(preamble):
                snippets.append({"path": source, "start": text.count("\n", 0, declaration.start()) + 1,
                                 "end": text.count("\n", 0, stop) + 1, "purpose": "original fixture declaration",
                                 "text": text[declaration.start():stop]})
            for base in (declaration[1] or "").split(","):
                base = re.sub(r'\b(?:public|protected|private|virtual)\b', '', base).strip()
                if base:
                    pending.append(base)
    return {"status": "EXTRACTED", "fixture": match[2], "matching_original_definitions": len(matches),
            "assertion_lines": [start_line + i for i, line in enumerate(excerpt.splitlines()) if re.search(r'\b(?:ASSERT|EXPECT)_\w+\s*\(', line)],
            "available_fixtures": [m[2] for m in matches],
            "snippets": snippets,
            "imports": {source: re.findall(r'^\s*#include[^\n]+', text, re.M)},
            "dependency_review": dependencies + ["Inspect included definitions, assertion macro semantics, numeric domains and fixture setup before translation."],
            "original_files": {source: digest(text.encode())}, "boundary": "This is source extraction, not a C++ semantic parser."}


def brief(root, profile, args):
    from .destiny import git, source_snapshot, state_path
    require(2000 <= args.max_bytes <= 32_000, "packet budget must be 2000..32000 bytes")
    require(not args.fresh or args.reason and args.reason.strip(), "fresh packet requires a concrete reason")
    rows = qualified_index(root, args.original)
    matches = [r for r in rows if r["id"] == args.case or r["legacy_marker"] == args.case]
    require(matches, "case is absent from the fixture-qualified original catalog")
    repo = (args.original or root).resolve(strict=True)
    authority = load_json((FRAMEWORK / "contracts/destiny.json").read_text())
    revision = authority["original_catalog_commit"]
    require(git(repo, "--no-replace-objects", "rev-parse", "--verify", revision + "^{commit}").strip() == revision, "catalog original revision is not available locally")
    lock = FileLock(state_path(root, "harness-focus.lock"), "one-harness-work-item")
    lock.acquire(timeout=0)
    try:
        focus_path = state_path(root, "harness-focus.json")
        focus = load_json(focus_path.read_text()) if focus_path.exists() else None
        if focus and focus["status"] == "OPEN" and focus["request"]["case"] not in {r["id"] for r in matches}:
            return {"status": "FOCUS_REQUIRED", "active": focus["request"],
                    "notice": "Finish, reuse or block the active work item with harness-close before opening another."}
        snapshot = source_snapshot(root, profile["checks"]["proof-markers"]["read_globs"])
        history_path = state_path(root, "harness-history.json")
        history = load_json(history_path.read_text()) if history_path.exists() else {}
        if focus and focus["status"] == "OPEN":
            row = next(r for r in matches if r["id"] == focus["request"]["case"])
        else:
            available = [r for r in matches if args.fresh or r["id"] not in history]
            if not available:
                return {"status": "WORK_ALREADY_RECORDED", "cases": [r["id"] for r in matches],
                        "notice": "Use the saved decisions; reopen only with --fresh --reason."}
            row = available[0]
        source, name = row["source"], row["test"]
        request = {"case": row["id"], "fixture": row["fixture"]}
        key = digest({"request": request, "original": revision, "source": snapshot,
                      "reader": digest(Path(__file__).read_bytes()), "max_bytes": args.max_bytes})
        packet_path = state_path(root, f"packets/{key}.json")
        if packet_path.exists() and not args.fresh:
            atomic_write_json(focus_path, {"status": "OPEN", "request": request, "packet": str(packet_path)})
            return {"status": "REUSED_PACKET", "packet": str(packet_path), "case": row["id"],
                    "notice": "Reuse the saved brief and previous decision. No proof or implementation was run."}
        if packet_path.exists() and args.fresh:
            attempts_path = state_path(root, f"packets/{key}.reads.json")
            attempts = load_json(attempts_path.read_text()) if attempts_path.exists() else {"fresh_reads": 0}
            require(attempts["fresh_reads"] < 1, "packet reread budget exhausted; inspect the saved decision instead")
            atomic_write_json(attempts_path, {"fresh_reads": attempts["fresh_reads"] + 1, "reason": args.reason})
        read_original = lambda path: original_text(repo, revision, path)
        extracted = (python_case if source.endswith(".py") else cpp_case)(source, name, row["fixture"], read_original)
        if extracted["status"] != "EXTRACTED":
            return {**extracted, "case": row["id"]}
        require(extracted["matching_original_definitions"] == row["legacy_multiplicity"], "catalog/source multiplicity differs; review the mapping instead of dropping an obligation")
        candidates, ambiguous = candidates_for(row, existing(root))
        packet = {"status": "HARNESS_BRIEF", "case": row["id"], "legacy_multiplicity": row["legacy_multiplicity"],
                  "original_commit": revision, "source_identity": snapshot, "original": extracted,
                  "existing_kani": candidates, "ambiguous_markers": ambiguous,
                  "next_action": "REVIEW_EXISTING_BEFORE_IMPLEMENTING" if candidates or ambiguous else "IMPLEMENT_ONE_CASE",
                  "fidelity": {
                      "preserve": ["fixture setup and defaults", "operation order and every assertion", "numeric widths, floating-point tolerances and failure behavior"],
                      "separate": "Retain the exact original scenario; put symbolic generalizations in a separate harness with justified bounds.",
                      "implementation_link": "Identify the production Rust call path. A harness that only calls destiny_original_spec is specification evidence, not concrete-runtime parity.",
                      "assumptions": "Do not turn missing implementation, assertion outcomes or unsupported behavior into kani::assume. Record every domain restriction and unwind justification.",
                      "coverage": "Map each original assertion line to a Rust assertion and each setup dependency to a representation/default. Mark unresolved mappings BLOCKED.",
                  },
                  "economy": {"context_bytes": args.max_bytes, "one_active_case": True, "exact_harness_only": True,
                              "initial_proof_seconds": profile["checks"]["kani"]["scoped_timeout"], "max_attempts_per_input": 2,
                              "stop": "Stop on missing prerequisites, unresolved mapping or a failed/timed-out attempt. Diagnose before retry; do not run an Aegis-wide suite."}}
        encoded = json.dumps(packet, indent=2, sort_keys=True).encode()
        if len(encoded) > args.max_bytes:
            return {"status": "PACKET_TOO_LARGE", "bytes": len(encoded), "budget": args.max_bytes,
                    "case": args.case, "notice": "Split dependency review or explicitly increase --max-bytes. No assertion was silently truncated."}
        require(source_snapshot(root, profile["checks"]["proof-markers"]["read_globs"]) == snapshot, "target inputs changed during packet preparation")
        atomic_write_json(packet_path, packet)
        atomic_write_json(focus_path, {"status": "OPEN", "request": request, "packet": str(packet_path)})
        return packet
    finally:
        lock.release()


def close(root, args):
    from .destiny import state_path
    require(args.note and 1 <= len(args.note.strip()) <= 2000, "record a bounded result or blocker before changing work items")
    lock = FileLock(state_path(root, "harness-focus.lock"), "one-harness-work-item")
    lock.acquire(timeout=0)
    try:
        path = state_path(root, "harness-focus.json")
        value = load_json(path.read_text())
        require(value["status"] == "OPEN", "no open harness work item")
        value.update(status="CLOSED", outcome=args.outcome, note=args.note)
        history_path = state_path(root, "harness-history.json")
        history = load_json(history_path.read_text()) if history_path.exists() else {}
        history.setdefault(value["request"]["case"], {})[value["request"]["fixture"]] = {
            "outcome": args.outcome, "note": args.note, "packet": value["packet"]}
        atomic_write_json(history_path, history)
        atomic_write_json(state_path(root, f"harness-decisions/{digest(value)}.json"), value)
        atomic_write_json(path, value)
        return {"status": "WORK_RECORDED", "case": value["request"], "outcome": args.outcome,
                "notice": "Progress record only; completion here is not proof evidence."}
    finally:
        lock.release()
