# Authoring rules for UNSLOP.md

Every file in `src/parts/` is concatenated, in filename order, into `UNSLOP.md`.
Every part file must pass `python3 scripts/lint.py <file>` with 0 problems before it is committed.

## Hard rules the linter enforces

1. No emoji or pictographic symbols anywhere, code blocks included. No check marks, no sparkles, no arrows (U+2190 to U+21FF), no stars. Write "to" or "->" instead of an arrow glyph.
2. No em dashes and no en dashes anywhere. Use a period, a comma, a colon, parentheses, or a plain hyphen.
3. None of the 350 entries in `src/banned-words.txt` may appear in prose, in any inflection (s, ed, ing, ly, er, ment, ness, ization). Prose is everything outside fenced code and inline code.
4. A banned word may only appear as a *mention*: inside inline code (`delve`) or inside a fenced block tagged `slop`. Use `slop` fences for every bad example.
5. No exclamation marks in prose.
6. In any fenced code block that is NOT tagged `slop`: no `box-shadow` other than `none`, no `text-shadow` other than `none`, no `drop-shadow()`, no Tailwind `shadow`/`shadow-*` utilities except `shadow-none`, no CSS gradients of any kind, no Tailwind gradient utilities, no `backdrop-blur` / `backdrop-filter`.

Watch for words that are easy to type by accident: essential, crucial, vital (also "Web Vitals"), robust, powerful, modern, clean, crisp, intuitive, seamless, overall, ultimately, indeed, truly, solution, insight, landscape, journey, navigate, enhance (also "enhancement"), optimize (also "optimization"), boost, leverage, dynamic, unified, premium, tailored, diverse, vast, magic, delight, beautiful, elegant, engaging, strategic, granular, comprehensive, best practices, underscore, showcase, foster, the power of, when it comes to, more than just, feel free to. If you need the literal sense, use inline code or a plainer word.

## House style for prose

- Imperative, specific, short. State the rule, then the number. "Body text is 16px at 1.5 line height." Not "Consider choosing a comfortable size."
- Numbers beat adjectives. Hex values, px, ms, ratios, counts.
- No rhetorical questions. No "Here is the thing." No colon reveals ("The result: ..."). No "It is not X, it is Y" constructions. No groups of three adjectives.
- No filler openers ("In this section we will"). Start with the rule.
- Bold sparingly: only the rule label at the start of a list item, if at all.
- Every claim about why a pattern reads as machine-made must be concrete: name the default it comes from (Tailwind `indigo-500`, shadcn `Card`, `rounded-2xl shadow-lg`, the Inter default, the hero with a radial glow, etc).

## Heading levels

- `##` Part (only at the top of a Part's first file): `## Part 4. Components, A to M`
- `###` Chapter: `### 4.3 Buttons`
- `####` Section or lexicon entry
- Deeper levels are allowed inside a section.

## Canonical tokens (use these everywhere so the document agrees with itself)

Light theme:

```css
:root {
  --paper: #F7F5F0;      /* page background */
  --paper-2: #EFECE4;    /* recessed surface: table header, code block, sidebar */
  --paper-3: #E5E1D6;    /* pressed / selected surface */
  --ink: #1A1A18;        /* primary text, strong rules */
  --ink-2: #4A4843;      /* secondary text */
  --ink-3: #6F6C64;      /* tertiary text, placeholders (4.6:1 on --paper) */
  --rule: #D9D5CB;       /* default 1px border */
  --rule-strong: #1A1A18;/* emphasis border, focus ring base */
  --accent: #B4441C;     /* burnt orange; one accent per product */
  --accent-ink: #FFFFFF; /* text on accent */
  --ok: #2F6B3A;
  --warn: #8A6100;
  --bad: #A3271F;
  --focus: #1A1A18;
  --radius: 2px;         /* 0 or 2px. Never above 4px. */
  --font-sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-serif: "Source Serif 4", Georgia, "Times New Roman", serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}
```

Dark theme:

```css
:root[data-theme="dark"] {
  --paper: #141412;
  --paper-2: #1E1D1A;
  --paper-3: #2A2925;
  --ink: #ECE9E1;
  --ink-2: #B5B1A7;
  --ink-3: #8F8B81;
  --rule: #34322E;
  --rule-strong: #ECE9E1;
  --accent: #E2703F;
  --accent-ink: #141412;
  --ok: #7FB38A;
  --warn: #D9A93A;
  --bad: #E0705F;
  --focus: #ECE9E1;
}
```

Spacing scale (px): 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
Type scale (px): 12, 14, 16, 18, 21, 24, 32, 40, 56. Body 16. Line height 1.5 body, 1.15 to 1.25 headings.
Max line length: 66ch for prose.
Borders: 1px solid `var(--rule)`. Depth comes from borders, tonal steps between `--paper`, `--paper-2`, `--paper-3`, and spacing. Never from shadows.
Focus: `outline: 2px solid var(--focus); outline-offset: 2px;`
Motion: 0ms to 150ms, `ease-out`, opacity and transform only, and nothing at all under `prefers-reduced-motion: reduce`.
Icons: one SVG icon set (stroke 1.5px, 16 or 20px), never emoji.

## Example block conventions

Bad example:

```slop
<div class="rounded-2xl shadow-xl bg-gradient-to-r from-indigo-500 to-purple-600 p-8">
  <span>Unlock seamless productivity</span>
</div>
```

Good example (normal language tag, must pass the code rules):

```html
<section class="panel">
  <h2>Ship invoices in two clicks</h2>
</section>
```
