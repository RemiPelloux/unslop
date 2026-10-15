### 2.6 Borders and rules

With shadows gone, borders and rules carry most of the structure. That makes them easy to overuse. The rules below keep them few, thin and meaningful.

#### Weights

| Weight | Color | Meaning | Where |
|---|---|---|---|
| 1px | `--rule` | Separates | Card edges, list dividers, table row rules, section dividers, the shared edge of a recessed region |
| 1px | `--ink-3` | Identifies a control | Text inputs, selects, checkboxes, radio buttons (the 3:1 rule from 2.3) |
| 1px | `--rule-strong` | Sits on top | Menus, popovers, dialogs, a stuck header, the bottom of a table header row |
| 2px | `--ink` | This one | Selected item, recommended plan, active section top rule, invalid field in `--bad` |
| 2px | `--accent` | Current location | Active tab underline, current navigation item marker |
| 3px double | `--ink` | Grand total | The bottom rule under a final total row, as in printed accounts |
| 4px | `--ink` | Masthead | One rule at the top of a page or report, at most once |

Nothing is thicker than 4px. Nothing uses a dotted border. Dashed borders appear in exactly one place: an empty drop target or placeholder (2.5).

1px separates; 2px marks. A 2px rule says "this one, not the others", so a view group contains at most one 2px element of each meaning. If three cards in a row each have a 2px border, none of them is marked.

#### Colors

Borders use five colors: `--rule`, `--rule-strong`, `--ink-3`, `--accent`, and the three status colors in alerts and invalid fields. No border is ever a tint of the accent (`border-orange-200`), a translucent white (`border-white/10`), or a translucent black (`ring-black/5`). Translucent borders are a glass-era habit: their color depends on what sits behind them, so the same component shows a different edge on every surface.

On `--paper-2`, the default `--rule` drops from 1.34:1 to 1.24:1 against its surface. That is still visible for dividers. For anything stronger inside a recessed region, step to `--ink-3`, never to a darker invented gray.

#### 1px on high-density and scaled displays

- Use `border`, not a 1px-high element with a background color. Browsers snap border widths to whole device pixels. A `div` with `height: 1px` is laid out like any other box, so at 125% and 150% Windows display scaling some of these lines land on one device pixel and others on two, and a stack of dividers looks uneven.
- Do not use `0.5px` hairlines. Safari draws them as one device pixel on 2x screens; Chrome and Firefox round sub-pixel border widths up to one device pixel, so the "hairline" is a normal 1px line on most screens and a different weight on Safari. For a lighter line, lighten the color, not the width.
- Do not fake hairlines with `transform: scaleY(0.5)` pseudo-elements. They blur on 1x displays and break when the parent is scaled.
- Keep boxes with borders on whole-pixel positions. `transform: translate(-50%, -50%)` on an element with an odd width puts its edges on half pixels, and the 1px border renders as a 2px gray smear. Center with grid or flex instead, or round the size to an even number.

```css
:root { --rule-w: 1px; }
.divider { border: 0; border-top: var(--rule-w) solid var(--rule); }
.center-overlay {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center; /* no translate(-50%) half-pixel edges */
}
```

#### Dividers or spacing

Pick one per boundary. Never a rule and a 48px gap on the same edge.

Use a rule when:

- Items are of the same kind and the reader scans across rows (tables, inbox lists, settings lists, line items).
- Rows are dense (row height under 48px) and spacing alone would need too much height to separate them.
- A boundary must survive reflow, such as a sticky header meeting the content below.

Use spacing when:

- Groups differ in kind (account details, then billing, then danger zone).
- The content inside each group already has strong edges (inputs, images, buttons).
- There are fewer than five groups on the screen.

For lists, draw rules between items, not around them. A list of eight items needs seven lines, not eight boxes.

```css
.list { margin: 0; padding: 0; list-style: none; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); }
.list > li { padding: 12px 0; }
.list > li + li { border-top: 1px solid var(--rule); }
```

#### Table rules

Tables follow the conventions of printed financial tables, which solved this problem a century ago.

