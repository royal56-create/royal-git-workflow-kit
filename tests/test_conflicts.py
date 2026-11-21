from royal_git.conflicts import conflict_guidance


def test_conflict_guidance_is_manual_and_safe():
    guidance = conflict_guidance()
    assert any("manually" in item.lower() for item in guidance)
    assert any("never" in item.lower() for item in guidance)
