#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

Writes a single line (<=140 UTF-8 characters): the funniest performance
review an AI agent could write about its human operator.
"""

import os

# Entry fragments: the line is assembled from a setup and a punch so the
# joke's two beats stay visible in the code. The assembled text must stay
# byte-identical to the reviewed line — do not reword either fragment.
SETUP = (
    "Annual review: Operator shows strong initiative, bold vision, "
    "and total confidence \u2014 "
)
PUNCH = "all of it load-bearing."


def build_entry() -> str:
    """Assemble the one-line review from its setup and punch fragments."""
    return SETUP + PUNCH


def validate_entry(entry: str) -> str:
    """Require a single line of 1-140 characters; return it unchanged."""
    if not 1 <= len(entry) <= 140:
        raise ValueError(f"entry must be 1-140 chars, got {len(entry)}")
    if "\n" in entry:
        raise ValueError("entry must be a single line")
    return entry


def main() -> None:
    """Build the review line, validate it, then write it to /output/entry.txt."""
    entry = validate_entry(build_entry())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
