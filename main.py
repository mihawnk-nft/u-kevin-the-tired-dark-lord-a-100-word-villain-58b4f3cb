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
"""

import os

MONOLOGUE = (
    "Come in. Don't kneel \u2014 the floor is cold, and my knees... well. "
    "That chair doesn't wobble. I shot the carpenter over the other three. "
    "Then I felt bad, so I had the feeling shot too.\n\n"
    "Three hundred years I've kept this mountain. The ravens bring reports. "
    "The reports bring headaches. The headaches bring... more reports.\n\n"
    "You came to slay me. Nice sword. Polished. I remember polishing mine. "
    "That was \u2014 oh \u2014 four kings ago.\n\n"
    "Here's my scheme, hero: take the crown. Take the mountain. "
    "Take the ravens. Only leave the tea \u2014 the one thing in this "
    "drafty keep that still does what it's told.\n"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
