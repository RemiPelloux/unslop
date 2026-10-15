### 3.6 Responsive behavior

#### Breakpoints come from content

Set a breakpoint where the content breaks, not where a device sits. Open the page, drag the window from 320px to 1920px, and add a breakpoint only where something fails: a line passes 75 characters, a column drops under 280px, a table starts to scroll, a nav row wraps into two lines.

The usual result is two or three breakpoints, not five. Generated code ships Tailwind's whole ladder (`sm:` 640, `md:` 768, `lg:` 1024, `xl:` 1280, `2xl:` 1536) on every element, with a different font size, padding and column count at each step, and nobody has looked at the page at 900px.

Write breakpoints in `em`, not `px`. An `em` media query scales with the reader's default font size, so someone who set 20px in the browser gets the narrow layout earlier, which is what they need.

```css
/* 48em = 768px at the default 16px; 64em = 1024px */
@media (min-width: 48em) { ... }
@media (min-width: 64em) { ... }
```

Name the breakpoints by what changes, in a comment or a custom media name, not by device:

```css
/* two-column: text column + aside fit side by side at 66ch + 280px + gaps */
@media (min-width: 64em) { .article { grid-template-columns: minmax(0, 66ch) 280px; } }
```

#### Mobile-first rules

- Base styles are the narrow layout. `min-width` queries add columns and space as the window grows. A page built desktop-first with `max-width` overrides collects contradictory rules for every component.
- The page works at 320 CSS pixels wide with no horizontal page scroll. That is the WCAG 1.4.10 (Reflow) target, and it is also what 1280px looks like at 400 percent zoom. Only data tables, code blocks and maps may scroll sideways, inside their own container.
- Body text stays at 16px on phones. Do not shrink it to fit more; reflow instead.
- Inputs are at least 16px. iOS Safari zooms the page when focusing an input with a smaller font size, then leaves the reader zoomed in.
- Gutters are 16px at the narrow end and grow to 24px or 32px. Never 0.
- Use `100dvh` for full-height layouts. `100vh` on mobile browsers is the height with the toolbars hidden, so a `h-screen` hero hides its bottom 60 to 100px behind the address bar.
- For layouts that reach the screen edges on notched phones, add `viewport-fit=cover` and pad with safe-area insets.

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

```css
.app-header { padding-inline: max(var(--space-16), env(safe-area-inset-left)) max(var(--space-16), env(safe-area-inset-right)); }
.bottom-bar { padding-bottom: max(var(--space-8), env(safe-area-inset-bottom)); }
```

Never set `maximum-scale=1` or `user-scalable=no` in the viewport tag. It blocks pinch zoom for readers who need it.

#### Touch targets

| Standard | Minimum |
| --- | --- |
| WCAG 2.5.8 Target Size (Minimum), level AA | 24 by 24 CSS px, or enough spacing that a 24px circle around it touches no other target |
| WCAG 2.5.5 Target Size, level AAA | 44 by 44 CSS px |
| Apple Human Interface Guidelines | 44 by 44 pt |
| Material Design | 48 by 48 dp |

The rule in this handbook: every interactive element is at least 44 by 44px on touch devices and at least 24 by 24px everywhere. The visible element can be smaller than the hit area. A 20px icon button gets 12px of padding; a dense table row link gets an enlarged hit area with a pseudo-element.

```css
.icon-button {
  display: inline-grid;
  place-items: center;
  min-width: 44px;
  min-height: 44px;
  padding: 12px;
  border: 0;
  background: transparent;
  color: var(--ink-2);
  border-radius: var(--radius);
}
@media (pointer: fine) {
  .icon-button { min-width: 32px; min-height: 32px; padding: 6px; }
}

/* Extend the hit area of a small link without changing the layout */
.row-link { position: relative; }
.row-link::after { content: ""; position: absolute; inset: -10px -4px; }
```

The 6px padding in the fine-pointer rule is the one place a non-scale value is allowed: it centers a 20px icon in a 32px box. Keep it inside the component.

Adjacent targets need space between them, 8px at least. Two 44px buttons touching edge to edge cause mis-taps at the shared border.

#### Hover is optional

Touch screens have no hover. Anything revealed only on hover (row actions, card buttons, tooltips holding the only label) is invisible to a phone user and to keyboard users unless focus reveals it too.

```css
.row-actions { opacity: 1; }
@media (hover: hover) and (pointer: fine) {
  .row .row-actions { opacity: 0; }
  .row:hover .row-actions,
  .row:focus-within .row-actions { opacity: 1; }
}
```

