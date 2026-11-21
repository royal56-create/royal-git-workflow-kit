# Branching Guide

## Feature branch workflow
1. Start from an up-to-date shared base branch.
2. Create a short-lived feature branch.
3. Make focused commits.
4. Run tests and inspect the diff.
5. Open a pull request, request review, and merge under repository policy.

Example commands to review and run only where authorized:
```bash
git status
git switch -c feature/short-description
git diff
git log --oneline --decorate -10
```

**Merge** combines histories and may preserve branch topology. **Rebase** replays commits and rewrites commit IDs. Follow team policy; do not rebase shared branches without agreement. The toolkit does not execute branch switching, merge, rebase, or push.