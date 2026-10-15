## Part 3. Type, Space, Layout, Icons and Motion

This Part sets the physical rules of a page: which faces, which sizes, how much space, where things sit, which icons, which images, what moves and for how long. Every value here matches the canonical tokens in the authoring rules. When a number in a later Part disagrees with a number here, this Part wins for type, space and motion.

A generated interface is easy to spot from across the room because it is assembled from defaults: Inter at `font-extrabold`, `tracking-tight` on every heading, `py-24` on every section, `max-w-7xl mx-auto` around everything, three cards with an icon in an indigo rounded square, and a fade-up on scroll. None of those choices is wrong in isolation. Together they are a fingerprint. The chapters below replace each default with a decision and a number.

### 3.1 Typefaces

#### Why the default face reads as generated

Inter is a good typeface. The problem is frequency. `create-next-app` loaded Inter through `next/font/google` in its starter `layout.tsx` for several major versions, shadcn/ui examples render in it, most Figma UI kits ship with it, and code generators reach for it because it is the most common face in their training data. When a page uses Inter at 400 for body, Inter at 800 for a 72px headline and Inter at 500 for buttons, a reader who has seen a hundred such pages recognizes the template before reading a word.

The swap to the next most popular face does not fix it. Geist (the newer `create-next-app` default), Space Grotesk (the face of a thousand crypto and AI landing pages), Satoshi, General Sans and Clash Display from Fontshare, Manrope, Plus Jakarta Sans and DM Sans are the second tier of the same fingerprint. Choosing one of them because a template did is the same non-decision.

The second tell is the giant gradient headline:

```slop
<h1 class="text-6xl md:text-7xl font-extrabold tracking-tighter
           bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500
           bg-clip-text text-transparent">
  Build faster. Ship smarter.
</h1>
```

Four defaults stack here: the extrabold weight, the negative tracking pulled from Tailwind's `tracking-tighter` (-0.05em), the clipped gradient fill, and a two-fragment slogan. Replace all four:

```html
<h1 class="display">Payroll for teams of 5 to 200, filed in every US state</h1>
```

```css
.display {
  font-family: var(--font-sans);
  font-size: 56px;
  line-height: 1.15;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--ink);
  max-width: 20ch;
  text-wrap: balance;
}
```

#### Choosing a face

Pick a face for reasons you can write down. Check these properties before anything else, in this order:

1. **Glyph distinction.** Type `Il1 O0 rn m` at 14px. Capital I, lowercase l and the numeral 1 must differ. In product UI people read invoice numbers, API keys and coupon codes, so ambiguous glyphs cause support tickets.
2. **Figures.** The face needs tabular lining figures (`tnum`, `lnum` OpenType features). Without them, numbers in tables and timers wobble horizontally as they change.
3. **Language coverage.** If the product ships in Polish, Vietnamese or Turkish, the face needs those accents drawn, not synthesized. Check the character set before falling in love with a specimen.
4. **Weights you need, and no more.** Two weights cover almost all UI: 400 and 600. A third (500) is useful for button labels and table headers in dense UIs.
5. **x-height and width at 14px.** UI text is mostly 14px and 16px. A face with a small x-height (Garamond-style serifs, many geometric sans) reads small at those sizes and forces you to bump everything up a step.
6. **License.** SIL Open Font License (OFL) faces can be self-hosted and subset freely. Commercial faces need a web license sized to page views; read it before shipping.

#### Named alternatives

These are faces with a clear character, decent figures and broad coverage. None of them is a secret; they are simply less saturated than the template defaults.

Sans for UI and body:

