import pytest

from royal_git.workflow import build_plan
from royal_git.hooks import get_hook_template


def test_feature_plan_is_instructional():
    plan = build_plan("feature")
    assert len(plan) >= 5
    assert any("pull request" in step.lower() for step in plan)


def test_unknown_plan_rejected():
    with pytest.raises(ValueError):
        build_plan("unknown")


def test_hook_template_is_output_only():
    template = get_hook_template()
    assert "python -m pytest" in template
    assert ".git/hooks" in template
