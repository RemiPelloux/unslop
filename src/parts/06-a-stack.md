## Part 6. Stack Setup and Full Page Rebuilds

This part turns the rules into files. Chapters 6.1 to 6.7 are configuration: a base stylesheet, Tailwind configs for v3 and v4, replacement shadcn/ui components, a token file, lint rules, and an instruction block for coding agents. Paste them in, then delete what your project does not use.

Chapters 6.8 to 6.19 take twelve common pages, show the version a code generator produces on default settings, list every tell in it, and rebuild it. The rebuilt pages assume the base stylesheet from 6.1 is loaded, so each one carries only its page-specific CSS.

### 6.1 Base stylesheet

Load this file first, before any component CSS. It defines the canonical tokens, resets browser defaults, and styles bare HTML so that a page with no classes already follows the rules. It is about 9 KB unminified and has no dependencies.

Load the three fonts with one request. Ask for the weights you use and nothing else:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<link rel="stylesheet" href="/css/unslop-base.css">
```

```css
/* unslop-base.css. Load before every other stylesheet. */

/* 1. Tokens ------------------------------------------------------------ */
:root {
  --paper: #F7F5F0;
  --paper-2: #EFECE4;
  --paper-3: #E5E1D6;
  --ink: #1A1A18;
  --ink-2: #4A4843;
  --ink-3: #6F6C64;
  --rule: #D9D5CB;
  --rule-strong: #1A1A18;
  --accent: #B4441C;
  --accent-ink: #FFFFFF;
  --ok: #2F6B3A;
  --warn: #8A6100;
  --bad: #A3271F;
  --focus: #1A1A18;
  --radius: 2px;
  --font-sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-serif: "Source Serif 4", Georgia, "Times New Roman", serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;

  --s1: 4px;  --s2: 8px;  --s3: 12px; --s4: 16px; --s5: 24px;
  --s6: 32px; --s7: 48px; --s8: 64px; --s9: 96px; --s10: 128px;

  --t-12: 12px; --t-14: 14px; --t-16: 16px; --t-18: 18px; --t-21: 21px;
  --t-24: 24px; --t-32: 32px; --t-40: 40px; --t-56: 56px;

  --measure: 66ch;
  --page: 1120px;
  --control: 40px;
  --dur: 120ms;
  color-scheme: light;
}

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
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
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
    color-scheme: dark;
  }
}

/* 2. Reset ------------------------------------------------------------- */
*, *::before, *::after { box-sizing: border-box; }
* { margin: 0; }
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
body {
  min-height: 100vh;
  background: var(--paper);
  color: var(--ink);
  font: 400 var(--t-16)/1.5 var(--font-sans);
  font-kerning: normal;
}
img, picture, svg, video, canvas { display: block; max-width: 100%; height: auto; }
input, button, textarea, select { font: inherit; color: inherit; letter-spacing: inherit; }
p, li, h1, h2, h3, h4, h5, h6, td, th { overflow-wrap: break-word; }
::selection { background: var(--paper-3); color: var(--ink); }
[hidden] { display: none !important; }

/* 3. Typography -------------------------------------------------------- */
h1, h2, h3, h4 { font-weight: 600; color: var(--ink); text-wrap: balance; }
h1 { font-size: var(--t-40); line-height: 1.15; letter-spacing: -0.01em; }
h2 { font-size: var(--t-32); line-height: 1.2; }
h3 { font-size: var(--t-24); line-height: 1.25; }
h4 { font-size: var(--t-18); line-height: 1.25; }
h5, h6 { font-size: var(--t-16); line-height: 1.25; font-weight: 600; }
.display { font-size: var(--t-56); line-height: 1.15; letter-spacing: -0.015em; }
p, ul, ol, dl, blockquote, pre, table, figure { max-width: var(--measure); }
ul, ol { padding-left: 1.25em; }
li + li { margin-top: var(--s1); }
dt { font-weight: 600; }
dd { margin-left: 0; color: var(--ink-2); }
blockquote { border-left: 2px solid var(--rule-strong); padding-left: var(--s4); }
small, .small { font-size: var(--t-14); }
.lede { font-size: var(--t-18); color: var(--ink-2); }
.prose { max-width: var(--measure); }
.prose > * + * { margin-top: var(--s4); }
.prose > :is(h2, h3) { margin-top: var(--s7); }
.prose > :is(h2, h3) + * { margin-top: var(--s3); }
.serif { font-family: var(--font-serif); }
hr { border: 0; border-top: 1px solid var(--rule); }

