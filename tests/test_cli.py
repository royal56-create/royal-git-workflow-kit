from royal_git.cli import main


def test_commit_suggest_cli(capsys):
    assert main(["commit-suggest", "--type", "feat", "--scope", "cli", "--description", "add status command"]) == 0
    assert capsys.readouterr().out.strip() == "feat(cli): add status command"


def test_commit_check_cli_rejects_bad_message(capsys):
    assert main(["commit-check", "bad message"]) == 2
    assert "Expected:" in capsys.readouterr().out
