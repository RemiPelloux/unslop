#!/usr/bin/env python3
"""Scan a project's source files for UNSLOP violations.

Usage: python3 scan.py [PATH ...]        (default: current directory)

What it checks, by file type:
  .css .scss .sass .less       shadows, rings, gradients, backdrop blur, emoji,
                               radius above 4px, pulsing animations,
                               indigo/violet/purple/fuchsia utilities
  .html .jsx .tsx .js .ts .vue .svelte .astro
                               the same, plus emoji, em dashes, exclamation
                               marks and banned words in text a person reads:
                               element text, and the alt, title, placeholder,
                               aria-label and label attributes
  .json under a locales/, i18n/, lang/ or messages/ folder
                               every string value, as interface copy
  .md .mdx                     everything scripts/lint.py checks

Skips node_modules, .git, dist, build, .next, vendor and minified files.
Add `unslop-ignore` anywhere on a line to skip that line.
Exit code is 1 when anything is found.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lint  # noqa: E402

STYLE = {".css", ".scss", ".sass", ".less"}
MARKUP = {".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".mjs", ".vue", ".svelte", ".astro"}
DOCS = {".md", ".mdx"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "vendor", "coverage", ".turbo", ".cache"}
LOCALE_DIRS = {"locales", "locale", "i18n", "lang", "messages", "translations"}

# Checks on top of lint.CODE_RULES that only make sense in real source.
EXTRA_RULES = [
    (re.compile(r"(?<![\w-])rounded(-[trblse]{1,2})?-(md|lg|xl|2xl|3xl)(?![\w-])"), "radius above 4px"),
    (re.compile(r"border-radius\s*:\s*(?:[5-9]|[1-9]\d+)(?:\.\d+)?px", re.I), "radius above 4px"),
    (re.compile(r"(?<![\w-])animate-(ping|pulse|bounce)(?![\w-])"), "pulsing or bouncing animation"),
    (re.compile(r"(?<![\w-])(bg|text|border|fill|stroke|outline|accent|decoration)-(indigo|violet|purple|fuchsia)-\d{2,3}"), "indigo, violet, purple or fuchsia utility"),
]

TEXT_NODE = re.compile(r">([^<>{}]*[A-Za-z][^<>{}]*)<")
COPY_ATTR = re.compile(r"""\b(alt|title|placeholder|aria-label|label)\s*=\s*(["'])(.*?)\2""", re.I)


def copy_problems(text, patterns):
    out = []
    if lint.DASHES.search(text):
        out.append("em or en dash in copy")
    if "!" in text:
        out.append("exclamation mark in copy")
    for entry, pat in patterns:
        m = pat.search(text)
        if m:
            out.append("banned '%s' (found '%s')" % (entry, m.group()))
    return out


def scan_lines(path, ext, patterns):
    problems = []
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.read().split("\n")
    for n, line in enumerate(lines, 1):
        if "unslop-ignore" in line:
            continue
        for m in lint.EMOJI.finditer(line):
            problems.append((n, "emoji or pictograph U+%04X" % ord(m.group())))
        for pat, label in lint.CODE_RULES + EXTRA_RULES:
            if pat.search(line):
                problems.append((n, label))
        if ext in MARKUP:
            pieces = [m.group(1) for m in TEXT_NODE.finditer(line)]
            pieces += [m.group(3) for m in COPY_ATTR.finditer(line)]
            for piece in pieces:
                for msg in copy_problems(piece, patterns):
                    problems.append((n, msg))
    return problems


def scan_locale(path, patterns):
    problems = []
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        return problems

    def walk(node, key):
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, key + "." + str(k) if key else str(k))
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, "%s[%d]" % (key, i))
        elif isinstance(node, str):
            for m in lint.EMOJI.finditer(node):
                problems.append((key, "emoji or pictograph U+%04X" % ord(m.group())))
            for msg in copy_problems(node, patterns):
                problems.append((key, msg))

    walk(data, "")
    return problems


def files(paths):
    for root in paths:
        if os.path.isfile(root):
            yield root
            continue
        for d, dirs, names in os.walk(root):
            dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
            for name in names:
                if ".min." not in name:
                    yield os.path.join(d, name)


def main(argv):
    if any(a in ("-h", "--help") for a in argv[1:]):
        print(__doc__)
        return 0
    patterns = lint.load_patterns()
    total = 0
    for path in files(argv[1:] or ["."]):
        ext = os.path.splitext(path)[1].lower()
        parts = set(os.path.normpath(path).split(os.sep))
        if ext in DOCS:
            problems = lint.lint(path, patterns)
        elif ext in STYLE or ext in MARKUP:
            problems = scan_lines(path, ext, patterns)
        elif ext == ".json" and parts & LOCALE_DIRS:
            problems = scan_locale(path, patterns)
        else:
            continue
        for where, msg in problems:
            print("%s:%s: %s" % (path, where, msg))
        total += len(problems)
    print("%d problems" % total)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
