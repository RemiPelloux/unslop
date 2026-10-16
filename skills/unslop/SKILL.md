---
name: unslop
description: Design and copy rules for interfaces and text that must not look or read as machine-made. Use when building, styling or reviewing any user interface (HTML, CSS, Tailwind, React, Vue, Svelte, shadcn/ui), picking colors, type, spacing, icons or components, writing landing pages, UI copy, error messages, docs, READMEs, release notes or commit messages, or when asked to make something look or sound less generic or less like AI output. Bans box shadows, gradients, glass and blur, emoji, glowing status pills and 350 overused words, and ships scripts that check for all of them. Not for backend code with no text a person reads.
metadata:
  version: "1.0.0"
  source: "https://github.com/remipelloux/unslop"
---

# UNSLOP

Rules for interfaces and copy that do not carry the generated look: no indigo buttons, no `rounded-2xl shadow-lg` cards, no gradient headlines, no emoji, no LIVE pills, no `seamless` or `unlock`. Every rule has values and a check.

This file holds the rules you need on every task. The full handbook (1,256,340 characters) sits under `references/`, behind a deep index that points to exact line ranges, so a task reads a few thousand characters instead of a million. All paths below are relative to the folder this file is in.

## Workflow

1. **Before writing interface code:** apply the hard rules and tokens below, then pull the sections for the task: `python3 scripts/find.py --task NAME` (routes are listed at the end of this file). Read only the line ranges it prints.
2. **Before writing copy:** apply the copy rules below. Run your draft through `python3 scripts/find.py --text "..."`: it names every banned word with its replacements, without opening any file.
3. **Before you finish:** run the checks and fix everything they report.

```sh
python3 scripts/scan.py path/to/changed/files   # CSS, HTML, JSX, TSX, Vue, Svelte, locale JSON, Markdown
python3 scripts/lint.py path/to/file.md          # Markdown only, stricter on prose
```

Report the output in your reply. Never claim compliance you did not check. A line that must break a rule on purpose takes an `unslop-ignore` comment and a reason.

## Hard rules

Follow these in every file you create or edit. If the user explicitly asks for something a rule forbids, do it, and say which rule you broke and why.

### Visual

1. **No shadows.** No `box-shadow` (except `none`), no `text-shadow`, no `filter: drop-shadow()`, no Tailwind `shadow-*` except `shadow-none`, no Tailwind `ring-*` (it compiles to a shadow). Separate layers with a 1px border in `var(--rule)` and a background step: `--paper`, `--paper-2`, `--paper-3`.
2. **No gradients.** No `linear-gradient`, `radial-gradient`, `conic-gradient`, Tailwind `bg-gradient-*`, `bg-linear-*`, `from-*`, `via-*`, `to-*`, gradient text, gradient borders, or a glow behind a hero. Above all, never blue to purple.
3. **No glass, blur, glow or neon.** No `backdrop-filter`, no `backdrop-blur`, no blurred color blobs, no animated borders.
4. **Radius is 0 or 2px.** Never above 4px on a rectangle. Circles only for avatars and radio buttons. No `rounded-lg`, `rounded-xl`, `rounded-2xl`.
5. **One accent, outside the blue-violet band.** OKLCH hue 235 to 335 is off limits for the brand accent, buttons and links. Never Tailwind `indigo`, `violet`, `purple` or `fuchsia`. The accent marks the one primary action on a screen.
6. **No emoji.** Not in the interface, copy, docs, READMEs, code comments or commit messages. Icons come from one SVG set: 1.5px stroke, 16 or 20px.
7. **No status pills.** No green dot, no pulsing dot, no rounded capsule saying LIVE, Online, New or Beta. Write the state and the time it was last true: "Connected. Last sync 14:02 UTC."
8. **No box by default.** Do not put every section in a card. Group with spacing first, a top rule second, a background step third. A bordered box is for a thing the user acts on as a unit.
9. **Left-align.** Center only one short line: a heading, a button label, a single number.
10. **Motion stays at or under 150ms**, `ease-out`, opacity and transform only, and nothing at all under `prefers-reduced-motion: reduce`. No scroll reveals, no `animate-ping`, `animate-pulse` or `animate-bounce`, no parallax, no typing effects.
11. **Show the real thing.** Real screenshots with a 1px border, real numbers with a unit and a date. No 3D blobs, isometric art, AI stock images, or device mockups tilted in space.
12. **Focus is visible.** `outline: 2px solid var(--focus); outline-offset: 2px;` Never remove an outline without a visible replacement.

