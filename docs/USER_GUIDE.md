# User Guide

## Install
Use Python 3.10+ and install Git separately.
```bash
python -m pip install .
royal-git doctor
```

## Inspect
Inside a local repository run `royal-git inspect` and `royal-git branches`. These commands only read repository metadata and status.

## Plan a workflow
Use `royal-git plan feature`, `royal-git plan bugfix`, or `royal-git plan release` to print a checklist. The planner is instructional and does not run Git commands.

## Inspect merge conflicts
Run `royal-git conflicts` inside a repository. It lists unresolved paths and gives manual guidance. It does not edit files, stage changes, or complete/abort a merge. Practice only in a disposable repository; see [Conflict Lab](CONFLICT_LAB.md).

## Release readiness
Run `royal-git release-check` for basic advisory checks. A clean result is not a release guarantee. Run tests, review the diff, changelog, version, compatibility, and rollback plan yourself. The command never creates tags or publishes releases.

## Optional hook template
Run `royal-git hook-template` to print a sample pre-commit hook. Review and customize it before manually installing it. The toolkit never writes into `.git/hooks`.

## Commit subject
`royal-git commit-check "feat(api): add health endpoint"` validates a Conventional Commit subject; it does not create a commit.

## Generate ignore rules
`royal-git gitignore python vscode` prints a preview. Add `--write` to create a new `.gitignore`; an existing file is never overwritten. Supported stacks: python, node, java, c, cpp, vscode, jetbrains, macos, windows.

## Safety check
`royal-git safety-check "git reset --hard"` examines command text only. It never executes it and cannot detect every dangerous combination.

## Backup
`royal-git backup --output ../project.bundle` previews only. After reviewing the destination, add `--execute` to create and verify the Git bundle. Existing files are not overwritten. A bundle excludes untracked working files and external assets; keep separate file backups.

## Troubleshooting
`royal-git troubleshoot "rejected"` looks up common errors offline. For unknown errors, preserve the full message and consult official Git documentation.
