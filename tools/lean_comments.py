#!/usr/bin/env python3
"""Replace comments in Lean 4 source by a single space, keeping every line break.

Used to show that a source edit touched comments only. Two texts are taken to
differ in comments alone when their stripped forms are identical. The scanner
recognises, so that comment markers inside them stay code:

- ordinary strings with escapes (including `s!"..."` and other prefixed forms);
- raw strings `r"..."`, `r#"..."#`, `r##"..."##` and so on;
- character literals;
- guillemet identifiers `«...»`, in which `--` and `/-` are ordinary characters.

A `--` comment and a nested `/- ... -/` block (including `/--` and `/-!`) each
become one space, so a comment that separated two tokens still separates them.
Line breaks inside a block comment are kept, so every line of code keeps its line
number. Anything the scanner cannot close raises ValueError rather than guessing.
"""

IDENT = set("_'!?.")


def _ident_char(c):
    return c.isalnum() or c in IDENT or ord(c) > 127


def _raw_string_end(text, i):
    """If a raw string starts at i, return the index just past it, else None."""
    if text[i] != "r" or (i and _ident_char(text[i - 1])):
        return None
    j = i + 1
    while j < len(text) and text[j] == "#":
        j += 1
    if j >= len(text) or text[j] != '"':
        return None
    close = '"' + "#" * (j - i - 1)
    end = text.find(close, j + 1)
    if end < 0:
        raise ValueError("unterminated raw string literal")
    return end + len(close)


def strip_comments(text):
    out = []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if text.startswith("/-", i):
            depth, j = 1, i + 2
            while j < n and depth:
                if text.startswith("/-", j):
                    depth, j = depth + 1, j + 2
                elif text.startswith("-/", j):
                    depth, j = depth - 1, j + 2
                else:
                    j += 1
            if depth:
                raise ValueError("unterminated block comment")
            out.append(" " + "\n" * text.count("\n", i, j))
            i = j
        elif text.startswith("--", i):
            while i < n and text[i] != "\n":
                i += 1
            out.append(" ")
        elif c == "«":
            j = text.find("»", i + 1)
            if j < 0:
                raise ValueError("unterminated guillemet identifier")
            out.append(text[i:j + 1])
            i = j + 1
        elif (end := _raw_string_end(text, i)) is not None:
            out.append(text[i:end])
            i = end
        elif c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            if j >= n:
                raise ValueError("unterminated string literal")
            out.append(text[i:j + 1])
            i = j + 1
        elif (c == "'" and i + 2 < n and not (i and _ident_char(text[i - 1]))
              and (text[i + 2] == "'" or (text[i + 1] == "\\" and "'" in text[i + 2:i + 12]))):
            j = text.index("'", i + 2 if text[i + 1] != "\\" else i + 3)
            out.append(text[i:j + 1])
            i = j + 1
        else:
            out.append(c)
            i += 1
    return "".join(out)