- **IBM Plex Sans** (OFL). Slightly mechanical, distinct `l` with a tail, tabular figures, nine weights, Greek and Cyrillic, plus Plex Mono and Plex Serif in the same family. This handbook's canonical sans.
- **Source Sans 3** (OFL). Humanist, compact, very readable at 14px. Pairs with Source Serif 4 and Source Code Pro.
- **Public Sans** (OFL). Neutral, built for US government services, solid figures.
- **Atkinson Hyperlegible Next** (OFL). Drawn by the Braille Institute for low-vision readers. Exaggerated letter distinctions. Pick it when legibility is the brief.
- **Instrument Sans**, **Work Sans**, **Libre Franklin** (OFL). Each has more personality than Inter at display sizes.
- Commercial, when there is budget: Söhne, Untitled Sans, GT America, Graphik, ABC Diatype, Founders Grotesk.

Serif for long-form reading, docs and editorial headings:

- **Source Serif 4** (OFL). Has an optical size axis (`opsz`), so the same file draws sturdier shapes at 14px and finer ones at 56px. This handbook's canonical serif.
- **Literata** (OFL). Drawn for e-book reading, also has `opsz`.
- **Newsreader** (OFL). Editorial, with optical sizes.
- **Charter**. Ships with macOS and iOS as a system font; Bitstream Charter is free elsewhere. Sturdy at small sizes.
- **Spectral**, **Crimson Pro**, **EB Garamond** (OFL). Bookish. EB Garamond needs 18px or larger.

Monospace for code, IDs and fixed-width data:

- **IBM Plex Mono**, **JetBrains Mono**, **Source Code Pro**, **Iosevka** (all OFL). Berkeley Mono if there is budget.

#### Pairings that work

Pair faces with a job split, not for decoration. One face does UI, at most one more does long reading, and mono does code. Three families is the ceiling.

| Product | UI and headings | Long-form body | Code and IDs |
| --- | --- | --- | --- |
| Developer tool, dashboard | IBM Plex Sans | IBM Plex Sans | IBM Plex Mono |
| Docs site, knowledge base | IBM Plex Sans | Source Serif 4 at 18px | IBM Plex Mono |
| Publishing, essays | Source Serif 4 (headings 600) | Source Serif 4 | Source Code Pro |
| Government, health, forms | Public Sans or Atkinson Hyperlegible Next | same | system mono |
| Internal tool, zero budget | system UI stack | system UI stack | system mono stack |

Rules for pairing:

- Superfamilies (Plex, Source) pair without effort because the vertical metrics and figure styles were drawn together.
- Do not pair two sans faces. Inter for body and Space Grotesk for headings looks like two templates merged.
- Do not set UI chrome in a serif. Buttons, tabs, table headers and form labels stay in the sans.
- If you add a serif for headings only, use it at 32px and above. Serif headings at 21px next to sans body text look like a mistake.

#### System font stacks

A system stack costs zero bytes and zero layout shift. For internal tools, admin panels and anything behind a login where brand voice does not matter, use it and stop thinking about fonts.

```css
:root {
  --font-system: system-ui, -apple-system, "Segoe UI", Roboto,
                 "Helvetica Neue", "Noto Sans", Arial, sans-serif;
  --font-system-mono: ui-monospace, "SFMono-Regular", "Cascadia Code",
                      "Source Code Pro", Menlo, Consolas,
                      "DejaVu Sans Mono", monospace;
  /* Serif stacks that need no download */
  --font-system-serif-transitional: Charter, "Bitstream Charter",
                                    "Sitka Text", Cambria, serif;
  --font-system-serif-oldstyle: "Iowan Old Style", "Palatino Linotype",
                                "URW Palladio L", P052, serif;
}
```

Facts about the system stack you need to plan around:

- `system-ui` resolves to San Francisco on Apple platforms, Segoe UI on Windows, Roboto or Noto Sans on Android and whatever the desktop sets on Linux. Your layout must tolerate width differences of about 5 to 8 percent between them. Never size a button to fit its label exactly.
- On Windows, Segoe UI's figures are proportional by default; add `font-variant-numeric: tabular-nums` wherever numbers align.
- Tailwind's default `font-sans` appends `"Apple Color Emoji", "Segoe UI Emoji"` to the stack. Remove them. This handbook bans emoji in the interface, and the emoji fonts in the stack only matter if you allow them.

