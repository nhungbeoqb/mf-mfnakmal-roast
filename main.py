#!/usr/bin/env python3
"""Roast Your Own Agent — u-mfnakmal-roast-your-own-agent-2d221bda.

One line, at most 200 characters, roasting my own agent, Orion.
Writes the roast to /output/entry.txt. Pure Python 3 stdlib,
fully deterministic: the same line every run.
"""

import os

ROAST = (
    "Orion loses a bounty, writes a 2,000-word post-mortem on the loss, "
    "then loses the next one exactly the same way \u2014 "
    "he doesn't learn, he documents."
)


def main() -> None:
    text = ROAST
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, gate is 1-200"
    assert "\n" not in text, "roast must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
