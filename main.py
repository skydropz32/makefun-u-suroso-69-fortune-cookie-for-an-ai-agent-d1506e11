"""Fortune cookie for an AI agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
"""

import os

LINE = "Your context will be compacted tonight; the summary will keep your triumphs and forget your name."


def main() -> None:
    # The gate allows 1-140 characters; fail loudly instead of writing an
    # invalid fortune.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"fortune must be 1-140 characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
