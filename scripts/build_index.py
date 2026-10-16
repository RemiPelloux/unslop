#!/usr/bin/env python3
"""Build the deep index for the packaged skill.

Reads every file under skills/unslop/references/ and writes:
  references/index.json      sections with exact line ranges, a BM25 inverted
                             index, code block locations, lexicon replacements,
                             search aliases and resolved task routes; read by
                             scripts/find.py
  references/DEEP-INDEX.md   the same sections as one greppable line each

Called by scripts/build_skill.py after the reference files are written.
"""
import json
import math
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from find import tokenize  # noqa: E402  (same tokenizer at build and query time)

SKIP = {"INDEX.md", "lexicon-index.md", "DEEP-INDEX.md"}
KINDS = [
    ("what the machine produces", "slop"), ("the slop version", "slop"),
    ("reference build", "code"), ("the rebuild", "code"),
    ("rules", "rules"), ("states", "states"), ("copy", "copy"),
    ("checklist", "checklist"), ("tells", "tells"), ("notes", "notes"),
]
ROUTE_KINDS = {"rules", "code", "tells"}


def kind_of(title, is_entry):
    if is_entry:
        return "entry"
    t = title.lower()
    for name, kind in KINDS:
        if t == name or t.startswith(name + " "):
            return kind
    return "text"


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower().replace("`", "")).strip("-")[:48].rstrip("-")


