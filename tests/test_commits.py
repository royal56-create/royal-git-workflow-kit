from royal_git.commits import build_commit_message, validate_commit_message


def test_valid_conventional_commit():
    assert validate_commit_message("feat(cli): add inspect command")[0]


def test_invalid_conventional_commit():
    assert not validate_commit_message("added stuff")[0]


def test_build_commit_message():
    assert build_commit_message("fix", "handle missing git", "runner") == "fix(runner): handle missing git"
