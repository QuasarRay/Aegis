# Generic bootstrap

For a repository that already has its own root `AGENTS.md`, copy `.agents/` first and **do not overwrite the
existing root file**. Preview the merge:

```text
python .agents/bootstrap/install.py
```

Apply it:

```text
python .agents/bootstrap/install.py --apply
```

The installer adds/replaces only the marked Aegis block, preserves unrelated instructions, serializes writes,
uses atomic replacement, records a local journal, and backs up an existing root instruction file. If it finds
an unknown edited Aegis block, it fails closed. `--replace-managed-block` is an explicit escape hatch after
manual review.

Uninstall preview/apply:

```text
python .agents/bootstrap/uninstall.py
python .agents/bootstrap/uninstall.py --apply
```

Uninstall removes only the managed block and refuses when that block drifted after installation unless the
explicit force flag is used. Project-specific instructions outside the block remain untouched.

For a clean repository with no root instructions, the packaged `AGENTS.md` is already the same bootstrap body
and can be used directly.