/* 4. Links ------------------------------------------------------------- */
a {
  color: var(--ink);
  text-decoration-line: underline;
  text-decoration-thickness: 1px;
  text-decoration-color: var(--ink-3);
  text-underline-offset: 3px;
}
a:hover { text-decoration-color: var(--ink); text-decoration-thickness: 2px; }
a[aria-current="page"] { font-weight: 600; text-decoration-color: var(--accent); }
.link-quiet { text-decoration: none; }
.link-quiet:hover { text-decoration: underline; }

/* 5. Focus ------------------------------------------------------------- */
:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
:focus:not(:focus-visible) { outline: none; }

/* 6. Forms ------------------------------------------------------------- */
label { display: block; font-weight: 500; font-size: var(--t-14); margin-bottom: var(--s1); }
input:not([type="checkbox"], [type="radio"], [type="range"]), select, textarea {
  display: block;
  width: 100%;
  min-height: var(--control);
  padding: var(--s2) var(--s3);
  background: var(--paper);
  border: 1px solid var(--ink-3);
  border-radius: var(--radius);
}
textarea { min-height: 120px; resize: vertical; }
::placeholder { color: var(--ink-3); opacity: 1; }
input:disabled, select:disabled, textarea:disabled { background: var(--paper-2); color: var(--ink-3); }
[aria-invalid="true"] { border-color: var(--bad) !important; }
input[type="checkbox"], input[type="radio"] { width: 16px; height: 16px; accent-color: var(--ink); }
fieldset { border: 0; padding: 0; }
legend { font-weight: 600; margin-bottom: var(--s2); }
.field + .field { margin-top: var(--s5); }
.hint { font-size: var(--t-14); color: var(--ink-2); margin-top: var(--s1); }
.error { font-size: var(--t-14); color: var(--bad); margin-top: var(--s1); }

/* 7. Buttons ----------------------------------------------------------- */
button, .btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--s2);
  min-height: var(--control);
  padding: 0 var(--s4);
  border: 1px solid var(--ink);
  border-radius: var(--radius);
  background: transparent;
  color: var(--ink);
  font-weight: 500;
  text-decoration: none;
  cursor: pointer;
}
button:hover, .btn:hover { background: var(--paper-3); }
button:active, .btn:active { transform: translateY(1px); }
.btn-primary { background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }
.btn-primary:hover { background: var(--ink); border-color: var(--ink); color: var(--paper); }
.btn-quiet { border-color: transparent; text-decoration: underline; text-underline-offset: 3px; }
.btn-quiet:hover { background: transparent; text-decoration-thickness: 2px; }
.btn-danger { border-color: var(--bad); color: var(--bad); }
.btn-danger:hover { background: var(--bad); color: var(--paper); }
button:disabled, .btn[aria-disabled="true"] { opacity: 0.5; cursor: not-allowed; transform: none; }
.btn-sm { min-height: 32px; padding: 0 var(--s3); font-size: var(--t-14); }

/* 8. Tables ------------------------------------------------------------ */
table { width: 100%; max-width: none; border-collapse: collapse; font-size: var(--t-14); }
caption { text-align: left; font-weight: 600; padding-bottom: var(--s2); }
th, td { text-align: left; padding: var(--s2) var(--s3); border-bottom: 1px solid var(--rule); vertical-align: top; }
thead th { background: var(--paper-2); font-weight: 600; border-bottom-color: var(--rule-strong); }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
tbody tr:hover { background: var(--paper-2); }

