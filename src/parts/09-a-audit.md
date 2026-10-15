## Part 9. Audit and Enforcement

The earlier parts say what to build and how to write. This part says how to find the defaults already in a product and how to stop them from coming back. Searches find most visual tells in minutes. Verbal tells need searches plus a human read. Enforcement turns both into checks that run on every commit, so the fix holds after the people who made it move on.

### 9.1 Auditing an existing product

The procedure below is sized for a product with about 20 distinct screens or page templates and a marketing site of about 10 pages. Scale the times linearly. One person can do it in one working day; two people working in parallel on the visual and copy passes finish in about five hours.

#### Step 1. Inventory (30 minutes)

List every route, page template, transactional email and system message. Pull routes from the router config, emails from the mail template directory, and messages from the locale files. Screenshot each screen at 1280px and 375px wide, in light and dark theme if both exist. Name the files by route so findings can point at them: `invoices-list-1280-light.png`.

Record the inventory in a findings log. A Markdown table or a spreadsheet both work; the columns matter more than the tool.

| ID | Screen or file | Tell | Category | Count | Source | Severity | Fix |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V-001 | `/invoices` | Card with `shadow-lg` | Depth | 14 | `components/Card.tsx` | High | Border and `--paper-2` |
| C-001 | Pricing hero | False contrast | Copy | 1 | `pages/pricing.mdx` | Medium | Rewrite from fact sheet |

#### Step 2. Mechanical searches (20 minutes)

Run every command in 9.2 and 9.3 from the repository root and save the output to an `audit/` directory, one file per search. Counts per file tell you where the defaults live. A shadow utility that appears 200 times across 3 files is a component problem, fixed in 3 places. One that appears 200 times across 90 files is a habit, fixed with a lint rule and a codemod.

#### Step 3. Visual pass (60 to 90 minutes)

Open each screenshot at 100% and mark every visual tell the searches cannot see: a glow behind the hero, a three-card feature grid, a pill badge with a pulsing dot, an illustration in the generic flat style, a gradient baked into an image file, icons from three different sets, emoji used as icons. Log each one with the screen ID. Check contrast on every text color against its background and log anything under 4.5:1 for body text or 3:1 for large text and icons.

#### Step 4. Copy pass (60 to 120 minutes)

Read every page aloud, at speaking pace. Mark each tell from Part 8 with a short code (FC for false contrast, TRI for tricolon, CR for colon reveal, and so on) in the margin of a printout or as comments on a copy of the text. Then count tells per 500 words for each page and log the density. Pages above 3 per 500 words go to the top of the rewrite list. Marketing pages usually score worst; settings screens usually score best.

#### Step 5. Microcopy pass (45 minutes)

Export every interface string from the locale files into one sorted list. Read it as a list, grouped by type: all buttons together, all errors together, all empty states together. Inconsistencies show up only in a list ("Delete", "Remove", "Trash" for the same action; "Your invoices" next to "My clients"). Check each group against the rules in 8.6 and 8.7.

#### Step 6. Score (30 minutes)

Score each page template with the rubric in 9.7. Two people score independently, then compare. Any criterion where the scores differ by more than one point gets discussed until both agree on the reason, which usually exposes a rule nobody wrote down.

#### Step 7. Prioritize (30 minutes)

Order the fix list by reach, then severity. Shared components and layout templates come first, because one change there removes dozens of instances. Then the pages with the most traffic. Then everything else. Hard fails from 9.7 (shadows, gradients, emoji, banned words, status pills) are fixed before any page ships again, whatever their traffic.

#### Step 8. Fix, then lock (varies)

Fix in the order of the list. As each category reaches zero, add its check to CI (9.5) and the pre-commit hook (9.6) so it stays at zero. A category without an automated check comes back within two release cycles, usually through a copied component or a generated page.

Time summary for the reference size:

| Step | Time |
| --- | --- |
| Inventory | 30 min |
| Mechanical searches | 20 min |
| Visual pass | 60 to 90 min |
| Copy pass | 60 to 120 min |
| Microcopy pass | 45 min |
| Score | 30 min |
| Prioritize | 30 min |
| Total before fixing | 4.5 to 6 hours |

### 9.2 Search commands for visual tells

All commands use ripgrep 14. Run them from the repository root. ripgrep skips files listed in `.gitignore`, so `node_modules` and build output are excluded unless you pass `--no-ignore`. Each command prints file, line and match; add `-c` for counts per file or `--stats` for a total.