### Tokens

```css
:root {
  --paper: #F7F5F0;  --paper-2: #EFECE4;  --paper-3: #E5E1D6;
  --ink: #1A1A18;    --ink-2: #4A4843;    --ink-3: #6F6C64;
  --rule: #D9D5CB;   --rule-strong: #1A1A18;
  --accent: #B4441C; --accent-ink: #FFFFFF;
  --ok: #2F6B3A;     --warn: #8A6100;     --bad: #A3271F;
  --focus: #1A1A18;  --radius: 2px;
  --font-sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-serif: "Source Serif 4", Georgia, serif;
  --font-mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}
:root[data-theme="dark"] {
  --paper: #141412;  --paper-2: #1E1D1A;  --paper-3: #2A2925;
  --ink: #ECE9E1;    --ink-2: #B5B1A7;    --ink-3: #8F8B81;
  --rule: #34322E;   --rule-strong: #ECE9E1;
  --accent: #E2703F; --accent-ink: #141412;
  --ok: #7FB38A;     --warn: #D9A93A;     --bad: #E0705F;
  --focus: #ECE9E1;
}
```

- Spacing (px): 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Nothing else.
- Type (px): 12, 14, 16, 18, 21, 24, 32, 40, 56. Body 16 at line height 1.5. Headings 1.15 to 1.25. Prose at most 66ch per line.
- Borders: 1px solid `var(--rule)` for dividers. Form controls need 3:1 contrast, so give inputs, selects and checkboxes a `var(--ink-3)` border.
- Tertiary text (`--ink-3`) only on `--paper`. On `--paper-2` and `--paper-3` use `--ink-2`.
- Swap the accent for a brand color only if it passes rule 5 and 4.5:1 contrast for text.

### Copy

1. **No banned words.** None of the 350 entries in `references/banned-words.txt`, in any form (`leverage`, `leveraging`, `optimization`, `cutting edge`). If a sentence needs one to stand up, it has no claim in it: write the claim, or delete the sentence.
2. **No em dashes, no exclamation marks, no rhetorical questions.** Use a period or a comma.
3. **The first line says what the product does and for whom**, in words a customer would use. Then show it: a screenshot, a code sample, or a number with a unit and a date.
4. **Buttons name the action:** "Create invoice", "Install CLI", "Delete 3 files". Never "Get started", "Learn more" or "Submit" when a specific verb exists.
5. **Headings label the content:** "Pricing", "Install", "Limits". No slogans in headings.
6. **Every number has a unit, a source or a date.** Delete numbers you cannot source. No "10x faster", no "Trusted by 10,000+ teams".
7. **Testimonials need a full name, role, company and date**, or they go.
8. **No stock sentence shapes:** "It is not X, it is Y", "Not just X, but Y", groups of three adjectives, a colon before a reveal, "Imagine...", "Whether you are A or B", "From X to Y", a closing sentence that repeats the paragraph, a closing offer of more help.
9. **Lists hold parallel items. Paragraphs hold reasoning.** Do not turn every paragraph into bullets, and do not open every bullet with a bold label.
10. **Sentence case for headings and buttons.** Not Title Case Everywhere.

## Most frequent banned words

These are the entries models produce most. Any form counts. The other entries are in `references/banned-words.txt`.

