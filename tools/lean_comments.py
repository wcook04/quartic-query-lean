#!/usr/bin/env python3
"""Remove comments from Lean 4 source, leaving every other byte in place.

Used to show that a source edit touched comments only. Handles `--` line
comments, nested `/- ... -/` block comments (including `/--` and `/-!`), string
literals with escapes, and character literals, so comment markers inside a
string or a character are kept as code. Comment text is removed; the line break
ending a `--` comment is kept.
"""


def strip_comments(text):
    out = []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if text.startswith("/-", i):
            depth, i = 1, i + 2
            while i < n and depth:
                if text.startswith("/-", i):
                    depth, i = depth + 1, i + 2
                elif text.startswith("-/", i):
                    depth, i = depth - 1, i + 2
                else:
                    i += 1
            if depth:
                raise ValueError("unterminated block comment")
        elif text.startswith("--", i):
            while i < n and text[i] != "\n":
                i += 1
        elif c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            if j >= n:
                raise ValueError("unterminated string literal")
            out.append(text[i:j + 1])
            i = j + 1
        elif (c == "'" and i + 2 < n and not (i and (text[i - 1].isalnum() or text[i - 1] in "_'!?."))
              and (text[i + 2] == "'" or (text[i + 1] == "\\" and "'" in text[i + 2:i + 12]))):
            j = text.index("'", i + 2 if text[i + 1] != "\\" else i + 3)
            out.append(text[i:j + 1])
            i = j + 1
        else:
            out.append(c)
            i += 1
    return "".join(out)