- Horizontal rules only, 1px `--rule`, between rows.
- No vertical rules, except one 1px `--rule` to separate a group of columns (before a totals column, between "This year" and "Last year" groups).
- The header row sits on `--paper-2` with a 1px `--rule-strong` bottom edge.
- A subtotal row has a 1px `--ink` top rule. A grand total has a 1px `--ink` top rule and a 3px double `--ink` bottom rule.
- Zebra striping is for tables wider than eight columns, where the eye loses the row. When stripes are used, row rules are removed. Never both.
- Row hover is `--paper-2`. Selected row is `--paper-3`, with a checkbox in the first column showing the state.

```css
.ledger { width: 100%; border-collapse: collapse; font: 400 14px/1.4 var(--font-sans); font-variant-numeric: tabular-nums; }
.ledger th, .ledger td { padding: 8px 12px; text-align: left; border-bottom: 1px solid var(--rule); }
.ledger thead th { background: var(--paper-2); border-bottom: 1px solid var(--rule-strong); font-weight: 600; }
.ledger td.num, .ledger th.num { text-align: right; }
.ledger .group-start { border-left: 1px solid var(--rule); }
.ledger tr.subtotal td { border-top: 1px solid var(--ink); font-weight: 600; }
.ledger tr.total td { border-top: 1px solid var(--ink); border-bottom: 3px double var(--ink); font-weight: 600; }
.ledger tbody tr:hover { background: var(--paper-2); }
.ledger tbody tr[aria-selected="true"] { background: var(--paper-3); }
```

#### The "border on everything" failure

When a team removes shadows without a plan, it replaces each shadow with a border. The page turns into box soup: a bordered section containing bordered cards containing bordered inputs inside bordered field groups. Every element announces its edges and none of them stands out.

```slop
<section class="rounded-lg border border-gray-200 p-6">
  <div class="rounded-lg border border-gray-200 p-4">
    <div class="rounded-md border border-gray-200 p-3">
      <label class="text-sm">Email</label>
      <input class="mt-1 w-full rounded-md border border-gray-300 px-3 py-2">
    </div>
    <div class="rounded-md border border-gray-200 p-3">...</div>
  </div>
</section>
```

Four nested boxes around one input. Fix it with three limits:

1. At most two bordered containers nested inside each other. A bordered card may hold bordered inputs. A bordered card may not hold a bordered card.
2. Inside a bordered container, group with spacing and rules, not boxes.
3. A page section is not a box. Sections are separated by spacing, a tone change or a single rule.

```html
<section class="settings-section">
  <h2>Contact</h2>
  <div class="field"><label for="email">Email</label><input id="email" type="email"></div>
  <div class="field"><label for="phone">Phone</label><input id="phone" type="tel"></div>
</section>
```

```css
.settings-section { padding: 32px 0; border-top: 1px solid var(--rule); }
.settings-section h2 { margin: 0 0 24px; font: 600 18px/1.25 var(--font-sans); }
.field { display: grid; gap: 4px; margin-bottom: 24px; max-width: 28rem; }
.field label { font: 500 14px/1.4 var(--font-sans); color: var(--ink); }
```

One rule above the section, borders on the inputs, nothing else.

#### Grids of cells without doubled lines

Adjacent bordered cells with no gap draw 2px lines where they meet. Draw the grid with a gap and let the container's background show through it:

```css
.cells {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1px;
  background: var(--rule);
  border: 1px solid var(--rule);
}
.cells > * { background: var(--paper); padding: 16px; }
```

Every line is exactly 1px, including at the outer edge, at any column count. If the last row is incomplete, the empty area shows as `--rule`; fill it with empty cells or set the container background to `--paper` and give the cells `outline: 1px solid var(--rule)` instead.

#### Review checklist for 2.6

- Every border uses one of the listed weights and colors. No translucent borders.
- No element has more than two bordered ancestors.
- Each boundary is a rule or a gap, not both.
- Tables have horizontal rules only, a strong header edge and accounting rules on totals.
- Rules are drawn with `border`, never with 1px filled elements, and never at 0.5px.
- Dashed borders appear only on placeholders and drop targets.

### 2.7 Corner radius

Use `--radius: 2px` everywhere, or `0` everywhere. Never above 4px on a rectangle.

#### Why large radius reads as generated

Library radius defaults have climbed for a decade and generated code takes the top of the range:

| Source | Value |
|---|---|
| Tailwind `rounded` / `rounded-md` / `rounded-lg` | 4px / 6px / 8px |
| Tailwind `rounded-xl` / `rounded-2xl` / `rounded-3xl` | 12px / 16px / 24px |
| shadcn/ui `--radius` | 0.5rem (8px), later 0.625rem (10px), with `Card` at `rounded-xl` |
| Bootstrap 5 `--bs-border-radius` | 0.375rem (6px) |
| iOS app icon mask | about 22% of the icon width |

`rounded-2xl` on cards and `rounded-xl` on buttons are what a model writes when nothing tells it otherwise. A 16px corner on a 320px card reads as an app-store tile, and putting that tile on every surface makes a document look like a phone home screen. Large radii also cost space: text must clear the curve, so a 16px corner forces padding of at least 16px in every direction, and dense tables or toolbars cannot use it at all.

#### The policy

- `--radius: 2px` for products with controls (apps, dashboards, forms). 2px is enough to soften the anti-aliased corner pixel so edges do not look jagged on 1x screens, and small enough that nobody perceives the shape as rounded.
- `--radius: 0` for editorial products, reports and documents, where everything should feel set on a page.
- One value per product. Buttons, inputs, cards, menus, dialogs, badges, tooltips, code blocks and images all use it.
- 4px is the hard ceiling and is reserved for one case: a component that sits inside a third-party frame with its own larger radius (an embedded payment field, for example) and would look broken at 2px.

```css
:root { --radius: 2px; }
button, input, select, textarea, .card, .menu, dialog, .badge, .tooltip, pre, img.framed {
  border-radius: var(--radius);
}
```

#### Nested radius math

When a rounded element sits inside another with padding between them, the inner radius must be the outer radius minus the padding, or the gap between the curves looks thicker at the corners:

```
inner radius = max(0, outer radius - padding)
```

Generated code nests equal radii (`rounded-2xl` inside `rounded-2xl` with `p-2`), which produces a visible fat crescent at each corner. With a 16px outer radius and 8px of padding, the inner should be 8px, not 16px.

With this handbook's policy, the math almost always returns zero: a 2px outer radius with any padding of 2px or more gives an inner radius of 0. That is correct. Square children inside a 2px frame look aligned.

```css
.frame {
  --pad: 4px;
  padding: var(--pad);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
}
.frame > * {
  border-radius: max(0px, calc(var(--radius) - var(--pad))); /* resolves to 0 */
}
```

The same rule applies to the focus outline. Current browsers draw `outline` following `border-radius` (Chrome 94, Firefox 88, Safari 16.4 and later). With `outline-offset: 2px` the outline's curve has radius `--radius + 2px`, which is 4px with the policy above, and still reads as square.

#### The pill ban

`rounded-full` on a rectangle is banned: no pill buttons, pill badges, pill tags, pill search fields, pill navigation, pill toggle groups. Reasons:

- The LIVE, NEW and BETA pill is a fingerprint (2.1).
- A pill needs end caps of half its height. A 32px tall pill button needs about 16px more horizontal padding than a 2px button to keep the label off the curve, and that space multiplies across a toolbar.
- Pills with long labels stretch into capsules and wrap badly.
- A row of pills reads as one undifferentiated chain; a row of square tags with 8px gaps reads as separate items.

Circles and capsules are allowed only where the shape itself carries meaning:

| Element | Shape | Why |
|---|---|---|
| Avatar | Circle | Convention for a person; separates people from objects |
| Radio input | Circle | Platform convention that separates single choice from checkbox |
| Switch track and thumb | Capsule and circle | Platform convention for an on/off toggle |
| Color swatch in a picker | Circle or square, consistently | The fill is the content |
| Map pin, chart dot | Circle | Data mark, not a container |

A count beside a navigation item (unread messages) is a square badge with `--radius`, not a red circle.

#### Review checklist for 2.7

- One radius value in the whole product: 2px or 0.
- No `rounded-lg`, `rounded-xl`, `rounded-2xl`, `rounded-3xl` or `rounded-full` on rectangles.
- Nested elements follow `inner = max(0, outer - padding)`.
- Circles appear only for avatars, radio buttons, switch parts, swatches and data marks.
- Images are square-cornered or match `--radius`, never more.

