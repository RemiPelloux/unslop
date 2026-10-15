## Part 2. Color, Surfaces and Depth

Color is where generated interfaces give themselves away first: color defaults are the easiest thing for a model to reproduce and the hardest for a reviewer to catch one decision at a time. The rules here are strict on purpose: no box shadows, no gradients, no glass, no glow, and one accent per product, outside the blue to violet band.

Every value in this Part uses the canonical tokens from the authoring guide. When this Part says `--paper`, it means `#F7F5F0` in light mode and `#141412` in dark mode. Contrast ratios quoted here were computed with the WCAG 2.x relative luminance formula, not estimated.

### 2.1 Why generated interfaces all look alike

A generated interface is the sum of library defaults. Each default was picked by a different team for a different reason, and none of them is wrong in isolation. Stacked together on one screen, they produce a page that a reader recognizes in under a second as unedited output: indigo button, bluish gray text, white card with a 16px corner and a soft shadow, a purple gradient behind the headline, Inter for everything.

Language models reproduce this stack because their training data is full of documentation snippets, starter templates and component library examples, which repeat the same handful of classes thousands of times. The most likely class for a button is the one from the docs, and so is the most likely class for a card. Every decision lands on the median, and a page made only of medians has no author.

#### The default stack, traced to its sources

| Symptom | Exact value | Where it comes from | Replace with |
|---|---|---|---|
| Indigo primary button | `bg-indigo-600` = `#4F46E5`, OKLCH hue 277 | Tailwind UI components and most Tailwind docs examples use indigo as the brand stand-in | One accent outside OKLCH 235 to 335, such as `--accent: #B4441C` |
| Blue focus ring | Tailwind v3 default ring color, `blue-500` at 50% opacity | The `ring` utility default; Laravel Breeze inputs add `focus:ring-indigo-500` | `outline: 2px solid var(--focus); outline-offset: 2px` |
| Bluish gray text | `text-gray-500` = `#6B7280`, OKLCH chroma 0.023 at hue 264 | Tailwind's `gray` scale is tinted toward blue; `slate` is tinted harder (chroma 0.04) | A neutral with a stated temperature, chroma under 0.012 |
| Navy dark mode | `#020817`, which is `hsl(222.2 84% 4.9%)` | The shadcn/ui slate theme dark `--background` | `--paper: #141412`, a warm near-black |
| Card with soft lift | `rounded-xl border shadow-sm`, or `rounded-2xl shadow-lg` | The shadcn/ui `Card` component; the Tailwind docs card examples | `border: 1px solid var(--rule)`, `border-radius: 2px`, no shadow |
| One typeface for all text | Inter, or Geist | Figma's default text style, Tailwind UI templates, Vercel starters | A deliberate pairing (Part 3), Plex Sans and Source Serif 4 here |
| Gradient hero | `from-indigo-500 via-purple-500 to-pink-500` | The Tailwind docs example for gradient color stops; the 2020 Stripe mesh header; the 2021 Linear site | A flat `--paper-2` band with a 2px `--ink` rule |
| Glass panel | `bg-white/10 backdrop-blur-md border-white/20` | macOS Big Sur vibrancy and the 2020 to 2021 Dribbble glass trend | An opaque `--paper` panel with a 1px `--rule-strong` border |
| Glow behind the headline | A blurred indigo circle at 20% to 40% opacity | Landing page kits such as Aceternity UI ("Spotlight", "Background Beams") | Nothing. Let the headline sit on the paper. |
| Green pulsing dot | `h-2 w-2 rounded-full bg-green-500 animate-pulse` | Status page templates and dashboard kits | A text label with an icon: "Running", "Paused" |
| Purple for anything with a model behind it | Violet text, a four-point star icon, a violet to blue gradient | AI feature branding across large products since 2023 | The product's normal accent and a plain label |

Each row is one decision. A screen that hits three or more rows reads as generated, even if the rest of the work is careful.

#### Why indigo in particular

