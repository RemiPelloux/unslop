#!/usr/bin/env python3
"""Find the exact UNSLOP section a task needs, without reading whole chapters.

Usage:
  find.py QUERY ...            rank sections by relevance (BM25 over a prebuilt index)
  find.py QUERY ... --show     ... and print the text of the best hit
  find.py QUERY ... --budget N ... and print the best hits until N characters are used
  find.py --task NAME          the reading list for a kind of task, with exact line ranges
  find.py --tasks              list every task route
  find.py --chapter 4.6        every section of one chapter, with line ranges
  find.py --section 4.6/rules  print one section
  find.py --code buttons       reference code blocks (add --lang css to filter)
  find.py --word seamlessly    the banned entry behind any word form, with replacements
  find.py --text "draft copy"  every banned word in a draft, with replacements inline
                               (exits 1 when it finds any, like a linter)

Common options: -n N (number of hits, default 5), --json (machine output).

Every hit prints `path:start-end`. Read only those lines: with a file tool's
offset and limit, or `sed -n 'START,ENDp' PATH`, or `--show` here.
The index is references/index.json, built by scripts/build.py.
"""
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.normpath(os.path.join(HERE, ".."))
INDEX_CANDIDATES = [
    os.path.join(SKILL_DIR, "references", "index.json"),
    os.path.join(SKILL_DIR, "skills", "unslop", "references", "index.json"),
]

STOP = set("""a an and are as at be been but by can do does for from has have how i if in into is it
its may more most must no not of on one or so such than that the their them then there these they this
to too use used uses using was we what when where which while who why will with you your yours""".split())


def stem(t):
    """Light suffix stripping, enough to join plurals and verb forms.
    Same function at build and query time, so it only has to be consistent."""
    if len(t) > 5 and t.endswith("ies"):
        return t[:-3] + "y"
    if len(t) > 4 and t.endswith("es") and t[-3] in "sxz" or t.endswith(("ches", "shes")):
        return t[:-2]
    for suf in ("ing", "ed", "s"):
        if len(t) > len(suf) + 3 and t.endswith(suf) and not t.endswith("ss"):
            t = t[: -len(suf)]
            if suf != "s" and len(t) > 3 and t[-1] == t[-2] and t[-1] not in "lsz":
                t = t[:-1]  # stopped -> stop, sitting -> sit
            return t
    return t


def tokenize(text):
    """Words and hyphenated terms (box-shadow, ring-2, rounded-2xl) both count."""
    out = []
    for tok in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text.lower()):
        if "-" in tok:
            out.append(tok)
            out.extend(stem(p) for p in tok.split("-") if p not in STOP and len(p) > 1)
        elif tok not in STOP and len(tok) > 1:
            out.append(stem(tok))
    return out


def decode(packed, with_tf=True):
    """Reverse of build_index.encode: '3 11:2 1' -> [(3, 1), (40, 2), (41, 1)]."""
    out, prev = [], 0
    for tok in packed.split(" "):
        gap, _, tf = tok.partition(":")
        prev += int(gap, 36)
        out.append((prev, int(tf, 36) if tf else 1) if with_tf else prev)
    return out


def unpack(raw):
    files, chapters = raw["files"], raw["chapters"]
    secs = []
    for row in raw["sections"]:
        s = dict(zip(raw["fields"], row))
        s["path"] = files[s.pop("file")]
        s["chapter_title"] = chapters[s["chapter"]]
        s["code"] = s["code"].split(",") if s["code"] else []
        s["terms"] = s["terms"].split()
        s["title"] = s["section"] if s["kind"] == "entry" or s["section"] == s["chapter_title"] \
            else "%s > %s" % (s["chapter_title"], s["section"])
        secs.append(s)
    code = [dict(chapter=c, chapter_title=chapters[c], section_title=st, path=files[f], start=a, end=b, lang=l, first=fi)
            for c, st, f, a, b, l, fi in raw["code"]]
    lexicon = [dict(no=no, entry=e, id=i, path=files[f], start=a, end=b, replace=r)
               for no, e, i, f, a, b, r in raw["lexicon"]]
    return dict(raw, sections=secs, code=code, lexicon=lexicon)