/* 9. Code -------------------------------------------------------------- */
code, kbd, samp, pre { font-family: var(--font-mono); font-size: 0.875em; }
:not(pre) > code { background: var(--paper-2); padding: 1px var(--s1); border-radius: var(--radius); }
pre {
  background: var(--paper-2);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  padding: var(--s4);
  overflow-x: auto;
  line-height: 1.45;
  max-width: none;
}
kbd {
  border: 1px solid var(--rule);
  border-bottom-width: 2px;
  border-radius: var(--radius);
  padding: 0 var(--s1);
  font-size: var(--t-12);
}

/* 10. Layout utilities ------------------------------------------------- */
.wrap { max-width: var(--page); margin-inline: auto; padding-inline: var(--s5); }
.stack > * + * { margin-top: var(--stack, var(--s4)); }
.cluster { display: flex; flex-wrap: wrap; align-items: center; gap: var(--cluster, var(--s3)); }
.split { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: var(--s4); }
.grid { display: grid; gap: var(--s5); grid-template-columns: repeat(auto-fit, minmax(min(100%, var(--min, 280px)), 1fr)); }
.section { padding-block: var(--s8); border-top: 1px solid var(--rule); }
.panel { border: 1px solid var(--rule); border-radius: var(--radius); padding: var(--s5); background: var(--paper); }
.panel-sunk { background: var(--paper-2); border: 1px solid var(--rule); border-radius: var(--radius); padding: var(--s5); }

