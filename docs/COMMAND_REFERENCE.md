# Command Reference

| Command | Options | Behavior |
|---|---|---|
| `royal-git doctor` | none | Check Python and Git |
| `royal-git inspect` | `--path DIR` | Read-only repository summary |
| `royal-git branches` | `--path DIR` | List local branches |
| `royal-git commit-check MESSAGE` | none | Validate one-line Conventional Commit subject |
| `royal-git gitignore STACK...` | `--write --path FILE` | Preview or create a new ignore file |
| `royal-git safety-check TEXT` | none | Heuristic text scan only |
| `royal-git backup` | `--repo DIR --output FILE --execute` | Preview or explicitly create a bundle |
| `royal-git troubleshoot TEXT` | none | Offline error lookup |

Run `royal-git --help` or `royal-git COMMAND --help` for options. Exit codes: 0 success, 1 runtime/lookup error, 2 invalid commit message.