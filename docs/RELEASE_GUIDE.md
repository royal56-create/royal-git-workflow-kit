# Release and Tag Guide

Semantic Versioning uses `MAJOR.MINOR.PATCH`: MAJOR for incompatible changes, MINOR for backward-compatible features, PATCH for backward-compatible fixes.

## Release checklist
- [ ] Tests pass on supported Python versions.
- [ ] Documentation and changelog are updated.
- [ ] Version numbers are consistent.
- [ ] Working tree and target commit are reviewed.
- [ ] Tag name and release notes are checked.
- [ ] Maintainer approval is obtained.

Example commands for maintainers to review and run manually:
```bash
git tag -a v1.0.0 -m "Release 1.0.0"
git show v1.0.0
git push origin v1.0.0
```
The toolkit does not create or push tags.