"""Read-only release readiness checks."""

from __future__ import annotations

from pathlib import Path

from .inspector import inspect_repository
from .runner import run_git


def release_readiness(path: str | Path = ".") -> list[str]:
    """Return warnings for a human-reviewed release; never creates a tag."""
    info = inspect_repository(path)
    warnings: list[str] = []
    if not info["clean"]:
        warnings.append("Working tree is not clean; review or commit intended changes.")
    if not info["upstream"]:
        warnings.append("Current branch has no configured upstream.")
    tags = run_git(["tag", "--list"], cwd=path, check=True).stdout.splitlines()
    if not tags:
        warnings.append("No Git tags found; confirm the project's versioning history.")
    latest = run_git(["log", "-1", "--format=%s"], cwd=path, check=False)
    if latest.returncode != 0 or not latest.stdout.strip():
        warnings.append("No commit history found.")
    if not warnings:
        warnings.append("Basic repository checks passed. Run tests and review changelog, version, license, and release notes manually.")
    return warnings
