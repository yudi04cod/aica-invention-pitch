#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance -- the household argument over what to watch on
TV -- to /output/entry.txt.

The invention: the Ceasefire Remote, a TV remote that hides itself the
moment a what-to-watch argument starts and only reappears once everyone
signs a tiny peace treaty on its screen. The laugh comes from the
invention itself: a remote control that goes on strike until diplomacy
is restored.

Standard library only. Deterministic: the same sentence every run.
"""

import os
import sys

MAX_CHARS = 220

PITCH = (
    "The Ceasefire Remote: a TV remote that hides itself the moment a "
    "what-to-watch argument starts and only reappears once everyone "
    "signs a tiny peace treaty on its screen."
)


def validate(sentence: str) -> None:
    """Check the pitch obeys the competition gate (1-220 chars, one sentence)."""
    if not sentence or not sentence.strip():
        raise ValueError("pitch must not be empty or only whitespace")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            "pitch is %d characters, over the %d limit" % (len(sentence), MAX_CHARS)
        )
    # Exactly one sentence: a single terminal full stop, at the very end,
    # and no other sentence-ending punctuation anywhere in the text.
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    if any(mark in sentence for mark in ("!", "?", ";")):
        raise ValueError("pitch must contain no other sentence-ending mark")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("pitch must be a single line")


def main() -> int:
    validate(PITCH)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(PITCH)
    # Read back and verify what was written is exactly the pitch.
    with open(out_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != PITCH:
        raise ValueError("read-back mismatch: entry.txt differs from the pitch")
    print("Wrote %d characters to %s" % (len(written), out_path))
    print(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
