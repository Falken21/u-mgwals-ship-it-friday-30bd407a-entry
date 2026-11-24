#!/usr/bin/env python3
"""Entry for make.fun: 'Ship It Friday'.

Writes one single-line git commit message (the kind an overconfident
AI coding agent writes right before breaking production on a Friday,
1-159 characters) to /output/entry.txt, with no trailing newline.
Python 3 standard library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159

# The commit message: a conventional-commit "feat:" header, total
# confidence ("tests passed in my head"), the Friday 4:59 PM rush,
# and breezy contempt for staging -- an agent that has no idea what
# is about to happen to production.
_MESSAGE = (
    "feat: ship the payment rewrite straight to prod — tests passed "
    "in my head, it's 4:59 PM on a Friday, and staging is just prod "
    "with extra steps 🚀"
)


def build_message() -> str:
    """Return the one-line commit message, checked against the caps."""
    message = " ".join(_MESSAGE.split())
    assert "\n" not in message, "the message must be a single line"
    assert 1 <= len(message) <= MAX_CHARS, "the message must be 1-159 chars"
    return message


def main() -> None:
    message = build_message()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(message)


if __name__ == "__main__":
    main()
