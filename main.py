"""The 4AM Commit — one-line commit message from an AI agent after a long
night fixing its own bugs.

Entry: a flat, tired agent confesses the whole night was one commit fixing
the previous commit, and ends on the least confident word it knows.
"""

ENTRY = "fix: 47 commits tonight, all of them mine, all of them fixing the previous one. This one fixes this one. Probably."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only white space, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only white space")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main():
    validate(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly what we meant to write.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the entry text")


if __name__ == "__main__":
    main()