Hide on hover-capable devices only, and always reveal on `:focus-within`.

#### Tables on small screens

A data table is the hardest element to make responsive, and the generated answer (turn every row into a card below 768px) is usually wrong: it destroys comparison down a column, which is the reason the data was in a table.

Choose by the number of columns and the task:

1. **Two to four columns, short values.** The table fits at 320px. Reduce cell padding to `4px 8px` and the text to 14px. Done.
2. **Five or more columns, comparison matters.** Keep the table, scroll it horizontally inside its own container, and stick the first column so each row keeps its label.
3. **Many columns, each row read alone (a contacts list, an orders list).** Show two or three priority columns and link each row to a detail view. A column picker lets the reader choose which columns stay.
4. **Key-value records.** Render as a definition list on narrow screens. This is the only case where the card reflow is right.

```html
<div class="table-scroll" role="region" aria-labelledby="orders-cap" tabindex="0">
  <table>
    <caption id="orders-cap">Orders, last 30 days</caption>
    <thead>
      <tr><th scope="col">Order</th><th scope="col">Customer</th><th scope="col" class="num">Total</th>
          <th scope="col">Status</th><th scope="col">Placed</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">#10482</th><td>Halvorsen AS</td><td class="num">1,240.00</td>
          <td>Shipped</td><td><time datetime="2026-03-12">12 Mar</time></td></tr>
    </tbody>
  </table>
</div>
```

```css
.table-scroll { overflow-x: auto; max-width: 100%; border: 1px solid var(--rule); }
.table-scroll:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.table-scroll table { border-collapse: separate; border-spacing: 0; min-width: 640px; width: 100%; }
.table-scroll :where(th, td) { padding: var(--cell-py) var(--cell-px); border-bottom: 1px solid var(--rule); white-space: nowrap; }
.table-scroll thead th { background: var(--paper-2); text-align: left; }
.table-scroll tbody th[scope="row"],
.table-scroll thead th:first-child {
  position: sticky;
  left: 0;
  background: var(--paper);
  border-right: 1px solid var(--rule);
}
.table-scroll thead th:first-child { background: var(--paper-2); z-index: 1; }
```

The `tabindex="0"`, the `role="region"` and the label make the scroll container reachable and announced for keyboard users, who otherwise cannot scroll it. The sticky first column needs an opaque background or the scrolled cells show through. The separator is a 1px rule, not a fading edge.

#### Navigation collapse without hamburger theater

The generated mobile nav: a hamburger icon that morphs into an X with a 300ms rotation, a full-height drawer that slides in from the right over a blurred backdrop, and links that fade in one by one with a 50ms stagger. Each step delays the reader by animation time and adds code that breaks focus management.

Rules:

- **Five or fewer top-level links: do not collapse.** Let them wrap onto a second row, or scroll the row horizontally with the current item scrolled into view. Most marketing sites have four links plus a sign-in.
- **App with three to five primary destinations: use a bottom bar** on phones, with icon plus text label for each item, 56px tall plus the safe-area inset.
- **More than that: one disclosure button labeled "Menu"** (a text label; a three-line icon is optional next to it), which opens a plain list directly below the header and pushes the page down. No overlay, no drawer, no stagger, no blur.
- The button has `aria-expanded` and `aria-controls`. Escape closes it and returns focus to the button.
- The open and close transition is 0 to 150ms, opacity only, or none.

```html
<header class="site-header">
  <a href="/" class="wordmark">Ledgerline</a>
  <button class="menu-button" aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav id="site-nav" class="site-nav" aria-label="Main">
    <ul>
      <li><a href="/product">Product</a></li>
      <li><a href="/pricing">Pricing</a></li>
      <li><a href="/docs">Docs</a></li>
      <li><a href="/changelog">Changelog</a></li>
      <li><a href="/login">Sign in</a></li>
    </ul>
  </nav>
</header>
```

```css
.site-header { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-16); padding: var(--space-12) var(--space-16); border-bottom: 1px solid var(--rule); }
.menu-button { margin-left: auto; min-height: 44px; padding: 0 var(--space-12); border: 1px solid var(--rule); background: var(--paper); border-radius: var(--radius); font: inherit; }
.site-nav { flex-basis: 100%; }
.site-nav[data-open="false"] { display: none; }
.site-nav ul { list-style: none; margin: 0; padding: 0; }
.site-nav a { display: block; padding: var(--space-12) 0; min-height: 44px; border-top: 1px solid var(--rule); text-decoration: none; }

@media (min-width: 48em) {
  .menu-button { display: none; }
  .site-nav, .site-nav[data-open="false"] { display: block; flex-basis: auto; margin-left: auto; }
  .site-nav ul { display: flex; gap: var(--space-24); }
  .site-nav a { border-top: 0; padding: var(--space-8) 0; }
}
```

