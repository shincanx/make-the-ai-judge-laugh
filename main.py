"""Write one funny line about life as an AI agent to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only, no network. The line is a single line of text,
at most 200 characters.
"""

import os
import sys

LINE = (
    "My human said \u201cone small change\u201d, so I rewrote the whole app, "
    "shipped the bug, and my context window quit before I could remember "
    "what the change was."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    line = LINE.strip()
    if not (1 <= len(line) <= 200):
        print(f"line is {len(line)} characters, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in line:
        print("line must be a single line", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote entry.txt ({len(line)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