Set the file globs once per shell session:

```sh
UI='*.{html,css,scss,sass,less,js,jsx,ts,tsx,vue,svelte,astro,mdx}'
```

Some patterns spell a word with a one-letter character class, such as `s[h]adow`. The class matches the same text; it only stops the handbook's own linter from flagging the command as a use of the utility.

#### Shadows

CSS declarations and the filter function:

```sh
rg -nP -g "$UI" '(box|text)-shadow\s*:(?!\s*none\b)|drop-shadow' .
```

Tailwind utilities, including variants such as `hover:` and colored shadows, but not `shadow-none`:

```sh
rg -nP -g "$UI" '(?<![\w-])s[h]adow(-(sm|md|lg|xl|2xl|inner|\[[^\]]*\]|[a-z]+-[0-9]{2,3}))?(?![\w-])' .
```

Shadow and elevation tokens in a theme or design token file (this also repeats CSS declarations found by the first search):

```sh
rg -nP -g '*.{js,ts,json,css,scss}' '(--|["'\'']?)(s[h]adow|elevation)[\w-]*["'\'']?\s*:' .
```

Replace each shadow with a 1px `--rule` border, a tonal step to `--paper-2`, or more spacing. Delete the token so nobody reaches for it again.

#### Gradients

CSS gradient functions, Tailwind gradient utilities and Tailwind color stops:

```sh
rg -nP -g "$UI" '(repeating-)?(linear|radial|conic)-gradient\s*\(|(?<![\w-])bg-(gradient|linear|radial|conic)-|(?<![\w-])(from|via|to)-[a-z]+-[0-9]{2,3}(?![\w-])' .
```

SVG gradients, which ship inside icons and illustrations:

```sh
rg -n -g '*.{svg,jsx,tsx,vue,svelte,html}' '<(linear|radial)Gradient' .
```

Gradients baked into raster images do not show up in any search. The visual pass in 9.1 catches them; replace the image.

#### Blur and glass

Backdrop blur, blur filters, and the large blur utilities used for glow blobs behind hero sections:

```sh
rg -nP -g "$UI" 'backdrop-(blur|filter)|filter\s*:[^;]*blur\(|(?<![\w-])blur-(sm|md|lg|xl|2xl|3xl)(?![\w-])' .
```

A glow blob is usually an absolutely positioned `div` with `rounded-full`, a saturated background and `blur-3xl`. Delete the element, not just the blur.

#### Radius

Tailwind radius utilities above the 4px ceiling, and CSS radius values above 4px:

```sh
rg -nP -g "$UI" '(?<![\w-])rounded(-[trblse]{1,2})?-(md|lg|xl|2xl|3xl)(?![\w-])|border-radius\s*:\s*([5-9]|[1-9][0-9]+)px|border-radius\s*:\s*(0?\.[3-9]|[1-9][0-9.]*)rem' .
```

Then review `rounded-full` by hand. It is correct for avatars, radio buttons and switch knobs, and wrong on buttons, badges and cards:

```sh
rg -n -g "$UI" 'rounded-full' .
```

#### Indigo, violet and purple

Tailwind color utilities in the default AI palette:

```sh
rg -nP -g "$UI" '(?<![\w-])(bg|text|border|ring|outline|fill|stroke|from|via|to|accent|caret|decoration|divide|placeholder)-(indigo|violet|purple|fuchsia)-[0-9]{2,3}' .
```

The same colors as hex values (Tailwind v3 indigo, violet, purple and fuchsia at 400 to 700), and as Tailwind v4 theme variables:

```sh
rg -niP -g "$UI" '#(818cf8|6366f1|4f46e5|4338ca|a78bfa|8b5cf6|7c3aed|6d28d9|c084fc|a855f7|9333ea|d946ef)\b' .
rg -n -g "$UI" -e '--color-(indigo|violet|purple|fuchsia)' .
```

Blue is not banned as an accent, but blue next to purple in a gradient is. Run the gradient search above with `blue` in mind, and check any `sky` or `cyan` stop next to a purple one.

#### Emoji and pictographs

The same ranges `scripts/lint.py` rejects, in every text file:

```sh
rg -nP '[\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}\x{2B00}-\x{2BFF}\x{2190}-\x{21FF}\x{2300}-\x{23FF}\x{FE0F}\x{200D}\x{20E3}]' .
```