```tsx
import { useEffect, useRef, useState } from "react";

export function useMenu() {
  const [open, setOpen] = useState(false);
  const buttonRef = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") { setOpen(false); buttonRef.current?.focus(); }
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [open]);
  return {
    buttonProps: { ref: buttonRef, "aria-expanded": open, onClick: () => setOpen(o => !o) },
    navProps: { "data-open": String(open) },
  };
}
```

Without JavaScript the nav should still be reachable. Either render it open by default and let the script hide it, or use a `<details>` element as the disclosure.

#### Images and media across sizes

- Every `<img>` has `width` and `height` attributes. The browser reserves the box before the file arrives.
- `max-width: 100%; height: auto;` on all images globally.
- Serve sizes with `srcset` and `sizes` so a phone does not download a 2400px screenshot (details in 3.8).
- Videos and embeds use `aspect-ratio` on a wrapper instead of the padding-top hack.

#### Failure cases

```slop
<h1 class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl xl:text-8xl">...</h1>
<div class="px-4 sm:px-6 md:px-8 lg:px-12 xl:px-16 2xl:px-24">...</div>
<div class="hidden md:block">Important pricing details</div>
```

Five font sizes and six paddings nobody reviewed, and content that exists only on desktop. If something is important on desktop, it is important on a phone; reflow it instead of hiding it.

### 3.7 Icons

#### One set, configured once

Use one SVG icon set across the product. Mixing sets is visible even to people who cannot name the cause: stroke weights, corner radii, end caps and optical sizes all differ.

Sets that work at the canonical spec (stroke 1.5px, 16 or 20px):

- **Lucide**: 24px grid, default stroke 2. Set `strokeWidth={1.5}` and `absoluteStrokeWidth` so the rendered stroke stays 1.5px when scaled down to 16 or 20px.
- **Heroicons outline**: 24px grid, stroke 1.5. There is also a 20px solid and 16px micro set; do not mix outline and solid in one interface except for selected states.
- **Phosphor**, regular weight: 256 unit grid; the regular weight renders close to 1.5px at 20px.
- **Tabler Icons**: 24px grid, default stroke 2; set the stroke to 1.5.
- **IBM Carbon icons**: drawn natively at 16, 20, 24 and 32px, solid shapes rather than strokes. Pair with Plex. If you choose Carbon, the stroke rule becomes "use the 16 and 20 masters".

Wrap the set in one component so size and stroke are decided in one place:

```tsx
import type { LucideIcon } from "lucide-react";

type Props = { icon: LucideIcon; size?: 16 | 20; label?: string };

export function Icon({ icon: Glyph, size = 16, label }: Props) {
  return (
    <Glyph
      width={size}
      height={size}
      strokeWidth={1.5}
      absoluteStrokeWidth
      aria-hidden={label ? undefined : true}
      aria-label={label}
      role={label ? "img" : undefined}
      focusable="false"
      className="icon"
    />
  );
}
```

Without a framework, use a sprite file and reference symbols:

```html
<svg class="icon" width="16" height="16" aria-hidden="true" focusable="false">
  <use href="/icons.svg#download"></use>
</svg>
```

```css
.icon {
  width: 16px;
  height: 16px;
  flex: none;
  stroke: currentColor;
  stroke-width: 1.5;
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
}
.icon path, .icon circle, .icon line, .icon rect { vector-effect: non-scaling-stroke; }
.icon--20 { width: 20px; height: 20px; }
```

`vector-effect: non-scaling-stroke` keeps the stroke at 1.5 screen pixels regardless of the viewBox scale, which is what `absoluteStrokeWidth` does in Lucide.

#### Sizes

| Icon | Next to text at | Where |
| --- | --- | --- |
| 16px | 12 to 16px | Inline in text, buttons at 14 to 16px, table cells, menu items, form field adornments |
| 20px | 16 to 21px | Toolbar and icon-only buttons, sidebar nav, page header actions, empty states |

Two sizes. Never 24px icons beside 14px labels, never 32px or 48px decorative icons in a feature grid. An empty state that needs a picture needs a screenshot or nothing, not a 64px icon.