### 2.8 Glass, blur, glow, noise and neon

These five effects share a cause: they try to give a flat screen the look of a lit, physical object. Each one became a trend, then a component library preset, then a default in generated output. All are banned. Each has a flat replacement that is easier to read and cheaper to render.

#### The ban list

| Effect | Typical code | Why it fails | Replacement |
|---|---|---|---|
| Glass panel | `bg-white/10 backdrop-blur-lg border-white/20` | Text contrast depends on whatever scrolls behind; `backdrop-filter` recomposites a blurred copy of the page on every scroll frame | Opaque `--paper` or `--paper-2` panel with a 1px border |
| Frosted header | `sticky top-0 bg-white/70 backdrop-blur` | Headings scroll under the header and show through as gray smears; the header has no fixed contrast | Opaque `--paper` header, rule when stuck (2.5) |
| Blur blobs | `absolute h-96 w-96 bg-purple-500 opacity-30 blur-3xl` | Pure decoration; large offscreen layer; leads straight back to blue-violet | Delete |
| Colored glow | `shadow-lg shadow-indigo-500/50`, `0 0 40px rgba(99,102,241,.5)` | A shadow with a hue; on dark pages it halos text and blurs edges | 1px `--rule-strong` border, or nothing |
| Focus glow | `focus:ring-4 focus:ring-indigo-500/25` | Soft, low-contrast ring (indigo at 25% on white is about 1.4:1) | `outline: 2px solid var(--focus); outline-offset: 2px` |
| Text glow | `text-shadow: 0 0 12px #22d3ee` | Blurs letter edges; reduces legibility; reads as a synthwave template | Plain text in `--ink` or `--accent` |
| Neon on black | Saturated cyan or magenta text on `#000` | Halation: bright saturated strokes on black bleed into the background for readers with astigmatism | `--ink` dark (`#ECE9E1`) on `--paper` dark (`#141412`) |
| Grain and noise | SVG `feTurbulence` or a noise PNG at 3% to 8% opacity over the page | Exists to hide gradient banding; with no gradients it has no job; costs a full-page layer | Nothing. Texture comes from type and rules. |
| Cursor spotlight | A radial gradient that follows the pointer | Gradient plus motion; invisible to touch and keyboard users | Hover border change on the item under the pointer |
| Tilt cards | `perspective` plus `rotateX/rotateY` following the pointer | Moves text while the user reads it; ignores reduced motion | Static card with hover border |
| Shimmer skeleton | A light gradient sweeping across gray blocks forever | Gradient plus endless motion | Static `--paper-2` blocks, then content |
| Inner glow on inputs | `ring-inset` with a colored blur | Box shadow by another name | `--ink-3` border, 2px `--bad` when invalid |

#### Why glass fails contrast

A glass panel is translucent by definition, so its text sits on a background that changes as the page scrolls. With `bg-white/10` over a dark photo, white text may measure 12:1 over a shadow area and 1.3:1 over a sky. No single ratio exists, and automated tests cannot compute one. The only fix that keeps contrast stable is an opaque background, which is the end of the glass.

The cost is concrete too. `backdrop-filter: blur(16px)` makes the browser render the content behind the element into a separate texture, blur it and composite the result on every frame that the content or the panel moves. On a sticky header that runs on every scroll frame, and on low-end Android phones it is a common cause of scroll jank.

#### Skeletons without shimmer

```css
.skeleton {
  display: block;
  height: 14px;
  margin: 8px 0;
  background: var(--paper-2);
  border-radius: var(--radius);
}
.skeleton[data-w="60"] { width: 60%; }
.skeleton[data-w="40"] { width: 40%; }
```

A static block tells the user where content will appear. The shimmer adds nothing to that and moves forever. If loading takes longer than about one second, replace the skeleton with a sentence ("Loading 2,418 invoices") rather than animating it.

#### Focus without glow

The focus indicator is an outline. It is not a ring utility, not a box shadow and not a colored halo.

```css
:where(a, button, input, select, textarea, summary, [tabindex]):focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
  box-shadow: none;
}
```

