#!/usr/bin/env python3
"""PreToolUse guard: block file writes outside an agent's allowed paths.

Usage (in an agent's frontmatter hook):
    python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/guard_paths.py" research/reviews/ research/BIB.md

Each argument is a path relative to the project root. A trailing "/" means
"anything under this directory"; otherwise it must match the file exactly.
Exit code 2 blocks the tool call and shows stderr to the agent.
"""
import json
import os
import sys


def main() -> int:
    allowed = sys.argv[1:]
    try:
        data = json.load(sys.stdin)
    except Exception:
        print("guard_paths: could not parse hook input; blocking to be safe", file=sys.stderr)
        return 2

    tool_input = data.get("tool_input") or {}
    target = tool_input.get("file_path") or tool_input.get("notebook_path") or tool_input.get("path")
    if not target:
        return 0  # nothing path-like to guard

    root = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd())
    cwd = data.get("cwd") or root
    abs_target = os.path.realpath(target if os.path.isabs(target) else os.path.join(cwd, target))

    # Scratch space outside the repo is always fine.
    for scratch in ("/tmp/", os.path.realpath("/tmp") + "/"):
        if abs_target.startswith(scratch):
            return 0

    rel = os.path.relpath(abs_target, root)
    if rel.startswith(".."):
        print(f"guard_paths: {target} is outside the project; blocked", file=sys.stderr)
        return 2

    for a in allowed:
        a_norm = a.rstrip("/")
        if a.endswith("/"):
            if rel == a_norm or rel.startswith(a_norm + "/"):
                return 0
        elif rel == a_norm:
            return 0

    print(
        f"guard_paths: this agent may not write {rel}. Allowed: {', '.join(allowed) or '(nothing)'}. "
        "Separation of powers (CLAUDE.md rule 4): write your output to your own allowed location.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
