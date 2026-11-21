# Merge Conflict Practice Lab

Use a disposable local repository; never practice on important project files.

1. Create a temporary repository and make an initial commit.
2. Create two branches from the same commit.
3. Edit the same line differently on each branch and commit both changes.
4. Merge one branch into the other to produce a conflict.
5. Run `royal-git conflicts` to list unresolved paths.
6. Open each file, inspect both versions, and resolve the conflict manually.
7. Run tests and inspect `git diff` before staging.
8. Stage only reviewed resolved files, then complete the merge manually.

The toolkit reports conflicts and gives guidance. It does not edit files, stage changes, or complete/abort merges.
