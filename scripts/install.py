#!/usr/bin/env python3
"""Install the UNSLOP skill for one or more coding agents.

Usage:
  python3 scripts/install.py TOOL [TOOL ...] [--dir PROJECT] [--user]

TOOL is one of:
  claude    Claude Code skill        PROJECT/.claude/skills/unslop   (--user: ~/.claude/skills/unslop)
  codex     Codex skill              PROJECT/.agents/skills/unslop   (--user: ~/.agents/skills/unslop)
  agents    AGENTS.md block          PROJECT/AGENTS.md, plus the skill in .agents/skills/unslop
  cursor    Cursor project rule      PROJECT/.cursor/rules/unslop.mdc, plus the skill
  copilot   GitHub Copilot           PROJECT/.github/copilot-instructions.md, plus the skill
  gemini    Gemini CLI               PROJECT/GEMINI.md, plus the skill
  all       every one of the above

PROJECT defaults to the current directory. Blocks added to an existing
AGENTS.md, GEMINI.md or copilot-instructions.md sit between
<!-- unslop:start --> and <!-- unslop:end --> and are replaced on reinstall;
the rest of the file is left alone.
"""
import argparse
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "skills", "unslop")
DIST = os.path.join(ROOT, "dist")
DEFAULT_SKILL_DIR = ".agents/skills/unslop"
START, END = "<!-- unslop:start -->", "<!-- unslop:end -->"
TOOLS = ["claude", "codex", "agents", "cursor", "copilot", "gemini"]


def copy_skill(dest):
    marker = os.path.join(dest, "SKILL.md")
    if os.path.exists(dest):
        if not os.path.isfile(marker) or "name: unslop" not in open(marker, encoding="utf-8").read(2000):
            sys.exit("install: %s exists and is not an UNSLOP skill; not touching it" % dest)
        shutil.rmtree(dest)
    shutil.copytree(SKILL, dest, ignore=shutil.ignore_patterns("__pycache__"))
    print("skill    -> %s" % dest)


def adapter(name, skill_dir):
    with open(os.path.join(DIST, name), encoding="utf-8") as f:
        return f.read().replace(DEFAULT_SKILL_DIR, skill_dir)


def put_block(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    block = "%s\n%s\n%s\n" % (START, text.strip(), END)
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    if START in old and END in old:
        head, rest = old.split(START, 1)
        new = head + block + rest.split(END, 1)[1].lstrip("\n")
    else:
        new = (old.rstrip("\n") + "\n\n" if old.strip() else "") + block
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)
    print("rules    -> %s" % path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tools", nargs="+", choices=TOOLS + ["all"])
    ap.add_argument("--dir", default=".", help="project to install into (default: current directory)")
    ap.add_argument("--user", action="store_true", help="install the skill for your user account instead of one project")
    args = ap.parse_args()
    if not os.path.isfile(os.path.join(SKILL, "SKILL.md")):
        sys.exit("install: skills/unslop is missing; run python3 scripts/build.py first")

    tools = TOOLS if "all" in args.tools else args.tools
    project = os.path.abspath(args.dir)
    home = os.path.expanduser("~")
    if args.user and set(tools) - {"claude", "codex"}:
        sys.exit("install: --user works for claude and codex only; the other tools read rules per project")

    shared = os.path.join(home if args.user else project, ".agents", "skills", "unslop")
    shared_done = False
    for tool in tools:
        if tool == "claude":
            copy_skill(os.path.join(home if args.user else project, ".claude", "skills", "unslop"))
            continue
        if not shared_done:
            copy_skill(shared)
            shared_done = True
        if tool == "agents":
            put_block(os.path.join(project, "AGENTS.md"), adapter("AGENTS.md", DEFAULT_SKILL_DIR))
        elif tool == "gemini":
            put_block(os.path.join(project, "GEMINI.md"), adapter("GEMINI.md", DEFAULT_SKILL_DIR))
        elif tool == "copilot":
            put_block(os.path.join(project, ".github", "copilot-instructions.md"),
                      adapter("copilot-instructions.md", DEFAULT_SKILL_DIR))
        elif tool == "cursor":
            path = os.path.join(project, ".cursor", "rules", "unslop.mdc")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(adapter("unslop.mdc", DEFAULT_SKILL_DIR))
            print("rules    -> %s" % path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
