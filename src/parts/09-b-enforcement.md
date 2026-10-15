### 9.4 What scripts/lint.py checks

`scripts/lint.py` is the linter this handbook passes on every build. It is a single Python 3 file with no dependencies, written for Markdown. Copy it, with `src/banned-words.txt`, into any repository whose docs you want held to the same rules. It expects the word list at `src/banned-words.txt` relative to the parent of its own directory; change the `WORDS_FILE` line if your layout differs.

#### Running it

```sh
python3 scripts/lint.py src/parts/*.md
python3 scripts/lint.py README.md docs/*.md
python3 scripts/build.py
```

The first form lints the source parts. The second lints any other Markdown. The third concatenates the parts into `UNSLOP.md`, generates the contents and appendix, and runs the linter on the built file; it fails if the linter reports anything.

For each problem the linter prints one line, `path:line: message`. After each file it prints a summary line, `path: N characters, M problems`. The exit code is 1 when any file has a problem and 0 otherwise. Run with no arguments, it prints its usage text and exits with 2.

#### How it splits prose from code

The linter reads each file line by line and labels every line as fence, prose, code or slop.

- A line that starts, after optional spaces, with three or more backticks or tildes opens a fenced block when no block is open. The word after the fence is the tag, compared in lowercase.
- The block closes on a line that starts with the same fence string and contains nothing but fence characters.
- Lines inside a block tagged `slop` are slop. Lines inside any other fenced block, tagged or not, are code. Everything outside fences is prose.
- Inside prose, the linter removes inline code spans (backtick pairs on one line), link targets (the `(...)` part of `[text](...)`) and HTML comments that open and close on the same line before it looks for words and exclamation marks.

#### The five checks

1. Emoji and pictographs, on every line, including code and slop. One report per character, with its code point. The ranges are listed in the table below.
2. Em and en dashes (U+2014 and U+2013), on every line, including code and slop. One report per line.
3. Banned entries, in prose only. Each entry in `src/banned-words.txt` is matched case-insensitively, with no letter or digit directly before or after the match. One report per entry per line, quoting the text that matched.
4. Exclamation marks, in prose only. Any `!` that is not followed by `[` is reported, so image syntax `![alt](src)` passes.
5. Shadows, gradients and blur, in code only (fenced blocks not tagged `slop`). The rules are listed in the second table below.

Character ranges for check 1:

| Range | Contents |
| --- | --- |
| U+1F000 to U+1FAFF | Pictographs, emoticons, transport symbols, regional indicator flags |
| U+2600 to U+27BF | Miscellaneous symbols and dingbats: check marks, sparkles, stars, hearts |
| U+2B00 to U+2BFF | Arrows and stars used as emoji |
| U+2190 to U+21FF | Arrows |
| U+2300 to U+23FF | Miscellaneous technical: watch, hourglass, the command key symbol |
| U+FE0F, U+200D, U+20E3 | Emoji variation selector, zero-width joiner, keycap combiner |

Rules for check 5:

| Report | What it matches | Allowed |
| --- | --- | --- |
| box-shadow other than none | a `box-shadow` declaration | `box-shadow: none` |
| text-shadow other than none | a `text-shadow` declaration | `text-shadow: none` |
| drop-shadow filter | the CSS `drop-shadow()` function | nothing |
| Tailwind shadow utility | the bare utility and its `sm` to `2xl`, `inner` and arbitrary-value sizes | `shadow-none` |
| CSS gradient | `linear-`, `radial-`, `conic-` and repeating gradient functions | nothing |
| Tailwind gradient utility | `bg-gradient-*`, `bg-linear-*`, `bg-radial-*`, `bg-conic-*` | nothing |
| gradient color stop | `from-`, `via-`, `to-` with blue, indigo, violet, purple, fuchsia, sky or cyan | other stop colors, which still fail as part of a gradient utility |
| Tailwind ring utility | `ring-1`, `ring-2`, `ring-4`, `ring-8`, `ring-inset`, `ring-offset-*` and colored rings; they compile to `box-shadow` | `outline` utilities, `ring-0` |
| backdrop blur | a `backdrop-filter` declaration and the Tailwind `backdrop-blur` utilities | `backdrop-filter: none` |

#### How banned entries are matched

- A single word gets its inflections. The linter adds the suffixes s, es, d, ed, ing, ly, er, ers, est, ment, ments and ness. Words ending in e also match with the e dropped before ing, ingly and ely. Words ending in y also match the ies, ied, ily, ier and iest forms. Words ending in ize also match ization and izations, and every form is also matched with the British "is" spelling. Words ending in al also match ally.
- A phrase (any entry with a space or an apostrophe) is matched as written, with any run of whitespace between words. Matching works one line at a time, so a phrase broken across two lines is not caught. Phrases get no inflections.
- A hyphen inside an entry matches a hyphen or whitespace, so the entry for a hyphenated adjective also catches the same words written with a space.
- An apostrophe inside an entry matches a straight or a typographic apostrophe.

