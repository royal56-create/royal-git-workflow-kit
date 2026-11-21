"""Read-only workflow planner for common Git tasks."""

from __future__ import annotations


PLANS = {
    "feature": (
        "Start from an up-to-date main branch after checking its status.",
        "Create a short-lived feature branch (for example: feature/<name>).",
        "Make focused changes and run relevant tests locally.",
        "Review the diff and check for secrets or generated files.",
        "Prepare a Conventional Commit message; commit only after manual review.",
        "Push the branch yourself and open a pull request.",
        "Address review feedback and merge using the repository's policy.",
    ),
    "bugfix": (
        "Reproduce the issue and record expected versus actual behavior.",
        "Create a short-lived fix branch from the intended base.",
        "Add a regression test before or alongside the fix.",
        "Make the smallest safe change and run the full test suite.",
        "Review the diff, then prepare a Conventional Commit message.",
        "Open a pull request with reproduction steps and test evidence.",
    ),
    "release": (
        "Confirm the working tree is clean and tests pass.",
        "Review the changelog and compatibility notes.",
        "Check version metadata and dependency constraints.",
        "Review commits included since the previous release.",
        "Create and publish a tag/release manually after approval.",
        "Verify the published artifact and document rollback guidance.",
    ),
}


def build_plan(kind: str) -> tuple[str, ...]:
    """Return an instructional plan; it does not execute Git commands."""
    try:
        return PLANS[kind]
    except KeyError as exc:
        raise ValueError(f"Unknown workflow '{kind}'. Choose: {', '.join(sorted(PLANS))}") from exc