def load_index():
    for path in INDEX_CANDIDATES:
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as f:
                return unpack(json.load(f)), os.path.dirname(os.path.dirname(path))
    sys.exit("find.py: references/index.json not found; run scripts/build.py")


def expand(terms, aliases):
    out = list(terms)
    for t in terms:
        for a in aliases.get(t, []):
            out.extend(tokenize(a))
    return out


def norm(text):
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def search(idx, query, n):
    """BM25 over section bodies, plus fixed boosts for terms in the section
    title and the chapter title, plus a boost when the whole query appears in
    the section title. Checklists rank a little lower: they summarize rules
    that live in the same chapter."""
    terms = expand(tokenize(query), idx["aliases"])
    secs, body, titles, chaps = idx["sections"], idx["postings"], idx["title_postings"], idx["chapter_postings"]
    N, avg = len(secs), idx["avg_len"]
    k1, b = 1.2, 0.5
    scores = {}
    for t in set(terms):
        packed = body.get(t)
        if not packed:
            continue
        p = decode(packed)
        df = len(p)
        idf = math.log(1 + (N - df + 0.5) / (df + 0.5))
        qtf = terms.count(t)
        for s, tf in p:
            dl = secs[s]["len"]
            scores[s] = scores.get(s, 0.0) + qtf * idf * tf * (k1 + 1) / (tf + k1 * (1 - b + b * dl / avg))
        for post, weight in ((titles, 3.0), (chaps, 2.0)):
            if t in post:
                for s in decode(post[t], with_tf=False):
                    scores[s] = scores.get(s, 0.0) + weight * idf
    q = norm(query)
    qset = set(tokenize(query))
    if q:
        for i, sec in enumerate(secs):
            if q in norm(sec["section"]):
                scores[i] = scores.get(i, 0.0) + 12.0
            # every query word names the chapter ("data table", "toast"):
            # lift the sections that carry its rules and reference code
            if sec["kind"] in ("rules", "code") and qset and qset <= set(tokenize(sec["chapter_title"])):
                scores[i] = scores.get(i, 0.0) + 8.0
    for s in scores:
        if secs[s]["kind"] == "checklist":
            scores[s] *= 0.75
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])[:n]
    return [(secs[s], sc) for s, sc in ranked]


def where(sec):
    return "%s:%d-%d" % (sec["path"], sec["start"], sec["end"])


