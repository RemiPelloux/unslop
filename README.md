# unslop

Rules for interfaces and copy that do not look machine-made, packaged as an Agent Skill that loads into Claude, Codex, Cursor, Copilot, Gemini or any model through a system prompt.

It bans, with exact values and a check for each rule:

- box shadows of every kind, including Tailwind `ring-*`
- emoji, anywhere
- green-dot `LIVE` status pills
- blue and purple gradients (and in practice all gradients in interface chrome)
- glass, blur, glow, `rounded-2xl`
- 350 words and phrases that models overuse, in every inflection

The handbook behind it, `UNSLOP.md`, is 1,256,340 characters. The skill splits it into 487 small files so an agent reads only what the task needs: `SKILL.md` (about 300 lines) holds the rules for every task, and points to one file per chapter and one file per banned word.

## Install

### Claude Code

As a plugin, from inside Claude Code:

```text
/plugin marketplace add remipelloux/unslop
/plugin install unslop@unslop
```

Or copy the skill folder, for one project or for your account:

```sh
python3 scripts/install.py claude --dir path/to/project
python3 scripts/install.py claude --user        # ~/.claude/skills/unslop
```

### Claude apps (claude.ai, desktop) and the Claude API

Upload `dist/unslop-skill.zip` in the Skills section of Settings in claude.ai or the desktop app. For the API, upload the same folder through the Skills endpoint. The zip holds the `unslop/` skill folder.

### Codex

```sh
python3 scripts/install.py codex --dir path/to/project   # .agents/skills/unslop
python3 scripts/install.py codex --user                  # ~/.agents/skills/unslop
```

Codex picks the skill up on its own when a task matches, or call it with `$unslop`.

### Cursor, GitHub Copilot, Gemini CLI, and anything that reads AGENTS.md

```sh
python3 scripts/install.py cursor  --dir path/to/project   # .cursor/rules/unslop.mdc
python3 scripts/install.py copilot --dir path/to/project   # .github/copilot-instructions.md
python3 scripts/install.py gemini  --dir path/to/project   # GEMINI.md
python3 scripts/install.py agents  --dir path/to/project   # AGENTS.md (Jules, Amp, Zed, others)
python3 scripts/install.py all     --dir path/to/project
```

Each one writes the rules file and copies the skill to `.agents/skills/unslop/`, which the rules file points to for chapters and checks. Existing `AGENTS.md`, `GEMINI.md` and `copilot-instructions.md` files are kept: the rules go between `<!-- unslop:start -->` and `<!-- unslop:end -->`, and a reinstall replaces only that block.

### Any other model, through an API

Paste `dist/system-prompt.md` into the system prompt. It needs no files: it holds the hard rules, the tokens, the copy rules and all 350 banned words.

## Checks

The skill ships two scripts with no dependencies beyond Python 3. Agents are told to run them before finishing and report the output.

```sh
python3 .agents/skills/unslop/scripts/scan.py src/        # CSS, HTML, JSX, TSX, Vue, Svelte, locale JSON, Markdown
python3 .agents/skills/unslop/scripts/lint.py README.md   # Markdown, stricter on prose
```

`scan.py` flags shadows, rings, gradients, backdrop blur, radius above 4px, pulsing animations, indigo or purple utilities, emoji, and banned words, dashes or exclamation marks in text a person reads. Add `unslop-ignore` to a line to skip it on purpose.

## Layout

| Path | What it is |
| --- | --- |
| `skills/unslop/` | The skill. Generated; do not edit by hand. |
| `dist/` | Zip for upload, adapters for other tools, system prompt. Generated. |
| `.claude-plugin/` | Claude Code plugin and marketplace manifests. |
| `UNSLOP.md` | The whole handbook in one file. Generated. |
| `src/parts/*.md` | Handbook source, concatenated in filename order. |
| `src/skill/` | Templates for `SKILL.md`, the adapters and the system prompt. |
| `src/banned-words.txt` | The 350 banned entries. |
| `src/AUTHORING.md` | Rules for anyone editing the parts. |
| `scripts/build.py` | Builds `UNSLOP.md`, then the skill and `dist/`, and lints all of it. |
| `scripts/install.py` | Installs the skill for one or more tools. |

## Build

```sh
python3 scripts/build.py
```

The build fails if the linter finds a single problem in the handbook, the skill or the adapters. Bump `VERSION` and the two files in `.claude-plugin/` together when you release.
