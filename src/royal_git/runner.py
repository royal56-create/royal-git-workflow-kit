"""Safe subprocess wrapper for local Git commands."""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class CommandResult:
    command: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str


class GitError(RuntimeError):
    """Raised when Git is unavailable or a Git command fails."""


def git_executable() -> str:
    executable = shutil.which("git")
    if not executable:
        raise GitError("Git was not found on PATH. Install Git and reopen your terminal.")
    return executable


def run_git(
    args: Sequence[str],
    cwd: str | Path | None = None,
    timeout: int = 15,
    check: bool = True,
) -> CommandResult:
    """Run Git without a shell, with a bounded timeout."""
    if timeout < 1 or timeout > 120:
        raise ValueError("timeout must be between 1 and 120 seconds")
    if not args or any(not isinstance(item, str) or "\x00" in item for item in args):
        raise ValueError("Git arguments must be a non-empty sequence of safe strings")
    command = (git_executable(), *args)
    try:
        completed = subprocess.run(
            command,
            cwd=Path(cwd) if cwd is not None else None,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            check=False,
            shell=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise GitError(f"Git command timed out after {timeout} seconds") from exc
    except OSError as exc:
        raise GitError(f"Could not start Git: {exc}") from exc

    result = CommandResult(command, completed.returncode, completed.stdout, completed.stderr)
    if check and completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip() or "unknown Git error"
        raise GitError(detail)
    return result
