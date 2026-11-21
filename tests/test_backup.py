import shutil
import subprocess

import pytest

from royal_git.backup import create_bundle


pytestmark = pytest.mark.skipif(shutil.which("git") is None, reason="Git is not installed")


def test_bundle_created_and_existing_file_is_not_overwritten(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", str(repo)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.name", "Test User"], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.email", "test@example.invalid"], check=True)
    (repo / "tracked.txt").write_text("tracked\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(repo), "add", "tracked.txt"], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-m", "test: initial"], check=True, capture_output=True)

    bundle = tmp_path / "backup.bundle"
    assert create_bundle(bundle, repo) == bundle
    assert bundle.is_file() and bundle.stat().st_size > 0
    with pytest.raises(FileExistsError):
        create_bundle(bundle, repo)