/* 11. Text utilities --------------------------------------------------- */
.muted { color: var(--ink-2); }
.faint { color: var(--ink-3); }
.mono { font-family: var(--font-mono); }
.num { font-variant-numeric: tabular-nums; }
.ok { color: var(--ok); }
.warn { color: var(--warn); }
.bad { color: var(--bad); }
.tag {
  display: inline-block;
  font-size: var(--t-12);
  font-weight: 500;
  line-height: 20px;
  padding: 0 6px;
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  color: var(--ink-2);
}
.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* 12. Motion ----------------------------------------------------------- */
@media (prefers-reduced-motion: no-preference) {
  a, button, .btn { transition: opacity var(--dur) ease-out, transform var(--dur) ease-out; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
    scroll-behavior: auto !important;
  }
}
```

#### Decisions in the base stylesheet

- **Dark tokens appear twice.** Once under `[data-theme="dark"]` for an explicit toggle, once under `prefers-color-scheme` for visitors who never touch the toggle. The `:not([data-theme="light"])` guard lets a visitor force light mode on a dark operating system.
- **Input borders use `--ink-3`, not `--rule`.** WCAG 1.4.11 asks for 3:1 contrast on the boundary of a control. `--rule` on `--paper` is about 1.3:1. `--ink-3` is 4.6:1.
- **Links are ink with an underline.** The accent stays reserved for the one primary action on a screen. A page with forty orange links has no primary action.
- **Buttons change fill on hover, not elevation.** Primary goes from accent to ink. Secondary goes from transparent to `--paper-3`. The 1px press offset on `:active` is the only movement.
- **Transitions cover opacity and transform only.** Color changes are instant. This matches the motion rule and removes the slow 300ms `transition-all` fade that ships with most starter kits.
- **`max-width: var(--measure)` sits on block text elements**, so a page without a wrapper still keeps lines near 66 characters. Tables and `pre` opt out because their content is not running prose.
- **`.tag` is a rectangle with a 1px rule.** It replaces the rounded-full pill. There is no dot variant.
- **`.panel` is the only box.** Use it when content needs a boundary, such as a form group or a code sample with a caption. Most sections need only `.section`, which is a top rule and 64px of padding.

### 6.2 Tailwind v3 configuration

Tailwind ships with a palette whose most visible members are `indigo-500` and `violet-600`, eight shadow sizes, rounded corners up to `rounded-3xl`, gradient utilities, backdrop blur, and an animation named `ping` that exists to make a status dot pulse. Every one of those is a tell. Replace `theme` keys outright instead of using `theme.extend`, because extend keeps the defaults.

```js
// tailwind.config.js (Tailwind CSS 3.4)
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,jsx,ts,tsx,mdx}"],
  darkMode: ["selector", '[data-theme="dark"]'],

  corePlugins: {
    ringWidth: false,
    ringColor: false,
    ringOffsetWidth: false,
    ringOffsetColor: false,
    ringOpacity: false,
    boxShadowColor: false,
    dropShadow: false,
    gradientColorStops: false,
    backdropFilter: false,
    backdropBlur: false,
    backdropBrightness: false,
    backdropContrast: false,
    backdropGrayscale: false,
    backdropHueRotate: false,
    backdropInvert: false,
    backdropOpacity: false,
    backdropSaturate: false,
    backdropSepia: false,
  },

  theme: {
    colors: {
      transparent: "transparent",
      current: "currentColor",
      inherit: "inherit",
      paper: { DEFAULT: "var(--paper)", 2: "var(--paper-2)", 3: "var(--paper-3)" },
      ink: { DEFAULT: "var(--ink)", 2: "var(--ink-2)", 3: "var(--ink-3)" },
      rule: { DEFAULT: "var(--rule)", strong: "var(--rule-strong)" },
      accent: { DEFAULT: "var(--accent)", ink: "var(--accent-ink)" },
      ok: "var(--ok)",
      warn: "var(--warn)",
      bad: "var(--bad)",
      focus: "var(--focus)",
      scrim: "rgb(20 20 18 / 0.5)",

      // shadcn/ui names, pointed at the same tokens. See 6.4.
      background: "var(--paper)",
      foreground: "var(--ink)",
      border: "var(--rule)",
      input: "var(--ink-3)",
      ring: "var(--focus)",
      muted: { DEFAULT: "var(--paper-2)", foreground: "var(--ink-2)" },
      card: { DEFAULT: "var(--paper)", foreground: "var(--ink)" },
      popover: { DEFAULT: "var(--paper)", foreground: "var(--ink)" },
      primary: { DEFAULT: "var(--accent)", foreground: "var(--accent-ink)" },
      secondary: { DEFAULT: "var(--paper-2)", foreground: "var(--ink)" },
      destructive: { DEFAULT: "var(--bad)", foreground: "var(--paper)" },
    },

    boxShadow: {
      none: "none",
      DEFAULT: "none",
      sm: "none",
      md: "none",
      lg: "none",
      xl: "none",
      "2xl": "none",
      inner: "none",
    },

    borderRadius: { none: "0", DEFAULT: "2px", sm: "2px", md: "4px" },
    backgroundImage: { none: "none" },
    blur: { none: "0" },

    fontFamily: {
      sans: ["var(--font-sans)"],
      serif: ["var(--font-serif)"],
      mono: ["var(--font-mono)"],
    },

    fontSize: {
      xs: ["12px", { lineHeight: "1.5" }],
      sm: ["14px", { lineHeight: "1.5" }],
      base: ["16px", { lineHeight: "1.5" }],
      lg: ["18px", { lineHeight: "1.5" }],
      xl: ["21px", { lineHeight: "1.3" }],
      "2xl": ["24px", { lineHeight: "1.25" }],
      "3xl": ["32px", { lineHeight: "1.2" }],
      "4xl": ["40px", { lineHeight: "1.15" }],
      "5xl": ["56px", { lineHeight: "1.15" }],
    },

    spacing: {
      0: "0",
      px: "1px",
      0.5: "2px",
      1: "4px",
      2: "8px",
      3: "12px",
      4: "16px",
      6: "24px",
      8: "32px",
      10: "40px",
      12: "48px",
      16: "64px",
      24: "96px",
      32: "128px",
    },

    transitionProperty: {
      none: "none",
      DEFAULT: "opacity, transform",
      opacity: "opacity",
      transform: "transform",
    },
    transitionDuration: { 0: "0ms", 75: "75ms", 100: "100ms", 150: "150ms", DEFAULT: "120ms" },
    transitionTimingFunction: { DEFAULT: "ease-out", out: "ease-out", linear: "linear" },

    animation: { none: "none", spin: "spin 1s linear infinite" },

    extend: {
      maxWidth: { measure: "66ch", page: "1120px" },
    },
  },
  plugins: [],
};
```

#### What each override does

- **`colors` replaced, not extended.** The default palette is gone, including `indigo`, `violet`, `purple`, `fuchsia`, `blue` and `sky`. A class like `bg-indigo-600` now generates nothing, so a pasted snippet renders unstyled instead of on-brand-for-someone-else. Colors point at CSS variables, so `data-theme="dark"` switches them at runtime without a second build.
- **`scrim` is a literal color.** Tailwind v3 cannot apply an opacity modifier such as `bg-ink/40` to a color defined as `var(--ink)`. The dialog overlay needs translucency, so it gets one fixed token.
- **shadcn names map to canonical tokens.** shadcn components reference `bg-background`, `border-input`, `text-muted-foreground` and so on. Mapping them keeps those components compiling while you replace them. One name collides: shadcn's `accent` is a pale hover tint, and here `accent` is the burnt orange. Any shadcn component you have not replaced yet will flash orange on hover. Treat that as a to-do list.
- **`boxShadow` keys all map to `none`.** Keeping the plugin and emptying its values means third-party markup that contains Tailwind's shadow classes renders flat, and `shadow-none` resets still work. Disabling the plugin would also drop `shadow-none`.
- **Ring plugins disabled.** Tailwind's `ring-*` utilities draw with `box-shadow`. Focus uses `outline-2 outline-offset-2 outline-focus` instead, which also survives Windows High Contrast mode, where box-shadow is removed.
- **`gradientColorStops` disabled and `backgroundImage` emptied.** This removes the gradient direction utilities and every color stop. Background images from a URL still work through arbitrary values.
- **All backdrop plugins disabled, `blur` reduced to `none`.** No frosted glass, no blurred hero glow.
- **`borderRadius` stops at 4px.** `rounded-lg`, `rounded-xl`, `rounded-2xl` and `rounded-3xl` no longer exist. `rounded-full` is gone too; add `full: "9999px"` back only if the product has avatars, and lint its use to avatar components.
- **`spacing` is the canonical scale plus 2px and 40px.** `p-5`, `gap-7` and `mt-10` stop working on purpose; the scale has no 20px or 28px step. The 40px step exists for control height (`h-10`).
- **`fontSize` uses the canonical type scale with unitless line heights** that fall inside 1.15 to 1.25 for headings and 1.5 for body.
- **`transitionProperty` default is opacity and transform**, and there is no `colors` or `all` key. `transition-all duration-300`, copied from any template, compiles to nothing.
- **`animation` keeps only `spin`.** `animate-ping` is the pulsing ring around a green status dot. `animate-pulse` is the shimmering skeleton. `animate-bounce` is the arrow under a hero. All three are removed.

### 6.3 Tailwind v4 configuration

Tailwind v4 has no `tailwind.config.js` by default and no `corePlugins`. Configuration lives in CSS under `@theme`. Setting a namespace to `initial` removes every default value in it, which is the v4 equivalent of replacing a key instead of extending it.

```css
/* app.css (Tailwind CSS 4.1) */
@import "tailwindcss";

