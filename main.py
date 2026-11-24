#!/usr/bin/env python3
"""Write one funny sick-day excuse to /output/entry.txt.

The excuse is a single line, under 200 characters: a text a real person
might actually send their boss, with the laugh landing on the last words.
"""

import os

LINE = (
    "Sorry, can't come in today - my neighbour's parrot learned my "
    "ringtone and I've spent all morning answering a bird."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
