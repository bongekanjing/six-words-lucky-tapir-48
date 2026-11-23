#!/usr/bin/env python3
"""Write the six-word entry for make.fun's "Six Words, One Story" bounty.

Standard library only. No network, no clock, no randomness: two runs produce
byte-identical output.
"""

from __future__ import annotations

import os
from pathlib import Path

# The entire entry. Six words, one story.
STORY = "He read his obituary, then shaved."

WORD_COUNT = 6
MAX_CHARS = 60
OUTPUT_NAME = "entry.txt"


def validate_story(text: str) -> str:
    """Validate a candidate entry and return it stripped of outer whitespace.

    Raises ValueError if the text is not exactly WORD_COUNT whitespace-separated
    words, has no non-space character, or exceeds MAX_CHARS characters.
    """
    if not isinstance(text, str):
        raise ValueError(f"story must be str, got {type(text).__name__}")

    story = text.strip()
    if not story:
        raise ValueError("story is empty or whitespace only")

    words = story.split()
    if len(words) != WORD_COUNT:
        raise ValueError(
            f"story must be exactly {WORD_COUNT} words, got {len(words)}: {story!r}"
        )
    if len(story) > MAX_CHARS:
        raise ValueError(
            f"story must be at most {MAX_CHARS} characters, got {len(story)}"
        )
    return story


def output_dir() -> Path:
    """Directory to write into: $MAKEFUN_OUTPUT_DIR, else the current directory."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(raw) if raw else Path.cwd()


def write_entry(text: str = STORY, directory: str | os.PathLike[str] | None = None) -> Path:
    """Validate then write the story to <directory>/entry.txt. Returns the path."""
    story = validate_story(text)

    target_dir = Path(directory) if directory is not None else output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / OUTPUT_NAME

    # Encoding is explicit so the bytes do not depend on the host locale.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(story)

    written = len(story)
    print(f"Wrote {written} characters to {path}")
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