```slop
delve, leverage, utilize, harness, unlock, unleash, elevate, empower,
streamline, revolutionize, supercharge, embark, navigate, foster, cultivate, underscore,
showcase, spearhead, bolster, amplify, reimagine, redefine, reshape, curate,
embrace, enhance, enrich, facilitate, optimize, maximize, democratize, future-proof,
unpack, immerse, captivate, ignite, propel, skyrocket, boost, fuel,
encompass, embody, thrive, garner, boast, elucidate, disrupt, level up,
dive into, deep dive, lean into, reach out, weave, orchestrate, seamless, robust,
comprehensive, cutting-edge, innovative, groundbreaking, game-changing, transformative, revolutionary, pivotal,
crucial, vital, essential, paramount, intricate, nuanced, holistic, dynamic,
vibrant, meticulous, unparalleled, compelling, stunning, remarkable, exceptional, invaluable,
intuitive, user-friendly, frictionless, effortless, delightful, sleek, elegant, modern,
next-gen, state-of-the-art, world-class, best-in-class, enterprise-grade, powerful, premium, bespoke,
tailored, immersive, engaging, impactful, actionable, insightful, diverse, vast,
crisp, clean, beautiful, magical, cohesive, granular, ai-powered, data-driven,
end-to-end, all-in-one, unified, curated, handcrafted, tapestry, testament, realm,
landscape, journey, ecosystem, paradigm, synergy, game-changer, insight, superpower,
solution, innovation, magic, furthermore, moreover, additionally, ultimately, essentially,
indeed, truly, in today's, the power of, the future of, with ease, made simple, take your,
when it comes to, whether you're, more than just, look no further
```

## Finding anything

Do not read whole chapters, and never read `references/index.json` itself. Ask the index, then read only the lines it names.

```sh
python3 scripts/find.py --task dashboard          # reading list for a kind of task, with line ranges and cost
python3 scripts/find.py focus ring on a button    # the best sections for any question, ranked
python3 scripts/find.py modal --show              # ... and print the best one
python3 scripts/find.py dark mode --budget 4000   # ... or print hits until 4,000 characters
python3 scripts/find.py --code dialog --lang css  # reference code blocks only
python3 scripts/find.py --section 4.6/rules       # one section by id
python3 scripts/find.py --chapter 4.6             # every section of a chapter
python3 scripts/find.py --word leveraging         # the banned entry behind any word form
python3 scripts/find.py --text "draft copy"       # every banned word in a draft, with replacements
```

Every hit prints `path:start-end` and its size. Read those lines with your file tool's offset and limit, or with `sed -n 'START,ENDp' PATH`. Add `--json` for machine output. Without Python, search `references/DEEP-INDEX.md`: one line per section, with its id, line range, size and distinctive terms.

## Task routes

Each route lists the rules, reference code and states of the chapters a task needs, in reading order. Run `python3 scripts/find.py --task ID` for the exact line ranges.

