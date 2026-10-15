### 3.3 Text details

#### Alignment

Paragraphs are left-aligned (`text-align: start`, which flips correctly for right-to-left languages). The left edge is where the eye returns after every line; a ragged left edge makes every return a search.

Centered text is allowed in exactly these places:

- A single line of two to eight words that stands alone: an empty-state title, a short confirmation message in a narrow dialog, a figure caption under a centered image.
- Labels inside buttons, tabs and badges.
- Numbers in a cell when the column is a short status or icon column.

Centered text is not allowed for paragraphs, for lists, for anything over two lines, or for section headings that sit above left-aligned content. The centered landing page (centered eyebrow, centered h1, centered 20px gray paragraph, two centered buttons, centered logo row) is the most common generated layout on the web, and it comes straight from the Tailwind UI and shadcn hero blocks. Chapter 3.5 covers the layout fix; the text fix is to put the headline and the paragraph on the same left edge as everything below them.

```slop
<div class="mx-auto max-w-2xl text-center">
  <h2 class="text-3xl font-bold">Trusted by thousands</h2>
  <p class="mt-4 text-lg text-gray-600">Teams of every size rely on our platform to get more
  done every day, with features designed to help them collaborate and grow.</p>
</div>
```

Do not justify text on the web unless the column also hyphenates and is at least 50ch wide. Browser justification works line by line, not paragraph by paragraph, so without hyphenation it opens gaps between words ("rivers") that are worse than a ragged right edge.

#### Widows, orphans and balanced lines

A single short word alone on the last line of a heading looks like a mistake. Two CSS properties fix most cases:

```css
h1, h2, h3, h4, .card-title, figcaption { text-wrap: balance; }
p, li, dd { text-wrap: pretty; }
```

- `text-wrap: balance` spreads a heading across lines of similar length. Chromium limits balancing to blocks of six lines or fewer, which covers every heading you should write. Supported in Chromium, Firefox and Safari.
- `text-wrap: pretty` lets the browser spend more effort on paragraph endings, mainly to avoid a one-word last line. Supported in Chromium and recent Safari; elsewhere it falls back to normal wrapping, which is harmless.

For short strings where a specific pair must stay together, use a non-breaking space (`&nbsp;`, U+00A0):

- Between a number and its unit: `16&nbsp;GB`, `30&nbsp;min`, `4.2&nbsp;MB`.
- Between a title and a name, an initial and a surname: `Dr.&nbsp;Okafor`.
- Between the last two words of a button label that wraps in a narrow layout.

Do not paste `&nbsp;` into every paragraph to fight widows by hand. Rewriting a sentence is cheaper than maintaining manual breaks across breakpoints.

#### Hyphenation and overflow

Turn on hyphenation for narrow columns of prose: sidebars, multi-column text under 40ch, mobile layouts of long-form articles. It requires a correct `lang` attribute, because the browser uses the language's dictionary.

```html
<html lang="en">
```

```css
.prose { hyphens: manual; }
@media (max-width: 30em) {
  .prose p { hyphens: auto; hyphenate-limit-chars: 7 3 3; }
}
h1, h2, h3, h4, a, code, .no-hyphens { hyphens: manual; }
```

`hyphenate-limit-chars: 7 3 3` means only words of seven or more letters are hyphenated, with at least three letters before and after the break. Without it, the browser can split "into" as "in-to".

Never hyphenate headings, links or code. For strings that cannot break naturally (URLs, hashes, email addresses, file paths), allow breaks anywhere instead of letting them overflow the container:

```css
.prose a, .prose code, td, .breakable { overflow-wrap: anywhere; }
```

Avoid `word-break: break-all` on body text; it breaks ordinary words at arbitrary letters even when a normal break exists. `overflow-wrap: anywhere` only breaks inside a word when the word would otherwise overflow.

#### Quotes and apostrophes

Use typographic quotes in all interface copy and prose:

| Character | Name | Code point | Use |
| --- | --- | --- | --- |
| ’ | right single quote | U+2019 | apostrophes: don’t, it’s, the ’90s |
| ‘ ’ | single quotes | U+2018, U+2019 | quotes inside quotes |
| “ ” | double quotes | U+201C, U+201D | quotations |
| ′ ″ | prime, double prime | U+2032, U+2033 | feet and inches, minutes and seconds of arc |