`--focus` is `#1A1A18` in light mode (16:1 on `--paper`) and `#ECE9E1` in dark mode (15.2:1). It passes WCAG 2.2 focus appearance with room to spare. The Tailwind equivalent is `focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2`, and every `ring-*` class should be removed (2.11 disables them in the config).

#### Review checklist for 2.8

- No `backdrop-filter`, no `backdrop-blur`, no translucent panel backgrounds over content.
- No `blur()` filters on decorative elements.
- No colored shadows, no `text-shadow`, no glow on focus.
- No noise or grain layers.
- No pointer-following or tilt effects.
- Skeletons are static.

### 2.9 Dark mode done by hand

Dark mode is a second palette, designed and measured like the first. It is not the light palette inverted, not `filter: invert(1)`, and not every class doubled with `dark:bg-gray-900 dark:text-white`.

#### What generated dark modes get wrong

```slop
<div class="bg-white text-gray-900 dark:bg-slate-900 dark:text-white">
  <div class="rounded-2xl bg-white shadow-lg dark:bg-slate-800 dark:shadow-indigo-500/10">
```

- `slate-900` is `#0F172A`, a navy at OKLCH chroma 0.040 and hue 266. The whole page turns blue.
- `text-white` on `slate-900` is 17.85:1. Pure white on near-black at that ratio produces halation for many readers: the strokes glow and smear.
- The shadow does nothing on a dark page, so the kit tints it indigo to make it show. That is a glow.
- The card is `slate-800` on `slate-900`, one step lighter, which is right in principle, but chosen from a blue ramp.

#### The canonical dark tokens, measured

| Token | Hex | OKLCH | On dark `--paper` |
|---|---|---|---|
| `--paper` | `#141412` | `0.190 0.004 107` | 1.00:1 |
| `--paper-2` | `#1E1D1A` | `0.231 0.006 92` | 1.09:1 |
| `--paper-3` | `#2A2925` | `0.281 0.007 95` | 1.27:1 |
| `--rule` | `#34322E` | `0.318 0.008 85` | 1.44:1 |
| `--ink-3` | `#8F8B81` | `0.637 0.015 89` | 5.43:1 |
| `--ink-2` | `#B5B1A7` | `0.761 0.015 89` | 8.62:1 |
| `--ink` | `#ECE9E1` | `0.934 0.011 90` | 15.20:1 |
| `--accent` | `#E2703F` | `0.671 0.156 43` | 5.82:1 |
| `--accent-ink` on `--accent` | `#141412` | | 5.82:1 |
| `--ok` | `#7FB38A` | `0.719 0.081 151` | 7.66:1 |
| `--warn` | `#D9A93A` | `0.760 0.136 84` | 8.51:1 |
| `--bad` | `#E0705F` | `0.672 0.143 30` | 5.84:1 |

#### Rules for the dark palette

- No pure black. `#000000` turns OLED pixels fully off; when the page scrolls, pixels switching on from off lag behind their neighbors and smear dark content. It also pushes halation around light text to its peak. Keep the darkest surface between OKLCH L 0.16 and 0.22. `#141412` is 0.190.
- No pure white text. `#FFFFFF` on `#141412` is 18.44:1. The canonical `--ink` at 15.20:1 is easier to read for long stretches and still far above 7:1.
- Keep the temperature. The dark neutrals share the light neutrals' hue (about 90), so both themes feel like the same product.
- Spread the surface steps wider. Light surfaces step about 0.03 in L; dark surfaces step about 0.04 to 0.05 (0.190, 0.231, 0.281). Equal L steps look smaller at the dark end, and the contrast ratios confirm it: the light `--paper` to `--paper-3` step is 1.20:1 and the dark one is 1.27:1, which is about the minimum that reads as a separate surface on a dim screen.
- Lighter means closer. Floating layers move up one surface step (2.5).
- Re-pick the accent. The light accent `#B4441C` on `#141412` is 3.32:1 and fails for text. The dark accent `#E2703F` keeps hue (39 to 43) and chroma, raises L from 0.535 to 0.671, and flips `--accent-ink` to dark.
- Calm the status colors. Saturated colors on dark grounds vibrate. The dark status colors raise L to 0.67 to 0.76 and cut chroma by 15% to 20% against their light versions (ok goes from 0.100 to 0.081).
- No glow, ever. Dark mode is where glows creep back in, because a dark page with no shadows can feel flat to a team used to them. The answer is the tone steps and `--rule-strong` borders, not light leaking from edges.

