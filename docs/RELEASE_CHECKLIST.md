# Release Readiness Checklist

Royal Git Workflow Kit's release helper is advisory only. It does not create tags, publish packages, push commits, or change repository state.

Before a release:

- [ ] Confirm the intended branch and a clean working tree.
- [ ] Run the complete test suite on supported Python versions and operating systems.
- [ ] Review the diff and included commits.
- [ ] Update version metadata and changelog.
- [ ] Check license, dependency constraints, and security notes.
- [ ] Prepare release notes and compatibility/upgrade guidance.
- [ ] Decide and document rollback steps.
- [ ] Create and publish the tag/release manually after review.
- [ ] Verify the published artifact from a clean environment.

A passing readiness check is not proof that a release is safe. Human review and CI remain required.