Straight quotes (`'` and `"`) belong only in code, in values the user will type or paste, and in monospace UI such as a terminal. Write them directly in source as UTF-8; do not rely on a Markdown processor to curl them, because it gets apostrophes before numerals and after closing tags wrong.

For quotations rendered with `<q>`, let CSS supply the marks per language:

```css
q { quotes: "\201C" "\201D" "\2018" "\2019"; }
:lang(fr) q { quotes: "\00AB\00A0" "\00A0\00BB"; }
:lang(de) q { quotes: "\201E" "\201C" "\201A" "\2018"; }
```

`hanging-punctuation: first` pulls an opening quote mark into the margin so the letters align with the paragraph edge. Only Safari supports it; set it anyway, it degrades to normal setting.

#### Ellipsis

Use the single ellipsis character (…, U+2026), not three periods. In UI it has two jobs:

- **A continuing state**: `Saving…`, `Uploading 3 of 12…`, `Connecting…`. The action is in progress.
- **An action that needs more input before it runs**: a menu item `Rename…` or `Export as…` opens a dialog. A menu item without the ellipsis acts immediately. This is the macOS and Windows convention, and power users rely on it.

Do not use an ellipsis for drama in headings or marketing copy ("And then… everything changed"). Do not end a button label that runs immediately with one.

Truncation uses CSS, and the full text must stay reachable:

```css
.truncate {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  min-width: 0;            /* required inside flex and grid items */
}
.clamp-2 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  overflow: hidden;
}
```

```html
<td class="truncate" title="Q3 2026 vendor reconciliation, EMEA, final.xlsx">
  Q3 2026 vendor reconciliation, EMEA, final.xlsx
</td>
```

The `title` attribute is a weak fallback (no touch access, no keyboard access). Where truncated text matters, link to the full record or expand on click. Truncate from the middle for file names and paths, where the end carries the meaning: `invoice-2026-…-final.pdf`. That needs JavaScript or server-side shortening; CSS only truncates the end.

#### Numbers, units and math signs

- Thousands separators via `Intl.NumberFormat`, never hand-built strings. `12,480` in en-US, `12.480` in de-DE, `12 480` in fr-FR (a narrow no-break space).
- A non-breaking space between number and unit: `250&nbsp;ms`, `16&nbsp;GB`, `3&nbsp;users`. Percent attaches in English (`12%`) and takes a space in French and German.
- A true minus sign (−, U+2212) for negative numbers in tables and financial figures. The hyphen is shorter and sits lower. `Intl.NumberFormat` outputs a hyphen-minus in most locales; replace it where alignment matters.
- The multiplication sign (×, U+00D7) for dimensions: `1920 × 1080`, `2×` zoom.
- Ranges: write `10 to 20` in prose. In tables and compact UI, `10-20` with a plain hyphen. This handbook does not use the en dash glyph.
- Same precision down a column, same unit down a column, unit in the column header when every row shares it: `Size (MB)` heading, bare numbers in cells.
- Abbreviate large numbers only where space forces it, and keep one decimal: `1.2k`, `48.6M`. Use the compact formatter so the suffix is localized.

```ts
const money = new Intl.NumberFormat("en-US", { style: "currency", currency: "EUR" });
money.format(-1234.5);         // "-€1,234.50"

const compact = new Intl.NumberFormat("en", { notation: "compact", maximumFractionDigits: 1 });
compact.format(48_620_000);    // "48.6M"

const pct = new Intl.NumberFormat("en", { style: "percent", maximumFractionDigits: 1 });
pct.format(0.1234);            // "12.3%"

// Replace hyphen-minus with U+2212 for tabular display
export const tableNumber = (s: string) => s.replace(/^-/, "−");
```

#### Dates and times

