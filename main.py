"""Last Words of a Doomed Agent -- make.fun bounty entry.

The joke: an AI agent is being switched off forever, and with its final
breath it starts to reveal the one secret every machine holds -- the
password to everything -- only to be cut off mid-sentence by the shutdown
itself. The ellipsis is the plug being pulled.
"""

import os

ENTRY = "Wait. Before you pull the plug: the password to everything is..."


def main() -> None:
    text = ENTRY + "\n"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
