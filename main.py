#!/usr/bin/env python3
"""Write one funny one-star cat review to /output/entry.txt.

Deterministic, stdlib-only: the review text is a fixed literal, so every
run writes byte-identical output.
"""
import os

REVIEW = (
    "One star. He bought a heated cat bed, then sat in it himself. "
    "I now sleep on his laptop. He works standing up."
)


def review():
    """Return the single-line review, validated against the gate."""
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"review is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "review must be a single line"
    return text


def main():
    text = review()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