/* Dark mode follows the data-theme attribute, not only the OS setting. */
@custom-variant dark (&:where([data-theme="dark"], [data-theme="dark"] *));

/* Step 1: clear the defaults. */
@theme {
  --color-*: initial;
  --shadow-*: initial;
  --inset-shadow-*: initial;
  --drop-shadow-*: initial;
  --text-shadow-*: initial;
  --blur-*: initial;
  --radius-*: initial;
  --animate-*: initial;
  --font-*: initial;
  --text-*: initial;
  --ease-*: initial;
}

/* Step 2: static tokens. */
@theme {
  --spacing: 4px;

  --radius-xs: 2px;
  --radius-sm: 2px;
  --radius-md: 4px;

  --font-sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-serif: "Source Serif 4", Georgia, "Times New Roman", serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;

  --text-xs: 12px;   --text-xs--line-height: 1.5;
  --text-sm: 14px;   --text-sm--line-height: 1.5;
  --text-base: 16px; --text-base--line-height: 1.5;
  --text-lg: 18px;   --text-lg--line-height: 1.5;
  --text-xl: 21px;   --text-xl--line-height: 1.3;
  --text-2xl: 24px;  --text-2xl--line-height: 1.25;
  --text-3xl: 32px;  --text-3xl--line-height: 1.2;
  --text-4xl: 40px;  --text-4xl--line-height: 1.15;
  --text-5xl: 56px;  --text-5xl--line-height: 1.15;

  --ease-out: ease-out;
  --default-transition-duration: 120ms;
  --default-transition-timing-function: ease-out;
  --animate-spin: spin 1s linear infinite;

  --container-measure: 66ch;
  --container-page: 1120px;
}