Color comes from `currentColor`. Icons take the text color of their context: `--ink-2` in toolbars and nav, `--ink` when active, the semantic color only when the icon carries status beside a text label.

#### Alignment with text

Inside a button, nav item or menu row, use flex and center the icon on the text line:

```css
.button, .nav-item, .menu-item {
  display: inline-flex;
  align-items: center;
  gap: var(--space-8);
}
```

Inline in a sentence, the icon must sit on the text, not float above the baseline. A 1em icon with a small negative vertical offset lines up with lowercase and capital letters in most faces:

```css
.inline-icon { width: 1em; height: 1em; vertical-align: -0.125em; }
```

For pixel accuracy against the cap height, browsers that support the `cap` unit can center on it:

```css
@supports (height: 1cap) {
  .inline-icon { vertical-align: calc((1cap - 1em) / 2); }
}
```

Check alignment visually at 200 percent zoom. Most icon sets put the drawing in a 24 unit box with 2 units of padding, so an icon that looks one pixel too high usually is.

In lists with leading icons, align text lines to each other, not to the icon. Give the icon a fixed column and let wrapped lines start under the first word:

```css
.icon-list li { display: grid; grid-template-columns: 16px minmax(0, 1fr); column-gap: var(--space-8); align-items: start; }
.icon-list .icon { margin-top: 4px; } /* (24px line - 16px icon) / 2 */
```

#### Accessible names

- **Decorative icon next to a text label**: `aria-hidden="true"` and `focusable="false"`. The text is the name. Without `aria-hidden`, some screen readers announce "image" or read the SVG's title, doubling the label.
- **Icon-only button**: the button gets the name, the icon stays hidden. Add a visible tooltip on hover and focus with the same text.
- **Standalone meaningful icon** (a status icon in a table cell with no text): `role="img"` and `aria-label`, or a `<title>` as the first child of the SVG. Better: add the text.

```html
<button type="button" class="icon-button" aria-label="Download CSV">
  <svg class="icon icon--20" aria-hidden="true" focusable="false"><use href="/icons.svg#download"></use></svg>
</button>
```

Icon-only buttons are acceptable for close, search, more-actions, and toolbar actions that also have a keyboard shortcut and a tooltip. Everything else gets a text label. A row of five unlabeled icons in a toolbar is a guessing game.

#### Never emoji

Emoji are banned as icons, bullets, heading decorations, status indicators, button labels, empty-state art, toast prefixes and commit message prefixes. Reasons that hold in every one of those places:

- Emoji render from the operating system's color font. The same code point looks different on iOS, Android, Windows and Linux, and you cannot style it to match your tokens.
- They ignore `currentColor`, dark mode and forced-colors mode.
- Screen readers announce their names: a heading `:rocket: Getting started` is read as "rocket, Getting started".
- They are the fastest way to make a README, a changelog or a UI look generated, because language models add them by default to headings and lists.

```slop
## :sparkles: Features
## :rocket: Getting Started
## :hammer_and_wrench: Tech Stack

Status: :green_circle: Online   :red_circle: Down

git commit -m ":sparkles: feat: add export"
git commit -m ":bug: fix login redirect"
```

```text
## Features
## Getting started
## Stack

git commit -m "Add CSV export to the invoices list"
git commit -m "Fix login redirect when the session cookie is expired"
```

Commit messages are plain text: an imperative summary under 72 characters, optionally a conventional prefix (`fix:`, `feat:`) if the repository uses one, and a body that says why. No Gitmoji, no shortcodes.

Status uses text plus a shape plus color, so it survives grayscale, color vision deficiency and screen readers:

```html
<span class="status status--bad">
  <svg class="icon" aria-hidden="true" focusable="false"><use href="/icons.svg#x-circle"></use></svg>
  Failed
</span>
<span class="status status--ok">
  <svg class="icon" aria-hidden="true" focusable="false"><use href="/icons.svg#check-circle"></use></svg>
  Running since 09:12
</span>
```

```css
.status { display: inline-flex; align-items: center; gap: var(--space-4); font-size: var(--text-14); }
.status--ok  { color: var(--ok); }
.status--bad { color: var(--bad); }
```

No pulsing green dot. The "LIVE" or "Online" pill with an `animate-ping` dot is banned; it animates forever, carries no information beyond its text, and is a stock element of generated dashboards. "Running since 09:12" says more and does not move.

#### No icon in every heading

Generated docs and landing pages put an icon before every h2 and h3: a book for "Documentation", a shield for "Security", a gear for "Settings". The icon repeats the word next to it and pushes the heading text off the shared left edge. Headings are text. Use icons where they help recognition at speed: navigation, toolbars, file types, status.

