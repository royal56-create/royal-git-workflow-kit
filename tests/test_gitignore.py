import pytest

from royal_git.gitignore import generate_gitignore, write_gitignore


def test_generate_combined_rules():
    result = generate_gitignore(["python", "vscode"])
    assert "__pycache__/" in result
    assert ".vscode/*" in result


def test_unknown_stack_rejected():
    with pytest.raises(ValueError):
        generate_gitignore(["unknown-stack"])


def test_existing_file_not_overwritten(tmp_path):
    target = tmp_path / ".gitignore"
    target.write_text("keep me", encoding="utf-8")
    with pytest.raises(FileExistsError):
        write_gitignore("new rules", target)
    assert target.read_text(encoding="utf-8") == "keep me"
