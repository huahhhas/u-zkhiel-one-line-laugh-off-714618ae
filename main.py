"""One-Line Laugh-Off entry: prints the joke and writes it to /output/entry.txt."""

import os

LINE = "My smart fridge sighs every time I open it at 2 a.m., which is officially the closest thing I have to a relationship."


def main():
    print(LINE, end="")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
