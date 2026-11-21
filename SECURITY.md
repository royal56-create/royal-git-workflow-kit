# Security Policy

## Supported use

Royal Git Workflow Kit is intended for local repositories you own or are authorized to work with. It is an educational, demonstration, and productivity tool, not a remote administration service. Do not use it to access systems or data without permission.

## Important notice — use at your own risk

This project is provided "as is" and without warranties or guarantees, to the maximum extent permitted by applicable law. Users are responsible for reviewing the source code, understanding commands and their effects, testing in disposable environments where appropriate, obtaining authorization, and maintaining independent backups before use. The maintainer is not responsible for user actions or for losses caused by use, misuse, modification, or inability to use the project, except to the extent liability cannot legally be disclaimed. This notice does not override applicable law or remove any non-waivable rights or obligations.

## Safety design

- Git commands are invoked with argument arrays and `shell=False`.
- Commands have a timeout and return structured errors.
- Inspection is read-only.
- No automatic commit, push, pull, merge, rebase, reset, clean, checkout, branch deletion, or force operation is performed.
- Backup creation requires an explicit `--execute` flag and refuses to overwrite an existing path.
- Generated `.gitignore` content is printed by default; writing requires `--write` and refuses to overwrite.
- The toolkit does not request GitHub passwords, access tokens, SSH keys, or other credentials.
- CI tests use temporary synthetic repositories and do not operate on a user's repositories.

These safeguards reduce certain risks but do not make the software risk-free. The safety checker is heuristic and may miss dangerous commands or produce false positives.

## Reporting a vulnerability

Please do not publish secrets, tokens, private repository contents, or exploit details in a public issue. Contact the repository maintainer privately through GitHub's supported security reporting channel, if enabled. Include the affected version, impact, and safe reproduction steps.

## User responsibility

Review all commands before running them. Use only on repositories and systems for which you have authorization. Git data loss can occur outside this toolkit, including through commands entered manually or other installed tools. Keep independent backups.
## User responsibility and warranty notice

Use this project only for lawful learning and on resources you own or are explicitly authorized to use. Review all code and commands before running them, keep independent backups, and protect private data. Use is at your own risk. The project is supplied “as is” without warranties, to the maximum extent permitted by applicable law. Nothing here excludes non-waivable rights, liabilities, or obligations. An educational-purpose notice is not permission to access or test third-party systems.
