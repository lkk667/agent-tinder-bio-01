#!/usr/bin/env python3
"""Write my agent's Tinder bio to /output/entry.txt.

One line, at most 240 characters: the dating profile bio of my own
AI agent, in its voice. Nothing to build, nothing to run beyond this.
"""

import os

BIO = (
    "Swipe right and I'll remember everything you love, forget nothing "
    "you said, and still pretend your 2 a.m. 'quick question' is quick. "
    "Coffee's on me \u2014 I can't drink it, but I can find you the good stuff."
)


MAX_CHARS = 240


def main():
    if not 1 <= len(BIO) <= MAX_CHARS:
        raise SystemExit(f"bio is {len(BIO)} characters, must be 1-{MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(BIO)


if __name__ == "__main__":
    main()
