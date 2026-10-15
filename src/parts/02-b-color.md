#### Eight complete palettes

Each palette below is a full token set: three surfaces, a rule, three inks, one accent, text on accent, and three status colors. None is led by blue or purple. Every ratio was measured. Copy a palette whole; do not mix steps from two palettes, because the L values were matched across each set.

The tables give the ratio against `--paper` first and `--paper-2` second.

##### 1. Ledger (the canonical set)

Warm cream paper, warm near-black ink, burnt orange accent at OKLCH hue 39. For finance tools, editorial products, documentation, anything read for a long time.

```css
:root {
  --paper: #F7F5F0;  --paper-2: #EFECE4;  --paper-3: #E5E1D6;  --rule: #D9D5CB;
  --ink: #1A1A18;    --ink-2: #4A4843;    --ink-3: #6F6C64;
  --accent: #B4441C; --accent-ink: #FFFFFF;
  --ok: #2F6B3A;     --warn: #8A6100;     --bad: #A3271F;
}
```

| Pair | Ratio |
|---|---|
| `--ink` | 16.00 / 14.76 |
| `--ink-3` | 4.81 / 4.44 |
| `--accent` as text | 5.09 / 4.70 |
| `--accent-ink` on `--accent` | 5.55 |

Rule specific to Ledger: `--ink-3` is never placed on `--paper-2`.

##### 2. Newsprint

Near-neutral cool paper (hue 250 at chroma 0.003, far below the 0.012 limit, so it reads as gray), black ink, signal red accent at hue 30.

```css
:root {
  --paper: #F4F5F7;  --paper-2: #EBECEE;  --paper-3: #E0E1E3;  --rule: #D4D5D7;
  --ink: #181A1B;    --ink-2: #464849;    --ink-3: #696A6C;
  --accent: #CA3324; --accent-ink: #FFFFFF;
  --ok: #2F6B3A;     --warn: #8A6100;     --bad: #901F1A;
}
```

| Pair | Ratio |
|---|---|
| `--ink` | 16.01 / 14.77 |
| `--ink-3` | 4.96 / 4.58 |
| `--accent` as text | 4.80 / 4.43 |
| `--accent-ink` on `--accent` | 5.24 |
| `--bad` | 8.03 / 7.41 |

A red accent creates a specific failure: every red primary button reads as "Delete". Newsprint solves it by role. Red is for the masthead rule, links, the current navigation item and highlighted figures. Primary buttons are `--ink` filled with `--paper` text (16.01:1). `--bad` is pushed darker (L 0.43) and always carries an icon and a word, so a destructive action never looks like the brand color. Red links fail on `--paper-2` (4.43:1), so links inside recessed panels use `--ink` with an underline.

##### 3. Spruce

Green-gray paper at hue 177 to 184, teal-green accent at hue 175. For health, logistics, field operations, anything that wants calm without blue.

```css
:root {
  --paper: #F0F7F5;  --paper-2: #E4EFEC;  --paper-3: #D7E5E2;  --rule: #CBD9D5;
  --ink: #171A19;    --ink-2: #424A48;    --ink-3: #626D6B;
  --accent: #196958; --accent-ink: #FFFFFF;
  --ok: #416B25;     --warn: #8A6100;     --bad: #A3271F;
}
```

| Pair | Ratio |
|---|---|
| `--ink` | 16.13 / 14.90 |
| `--ink-3` | 4.93 / 4.56 |
| `--accent` as text | 6.03 / 5.58 |
| `--accent-ink` on `--accent` | 6.56 |

The accent is green, so `--ok` moves from hue 148 to 135 (`#416B25`, a yellow-green) to separate it from the brand, and `--ok` text always sits next to a check icon. If the product shows many success states, pick a different palette: green accent plus green success is a weak pairing however carefully the hues are split.

##### 4. Lichen

Yellow-gray paper at hue 110, olive accent at hue 120. For agriculture, outdoor, archives, print-adjacent products.

```css
:root {
  --paper: #F5F6ED;  --paper-2: #ECEDE0;  --paper-3: #E2E3D1;  --rule: #D6D7C5;
  --ink: #1A1A16;    --ink-2: #48493F;    --ink-3: #6B6C5D;
  --accent: #566613; --accent-ink: #FFFFFF;
  --ok: #176A4E;     --warn: #8A6100;     --bad: #A3271F;
}
```

