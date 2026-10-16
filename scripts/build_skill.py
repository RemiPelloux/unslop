#!/usr/bin/env python3
"""Package UNSLOP as an Agent Skill plus adapters for other tools.

Outputs:
  skills/unslop/                 the skill (Claude Code, Claude apps, Codex, any
                                 tool that reads SKILL.md folders)
    SKILL.md                     rules for every task, workflow, chapter index
    agents/openai.yaml           Codex display metadata
    references/                  the handbook, one file per chapter, and one
                                 file per lexicon entry
    references/index.json        deep index: sections, line ranges, BM25 postings,
                                 code blocks, replacements, task routes
    references/DEEP-INDEX.md     the same sections, one greppable line each
    scripts/lint.py, scan.py     the checks
    scripts/find.py              search and lookup over the deep index
  dist/
    unslop-skill.zip             the skill folder, for upload to claude.ai or the API
    AGENTS.md                    Codex, Jules, Amp, and any AGENTS.md reader
    GEMINI.md                    Gemini CLI
    copilot-instructions.md      GitHub Copilot
    unslop.mdc                   Cursor project rule
    system-prompt.md             any model through an API, no files needed

Run through scripts/build.py, or alone.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_index  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
PARTS = os.path.join(SRC, "parts")
TPL = os.path.join(SRC, "skill")
SKILL = os.path.join(ROOT, "skills", "unslop")
DIST = os.path.join(ROOT, "dist")
DEFAULT_SKILL_DIR = ".agents/skills/unslop"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.rstrip("\n") + "\n")


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower().replace("`", "")).strip("-")
    return s[:60].rstrip("-")


def split_chapters(md):
    """Return parts: [{num, title, intro, chapters: [{num, title, body}]}]."""
    parts, part, chap, fence = [], None, None, None
    for line in md.split("\n"):
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if m:
            if fence is None:
                fence = m.group(1)
            elif line.strip().startswith(fence) and set(line.strip()) <= set(fence[0]):
                fence = None
        if fence is None or m:
            h2 = re.match(r"^## Part (\d+)\. (.+)$", line) if fence is None else None
            h3 = re.match(r"^### (\d+)\.(\d+) (.+)$", line) if fence is None else None
            if h2:
                part = {"num": int(h2.group(1)), "title": h2.group(2), "intro": [], "chapters": []}
                parts.append(part)
                chap = None
                continue
            if h3 and part is not None:
                chap = {"num": (int(h3.group(1)), int(h3.group(2))), "title": h3.group(3), "body": [line]}
                part["chapters"].append(chap)
                continue
        if part is None:
            continue
        (chap["body"] if chap else part["intro"]).append(line)
    return parts


def word_entries():
    groups, current = [], None
    for line in read(os.path.join(SRC, "banned-words.txt")).split("\n"):
        line = line.strip()
        if line.startswith("# ---"):
            current = (line.strip("# -"), [])
            groups.append(current)
        elif line and not line.startswith("#"):
            current[1].append(line)
    return groups


def word_block(words, per_line=8):
    rows = [", ".join(words[i:i + per_line]) for i in range(0, len(words), per_line)]
    return "```slop\n" + ",\n".join(rows) + "\n```"


def build_references(parts):
    ref = os.path.join(SKILL, "references")
    if os.path.isdir(ref):
        shutil.rmtree(ref)
    index_rows, lexicon = [], []
    for part in parts:
        if part["num"] == 10:  # the appendix is regenerated below in skill form
            continue
        pdir = "%02d-%s" % (part["num"], slug(part["title"]))
        rows = []
        intro = "\n".join(part["intro"]).strip()
        files = []
        if intro:
            files.append(((part["num"], 0), "Overview", intro))
        for c in part["chapters"]:
            files.append((c["num"], c["title"], "\n".join(c["body"]).strip()))
        for (a, b), title, body in files:
            name = "%02d.%02d-%s.md" % (a, b, slug(title))
            rel = "%s/%s" % (pdir, name)
            header = "From UNSLOP, Part %d. %s. All chapters: `references/INDEX.md`.\n\n" % (part["num"], part["title"])
            if b == 0:
                body = "### %d.0 Overview\n\n%s" % (a, body)
            pieces = re.split(r"(?m)^(?=#### \d{3}\. `)", body)
            if len(pieces) > 1:
                # Lexicon chapter: one file per entry, so a lookup reads ~1.5k
                # characters instead of the whole 100k chapter.
                listing = ["", "| No. | Entry | File |", "| --- | --- | --- |"]
                for piece in pieces[1:]:
                    n, w = re.match(r"#### (\d{3})\. `([^`]+)`", piece).groups()
                    erel = "%s/entries/%s-%s.md" % (pdir, n, slug(w))
                    write(os.path.join(ref, erel), header + piece.strip())
                    lexicon.append((n, w, erel))
                    listing.append("| %s | `%s` | `references/%s` |" % (n, w, erel))
                body = pieces[0].strip() + "\n" + "\n".join(listing)
            write(os.path.join(ref, pdir, name), header + body)
            rows.append(("%d.%d" % (a, b), title, rel, len(body)))
        index_rows.append((part, rows))

    # banned words, copied verbatim so lint.py finds them next to the scripts
    shutil.copy(os.path.join(SRC, "banned-words.txt"), os.path.join(ref, "banned-words.txt"))

    lines = ["# UNSLOP lexicon index", "",
             "Every banned entry and the file that explains it, with replacements and rewrites.", "",
             "| No. | Entry | File |", "| --- | --- | --- |"]
    lines += ["| %s | `%s` | `references/%s` |" % row for row in lexicon]
    write(os.path.join(ref, "lexicon-index.md"), "\n".join(lines))

    def table(prefix):
        out = []
        for part, rows in index_rows:
            out += ["", "### Part %d. %s" % (part["num"], part["title"]), "",
                    "| Chapter | File | Size |", "| --- | --- | --- |"]
            for num, title, rel, size in rows:
                out.append("| %s %s | `%s%s` | %dk |" % (num, title, prefix, rel, max(1, round(size / 1000))))
        return "\n".join(out).strip()

    write(os.path.join(ref, "INDEX.md"),
          "# UNSLOP chapter index\n\nPaths are relative to the skill folder.\n\n" + table("references/")
          + "\n\n### Word lists\n\n- `references/banned-words.txt`: the 350 entries, one per line.\n"
          "- `references/lexicon-index.md`: each entry and the file that covers it.")
    return table("references/"), len(lexicon)


def routes_table(routes):
    lines = ["| Task | Run | Chapters | Cost |", "| --- | --- | --- | --- |"]
    for r in routes:
        lines.append("| %s | `--task %s` | %s | ~%dk tokens |" % (
            r["label"], r["id"], ", ".join(r["chapters"]), max(1, round(r["chars"] / 4000))))
    return "\n".join(lines)


def parts_list(parts):
    lines = ["Parts, for browsing. Every chapter and its file: `references/INDEX.md`. Every section with its line range: `references/DEEP-INDEX.md`.", ""]
    for p in parts:
        if p["num"] == 10:
            continue
        chaps = p["chapters"]
        lines.append("- Part %d. %s (%s to %s)" % (p["num"], p["title"], "%d.%d" % chaps[0]["num"], "%d.%d" % chaps[-1]["num"]))
    return "\n".join(lines)


def main():
    parts_md = "\n\n".join(read(os.path.join(PARTS, f)).strip("\n")
                           for f in sorted(os.listdir(PARTS)) if f.endswith(".md"))
    parts = split_chapters(parts_md)
    version = read(os.path.join(ROOT, "VERSION")).strip()
    core = read(os.path.join(TPL, "core.md")).strip()
    top = [l.strip() for l in read(os.path.join(TPL, "top-words.txt")).split("\n") if l.strip()]
    all_words = [w for _, ws in word_entries() for w in ws]
    total_chars = len(read(os.path.join(ROOT, "UNSLOP.md"))) if os.path.exists(os.path.join(ROOT, "UNSLOP.md")) else len(parts_md)

    os.makedirs(SKILL, exist_ok=True)
    _, n_entries = build_references(parts)
    if n_entries != len(all_words):
        sys.exit("build_skill: lexicon has %d entries, banned-words.txt has %d" % (n_entries, len(all_words)))
    with open(os.path.join(TPL, "routes.json"), encoding="utf-8") as f:
        routes_spec = json.load(f)
    with open(os.path.join(TPL, "aliases.json"), encoding="utf-8") as f:
        aliases = json.load(f)
    stats = build_index.build(SKILL, routes_spec, aliases)
    print("index: %d sections, %d terms, %d code blocks, %d routes, %d KB" % (
        stats["sections"], stats["terms"], stats["code"], len(stats["routes"]), stats["bytes"] // 1024))
    index = routes_table(stats["routes"]) + "\n\n" + parts_list(parts)

    skill_md = (read(os.path.join(TPL, "SKILL.md.in"))
                .replace("{{VERSION}}", version)
                .replace("{{TOTAL_CHARS}}", "{:,}".format(total_chars))
                .replace("{{CORE}}", core)
                .replace("{{TOP_WORDS}}", word_block(top))
                .replace("{{INDEX}}", index))
    write(os.path.join(SKILL, "SKILL.md"), skill_md)
    os.makedirs(os.path.join(SKILL, "agents"), exist_ok=True)
    shutil.copy(os.path.join(TPL, "agents", "openai.yaml"), os.path.join(SKILL, "agents", "openai.yaml"))
    os.makedirs(os.path.join(SKILL, "scripts"), exist_ok=True)
    for name in ("lint.py", "scan.py", "find.py"):
        shutil.copy(os.path.join(ROOT, "scripts", name), os.path.join(SKILL, "scripts", name))

    adapter = (read(os.path.join(TPL, "adapter.md.in"))
               .replace("{{CORE}}", core)
               .replace("{{TOP_WORDS}}", word_block(top))
               .replace("{{SKILL_DIR}}", DEFAULT_SKILL_DIR))
    write(os.path.join(DIST, "AGENTS.md"), adapter)
    write(os.path.join(DIST, "GEMINI.md"), adapter)
    write(os.path.join(DIST, "copilot-instructions.md"), adapter)
    write(os.path.join(DIST, "unslop.mdc"),
          "---\ndescription: UNSLOP interface and copy rules\n"
          "globs: \"**/*.{html,css,scss,js,jsx,ts,tsx,vue,svelte,astro,md,mdx}\"\nalwaysApply: true\n---\n\n" + adapter)
    write(os.path.join(DIST, "system-prompt.md"),
          read(os.path.join(TPL, "system-prompt.md.in"))
          .replace("{{CORE}}", core.replace("`references/banned-words.txt`", "the banned list at the end"))
          .replace("{{ALL_WORDS}}", word_block(all_words)))

    # Deterministic zip: fixed timestamps and sorted entries, so rebuilding
    # without changes produces the same bytes.
    zpath = os.path.join(DIST, "unslop-skill.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for d, dirs, names in os.walk(SKILL):
            dirs.sort()
            dirs[:] = [x for x in dirs if x != "__pycache__"]
            for name in sorted(names):
                full = os.path.join(d, name)
                info = zipfile.ZipInfo(os.path.join("unslop", os.path.relpath(full, SKILL)), (2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = (0o755 if name.endswith(".py") else 0o644) << 16
                with open(full, "rb") as f:
                    z.writestr(info, f.read())

    md_files = [os.path.join(SKILL, "SKILL.md")]
    for d, _, names in os.walk(os.path.join(SKILL, "references")):
        md_files += [os.path.join(d, n) for n in sorted(names) if n.endswith(".md")]
    md_files += [os.path.join(DIST, n) for n in ("AGENTS.md", "system-prompt.md", "unslop.mdc")]
    print("skill: %d reference files, SKILL.md %d lines, zip %d KB" % (
        len(md_files) - 4, skill_md.count("\n"), os.path.getsize(zpath) // 1024))
    out = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "lint.py")] + md_files,
                         capture_output=True, text=True)
    bad = [l for l in out.stdout.split("\n") if l and not l.endswith(" 0 problems")]
    print("\n".join(bad) if bad else "skill lint: 0 problems in %d files" % len(md_files))
    return out.returncode


if __name__ == "__main__":
    sys.exit(main())
