# Git Hooks: Safe Use

The toolkit can print an example pre-commit hook. It never installs hooks automatically.

1. Generate or copy the template with `royal-git hook-template`.
2. Read every line and adapt the test command to your project.
3. Back up any existing hook before replacing it.
4. Install it manually in `.git/hooks/pre-commit` and make it executable where required.
5. Test it with a harmless change.

Hooks run local commands during Git operations. Only use scripts you understand and trust. Do not place credentials in hooks.
