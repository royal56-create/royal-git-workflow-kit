# Contributing

Thanks for considering a contribution.

## Development setup

```bash
python -m pip install -e .
python -m pip install pytest
pytest
```

## Guidelines

- Keep the standard library as the runtime dependency unless there is a strong reason otherwise.
- Use `subprocess.run` with argument lists; never use `shell=True`.
- Add timeouts and validate user-controlled inputs.
- Never add automatic destructive Git operations.
- Write tests with temporary directories and temporary Git repositories.
- Do not make network requests in tests.
- Update the user guide and feature inventory when behavior changes.
- Keep examples safe and clearly label commands that alter a repository.

## Pull requests

Describe the problem, the change, how it was tested, and any safety implications. Include tests for new behavior.
