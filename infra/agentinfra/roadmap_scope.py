"""Declared writer scope checks; reference bytes and original tests are protected."""
from fnmatch import fnmatchcase
from pathlib import Path, PurePosixPath

from .roadmap_records import require
from .security import confined_path


def validate_write_scope(root: Path, contract: dict, paths: list[str]) -> None:
    require(bool(paths), "write scope cannot be empty")
    for name in paths:
        path = PurePosixPath(name)
        require(not path.is_absolute() and ".." not in path.parts and "\\" not in name, "write path must be confined and repository-relative")
        confined_path(root, name)
        require(not any(fnmatchcase(name, p) for p in contract["protected_scope"]), "protected source/reference/test path")
        require(any(fnmatchcase(name, p) for p in contract["write_scope"]), "path is outside milestone writer scope")