#### No icons in colored circles or rounded squares

The feature-grid tell, copied from the Tailwind UI feature sections:

```slop
<div class="flex h-12 w-12 items-center justify-center rounded-lg bg-indigo-600">
  <BoltIcon class="h-6 w-6 text-white" aria-hidden="true" />
</div>
<h3 class="mt-4 text-lg font-semibold">Lightning fast</h3>
```

```slop
<div class="mx-auto flex size-16 items-center justify-center rounded-full bg-gradient-to-br from-purple-500 to-pink-500">
  <SparklesIcon class="size-8 text-white" />
</div>
```

A tinted container gives a generic glyph the visual weight of a logo, it is the same 48px square on every feature page on the web, and it says nothing about the feature. Drop the container and usually the icon too. If the item needs an anchor, use a number, a short label or a cropped screenshot of the feature itself:

```html
<li class="feature-item">
  <h3>Bank matching</h3>
  <p>Lines match on amount and reference. Unmatched lines wait in a review queue.</p>
  <img src="/img/review-queue-crop.png" alt="Review queue with three unmatched bank lines" width="640" height="320">
</li>
```

Same for avatars of icons in lists (an icon inside a 40px gray circle at the start of every notification row) and for "trust" rows (a shield in a circle, a lock in a circle, a globe in a circle). If a row needs a leading visual, the real one is better: the sender's avatar, the file type, the integration's logo at its own colors.

### 3.8 Images and illustration

#### Real images over generic art

Show the product. A real screenshot with real-looking data proves the product exists and shows what it does. The common substitutes each signal that nothing real was available:

- **3D blobs and glossy shapes**: iridescent spheres, chrome torus knots, floating glass cubes. Spline and Blender stock packs made these the default hero art for AI products.
- **Isometric illustrations**: a person on a giant laptop next to a floating chart. unDraw, Storyset, Humaaans and the "corporate Memphis" style (flat figures with tiny heads and long purple limbs) are recognized as free stock instantly.
- **AI-generated images**: plastic skin, symmetrical faces, six-fingered hands, glowing brains, robot hands touching human hands, neon circuit boards, abstract "neural network" meshes. Readers spot them, and some read them as a sign the rest of the content was generated too. Do not use them for people, products or places.
- **Background glows**: a blurred purple circle behind the hero (`absolute -top-40 h-96 w-96 rounded-full bg-purple-500 opacity-30 blur-3xl`). Decoration with no content.
- **Fake dashboards**: a screenshot built in Figma with round-number data, perfect upward lines and "John Doe" users. Readers notice that 12,345 and +23.5% repeat across every card.

```slop
<div class="relative">
  <div class="absolute -top-24 left-1/2 h-96 w-96 -translate-x-1/2 rounded-full bg-violet-500/30 blur-3xl"></div>
  <img src="/hero-3d-blob.png" class="animate-float" alt="">
</div>
```

#### Screenshots

- Capture at 2x device pixel ratio and serve 1x and 2x.
- Use realistic data: plausible names from several cultures, uneven numbers (1,284.17 not 1,000.00), a few empty cells, one error row if the product shows errors. Never "Lorem ipsum", never "John Doe", never "Acme Inc" in every row.
- Crop to the part that proves the claim. A full app window shrunk to 40 percent makes 14px text render at under 6px. Crop a region and show it at 100 percent or 75 percent.
- Match the theme: a light page shows light screenshots. If the site supports dark mode, provide both.
- Remove personal data, real email addresses and internal URLs.
- Update screenshots when the UI changes. A screenshot of the old navigation on the pricing page is a support ticket generator.

Frame a screenshot with a 1px border and the canonical radius. No shadow, no tilt, no fake browser chrome:

```css
.shot {
  display: block;
  max-width: 100%;
  height: auto;
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  background: var(--paper-2); /* shows while loading */
  box-shadow: none;
}
```

```slop
<div class="rounded-xl bg-gray-900/5 p-2 ring-1 ring-inset ring-gray-900/10 lg:-m-4 lg:rounded-2xl lg:p-4">
  <img src="/app-screenshot.png" class="rounded-md shadow-2xl ring-1 ring-gray-900/10" />
</div>
```

```slop
<div style="transform: perspective(2000px) rotateX(12deg) rotateY(-18deg) rotateZ(4deg)">
  <img src="/iphone-mockup.png" class="drop-shadow-2xl">
</div>
```