Some forms the suffix rules produce are not English words. That costs nothing, since they never match real text. A few real words are caught as forms of a banned stem; rewrite the sentence rather than arguing with the list.

#### What it does not check

- Banned words inside fenced code, including `text` blocks used for good examples. Read those by hand or with the searches in 9.3.
- Indented code blocks (four spaces, no fence). They are treated as prose, so a banned word in one is reported. Use fenced blocks.
- Inline code that spans a line break, and HTML comments that span lines. The parts on each line are linted as prose.
- Anything outside Markdown semantics. Run against HTML, JSX or CSS, the whole file is prose: banned words are caught, but shadows and gradients are not, because there are no fences. Use the scan script in 9.5 for product source.
- Sentence-level tells, layout, contrast, spacing and radius. Those need the searches in 9.2 and 9.3, and a person.

#### Fixing reports

| Report | Fix |
| --- | --- |
| `emoji or pictograph` | Delete it. Use a word, or `->` for an arrow. In UI, use an SVG icon with a label. |
| `em or en dash` | Period, comma, colon or parentheses. "to" for ranges. |
| `banned '...'` in a sentence | Rewrite with a plainer word or a number. |
| `banned '...'` when quoting the word | Put the mention in inline code, or move the example into a `slop` block. |
| `exclamation mark in prose` | Replace with a period. |
| `... in non-slop code` | Fix the example to follow the rules, or tag the block `slop` if it is meant as a bad example. |

### 9.5 CI integration

Two jobs cover a typical repository. The first lints Markdown with `scripts/lint.py`. The second scans product source with ripgrep for the visual and verbal tells that the Markdown linter cannot see.

#### The scan script

Save as `scripts/unslop-scan.sh` and make it executable. It runs each search, prints a GitHub annotation for every hit so the lines show up in the pull request diff, and exits with 1 when anything matched. The patterns are the ones from 9.2 and 9.3, reduced to the checks that should block a merge.

```sh
#!/usr/bin/env bash
# Fail when visual or verbal tells appear in product source.
set -uo pipefail

UI='*.{html,css,scss,sass,less,js,jsx,ts,tsx,vue,svelte,astro,mdx}'
TEXT='*.{md,mdx,html,jsx,tsx,vue,svelte,astro,json,yml,yaml}'
WORDS="${WORDS:-src/banned-words.txt}"
status=0

report() {
  local name="$1" hits="$2"
  [ -z "$hits" ] && return
  status=1
  while IFS= read -r hit; do
    file="${hit%%:*}"; rest="${hit#*:}"; line="${rest%%:*}"
    echo "::error file=${file#./},line=${line}::unslop: ${name}"
  done <<< "$hits"
  echo "${name}: $(printf '%s\n' "$hits" | wc -l) hits" >&2
}

check() {
  local name="$1" glob="$2" pattern="$3"
  report "$name" "$(rg -nP --no-heading -g "$glob" -g '!scripts/unslop-scan.sh' "$pattern" . || true)"
}

check "shadows"  "$UI" '(box|text)-shadow\s*:(?!\s*none\b)|drop-shadow|(?<![\w-])s[h]adow(-(sm|md|lg|xl|2xl|inner|\[[^\]]*\]))?(?![\w-])'
check "gradient" "$UI" '(repeating-)?(linear|radial|conic)-gradient\s*\(|(?<![\w-])bg-(gradient|linear|radial|conic)-|<(linear|radial)Gradient'
check "blur"     "$UI" 'backdrop-(blur|filter)|filter\s*:[^;]*blur\('
check "radius"   "$UI" '(?<![\w-])rounded(-[trblse]{1,2})?-(md|lg|xl|2xl|3xl)(?![\w-])|border-radius\s*:\s*([5-9]|[1-9][0-9]+)px'
check "purple"   "$UI" '(?<![\w-])(bg|text|border|ring|from|via|to)-(indigo|violet|purple|fuchsia)-[0-9]{2,3}'
check "pulse"    "$UI" 'animate-(ping|pulse)|>\s*(LIVE|NEW|BETA)\s*<'
check "emoji"    "*"   '[\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}\x{2B00}-\x{2BFF}\x{2190}-\x{21FF}\x{2300}-\x{23FF}\x{FE0F}\x{200D}]'
check "dash"     "*"   '[\x{2013}\x{2014}]|&[mn]dash;'
check "exclaim"  "*.json" ':\s*"[^"]*\w![^"]*"'

if [ -f "$WORDS" ]; then
  list="$(mktemp)"
  grep -v '^#' "$WORDS" | sed '/^$/d' > "$list"
  report "banned word" "$(rg -n -i -w -F --no-heading -f "$list" -g "$TEXT" -g '!banned-words.txt' . || true)"
  rm -f "$list"
fi

exit "$status"
```

