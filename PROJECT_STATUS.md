# Project Status

**Version:** 1.0.0  
**Status:** Expanded CLI release candidate — verification in progress  
**Language:** Python 3.10+  
**Runtime dependencies:** Python standard library only

## Implemented

- Git/Python environment doctor.
- Read-only repository inspection and local branch listing.
- Conventional Commit message suggestion and validation.
- .gitignore generation for common stacks and editors.
- Heuristic risk-pattern checker for Git command text.
- Git bundle backup preview plus explicit creation and verification.
- Common-error troubleshooting helper.
- Read-only unresolved merge-conflict inspection and manual guidance.
- Feature, bug-fix, and release workflow planner.
- Advisory release-readiness checks; no tags or publishing are performed.
- Optional pre-commit hook template output; no automatic installation.
- User documentation, safe practice labs, GitHub templates, and cross-platform CI configuration.

## Deliberately out of scope

- GUI or web dashboard.
- GitHub API automation or account authentication.
- Automatic push, pull, commit, merge, rebase, reset, clean, conflict resolution, tag creation, release publishing, or branch deletion.
- Credential storage or remote-repository secret scanning.
- Full Git conflict auto-resolution.

## Verification still required

- Run the complete pytest suite on Python 3.10–3.12 and Windows, macOS, and Linux.
- Confirm the latest GitHub Actions run is green.
- Manually exercise the new `conflicts`, `plan`, `release-check`, and `hook-template` commands in disposable repositories.
- Review package installation and CLI help from a clean environment.

A green CI run verifies tested code paths only; it is not a guarantee against every environment-specific issue. Do not describe this project as fully verified until these checks pass.