Emoji written as shortcodes, HTML entities or JavaScript escapes:

```sh
rg -n ':(sparkles|rocket|tada|fire|zap|bulb|star2?|white_check_mark|heavy_check_mark|art|bug|memo|lock|wrench|recycle|boom|100|eyes|raised_hands|point_right):' .
rg -niP '&#x(1F[0-9a-f]{3}|2[67][0-9a-f]{2});|\\u\{1F[0-9a-f]{3}\}|\\uD83[CDE]' .
```

The arrow range catches `->` replaced by a glyph in button labels. The misc technical range catches the command key symbol in shortcut hints; write "Cmd" instead.

#### Dashes

```sh
rg -nP '[\x{2013}\x{2014}]|&[mn]dash;|&#821[12];' .
```

#### Status pills and pulsing dots

The "LIVE" badge with a green dot is usually a pill with `animate-ping` or `animate-pulse` on a small circle:

```sh
rg -nP -g "$UI" 'animate-(ping|pulse)|@keyframes\s+(pulse|ping|glow)' .
rg -nP -g "$UI" '>\s*(LIVE|NEW|BETA|HOT)\s*<' .
```

Replace with the word and a timestamp: "Updated 14:02". Skeleton loaders may use a pulse; check each hit.

#### Default type and layout

The Inter default and the three-card feature grid are not banned outright, but each needs a reason:

```sh
rg -nP -g "$UI" "(font-family\s*:[^;]*|family=|import\s*\{\s*)Inter\b|['\"]Inter['\"]" .
rg -nP -g "$UI" '(?<![\w-])((sm|md|lg|xl):)?grid-cols-3(?![\w-])' .
```

### 9.3 Search commands for verbal tells

Set a glob that covers copy, wherever it lives: Markdown, templates, components and locale files.

```sh
TEXT='*.{md,mdx,txt,html,jsx,tsx,vue,svelte,astro,json,yml,yaml,po,strings,xml}'
```

#### Banned words

Strip comments and blank lines from the list, then search for whole words, case-insensitive. The `!banned-words.txt` glob keeps the list from matching itself.

```sh
grep -v '^#' src/banned-words.txt | sed '/^$/d' > /tmp/unslop-words.txt
rg -n -i -w -F -f /tmp/unslop-words.txt -g "$TEXT" -g '!banned-words.txt' .
```

This matches each entry exactly as written. It misses inflections that `scripts/lint.py` catches (`optimization`, `leveraging`), so add a stem search for the most common verbs:

```sh
rg -niP -g "$TEXT" '\b(leverag|utili[sz]|optimi[sz]|enhanc|empower|streamlin|elevat|unlock|unleash|revolutioni[sz]|supercharg|harness|foster|showcas|underscor)\w*' -g '!banned-words.txt' .
```

Frequency table, to see which words a codebase leans on:

```sh
rg -o -i -w -F -N --no-filename -f /tmp/unslop-words.txt -g "$TEXT" -g '!banned-words.txt' . \
  | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -rn | head -40
```

Product repositories do not contain `src/banned-words.txt`. Copy the file in, or point `-f` at a shared copy.

#### Sentence patterns

Each search below finds candidates. Read every hit; some will be fine in context. Patterns use `.?` in place of an apostrophe so they match straight and typographic quotes and stay easy to quote in a shell.

False contrast:

```sh
rg -nPi -g "$TEXT" '\b(isn.?t|is not|aren.?t|are not|don.?t|do not)\s+(just\s+)?(a|an|about|sell)\b[^.]{0,60}\.\s+(it|we|they)(.?s|.?re| is| are| sell)\b' .
```

"Not just X, but Y" and its relatives:

```sh
rg -nPi -g "$TEXT" '\bnot (just|only|merely)\b[^.]{0,80}\bbut\b|\bmore than (just )?an?\b|\band so much more\b|\band beyond\b' .
```

Groups of three (adjective triples on their own line, and clipped imperative triples):

```sh
rg -nP -g "$TEXT" '^\s*[A-Z][a-z]+, [a-z]+,? and [a-z]+\.?\s*$' .
rg -nP -g "$TEXT" '\b[A-Z][a-z]+ [a-z]+\. [A-Z][a-z]+ [a-z]+\. [A-Z][a-z]+( [a-z]+){1,3}\.' .
```

Colon reveals:

