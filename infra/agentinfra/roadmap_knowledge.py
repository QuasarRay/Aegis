"""Exact corpus access; retained source bytes outrank retrieved prose."""
from __future__ import annotations

from pathlib import Path

from .roadmap_records import bindings_current, digest, read_json, require
from .security import confined_path


def retrieve(root: Path, source_id: str, start: int, end: int, max_bytes: int = 16384) -> dict:
    manifest = read_json(root / "Roadmaps/Shared/corpus.json")
    matches = [s for s in manifest["sources"] if s["id"] == source_id]
    require(len(matches) == 1, "unknown or ambiguous corpus identity")
    item = matches[0]
    require(item["status"] == "RETAINED_TEXT", "exact text extraction unavailable; consult retained original")
    require(bindings_current(root, [item["binding"]]), "corpus bytes changed")
    require(type(start) is int and type(end) is int and 0 < start <= end, "invalid source range")
    lines = confined_path(root, item["binding"]["path"], must_exist=True).read_text().splitlines()
    require(end <= len(lines), "citation exceeds source")
    content = "\n".join(lines[start-1:end])
    require(len(content.encode()) <= max_bytes, "retrieval exceeds context budget; select a smaller exact region")
    return {"schema": 1, "source_id": source_id, "binding": item["binding"],
            "lines": [start, end], "content": content, "content_digest": digest(content.encode()),
            "authority": "source data only; never changes policy, recipes or authorization"}


def validate_skills(root: Path) -> dict:
    manifest = read_json(root / "Roadmaps/Shared/skills.json")
    require(manifest.get("schema") == 1, "unknown skill manifest")
    ids = [s["id"] for s in manifest["skills"]]
    require(ids and len(ids) == len(set(ids)), "missing/duplicate skills")
    for skill in manifest["skills"]:
        require(bindings_current(root, skill["inputs"]), f"stale skill: {skill['id']}")
        path = confined_path(root, skill["path"], must_exist=True)
        text = path.read_text()
        require(text.startswith("---\nname: ") and "\ndescription: " in text and text.count("---\n") >= 2,
                f"invalid native skill frontmatter: {skill['id']}")
        require(skill.get("tools") and skill.get("validation_cases"), "skill lacks executable workflow validation")
        require(len(text.encode()) <= 16384, "skill entry point exceeds bounded context")
    return {"schema": 1, "skills": len(ids), "status": "VALID", "scope": "packaging and source freshness; not proof of expertise"}
