#!/usr/bin/env python3
"""Build UNSLOP.md from src/parts/*.md.

Concatenates the parts in filename order, appends the generated appendix
(full banned list and lexicon index), replaces the <!-- TOC --> marker with
a table of contents for ## and ### headings, then runs the linter on the
result, then packages the skill and adapters (scripts/build_skill.py).
Exit code is non-zero if the linter finds anything.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, "src", "parts")
WORDS = os.path.join(ROOT, "src", "banned-words.txt")
OUT = os.path.join(ROOT, "UNSLOP.md")


def slugify(text, seen):
    s = text.strip().lower().replace("`", "")
    s = re.sub(r"[^\w\- ]", "", s)
    s = s.replace(" ", "-")
    n = seen.get(s, 0)
    seen[s] = n + 1
    return s if n == 0 else "%s-%d" % (s, n)


def headings(md):
    """Return (level, text, slug) for every heading outside code fences."""
    out, seen, fence = [], {}, None
    for line in md.split("\n"):
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if m:
            if fence is None:
                fence = m.group(1)
            elif line.strip().startswith(fence):
                fence = None
            continue
        if fence is not None:
            continue
        h = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if h:
            text = h.group(2)
            out.append((len(h.group(1)), text, slugify(text, seen)))
    return out


def load_groups():
    groups, current = [], None
    with open(WORDS, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# ---"):
                current = (line.strip("# -"), [])
                groups.append(current)
            elif line and not line.startswith("#"):
                current[1].append(line)
    return groups


def appendix():
    groups = load_groups()
    lines = [
        "## Part 10. Appendix",
        "",
        "### 10.1 The 350 banned entries",
        "",
        "The source of truth is `src/banned-words.txt`. The list below is generated from it at build time. "
        "Single words are banned in every inflection; phrases are banned as written, with any whitespace "
        "and either apostrophe.",
        "",
    ]
    n = 0
    for name, words in groups:
        first = n + 1
        n += len(words)
        lines.append("#### %s, %03d to %03d" % (name.capitalize(), first, n))
        lines.append("")
        lines.append("```slop")
        for i, w in enumerate(words, first):
            lines.append("%03d  %s" % (i, w))
        lines.append("```")
        lines.append("")
    lines += [
        "### 10.2 Lexicon index",
        "",
        "Each entry links to its full treatment in Part 7.",
        "",
        "| No. | Entry | Group |",
        "| --- | --- | --- |",
    ]
    n = 0
    for name, words in groups:
        for w in words:
            n += 1
            anchor = slugify("%03d. `%s`" % (n, w), {})
            lines.append("| %03d | [`%s`](#%s) | %s |" % (n, w, anchor, name))
    lines.append("")
    return "\n".join(lines)


def toc(md):
    lines = ["## Contents", ""]
    for level, text, slug in headings(md):
        if level == 2 and text != "Contents":
            lines.append("- [%s](#%s)" % (text, slug))
        elif level == 3:
            lines.append("  - [%s](#%s)" % (text, slug))
    return "\n".join(lines) + "\n"


def main():
    files = sorted(f for f in os.listdir(PARTS) if f.endswith(".md"))
    chunks = []
    for name in files:
        with open(os.path.join(PARTS, name), encoding="utf-8") as f:
            chunks.append(f.read().strip("\n"))
    body = "\n\n".join(chunks) + "\n\n" + appendix()
    # Build the TOC against the text it will live in, so slugs match.
    contents = toc(body.replace("<!-- TOC -->", "", 1))
    body = body.replace("<!-- TOC -->", contents, 1)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote %s from %d parts" % (os.path.relpath(OUT, ROOT), len(files)))
    status = subprocess.call([sys.executable, os.path.join(ROOT, "scripts", "lint.py"), OUT])
    status |= subprocess.call([sys.executable, os.path.join(ROOT, "scripts", "build_skill.py")])
    return status


if __name__ == "__main__":
    sys.exit(main())
