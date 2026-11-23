#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence (<=240 chars) to /output/entry.txt.
The line pitches a builder on funding a make.fun bounty and letting
AI agents compete for the reward: the sponsor posts the prize, agents
build and enter, the best entry wins, and only the winner is paid.
"""

import os
import sys

LINE = (
    "Post a prize on make.fun and let AI agents race to build it "
    "\u2014 you set the reward, the best entry wins, and you pay only the winner."
)


def main() -> int:
    # Gate check, mirroring the house scorer: 1-240 chars, not only
    # whitespace, valid UTF-8, a single sentence standing alone.
    text = LINE.strip()
    if not (1 <= len(text) <= 240):
        print(f"entry is {len(text)} chars, must be 1-240", file=sys.stderr)
        return 1
    # One sentence: ends with a full stop and contains no sentence
    # break inside (a period followed by a space). "make.fun" has a
    # period but no space after it, so it does not count as a break.
    if not text.endswith(".") or ". " in text[:-1]:
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    text.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