Every `rg` call passes `.` as the path. Without a path, ripgrep reads standard input whenever it is not a terminal, which is the case in CI and in git hooks, and the search would hang or find nothing.

Skeleton loaders that pulse and avatars that use `rounded-full` are legitimate. Exclude their files with an extra `-g '!path'` in the relevant `check` line, and write the reason in a comment above it.

#### The workflow

Save as `.github/workflows/unslop.yml`:

```yaml
name: unslop

on:
  pull_request:
  push:
    branches: [main]

jobs:
  markdown:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Lint Markdown
        run: python3 scripts/lint.py $(git ls-files '*.md')

  source:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@v4
      - name: Install ripgrep
        run: sudo apt-get update && sudo apt-get install -y ripgrep
      - name: Scan for visual and verbal tells
        run: bash scripts/unslop-scan.sh
```

In this handbook's own repository, replace the Markdown step with `python3 scripts/build.py`, which builds `UNSLOP.md` and lints the result.

#### Changed files only

An existing product will fail the scan on its first run. Gate new code first and work through the backlog with the audit in 9.1. This variant lints only Markdown files the pull request touches:

```yaml
  markdown-changed:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Lint changed Markdown
        run: |
          files=$(git diff --name-only --diff-filter=ACMR "origin/${{ github.base_ref }}...HEAD" -- '*.md')
          if [ -n "$files" ]; then python3 scripts/lint.py $files; fi
```

For the source scan, run it on the base branch once, save the hit count per check, and fail the pull request only when a count goes up. Lower the saved counts as the backlog shrinks. When a count reaches zero, switch that check to the blocking script above.

### 9.6 Pre-commit hook

A hook catches problems before they reach CI, on the machine of the person who wrote them, in under a second.

#### Plain git hook

Commit the hook to `.githooks/pre-commit` and point git at the directory once per clone with `git config core.hooksPath .githooks`.

```sh
#!/bin/sh
# Lint staged Markdown and scan staged source for tells.
set -eu

md=$(git diff --cached --name-only --diff-filter=ACMR -- '*.md')
if [ -n "$md" ]; then
  python3 scripts/lint.py $md
fi

src=$(git diff --cached --name-only --diff-filter=ACMR -- \
  '*.css' '*.scss' '*.html' '*.jsx' '*.tsx' '*.vue' '*.svelte' '*.astro')
if [ -n "$src" ]; then
  if rg -nP '(box|text)-shadow\s*:(?!\s*none\b)|(?<![\w-])s[h]adow-(sm|md|lg|xl|2xl)|(linear|radial|conic)-gradient\s*\(|backdrop-(blur|filter)|[\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}\x{2013}\x{2014}]' $src; then
    echo "unslop: fix the lines above, or commit with --no-verify and explain why in the message." >&2
    exit 1
  fi
fi
```

The hook checks files as they are in the working tree, which can differ from what is staged when a file is partly staged. For most teams that gap does not matter; CI checks the committed version anyway.

#### pre-commit framework

If the repository already uses the `pre-commit` framework, add local hooks to `.pre-commit-config.yaml`. The framework passes only the staged file names that match `files`.

```yaml
repos:
  - repo: local
    hooks:
      - id: unslop-lint
        name: unslop lint (Markdown)
        entry: python3 scripts/lint.py
        language: system
        files: \.md$
      - id: unslop-scan
        name: unslop scan (source)
        entry: bash scripts/unslop-scan.sh
        language: system
        pass_filenames: false
        files: \.(css|scss|html|jsx|tsx|vue|svelte|astro|json)$
```

Then run `pre-commit install` once per clone, and `pre-commit run --all-files` to check the whole repository.

### 9.7 Review rubric

Automated checks catch the defaults. The rubric catches the rest. Score each page or template on the 15 criteria below, 0 to 2 points each, for a maximum of 30. Two reviewers score independently and then compare.

#### Hard fails

Any one of these fails the page regardless of score. Fix it before scoring the rest.

- Any shadow on any element, including focus rings drawn with a shadow.
- Any gradient in interface chrome: backgrounds, buttons, text, borders, overlays.
- Any emoji in text the team wrote.
- Any banned word in shipped copy.
- A "LIVE", "NEW" or "BETA" pill, or a pulsing status dot.
- Body text below 4.5:1 contrast against its background.

#### Criteria

