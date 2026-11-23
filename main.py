"""Make the Judge Smile — entry program.

Writes one line (at most 200 characters) about a small good thing
that happened today to /output/entry.txt, and nothing else.
"""

from pathlib import Path

LINE = (
    "After two years of ignoring me, the neighbour's cat chose "
    "this rainy 6 a.m. to headbutt my ankle and purr like we were "
    "old friends."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 200 characters that is not only white space.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
