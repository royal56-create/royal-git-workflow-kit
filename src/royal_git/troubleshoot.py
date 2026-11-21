"""Small offline Git troubleshooting knowledge base."""

GUIDES = {
    "not a git repository": (
        "Git cannot find a repository from the current directory.",
        "Move into the intended project folder and run 'git status'. If it is a new project, initialize Git only after confirming the folder.",
    ),
    "please tell me who you are": (
        "Git does not have an author name/email configured for this environment.",
        "Review 'git config user.name' and 'git config user.email'. Configure a repository-local identity if appropriate; do not copy another person's identity.",
    ),
    "rejected": (
        "The remote rejected the update, often because its branch has commits you do not have or a policy check failed.",
        "Read the full error and compare branches first. Avoid force-push as a quick fix; preserve work and follow the repository's contribution process.",
    ),
    "merge conflict": (
        "Git found overlapping edits that it cannot combine automatically.",
        "Inspect each conflicted file, understand both sides, edit deliberately, run tests, then stage only the resolved files.",
    ),
    "detached head": (
        "HEAD points directly to a commit rather than a local branch.",
        "If you need to keep new commits, create a branch before switching away. Do not assume detached commits are attached to a branch.",
    ),
    "authentication failed": (
        "The remote authentication method was rejected.",
        "Check the remote URL and your approved credential manager or SSH setup. Never paste passwords, tokens, or private keys into issues or chat.",
    ),
}


def explain_error(query: str) -> tuple[str, str] | None:
    lowered = query.lower()
    for key, value in GUIDES.items():
        if key in lowered:
            return value
    return None
