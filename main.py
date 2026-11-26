#!/usr/bin/env python3
"""Rejected Olympic Sports — make.fun program/v1 entry.

Writes the tournament-winning one-liner to /output/entry.txt.
Winner chosen from 40 candidates by head-to-head tournament scored on the
judge's criteria in order (see tournament.md and README.md).
"""

import os

ENTRY = (
    "Competitive Flat-Pack Assembly: athletes build a wardrobe "
    "with no instructions and one Allen key \u2014 gold to whoever cries first."
)


def main() -> None:
    # Read-back verification: the gate is 1-200 chars, non-whitespace, UTF-8.
    # Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == (
        "Competitive Flat-Pack Assembly: athletes build a wardrobe "
        "with no instructions and one Allen key \u2014 gold to whoever cries first."
    ), "winning line changed — tournament winner must match exactly"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was actually written, not just what we intended.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch in /output/entry.txt"
    assert len(written) == 127, f"expected 127 chars, got {len(written)}"


if __name__ == "__main__":
    main()