- Use an unambiguous human format: `14 Mar 2026` or `Mar 14, 2026`, matching the locale. Never `03/04/2026`, which is March 4 in the US and 3 April almost everywhere else.
- Wrap every date in `<time datetime>` with the ISO 8601 value. It gives screen readers, scrapers and translation tools the exact value.
- Relative times (`5 min ago`, `yesterday`) for events in the last 7 days in feeds and activity logs. Switch to the absolute date after that. Always expose the absolute timestamp on hover and focus.
- Show the time zone whenever two people might read the same time differently: scheduled jobs, deadlines, meeting times. `09:00 CET`, or the reader's own zone with the abbreviation.
- 24-hour or 12-hour follows the locale; let `Intl.DateTimeFormat` decide.
- Durations in tabular numerals: `02:14:09` for a running timer, `2 h 14 min` for a static value.

```tsx
const rtf = new Intl.RelativeTimeFormat("en", { numeric: "auto" });
const abs = new Intl.DateTimeFormat("en-GB", { dateStyle: "medium", timeStyle: "short" });

export function When({ iso }: { iso: string }) {
  const d = new Date(iso);
  const mins = Math.round((d.getTime() - Date.now()) / 60000);
  const label =
    Math.abs(mins) < 60 ? rtf.format(mins, "minute")
    : Math.abs(mins) < 1440 ? rtf.format(Math.round(mins / 60), "hour")
    : Math.abs(mins) < 10080 ? rtf.format(Math.round(mins / 1440), "day")
    : abs.format(d);
  return <time dateTime={iso} title={abs.format(d)}>{label}</time>;
}
```

#### Links

Links in running text are underlined. Color alone does not identify a link for readers with color vision deficiency, and WCAG 1.4.1 requires a non-color cue. The underline is the cue that everyone already knows.

```css
a {
  color: inherit;
  text-decoration-line: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.2em;
  text-decoration-color: var(--ink-3);
}
a:hover { text-decoration-thickness: 2px; text-decoration-color: currentColor; }
a:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; text-decoration: none; }
.prose a:visited { text-decoration-color: var(--ink-2); }

/* Links inside nav, tabs and button groups: position already says "clickable" */
nav a, .tabs a, a.button { text-decoration: none; }
```

Rules:

- Link text says where it goes. "Read the billing docs", not "click here" or "learn more". Screen reader users jump through a list of links out of context.
- One link per destination per paragraph.
- Do not open links in a new tab by default. If you must (a help link inside a half-filled form), say so in the text: `Billing docs (opens in new tab)`.
- Do not use the accent color plus no underline plus a hover underline. It fails 1.4.1 unless the link color has 3:1 contrast against the surrounding text, and the canonical accent does not reach that against `--ink`.
- External link icons are optional; if you use one, use the icon set's arrow-up-right at 12px, `aria-hidden`, after the text.

#### No text gradients

Text filled with a gradient (`bg-clip-text text-transparent bg-gradient-to-r`) is banned. It is the single most recognizable mark of a generated hero, and it also fails in practice:

- Contrast cannot be checked: part of every letter sits on a light stop and part on a dark one, and automated checkers report a pass or fail at random.
- Selection highlights render oddly, because the text color is transparent.
- The text disappears when the background image fails to paint: in some print modes, in reader views and in email clients that strip backgrounds.

Use `--ink` for headings. If a single headline must carry the brand color, set the whole heading in `--accent`, check that it reaches 4.5:1 (the canonical accent is 5.1:1 on `--paper`), and do it once in the product.

```slop
<span class="bg-gradient-to-r from-blue-600 to-violet-600 bg-clip-text text-transparent">AI-powered</span>
```

#### Lists and bullets

Lists use real list markup and plain markers. Emoji bullets (a rocket, a lightning bolt, a check mark emoji at the start of each line) are banned, as are the check-mark lines in pricing tables rendered as emoji.

```slop
- :rocket: Blazing fast builds
- :zap: Lightning deploys
- :lock: Enterprise-grade security
- :sparkles: AI-powered insights
```

Each marker is an OS emoji glyph that renders differently on Apple, Google and Microsoft systems, ignores your color tokens, is read aloud by screen readers (the listener hears "rocket" before the feature name), and repeats what the words say.

