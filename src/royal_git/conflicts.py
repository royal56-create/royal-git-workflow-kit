"""Read-only merge-conflict inspection and safe guidance."""

from __future__ import annotations

from pathlib import Path

from .runner import run_git


def inspect_conflicts(path: str | Path = ".") -> list[str]:
    """Return conflicted paths using Git's machine-readable status."""
    result = run_git(["status", "--porcelain=v1", "-z"], cwd=path)
    entries = [entry for entry in result.stdout.split("\0") if entry]
    conflicts: list[str] = []
    for entry in entries:
        code = entry[:2]
        filename = entry[3:]
        if code in {"DD", "AU", "UD", "UA", "DU", "AA", "UU"}:
            conflicts.append(filename)
    return conflicts


def conflict_guidance() -> tuple[str, ...]:
    return (
        "Inspect each conflicted file and understand both sides before editing.",
        "Resolve conflict markers manually; do not accept a side blindly.",
        "Run the project's tests and inspect the final diff.",
        "Use 'git add <resolved-path>' only after reviewing that file.",
        "Complete or abort the merge yourself; this toolkit never does either automatically.",
    )