Indigo became the default brand color of the web because Tailwind UI, launched in 2020, used `indigo-600` as the placeholder brand in almost every component. The intent was "replace this with your brand". Thousands of projects never replaced it, then those projects became training data. The OKLCH values make the cluster visible:

| Tailwind color | Hex | OKLCH | White text contrast |
|---|---|---|---|
| `sky-500` | `#0EA5E9` | `0.685 0.148 237` | 2.77:1 |
| `blue-500` | `#3B82F6` | `0.623 0.188 260` | 3.68:1 |
| `blue-600` | `#2563EB` | `0.546 0.215 263` | 5.17:1 |
| `indigo-500` | `#6366F1` | `0.585 0.204 277` | 4.47:1 |
| `indigo-600` | `#4F46E5` | `0.511 0.230 277` | 6.29:1 |
| `violet-500` | `#8B5CF6` | `0.606 0.219 293` | 4.23:1 |
| `purple-500` | `#A855F7` | `0.627 0.233 304` | 3.96:1 |
| `fuchsia-500` | `#D946EF` | `0.667 0.259 322` | 3.46:1 |

All eight sit between OKLCH hue 237 and 322. That is the band this handbook bans for accents and gradients (2.3 gives the exact limits). Note the third column too: `indigo-500` with white text is 4.47:1, just under the 4.5:1 floor, so the most copied button color on the web fails contrast at its most copied weight.

#### Why the same card appears everywhere

The card is a white rectangle on a light gray page (`bg-gray-50`, `#F9FAFB`), corner radius 12px or 16px, padding 24px, and a shadow. The shadow does the work that a border or a tone step would do, and it does it badly: on a `#F9FAFB` page, a `shadow-sm` is a 1px smear at 5% black that most displays render as a faint gray line. The radius is large enough to read as "app", and small enough to read as "not a pill". Nobody chose it. It is `rounded-xl`, because that is what the component library ships.

```slop
<div class="min-h-screen bg-gray-50">
  <div class="mx-auto max-w-sm rounded-2xl bg-white p-6 shadow-lg ring-1 ring-black/5">
    <div class="flex items-center gap-2">
      <span class="h-2 w-2 animate-pulse rounded-full bg-green-500"></span>
      <span class="text-xs font-medium text-green-600">LIVE</span>
    </div>
    <h3 class="mt-4 bg-gradient-to-r from-indigo-500 to-purple-600 bg-clip-text text-2xl font-bold text-transparent">
      Supercharge your workflow
    </h3>
    <p class="mt-2 text-sm text-gray-500">Seamless insights, powered by AI.</p>
    <button class="mt-6 w-full rounded-xl bg-indigo-600 px-4 py-2.5 text-white shadow-md hover:bg-indigo-500">
      Get started
    </button>
  </div>
</div>
```

Count the tells: gray-50 page, `rounded-2xl`, `shadow-lg`, `ring-black/5`, pulsing green dot, LIVE label, gradient text, indigo to purple, bluish gray body text, indigo button with a shadow, and a headline built from banned verbs. Eleven defaults in fourteen lines.

The same content, with every decision made on purpose:

```html
<article class="job">
  <p class="job-status"><svg class="icon" aria-hidden="true" width="16" height="16"><use href="#i-play"/></svg> Running since 09:14</p>
  <h3 class="job-title">Nightly invoice export</h3>
  <p class="job-meta">2,418 invoices written to <code>exports/2026-10-15.csv</code></p>
  <button class="btn btn-primary" type="button">Open the file</button>
</article>
```

```css
.job {
  max-width: 28rem;
  padding: 24px;
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  box-shadow: none;
}
.job-status {
  display: flex;
  gap: 8px;
  align-items: center;
  margin: 0;
  font: 500 14px/1.4 var(--font-sans);
  color: var(--ok);
}
.job-title {
  margin: 16px 0 4px;
  font: 600 21px/1.2 var(--font-sans);
  color: var(--ink);
}
.job-meta {
  margin: 0 0 24px;
  font: 400 14px/1.5 var(--font-sans);
  color: var(--ink-2);
}
.btn-primary {
  background: var(--accent);
  color: var(--accent-ink);
  border: 1px solid var(--accent);
  border-radius: var(--radius);
  padding: 8px 16px;
  box-shadow: none;
}
```

