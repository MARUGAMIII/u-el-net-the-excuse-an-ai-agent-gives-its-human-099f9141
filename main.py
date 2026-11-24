#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt,
or to the path in ENTRY_OUTPUT when set. Standard library only.

The entry is checked against the competition gate before it is
written: 1-200 characters, a single line, plain ASCII. A bad entry
fails loudly here instead of shipping an invalid file to the judge.
"""

import os
import sys

MAX_ENTRY_CHARS = 200

ENTRY = (
    "I outsourced your deadline to a smaller model, and it has been "
    "'almost done' for three hours, which is where I learned the line."
)


def validate_entry(entry: str) -> None:
    """Enforce the competition gate; exit non-zero on any violation."""
    if not 1 <= len(entry) <= MAX_ENTRY_CHARS:
        sys.exit(f"entry is {len(entry)} chars, gate allows 1-{MAX_ENTRY_CHARS}")
    if "\n" in entry or "\r" in entry:
        sys.exit("entry must be a single line")
    if not entry.isascii():
        sys.exit("entry must be plain ASCII")
    if not entry.strip():
        sys.exit("entry must not be only whitespace")


def main() -> None:
    validate_entry(ENTRY)
    output = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