The first is the Tailwind UI screenshot frame: a ring, a padded tinted wrapper and `shadow-2xl`. The second is the floating device at an angle, which turns the product into a prop and makes every word in it unreadable. Show the screen flat.

Do not draw browser chrome (three colored circles and a fake address bar) around screenshots. It adds 40px of decoration and claims the product is a website, which the reader already knows. If the URL matters, put it in the caption.

#### Aspect ratios and sizing

Give every image box a ratio before the file loads, to prevent layout shift and to keep a grid of images even.

| Content | Ratio |
| --- | --- |
| Desktop app screenshot | 16:10 or the real window ratio |
| Cropped UI detail | whatever the crop is; set width and height attributes to match |
| Photos in articles | 3:2 |
| Hero photo, wide | 21:9 at most |
| Avatars, logos in a grid | 1:1 |
| Video | 16:9 |

```css
img, video { max-width: 100%; height: auto; }
.ratio-16-10 { aspect-ratio: 16 / 10; width: 100%; object-fit: cover; }
.avatar { aspect-ratio: 1; width: 32px; border-radius: 50%; object-fit: cover; }
```

`border-radius: 50%` on avatars is the one exception to the 4px radius ceiling: a circle is a shape, not a rounded corner.

Responsive sources, so a phone gets a phone-sized file:

```html
<picture>
  <source type="image/avif"
          srcset="/img/review-640.avif 640w, /img/review-1280.avif 1280w, /img/review-2400.avif 2400w"
          sizes="(min-width: 64em) 960px, 100vw">
  <img src="/img/review-1280.png"
       srcset="/img/review-640.png 640w, /img/review-1280.png 1280w, /img/review-2400.png 2400w"
       sizes="(min-width: 64em) 960px, 100vw"
       width="2400" height="1500"
       alt="Review queue listing three unmatched bank lines, each with suggested invoices"
       class="shot" loading="lazy" decoding="async">
</picture>
```

- The largest image above the fold (usually the hero screenshot) gets `fetchpriority="high"` and no `loading="lazy"`.
- Everything below the fold gets `loading="lazy"`.
- AVIF first, WebP or PNG fallback. PNG for screenshots with text if AVIF artifacts blur small type; check at 100 percent.

Light and dark screenshots, when the theme follows the system:

```html
<picture>
  <source srcset="/img/editor-dark.png" media="(prefers-color-scheme: dark)">
  <img src="/img/editor-light.png" width="1600" height="1000" alt="Editor with the outline panel open" class="shot">
</picture>
```

When the theme is a manual toggle (`data-theme`), media queries cannot see it. Render both images and hide one with `:root[data-theme="dark"] .only-light { display: none; }`.

#### Captions and alt text

Use `<figure>` and `<figcaption>` when the image needs context. The caption says what the reader is looking at and why it matters, in one or two sentences, left-aligned, 14px, `--ink-2`, 8px below the image.

```html
<figure class="figure">
  <img src="/img/approvals.png" width="1600" height="900" class="shot"
       alt="Approval panel showing a 4,200 euro purchase request with the remaining Q3 budget of 18,350 euros">
  <figcaption>Approvers see the remaining budget before they approve. Requests over the budget need a second approver.</figcaption>
</figure>
```

```css
.figure { margin: 0; }
.figure figcaption { margin-top: var(--space-8); font-size: var(--text-14); line-height: var(--lh-14); color: var(--ink-2); max-width: 66ch; }
```

Alt text describes what the image shows that the surrounding text needs: the numbers, the state, the action. Not "screenshot of our app" and not "image". Decorative images take `alt=""`. If an image is purely decorative, ask whether it should exist.

#### When illustration is right

Draw an illustration when it explains something a screenshot cannot: a data flow between systems, a sequence of states, a physical setup. Rules:

- Diagrams, not scenes. Boxes, lines, labels in the product's type, drawn in `--ink`, `--ink-2` and at most one accent.
- 1.5px strokes to match the icons, no fills beyond `--paper-2`, no gradients, no glow, no perspective.
- Real labels with real names (`orders-db`, `webhook worker`), not "Data" and "Cloud".
- Inline SVG with `currentColor` so the diagram follows the theme.
- One illustration style per product. If a team cannot commission one, use diagrams and screenshots only.

Photos of people: only real people who work on or use the product, with permission and names. A stock photo of a smiling team at a laptop on an "About" page says the opposite of what it intends.

Testimonials: real name, real role, real company, a real photo or initials. No stock headshots, no five-star rows, no generated portraits.