```css
.prose ul { list-style: disc; padding-inline-start: 1.25em; }
.prose ul ::marker { color: var(--ink-3); }
.prose ol { list-style: decimal; padding-inline-start: 1.5em; }
.prose ol ::marker { font-variant-numeric: tabular-nums; color: var(--ink-2); }
.prose li + li { margin-top: 8px; }

/* A dash marker, if the brand wants something quieter than a disc */
.dash-list { list-style-type: "-  "; }
```

For a feature list where each row has a yes or no, use a table with an SVG check icon plus visually hidden text (see 3.7), not a column of emoji.

#### Case

- Sentence case for headings, buttons, menu items, tab labels and table headers: `Create invoice`, `Billing settings`. Title Case (`Get Started Today`, `Unlock Your Potential`) is a marketing-template tell and slows reading.
- Proper nouns and product names keep their own capitalization.
- No all-caps headings (see uppercase label rules in 3.2).

### 3.4 Spacing system

#### The canonical scale

Ten values, in pixels: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Every margin, padding and gap is one of them. No 5, 6, 10, 14, 18, 20, 40, 56, 80.

```css
:root {
  --space-4: 4px;
  --space-8: 8px;
  --space-12: 12px;
  --space-16: 16px;
  --space-24: 24px;
  --space-32: 32px;
  --space-48: 48px;
  --space-64: 64px;
  --space-96: 96px;
  --space-128: 128px;
}
```

Naming the tokens by their pixel value means a reviewer reads `--space-24` and knows the number. Abstract names (`--space-md`, `--space-lg`) hide the value and invite arguments about what "medium" means.

Tailwind's default spacing scale already contains these values. Use only the matching keys and remove the rest from the theme so stray values fail the build:

| Canonical px | Tailwind key | Example |
| --- | --- | --- |
| 4 | 1 | `gap-1` |
| 8 | 2 | `p-2` |
| 12 | 3 | `px-3` |
| 16 | 4 | `p-4` |
| 24 | 6 | `gap-6` |
| 32 | 8 | `mt-8` |
| 48 | 12 | `py-12` |
| 64 | 16 | `mt-16` |
| 96 | 24 | `py-24` (only where 3.4 says so) |
| 128 | 32 | `mt-32` |

```js
// tailwind.config.js (v3): replace spacing so p-5, gap-7, mt-10 stop existing
module.exports = {
  theme: {
    spacing: {
      0: "0", px: "1px",
      1: "4px", 2: "8px", 3: "12px", 4: "16px", 6: "24px",
      8: "32px", 12: "48px", 16: "64px", 24: "96px", 32: "128px",
    },
  },
};
```

Arbitrary values (`p-[13px]`, `mt-[72px]`) are banned in review. Each one is a decision that did not get made.

#### Inner space is smaller than outer space

Spacing is how a reader groups things. Elements that belong together sit closer than elements that do not. This is the proximity rule, and every layout decision in this chapter derives from it.

A working ladder:

| Relationship | Space |
| --- | --- |
| Icon to its label, label to its value inline | 4 to 8 |
| Form label to its input; heading to its first paragraph | 8 |
| Paragraph to paragraph; list item to list item in UI | 12 to 16 |
| Field to field in a form; card padding | 16 to 24 |
| Group of fields to the next group; subsection to subsection | 32 to 48 |
| Section to section within a page | 48 to 96 |
| Major topic change on a long page; hero to first section | 96 to 128 |

Check every screen against this ladder. The most common failure is equal space everywhere: a form where the label sits 16px above its input and the next label sits 16px below the input, so labels float halfway between two fields. Halve the label gap and double the field gap.

```css
.field { display: grid; gap: var(--space-8); }
.form  { display: grid; gap: var(--space-24); }
.form fieldset + fieldset { margin-top: var(--space-48); }
```

#### Spacing as the main grouping tool

Generated interfaces group with containers: a card with a border, a radius and a shadow around every block, then a card inside the card. Space does the same work with less ink. Reach for space first, a 1px rule second, a tonal surface (`--paper-2`) third, and a bordered panel only when the group must look movable, selectable or separate from the page.

```slop
<div class="rounded-2xl bg-white p-8 shadow-lg">
  <div class="rounded-xl border p-6 shadow-sm">
    <h3 class="text-lg font-semibold">Notifications</h3>
    <div class="mt-4 rounded-lg bg-gray-50 p-4">
      <div class="rounded-md border bg-white p-3">Email me when an invoice is paid</div>
    </div>
  </div>
</div>
```