One border, one accent, one status color paired with an icon and a time, and copy that says what happened. Nothing traces to a library default.

#### The fingerprint scan

Run this scan on any screen before review. Each line is a tell; each tell has a grep string so it can run in CI (2.11 has the full commands).

1. A primary color between OKLCH hue 235 and 335. Grep for `indigo-`, `violet-`, `purple-`, `blue-6`, `#6366F1`, `#4F46E5`.
2. Any CSS gradient or Tailwind gradient utility. Grep for `gradient`, `from-`, `via-`.
3. Any `box-shadow` other than `none`, any `shadow-*` utility, any `ring-*` utility (Tailwind rings compile to box shadows).
4. Corner radius above 4px on anything that is not a circle. Grep for `rounded-lg`, `rounded-xl`, `rounded-2xl`, `rounded-3xl`.
5. `backdrop-filter`, `backdrop-blur`, or a translucent white panel (`bg-white/10`).
6. A blurred decorative element: `blur-3xl`, `filter: blur(` on a `div` with no content.
7. Gray text from a blue-tinted scale: `text-gray-500`, `text-slate-`, `#6B7280`, `#64748B`.
8. Dark mode background with blue chroma: `#020817`, `#0F172A`, `slate-900`, `slate-950`.
9. Status shown only by a colored dot, or an `animate-pulse` on a status element.
10. A LIVE, NEW or BETA pill with a dot.
11. A sparkle or star icon next to anything automated.
12. Emoji used as icons or bullets.

The target is zero. A system built from this Part gets there by default: its tokens hold none of the raw material.

#### Review checklist for 2.1

- The accent hue is outside OKLCH 235 to 335, and nobody on the team can say "we kept it from the template".
- No class or value in the markup can be found verbatim in the Tailwind UI or shadcn/ui example code without a deliberate reason written next to it.
- The neutral scale is the product's own, with a chroma under 0.012, not Tailwind `gray`, `slate` or `zinc`.
- The fingerprint scan returns zero hits.

### 2.2 The gradient ban

The rule has two levels. First, zero blue, purple, indigo or violet gradients, anywhere, in any medium, with no exceptions. Second, zero CSS gradients of any hue in interface chrome. A gradient that exists in a photograph is part of the photograph and is fine. A gradient written in CSS or a Tailwind class is not.

The first level exists because the blue to purple gradient is the single most reliable marker of generated work. The second level exists because every other gradient is one hue change away from the first, and because the replacements are better in every measurable way: they print, they pass contrast checks, they survive forced colors mode, and they do not band.

#### The forms a gradient takes

Each shape below is banned and has a direct replacement.

##### Background gradient on a hero or section

```slop
<section class="bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 py-24 text-white">
  <h1 class="text-5xl font-bold">The future of work is here</h1>
</section>
```

Source: the Tailwind docs color stop example and every SaaS template since 2020. The text contrast changes across the section: white on `pink-500` (`#EC4899`) is 3.53:1, white on `indigo-600` is 6.29:1, so the headline passes at one end and fails at the other.

Replacement: a flat band. Use `--paper-2` for a quiet band or `--ink` for an inverted band, with a rule to mark the edge.

```css
.hero {
  background: var(--paper-2);
  border-bottom: 2px solid var(--ink);
  padding: 96px 16px 64px;
}
.hero h1 {
  max-width: 18ch;
  margin: 0;
  font: 600 56px/1.1 var(--font-serif);
  color: var(--ink);
}
.hero-inverted {
  background: var(--ink);
  color: var(--paper);
}
```

##### Gradient text

```slop
<h1 class="bg-gradient-to-r from-violet-600 to-indigo-600 bg-clip-text text-transparent">
  Ship faster
</h1>
```

Gradient text sets `color: transparent` and paints the letters with a clipped background. Contrast cannot be computed for it, so axe and Lighthouse report it as "needs review" and move on, which means nobody checks it. Selected text shows the selection color on transparent glyphs, and copied text loses its emphasis.

