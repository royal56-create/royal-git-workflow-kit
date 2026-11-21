"""Safe Git hook templates; output only, never installs automatically."""

PRE_COMMIT_TEMPLATE = """#!/bin/sh
# Optional Royal Git Workflow Kit example hook.
# Review and customize this script before placing it in .git/hooks/pre-commit.
set -eu
python -m pytest
"""


def get_hook_template(name: str = "pre-commit") -> str:
    if name != "pre-commit":
        raise ValueError("Supported hook template: pre-commit")
    return PRE_COMMIT_TEMPLATE
