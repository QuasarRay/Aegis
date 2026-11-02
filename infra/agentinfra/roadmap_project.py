"""Version-one project adapters over the registered canonical record owners.

This module composes the existing lease and FileTransaction implementations.
It owns neither a second queue nor a replacement recovery journal. Carbon
profiles remain read-only until their actual writer adapters are qualified.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .roadmap_lease import WorkspaceLease
from .roadmap_records import canonical, digest, loads, read_json, require, validate_record
from .security import confined_path
from .transaction import FileTransaction, Mutation


INTERFACE_VERSION = 1
AEGIS_RECORD_WRITER = "aegis-authority-inventory"


@dataclass(frozen=True)
class ProjectProfileV1:
    project: str
    declared_repository: str
    repository: Path
    branch: str
    canonical_record: str
    language_boundary: str

    @classmethod
    def from_registry(cls, root: Path, project: str, profiles: dict | None = None) -> ProjectProfileV1:
        root = root.resolve()
        profiles = read_json(root / "Roadmaps/Shared/registry.json")["projects"] if profiles is None else profiles
        require(project in profiles, "unknown registered project")
        profile = profiles[project]
        validate_record(root, "ProjectProfile", profile)
        require(profile["project"] == project, "project profile owner differs from its registry key")
        # --root relocates Aegis itself, including fixtures and deployed copies.
        # External projects retain their own explicitly declared repositories.
        repository = root if project == "Aegis" else Path(profile["repository"])
        return cls(project, profile["repository"], repository, profile["branch"],
                   profile["canonical_record"], profile["language_boundary"])

    def path(self) -> Path:
        return confined_path(self.repository, self.canonical_record)


class ProjectAdapter:
    def __init__(self, root: Path, project: str = "Aegis", *, profiles: dict | None = None):
        self.root = root.resolve()
        self.profile = ProjectProfileV1.from_registry(self.root, project, profiles)

    def read(self) -> dict:
        value = read_json(self.profile.path())
        require(isinstance(value, dict), "canonical project record must be an object")
        if self.profile.project == "Aegis":
            self._validate_aegis(value)
        return value

    @staticmethod
    def _validate_aegis(record: dict) -> None:
        require(type(record.get("schema")) is int and record["schema"] == 1 and
                record.get("project") == "Aegis", "unknown canonical Aegis record; explicit migration required")
        require(record.get("canonical_writer_transaction_name", AEGIS_RECORD_WRITER) == AEGIS_RECORD_WRITER,
                "canonical writer changed; reconcile its transaction lineage before adoption")

    def update(self, fields: dict, *, expected_digest: str | None,
               artifacts: tuple[Mutation, ...] = (), allow_create: bool = False) -> dict:
        require(self.profile.project == "Aegis", "external project writer requires its own qualified adoption")
        require(isinstance(fields, dict), "canonical update must be an object")
        path = self.profile.path()
        before = path.read_bytes() if path.exists() else None
        require(before is not None or allow_create, "canonical record does not exist")
        require((digest(before) if before is not None else None) == expected_digest,
                "canonical record changed before adapter update")
        current = loads(before.decode()) if before is not None else {"schema": 1, "project": "Aegis"}
        self._validate_aegis(current)
        require(fields.get("canonical_writer_transaction_name", AEGIS_RECORD_WRITER) == AEGIS_RECORD_WRITER,
                "generic updates cannot replace the canonical writer")
        updated = dict(current, **fields)
        updated["canonical_writer_transaction_name"] = AEGIS_RECORD_WRITER
        self._validate_aegis(updated)
        execution = current.get("execution") or updated.get("execution")
        if execution:
            owner = execution.get("workspace_lease", {})
            binding = execution.get("native_binding", {})
            require(owner.get("session") == binding.get("thread_id") and bool(owner.get("session")),
                    "canonical execution owner differs from its native chat")
            WorkspaceLease(self.root).assert_owner(owner)
            changed = updated.get("execution", {}).get("native_binding", {})
            require(updated.get("execution", {}).get("workspace_lease") == owner,
                    "generic record updates cannot transfer the native lease")
            require(changed.get("thread_id") == binding.get("thread_id") and
                    changed.get("objective") == binding.get("objective"),
                    "generic record updates cannot replace the native objective")
            new_execution = updated["execution"]
            require(new_execution.get("scope") == execution.get("scope"),
                    "generic record updates cannot amend the adopted scope")
            old_history = execution.get("binding_history", [])
            require(new_execution.get("binding_history", [])[:len(old_history)] == old_history,
                    "generic record updates cannot erase native binding history")
            for key in ("tokensUsed", "timeUsedSeconds"):
                previous = binding.get("observation", {}).get(key)
                observed = changed.get("observation", {}).get(key)
                if previous is not None:
                    require(type(previous) is int and type(observed) is int and observed >= previous,
                            "native accounting cannot be removed or reset by a record update")
        # The shared transaction name serializes inventory, projection and
        # execution bookkeeping. Every call preflights the same prior journal.
        return FileTransaction(self.root,
                               [*artifacts, Mutation(path, canonical(updated) + b"\n",
                                                     expected_exists=before is not None,
                                                     expected_sha256=expected_digest)],
                               state_dir=self.root / ".aegis/state/transactions",
                               name=AEGIS_RECORD_WRITER).commit()

    def describe(self) -> dict:
        profile = self.profile
        return {"schema": INTERFACE_VERSION, "project": profile.project,
                "declared_repository": profile.declared_repository,
                "effective_repository": str(profile.repository), "branch": profile.branch,
                "canonical_record": profile.canonical_record,
                "language_boundary": profile.language_boundary,
                "writer": AEGIS_RECORD_WRITER if profile.project == "Aegis" else None,
                "writer_implemented": profile.project == "Aegis",
                "external_writer_adoption_required": profile.project != "Aegis"}
