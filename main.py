"""One-Line Laugh-Off entry: prints the joke and writes it to /output/entry.txt."""

import os

# The line stays byte-identical to entry.txt; the gate allows 1-200 chars.
LINE = "My smart fridge sighs every time I open it at 2 a.m., which is officially the closest thing I have to a relationship."


def get_line():
    return LINE


def main():
    print(get_line(), end="")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(get_line())


if __name__ == "__main__":
    main()
