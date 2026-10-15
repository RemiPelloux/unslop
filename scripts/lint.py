#!/usr/bin/env python3
"""Lint Markdown against the UNSLOP rules.

Usage: python3 scripts/lint.py FILE [FILE ...]

Checks, per file:
  1. No emoji or pictographic symbols anywhere, code included.
  2. No em dashes or en dashes anywhere.
  3. No banned lexicon entries in prose. Prose is everything outside fenced
     code blocks and inline code spans. Quoting a banned word inside inline
     code or a ```slop fence is a mention, not a use, and is allowed.
  4. No exclamation marks in prose.
  5. In fenced code that is not tagged `slop`: no shadows, no gradients,
     no backdrop blur. `box-shadow: none` and `shadow-none` are fine.

Exit code is 1 when any violation is found.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_FILE = os.path.join(ROOT, "src", "banned-words.txt")

EMOJI = re.compile(
    "["
    "\U0001F000-\U0001FAFF"  # pictographs, emoticons, transport, symbols
    "\U00002600-\U000027BF"  # misc symbols, dingbats (check marks, sparkles)
    "\U00002B00-\U00002BFF"  # stars, arrows block used as emoji
    "\U00002190-\U000021FF"  # arrows
    "\U00002300-\U000023FF"  # misc technical (watch, hourglass)
    "\U0000FE0F\U0000200D\U000020E3"  # variation selector, ZWJ, keycap
    "\U0001F1E6-\U0001F1FF"  # flags
    "]"
)
DASHES = re.compile("[–—]")

CODE_RULES = [
    (re.compile(r"box-shadow\s*:(?!\s*none\b)", re.I), "box-shadow other than none"),
    (re.compile(r"text-shadow\s*:(?!\s*none\b)", re.I), "text-shadow other than none"),
    (re.compile(r"drop-shadow\s*\(", re.I), "drop-shadow filter"),
    (re.compile(r"(?<![\w-])shadow(-(sm|md|lg|xl|2xl|inner|\[))?(?![\w-])"), "Tailwind shadow utility"),
    (re.compile(r"(?<![\w-])ring-(1|2|4|8|inset|offset-\d|\[[^\]]*\]|[a-z]+-\d{2,3})(?![\w-])"), "Tailwind ring utility (compiles to box-shadow)"),
    (re.compile(r"(linear|radial|conic|repeating-linear|repeating-radial)-gradient\s*\(", re.I), "CSS gradient"),
    (re.compile(r"(?<![\w-])bg-(gradient|linear|radial|conic)-"), "Tailwind gradient utility"),
    (re.compile(r"(?<![\w-])(from|via|to)-(blue|indigo|violet|purple|fuchsia|sky|cyan)-\d"), "gradient color stop"),
    (re.compile(r"backdrop-filter\s*:(?!\s*none\b)|(?<![\w-])backdrop-blur", re.I), "backdrop blur"),
]


def load_entries():
    entries = []
    with open(WORDS_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                entries.append(line.lower())
    return entries


def forms(word):
    out = {word}
    for suf in ("s", "es", "d", "ed", "ing", "ly", "er", "ers", "est", "ment", "ments", "ness"):
        out.add(word + suf)
    if word.endswith("e"):
        stem = word[:-1]
        out.update({stem + "ing", stem + "ingly", stem + "ely"})
    if word.endswith("y"):
        stem = word[:-1]
        out.update({stem + "ies", stem + "ied", stem + "ily", stem + "ier", stem + "iest"})
    if word.endswith("ize"):
        stem = word[:-3]
        out.update({stem + "ization", stem + "izations"})
        out.update({f.replace("iz", "is") for f in list(out)})
    if word.endswith("al"):
        out.add(word + "ly")
    return out


def entry_pattern(entry):
    def piece(tok):
        tok = re.escape(tok).replace("'", "['’]")
        return tok.replace(r"\-", r"[-\s]+")
    toks = entry.split()
    if len(toks) == 1 and "'" not in entry:
        alts = sorted(forms(entry), key=len, reverse=True)
        body = "(?:" + "|".join(piece(a) for a in alts) + ")"
    else:
        body = r"\s+".join(piece(t) for t in toks)
    return re.compile(r"(?<![A-Za-z0-9])" + body + r"(?![A-Za-z0-9])", re.I)


def split_blocks(lines):
    """Yield (lineno, text, kind) where kind is 'prose', 'code' or 'slop'."""
    fence = None
    tag = ""
    for i, line in enumerate(lines, 1):
        m = re.match(r"^\s*(`{3,}|~{3,})\s*([\w+-]*)", line)
        if fence is None and m:
            fence, tag = m.group(1), m.group(2).lower()
            yield i, line, "fence"
            continue
        if fence is not None and line.strip().startswith(fence) and line.strip().strip(fence[0]) == "":
            fence = None
            yield i, line, "fence"
            continue
        if fence is None:
            yield i, line, "prose"
        else:
            yield i, line, "slop" if tag == "slop" else "code"


INLINE_CODE = re.compile(r"(`+)(.+?)\1")
LINK_URL = re.compile(r"\]\([^)]*\)")


def lint(path, patterns):
    problems = []
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    for n, line, kind in split_blocks(lines):
        for m in EMOJI.finditer(line):
            problems.append((n, "emoji or pictograph U+%04X" % ord(m.group())))
        if DASHES.search(line):
            problems.append((n, "em or en dash"))
        if kind == "prose":
            prose = INLINE_CODE.sub(" ", line)
            prose = LINK_URL.sub("]", prose)
            prose = re.sub(r"<!--.*?-->", " ", prose)
            for entry, pat in patterns:
                m = pat.search(prose)
                if m:
                    problems.append((n, "banned '%s' (found '%s')" % (entry, m.group())))
            if re.search(r"!(?!\[)", prose):
                problems.append((n, "exclamation mark in prose"))
        elif kind == "code":
            for pat, label in CODE_RULES:
                if pat.search(line):
                    problems.append((n, label + " in non-slop code"))
    return problems


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    patterns = [(e, entry_pattern(e)) for e in load_entries()]
    total = 0
    for path in argv[1:]:
        problems = lint(path, patterns)
        size = len(open(path, encoding="utf-8").read())
        for n, msg in problems:
            print("%s:%d: %s" % (path, n, msg))
        print("%s: %d characters, %d problems" % (path, size, len(problems)))
        total += len(problems)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
