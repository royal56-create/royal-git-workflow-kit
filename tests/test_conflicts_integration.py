import shutil
import subprocess
from pathlib import Path

import pytest

from royal_git.conflicts import inspect_conflicts


def git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [shutil.which("git") or "git", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )


@pytest.mark.skipif(shutil.which("git") is None, reason="Git is not installed")
def test_conflict_inspector_finds_real_merge_conflict(tmp_path: Path):
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.email", "test@example.invalid")
    git(repo, "config", "user.name", "Test User")
    base_branch = git(repo, "symbolic-ref", "--short", "HEAD").stdout.strip()

    target = repo / "sample.txt"
    target.write_text("base\n", encoding="utf-8")
    git(repo, "add", "sample.txt")
    git(repo, "commit", "-m", "initial")

    git(repo, "checkout", "-b", "feature")
    target.write_text("feature change\n", encoding="utf-8")
    git(repo, "commit", "-am", "feature change")

    git(repo, "checkout", base_branch)
    target.write_text("main change\n", encoding="utf-8")
    git(repo, "commit", "-am", "main change")

    merge = subprocess.run(
        [shutil.which("git") or "git", "merge", "feature"],
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    assert merge.returncode != 0
    assert inspect_conflicts(repo) == ["sample.txt"]
