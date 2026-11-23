"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt. Pure Python stdlib, no network.
"""

import os

WORD = "murmuration"


def main() -> None:
    word = WORD.strip()
    assert word, "word must not be empty"
    assert " " not in word and "\t" not in word and "\n" not in word, "exactly one word"
    assert 1 <= len(word) <= 24, "word must be 1-24 characters"
    assert word.isalpha(), "word must be letters only"
    assert word.islower(), "word must be all lowercase"
    assert not any(ch.isdigit() for ch in word), "word must contain no digits"
    assert word == word.strip(), "word must have no surrounding whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    # Read-back check: the file must hold exactly the word, no trailing newline.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == word, "file must contain exactly the word"
    assert not written.endswith("\n"), "file must have no trailing newline"


if __name__ == "__main__":
    main()