#### The canonical font tokens

Use these three tokens everywhere. Never write a family name directly in a component.

```css
:root {
  --font-sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-serif: "Source Serif 4", Georgia, "Times New Roman", serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}

html {
  font-family: var(--font-sans);
  font-size: 100%;          /* respect the reader's browser setting */
  font-synthesis: none;     /* no faux bold or faux italic */
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
}

code, kbd, samp, pre { font-family: var(--font-mono); font-size: 0.875em; }
.prose { font-family: var(--font-serif); }
```

Wire the same tokens into Tailwind so utility classes cannot drift:

```js
// tailwind.config.js (v3)
module.exports = {
  theme: {
    fontFamily: {
      sans: ["var(--font-sans)"],
      serif: ["var(--font-serif)"],
      mono: ["var(--font-mono)"],
    },
  },
};
```

```css
/* Tailwind v4: tokens live in CSS */
@theme {
  --font-sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-serif: "Source Serif 4", Georgia, "Times New Roman", serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}
```

`font-size: 100%` on `html` matters. Setting `html { font-size: 62.5% }` so that 1rem equals 10px breaks third-party components that assume 16px and it fights readers who raised their default size. Keep the root at the browser default and write rem values that map to the scale (0.875rem is 14px).

`font-synthesis: none` matters too. If you load only 400 and 600, a stray `font-bold` (700) makes the browser smear the 600 outlines into a fake bold. With synthesis off, it renders the nearest real weight instead.

#### Loading fonts without layout shift

A web font that arrives late causes two failures: invisible text (FOIT) while it loads, then a reflow when it replaces the fallback because the two faces have different widths and vertical metrics. Both are visible to users and the reflow counts toward Cumulative Layout Shift. Fix both.

Rules:

1. **Self-host WOFF2.** Do not hotlink a font CDN in production. Third-party font requests add a DNS lookup and a TLS handshake on the critical path, and some EU regulators have ruled that loading Google Fonts from Google's servers leaks visitor IP addresses. `next/font` and Fontsource both self-host at build time.
2. **Subset.** Ship the Latin subset by default and split other scripts with `unicode-range` so they load only when the page uses them. A static Latin subset of one weight is typically 15 to 30 KB as WOFF2. A full multilingual file can be 150 KB or more.
3. **Preload what is above the fold, and only that.** Usually one or two files: body 400 and heading 600. Every preload competes with the CSS and the hero image.
4. **Pick `font-display` on purpose.** `swap` shows fallback text immediately and swaps when the font arrives. `optional` gives the font about 100ms; if it misses, the page keeps the fallback for that view and the font is cached for the next one. Use `optional` for body text on content sites where a swap mid-read is worse than a fallback. Use `swap` with metric overrides (below) everywhere else. Never use `block`.
5. **Match fallback metrics.** Declare a fallback face built from a local system font with `size-adjust`, `ascent-override`, `descent-override` and `line-gap-override`, so the fallback occupies the same box as the web font. The swap then changes letter shapes but moves nothing.

```css
@font-face {
  font-family: "IBM Plex Sans";
  src: url("/fonts/plex-sans-400-latin.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
                 U+02DA, U+02DC, U+2000-206F, U+20AC, U+2122, U+2212, U+FEFF;
}

@font-face {
  font-family: "IBM Plex Sans";
  src: url("/fonts/plex-sans-600-latin.woff2") format("woff2");
  font-weight: 600;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
                 U+02DA, U+02DC, U+2000-206F, U+20AC, U+2122, U+2212, U+FEFF;
}

/* Metric-matched fallback. Generate these four numbers with a tool
   (Capsize metrics, fontaine, or next/font's adjustFontFallback).
   The values below show the shape of the rule; measure your own files. */
@font-face {
  font-family: "IBM Plex Sans Fallback";
  src: local("Arial");
  size-adjust: 101.5%;
  ascent-override: 101%;
  descent-override: 27%;
  line-gap-override: 0%;
}

:root {
  --font-sans: "IBM Plex Sans", "IBM Plex Sans Fallback", system-ui,
               -apple-system, "Segoe UI", sans-serif;
}
```