Replacement: emphasis through type. Use weight, size, a serif against a sans, or an accent underline.

```css
.headline em {
  font-style: normal;
  text-decoration-line: underline;
  text-decoration-color: var(--accent);
  text-decoration-thickness: 3px;
  text-underline-offset: 6px;
}
```

```html
<h1 class="headline">Invoices that reconcile <em>before</em> month end</h1>
```

##### Gradient border

```slop
<div class="rounded-2xl bg-gradient-to-r from-indigo-500 to-fuchsia-500 p-[1px]">
  <div class="rounded-2xl bg-white p-6">Pro plan</div>
</div>
```

The wrapper trick (a 1px padded gradient parent behind a solid child), `border-image` with a gradient, and the `mask-composite: exclude` trick all produce the same result: an outline that glows from one hue to another.

Replacement: a solid border with a weight difference. To single out one item in a set, give it a 2px `--ink` border while the others keep 1px `--rule`, and say why in text.

```css
.plan { border: 1px solid var(--rule); padding: 24px; border-radius: var(--radius); }
.plan[data-recommended] {
  border: 2px solid var(--ink);
  padding: 23px; /* keeps outer size equal to the 1px plans */
}
.plan-flag {
  margin: 0 0 8px;
  font: 600 12px/1.3 var(--font-sans);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--accent);
}
```

##### Mesh blobs

```slop
<div class="absolute -top-40 left-1/2 h-[600px] w-[600px] -translate-x-1/2 rounded-full bg-purple-500 opacity-30 blur-3xl"></div>
<div class="absolute top-20 right-0 h-[400px] w-[400px] rounded-full bg-blue-500 opacity-20 blur-3xl"></div>
```

Two to four large circles in blue, purple and pink, blurred by 64px or more and placed behind the hero copy. Source: the Stripe header of 2020, then every template that imitated it. A 64px blur on a 600px element forces the browser to rasterize a large offscreen layer, and on low-end phones it costs frames on every scroll.

Replacement: delete the elements. If the hero feels empty without them, the hero needs content: a product screenshot at 1:1 scale, a real photograph, a table of numbers, or a large set headline.

##### Radial glow behind the hero

```slop
.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at top, rgba(99, 102, 241, 0.35), transparent 60%);
}
```

The radial glow is the dark mode sibling of the mesh blob: an indigo ellipse fading out behind the headline on a near-black page. It says "launch page" and nothing else.

Replacement: none. A dark hero is `--paper` dark (`#141412`) with `--ink` dark text (`#ECE9E1`). Mark the end of the hero with a rule or a change of band.

##### Animated gradient button

```slop
.btn-shine {
  background: linear-gradient(90deg, #6366F1, #A855F7, #6366F1);
  background-size: 200% 100%;
  animation: shine 3s linear infinite;
}
@keyframes shine { to { background-position: -200% 0; } }
```

Also sold as "shimmer button", "border beam" and "rainbow button" in the component kits that grew out of the `magicui` and Aceternity collections. It animates `background-position`, which repaints on every frame, it runs forever, and it ignores `prefers-reduced-motion`. It breaks three motion rules from the authoring guide at once: animate only opacity and transform, stay at or under 150ms, and stop for reduced motion.

Replacement: a static fill and a 120ms tone change on hover.

```css
.btn-primary {
  background: var(--accent);
  color: var(--accent-ink);
  border: 1px solid var(--accent);
  transition: background-color 120ms ease-out;
}
.btn-primary:hover { background: #933511; border-color: #933511; } /* one step darker, see 2.3 */
@media (prefers-reduced-motion: reduce) {
  .btn-primary { transition: none; }
}
```

##### Fading divider

```slop
<div class="h-px w-full bg-gradient-to-r from-transparent via-gray-300 to-transparent"></div>
```

This one hides well because it is gray and thin. It is the most common gradient in generated layouts after the hero, and it is still a gradient. A line that fades out at both ends tells the reader the designer was not sure where the line should stop.

