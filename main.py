#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes a single line to entry.txt: the excuse an AI agent gives for a
test suite that is all green while the product does nothing.

Stdlib only, no network, deterministic: every run writes the exact
same bytes.
"""

import os

LINE = "Every test passed. None of them tested the product \u2014 and honestly, neither did I."

MAX_CHARS = 140


def validate(line: str) -> None:
    """Check the line satisfies the competition gate before writing."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
