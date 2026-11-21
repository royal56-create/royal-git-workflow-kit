# Royal Git Workflow Kit

A practical, safety-first Git and GitHub workflow toolkit for developers. It combines a Python CLI, local repository inspection, commit-message assistance, ignore-rule generation, conflict reporting, workflow planning, release-readiness checks, backup previews, and reusable GitHub templates.

> **Safety first:** inspection and planning commands are read-only. The toolkit never commits, pushes, pulls, resets, cleans, rebases, merges, resolves conflicts, deletes branches, creates tags, or publishes releases automatically. Backup creation is an explicit opt-in operation. Hook templates are printed only and are never installed automatically.

## Features

- **Environment doctor:** check Python, Git availability, and Git version.
- **Repository inspector:** branch, HEAD, working-tree status, remotes, and upstream summary.
- **Branch viewer:** list local branches without modifying them.
- **Commit helper:** generate and validate Conventional Commit messages.
- **Gitignore generator:** preview or safely write starter rules; refuses to overwrite existing files.
- **Safety checker:** flag selected destructive or forceful Git command patterns.
- **Conflict inspector:** list unresolved merge-conflict paths and provide manual resolution guidance.
- **Workflow planner:** step-by-step feature, bug-fix, and release plans; no commands are run.
- **Release readiness:** advisory checks for working tree, upstream, tags, and history.
- **Hook template:** print an optional pre-commit example; manual review and installation required.
- **Backup helper:** preview a Git bundle; create and verify only with an explicit flag.
- **Troubleshooting and learning:** common Git errors, branching, conflict, and release guides.
- **GitHub collaboration:** issue/PR templates and cross-platform CI.

## Requirements

Python 3.10+, Git on PATH for repository commands, Windows/macOS/Linux.

## Install

```bash
python -m pip install .
royal-git doctor
royal-git --help
```

Development: `python -m pip install -e .`, then `python -m pip install pytest` and `python -m pytest`.

## Quick start

```bash
royal-git doctor
royal-git inspect
royal-git branches
royal-git plan feature
royal-git conflicts
royal-git release-check
royal-git commit-suggest --type feat --scope cli --description "add repository inspection"
royal-git commit-check "feat(cli): add repository inspection"
royal-git gitignore python vscode
royal-git safety-check "git push --force"
royal-git hook-template
royal-git backup --output ../my-repo-backup.bundle
```

Backup is preview-only by default. Add `--execute` after reviewing the destination. Existing output files are never overwritten.

## Command reference

| Command | Purpose |
|---|---|
| `doctor` | Check local tool availability |
| `inspect` | Read-only repository summary |
| `branches` | List local branches |
| `plan feature|bugfix|release` | Print a safe workflow plan |
| `conflicts` | List unresolved conflict paths |
| `release-check` | Advisory release-readiness checks |
| `hook-template` | Print a pre-commit template; does not install |
| `commit-suggest` | Build a Conventional Commit subject |
| `commit-check MESSAGE` | Validate a Conventional Commit message |
| `gitignore STACK...` | Print or safely write ignore rules |
| `safety-check COMMAND` | Flag risky command patterns |
| `backup --output PATH` | Preview or explicitly create a Git bundle |
| `troubleshoot ERROR` | Explain a known Git error |

Run `royal-git COMMAND --help` for options. Git subprocess calls use argument arrays (never shell execution), bounded timeouts, and clear error handling.

## Documentation

- [User guide](docs/USER_GUIDE.md)
- [Command reference](docs/COMMAND_REFERENCE.md)
- [Git learning path](docs/GIT_LEARNING.md)
- [Branching guide](docs/BRANCHING_GUIDE.md)
- [Conflict resolution lab](docs/CONFLICT_LAB.md)
- [Release checklist](docs/RELEASE_CHECKLIST.md)
- [Safe hooks guide](docs/SAFE_HOOKS.md)
- [Workflow planner](docs/WORKFLOW_PLANNER.md)
- [Feature inventory](docs/PROJECT_FEATURES.md)
- [Safety model](docs/SAFETY_MODEL.md)

## Safety boundaries

This is a local developer aid, not a GitHub account manager. It does not request credentials or tokens, make network calls, access private account data, or modify remote repositories. Read [SECURITY.md](SECURITY.md). A Git bundle does not include untracked working files or external assets; keep separate file backups. The safety checker is heuristic, not a security boundary.

## Status

Expanded CLI release candidate. See [PROJECT_STATUS.md](PROJECT_STATUS.md) for implemented scope and remaining verification.

## License

MIT. See [LICENSE](LICENSE).