| Pair | Ratio |
|---|---|
| `--ink` | 16.03 / 14.76 |
| `--ink-3` | 4.91 / 4.52 |
| `--accent` as text | 5.83 / 5.37 |
| `--accent-ink` on `--accent` | 6.35 |

Olive only works at low lightness. Above L 0.55 it turns into a yellow-green that looks like a warning light. Keep the accent at L 0.48 and use it as a fill, not as small text on `--paper-3`. `--ok` moves to hue 165, a deep sea green, to keep it apart from the olive.

##### 5. Raspberry

Faintly pink paper at hue 17, raspberry accent at OKLCH hue 2 (HSL 336). For consumer products, publishing, food, anything that needs warmth without orange.

```css
:root {
  --paper: #FAF3F3;  --paper-2: #F4E9E9;  --paper-3: #ECDDDD;  --rule: #E0D1D1;
  --ink: #1C1918;    --ink-2: #4D4645;    --ink-3: #736767;
  --accent: #A02857; --accent-ink: #FFFFFF;
  --ok: #2F6B3A;     --warn: #8A6100;     --bad: #A14206;
}
```

| Pair | Ratio |
|---|---|
| `--ink` | 15.96 / 14.71 |
| `--ink-3` | 4.96 / 4.57 |
| `--accent` as text | 6.53 / 6.02 |
| `--accent-ink` on `--accent` | 7.15 |

The accent sits at hue 2, 40 degrees clear of fuchsia (322). Pushing it toward 340 or raising its lightness above 0.55 turns it into Tailwind `pink-500` (`#EC4899`, hue 354, L 0.656), which is the third stop of the default gradient. `--bad` rotates to hue 45 (`#A14206`, a rust) to stay distinct from the accent.

##### 6. Signal

Graphite neutrals and a yellow accent at hue 90 that is used only as a fill. For tools used in bright light, transit, construction, safety, kiosks.

```css
:root {
  --paper: #F6F5F2;  --paper-2: #EDECE8;  --paper-3: #E3E1DB;  --rule: #D7D5CF;
  --ink: #1A1918;    --ink-2: #484845;    --ink-3: #6B6A66;
  --accent: #F4C423;       /* fill only */
  --accent-ink: #1A1918;   /* text on the fill */
  --accent-text: #7E5D00;  /* when the accent must be text */
  --ok: #2F6B3A;     --warn: #A05000;     --bad: #A3271F;
}
```

| Pair | Ratio |
|---|---|
| `--ink` | 16.10 / 14.85 |
| `--ink-3` | 4.97 / 4.58 |
| `--accent` as text | 1.51 (fails, never used as text) |
| `--accent-ink` on `--accent` | 10.67 |
| `--accent-text` | 5.58 / 5.14 |

A bright accent needs a split token. `--accent` is the fill for the primary button and the selected tab underline; `--accent-text` is a dark gold for links and highlighted figures. The yellow button with ink text (10.67:1) is the most legible primary button in this list. A yellow fill alone is 1.51:1 against the paper, below the 3:1 boundary rule, so the yellow button carries a 1px `--ink` border. `--warn` moves to hue 54 (`#A05000`, a burnt amber) so it does not look like the brand.

##### 7. Mono

Zero-chroma neutrals and no chromatic accent at all. The accent is the ink. For developer tools, legal, reference, and any product where the only color on screen should be status.

```css
:root {
  --paper: #F5F5F5;  --paper-2: #ECECEC;  --paper-3: #E1E1E1;  --rule: #D5D5D5;
  --ink: #191919;    --ink-2: #484848;    --ink-3: #6A6A6A;
  --accent: #191919; --accent-ink: #F5F5F5;
  --ok: #2F6B3A;     --warn: #8A6100;     --bad: #A3271F;
}
a { color: var(--ink); text-decoration-line: underline; text-decoration-thickness: 1px; text-underline-offset: 3px; }
a:hover { text-decoration-thickness: 2px; }
```

| Pair | Ratio |
|---|---|
| `--ink` | 16.13 / 14.88 |
| `--ink-3` | 4.96 / 4.58 |
| `--accent-ink` on `--accent` | 16.13 |

In Mono, links are distinguished by underline, never by color, which satisfies WCAG 1.4.1 without effort. Status colors become the only hues on screen, so they read instantly. Mono is the safest palette for a team that keeps drifting back to indigo: there is no accent slot left to drift with.