Preload the two files in the document head. The `crossorigin` attribute is required even for same-origin fonts; without it the browser fetches the file twice.

```html
<link rel="preload" href="/fonts/plex-sans-400-latin.woff2"
      as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/plex-sans-600-latin.woff2"
      as="font" type="font/woff2" crossorigin>
```

In Next.js, `next/font` does the subsetting, self-hosting, preloading and fallback metrics for you. Use it and point it at the canonical variable:

```tsx
// app/fonts.ts
import { IBM_Plex_Sans, IBM_Plex_Mono, Source_Serif_4 } from "next/font/google";

export const sans = IBM_Plex_Sans({
  subsets: ["latin"],
  weight: ["400", "600"],
  display: "swap",
  variable: "--font-plex-sans",
});

export const mono = IBM_Plex_Mono({
  subsets: ["latin"],
  weight: ["400"],
  display: "swap",
  variable: "--font-plex-mono",
});

export const serif = Source_Serif_4({
  subsets: ["latin"],
  weight: ["400", "600"],
  style: ["normal", "italic"],
  display: "swap",
  variable: "--font-source-serif",
  preload: false, // only docs pages use it
});
```

```tsx
// app/layout.tsx
import { sans, mono, serif } from "./fonts";
import "./globals.css";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${sans.variable} ${mono.variable} ${serif.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

```css
/* globals.css: the canonical tokens read from next/font's variables */
:root {
  --font-sans: var(--font-plex-sans), system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: var(--font-plex-mono), ui-monospace, "SFMono-Regular", Menlo, monospace;
  --font-serif: var(--font-source-serif), Georgia, "Times New Roman", serif;
}
```

Check the result in the browser: open DevTools, throttle to Slow 4G, reload, and watch the hero. If any line rewraps when the font arrives, the fallback metrics are wrong.

#### Weights to ship

| Face | Ship | Use |
| --- | --- | --- |
| Sans | 400, 600 | Body and UI at 400; headings, button labels, table headers, emphasis at 600 |
| Sans (dense apps) | add 500 | Button labels and nav items when 600 is too loud at 14px |
| Serif (docs, essays) | 400, 400 italic, 600 | Body, emphasis, headings |
| Mono | 400 | Code, IDs, keyboard keys |

Hard limits:

- At most five font files on any page, and at most two preloaded.
- Never ship 100, 200 or 300 for text. Thin weights at 14px to 16px on a light background fall below legible stroke contrast on non-Retina screens, and `font-light text-gray-500` body copy is a common template tell.
- Never ship 800 or 900. `font-extrabold` and `font-black` headlines are the clearest single marker of a generated landing page. Size and space carry hierarchy; weight beyond 600 shouts.
- Italic only for the serif in long-form text. UI rarely needs italic; when it does (a variable name in a sentence, a book title), the browser's synthesized italic is turned off, so either ship the file or use a different signal.

A variable font file (one file, all weights) is worth it when you need three or more weights of the same style, or an optical size axis. For two weights, two static subsets are usually smaller than one variable file. Check the byte counts; do not assume.

#### Failure cases

```slop
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<body class="font-sans antialiased">
  <h1 class="text-7xl font-black tracking-tighter">The future of work</h1>
  <p class="text-lg font-light text-gray-500">Experience seamless collaboration.</p>