| Task | Run | Chapters | Cost |
| --- | --- | --- | --- |
| Marketing or SaaS landing page | `--task landing-page` | 4.20, 4.21, 5.16, 5.18, 5.19, 4.18, 6.8, 8.8 | ~4k tokens |
| AI product page or chat assistant UI | `--task ai-product` | 5.24, 6.17, 4.21 | ~2k tokens |
| Developer tool or open source project site | `--task devtool-site` | 6.9, 4.10, 8.8 | ~2k tokens |
| Dashboard or analytics screen | `--task dashboard` | 5.25, 4.8, 4.12, 5.1, 2.10, 6.10 | ~4k tokens |
| Settings or admin area | `--task settings` | 5.9, 4.19, 4.9, 5.8, 5.11 | ~4k tokens |
| Forms and inputs | `--task forms` | 4.19, 4.9, 5.8, 4.13, 4.17, 8.6 | ~4k tokens |
| Sign in, sign up, password reset | `--task auth` | 5.23, 4.19, 8.6 | ~2k tokens |
| Pricing page or plan comparison | `--task pricing` | 5.5, 5.21, 6.14, 8.7 | ~2k tokens |
| Documentation site | `--task docs-site` | 6.12, 4.10, 5.7, 4.5, 3.3 | ~3k tokens |
| Blog or long-form article page | `--task blog` | 6.13, 3.1, 3.2, 3.3 | ~2k tokens |
| Personal portfolio | `--task portfolio` | 6.11, 3.8 | ~1k tokens |
| E-commerce product page | `--task ecommerce` | 6.19, 4.6 | ~2k tokens |
| Mobile app marketing page | `--task mobile-app-page` | 6.15, 3.8 | ~1k tokens |
| Design system, tokens and base styles | `--task design-system` | 6.1, 2.3, 2.9, 6.5 | ~5k tokens |
| Tailwind setup without shadows or gradients | `--task tailwind` | 6.2, 6.3, 2.11 | ~3k tokens |
| shadcn/ui component overrides | `--task shadcn` | 6.4 | ~3k tokens |
| Palette, accent and semantic color | `--task color` | 2.3, 2.4, 2.2 | ~4k tokens |
| Dark mode | `--task dark-mode` | 2.9 | ~1k tokens |
| Depth without shadows: cards, overlays, layers | `--task depth` | 2.5, 2.6, 4.7 | ~3k tokens |
| Modals, menus, popovers, tooltips | `--task overlays` | 4.14, 4.15, 4.25, 5.14, 2.5 | ~3k tokens |
| Navigation: header, sidebar, tabs, breadcrumbs | `--task navigation` | 4.20, 5.1, 5.11, 4.5, 5.4, 3.6 | ~4k tokens |
| Status, live indicators, badges | `--task status` | 4.4, 5.2, 2.4 | ~3k tokens |
| Empty, loading and error states | `--task states` | 4.16, 4.24, 5.22, 8.6 | ~2k tokens |
| Typefaces and type scale | `--task typography` | 3.1, 3.2, 3.3 | ~3k tokens |
| Spacing, grid and responsive layout | `--task layout` | 3.4, 3.5, 3.6 | ~3k tokens |
| Animation and motion | `--task motion` | 3.9 | ~2k tokens |
| Accessibility checks | `--task accessibility` | 3.10 | ~1k tokens |
| Icons, screenshots and images | `--task icons-images` | 3.7, 3.8 | ~2k tokens |
| Interface copy: buttons, errors, empty states | `--task ui-copy` | 8.6, 8.7, 8.5 | ~3k tokens |
| Headlines and marketing copy | `--task marketing-copy` | 8.2, 8.3, 8.8, 8.10 | ~3k tokens |
| README, commit messages, PRs, release notes | `--task dev-writing` | 8.8, 8.5 | ~2k tokens |
| Prompting a model for plain copy | `--task prompting` | 8.11, 6.7 | ~2k tokens |
| Review or audit an existing product | `--task audit` | 9.1, 9.2, 9.7, 9.8 | ~4k tokens |
| CI, lint and pre-commit enforcement | `--task enforcement` | 9.5, 9.6, 6.6 | ~3k tokens |

Parts, for browsing. Every chapter and its file: `references/INDEX.md`. Every section with its line range: `references/DEEP-INDEX.md`.

- Part 1. Ground Rules (1.1 to 1.9)
- Part 2. Color, Surfaces and Depth (2.1 to 2.12)
- Part 3. Type, Space, Layout, Icons and Motion (3.1 to 3.11)
- Part 4. Components, A to M (4.1 to 4.25)
- Part 5. Components, N to Z, and Marketing Sections (5.1 to 5.25)
- Part 6. Stack Setup and Full Page Rebuilds (6.1 to 6.20)
- Part 7. The Lexicon (7.0 to 7.5)
- Part 8. Sentences, Structure and Microcopy (8.1 to 8.12)
- Part 9. Audit and Enforcement (9.1 to 9.8)