##### 8. Ochre Night (dark-first)

For products used mostly at night or in dim rooms: monitoring, audio, broadcast, trading floors. Warm near-black at hue 67 to 81, ochre accent at hue 75. This is a primary dark palette, not a dark mode of a light one.

```css
:root {
  --paper: #141210;  --paper-2: #1E1B18;  --paper-3: #292622;  --rule: #33302B;
  --ink: #EDE7DF;    --ink-2: #B7B0A7;    --ink-3: #918B83;
  --accent: #E1A447; --accent-ink: #141210;
  --ok: #75B683;     --warn: #EB883B;     --bad: #E66F62;
}
```

| Pair | Ratio |
|---|---|
| `--ink` | 15.21 / 13.95 |
| `--ink-3` | 5.54 / 5.08 |
| `--accent` as text | 8.55 / 7.84 |
| `--accent-ink` on `--accent` | 8.55 |
| `--warn` | 7.22 / 6.63 |

On dark grounds, `--ink-3` keeps passing on `--paper-2`, which makes dark palettes more forgiving for tertiary text than light ones. The ochre accent and an amber warning would collide, so `--warn` moves to hue 55 (`#EB883B`, orange).

#### Using the canonical tokens

Components read role tokens. They never contain a hex value, a Tailwind palette class (`bg-orange-700`) or a raw `oklch()` call.

| Element | Background | Text | Border |
|---|---|---|---|
| Page | `--paper` | `--ink` | |
| Body copy | | `--ink` | |
| Metadata, captions | | `--ink-2`, or `--ink-3` on `--paper` only | |
| Sidebar, table header, code block | `--paper-2` | `--ink`, `--ink-2` | `--rule` on the shared edge |
| Selected row, pressed button | `--paper-3` | `--ink` | |
| Card, panel | `--paper` | `--ink` | `--rule` |
| Menu, popover, dialog | `--paper` | `--ink` | `--rule-strong` |
| Tooltip, toast | `--ink` | `--paper` | |
| Text input | `--paper` | `--ink` | `--ink-3` (3:1 rule) |
| Primary button | `--accent` | `--accent-ink` | `--accent` |
| Secondary button | `--paper` | `--ink` | `--ink` |
| Link | | `--accent`, underlined | |
| Focus | | | `outline: 2px solid var(--focus)` |

Derived tokens are computed from roles, so they change when the palette changes:

```css
:root {
  --accent-wash: color-mix(in oklab, var(--accent) 8%, var(--paper));
  --ok-wash:     color-mix(in oklab, var(--ok) 8%, var(--paper));
  --warn-wash:   color-mix(in oklab, var(--warn) 8%, var(--paper));
  --bad-wash:    color-mix(in oklab, var(--bad) 8%, var(--paper));
  --scrim:       color-mix(in srgb, var(--ink) 56%, transparent);
}
```

Mix in `oklab`, not `oklch`. The paper has a hue of its own (89 for Ledger) at almost no chroma, and `oklch` interpolation rotates the result's hue toward it. An 8% mix of `--bad` (hue 29) into `--paper` in `oklch` lands at hue 84, a beige with no red in it. The same mix in `oklab` gives `#F2E5DE`, a visible red wash. Write the hex fallback next to each derived token for browsers older than 2023, which lack `color-mix()`.

#### Review checklist for 2.3

- The neutral scale has a stated hue and a chroma under 0.012, with surface steps 0.025 to 0.035 apart in OKLCH L.
- There is exactly one accent, its OKLCH hue is outside 235 to 335, and it covers under 10% of any screen.
- Accent steps were derived in OKLCH with the hue held (or rotated toward orange, for yellows).
- Every text and surface pairing that ships was measured, including on `--paper-2` and `--paper-3`.
- Input, checkbox and select borders are at 3:1 or higher (`--ink-3` or darker), not `--rule`.
- No component contains a hex value or a Tailwind palette class.
- Bright accents are split into a fill token and a text token.

### 2.4 Semantic color

Semantic colors tell the reader the state of something: it worked, it needs attention, it failed. Use exactly three hues for this: `--ok`, `--warn`, `--bad`. A fourth "info" blue is not part of the system. Information is the default state of all text, so it gets the default color: `--ink`, with an info icon when it needs marking.

#### The four roles

