"""Explicit opt-in Git bundle backup."""

from __future__ import annotations

from pathlib import Path

from .runner import run_git


def create_bundle(output: str | Path, repo: str | Path = ".") -> Path:
    target = Path(output).expanduser().resolve()
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing backup: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    run_git(["bundle", "create", str(target), "--all"], cwd=repo, timeout=60)
    verify = run_git(["bundle", "verify", str(target)], cwd=repo, timeout=30, check=False)
    if verify.returncode != 0:
        raise RuntimeError("Bundle was created but verification failed; keep it separate and inspect manually.")
    return target
