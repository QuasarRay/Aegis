"""Installed native protocol identities and schema-bound read-only adapters.

The installed executable exports the schemas. A manifest pins their complete
bytes; it is not an implementation of the JSON Schema language or proof of a
server capability. Real RPC observations supply capability evidence separately.
"""
from __future__ import annotations

from pathlib import Path
import shutil

from .roadmap_records import bindings_current, digest, file_binding, read_json, require
from .security import confined_path


INTERFACE_VERSION = 1
REQUIRED_SCHEMAS = (
    "InitializeParams.json", "InitializeResponse.json", "ModelListParams.json", "ModelListResponse.json",
    "ThreadReadParams.json", "ThreadReadResponse.json", "ThreadTurnsListParams.json", "ThreadTurnsListResponse.json",
    "ThreadItemsListParams.json", "ThreadItemsListResponse.json", "ThreadListParams.json", "ThreadListResponse.json",
    "CollaborationModeListParams.json", "CollaborationModeListResponse.json",
    "ThreadGoalGetParams.json", "ThreadGoalGetResponse.json", "ThreadGoalSetParams.json", "ThreadGoalSetResponse.json",
    "ThreadGoalClearParams.json", "ThreadGoalClearResponse.json", "TurnPlanUpdatedNotification.json",
    "ThreadTokenUsageUpdatedNotification.json", "TurnCompletedNotification.json",
    "ModelReroutedNotification.json", "TurnStartedNotification.json", "ItemCompletedNotification.json",
    "ThreadResumeParams.json", "ThreadResumeResponse.json", "TurnStartParams.json", "TurnStartResponse.json",
    "TurnSteerParams.json", "TurnSteerResponse.json", "TurnInterruptParams.json", "TurnInterruptResponse.json",
    "ThreadStatusChangedNotification.json", "ErrorNotification.json",
)


def native_executable() -> dict:
    executable = shutil.which("codex")
    require(bool(executable), "installed Codex executable unavailable")
    path = Path(executable).resolve()
    return {"path": str(path), "sha256": digest(path.read_bytes())}


def export_manifest(root: Path, relative: str, executable: dict) -> dict:
    require(native_executable() == executable, "native executable changed during schema export")
    directory = confined_path(root, relative, must_exist=True)
    files = []
    total_bytes = 0
    for path in sorted(directory.rglob("*.json")):
        binding = file_binding(root, path.relative_to(root).as_posix())
        size = path.stat().st_size
        total_bytes += size
        require(size <= 16_000_000 and total_bytes <= 100_000_000 and len(files) < 5000,
                "native protocol export exceeds inspection bounds")
        require(isinstance(read_json(path), dict), "native schema export must contain objects")
        files.append(binding)
    require(bool(files), "native protocol export is empty")
    selected = {}
    for name in REQUIRED_SCHEMAS:
        matches = [b for b in files if Path(b["path"]).name == name]
        v2 = [b for b in matches if "/v2/" in b["path"]]
        choices = v2 or matches
        require(len(choices) == 1, f"required native protocol schema missing or ambiguous: {name}")
        selected[name.removesuffix(".json")] = choices[0]
    result = {"schema": INTERFACE_VERSION, "kind": "installed_codex_protocol_export", "executable": executable,
              "export_directory": directory.relative_to(root).as_posix(),
              "files": files, "selected": selected, "bytes": total_bytes, "experimental": True,
              "limits": ["Exported contracts identify this installed executable",
                         "An exported method does not establish live support, entitlement or successful execution"]}
    result["definitions"] = {}
    for name, source in (("ThreadItem", "ThreadItemsListResponse"), ("Turn", "ThreadTurnsListResponse")):
        binding = selected[source]
        document = read_json(confined_path(root, binding["path"]))
        require(name in document.get("definitions", {}), f"required native definition missing: {name}")
        result["definitions"][name] = {"schema_file": binding, "pointer": "/definitions/" + name,
                                       "sha256": digest(document["definitions"][name])}
    result["digest"] = digest(result)
    return result


def assert_protocol(root: Path, manifest: dict) -> None:
    require(manifest.get("schema") == INTERFACE_VERSION and
            manifest.get("kind") == "installed_codex_protocol_export" and
            manifest.get("digest") == digest({k: v for k, v in manifest.items() if k != "digest"}),
            "unknown or corrupt native protocol manifest")
    require(native_executable() == manifest["executable"] and bindings_current(root, manifest["files"]),
            "native executable/protocol contracts changed")
    directory = confined_path(root, manifest["export_directory"], must_exist=True)
    require({p.relative_to(root).as_posix() for p in directory.rglob("*.json")} == {b["path"] for b in manifest["files"]},
            "native protocol namespace changed")