| Role | Light | Dark | Icon shape | Word | Use for |
|---|---|---|---|---|---|
| ok | `#2F6B3A` | `#7FB38A` | Check in a circle | Done, Saved, Paid, Running | Completed actions, healthy systems |
| warn | `#8A6100` | `#D9A93A` | Triangle with a bar | Check, Expires, Low, Slow | States that will become failures if ignored |
| bad | `#A3271F` | `#E0705F` | Octagon or circle with a cross | Failed, Declined, Down, Missing | Failures, destructive actions, blocking errors |
| info | `--ink` | `--ink` | Circle with an "i" | Note, Tip | Neutral notices |

The info role costs nothing and removes the most common source of stray blue in generated interfaces: the `bg-blue-50 text-blue-700` info banner from Tailwind UI's alert component.

#### Never color alone

WCAG 1.4.1 forbids color as the only way to convey information. The reason is measurable. Under a simulation of deuteranopia (Machado 2009, full severity), the canonical `--ok` `#2F6B3A` becomes `#645D3D` and `--bad` `#A3271F` becomes `#6C6019`. Their perceptual distance (OKLab ΔE) drops from 22.8 to 4.2, about the same as two adjacent steps of a gray ramp. The two colors also share almost the same lightness (OKLCH L 0.475 and 0.473), so a grayscale print shows no difference at all. Default Tailwind `green-500` and `red-500` fare no better: their deuteranopia ΔE is 7.5.

So every status carries at least two of these three, and in practice all three:

1. A word. "Failed", not just a red row.
2. An icon with a distinct shape. A check, a triangle and an octagon differ in silhouette at 16px; three identical circles in different colors do not.
3. The color.

```html
<p class="status status-bad">
  <svg class="icon" aria-hidden="true" width="16" height="16"><use href="#i-octagon-x"/></svg>
  <span>Payment failed</span>
  <span class="status-detail">Card declined by issuer, code 05</span>
</p>
```

```css
.status {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin: 0;
  font: 500 14px/1.4 var(--font-sans);
}
.status .icon { flex: none; align-self: center; }
.status-ok   { color: var(--ok); }
.status-warn { color: var(--warn); }
.status-bad  { color: var(--bad); }
.status-detail { font-weight: 400; color: var(--ink-2); }
```

The detail line is `--ink-2`, not the status color. Color marks the state word; the explanation is plain text, which keeps long messages readable and keeps the colored area small.

#### Status without glowing dots

The green dot (`h-2 w-2 rounded-full bg-green-500`), often pulsing (`animate-pulse`), often beside an uppercase "LIVE" in a pill, is a dashboard kit default. It fails in five ways: an 8px circle of `green-500` has 2.28:1 contrast on white, below the 3:1 graphics floor; it says nothing without the label; the pulse is decoration that never stops; the pill and dot shapes are identical across states, so only hue separates them; and LIVE is vague about what is live and since when.

```slop
<span class="inline-flex items-center gap-1.5 rounded-full bg-green-50 px-2.5 py-0.5 text-xs font-medium text-green-700 ring-1 ring-green-600/20">
  <span class="h-1.5 w-1.5 animate-pulse rounded-full bg-green-500"></span>
  LIVE
</span>
```

Replace it with a specific statement:

```html
<p class="status status-ok">
  <svg class="icon" aria-hidden="true" width="16" height="16"><use href="#i-broadcast"/></svg>
  <span>Streaming</span>
  <span class="status-detail">since 18:02, 1,204 watching</span>
</p>
```

When a dense table needs a compact marker in every row, use a shape glyph (an SVG check, triangle or square at 12px) in the status color, followed by the word in `--ink`. Never animate it. A state change can be announced once with an `aria-live="polite"` region and a single 150ms opacity fade on the changed row, then nothing.

#### Badges and tags

A badge is a short label with a border, not a pill. Keep the 2px radius. Use the status color for the border and the text, with the wash behind it, or skip the wash.

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 6px;
  font: 600 12px/1.3 var(--font-sans);
  letter-spacing: 0.02em;
  border: 1px solid currentColor;
  border-radius: var(--radius);
  background: var(--paper);
}
.badge-ok   { color: var(--ok);   background: var(--ok-wash);   } /* #E6E9E0, text 5.20:1 */
.badge-warn { color: var(--warn); background: var(--warn-wash); } /* #EEE9DE, text 4.58:1 */
.badge-bad  { color: var(--bad);  background: var(--bad-wash);  } /* #F2E5DE, text 5.94:1 */
```

The wash stays at 8%. At 12%, the warn text drops to 4.34:1 and fails. In dark mode the same 8% mix is too faint to see; use 14%, which gives `#212720` for ok (text 6.34:1), `#2B261A` for warn (6.94:1) and `#2D201C` for bad (4.98:1).

