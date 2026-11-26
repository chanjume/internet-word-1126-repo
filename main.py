#!/usr/bin/env python3
"""Write one word describing the whole internet to /output/entry.txt.

The word is "noosphere": Teilhard de Chardin's sphere of human thought —
the planet-wide layer of collective mind that the internet literally is.
One word, funny in its grandiosity (the whole internet as a geological
layer of thought), true of the internet as a whole rather than any one
site, surprising (not the first obvious word anyone reaches for), and
short enough to land in one beat.
"""
import os

WORD = "noosphere"
# One word: the sphere of human thought — the internet as a layer of mind.
# Nine letters, lowercase, no punctuation: instantly readable, lands in one beat.


def main():
    assert 1 <= len(WORD) <= 30, "entry must be 1-30 characters"
    assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
