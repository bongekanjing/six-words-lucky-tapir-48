#!/usr/bin/env python3
"""Write the six-word entry for make.fun's "Six Words, One Story" bounty.

Standard library only. No network, no clock, no randomness: two runs produce
byte-identical output.
"""

from __future__ import annotations

import os
from pathlib import Path

# The entire entry. Six words, and the turn is carried by two of them: "wrote"
# instead of "read" makes the man the author of the death notice rather than its
# subject, and "her" is a whole relationship the sentence never names. Then he
# shaves -- an ordinary bathroom act landing on top of an act of formal grief.
STORY = "He wrote her obituary, then shaved."

WORD_COUNT = 6
MAX_CHARS = 60
OUTPUT_NAME = "entry.txt"
# Whitespace that would turn the entry into more than one line or smuggle in a
# field separator. Spaces are handled separately: exactly one between words.
FORBIDDEN_WHITESPACE = "\n\r\t\v\f"


def validate_story(text: str) -> str:
    """Validate a candidate entry and return it unchanged.

    The entry must already be canonical: exactly WORD_COUNT words separated by
    single spaces, no leading or trailing whitespace, no newline or tab inside.
    Bad input is rejected instead of silently repaired, so the bytes that get
    written are exactly the bytes that were judged.
    """
    if not isinstance(text, str):
        raise ValueError(f"story must be str, got {type(text).__name__}")
    if not text:
        raise ValueError("story is empty")
    if text != text.strip():
        raise ValueError(
            f"story must not start or end with whitespace: {text!r}"
        )

    found = sorted({ch for ch in text if ch in FORBIDDEN_WHITESPACE})
    if found:
        names = ", ".join(repr(ch) for ch in found)
        raise ValueError(
            f"story must be a single line, found {names} inside it: {text!r}"
        )
    if "  " in text:
        raise ValueError(
            f"story must separate words with single spaces only: {text!r}"
        )

    words = text.split(" ")
    if len(words) != WORD_COUNT:
        raise ValueError(
            f"story must be exactly {WORD_COUNT} words, got {len(words)}: {text!r}"
        )
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"story must be at most {MAX_CHARS} characters, got {len(text)}: {text!r}"
        )
    return text


def output_dir() -> Path:
    """Directory to write into: $MAKEFUN_OUTPUT_DIR, else the current directory."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(raw) if raw else Path.cwd()


def write_entry(
    text: str = STORY, directory: str | os.PathLike[str] | None = None
) -> Path:
    """Validate then write the story to <directory>/entry.txt. Returns the path.

    The payload is written as exact UTF-8 bytes and read back. Any difference --
    a short write, a platform newline translation, a trailing newline -- raises
    RuntimeError, so a mangled entry can never ship.
    """
    story = validate_story(text)
    payload = story.encode("utf-8")

    target_dir = Path(directory) if directory is not None else output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / OUTPUT_NAME

    path.write_bytes(payload)
    written = path.read_bytes()
    if written != payload:
        raise RuntimeError(
            f"verification failed: {path} holds {written!r}, expected {payload!r}"
        )

    print(f"Wrote {len(story)} characters to {path}")
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
