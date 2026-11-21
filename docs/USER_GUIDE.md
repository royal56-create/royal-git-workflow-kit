# User Guide

## Install
Use Python 3.10+ and install Git separately.
```bash
python -m pip install .
royal-git doctor
```

## Inspect
Inside a local repository run `royal-git inspect` and `royal-git branches`. These commands only read repository metadata and status.

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