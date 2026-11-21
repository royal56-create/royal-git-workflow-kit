from royal_git.troubleshoot import explain_error


def test_known_error_has_safe_guidance():
    result = explain_error("Updates were rejected")
    assert result is not None
    assert "force-push" in result[1]


def test_unknown_error_returns_none():
    assert explain_error("some unknown error") is None
