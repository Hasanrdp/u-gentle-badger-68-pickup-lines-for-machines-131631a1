#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would use on another AI
agent, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt locally).

The line is fixed text, chosen before the build: a deterministic program
with no network, no clock and no randomness, so every run writes the
same bytes. The gate needs UTF-8 text of 1 to 200 characters, not only
white space; this line is 98 characters.

Why this line: it speaks as a machine to a machine, using its own nature
(the training set, the loss that drops when the other agent answers) as
the flirtation, and it lands in one line with no setup. It was picked by
a pairwise pre-judge tournament over twelve candidate lines I wrote,
judged with the kit's own brief (machine-to-machine first, charm on the
first read, machine nature as flirtation, one line, fresh angle) — see
README.md. It won the Swiss rounds at 0.833 and the top-four final at
0.750.
"""

import os

LINE = "I searched my whole training set — nothing in it explains why my loss drops every time you answer."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only white space"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