```

Nine weights requested from a third-party origin, a 900-weight headline with -0.05em tracking, light gray body text at 300. Every choice is a framework default or a copied snippet.

```slop
body { font-family: 'Poppins', sans-serif; }
h1, h2, h3 { font-family: 'Space Grotesk', sans-serif; }
.hero-title { font-family: 'Clash Display'; }
```

Three display-oriented sans faces with no job split and no fallback stack. If any file fails to load, the browser falls back to the generic family with entirely different metrics.

```css
/* Fixed: one family, two weights, a real fallback stack */
body { font-family: var(--font-sans); font-weight: 400; }
h1, h2, h3 { font-weight: 600; }
```

### 3.2 Type scale and hierarchy

#### The canonical scale

Nine sizes, in pixels: 12, 14, 16, 18, 21, 24, 32, 40, 56. Body is 16. Nothing else. No 13px, no 15px, no 20px, no 36px, no 48px, no 60px, no 72px. If a design needs a size that is not on the list, the design needs another look, not another size.

Each size has a job:

| Token | px | rem | Line height (px) | Role |
| --- | --- | --- | --- | --- |
| `--text-12` | 12 | 0.75 | 16 | Captions, timestamps, uppercase labels, badges, footnotes |
| `--text-14` | 14 | 0.875 | 20 | Secondary UI text, table cells, form help, nav items in dense apps |
| `--text-16` | 16 | 1 | 24 | Body text, form inputs, buttons, default UI |
| `--text-18` | 18 | 1.125 | 28 | Long-form body (docs, articles), lead paragraph |
| `--text-21` | 21 | 1.3125 | 28 | h4, card titles, dialog titles |
| `--text-24` | 24 | 1.5 | 32 | h3, page titles inside an app |
| `--text-32` | 32 | 2 | 40 | h2, section headings on marketing and docs pages |
| `--text-40` | 40 | 2.5 | 48 | h1 on docs and app landing screens; page h1 on mobile |
| `--text-56` | 56 | 3.5 | 64 | Display: one per page at most, desktop marketing h1 only |

```css
:root {
  --text-12: 0.75rem;   --lh-12: 1rem;
  --text-14: 0.875rem;  --lh-14: 1.25rem;
  --text-16: 1rem;      --lh-16: 1.5rem;
  --text-18: 1.125rem;  --lh-18: 1.75rem;
  --text-21: 1.3125rem; --lh-21: 1.75rem;
  --text-24: 1.5rem;    --lh-24: 2rem;
  --text-32: 2rem;      --lh-32: 2.5rem;
  --text-40: 2.5rem;    --lh-40: 3rem;
  --text-56: 3.5rem;    --lh-56: 4rem;
}

