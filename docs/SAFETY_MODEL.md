# Safety Model

Inspection commands are read-only. Content generation previews by default.

- `gitignore --write` creates a new destination only and refuses overwrite.
- `backup --execute` explicitly creates a Git bundle, refuses overwrite, and verifies the result.
- The safety checker is pattern matching: it may miss dangerous commands or flag harmless text. It is not a sandbox and cannot inspect aliases, scripts, variables, or commands run elsewhere.
- No network requests, telemetry, credential collection, or GitHub API integration is implemented.
- Inspection output may include remote URLs and local paths; review it before sharing.