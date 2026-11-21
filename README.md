# Royal Git Workflow Kit

A practical, safety-first Git and GitHub workflow toolkit for developers. It combines a Python CLI, repository inspection, commit-message assistance, `.gitignore` generation, risk checks, backup previews, troubleshooting references, learning labs, and reusable GitHub templates.

> **Safety first:** inspection commands are read-only. The toolkit never commits, pushes, resets, cleans, rebases, merges, or deletes branches automatically. Backup creation is an explicit opt-in operation.

## Features
- **Environment doctor:** check Python, Git availability, and Git version.
- **Repository inspector:** branch, HEAD, working-tree status, remotes, and upstream summary.
- **Commit helper:** generate and validate Conventional Commit messages.
- **Gitignore generator:** create starter rules for common languages/tools, including environment-secret exclusions.
- **Safety checker:** flag selected destructive or forceful Git command patterns.
- **Backup helper:** preview a Git bundle; execute only with an explicit flag.
- **Troubleshooting reference:** explain common Git errors and safe next steps.
- **Learning resources:** branching, merge conflicts, releases, collaboration, and practice labs.
- **GitHub templates and CI:** automated tests using temporary repositories.

## Requirements
Python 3.10+, Git on PATH for repository commands, Windows/macOS/Linux.

## Install
```bash
python -m pip install .
royal-git doctor
royal-git --help
```
Development: `python -m pip install -e .`, then `python -m pip install pytest` and `pytest`.

## Quick start
```bash
royal-git doctor
royal-git inspect
royal-git branches
royal-git commit-suggest --type feat --scope cli --description "add repository inspection"
royal-git commit-check "feat(cli): add repository inspection"
royal-git gitignore python vscode
royal-git safety-check "git push --force"
royal-git backup --output ../my-repo-backup.bundle
```
Backup is preview-only by default. Add `--execute` after reviewing the destination. Existing output files are never overwritten.

## Commands
| Command | Purpose |
|---|---|
| `doctor` | Check local tool availability |
| `inspect` | Read-only repository summary |
| `branches` | List local branches |
| `commit-suggest` | Build a Conventional Commit subject |
| `commit-check MESSAGE` | Validate a Conventional Commit message |
| `gitignore STACK...` | Print or safely write ignore rules |
| `safety-check COMMAND` | Flag risky Git command patterns |
| `backup --output PATH` | Preview or explicitly create a Git bundle |
| `troubleshoot ERROR` | Explain a known Git error |

Run `royal-git COMMAND --help` for options. Git subprocess calls use argument arrays (never shell execution), bounded timeouts, and clear error handling.

## Documentation
- [User guide](docs/USER_GUIDE.md)
- [Command reference](docs/COMMAND_REFERENCE.md)
- [Git learning path](docs/GIT_LEARNING.md)
- [Branching guide](docs/BRANCHING_GUIDE.md)
- [Conflict resolution lab](docs/CONFLICT_RESOLUTION.md)
- [Release guide](docs/RELEASE_GUIDE.md)
- [Workflow planner](docs/WORKFLOW_PLANNER.md)
- [Feature inventory](docs/PROJECT_FEATURES.md)
- [Safety model](docs/SAFETY_MODEL.md)

## Safety boundaries
This is a local developer aid, not a GitHub account manager. It does not request credentials or tokens, make network calls, access private account data, or modify remote repositories. Read [SECURITY.md](SECURITY.md). A Git bundle does not include untracked working files or external assets; keep separate file backups.

## Status
Initial CLI release. GUI/dashboard and live GitHub API automation are intentionally out of scope. See [PROJECT_STATUS.md](PROJECT_STATUS.md).

## License
MIT. See [LICENSE](LICENSE).