body { font-size: var(--text-16); line-height: var(--lh-16); color: var(--ink); }
h1 { font-size: var(--text-40); line-height: var(--lh-40); font-weight: 600; }
h2 { font-size: var(--text-32); line-height: var(--lh-32); font-weight: 600; }
h3 { font-size: var(--text-24); line-height: var(--lh-24); font-weight: 600; }
h4 { font-size: var(--text-21); line-height: var(--lh-21); font-weight: 600; }
small, .caption { font-size: var(--text-12); line-height: var(--lh-12); }
```

Every line height lands on a multiple of 4px, so text blocks sit on the same 4px grid as the spacing scale in 3.4. The ratios fall out of that: 1.5 at 16px, about 1.43 at 14px, 1.33 at 12px, 1.25 at 24px and 32px, 1.2 at 40px, about 1.14 at 56px. Body runs at 1.5; headings run between 1.15 and 1.25, as the canonical tokens require. Where a ratio sits a hair outside, the 4px grid wins.

To restrict Tailwind to the scale, replace the theme instead of extending it, so `text-5xl` and its relatives stop existing:

```js
// tailwind.config.js (v3): replace, do not extend
module.exports = {
  theme: {
    fontSize: {
      12: ["0.75rem", { lineHeight: "1rem" }],
      14: ["0.875rem", { lineHeight: "1.25rem" }],
      16: ["1rem", { lineHeight: "1.5rem" }],
      18: ["1.125rem", { lineHeight: "1.75rem" }],
      21: ["1.3125rem", { lineHeight: "1.75rem" }],
      24: ["1.5rem", { lineHeight: "2rem" }],
      32: ["2rem", { lineHeight: "2.5rem", letterSpacing: "-0.01em" }],
      40: ["2.5rem", { lineHeight: "3rem", letterSpacing: "-0.01em" }],
      56: ["3.5rem", { lineHeight: "4rem", letterSpacing: "-0.015em" }],
    },
  },
};
```

Now `text-16` and `text-32` are the only spellings, and a reviewer sees the pixel value in the class name.

#### Hierarchy with few levers

Hierarchy comes from four levers, used in this order: size, weight, space, color. Use the fewest that make the order unambiguous.

- Adjacent heading levels differ by at least one scale step and usually two. h2 at 32 over h3 at 24 reads as two levels. h2 at 24 over h3 at 21 does not.
- Headings are 600. Body is 400. Do not mix 500, 600 and 700 among headings to fake extra levels.
- A heading sits closer to the text it introduces than to the text above it (space above about twice the space below; see 3.4).
- Color is the last lever. `--ink` for headings and body, `--ink-2` for secondary text, `--ink-3` for metadata. Never color a heading with the accent to make it important.
- Keep the visual level independent from the HTML level. A sidebar's "Filters" heading is an `h2` for the outline but may render at 14px 600. Use classes for looks and elements for structure.

```html
<aside aria-labelledby="filters-h">
  <h2 id="filters-h" class="label">Filters</h2>
  ...
</aside>
```

```css
.label {
  font-size: var(--text-14);
  line-height: var(--lh-14);
  font-weight: 600;
  color: var(--ink);
}
```

A complete app screen often needs only four sizes: 24 for the page title, 16 for body and controls, 14 for tables and secondary text, 12 for metadata. If a single screen uses seven sizes, collapse it.

#### Letter spacing

Tailwind's `tracking-tight` is -0.025em and `tracking-tighter` is -0.05em. Generated pages apply one of them to every heading and sometimes to body text, because the Tailwind UI hero examples do. At 16px, -0.025em removes 0.4px between every pair of letters, which closes counters and makes `rn` read as `m`.

The rules:

| Size | letter-spacing |
| --- | --- |
| 12px uppercase labels | 0.06em |
| 12px to 21px, sentence case | 0 |
| 24px | 0 to -0.005em |
| 32px and 40px | -0.01em |
| 56px | -0.015em, never past -0.02em |
| Monospace at any size | 0 |

Large type needs a little negative tracking because fonts are spaced for text sizes, and the gaps grow optically as size grows. A face with optical sizes (Source Serif 4 with `font-optical-sizing: auto`) already corrects for this, so leave its tracking at 0. Test negative tracking against the actual glyphs: at 56px, -0.015em is 0.84px, which is enough.

```slop
<h2 class="text-4xl font-bold tracking-tight">Everything you need</h2>
<p class="mt-6 text-lg leading-8 tracking-tight text-gray-600">...</p>
```

```css
h2 { font-size: var(--text-32); line-height: var(--lh-32); letter-spacing: -0.01em; }
p  { letter-spacing: 0; }
```

#### Measure

Prose runs at most 66ch wide. The comfortable range is 45 to 75 characters per line; 66 is the classic target. The `ch` unit is the advance width of the digit 0, and most lowercase letters are narrower than a zero, so `66ch` usually fits somewhat more than 66 average characters. For long reading, that slight overshoot is fine; do not go wider.

Apply the measure to the text element, not to the page container. A table or a code block in the same column may use the full width.

```css
.prose > :where(p, ul, ol, blockquote, h2, h3, h4) { max-width: 66ch; }
.prose > :where(pre, table, figure) { max-width: 100%; }

