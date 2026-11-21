import shutil
import subprocess

import pytest

from royal_git.inspector import inspect_repository, list_branches
from royal_git.runner import GitError, run_git


pytestmark = pytest.mark.skipif(shutil.which("git") is None, reason="Git is not installed")


def make_repo(path):
    subprocess.run(["git", "init", "-b", "main", str(path)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(path), "config", "user.name", "Test User"], check=True)
    subprocess.run(["git", "-C", str(path), "config", "user.email", "test@example.invalid"], check=True)
    (path / "README.md").write_text("temporary test repository\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(path), "add", "README.md"], check=True)
    subprocess.run(["git", "-C", str(path), "commit", "-m", "test: initial fixture"], check=True, capture_output=True)


def test_inspector_reads_temporary_repository(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    make_repo(repo)
    result = inspect_repository(repo)
    assert result["branch"] == "main"
    assert result["clean"] is True
    assert result["head"]


def test_branch_listing(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    make_repo(repo)
    assert any("main" in item for item in list_branches(repo))


def test_git_command_failure_is_reported(tmp_path):
    with pytest.raises(GitError):
        run_git(["status"], cwd=tmp_path)