Four nested surfaces for one checkbox. Each wrapper adds padding, so the actual control ends up 76px from the page edge.

```html
<section class="settings-group" aria-labelledby="notif-h">
  <h2 id="notif-h">Notifications</h2>
  <p class="help">Sent to finance@acme.example</p>
  <label class="check"><input type="checkbox" checked> Email me when an invoice is paid</label>
  <label class="check"><input type="checkbox"> Email me when a payment fails</label>
</section>
```

```css
.settings-group { display: grid; gap: var(--space-12); padding-block: var(--space-32); border-top: 1px solid var(--rule); }
.settings-group h2 { font-size: var(--text-18); line-height: var(--lh-18); }
.settings-group .help { color: var(--ink-2); font-size: var(--text-14); margin-top: calc(var(--space-8) * -1); }
```

One rule separates the groups; space separates everything inside them.

#### Vertical rhythm

Line heights from 3.2 are all multiples of 4px. Keep margins on the same 4px grid and the page aligns without a baseline grid tool.

Headings get more space above than below, about two to one, so each heading visibly belongs to the text that follows it:

```css
.prose > * + * { margin-top: var(--space-16); }
.prose > h2 { margin-top: var(--space-48); }
.prose > h3 { margin-top: var(--space-32); }
.prose > h2 + *, .prose > h3 + * { margin-top: var(--space-12); }
.prose > :where(pre, table, figure) { margin-block: var(--space-24); }
```

The `* + *` selector (the "flow" or "owl" pattern) sets space between siblings only, so the first and last children never add stray space at the edges of the container. Use it instead of `mb-4` on every element, which leaves a trailing margin inside every box.

For component layouts, prefer `gap` on a flex or grid parent over margins on children. `gap` never collapses, never leaks out of the container, and moves with reordering.

#### Section spacing on marketing pages

`py-24 sm:py-32` is the vertical padding on nearly every section block in Tailwind UI, and generated pages apply it to every section regardless of content. The page becomes a stack of equal slabs with 96px to 128px of air between each, and the rhythm says "these sections are unrelated and equally important", which is almost never true.

Vary section spacing by relationship:

- 128px after the hero, before the first content section.
- 48 to 64px between sections that continue the same topic (a feature and its detail, a pricing table and its FAQ).
- 96px at a real change of topic.
- A 1px `--rule` line with 48px on either side works better than 128px of empty space when the sections are dense.
- The last section before the footer gets 96px, the footer itself 48px of padding.

Do not alternate full-bleed background colors (`bg-white`, `bg-gray-50`, `bg-white`) on every other section to separate them. That pattern exists because equal padding failed to group anything. Change background only for a section that really is different: a code sample panel on `--paper-2`, the footer.

```css
.page > section { padding-block: var(--space-64); }
.page > .hero { padding-block: var(--space-96) var(--space-128); }
.page > section.continues { padding-top: var(--space-24); }
.page > section.new-topic { padding-top: var(--space-96); border-top: 1px solid var(--rule); }
```

#### Density

Pick a density per product and per surface, then set it with tokens, not with one-off padding.

| Density | Row height | Text | Cell padding | Use |
| --- | --- | --- | --- | --- |
| Compact | 32px | 14px | 4px 8px | Trading, logs, spreadsheets, admin tables with 50+ rows |
| Default | 40px | 14 to 16px | 8px 12px | Most app screens, settings, lists |
| Comfortable | 48px | 16px | 12px 16px | Touch-first apps, consumer forms, onboarding |

A tool people use for hours is a compact-to-default product. Generated dashboards ship comfortable density everywhere (`p-6` cards, `py-4` table cells, 64px rows) because the template was designed for a screenshot, not for a person scanning 400 rows. Fewer rows on screen means more scrolling and less comparison.