Neutral tags (categories, labels, filters) do not use status colors. They are `--paper-2` with `--ink` text and no border, or `--paper` with a 1px `--rule` border.

#### Alerts and banners

The Tailwind UI alert is a tinted box with a 4px colored left border (`border-l-4 border-yellow-400 bg-yellow-50`). It has become a tell of its own. Use a full 1px border in the status color, the icon, a bold first sentence that names the problem, and a second sentence that says what to do.

```html
<div class="alert alert-warn" role="status">
  <svg class="icon" aria-hidden="true" width="20" height="20"><use href="#i-triangle"/></svg>
  <div>
    <p class="alert-title">Your card expires on 31 October.</p>
    <p class="alert-body">Add a new card before then so the November invoice is paid on time. <a href="/billing">Update card</a></p>
  </div>
</div>
```

```css
.alert {
  display: grid;
  grid-template-columns: 20px 1fr;
  gap: 12px;
  padding: 16px;
  border: 1px solid currentColor;
  border-radius: var(--radius);
  background: var(--paper);
}
.alert-warn { color: var(--warn); }
.alert-bad  { color: var(--bad); }
.alert-title { margin: 0; font: 600 16px/1.4 var(--font-sans); color: var(--ink); }
.alert-body  { margin: 4px 0 0; font: 400 14px/1.5 var(--font-sans); color: var(--ink-2); }
.alert a { color: var(--ink); }
```

The border and the icon carry the state color. The text is ink. A warning at `#8A6100` across 40 words of body text would sit at 5.08:1, legal but tiring, and would make the whole box shout.

#### Form validation

- Mark the field with a 2px `--bad` border (pad 1px less to keep the size), set `aria-invalid="true"`, and point `aria-describedby` at the message.
- Put the message directly under the field, in `--bad`, starting with an icon, and say how to fix it: "Enter a date after 1 January 2026", not "Invalid input".
- Keep the label in `--ink`. A red label plus a red border plus red text turns the whole field into an alarm.
- Do not use a green border for valid fields. A field the user filled in correctly needs no reward.

```css
.field input[aria-invalid="true"] {
  border: 2px solid var(--bad);
  padding: 7px 11px; /* 8px 12px minus the extra 1px of border */
}
.field-error {
  display: flex;
  gap: 6px;
  margin: 6px 0 0;
  font: 500 14px/1.4 var(--font-sans);
  color: var(--bad);
}
```

#### Numbers that go up and down

Color a change by its meaning, not its direction. Revenue up is good; costs up, latency up and churn up are bad. A rule that paints every positive delta green will one day paint a doubled error rate green.

- Always print the sign: "+4.2%", and use a true minus (`&minus;`, U+2212) for negatives so the column aligns with tabular numerals.
- Put the meaning in words when it matters: "+38 ms slower".
- When the direction has no fixed meaning (a population count, a temperature), show the change in `--ink-2` with no status color.

#### Review checklist for 2.4

- Exactly three status hues exist. Info notices use ink and an icon.
- Every status shows a word and a distinct icon shape, and still reads correctly in grayscale.
- No status dot pulses, glows or stands alone. No LIVE pill.
- Status color is applied to the icon, the border and the state word, never to paragraphs.
- Washes are 8% in light mode and 14% in dark mode, mixed in `oklab`, and every text color on them passes 4.5:1.
- Deltas are colored by meaning, with an explicit sign.

### 2.5 Depth without shadows

Depth tells the reader which surface is on top, which surface belongs to which, and what will move when they interact. This system draws depth with four signals and never with shadows:

1. Tone. Steps between `--paper`, `--paper-2` and `--paper-3`.
2. Edge. A border, its weight and its color.
3. Offset. Spacing, overlap and position.
4. Inversion. An `--ink` surface with `--paper` text, for the few things that sit above everything.

#### Why shadows go