| No. | Criterion | 0 points | 1 point | 2 points |
| --- | --- | --- | --- | --- |
| 1 | Depth | Blur, glass or glow | Borders mixed with heavy fills | 1px rules, tonal steps and spacing only |
| 2 | Color | Two or more accents, or purple and blue together | One accent used on more than 3 elements per view | One accent, on the primary action and the active state |
| 3 | Radius | Above 8px on cards or buttons | 4 to 8px | 0 or 2px, `rounded-full` only on avatars and controls that need it |
| 4 | Type | Default font with no reason, sizes off the scale | Sizes on the scale, lines over 80ch | Sizes on the scale, body 16px at 1.5, prose under 66ch |
| 5 | Layout | Hero, three cards, testimonials, CTA in template order | Template order with real content | Order follows what this reader needs first |
| 6 | Icons and status | Emoji or mixed icon sets | One set, some icons without labels | One SVG set at 16 or 20px, labeled, status as words |
| 7 | Motion | Entrance animations or over 300ms | Under 300ms, ignores reduced motion | 150ms or less, opacity and transform, off under reduced motion |
| 8 | Headline | Passes the swap test (a competitor could use it) | Specific but over 12 words | Under 10 words, names what the product does |
| 9 | Sentence tells | 3 or more per 500 words | 1 to 2 per 500 words | Under 1 per 500 words |
| 10 | Numbers | Round numbers with plus signs, no sources | Real numbers, some without dates or sources | Every number has a source and a date, or there are none |
| 11 | Buttons and labels | Generic verbs, title case | Verb and object, some inconsistencies | Verb and object, sentence case, the same word for the same action everywhere |
| 12 | Errors and empty states | Jokes or raw codes | States the problem only | States the problem and the next step, next to where it happened |
| 13 | Structure | Bulleted reasons, bold-label lists | Lists mostly used for lists | Lists only for parallel items, headings name their content |
| 14 | Voice | Could be any company | Consistent but generic | Passes the voice sheet; a customer would recognize the team |
| 15 | Accessibility | Missing focus styles or labels | Focus visible, some unlabeled controls | Visible 2px focus outline, every control named, keyboard order matches visual order |

#### Thresholds

- 27 to 30: ship.
- 22 to 26: fix every criterion that scored 0, then ship.
- Under 22: rewrite the page from its facts and rebuild the layout from the tokens. Patching individual tells at this score usually leaves the template visible.

Record scores in the findings log from 9.1 with the date, so the next audit can show movement.

### 9.8 Ship checklist for a page

Run this list for every new or changed page before it goes live. Each item is a yes or no. A single no blocks the release until it is fixed or a named person signs off on the exception in writing.

#### Automated

- [ ] `scripts/lint.py` reports 0 problems on every Markdown file the page uses.
- [ ] `scripts/unslop-scan.sh` passes on the branch.
- [ ] The paragraph script in 9.3 shows no uniform files, or each flag has been read and accepted.

#### Visual

- [ ] No shadows, gradients, blur or glow, checked in the browser's computed styles as well as in source.
- [ ] Radius is 0 or 2px everywhere except avatars and round controls.
- [ ] One accent color, used on the primary action and the active state only.
- [ ] Colors come from the tokens in light and dark themes; no hard-coded hex in components.
- [ ] Icons come from one SVG set, at 16 or 20px, each with a label or accessible name.
- [ ] No status pills or pulsing dots. Live data shows a timestamp.
- [ ] At 375px wide: no horizontal scroll, 16px side margins, tap targets at least 44px.

#### Copy

- [ ] The headline names what the product or page does and fails the swap test.
- [ ] Every number has a source and a date in the copy, in a footnote, or in the fact sheet that produced it.
- [ ] The page was read aloud by someone who did not write it.
- [ ] Sentence tells are under 1 per 500 words.
- [ ] Headings and buttons are in sentence case.
- [ ] No exclamation marks, no emoji, no em or en dashes.

#### Microcopy

- [ ] Every button is a verb and an object. The primary action is the only filled button in its view.
- [ ] Every form field has a visible label above it; placeholders hold examples only.
- [ ] Every error message says what failed and what to do, next to where it failed.
- [ ] Every empty state says what will appear and offers one action.
- [ ] Destructive actions name the object and the count, and say whether they can be undone.
- [ ] The meta description is unique to the page and between 120 and 155 characters.

#### Accessibility and behavior

- [ ] Body text contrast is at least 4.5:1 and large text and icons at least 3:1, in both themes.
- [ ] Every interactive element shows a 2px focus outline with a 2px offset.
- [ ] The page works by keyboard alone, in visual order.
- [ ] With reduced motion turned on, nothing moves.
- [ ] The page returns the right status code (200 for content, 404 for missing pages).

#### Final read

- [ ] One person on the team reads the page top to bottom at the size and on the device most customers use, and would put their name to every sentence on it.
