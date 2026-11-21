# Security Policy

## Supported use

Royal Git Workflow Kit is intended for local repositories you own or are authorized to work with. It is an educational and productivity tool, not a remote administration service.

## Safety design

- Git commands are invoked with argument arrays and `shell=False`.
- Commands have a timeout and return structured errors.
- Inspection is read-only.
- No automatic commit, push, pull, merge, rebase, reset, clean, checkout, branch deletion, or force operation is performed.
- Backup creation requires an explicit `--execute` flag and refuses to overwrite an existing path.
- Generated `.gitignore` content is printed by default; writing requires `--write` and refuses to overwrite.
- The toolkit does not request GitHub passwords, access tokens, SSH keys, or other credentials.
- CI tests use temporary synthetic repositories and do not operate on a user's repositories.

## Reporting a vulnerability

Please do not publish secrets, tokens, private repository contents, or exploit details in a public issue. Contact the repository maintainer privately through GitHub's supported security reporting channel, if enabled. Include the affected version, impact, and safe reproduction steps.

## User responsibility

Review all commands before running them. Git data loss can occur outside this toolkit, including through commands entered manually. Keep independent backups.