```sh
rg -nPi -g "$TEXT" '\b(the (result|secret|catch|kicker|bottom line|truth|answer|twist|payoff)|one word)\s*[:?]' .
```

Rhetorical questions as headings, lines or element text:

```sh
rg -nP -g "$TEXT" '^(#+\s+)?[A-Z][^.?!\n]{3,80}\?\s*$|>\s*[A-Z][^<?]{3,80}\?\s*<' .
```

"Imagine", "Here is why" and the summary sentence:

```sh
rg -nPi -g "$TEXT" '\b(imagine|picture this|what if)\b' .
rg -nPi -g "$TEXT" '\bhere(.?s| is) (why|how|what|the thing)\b|\bthat.?s (exactly )?why\b' .
rg -nPi -g "$TEXT" '\b(in short|simply put|in summary|in conclusion|all in all|to sum up|the takeaway|the bottom line)\b' .
```

Audience and range openers:

```sh
rg -nPi -g "$TEXT" '\bwhether you(.?re| are)\b|\b(teams|businesses|companies) of all sizes\b' .
rg -nPi -g "$TEXT" '\bfrom (\w+ ){1,2}to (\w+ ?){1,2}[,.]' .
```

Sign-posting, closing offers and sycophantic openers:

```sh
rg -nPi -g "$TEXT" '\blet.?s (break|dive|explore|take a|get started|unpack)|\bwithout further ado\b|\bin this (article|guide|post|section|tutorial),? we.?ll\b' .
rg -nPi -g "$TEXT" '\b(let me know if|feel free to|hope this helps|happy coding|don.?t hesitate|reach out)\b' .
rg -nPi -g "$TEXT" '^\W*(great question|absolutely|certainly|of course|you.?re (absolutely )?right)\b|\b(awesome|woohoo|yay|nice work|great job|you did it)\b' .
```

Hedging stacks, fake specificity and adverb inflation:

```sh
rg -nPi -g "$TEXT" '\b(can|could|may|might)\s+(potentially|possibly|perhaps|help(s)? to)\b' .
rg -nPi -g "$TEXT" '\b[0-9][0-9,.]*\s?(k|m|million|thousand)?\+|\bup to [0-9]+|\b[0-9]+(\.[0-9])?x (faster|better|more|cheaper)\b|\bstudies (show|suggest)\b|\b99\.9+%' .
rg -nPi -g "$TEXT" '\b(seamlessly|effortlessly|simply|easily|incredibly|truly|really|instantly|literally)\b' .
```

Exclamation marks in interface strings (locale JSON, then element text):

```sh
rg -nP -g '*.json' ':\s*"[^"]*\w![^"]*"' .
rg -nP -g '*.{html,jsx,tsx,vue,svelte,astro}' '>[^<{]*\w![^<]*<' .
```

Bold-label bullets and title-case headings in Markdown, and title-case labels in components:

```sh
rg -nP -g '*.{md,mdx}' '^\s*[-*+] \*\*[^*]+(:\*\*|\*\*:)' .
rg -nP -g '*.{md,mdx}' '^#{1,6} ([A-Z][a-z]+ ){2,}[A-Z][a-z]+\s*$' .
rg -nP -g '*.{html,jsx,tsx,vue,svelte,astro}' '>\s*([A-Z][a-z]+ ){1,5}[A-Z][a-z]+\s*<' .
```

#### Paragraph length

Uniform paragraph length cannot be found with a regex. This script prints word counts per paragraph for Markdown files and flags files where the longest paragraph is less than three times the shortest:

```python
import re, sys

for path in sys.argv[1:]:
    text = re.sub(r"`{3}.*?`{3}", "", open(path, encoding="utf-8").read(), flags=re.S)
    paras = [p for p in re.split(r"\n\s*\n", text)
             if p.strip() and not re.match(r"\s*([#|>-]|\d+\.|\*)", p)]
    counts = [len(p.split()) for p in paras]
    if len(counts) < 4:
        continue
    ratio = max(counts) / max(min(counts), 1)
    flag = "UNIFORM" if ratio < 3 else "ok"
    print(f"{path}: {len(counts)} paragraphs, {min(counts)} to {max(counts)} words, ratio {ratio:.1f} {flag}")
```

Save it as `scripts/paragraphs.py` and run `python3 scripts/paragraphs.py $(git ls-files '*.md')`. Read every flagged file; a short changelog can be uniform for good reasons.
