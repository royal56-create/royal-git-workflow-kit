# Project Feature Inventory

## Implemented in the current main branch
| Area | Behavior |
|---|---|
| Doctor | Python version and Git availability/version |
| Inspector | Root, branch, HEAD, status, remotes, upstream |
| Branch listing | Local branches; read-only |
| Commit helper | Build and validate Conventional Commit subjects |
| Gitignore | Preview or create supported templates without overwrite; excludes common environment secret files while allowing .env.example |
| Safety checker | Flags selected risky patterns; never executes input |
| Backup | Preview by default; explicit Git bundle creation and verification |
| Conflict inspector | Lists unresolved merge-conflict paths and prints manual guidance; never edits or stages |
| Workflow planner | Feature, bug-fix, and release checklists; no commands are executed |
| Release readiness | Advisory working-tree, upstream, tag, and history checks; no tag or publication |
| Hook template | Prints a sample pre-commit hook; no automatic installation |
| Troubleshooter | Offline common-error lookup |
| Learning | Git basics, branching, conflict lab, release checklist, workflow planning |
| Collaboration | Issue and pull-request templates |
| CI | Unit and temporary-repository tests across OS/Python matrix |

Supported ignore templates: Python, Node.js, Java, C, C++, VS Code, JetBrains, macOS, Windows.

## Deliberately not included
GUI/dashboard, live GitHub API, authentication, credential storage, remote secret scanning, automatic conflict resolution, automatic push/pull/commit/merge/rebase/reset/clean, automatic tag/release publishing, and team analytics.
