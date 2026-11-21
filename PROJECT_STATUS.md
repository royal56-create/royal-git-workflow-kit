# Project Status

**Version:** 1.0.0  
**Status:** Initial public CLI release  
**Language:** Python 3.10+  
**Runtime dependencies:** Python standard library only

## Implemented

- Git/Python environment doctor.
- Read-only repository inspection and local branch listing.
- Conventional Commit message validation.
- .gitignore generation for common stacks and editors.
- Risk-pattern checker for Git command text.
- Git bundle backup preview and explicit execution.
- Common-error troubleshooting helper.
- User documentation, safe practice labs, GitHub templates, and CI tests.

## Deliberately out of scope

- GUI or web dashboard.
- GitHub API automation or account authentication.
- Automatic push, pull, commit, merge, rebase, reset, clean, or branch deletion.
- Credential storage or secret scanning of remote repositories.
- Full Git conflict auto-resolution.

## Verification

The GitHub Actions workflow runs unit tests and temporary local Git repository tests. A green CI run verifies the tested code paths only; it is not a guarantee against every environment-specific issue.
