"""Conventional Commit message helpers."""

from __future__ import annotations

import re

PATTERN = re.compile(
    r"^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)"
    r"(\([a-z0-9._/-]+\))?(!)?: .{1,72}$"
)


def validate_commit_message(message: str) -> tuple[bool, str]:
    candidate = message.strip()
    if not candidate:
        return False, "Commit message cannot be empty."
    if "\n" in candidate:
        return False, "Use a single-line subject; put longer details in the commit body."
    if len(candidate) > 100:
        return False, "Subject is too long; keep it concise (maximum 100 characters)."
    if not PATTERN.match(candidate):
        return False, (
            "Expected: type(scope): short description. Example: "
            "'feat(cli): add repository inspection'."
        )
    return True, "Valid Conventional Commit subject."


def build_commit_message(kind: str, description: str, scope: str | None = None) -> str:
    allowed = {"feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"}
    if kind not in allowed:
        raise ValueError(f"type must be one of: {', '.join(sorted(allowed))}")
    clean = " ".join(description.split())
    if not clean or "\n" in description:
        raise ValueError("description must contain non-empty single-line text")
    if scope and not re.fullmatch(r"[a-z0-9._/-]+", scope):
        raise ValueError("scope may contain lowercase letters, digits, dot, underscore, slash, and hyphen")
    prefix = f"{kind}({scope})" if scope else kind
    return f"{prefix}: {clean}"