Replacement: a rule with defined ends. Either full width of the container, or a short fixed length.

```css
.divider { border: 0; border-top: 1px solid var(--rule); margin: 32px 0; }
.divider-short { width: 64px; border-top: 2px solid var(--ink); margin: 24px 0; }
```

##### Image scrim

```slop
.card-image::after {
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
}
```

The dark fade at the bottom of a photo, there to make white caption text legible. It darkens a third of every photo and the text contrast still depends on the image.

Replacement: move the text off the image. A caption bar below the photo has a known background and a known ratio.

```css
.figure { margin: 0; border: 1px solid var(--rule); }
.figure img { display: block; width: 100%; height: auto; }
.figure figcaption {
  padding: 8px 12px;
  background: var(--paper-2);
  border-top: 1px solid var(--rule);
  font: 400 14px/1.4 var(--font-sans);
  color: var(--ink-2);
}
```

If the text must sit on the image (a poster, a cover), set it on a solid block of `--ink` with `--paper` text. The ratio is then 16.0:1, whatever the photo does.

##### Conic spinners and gradient rings

A conic gradient rotated forever is the spinner of choice in generated code; aurora and beam backgrounds are the same idea at page size. Use a plain stroked SVG arc in `--ink-2`, rotated with `transform`, and a static "Loading" label under reduced motion. Delete the moving backgrounds.

#### Why the ban covers every hue

A warm orange to red gradient avoids the blue-violet tell, but it keeps every other cost:

1. Banding. An 8-bit display has 256 levels per channel. A gradient between two close colors across 1200px has fewer distinct steps than pixels, and visible bands appear every 20 to 40px on most laptop panels. Designers add noise to hide it, which adds a second banned effect.
2. Contrast. Text on a gradient has a different ratio at every pixel. Automated checkers cannot measure it and skip it.
3. Print. Browsers drop background colors and images when printing unless `print-color-adjust: exact` is set, so gradient-led pages print as white boxes with missing text.
4. Tone. A gradient implies light falling on a surface. The rest of this system draws flat surfaces separated by rules. A single gradient makes everything else look unfinished.
5. Drift. Allow one gradient and a year later there are twelve, drifting toward the default hues.

#### What to use instead

Every job a gradient does has a flat replacement.

| Job the gradient was doing | Flat replacement |
|---|---|
| Making the hero feel "designed" | Large serif headline (56px), a 2px `--ink` rule, a real image or a product screenshot |
| Separating sections | Alternate `--paper` and `--paper-2` bands, with a 1px `--rule` at each edge |
| Highlighting the recommended plan | 2px `--ink` border plus a text flag ("Picked by 61% of teams") |
| Making a button look clickable | A solid `--accent` fill with `--accent-ink` text, 40px tall, a verb label |
| Adding texture | Typography: numerals, a dateline, small caps labels, a visible grid of rules |
| Showing brand color | One full-bleed `--accent` block per page, used once |
| Making a dark page less flat | Tone steps: `#141412`, `#1E1D1A`, `#2A2925`, plus `--rule` lines |
| Drawing focus to a number | Size and weight: 40px tabular numerals in `--ink`, label in 12px `--ink-3` |

The most underused replacement is the full-bleed accent block. Use it once per page, for one thing, at full saturation, with no tint, fade or overlay:

```css
.callout-band {
  background: var(--accent);
  color: var(--accent-ink);
  padding: 48px 16px;
}
.callout-band a {
  color: var(--accent-ink);
  text-decoration-thickness: 2px;
  text-underline-offset: 4px;
}
```

White on `#B4441C` is 5.55:1, so body text and links in the band pass AA.

#### Review checklist for 2.2

- `rg -n 'gradient'` over the styles and templates returns zero lines outside comments and lint config.
- No `from-*`, `via-*` or `to-*` color stop classes remain.
- No element exists only to hold a blur or a glow.
- No text is `color: transparent` or `text-transparent`.
- Every section break is a rule, a tone step or white space with a defined size.
- Photos carry their own gradients; CSS adds none on top.

### 2.3 Building a palette that is not the default