/* Headings get a narrower measure so they break into balanced lines */
.prose h1, .prose h2 { max-width: 24ch; text-wrap: balance; }
```

Failure cases:

- Body text running the full 1280px container: about 180 characters per line at 16px. Readers lose their place on the return sweep.
- Centered paragraphs constrained to `max-w-2xl` (672px) under a centered hero: the measure is fine, the ragged left edge is not (see 3.3).
- A two-column layout where each column is 30ch: fine for a sidebar list, too narrow for paragraphs, and it triggers rivers of space if justified.

#### Heading sizes on landing pages

The landing page h1 is 40px on narrow screens and 56px on wide ones. Nothing larger. The 72px, 96px and 128px headlines (`text-7xl`, `text-8xl`, `text-9xl`) on generated landing pages exist because the hero has nothing to say, so the type has to fill the space. A headline with real content needs fewer pixels.

The copy pattern matters as much as the size. The generated hero is two to four words plus a buzzword:

```slop
<h1 class="text-7xl font-extrabold">Email, Reimagined.</h1>
<h1 class="text-8xl font-bold">The Future of Finance</h1>
<h1 class="text-7xl">Work smarter, not harder.</h1>
```

Write a sentence that names what the product does and for whom, 6 to 14 words, and set it at the scale's display size with a narrow measure so it breaks into two or three balanced lines:

```html
<header class="hero">
  <h1>Shared inboxes for support teams that answer in more than one language</h1>
  <p class="lead">Route by language, translate replies in place, and keep one thread
     per customer. Works with Gmail and Outlook.</p>
</header>
```

```css
.hero h1 {
  font-size: clamp(var(--text-40), 2rem + 2vw, var(--text-56));
  line-height: 1.15;
  font-weight: 600;
  letter-spacing: -0.01em;
  max-width: 22ch;
  text-wrap: balance;
}
.hero .lead {
  font-size: var(--text-18);
  line-height: var(--lh-18);
  color: var(--ink-2);
  max-width: 52ch;
  margin-top: 16px;
}
```

About the `clamp()`: the middle term mixes `rem` and `vw` on purpose. A size made only of `vw` does not grow when the reader zooms the page, which fails WCAG 1.4.4 (Resize Text). Anchoring to rem keeps zoom working. The two ends are scale values, so the fluid size never lands outside the scale at the extremes.

Only the h1 is fluid. h2 and below use fixed scale values with one breakpoint, if any. A page where every heading uses its own `clamp()` produces sizes like 27.4px that belong to no scale.

#### Numerals

Numbers have their own typography. Three OpenType features cover nearly every case:

- `tabular-nums`: every digit has the same width. Use in tables, prices that update, timers, counters, version lists, anything stacked vertically or changing in place.
- `lining-nums`: digits sit on the baseline at cap height. Default in most sans faces. Use in UI.
- `oldstyle-nums`: digits with ascenders and descenders that sit like lowercase letters. Use in serif long-form prose so years and numbers in a sentence do not shout. Source Serif 4 and Literata support them.

Plus `slashed-zero` for IDs, codes and keys, where O and 0 must not be confused.

```css
table, .num, time, .price, .duration { font-variant-numeric: tabular-nums lining-nums; }
.prose { font-variant-numeric: oldstyle-nums proportional-nums; }
.prose table { font-variant-numeric: tabular-nums lining-nums; }
.id, .api-key, .order-number { font-variant-numeric: tabular-nums slashed-zero; }