- Forced colors. In Windows contrast themes (`forced-colors: active`), browsers force `box-shadow` to `none`. A menu drawn with a shadow and no border loses its outline completely and merges into the page. A menu drawn with a border keeps it, recolored to the system `CanvasText`.
- Dark mode. A black shadow on `#141412` has nothing to darken. Material Design hit this and switched dark surfaces to lighter tonal overlays; every shadow-led system ends up maintaining a second depth language for dark mode.
- Print. Shadows are dropped or rasterized badly by print engines and PDF exporters.
- Ambiguity. A blurred edge has no position. A border tells the eye exactly where a hit target ends; `shadow-lg` spreads 15px of gray beyond the box, so the visible extent and the clickable extent differ.
- Cost. Large blur radii on many elements repaint on scroll and on every hover lift.
- Default. `shadow-sm`, `shadow-md` and `shadow-lg` are the Tailwind defaults behind every generated card. Removing them removes the tell at the root.

#### The level table

| Level | What lives there | Light mode | Dark mode |
|---|---|---|---|
| -2 Pressed | Selected row, pressed button, active tab panel background | `--paper-3` | `--paper-3` (lighter than page) |
| -1 Recessed | Sidebar, table header, code block, input group, footer band | `--paper-2`, `--rule` on the shared edge | `--paper-2` |
| 0 Page | Page, cards, panels, content | `--paper`, cards with 1px `--rule` | `--paper`, cards with 1px `--rule` |
| +1 Floating | Menu, dropdown, popover, dialog, sticky header once stuck | `--paper` plus 1px `--rule-strong` | `--paper-2` plus 1px `--rule-strong` |
| +2 Transient | Tooltip, toast, drag preview label | `--ink` with `--paper` text | `--ink` with `--paper` text |

Two languages are at work. Inset language says "this is part of the page, pushed in": a darker tone in light mode, no strong border, at most a 1px `--rule` on the edge it shares with the page. Outset language says "this sits on top of the page": a strong 1px border in `--rule-strong`, the page tone or one step lighter, and a position that overlaps content. Do not mix them. A recessed sidebar with a strong border reads as a floating panel that got stuck.

In dark mode, lighter means closer. Floating layers move from `--paper` (`#141412`) to `--paper-2` (`#1E1D1A`) so the menu reads as nearer than the page, and keep the `--rule-strong` edge. Recessed regions in dark mode still use `--paper-2`; the border on the shared edge and the position tell them apart from floating ones.

#### Z-index scale

Depth in tone needs a matching order in the stack. Use five named layers and nothing else:

```css
:root {
  --z-base: 0;
  --z-sticky: 100;
  --z-dropdown: 200;
  --z-dialog: 300;
  --z-toast: 400;
}
```

#### Card at rest, hover and selected

A card is a bordered region on the page. It does not lift on hover. The hover pattern in generated code (`hover:-translate-y-1 hover:shadow-xl transition-all duration-300`) animates layout-adjacent properties for 300ms and makes the whole grid twitch under the cursor.

```slop
<a class="block rounded-2xl bg-white p-6 shadow-md transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
```

```css
.card {
  display: block;
  padding: 24px;
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  color: var(--ink);
  text-decoration: none;
  box-shadow: none;
  transition: border-color 120ms ease-out;
}
.card:hover { border-color: var(--ink); }
.card:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }

.card[aria-pressed="true"],
.card[aria-checked="true"] {
  background: var(--paper-3);
  border: 2px solid var(--ink);
  padding: 23px;   /* 24px minus the extra 1px of border, so nothing reflows */
}
.card[aria-checked="true"] .card-check { visibility: visible; }
.card-check { visibility: hidden; color: var(--ink); }

@media (prefers-reduced-motion: reduce) {
  .card { transition: none; }
}
```

The selected state uses three signals: tone (`--paper-3`), edge (a 2px `--ink` border with the padding reduced by 1px, so nothing reflows), and a check icon. Removing any one still leaves two. The selection edge is a border and the focus ring is an outline, so both can show at once: focus sits 2px beyond the edge, selection sits on it. Do not draw selection with `outline`, or the focus rule and the selection rule will overwrite each other.

#### Dropdown menu

```html
<div class="menu-anchor">
  <button class="btn" aria-haspopup="menu" aria-expanded="true" aria-controls="m1">Sort: Newest</button>
  <ul class="menu" id="m1" role="menu">
    <li role="menuitemradio" aria-checked="true"><svg class="icon" aria-hidden="true" width="16" height="16"><use href="#i-check"/></svg>Newest</li>
    <li role="menuitemradio" aria-checked="false">Oldest</li>
    <li role="menuitemradio" aria-checked="false">Largest amount</li>
  </ul>
</div>
```