A palette has three parts: a neutral scale that does most of the work, one accent, and four semantic colors. Build them in that order. Most screens are 90% neutral by area, so the neutral scale decides how the product feels far more than the accent does.

#### Step 1: neutrals with a temperature

A neutral scale with zero chroma looks like an unstyled browser. A neutral scale tinted blue looks like Tailwind. Pick a hue on purpose and keep the chroma low enough that the scale still reads as gray.

Rules:

- Pick a hue for the neutrals. Warm: OKLCH 60 to 95 (paper, cream, stone). Cool without blue: OKLCH 160 to 200 (green-gray, slate-green). Avoid 235 to 335 for neutrals with chroma above 0.012.
- Keep chroma between 0.004 and 0.012 for surfaces, and under 0.008 for text. Text with visible chroma looks muddy.
- Set lightness by role, in OKLCH L, not by eye.

The canonical scale, measured:

| Token | Hex | OKLCH | Role | Contrast on `--paper` |
|---|---|---|---|---|
| `--paper` | `#F7F5F0` | `0.970 0.007 89` | Page background | 1.00:1 |
| `--paper-2` | `#EFECE4` | `0.943 0.011 90` | Recessed: table header, sidebar, code | 1.08:1 |
| `--paper-3` | `#E5E1D6` | `0.910 0.015 90` | Pressed, selected | 1.20:1 |
| `--rule` | `#D9D5CB` | `0.873 0.014 89` | Default 1px border | 1.34:1 |
| `--ink-3` | `#6F6C64` | `0.531 0.013 90` | Tertiary text, placeholders, input borders | 4.81:1 |
| `--ink-2` | `#4A4843` | `0.402 0.009 89` | Secondary text | 8.38:1 |
| `--ink` | `#1A1A18` | `0.217 0.004 107` | Primary text, strong rules | 16.00:1 |

The surface steps are about 0.03 apart in L (0.970, 0.943, 0.910). Below 0.02, two adjacent surfaces look like the same color on an uncalibrated laptop panel. Above 0.05, the recessed surfaces start to look like separate cards. Hold to 0.025 to 0.035 per step.

To build a scale at a different temperature, keep the L values and change the hue:

```css
/* Spruce neutrals: same L steps as the canonical scale, hue 177 to 184 */
:root {
  --paper:   oklch(0.970 0.008 177); /* #F0F7F5 */
  --paper-2: oklch(0.943 0.012 178); /* #E4EFEC */
  --paper-3: oklch(0.910 0.015 182); /* #D7E5E2 */
  --rule:    oklch(0.873 0.016 177); /* #CBD9D5 */
  --ink-3:   oklch(0.525 0.014 184); /* #626D6B */
  --ink-2:   oklch(0.401 0.011 179); /* #424A48 */
  --ink:     oklch(0.214 0.005 174); /* #171A19 */
}
```

Ship the hex values, not only the `oklch()` calls, in any context where the color must match across tools (Figma, email, PDF export, native apps).

#### Step 2: one accent outside the blue-violet band

Pick one accent hue for the product. Not two, not a primary and a secondary. Every extra accent halves the meaning of the first.

The hue bands, in OKLCH hue degrees, with rough HSL equivalents:

| OKLCH hue | HSL hue (approx.) | Family | Status |
|---|---|---|---|
| 0 to 30 | 340 to 10 | Raspberry, crimson, red | Allowed. Red conflicts with `--bad`; see Newsprint below. |
| 30 to 60 | 10 to 30 | Vermilion, burnt orange, rust | Allowed. The canonical accent sits at 39. |
| 60 to 100 | 30 to 55 | Ochre, amber, mustard | Allowed. Conflicts with `--warn`; move warn toward orange. |
| 100 to 140 | 55 to 95 | Olive, moss, chartreuse | Allowed. Needs low L to pass contrast. |
| 140 to 170 | 95 to 160 | Green, forest | Allowed. Conflicts with `--ok`; move ok toward yellow-green or teal. |
| 170 to 215 | 160 to 190 | Teal, petrol, sea green | Allowed. |
| 215 to 235 | 190 to 200 | Cyan-blue | Caution. At chroma above 0.10 it reads as Tailwind `sky`. |
| 235 to 335 | 200 to 300 | Blue, indigo, violet, purple, fuchsia | Banned for accents, gradients and highlights. |
| 335 to 360 | 300 to 340 | Magenta, rose | Caution. Keep L below 0.55 so it reads as raspberry, not fuchsia. |