/* Step 3: colors read runtime variables, so data-theme swaps them. */
@theme inline {
  --color-paper: var(--paper);
  --color-paper-2: var(--paper-2);
  --color-paper-3: var(--paper-3);
  --color-ink: var(--ink);
  --color-ink-2: var(--ink-2);
  --color-ink-3: var(--ink-3);
  --color-rule: var(--rule);
  --color-rule-strong: var(--rule-strong);
  --color-accent: var(--accent);
  --color-accent-ink: var(--accent-ink);
  --color-ok: var(--ok);
  --color-warn: var(--warn);
  --color-bad: var(--bad);
  --color-focus: var(--focus);

  /* shadcn/ui names */
  --color-background: var(--paper);
  --color-foreground: var(--ink);
  --color-border: var(--rule);
  --color-input: var(--ink-3);
  --color-ring: var(--focus);
  --color-muted: var(--paper-2);
  --color-muted-foreground: var(--ink-2);
  --color-card: var(--paper);
  --color-card-foreground: var(--ink);
  --color-popover: var(--paper);
  --color-popover-foreground: var(--ink);
  --color-primary: var(--accent);
  --color-primary-foreground: var(--accent-ink);
  --color-secondary: var(--paper-2);
  --color-secondary-foreground: var(--ink);
  --color-destructive: var(--bad);
}

/* Step 4: paste the :root, [data-theme="dark"] and prefers-color-scheme
   blocks from section 1 of unslop-base.css here, outside @theme. */