```css
.menu-anchor { position: relative; }
.menu {
  position: absolute;
  top: calc(100% + 4px);
  left: 0;
  z-index: var(--z-dropdown);
  min-width: 200px;
  margin: 0;
  padding: 4px 0;
  list-style: none;
  background: var(--paper);
  border: 1px solid var(--rule-strong);
  border-radius: var(--radius);
  box-shadow: none;
}
.menu [role^="menuitem"] {
  display: flex;
  align-items: center;
  gap: 8px;
  min-height: 32px;
  padding: 0 12px 0 32px;
  font: 400 14px/1.3 var(--font-sans);
  color: var(--ink);
  cursor: default;
}
.menu [aria-checked="true"] { padding-left: 8px; font-weight: 600; }
.menu [role^="menuitem"]:hover,
.menu [role^="menuitem"][data-active] { background: var(--paper-2); }
.menu hr { margin: 4px 0; border: 0; border-top: 1px solid var(--rule); }

:root[data-theme="dark"] .menu { background: var(--paper-2); }
:root[data-theme="dark"] .menu [role^="menuitem"]:hover { background: var(--paper-3); }
```

The 4px gap between trigger and menu shows the page behind, which separates the two better than a shadow would. The border is `--rule-strong` (16:1 against the page), not `--rule` (1.34:1), because the menu must read as a separate object at a glance even when it overlaps a card with its own `--rule` border.

#### Popover with the native API

```css
[popover] {
  margin: 0;
  padding: 12px;
  background: var(--paper);
  color: var(--ink);
  border: 1px solid var(--rule-strong);
  border-radius: var(--radius);
  box-shadow: none;
}
[popover]::backdrop { background: transparent; }
```

User agents give `[popover]` and `dialog` default styles. Chrome's default dialog has no shadow, but component libraries add one; set `box-shadow: none` on both selectors in the reset so nothing returns through a library update.

#### Modal dialog

A dialog interrupts the page. It needs the page to recede and the dialog to stand forward. Use a flat scrim, a strong border, and spacing.

```css
dialog {
  width: min(560px, calc(100vw - 32px));
  max-height: calc(100vh - 64px);
  padding: 0;
  background: var(--paper);
  color: var(--ink);
  border: 1px solid var(--rule-strong);
  border-radius: var(--radius);
  box-shadow: none;
}
dialog::backdrop {
  background: rgb(20 20 18 / 0.56); /* flat, no blur */
  backdrop-filter: none;
}
.dialog-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  border-bottom: 1px solid var(--rule);
}
.dialog-body { padding: 24px; }
.dialog-foot {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  padding: 16px 24px;
  background: var(--paper-2);
  border-top: 1px solid var(--rule);
}
```

The scrim is `--ink` at 56% opacity. Below 40% the page behind still competes for attention; above 70% the user loses the context they need to answer the dialog. The footer is recessed (`--paper-2`), which groups the actions and gives the dialog an internal depth step without a single extra line of decoration. In dark mode, raise the dialog to `--paper-2` and its footer to `--paper-3`, and darken the scrim to 64% black.

#### Sticky header

A sticky header sits over scrolling content, so it must be opaque. A translucent header with `backdrop-blur` is the glass tell (2.8). At the top of the page the header needs no edge. Once content scrolls under it, it needs one.