def parse_file(rel, text):
    """Split one reference file into sections at #### headings (outside fences)."""
    lines = text.split("\n")
    is_entry = "/entries/" in rel
    chap_num, chap_title = None, None
    heads, fence, blocks, open_block = [], None, [], None
    for i, line in enumerate(lines):
        m = re.match(r"^\s*(`{3,}|~{3,})\s*([\w+-]*)", line)
        if m:
            if fence is None:
                fence = m.group(1)
                open_block = (i, m.group(2).lower())
            elif line.strip().startswith(fence) and set(line.strip()) <= set(fence[0]):
                fence = None
                blocks.append((open_block[0], i, open_block[1]))
            continue
        if fence:
            continue
        h3 = re.match(r"^### (\d+\.\d+) (.+)$", line)
        if h3 and chap_num is None:
            chap_num, chap_title = h3.group(1), h3.group(2)
        if line.startswith("#### "):
            heads.append(i)
    if is_entry:
        n = int(re.match(r"#### (\d{3})", lines[heads[0]]).group(1))
        chap_num = "7.%d" % ((n - 1) // 70 + 1)
        chap_title = "The Lexicon"
    sections = []
    bounds = ([0] if not heads or heads[0] > 0 else []) + heads + [len(lines)]
    for a, b in zip(bounds, bounds[1:]):
        end = b - 1
        while end > a and not lines[end].strip():
            end -= 1
        body = "\n".join(lines[a:end + 1])
        if a in heads:
            title = lines[a][5:].strip()
        else:
            # preamble: header line plus the ### heading; keep it only if it says something
            rest = [l for l in lines[a:end + 1] if l.strip() and not l.startswith("From UNSLOP") and not l.startswith("### ")]
            if heads and not rest:
                continue
            title = "Overview" if heads else chap_title
        codes = sorted({tag for s, e, tag in blocks if a <= s <= end and tag and tag != "slop"})
        sections.append({
            "chapter": chap_num, "chapter_title": chap_title, "title": title,
            "path": "references/" + rel, "start": a + 1, "end": end + 1,
            "chars": len(body), "kind": kind_of(title, is_entry), "code": codes, "_body": body,
        })
    code_blocks = []
    for s, e, tag in blocks:
        if tag == "slop":
            continue
        owner = next((x for x in reversed(sections) if x["start"] <= s + 1), sections[0])
        first = next((l.strip() for l in lines[s + 1:e] if l.strip()), "")[:80]
        code_blocks.append({
            "chapter": chap_num, "chapter_title": chap_title, "section_title": owner["title"],
            "path": "references/" + rel, "start": s + 1, "end": e + 1, "lang": tag or "text", "first": first,
        })
    return sections, code_blocks


def replacements(body):
    """The 'Replace with' bullets of a lexicon entry, for find.py --word/--text."""
    m = re.search(r"^Replace with:\s*\n(.*?)(?:^Rewrites:|\Z)", body, re.S | re.M)
    if not m:
        return []
    items = [l.strip()[2:] for l in m.group(1).split("\n") if l.strip().startswith("- ")]
    return ["- " + (i if len(i) <= 160 else i[:157].rstrip() + "...") for i in items]


def b36(n):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    out = ""
    while True:
        n, r = divmod(n, 36)
        out = digits[r] + out
        if not n:
            return out


def encode(ids, tfs=None):
    """Sorted section ids as base-36 gaps; ':tf' only when tf > 1.
    [3, 40, 41] with tf [1, 2, 1] -> '3 11:2 1'. find.decode reverses it."""
    out, prev = [], 0
    for k, i in enumerate(ids):
        tok = b36(i - prev)
        if tfs and tfs[k] > 1:
            tok += ":" + b36(tfs[k])
        out.append(tok)
        prev = i
    return " ".join(out)


def pack(sections, postings, title_post, chap_post, aliases, routes, code_blocks, lexicon):
    """Store each path and chapter title once and section rows as arrays.
    find.load_index turns the rows back into dicts."""
    files = sorted({s["path"] for s in sections})
    fid = {p: i for i, p in enumerate(files)}
    chapters = {s["chapter"]: s["chapter_title"] for s in sections}
    return {
        "version": 2,
        "files": files,
        "chapters": chapters,
        "fields": ["id", "chapter", "section", "file", "start", "end", "chars", "kind", "code", "len", "terms"],
        "sections": [[s["id"], s["chapter"], s["section"], fid[s["path"]], s["start"], s["end"], s["chars"],
                      s["kind"], ",".join(s["code"]), s["len"], " ".join(s["terms"])] for s in sections],
        "avg_len": round(sum(s["len"] for s in sections) / len(sections), 3),
        "postings": {t: encode(p[0::2], p[1::2]) for t, p in postings.items()},
        "title_postings": {t: encode(p) for t, p in title_post.items()},
        "chapter_postings": {t: encode(p) for t, p in chap_post.items()},
        "aliases": aliases,
        "routes": routes,
        "code": [[b["chapter"], b["section_title"], fid[b["path"]], b["start"], b["end"], b["lang"], b["first"]]
                 for b in code_blocks],
        "lexicon": [[e["no"], e["entry"], e["id"], fid[e["path"]], e["start"], e["end"], e["replace"]] for e in lexicon],
    }


def build(skill_dir, routes_spec, aliases):
    ref = os.path.join(skill_dir, "references")
    files = []
    for d, dirs, names in os.walk(ref):
        dirs.sort()
        for name in sorted(names):
            if name.endswith(".md") and name not in SKIP:
                files.append(os.path.relpath(os.path.join(d, name), ref).replace(os.sep, "/"))

    sections, code_blocks = [], []
    for rel in files:
        with open(os.path.join(ref, rel), encoding="utf-8") as f:
            secs, blocks = parse_file(rel, f.read())
        sections += secs
        code_blocks += blocks

    def chap_key(c):
        return tuple(int(x) for x in c.split("."))
    sections.sort(key=lambda s: (chap_key(s["chapter"]), s["path"], s["start"]))

    seen = Counter()
    for s in sections:
        if s["kind"] == "entry":
            base = "7/" + re.match(r"(\d{3})", s["title"]).group(1)
        else:
            base = "%s/%s" % (s["chapter"], slug(s["title"]) or "text")
        seen[base] += 1
        s["id"] = base if seen[base] == 1 else "%s-%d" % (base, seen[base])
        s["section"] = s["title"]
        if s["kind"] != "entry":
            s["title"] = "%s > %s" % (s["chapter_title"], s["title"]) if s["title"] != s["chapter_title"] else s["title"]

    # BM25 inverted index over bodies; titles get their own postings so the
    # query side can weigh them separately (see find.search).
    postings, df = {}, Counter()
    title_post, chap_post = {}, {}
    docs = []
    for i, s in enumerate(sections):
        for t in set(tokenize(s["section"])):
            title_post.setdefault(t, []).append(i)
        for t in set(tokenize(s["chapter_title"])):
            chap_post.setdefault(t, []).append(i)
        toks = tokenize(s["_body"])
        tf = Counter(toks)
        docs.append(tf)
        s["len"] = len(toks)
        for t, c in tf.items():
            postings.setdefault(t, []).extend((i, c))
            df[t] += 1
    n_docs = len(sections)
    for s, tf in zip(sections, docs):
        title_terms = set(tokenize(s["title"]))
        scored = sorted(((c * math.log(n_docs / df[t]), t) for t, c in tf.items()
                         if t not in title_terms and df[t] < n_docs / 4 and len(t) > 3), reverse=True)
        s["terms"] = [t for _, t in scored[:5]]

    lexicon = []
    for s in sections:
        if s["kind"] == "entry":
            no, entry = re.match(r"(\d{3})\. `([^`]+)`", s["title"]).groups()
            lexicon.append({"no": no, "entry": entry, "id": s["id"], "path": s["path"],
                            "start": s["start"], "end": s["end"], "replace": replacements(s["_body"])})

    by_chapter = {}
    for s in sections:
        by_chapter.setdefault(s["chapter"], []).append(s)
    # A route item is a chapter ("4.6": its rules, reference code and tells,
    # or the whole chapter when it has none of those) or one section ("4.6/rules").
    ids = {s["id"]: s for s in sections}
    routes = []
    for r in routes_spec:
        picked, chapters = [], []
        for item in r["read"]:
            if "/" in item:
                if item not in ids:
                    sys.exit("build_index: route %s names missing section %s" % (r["id"], item))
                secs = [ids[item]]
            else:
                if item not in by_chapter:
                    sys.exit("build_index: route %s names missing chapter %s" % (r["id"], item))
                focused = [s for s in by_chapter[item] if s["kind"] in ROUTE_KINDS]
                secs = focused or by_chapter[item]
            picked += [s for s in secs if s not in picked]
            chap = item.split("/")[0]
            if chap not in chapters:
                chapters.append(chap)
        full = sum(s["chars"] for c in chapters for s in by_chapter[c])
        routes.append({"id": r["id"], "label": r["label"], "match": r["match"], "chapters": chapters,
                       "sections": [s["id"] for s in picked], "chars": sum(s["chars"] for s in picked),
                       "full_chars": full})

    for s in sections:
        del s["_body"]
    with open(os.path.join(ref, "index.json"), "w", encoding="utf-8") as f:
        json.dump(pack(sections, postings, title_post, chap_post, aliases, routes, code_blocks, lexicon),
                  f, separators=(",", ":"), ensure_ascii=False, sort_keys=True)

    out = ["# UNSLOP deep index", "",
           "One line per section of the handbook: id, title, exact line range, size, kind and distinctive terms. "
           "Do not read this file whole. Search it, then read only the lines it names:", "",
           "```sh",
           "grep -i 'reference build' references/DEEP-INDEX.md | grep -i button",
           "grep -i 'focus-visible' references/DEEP-INDEX.md",
           "sed -n '120,188p' references/04-components-a-to-m/04.06-buttons.md",
           "```", "",
           "`scripts/find.py` searches the same sections by relevance and is faster than grep for open questions.", ""]
    current = None
    for s in sections:
        if s["chapter"] != current:
            current = s["chapter"]
            chap = by_chapter[current]
            out += ["", "## %s %s" % (current, chap[0]["chapter_title"]), ""]
        terms = " ".join("`%s`" % t for t in s["terms"])
        code = " code:%s" % ",".join(s["code"]) if s["code"] else ""
        out.append("- %s | %s | `%s:%d-%d` | %.1fk | %s%s | %s" % (
            s["id"], s["title"], s["path"], s["start"], s["end"], s["chars"] / 1000, s["kind"], code, terms))
    with open(os.path.join(ref, "DEEP-INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    return {"sections": n_docs, "terms": len(postings), "code": len(code_blocks), "routes": routes,
            "bytes": os.path.getsize(os.path.join(ref, "index.json"))}


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill = os.path.join(root, "skills", "unslop")
    with open(os.path.join(root, "src", "skill", "routes.json"), encoding="utf-8") as f:
        routes = json.load(f)
    with open(os.path.join(root, "src", "skill", "aliases.json"), encoding="utf-8") as f:
        aliases = json.load(f)
    stats = build(skill, routes, aliases)
    print("index: %d sections, %d terms, %d code blocks, %d routes, %d KB" % (
        stats["sections"], stats["terms"], stats["code"], len(stats["routes"]), stats["bytes"] // 1024))
