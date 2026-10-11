"""Runtime layout shared with the existing context ledger."""
from pathlib import Path

def cache_dir(root: Path) -> Path:
    return root / ".aegis" / "cache"