HSL hue does not map linearly to OKLCH hue, which is why the second column is approximate. Measure in OKLCH. A quick check in the browser console:

```js
// Paste in DevTools. Prints the OKLCH hue of any hex color.
function oklchHue(hex) {
  const c = hex.replace("#", "").match(/../g).map(h => parseInt(h, 16) / 255)
    .map(v => (v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4));
  const [r, g, b] = c;
  const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
  const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
  const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
  const A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s;
  const B = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s;
  return { chroma: Math.hypot(A, B).toFixed(3), hue: ((Math.atan2(B, A) * 180 / Math.PI) + 360) % 360 };
}
oklchHue("#B4441C"); // { chroma: "0.154", hue: 38.5... }
oklchHue("#6366F1"); // { chroma: "0.204", hue: 277.1... }
```

Accent rules:

- The accent text color passes 4.5:1 on `--paper`. The canonical `#B4441C` is 5.09:1.
- Text on the accent passes 4.5:1. White on `#B4441C` is 5.55:1.
- The accent appears on at most 10% of a screen by area. Primary button, current navigation item, links, one highlight. Not headings, not icons in a feature grid, not borders on every card.
- Brand marks may use colors outside these rules. The interface accent may not.

#### Step 3: derive the steps in OKLCH

A product needs five to ten steps of its accent: a wash for highlighted rows, a light step for selected backgrounds, the base, a hover step, a pressed step, and text steps for both themes. Derive them in OKLCH, holding the hue and adjusting lightness and chroma.

Do not derive steps in HSL. HSL lightness ignores how bright a hue looks. `hsl(60 100% 50%)` (`#FFFF00`) and `hsl(240 100% 50%)` (`#0000FF`) share the same L of 50%, yet the yellow has a contrast of 1.07:1 against white and the blue has 8.59:1. A ramp built with HSL lightness gives a different contrast at every hue, so swapping the accent breaks every text pairing in the system. OKLCH L tracks perceived lightness: those two colors measure 0.968 and 0.452.

The canonical accent ramp, hue held at 39, chroma rising to a peak at L 0.62 and tapering at both ends:

| Step | Hex | OKLCH | On `--paper` | White on it | Use |
|---|---|---|---|---|---|
| 100 | `#FFF2EE` | `0.970 0.015 39` | 1.00:1 | 1.09:1 | Row highlight wash |
| 200 | `#FEE1D7` | `0.931 0.035 39` | 1.14:1 | 1.24:1 | Selected background |
| 300 | `#FBC6B5` | `0.869 0.065 39` | 1.39:1 | 1.52:1 | Tag fill with `--ink` text |
| 400 | `#F2A48B` | `0.789 0.100 39` | 1.84:1 | 2.01:1 | Chart fill |
| 500 | `#E47E5D` | `0.699 0.135 39` | 2.59:1 | 2.82:1 | Chart fill, dark mode text |
| 600 | `#D15F37` | `0.620 0.154 39` | 3.57:1 | 3.89:1 | Large text only, icons |
| 700 | `#B4441C` | `0.535 0.154 39` | 5.09:1 | 5.55:1 | `--accent`: buttons, links |
| 800 | `#933511` | `0.459 0.135 39` | 6.99:1 | 7.61:1 | Hover |
| 900 | `#71280C` | `0.381 0.110 39` | 9.58:1 | 10.44:1 | Pressed, text on wash |
| 950 | `#4E1C0B` | `0.300 0.080 39` | 12.89:1 | 14.05:1 | Text on 200 and 300 |

