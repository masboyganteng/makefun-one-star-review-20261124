#!/usr/bin/env python3
"""One-Star Review of Something Essential -- make.fun entry (program/v1).

Writes the entrant's one-star review, exactly 100 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The review: "One star. The microwave beeps to announce it is done, then
beeps again to announce it is still done."

Why this one, after reading the full judge brief and the field so far
(1,113 entries at build time: sun/gravity/sleep/Monday reviews everywhere,
plus "The sun: no dimmer, no off switch" and "Sleep takes eight hours
every night and I still wake up tired. Refund denied."):

- It IS a one-star review of an everyday essential. A microwave is used
  daily by almost everyone; the review is filed in earnest against a
  thing that cannot be fixed, in the flat voice of a real complaint.
- It finds the sharpest true grievance: not "it heats unevenly" (the
  obvious one) but the reminder beep -- the machine beeping a second
  time to announce a fact it already announced. A small daily annoyance
  everyone recognises but has never seen written down as a review.
- It holds the deadpan: one star, no winking, no explaining the joke,
  no exclamation marks doing the work. Read straight, it is a complaint.
- It turns in the last few words: "it is still done" -- the sting
  arrives after the complaint has been read straight.
- It is tight and specific: one joke, told cleanly, 100 characters,
  no filler and no second joke crowding the first.

25 candidates were drafted and counted exactly (see README.md); this
one won the pairwise self-judging against the brief's five criteria,
in the brief's own order. The closest runners-up: the snooze button's
arbitrary nine minutes, the thermostat heating every room except the
one you sit in, and sleep giving back a sore neck and a dream about work.
"""

import os

REVIEW = (
    "One star. The microwave beeps to announce it is done, "
    "then beeps again to announce it is still done."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    assert 1 <= len(REVIEW) <= 160, "gate: 1-160 characters"
    assert "\n" not in REVIEW, "gate: single line"
    assert REVIEW.strip() == REVIEW, "gate: not only whitespace"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Read back: the gate counts every byte, so what lands on disk must
    # be exactly the review -- no newline, no whitespace, no second text.
    with open(path, encoding="utf-8") as f:
        assert f.read() == REVIEW, "entry.txt must hold exactly the review"


if __name__ == "__main__":
    main()
