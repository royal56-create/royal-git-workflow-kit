"""Heuristic warning system for risky Git command text."""

from __future__ import annotations

import re

RISK_PATTERNS = [
    (re.compile(r"\bpush\b.*(?:--force|-f)(?:\s|$)", re.I), "Force push can rewrite remote history."),
    (re.compile(r"\breset\b.*--hard", re.I), "reset --hard can discard working-tree changes."),
    (re.compile(r"\bclean\b.*-[a-z]*f", re.I), "git clean can permanently remove untracked files."),
    (re.compile(r"\bbranch\b.*-D(?:\s|$)", re.I), "branch -D forcibly deletes a branch."),
    (re.compile(r"\bcheckout\b.*--\s", re.I), "checkout -- can discard changes to selected paths."),
    (re.compile(r"\brebase\b.*(?:--onto|--interactive|-i)", re.I), "Rebase rewrites commit history and needs care."),
]


def check_command(command_text: str) -> list[str]:
    """Return warnings; this function never executes the supplied text."""
    if not command_text.strip():
        return ["Enter a command to inspect."]
    warnings = [message for pattern, message in RISK_PATTERNS if pattern.search(command_text)]
    return warnings or ["No known high-risk pattern detected. This is a heuristic, not a safety guarantee."]
