"""Command-line interface for Royal Git Workflow Kit."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .backup import create_bundle
from .commits import build_commit_message, validate_commit_message
from .gitignore import RULES, generate_gitignore, write_gitignore
from .inspector import inspect_repository, list_branches
from .runner import GitError, git_executable, run_git
from .safety import check_command
from .troubleshoot import explain_error


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="royal-git", description="Safety-first Git workflow helper")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("doctor", help="check Git and Python availability")
    inspect = sub.add_parser("inspect", help="inspect the current repository (read-only)")
    inspect.add_argument("--path", default=".")
    branches = sub.add_parser("branches", help="list local branches")
    branches.add_argument("--path", default=".")

    commit = sub.add_parser("commit-check", help="validate a Conventional Commit subject")
    commit.add_argument("message")
    suggest = sub.add_parser("commit-suggest", help="build a Conventional Commit subject")
    suggest.add_argument("--type", required=True, choices=["feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"])
    suggest.add_argument("--description", required=True)
    suggest.add_argument("--scope")

    ignore = sub.add_parser("gitignore", help="generate .gitignore rules")
    ignore.add_argument("stacks", nargs="+", choices=sorted(RULES))
    ignore.add_argument("--write", action="store_true", help="write .gitignore; refuses to overwrite")
    ignore.add_argument("--path", default=".gitignore")

    safety = sub.add_parser("safety-check", help="inspect command text; never executes it")
    safety.add_argument("command_text")

    backup = sub.add_parser("backup", help="preview or explicitly create a Git bundle")
    backup.add_argument("--output", required=True)
    backup.add_argument("--repo", default=".")
    backup.add_argument("--execute", action="store_true", help="create the bundle; otherwise preview only")

    trouble = sub.add_parser("troubleshoot", help="look up a common Git error")
    trouble.add_argument("error")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "doctor":
            print(f"Python: {sys.version.split()[0]}")
            try:
                executable = git_executable()
                version = run_git(["--version"]).stdout.strip()
                print(f"Git: {version} ({executable})")
            except GitError as exc:
                print(f"Git: unavailable — {exc}")
                return 1
            return 0

        if args.command == "inspect":
            info = inspect_repository(args.path)
            print(f"Repository: {info['root']}")
            print(f"Branch: {info['branch']}")
            print(f"HEAD: {info['head']}")
            print(f"Working tree clean: {'yes' if info['clean'] else 'no'}")
            print("Status:")
            for line in info["status"]:
                print(f"  {line}")
            print("Remotes:")
            for line in info["remotes"]:
                print(f"  {line}")
            print(f"Upstream: {info['upstream'] or '(not configured)'}")
            return 0

        if args.command == "branches":
            for branch in list_branches(args.path):
                print(branch)
            return 0

        if args.command == "commit-check":
            valid, message = validate_commit_message(args.message)
            print(message)
            return 0 if valid else 2

        if args.command == "commit-suggest":
            message = build_commit_message(args.type, args.description, args.scope)
            print(message)
            valid, explanation = validate_commit_message(message)
            if not valid:
                print(f"Note: {explanation}", file=sys.stderr)
                return 2
            return 0

        if args.command == "gitignore":
            content = generate_gitignore(args.stacks)
            if args.write:
                target = write_gitignore(content, args.path)
                print(f"Created {target}")
            else:
                print(content, end="")
                print("\nPreview only. Add --write to create the file (existing files are never overwritten).")
            return 0

        if args.command == "safety-check":
            for warning in check_command(args.command_text):
                print(f"- {warning}")
            print("This checker is heuristic; always review commands yourself.")
            return 0

        if args.command == "backup":
            target = Path(args.output).expanduser().resolve()
            if not args.execute:
                print("PREVIEW ONLY — no file was created.")
                print(f"Would create Git bundle: {target}")
                print(f"Repository: {Path(args.repo).resolve()}")
                print("Review the destination, then rerun with --execute to create and verify the bundle.")
                return 0
            created = create_bundle(target, args.repo)
            print(f"Bundle created and verified: {created}")
            return 0

        if args.command == "troubleshoot":
            result = explain_error(args.error)
            if not result:
                print("No exact guide found. Read the complete Git error and consult the official Git documentation.")
                return 1
            print(f"Likely cause: {result[0]}")
            print(f"Safe next step: {result[1]}")
            return 0

    except (GitError, ValueError, OSError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