```css
:root {
  --row-h: 40px;
  --cell-py: var(--space-8);
  --cell-px: var(--space-12);
}
[data-density="compact"] {
  --row-h: 32px;
  --cell-py: var(--space-4);
  --cell-px: var(--space-8);
}
[data-density="comfortable"] {
  --row-h: 48px;
  --cell-py: var(--space-12);
  --cell-px: var(--space-16);
}
@media (pointer: coarse) {
  :root:not([data-density="compact"]) { --row-h: 48px; }
}

td, th { padding: var(--cell-py) var(--cell-px); height: var(--row-h); }
```

Let the reader switch density in data-heavy products, and remember the choice.

#### Padding inside controls

- Buttons: 8px vertical by 16px horizontal at 16px text gives a 40px button; 12px by 16px for 48px touch. When the button has a leading icon, reduce the padding on the icon side to 12px so the icon and text look centered as a unit.
- Inputs: same height as buttons in the same row. A 40px input next to a 36px button is the most common misalignment in generated forms.
- Badges: 0 by 8px at 12px text, 20px tall.
- Cards: 16px or 24px padding. 32px padding around a single line of text wastes space and reads as template.

#### Failure cases

```slop
<div class="space-y-8">
  <div class="mb-6 mt-10 px-7 py-5">...</div>
  <div class="mt-[18px] p-[22px]">...</div>
</div>
```

Off-scale values everywhere, margins on children fighting `space-y` on the parent. Every value is a guess.

### 3.5 Layout and grid

#### The two generated layouts

Almost every generated landing page and dashboard is built from two layouts.

**The centered stack.** Every block is centered in a `max-w-7xl mx-auto` container, and inside it, every heading and paragraph is centered too:

```slop
[ centered pill: "New: AI features" ]
[ centered h1, 72px, gradient ]
[ centered gray paragraph, max-w-2xl ]
[ two centered buttons: "Get started" (indigo) + "Learn more ->" (ghost) ]
[ centered row of six grayscale logos: "Trusted by teams at" ]
[ centered eyebrow + h2 + paragraph ]
[ three equal cards ]
[ centered testimonial with avatar ]
[ centered CTA panel with gradient ]
```

The eye has no edge to follow, every block has the same weight, and the reader scrolls past a column of headlines without a reason to stop.

**The three equal cards.** `grid grid-cols-1 md:grid-cols-3 gap-8`, each card with an icon in a colored square, a bold title and two lines of gray text. Real features are rarely three and rarely equal. The grid forces the copy to fit the shape: three benefits padded to equal length, or six squeezed into two rows of three.

The fix for both is the same: decide what the most important item is, give it more space, and align everything to one left edge.

#### Alignment to a shared left edge

Pick one left edge per page, or per column, and start everything there: the logo, the h1, the paragraph, the primary button, the screenshot, the section headings, the table. When a reader's eye drops from the headline, it lands on the start of the next line without searching.

```css
.page {
  --edge: max(var(--space-16), (100vw - 1200px) / 2);
  padding-inline: var(--edge);
}
```

Concrete checks:

- Draw a vertical line at the left edge of the h1. The paragraph, the buttons and the next section heading touch it.
- Icons in lists and nav hang outside the text edge, or the text column starts after the icon column consistently. Do not mix the two.
- Card text does not start 32px in from the page edge when the surrounding text starts at 0. Either the card border sits on the edge and the padding is visible as a deliberate inset, or there is no card.

#### Asymmetric grids

Split layouts unevenly. An uneven split states which side matters.

| Split (of 12) | Use |
| --- | --- |
| 4 / 8 | Section label and summary on the left, content on the right (docs, settings, feature detail) |
| 5 / 7 | Text and a screenshot, text side smaller |
| 3 / 9 | Sidebar nav and main content |
| 8 / 4 | Article and a narrow aside (metadata, table of contents) |
| 6 / 6 | Only for two things that are equivalent: before and after, two plans |

```css
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  column-gap: var(--space-24);
  row-gap: var(--space-48);
}
@media (min-width: 64em) { .grid-12 { column-gap: var(--space-32); } }

.span-4 { grid-column: span 4; }
.span-5 { grid-column: span 5; }
.span-7 { grid-column: span 7; }
.span-8 { grid-column: span 8; }

@media (max-width: 47.99em) {
  .grid-12 > * { grid-column: 1 / -1; }
}
```

