"""Read-only local repository inspection with credential-safe remote display."""

from __future__ import annotations

import re
from pathlib import Path

from .runner import run_git


_HTTP_USERINFO = re.compile(r"(?i)(https?://)[^/@\s]+@")


def _redact_remote_credentials(line: str) -> str:
    """Hide HTTP(S) URL user-info before remote URLs are shown."""
    return _HTTP_USERINFO.sub(r"\1[REDACTED]@", line)


def inspect_repository(path: str | Path = ".") -> dict[str, object]:
    root = Path(path).resolve()
    top = run_git(["rev-parse", "--show-toplevel"], cwd=root).stdout.strip()
    branch_result = run_git(["branch", "--show-current"], cwd=root, check=False)
    head_result = run_git(["rev-parse", "--short", "HEAD"], cwd=root, check=False)
    status = run_git(["status", "--short", "--branch"], cwd=root).stdout.splitlines()
    remote_output = run_git(["remote", "-v"], cwd=root, check=False).stdout.splitlines()
    remotes = [_redact_remote_credentials(line) for line in remote_output]
    upstream = run_git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}"], cwd=root, check=False)

    return {
        "root": top,
        "branch": branch_result.stdout.strip() or "(detached HEAD or unborn branch)",
        "head": head_result.stdout.strip() or "(no commits yet)",
        "status": status,
        "remotes": remotes,
        "upstream": upstream.stdout.strip() if upstream.returncode == 0 else None,
        "clean": len(status) <= 1,
    }


def list_branches(path: str | Path = ".") -> list[str]:
    output = run_git(["branch", "--format=%(HEAD) %(refname:short)"], cwd=path).stdout
    return [line.strip() for line in output.splitlines() if line.strip()]