def fmt(sec, score=None):
    tag = "  [%s]" % sec["kind"] if sec["kind"] != "text" else ""
    code = "  code: %s" % ",".join(sec["code"]) if sec["code"] else ""
    head = "%s  %s%s%s  %s chars ~%d tokens" % (sec["id"], sec["title"], tag, code, "{:,}".format(sec["chars"]), sec["chars"] // 4)
    if score is not None:
        head = "%5.1f  %s" % (score, head)
    return head + "\n       " + where(sec)


def text_of(root, sec):
    with open(os.path.join(root, sec["path"]), encoding="utf-8") as f:
        lines = f.read().split("\n")
    return "\n".join(lines[sec["start"] - 1: sec["end"]])


def by_id(idx):
    return {s["id"]: s for s in idx["sections"]}


def lint_patterns(root):
    sys.path.insert(0, os.path.join(root, "scripts"))
    os.environ.setdefault("UNSLOP_WORDS", os.path.join(root, "references", "banned-words.txt"))
    import lint  # noqa: E402
    return lint.load_patterns()


def entry_hits(idx, root, text):
    entries = {e["entry"]: e for e in idx["lexicon"]}
    hits = []
    for entry, pat in lint_patterns(root):
        for m in pat.finditer(text):
            hits.append((m.start(), m.group(), entries[entry]))
    return sorted(hits, key=lambda h: h[0])


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(prog="find.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, add_help=True)
    ap.add_argument("query", nargs="*")
    ap.add_argument("-n", type=int, default=5)
    ap.add_argument("--json", action="store_true", dest="as_json")
    ap.add_argument("--show", action="store_true")
    ap.add_argument("--budget", type=int)
    ap.add_argument("--tasks", action="store_true", dest="list_tasks")
    for name in ("task", "chapter", "section", "code", "lang", "word", "text"):
        ap.add_argument("--" + name)
    a = ap.parse_args(argv[1:])
    as_json, show, list_tasks, n, budget = a.as_json, a.show, a.list_tasks, max(a.n, 1), a.budget
    task, chapter, section, code, lang, word, text = a.task, a.chapter, a.section, a.code, a.lang, a.word, a.text
    args = a.query
    idx, root = load_index()
    sections = by_id(idx)
    out = []

    if list_tasks:
        for t in idx["routes"]:
            print("%-22s %-48s %s chars ~%d tokens" % (t["id"], t["label"][:48], "{:,}".format(t["chars"]), t["chars"] // 4))
        return 0

    if task:
        q = task.lower()
        routes = [t for t in idx["routes"] if t["id"] == q] or \
                 [t for t in idx["routes"] if q in t["id"] or q in t["label"].lower() or q in t["match"]]
        if not routes:
            print("no task route matches %r; try --tasks" % task)
            return 1
        r = routes[0]
        items = [sections[s] for s in r["sections"]]
        if as_json:
            print(json.dumps({"route": r, "sections": items}, indent=1))
            return 0
        print("%s: %s\nread in order, %s chars ~%d tokens in total\n" % (r["id"], r["label"], "{:,}".format(r["chars"]), r["chars"] // 4))
        for s in items:
            print(fmt(s))
        if show:
            for s in items:
                print("\n" + text_of(root, s))
        return 0

    if chapter:
        items = [s for s in idx["sections"] if s["chapter"] == chapter]
        if not items:
            print("no chapter %s" % chapter)
            return 1
        print("\n".join(fmt(s) for s in items) if not as_json else json.dumps(items, indent=1))
        return 0

    if section:
        s = sections.get(section)
        if not s:
            print("no section %s" % section)
            return 1
        print(fmt(s) + "\n\n" + text_of(root, s))
        return 0

    if code:
        q = tokenize(code)
        items = [b for b in idx["code"] if (not lang or b["lang"] == lang)
                 and all(t in tokenize(b["chapter_title"] + " " + b["section_title"] + " " + b["first"]) for t in q)]
        # blocks from the chapter the query names come first
        items.sort(key=lambda b: (not set(q) <= set(tokenize(b["chapter_title"])),
                                  not set(q) <= set(tokenize(b["section_title"]))))
        for b in items[:n * 4]:
            print("%s  %s > %s  [%s]  %d lines\n       %s:%d-%d" % (
                b["chapter"], b["chapter_title"], b["section_title"], b["lang"], b["end"] - b["start"] + 1, b["path"], b["start"], b["end"]))
        if not items:
            print("no code blocks match; try fewer words or no --lang")
        return 0 if items else 1

    if word or text:
        hits = entry_hits(idx, root, word or text)
        if not hits:
            print("no banned entries found")
            return 0
        seen = set()
        for pos, found, e in hits:
            if as_json:
                out.append({"found": found, "at": pos, **e})
                continue
            print("%r -> %s. %s   %s" % (found, e["no"], e["entry"], e["path"]))
            if e["entry"] not in seen:
                seen.add(e["entry"])
                for line in e["replace"]:
                    print("       " + line)
        if as_json:
            print(json.dumps(out, indent=1))
        return 1 if text else 0

    query = " ".join(args)
    if not query:
        print(__doc__)
        return 2
    hits = search(idx, query, max(n, 1))
    if as_json:
        print(json.dumps([dict(s, score=round(sc, 2)) for s, sc in hits], indent=1))
        return 0
    for s, sc in hits:
        print(fmt(s, sc))
    if show and hits:
        print("\n" + text_of(root, hits[0][0]))
    if budget:
        used = 0
        for s, _ in hits:
            if used + s["chars"] > budget:
                break
            print("\n" + text_of(root, s))
            used += s["chars"]
    return 0 if hits else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