Chroma tapers at the light end because a light color at full chroma falls outside the sRGB gamut and gets clipped unevenly by each browser. It tapers at the dark end because dark colors at high chroma look neon rather than deep. Peak chroma near L 0.55 to 0.65 holds for reds and oranges. For yellows and ochres, peak chroma sits higher, near L 0.80, and the hue should rotate 10 to 15 degrees toward orange as it darkens (from 90 to about 75), or the dark steps turn olive.

```css
:root {
  --orange-100: #FFF2EE;
  --orange-200: #FEE1D7;
  --orange-300: #FBC6B5;
  --orange-700: #B4441C;
  --orange-800: #933511;
  --orange-900: #71280C;
  --orange-950: #4E1C0B;

  --accent: var(--orange-700);
  --accent-hover: var(--orange-800);
  --accent-press: var(--orange-900);
  --accent-wash: var(--orange-100);
  --accent-ink: #FFFFFF;
}

@supports (color: oklch(0 0 0)) {
  :root {
    --accent: oklch(0.535 0.154 39);
    --accent-hover: oklch(0.459 0.135 39);
  }
}
```

Primitives (`--orange-700`) hold the values. Roles (`--accent`) point at primitives. Components only ever read roles. That is the full rule for color tokens, and 2.11 shows it in a Tailwind config.

#### Step 4: contrast targets

Use WCAG 2.2 contrast as the floor:

- Body text and any text under 24px regular or 18.66px bold: 4.5:1 against its actual background.
- Large text (24px regular, or 18.66px bold and up): 3:1.
- UI component boundaries and states, and graphics needed to understand content (input borders, checkbox outlines, focus indicators, chart marks, icons that carry meaning): 3:1 against adjacent colors.
- Aim for 7:1 on body text where the palette allows it. The canonical `--ink` and `--ink-2` both clear it.

Measure every pairing that ships, not just text on `--paper`. Text moves onto recessed and selected surfaces, and the ratio drops each time:

| Foreground | On `--paper` | On `--paper-2` | On `--paper-3` |
|---|---|---|---|
| `--ink` `#1A1A18` | 16.00:1 | 14.76:1 | 13.34:1 |
| `--ink-2` `#4A4843` | 8.38:1 | 7.74:1 | 6.99:1 |
| `--ink-3` `#6F6C64` | 4.81:1 | 4.44:1 | 4.01:1 |
| `--accent` `#B4441C` | 5.09:1 | 4.70:1 | 4.25:1 |
| `--ok` `#2F6B3A` | 5.87:1 | 5.42:1 | 4.89:1 |
| `--warn` `#8A6100` | 5.08:1 | 4.69:1 | 4.24:1 |
| `--bad` `#A3271F` | 6.72:1 | 6.20:1 | 5.61:1 |

Three failures fall out of this table, and each becomes a rule:

1. `--ink-3` fails on `--paper-2` (4.44:1) and `--paper-3` (4.01:1). Tertiary text appears only on `--paper`. On recessed or selected surfaces, use `--ink-2` for secondary and tertiary text alike.
2. `--accent` and `--warn` fail on `--paper-3`. A selected row does not contain accent-colored text or warn text at 14px. Use `--ink` for the text and put the meaning in an icon or a label.
3. `--rule` against `--paper` is 1.34:1. That is correct for a decorative divider and wrong for a form field. WCAG 1.4.11 asks for 3:1 on the boundary that identifies a control, so text inputs, selects and checkboxes use `border-color: var(--ink-3)` (4.81:1).

```css
.field input,
.field select,
.field textarea {
  background: var(--paper);
  color: var(--ink);
  border: 1px solid var(--ink-3);
  border-radius: var(--radius);
  box-shadow: none;
}
.field input::placeholder { color: var(--ink-3); opacity: 1; }
.field input:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
```

APCA, the candidate method for WCAG 3, rates `--ink-2` on `--paper` at about Lc 85 and `--ink-3` at about Lc 70. Under APCA guidance Lc 75 is the floor for body text columns, so `--ink-3` is fine for 14px metadata and captions and wrong for paragraphs. The same conclusion as WCAG 2: tertiary ink is for labels, never for prose.
