"""Generate identical instructions in every Git-visible source directory."""
from pathlib import Path
import argparse
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def sync(check=False):
    paths = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT
    ).split(b"\0")
    directories = {Path(".")}
    for raw in paths:
        if raw:
            path = Path(raw.decode())
            if (ROOT / path).is_file() and "dist" not in path.parts:
                directories.update(path.parents)
    source = (ROOT / "AGENTS.md").read_bytes()
    errors = []
    for directory in sorted(directories):
        path = ROOT / directory / "AGENTS.md"
        if path.is_symlink() or any(parent.is_symlink() for parent in path.parents if parent != ROOT.parent):
            raise ValueError(f"Redirected instruction directory: {directory}")
        if not path.exists() or path.read_bytes() != source:
            if check:
                errors.append(str(directory))
            else:
                path.write_bytes(source)
    if errors:
        raise ValueError("Missing or divergent instructions: " + ", ".join(errors))
    return len(directories)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    print(f"Instruction directories: {sync(parser.parse_args().check)}")