#### Switching themes

Respect the system setting by default and let the user override it. Set `color-scheme` so native controls, scrollbars and the default canvas follow.

```html
<meta name="color-scheme" content="light dark">
<script>
  try {
    const t = localStorage.getItem("theme");
    if (t === "light" || t === "dark") document.documentElement.dataset.theme = t;
  } catch (e) {}
</script>
```

```css
:root { color-scheme: light; /* light tokens from the authoring guide */ }

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --paper: #141412; --paper-2: #1E1D1A; --paper-3: #2A2925;
    --ink: #ECE9E1;   --ink-2: #B5B1A7;   --ink-3: #8F8B81;
    --rule: #34322E;  --rule-strong: #ECE9E1;
    --accent: #E2703F; --accent-ink: #141412;
    --ok: #7FB38A;    --warn: #D9A93A;    --bad: #E0705F;
    --focus: #ECE9E1;
  }
}
:root[data-theme="dark"] {
  color-scheme: dark;
  /* same values as above */
}
body { background: var(--paper); color: var(--ink); }
```

The inline script runs before first paint, so a user who chose dark does not see a flash of light. Keep it in the `head`, before the stylesheet link. The tokens are declared twice (media query and attribute) because the attribute must win in both directions: `data-theme="light"` on a dark system and `data-theme="dark"` on a light one.

#### Borders in dark mode

`--rule` at `#34322E` is 1.44:1 on `--paper`, which is about the same visual weight as the light rule. On `--paper-3` it drops to 1.14:1 and nearly vanishes. Accept that for selected rows, where the tone change itself marks the row, but not for inputs: inputs keep `--ink-3` (5.43:1).

`--rule-strong` in dark mode is `#ECE9E1`, a bright line. On a large dialog that bright frame can dominate the screen. For floating layers larger than about 480px wide, use `--ink-3` (5.43:1) as the border instead; it still clears the 3:1 boundary rule and reads as an edge, not a frame.

#### Images, screenshots, logos and diagrams

- Do not invert or filter photographs. Put a 1px `--rule` border around them so pale photos do not bleed into the page edge.
- Ship dark screenshots of the product for dark mode with `<picture>` and a media query, rather than showing a white screenshot on a dark page.
- Logos need a reversed version. A dark logo on `#141412` disappears.
- Inline SVG icons and diagrams use `currentColor` and the tokens, so they switch themselves. Never hard-code `#000` or `#FFF` in an SVG that ships inline.
- Charts get their own dark palette (2.10).

```html
<picture>
  <source srcset="/img/report-dark.png" media="(prefers-color-scheme: dark)">
  <img src="/img/report-light.png" alt="Monthly report with revenue by region" width="1200" height="760">
</picture>
```

When the site has a manual theme toggle, the `media` attribute follows the system setting and not the toggle. Swap the `src` from the same script that sets `data-theme`, or render both images and hide one with `:root[data-theme="dark"] .only-light { display: none; }`.

#### Testing a dark palette

1. Measure every pairing in the table above against `--paper`, `--paper-2` and `--paper-3`, not only the page.
2. View it at full and at 20% screen brightness. Surface steps that vanish at 20% need a wider L gap.
3. View it on an OLED phone in a dark room. Halation and smear show there first.
4. Turn on forced colors emulation and check that every floating layer still has an edge.
5. Grep for `#000`, `#000000`, `#FFF`, `#FFFFFF`, `black` and `white` in component styles. Each hit should be a token instead.

#### Review checklist for 2.9

- Dark mode has its own measured token set with the same hue temperature as light mode.
- The darkest surface is between OKLCH L 0.16 and 0.22; no `#000`. No `#FFF` text.
- Surface steps are 0.04 to 0.05 apart in L.
- The accent and status colors were re-picked for dark and pass 4.5:1 as text.
- Floating layers move one step lighter; nothing glows.
- `color-scheme` is set, the theme loads before first paint, and images have dark variants or borders.
