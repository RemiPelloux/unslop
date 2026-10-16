#!/usr/bin/env python3
"""Check the deep index and measure find.py retrieval.

First verifies that every section and code block range in index.json points
at the lines it claims (heading, size, fences, no overlaps). Then runs
tests/search_eval.json.

Each case is [query, [acceptable section ids]]. Prints hit@1, hit@3 and
MRR@5, lists the misses, and exits 1 if hit@3 falls below --min (default 0.85).
"""
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import find  # noqa: E402


def check_ranges(idx, root):
    """Every range must point at what the index says is there."""
    errors, cache = [], {}

    def lines(path):
        if path not in cache:
            with open(os.path.join(root, path), encoding="utf-8") as f:
                cache[path] = f.read().split("\n")
        return cache[path]

    last = {}
    for s in idx["sections"]:
        ls = lines(s["path"])
        if not (1 <= s["start"] <= s["end"] <= len(ls)):
            errors.append("%s: range %d-%d outside file" % (s["id"], s["start"], s["end"]))
            continue
        head = ls[s["start"] - 1]
        if s["start"] > 1 and not head.startswith("#### "):
            errors.append("%s: line %d is not a heading" % (s["id"], s["start"]))
        if s["start"] > 1 and head[5:].strip() != s["section"]:
            errors.append("%s: heading reads %r" % (s["id"], head[5:].strip()))
        if s["start"] <= last.get(s["path"], 0):
            errors.append("%s: overlaps the previous section" % s["id"])
        last[s["path"]] = s["end"]
        if len("\n".join(ls[s["start"] - 1:s["end"]])) != s["chars"]:
            errors.append("%s: size changed since the index was built" % s["id"])
    for b in idx["code"]:
        ls = lines(b["path"])
        if not ls[b["start"] - 1].lstrip().startswith(("```", "~~~")) or not ls[b["end"] - 1].lstrip().startswith(("```", "~~~")):
            errors.append("code %s:%d-%d does not start and end on a fence" % (b["path"], b["start"], b["end"]))
    ids = {s["id"] for s in idx["sections"]}
    for r in idx["routes"]:
        errors += ["route %s: unknown section %s" % (r["id"], x) for x in r["sections"] if x not in ids]
    return errors


def main(argv):
    floor = float(argv[argv.index("--min") + 1]) if "--min" in argv else 0.85
    idx, root = find.load_index()
    errors = check_ranges(idx, root)
    print("ranges: %d sections, %d code blocks, %d problems" % (len(idx["sections"]), len(idx["code"]), len(errors)))
    for e in errors[:20]:
        print("  " + e)
    cases = json.load(open(os.path.join(ROOT, "tests", "search_eval.json"), encoding="utf-8"))
    h1 = h3 = mrr = 0.0
    misses = []
    t0 = time.perf_counter()
    for query, ok in cases:
        ids = [s["id"] for s, _ in find.search(idx, query, 5)]
        rank = next((i for i, x in enumerate(ids) if x in ok), None)
        h1 += rank == 0
        h3 += rank is not None and rank < 3
        mrr += 1.0 / (rank + 1) if rank is not None else 0
        if rank is None or rank >= 3:
            misses.append((query, ids[:3]))
    ms = (time.perf_counter() - t0) * 1000 / len(cases)
    n = len(cases)
    print("cases %d  hit@1 %.2f  hit@3 %.2f  MRR@5 %.2f  %.1f ms/query" % (n, h1 / n, h3 / n, mrr / n, ms))
    for q, ids in misses:
        print("  miss: %-40s got %s" % (q, ", ".join(ids)))
    return 0 if h3 / n >= floor and not errors else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
