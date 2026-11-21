from royal_git.safety import check_command


def test_force_push_warned():
    assert any("Force push" in item for item in check_command("git push origin main --force"))


def test_hard_reset_warned():
    assert any("discard" in item for item in check_command("git reset --hard"))


def test_safe_command_gets_heuristic_notice():
    assert any("heuristic" in item for item in check_command("git status"))
