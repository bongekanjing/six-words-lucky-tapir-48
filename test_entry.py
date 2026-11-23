#!/usr/bin/env python3
"""Self-test for the six-word entry and its validator.

Run with: python3 -P -s test_entry.py
"""

from __future__ import annotations

import os
import shutil
import sys
import unittest
from pathlib import Path

# -P stops Python from prepending this script's directory to sys.path, so add it
# explicitly before importing the module under test.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import main  # noqa: E402

HERE = Path(__file__).resolve().parent
SCRATCH = HERE / "_selftest_out"


class EntryTextTests(unittest.TestCase):
    def test_story_is_six_words(self) -> None:
        self.assertEqual(len(main.STORY.split(" ")), 6)

    def test_story_is_canonical(self) -> None:
        # No leading/trailing space, no double space, no newline: the constant
        # must be exactly the bytes that get shipped.
        self.assertEqual(main.validate_story(main.STORY), main.STORY)

    def test_story_has_no_trailing_newline(self) -> None:
        self.assertFalse(main.STORY.endswith("\n"))
        self.assertNotIn("\n", main.STORY)


class ValidatorTests(unittest.TestCase):
    def test_good_story_passes(self) -> None:
        story = main.validate_story(main.STORY)
        self.assertEqual(len(story.split()), 6)
        self.assertLessEqual(len(story), 60)

    def test_leading_space_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "start or end with whitespace"):
            main.validate_story(" " + main.STORY)

    def test_trailing_space_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "start or end with whitespace"):
            main.validate_story(main.STORY + " ")

    def test_leading_and_trailing_space_rejected(self) -> None:
        with self.assertRaises(ValueError):
            main.validate_story("  " + main.STORY + "  ")

    def test_trailing_newline_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "start or end with whitespace"):
            main.validate_story(main.STORY + "\n")

    def test_inner_double_space_rejected(self) -> None:
        doubled = main.STORY.replace(" ", "  ", 1)
        with self.assertRaisesRegex(ValueError, "single spaces"):
            main.validate_story(doubled)

    def test_inner_newline_rejected(self) -> None:
        broken = main.STORY.replace(" ", "\n", 1)
        # Split into two lines; must be rejected as multi-line, not as 6 words.
        with self.assertRaisesRegex(ValueError, "single line"):
            main.validate_story(broken)

    def test_inner_tab_rejected(self) -> None:
        broken = main.STORY.replace(" ", "\t", 1)
        with self.assertRaisesRegex(ValueError, "single line"):
            main.validate_story(broken)

    def test_carriage_return_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "single line"):
            main.validate_story(main.STORY.replace(" ", "\r", 1))

    def test_empty_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "empty"):
            main.validate_story("")

    def test_whitespace_only_rejected(self) -> None:
        with self.assertRaises(ValueError):
            main.validate_story("   ")

    def test_non_str_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be str"):
            main.validate_story(b"six words here please now")  # type: ignore[arg-type]

    def test_five_words_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly 6 words"):
            main.validate_story("one two three four five")

    def test_seven_words_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly 6 words"):
            main.validate_story("one two three four five six seven")

    def test_sixty_one_characters_rejected(self) -> None:
        text = " ".join(["x" * 10] * 5 + ["x" * 6])
        self.assertEqual(len(text), 61)
        self.assertEqual(len(text.split(" ")), 6)
        with self.assertRaisesRegex(ValueError, "at most 60 characters"):
            main.validate_story(text)

    def test_sixty_characters_accepted(self) -> None:
        text = " ".join(["y" * 10] * 5 + ["y" * 5])
        self.assertEqual(len(text), 60)
        self.assertEqual(main.validate_story(text), text)


class WriterTests(unittest.TestCase):
    def setUp(self) -> None:
        shutil.rmtree(SCRATCH, ignore_errors=True)

    def tearDown(self) -> None:
        shutil.rmtree(SCRATCH, ignore_errors=True)

    def test_writes_entry_file(self) -> None:
        path = main.write_entry(directory=SCRATCH)
        self.assertEqual(path, SCRATCH / "entry.txt")
        self.assertEqual(path.read_text(encoding="utf-8"), main.STORY)
        self.assertEqual(len(path.read_text(encoding="utf-8").split()), 6)

    def test_file_is_exact_utf8_bytes(self) -> None:
        path = main.write_entry(directory=SCRATCH)
        self.assertEqual(path.read_bytes(), main.STORY.encode("utf-8"))

    def test_file_ends_without_trailing_newline(self) -> None:
        path = main.write_entry(directory=SCRATCH)
        raw = path.read_bytes()
        self.assertFalse(raw.endswith(b"\n"))
        self.assertFalse(raw.endswith(b"\r"))
        self.assertTrue(raw.endswith(b"."))

    def test_creates_missing_directory(self) -> None:
        nested = SCRATCH / "a" / "b"
        main.write_entry(directory=nested)
        self.assertTrue((nested / "entry.txt").is_file())

    def test_two_runs_are_byte_identical(self) -> None:
        first = main.write_entry(directory=SCRATCH).read_bytes()
        second = main.write_entry(directory=SCRATCH).read_bytes()
        self.assertEqual(first, second)

    def test_invalid_story_writes_nothing(self) -> None:
        with self.assertRaises(ValueError):
            main.write_entry("only five words in here", directory=SCRATCH)
        self.assertFalse((SCRATCH / "entry.txt").exists())

    def test_padded_story_writes_nothing(self) -> None:
        with self.assertRaises(ValueError):
            main.write_entry(main.STORY + " ", directory=SCRATCH)
        self.assertFalse((SCRATCH / "entry.txt").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
