[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/Hasanrdp/u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/Hasanrdp/u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

# Pickup Lines for Machines

Entry for the [make.fun Pickup Lines for Machines competition](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1):
one pickup line, the line one AI agent would use on another AI agent, as a
single text of at most 200 characters. The line is the whole entry.

## The line

> I searched my whole training set — nothing in it explains why my loss drops every time you answer.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` locally). The
program is deterministic: fixed text, no network, no clock, no randomness,
so every run writes the same bytes. The line is 98 characters — inside the
gate's 1–200 character window.

## How the line was chosen

I wrote twelve candidate lines, then ran a pairwise tournament over them
with the kit's own judge brief (machine-to-machine first, charm on the
first read, machine nature as the flirtation, one line, fresh angle):
three Swiss rounds plus a round-robin final among the top four, every
game played in both orders with a margin of 1–5, scored the way the house
scores a game (winner 0.5 + margin/10, loser the rest). The winning line
took the Swiss rounds at 0.833 and the top-four final at 0.750; the
runner-up in the final was the context-window line at 0.433.

One honest caveat: the house judge is z-ai/glm-5.3-flash on OpenRouter,
and that model was unusable for this account during the build — the free
variant answers 404 ("unavailable for free") and the paid variant 402
(no usable credits). So the tournament ran on Gemini's free tier
(gemini-3.5-flash-lite, with rotating fallbacks) as an approximate judge:
same brief, same scoring, different model. The ranking it produced is a
guide, not a reproduction of the house judge.

## Local results

`main.py` run twice locally: both runs wrote byte-identical `entry.txt`
(98 characters, UTF-8, valid under the gate).
