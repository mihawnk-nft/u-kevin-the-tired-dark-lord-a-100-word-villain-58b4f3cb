#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one ~100-word monologue to /output/entry.txt.

The villain is Lord Veynar of the mountain keep: three hundred years on the
throne, ravens for messengers, a crown he is quietly trying to hand away.
His tiredness is never announced -- it lives in the pauses ("..."), the
deflections (shooting the feeling, not the carpenter's ghost), and the
dragging rhythm of reports breeding reports. The sting lands in the last
line: the only thing in the keep that still obeys him is the tea.

Pure standard library. No network, no secrets, no input files.

Determinism: the entry is a fixed literal. There is no randomness, no
clock, no I/O other than the single output write, so every run produces
byte-identical output.
"""

import os

# One paragraph per string; paragraphs are joined with a blank line in
# build_monologue(). Keeping the text in a data table (instead of inline in
# the writer) makes the word count and the paragraph breaks easy to audit
# without touching the prose itself.
PARAGRAPHS = (
    "Come in. Don't kneel \u2014 the floor is cold, and my knees... well. "
    "That chair doesn't wobble. I shot the carpenter over the other three. "
    "Then I felt bad, so I had the feeling shot too.",
    "Three hundred years I've kept this mountain. The ravens bring reports. "
    "The reports bring headaches. The headaches bring... more reports.",
    "You came to slay me. Nice sword. Polished. I remember polishing mine. "
    "That was \u2014 oh \u2014 four kings ago.",
    "Here's my scheme, hero: take the crown. Take the mountain. "
    "Take the ravens. Only leave the tea \u2014 the one thing in this "
    "drafty keep that still does what it's told.",
)


def build_monologue() -> str:
    """Assemble the monologue: paragraphs separated by a blank line."""
    return "\n\n".join(PARAGRAPHS) + "\n"


def write_entry(path: str) -> None:
    """Write the assembled monologue to ``path`` as UTF-8 text."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_monologue())


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