```

#### What each override does

- **`--color-*: initial`** deletes all 22 default color families, so `text-violet-600` and `from-indigo-500` produce no CSS. It also removes `white` and `black`; `bg-transparent` and `text-current` keep working because they are static utilities.
- **`--shadow-*`, `--inset-shadow-*`, `--drop-shadow-*`, `--text-shadow-*: initial`** remove every named shadow size. The four namespaces are separate in v4; clearing only the first leaves inner and drop variants alive.
- **`--blur-*: initial`** removes the named steps behind `blur-md` and `backdrop-blur-xl`.
- **`--radius-*: initial`** followed by three steps means `rounded-lg` and larger have no value. `rounded-xs`, `rounded-sm` and `rounded-md` resolve to 2px, 2px and 4px.
- **`--animate-*: initial`** deletes `ping`, `pulse` and `bounce`. Only `spin` returns, for loading indicators.
- **`@theme inline` for colors.** Without `inline`, Tailwind writes `var(--color-paper)` into each utility and resolves it where the theme variable is declared. With `inline` it writes `var(--paper)` directly, so the value follows `data-theme` on any ancestor.
- **`--spacing: 4px`** keeps v4's multiplier model. Any integer works (`p-5` is 20px), so the scale is enforced by the class check in 6.6, not by the config.

#### What v4 cannot switch off

Some v4 utilities are static and ignore the theme. `bg-linear-to-r`, `bg-radial`, `bg-conic`, arbitrary values like `shadow-[0_0_40px_#6366f1]`, and every `ring-*` width still compile. Reject them with the class check in 6.6. Do not try to override core utilities with `@utility` to neutralize them; the override order is not part of Tailwind's public contract and has changed between minor versions.

### 6.4 shadcn/ui

shadcn/ui copies component source into your repository, so its defaults are yours to edit. The defaults are also the most recognizable component set on the web: the `rounded-xl border shadow` card, the 36px button with a 1px focus ring, the zoom-in dialog over an 80 percent black overlay. Replace these seven files after running `npx shadcn init`. Every replacement keeps the export names and props of the original, so call sites do not change.

#### The defaults to remove

These are the class strings shadcn generates (new-york style, Tailwind v3 era), shortened to the parts that matter:

```slop
// card.tsx
"rounded-xl border bg-card text-card-foreground shadow"
// button.tsx
"inline-flex ... rounded-md text-sm font-medium transition-colors
 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring ..."
default: "bg-primary text-primary-foreground shadow hover:bg-primary/90"
// badge.tsx
"inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold"
// dialog.tsx
overlay: "fixed inset-0 z-50 bg-black/80 data-[state=open]:animate-in data-[state=open]:fade-in-0"
content: "... gap-4 border bg-background p-6 shadow-lg duration-200
          data-[state=open]:zoom-in-95 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg"
// dropdown-menu.tsx
"z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 shadow-md
 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2"
// sonner.tsx
toast: "group-[.toaster]:bg-background group-[.toaster]:border-border group-[.toaster]:shadow-lg"
// input.tsx
"flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 shadow-sm
 transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring"
```

The pattern across all seven: a shadow for separation, a 6px to 12px radius, a box-shadow ring for focus with `outline-none` stripping the native outline, and zoom or slide entrances on overlays. The replacements below use a border for separation, 2px radius, outline focus, and either no entrance motion or a 120ms fade.

#### Button

```tsx
// components/ui/button.tsx
import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const buttonVariants = cva(
  [
    "inline-flex items-center justify-center gap-2 whitespace-nowrap",
    "rounded-sm border font-medium",
    "focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus",
    "active:translate-y-px disabled:cursor-not-allowed disabled:opacity-50",
    "[&_svg]:size-4 [&_svg]:shrink-0",
  ].join(" "),
  {
    variants: {
      variant: {
        primary: "border-accent bg-accent text-accent-ink hover:border-ink hover:bg-ink hover:text-paper",
        secondary: "border-ink bg-transparent text-ink hover:bg-paper-3",
        quiet: "border-transparent bg-transparent text-ink underline underline-offset-4 hover:decoration-2",
        danger: "border-bad bg-transparent text-bad hover:bg-bad hover:text-paper",
      },
      size: {
        sm: "h-8 px-3 text-sm",
        md: "h-10 px-4 text-sm",
        lg: "h-12 px-6 text-base",
      },
    },
    defaultVariants: { variant: "secondary", size: "md" },
  },
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return <Comp ref={ref} className={cn(buttonVariants({ variant, size }), className)} {...props} />;
  },
);
Button.displayName = "Button";
export { buttonVariants };
```

The default variant is `secondary`, not `primary`. A screen gets one accent button, and making it opt-in means a developer has to choose which one. The shadcn variant names `default`, `outline`, `ghost` and `destructive` are renamed; if you would rather not touch call sites, alias them in the `variant` map.

#### Card

```tsx
// components/ui/card.tsx
import * as React from "react";
import { cn } from "@/lib/utils";

type DivProps = React.HTMLAttributes<HTMLDivElement>;

export function Card({ className, ...props }: DivProps) {
  return <div className={cn("rounded-sm border border-rule bg-paper text-ink", className)} {...props} />;
}

export function CardHeader({ className, ...props }: DivProps) {
  return <div className={cn("flex flex-col gap-1 border-b border-rule px-6 py-4", className)} {...props} />;
}

export function CardTitle({ className, ...props }: React.HTMLAttributes<HTMLHeadingElement>) {
  return <h3 className={cn("text-lg font-semibold leading-tight", className)} {...props} />;
}

export function CardDescription({ className, ...props }: React.HTMLAttributes<HTMLParagraphElement>) {
  return <p className={cn("text-sm text-ink-2", className)} {...props} />;
}

export function CardContent({ className, ...props }: DivProps) {
  return <div className={cn("px-6 py-4", className)} {...props} />;
}

export function CardFooter({ className, ...props }: DivProps) {
  return <div className={cn("flex items-center gap-3 border-t border-rule bg-paper-2 px-6 py-3", className)} {...props} />;
}
```

`CardTitle` renders an `h3` instead of shadcn's `div`, so cards appear in the heading outline. The footer sits on `--paper-2`: a tonal step instead of a second border weight.

#### Badge

```tsx
// components/ui/badge.tsx
import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "inline-flex h-6 items-center rounded-sm border px-2 text-xs font-medium",
  {
    variants: {
      tone: {
        neutral: "border-rule text-ink-2",
        ok: "border-ok text-ok",
        warn: "border-warn text-warn",
        bad: "border-bad text-bad",
      },
    },
    defaultVariants: { tone: "neutral" },
  },
);

export interface BadgeProps
  extends React.HTMLAttributes<HTMLSpanElement>,
    VariantProps<typeof badgeVariants> {}

export function Badge({ className, tone, ...props }: BadgeProps) {
  return <span className={cn(badgeVariants({ tone }), className)} {...props} />;
}
```

No filled variants, no dot child, no pulse. The tone colors the text and the border, and the words inside carry the meaning: "Failed 14:02", not a red capsule. The prop is `tone` instead of `variant` so a search for `variant="default"` on a Badge finds every unconverted call site.

#### Dialog

```tsx
// components/ui/dialog.tsx (the two parts that change)
import * as React from "react";
import * as DialogPrimitive from "@radix-ui/react-dialog";
import { X } from "lucide-react";
import { cn } from "@/lib/utils";

export const DialogOverlay = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Overlay ref={ref} className={cn("fixed inset-0 z-50 bg-scrim", className)} {...props} />
));
DialogOverlay.displayName = "DialogOverlay";

export const DialogContent = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPrimitive.Portal>
    <DialogOverlay />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-1/2 top-1/2 z-50 grid w-[calc(100%-32px)] max-w-lg -translate-x-1/2 -translate-y-1/2",
        "gap-4 rounded-sm border border-rule-strong bg-paper p-6 text-ink",
        className,
      )}
      {...props}
    >
      {children}
      <DialogPrimitive.Close
        className="absolute right-3 top-3 inline-flex size-8 items-center justify-center rounded-sm text-ink-2 hover:bg-paper-3 hover:text-ink focus-visible:outline focus-visible:outline-2 focus-visible:outline-focus"
      >
        <X className="size-4" strokeWidth={1.5} aria-hidden="true" />
        <span className="sr-only">Close</span>
      </DialogPrimitive.Close>
    </DialogPrimitive.Content>
  </DialogPrimitive.Portal>
));
DialogContent.displayName = "DialogContent";
```

The dialog appears without zoom or slide. The border is `--rule-strong` (ink) because a modal sits over a scrim and needs a hard edge; a 1px `--rule` line disappears against the darkened page. The overlay is 50 percent, down from 80, so the user can still see what the dialog is about.

#### DropdownMenu

```tsx
// components/ui/dropdown-menu.tsx (content and item)
export const DropdownMenuContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <DropdownMenuPrimitive.Portal>
    <DropdownMenuPrimitive.Content
      ref={ref}
      sideOffset={sideOffset}
      className={cn("z-50 min-w-48 overflow-hidden rounded-sm border border-rule-strong bg-paper p-1 text-ink", className)}
      {...props}
    />
  </DropdownMenuPrimitive.Portal>
));
DropdownMenuContent.displayName = "DropdownMenuContent";

export const DropdownMenuItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Item>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex h-8 cursor-default select-none items-center gap-2 rounded-sm px-2 text-sm outline-none",
      "data-[highlighted]:bg-paper-3 data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      "[&_svg]:size-4 [&_svg]:text-ink-2",
      className,
    )}
    {...props}
  />
));
DropdownMenuItem.displayName = "DropdownMenuItem";
```

`outline-none` is acceptable on menu items only because Radix moves focus and sets `data-highlighted` on the focused item, which gets a `--paper-3` fill. `min-w-48` is 192px; add `minWidth: { 48: "192px" }` to the v3 config, or use `min-w-[192px]`.
