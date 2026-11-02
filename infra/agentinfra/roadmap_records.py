"""Strict, dependency-free records for the executable roadmap package.

The supported JSON Schema vocabulary is deliberately finite. Unsupported keywords
fail instead of being ignored; these schemas are not a general schema interpreter.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .security import confined_path


class ContractError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                      allow_nan=False).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(value if isinstance(value, bytes) else canonical(value)).hexdigest()


def _pairs(pairs: list[tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def loads(text: str) -> Any:
    def bad_constant(value: str) -> None:
        raise ContractError(f"non-finite JSON constant: {value}")
    try:
        return json.loads(text, object_pairs_hook=_pairs, parse_constant=bad_constant)
    except (ValueError, TypeError) as exc:
        raise ContractError(str(exc)) from exc


def read_json(path: Path) -> Any:
    return loads(path.read_text(encoding="utf-8"))


KEYWORDS = {"$schema", "$id", "$defs", "$ref", "title", "description", "type", "enum",
            "const", "properties", "required", "additionalProperties", "items", "minItems",
            "uniqueItems", "minimum", "maximum", "minLength", "maxLength", "pattern",
            "anyOf"}


def validate(value: Any, schema: dict, *, root: dict | None = None, at: str = "$") -> None:
    root = schema if root is None else root
    require(isinstance(schema, dict), f"{at}: schema must be an object")
    require(not (set(schema) - KEYWORDS), f"{at}: unsupported schema keywords {set(schema) - KEYWORDS}")
    if "$ref" in schema:
        ref = schema["$ref"]
        require(isinstance(ref, str) and ref.startswith("#/$defs/"), "external schema references forbidden")
        name = ref.removeprefix("#/$defs/")
        require(name in root.get("$defs", {}), f"unknown schema definition: {name}")
        validate(value, root["$defs"][name], root=root, at=at)
    if "anyOf" in schema:
        failures = []
        for option in schema["anyOf"]:
            try:
                validate(value, option, root=root, at=at)
                break
            except ContractError as exc:
                failures.append(str(exc))
        else:
            raise ContractError(f"{at}: no schema alternative matched: {failures}")
    types = {"object": dict, "array": list, "string": str, "integer": int,
             "boolean": bool, "null": type(None)}
    if "type" in schema:
        expected = schema["type"]
        require(expected in types, f"unsupported schema type: {expected}")
        require(type(value) is types[expected], f"{at}: expected {expected}")
    if "const" in schema:
        require(type(value) is type(schema["const"]) and value == schema["const"], f"{at}: invalid constant")
    if "enum" in schema:
        require(any(type(value) is type(v) and value == v for v in schema["enum"]), f"{at}: unsupported value {value!r}")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        require(not (set(schema.get("required", [])) - set(value)), f"{at}: missing required fields")
        for key, item in value.items():
            if key in properties:
                validate(item, properties[key], root=root, at=f"{at}.{key}")
            elif schema.get("additionalProperties") is False:
                raise ContractError(f"{at}: unknown field {key}")
            elif isinstance(schema.get("additionalProperties"), dict):
                validate(item, schema["additionalProperties"], root=root, at=f"{at}.{key}")
    if isinstance(value, list):
        require(len(value) >= schema.get("minItems", 0), f"{at}: insufficient items")
        if schema.get("uniqueItems"):
            require(len({canonical(x) for x in value}) == len(value), f"{at}: duplicate items")
        for i, item in enumerate(value):
            if "items" in schema:
                validate(item, schema["items"], root=root, at=f"{at}[{i}]")
    if isinstance(value, str):
        require(len(value) >= schema.get("minLength", 0), f"{at}: empty/short string")
        require(len(value) <= schema.get("maxLength", len(value)), f"{at}: oversized string")
        if "pattern" in schema:
            require(re.search(schema["pattern"], value) is not None, f"{at}: pattern mismatch")
    if type(value) is int:
        require(schema.get("minimum", value) <= value <= schema.get("maximum", value), f"{at}: out of range")


def validate_record(root: Path, name: str, value: dict) -> None:
    schemas = read_json(root / "Roadmaps/Shared/records.schema.json")
    require(name in schemas["$defs"], f"unknown record type: {name}")
    validate(value, {"$ref": f"#/$defs/{name}"}, root=schemas)


def file_binding(root: Path, relative: str) -> dict:
    path = confined_path(root, relative, must_exist=True)
    require(path.is_file(), f"not a file: {relative}")
    return {"path": path.relative_to(root).as_posix(), "sha256": digest(path.read_bytes())}


def bindings_current(root: Path, bindings: list[dict]) -> bool:
    if not bindings:
        return False
    try:
        return all(file_binding(root, b["path"]) == b for b in bindings)
    except (OSError, KeyError, ValueError):
        return False