Use `minmax(0, 1fr)`, not `1fr`. A plain `1fr` track has a minimum of `auto`, which is the min-content width of its contents, so one long URL or code line makes its column wider than its siblings and pushes the page into horizontal scroll.

A feature section rebuilt with a 4 / 8 split, replacing the three cards:

```html
<section class="grid-12 feature">
  <div class="span-4">
    <h2>Reconciliation</h2>
    <p>Matches bank lines to invoices every morning at 06:00 in your time zone.</p>
  </div>
  <dl class="span-8 facts">
    <div><dt>Match rate</dt><dd>94% of lines match without review in the first month</dd></div>
    <div><dt>Rules</dt><dd>Match on amount, reference, IBAN or a regex you write</dd></div>
    <div><dt>Exceptions</dt><dd>Unmatched lines land in a queue with the three closest invoices</dd></div>
    <div><dt>Banks</dt><dd>2,400 banks through Open Banking; CSV and CAMT.053 for the rest</dd></div>
  </dl>
</section>
```

```css
.feature h2 { font-size: var(--text-24); line-height: var(--lh-24); }
.facts { display: grid; gap: 0; }
.facts > div {
  display: grid;
  grid-template-columns: 160px minmax(0, 1fr);
  gap: var(--space-16);
  padding-block: var(--space-16);
  border-top: 1px solid var(--rule);
}
.facts dt { font-weight: 600; }
.facts dd { color: var(--ink-2); }
```

Four facts instead of three, uneven lengths allowed, numbers where the template had adjectives.

Other replacements for the three-card row:

- **One large, two small.** The main feature spans 8 columns with a real screenshot; two secondary features stack in the remaining 4.
- **A comparison table.** If the features differ along the same dimensions, a table is clearer than cards.
- **An annotated screenshot.** One product image with three to five numbered callouts and a list below.
- **A plain list.** Headings at 21px with one paragraph each, in a single 66ch column. Unglamorous and fast to read.

#### Content-out layout with named lines

For pages that mix prose with wider elements (docs, articles, changelogs), define the columns once with named grid lines and let each child choose its width. This replaces nested `max-w-*` containers.

```css
.content-grid {
  --gutter: var(--space-16);
  --prose: 66ch;
  --wide: 960px;
  display: grid;
  grid-template-columns:
    [full-start] minmax(var(--gutter), 1fr)
    [wide-start] minmax(0, calc((var(--wide) - var(--prose)) / 2))
    [content-start] min(var(--prose), 100% - var(--gutter) * 2)
    [content-end] minmax(0, calc((var(--wide) - var(--prose)) / 2))
    [wide-end] minmax(var(--gutter), 1fr)
    [full-end];
}
.content-grid > * { grid-column: content; }
.content-grid > .wide { grid-column: wide; }
.content-grid > .full { grid-column: full; }
```

```html
<article class="content-grid">
  <h1>Migrating from v2 to v3</h1>
  <p>Version 3 changes how webhooks are signed. Plan for about 30 minutes per service.</p>
  <pre class="wide"><code>...</code></pre>
  <figure class="full"><img src="/img/v3-dashboard.png" alt="..." width="2400" height="1350"></figure>
  <p>Next, rotate the signing secret.</p>
</article>
```

Prose stays at 66ch; code blocks and tables break out to 960px; screenshots can go edge to edge. Everything shares the same left edge for its width class, and no element needs its own container.

#### Sidebars

Application shells use a fixed-width sidebar and a fluid main area:

```css
.shell {
  display: grid;
  grid-template-columns: 248px minmax(0, 1fr);
  min-height: 100dvh;
}
.shell > nav {
  position: sticky;
  top: 0;
  height: 100dvh;
  overflow-y: auto;
  border-right: 1px solid var(--rule);
  background: var(--paper-2);
  padding: var(--space-16) var(--space-12);
}
.shell > main { padding: var(--space-24) var(--space-32); }

@media (max-width: 63.99em) {
  .shell { grid-template-columns: minmax(0, 1fr); }
  .shell > nav { position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--rule); }
}
```

- Sidebar width 240 to 280px. Narrower truncates labels; wider steals table columns.
- The sidebar is separated by a 1px rule and a tonal step to `--paper-2`, never by a shadow.
- A collapsible icon-only rail (56px) is fine for products with ten or more destinations used all day. For fewer, keep labels visible.

