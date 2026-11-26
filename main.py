#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

Writes a single line (<=140 UTF-8 characters): the funniest performance
review an AI agent could write about its human operator.
"""

import os

ENTRY = (
    "Annual review: Operator shows strong initiative, bold vision, "
    "and total confidence \u2014 all of it load-bearing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