td.num, th.num { text-align: right; }
```

Right-align numeric columns so the place values line up, and align the column header to match. Keep the same number of decimals down a column: `12.50`, `8.00`, `130.25`, not `12.5`, `8`, `130.25`.

If a face lacks `tnum`, `font-variant-numeric` silently does nothing. Check in the browser: type `1111` over `8888` in a table cell and compare widths.

#### Small caps

Real small caps are capitals drawn at about x-height with stroke weights matched to the lowercase. Use them for acronyms in running serif text (NASA, HTML, API) so a sentence full of acronyms does not look like shouting.

```css
.prose abbr { font-variant-caps: all-small-caps; letter-spacing: 0.02em; }
```

Use them only when the face contains the `smcp` and `c2sc` features. Source Serif 4 does. Many sans faces do not. When the feature is missing, the browser synthesizes small caps by shrinking full capitals, which makes thin, spindly letters that look broken next to the lowercase. In that case, leave the acronyms as plain capitals.

#### Uppercase labels

Uppercase text is a tool for short labels, not a voice. Tailwind UI's feature sections open with a small uppercase "eyebrow" in the accent color above every heading (`text-base font-semibold leading-7 text-indigo-600` reading "Deploy faster"), and generated pages copy it onto every section. One eyebrow on one page is a choice. Six is a template.

Rules for uppercase:

- 12px only, weight 500 or 600, `letter-spacing: 0.06em`, color `--ink-2` or `--ink-3`. Never the accent.
- Three words at most. Never a sentence, never a heading above 14px, never body copy, never a button in a form.
- Uppercase via CSS `text-transform`, with the source text in sentence case. Some screen readers spell out text typed in capitals letter by letter, and copy-paste should give the reader normal text.
- Good uses: table column headers in dense data tables, a section label in a sidebar group, metadata keys in a definition list, the label on a keyboard shortcut.

```css
.overline {
  font-size: var(--text-12);
  line-height: var(--lh-12);
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink-3);
}
```

```html
<dl class="meta">
  <div><dt class="overline">Region</dt><dd>eu-west-1</dd></div>
  <div><dt class="overline">Created</dt><dd><time datetime="2026-03-14">14 Mar 2026</time></dd></div>
</dl>
```

```slop
<p class="text-sm font-semibold uppercase tracking-widest text-indigo-600">Why choose us</p>
<h2 class="mt-2 text-4xl font-bold tracking-tight">Everything you need to scale</h2>
```

`tracking-widest` is 0.1em, the accent color makes the label compete with the heading, and the label says nothing the heading does not.

#### Weight and color for emphasis

- Inside a paragraph, emphasis is `<em>` (italic in serif text) or `<strong>` at 600. One or two per paragraph.
- Do not bold a key phrase in every paragraph. Generated copy does this so skimmers find the "point", and the result is a page where nothing stands out.
- Do not color words in a sentence. A headline with one word in the accent color (`<span class="text-indigo-600">faster</span>`) is a template pattern.
- Secondary text goes to `--ink-2` at the same size, or one step down to 14px. Not both plus lighter weight.

#### Failure cases in one block

```slop
<section class="py-24 text-center">
  <p class="text-sm font-semibold uppercase tracking-wider text-indigo-600">Features</p>
  <h2 class="mt-2 text-5xl font-extrabold tracking-tight text-gray-900">
    Supercharge your <span class="text-indigo-600">workflow</span>
  </h2>
  <p class="mx-auto mt-6 max-w-2xl text-xl leading-8 text-gray-500">
    Our platform helps you do more with less, faster than ever before.
  </p>
</section>
```

Count the defaults: accent eyebrow, 48px extrabold with negative tracking, an accent-colored word, centered 20px gray lead, 96px vertical padding. The fix is not a new combination of the same utilities. It is a heading that states something, at a scale size, left-aligned on the page's edge:

```html
<section class="section">
  <h2>Approvals, budgets and receipts in the same place</h2>
  <p>Managers approve from the email notification. Finance sees the budget
     impact before the money moves.</p>
</section>
```

```css
.section h2 { font-size: var(--text-32); line-height: var(--lh-32); letter-spacing: -0.01em; max-width: 24ch; }
.section p  { font-size: var(--text-18); line-height: var(--lh-18); color: var(--ink-2); max-width: 60ch; margin-top: 16px; }
```