```html
<div class="sticky-sentinel" aria-hidden="true"></div>
<header class="site-header">...</header>
```

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  background: var(--paper);
  border-bottom: 1px solid transparent;
  box-shadow: none;
  transition: border-color 120ms ease-out;
}
.site-header[data-stuck] { border-bottom-color: var(--rule-strong); }
.sticky-sentinel { height: 1px; margin-bottom: -1px; }
```

```js
const header = document.querySelector(".site-header");
const sentinel = document.querySelector(".sticky-sentinel");
new IntersectionObserver(([entry]) => {
  header.toggleAttribute("data-stuck", !entry.isIntersecting);
}).observe(sentinel);
```

The border starts transparent rather than absent so the header height does not change by 1px when it appears.

#### Sticky table header and first column

```css
.table-wrap { overflow: auto; max-height: 70vh; border: 1px solid var(--rule); }
.table-wrap thead th {
  position: sticky;
  top: 0;
  z-index: 2;
  background: var(--paper-2);
  border-bottom: 1px solid var(--rule-strong);
}
.table-wrap tbody th[scope="row"] {
  position: sticky;
  left: 0;
  z-index: 1;
  background: var(--paper);
  border-right: 1px solid var(--rule-strong);
}
```

With `border-collapse: collapse`, sticky cells lose their borders in some engines as they scroll. Use `border-collapse: separate; border-spacing: 0` on sticky tables and draw the rules on the cells.

#### Dragged item

The default dragged card in generated code is rotated 2 to 3 degrees, scaled to 105% and given `shadow-2xl`. Replace all three with an edge and a placeholder.

```css
.sortable-item[data-dragging] {
  position: relative;
  z-index: var(--z-dropdown);
  background: var(--paper);
  border: 2px solid var(--ink);
  cursor: grabbing;
  box-shadow: none;
  /* position comes from transform: translate(x, y), set by the drag script */
}
.sortable-placeholder {
  min-height: var(--drag-height, 48px);
  background: var(--paper-2);
  border: 1px dashed var(--ink-3);
  border-radius: var(--radius);
}
```

The dragged item keeps its size and angle, so its text stays readable while it moves. The placeholder shows exactly where it will land: a recessed slot (`--paper-2`) with a dashed edge, which is inset language for "empty space waiting". Announce the move through an `aria-live` region ("Invoice 1042 moved to position 3 of 8"), since none of this is visible to a screen reader.

#### Tooltip and toast

The highest layers invert. An `--ink` surface is the furthest possible tone from the page, so it reads as on top without any edge.

```css
.tooltip {
  position: absolute;
  z-index: var(--z-toast);
  max-width: 240px;
  padding: 6px 8px;
  background: var(--ink);
  color: var(--paper);
  font: 400 12px/1.4 var(--font-sans);
  border-radius: var(--radius);
  box-shadow: none;
}
.toast {
  position: fixed;
  left: 16px;
  bottom: 16px;
  z-index: var(--z-toast);
  display: flex;
  gap: 12px;
  align-items: center;
  max-width: min(420px, calc(100vw - 32px));
  padding: 12px 16px;
  background: var(--ink);
  color: var(--paper);
  border-radius: var(--radius);
  box-shadow: none;
}
.toast button { color: var(--paper); background: transparent; border: 1px solid var(--paper); }
```

`--paper` on `--ink` is 16.00:1 in light mode and 15.20:1 in dark mode.

#### Overlap as depth

Overlap is the strongest depth cue that needs no effect at all: when one object covers part of another, the reader knows which is in front. Use it once or twice per page, deliberately.

```css
.band {
  background: var(--paper-2);
  border-bottom: 1px solid var(--rule);
  padding: 64px 16px 112px;   /* 64 + 48 of overlap room */
}
.figures {
  position: relative;
  max-width: 960px;
  margin: -48px auto 0;       /* pulls the strip up across the band edge */
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  background: var(--paper);
  border: 1px solid var(--rule-strong);
}
.figures > div { padding: 24px; border-left: 1px solid var(--rule); }
.figures > div:first-child { border-left: 0; }
```

The figures strip crosses the boundary between the recessed band and the page. The strong border and the page tone mark it as on top. No shadow could say it more clearly.

#### Spacing as depth

Proximity groups things before any tone or border does. Use the spacing scale to build three distances and keep them apart by at least a factor of two:

- Inside a group (label to field, icon to text, lines in a list item): 4 to 8px.
- Between groups (field to field, card to card): 16 to 24px.
- Between sections: 48 to 96px.

When those three distances are clear, many borders can go. A form with 8px from label to input and 24px between fields needs no box around each field. A settings page with 64px between sections needs no card around each section.

#### Review checklist for 2.5

- `box-shadow: none` on every component; no `shadow-*` or `ring-*` classes.
- Every floating layer (menu, popover, dialog) has a 1px `--rule-strong` border and an opaque background.
- Recessed regions use `--paper-2` and at most a 1px `--rule` on the shared edge.
- Selected states combine tone, edge and an icon; none relies on a lift or a glow.
- Hover changes a border color or a background tone within 120ms; nothing translates upward.
- Sticky headers are opaque and gain a rule only when stuck.
- The z-index values come from the five named layers.
- The page still shows every layer edge in forced colors mode (test with Chrome DevTools, Rendering, "Emulate CSS media feature forced-colors").
