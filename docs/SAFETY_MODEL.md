# Safety Model

Inspection commands are read-only. Content generation previews by default.

## Educational use and user responsibility

This project is supplied for educational, demonstration, and informational purposes. Users must review the code and commands, use it only with proper authorization, and maintain independent backups. Use is at the user's own risk. No guarantee of error-free or risk-free operation is made. Any disclaimer is subject to applicable law and cannot exclude liability or rights that cannot legally be excluded; see [SECURITY.md](../SECURITY.md).

## Technical boundaries

- `gitignore --write` creates a new destination only and refuses overwrite.
- `backup --execute` explicitly creates a Git bundle, refuses overwrite, and verifies the result.
- The safety checker is pattern matching: it may miss dangerous commands or flag harmless text. It is not a sandbox and cannot inspect aliases, scripts, variables, or commands run elsewhere.
- No network requests, telemetry, credential collection, or GitHub API integration is implemented.
- Inspection output may include remote URLs and local paths; review it before sharing.
