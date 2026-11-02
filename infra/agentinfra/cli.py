"""Canonical Destiny formal-contract CLI; no legacy acceptance entry points."""
import sys


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    families = {"roadmap", "policy", "codex", "verification", "budget", "review", "skills", "portability", "knowledge", "interfaces"}
    if argv and (argv[0] in families or argv[0] == "--root"):
        from .roadmap_cli import main as roadmap_main
        return roadmap_main(argv)
    from .destiny import main as legacy_main
    return legacy_main(argv)
