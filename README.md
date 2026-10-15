# unslop

`UNSLOP.md` is a single Markdown file, over 927,400 characters long, that tells AI coding agents (and people) how to build interfaces and write copy that do not look machine-made.

It bans, with exact values and a check for each rule:

- box shadows of every kind
- emoji, anywhere
- green-dot `LIVE` status pills
- blue and purple gradients (and in practice all gradients in interface chrome)
- glass, blur, glow, `rounded-2xl`
- 350 words and phrases that models overuse, in every inflection

The file follows its own rules. Its prose contains none of the banned words; they appear only as mentions in inline code or in code fences tagged `slop`, which hold the bad examples.

## Use it

Drop `UNSLOP.md` into your agent's context: `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, a system prompt, or a docs folder the agent can search. Part 6 has a short block meant for a system prompt if the whole file is too large for your setup.

## Layout

| Path | What it is |
| --- | --- |
| `UNSLOP.md` | The built file. Do not edit by hand. |
| `src/parts/*.md` | Source parts, concatenated in filename order. |
| `src/banned-words.txt` | The 350 banned entries. The appendix is generated from it. |
| `src/AUTHORING.md` | Rules for anyone editing the parts. |
| `scripts/build.py` | Builds `UNSLOP.md`, generates the contents and appendix, runs the linter. |
| `scripts/lint.py` | Checks Markdown for emoji, dashes, exclamation marks, banned words in prose, and shadows or gradients in non-`slop` code. |

## Build

```sh
python3 scripts/build.py
```

The build fails if the linter finds a single problem. To lint any other Markdown file, for example your own README:

```sh
python3 scripts/lint.py path/to/file.md
```