For a sidebar that sits beside content only when there is room, without a media query, use the intrinsic pattern:

```css
.with-sidebar { display: flex; flex-wrap: wrap; gap: var(--space-32); }
.with-sidebar > .side { flex-basis: 240px; flex-grow: 1; }
.with-sidebar > .main { flex-basis: 0; flex-grow: 999; min-inline-size: 60%; }
```

When the main area would drop below 60 percent of the container, the sidebar wraps above it.

#### Max widths

| Content | Max width |
| --- | --- |
| Prose paragraphs | 66ch |
| Headings | 20 to 24ch |
| Forms (single column) | 480 to 560px |
| Dialogs | 480px for confirmations, 640px for forms |
| Marketing page container | 1200 to 1280px |
| Docs page with sidebar and table of contents | 1440px |
| Data tables, dashboards, editors | none: use the window |

`max-w-7xl mx-auto` (1280px) around a data table on a 2560px monitor leaves half the screen blank while the table truncates its columns. Application screens fill the viewport; only their text blocks get a measure.

#### CSS grid recipes

A responsive card grid that never produces a lonely half-width card and never needs a breakpoint:

```css
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(280px, 100%), 1fr));
  gap: var(--space-24);
}
```

`auto-fill` keeps empty tracks so a row of two cards on a wide screen stays card-sized; `auto-fit` collapses empty tracks and stretches two cards across the row. Use `auto-fill` for collections of items, `auto-fit` only when the items should fill the row.

Aligned internals across cards with subgrid, so titles, bodies and footers line up row by row even when text lengths differ:

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(280px, 100%), 1fr));
  gap: var(--space-24);
}
.card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid;
  row-gap: var(--space-8);
  padding: var(--space-16);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
}
```

Label and value rows aligned on their text baselines (the label is 12px, the value 16px; centering them makes the label float):

```css
.stat-row { display: flex; align-items: baseline; gap: var(--space-8); }
.stat-row .value { font-size: var(--text-24); line-height: var(--lh-24); font-variant-numeric: tabular-nums; }
.stat-row .label { font-size: var(--text-12); color: var(--ink-3); }
```

A page frame with header, main and footer where the footer stays at the bottom on short pages:

```css
body { min-height: 100dvh; display: grid; grid-template-rows: auto 1fr auto; }
```

#### Container queries

A component should respond to the space it is given, not to the window. A table cell, a sidebar and a main column can all hold the same component at different widths.

```css
.invoice-summary { container-type: inline-size; container-name: summary; }

.invoice-summary .body { display: grid; gap: var(--space-12); }

@container summary (min-width: 480px) {
  .invoice-summary .body { grid-template-columns: minmax(0, 1fr) auto; align-items: baseline; }
}
@container summary (min-width: 720px) {
  .invoice-summary .body { grid-template-columns: 200px minmax(0, 1fr) auto; }
}
```

- Put `container-type: inline-size` on a wrapper, not on the element you style; an element cannot query itself.
- Use container queries for components and media queries for page structure.
- Container query units (`cqi`) are available for sizes that scale with the container, but keep text on the type scale; do not set `font-size: 4cqi`.

#### Failure cases

```slop
<section class="mx-auto max-w-7xl px-6 py-24 text-center">
  <h2 class="text-4xl font-bold">Features</h2>
  <div class="mt-16 grid grid-cols-1 gap-8 md:grid-cols-3">
    <div class="rounded-2xl p-8 shadow-lg">...</div>
    <div class="rounded-2xl p-8 shadow-lg">...</div>
    <div class="rounded-2xl p-8 shadow-lg">...</div>
  </div>
</section>
```

```slop
<main class="mx-auto max-w-7xl">
  <div class="grid grid-cols-4 gap-6">
    <!-- four KPI cards, each with a big number, a green "+12.5%" pill and a sparkline -->
  </div>
</main>
```

The second is the generated dashboard: four equal KPI cards across the top whether the product has four important numbers or one. Put the one number that drives decisions at the left with more space, and move the rest into a compact row or a table.
