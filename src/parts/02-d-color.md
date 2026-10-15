### 2.10 Data and chart color

Charts are where blue returns through the back door. Every major charting default leads with blue or violet, so a page that bans indigo in its buttons still ships it in its first chart.

#### The defaults and where they lead

| Library | First series color | OKLCH hue |
|---|---|---|
| D3 `schemeCategory10`, matplotlib `tab10` | `#1F77B4` | 245 |
| Tableau 10 | `#4E79A7` | 251 |
| Plotly default | `#636EFA` | 275 |
| Chart.js colors plugin | `#36A2EB` | 243 |
| Recharts documentation examples | `#8884D8` | 285 |
| Google Sheets default | `#4285F4` | 260 |
| matplotlib `viridis` (sequential) | starts at `#440154` | 318 |

The Recharts examples are the most copied chart code in generated React, and their first two strokes, `#8884d8` and `#82ca9d`, show up verbatim in thousands of dashboards. Treat those two hex values as a fingerprint.

#### Categorical palette

Six colors, built from the families in 2.3, with lightness spread on purpose so that series stay apart for readers with color vision deficiency. Measured as the smallest OKLab ΔE between any two colors, under normal vision and under simulated deuteranopia and protanopia (Machado 2009), the light set never drops below 10.4. Two default greens and reds sharing the same lightness can drop to 4 (2.4).

Light mode, on `--paper`:

| Order | Name | Hex | OKLCH | Contrast on `--paper` |
|---|---|---|---|---|
| 1 | Orange | `#D8662A` | `0.639 0.160 45` | 3.29:1 |
| 2 | Graphite | `#27241F` | `0.262 0.010 81` | 14.19:1 |
| 3 | Teal | `#429599` | `0.621 0.080 200` | 3.22:1 |
| 4 | Ochre | `#E0AF3B` | `0.779 0.140 85` | 1.86:1 |
| 5 | Raspberry | `#973462` | `0.481 0.140 355` | 6.46:1 |
| 6 | Olive | `#3F5700` | `0.421 0.107 126` | 7.49:1 |

Dark mode, on `#141412` (smallest ΔE 10.7):

| Order | Name | Hex | OKLCH | Contrast on dark `--paper` |
|---|---|---|---|---|
| 1 | Orange | `#F78955` | `0.740 0.150 45` | 7.61:1 |
| 2 | Stone | `#EFEAE2` | `0.939 0.012 80` | 15.40:1 |
| 3 | Teal | `#64C3C3` | `0.760 0.090 195` | 8.90:1 |
| 4 | Ochre | `#F8CA65` | `0.860 0.130 85` | 11.97:1 |
| 5 | Raspberry | `#C1628A` | `0.620 0.129 355` | 4.73:1 |
| 6 | Olive | `#667F30` | `0.559 0.110 125` | 4.08:1 |

Rules for categorical color:

- Six series at most. A seventh category goes into "Other" in `--ink-3`, or the chart becomes small multiples, one panel per series.
- Assign colors in order and keep the assignment stable. If "Europe" is orange on one chart, it is orange on every chart in the product.
- Light-mode ochre is 1.86:1 against the paper, under the 3:1 floor for graphics. Give ochre bars and areas a 1px `--ink` outline, or use ochre only for large areas that also carry a direct label.
- Do not use status colors as series colors. A green series next to a red series reads as good versus bad.

#### Gray plus one

Most charts answer one question about one series. Draw every series in `--ink-3` and the one that matters in `--accent`. This needs no legend and no categorical palette, and it is the single most effective chart color rule.

```css
.chart .series { stroke: var(--ink-3); stroke-width: 1.5; fill: none; }
.chart .series[data-focus] { stroke: var(--accent); stroke-width: 2.5; }
.chart .series-label { font: 400 12px/1 var(--font-sans); fill: var(--ink-2); }
.chart .series-label[data-focus] { fill: var(--ink); font-weight: 600; }
```

#### Sequential ramps

For ordered values (density, counts, rates), use a single-hue ramp from the paper toward a dark step of the accent family. Use five classes, not a continuous scale; five stepped colors can be named and read off a legend, a continuous ramp cannot.

| Class | Hex | OKLCH |
|---|---|---|
| 1 (lowest) | `#FEE1D7` | `0.931 0.035 39` |
| 2 | `#F2A48B` | `0.789 0.100 39` |
| 3 | `#D15F38` | `0.620 0.154 39` |
| 4 | `#933511` | `0.459 0.135 39` |
| 5 (highest) | `#4E1C0B` | `0.300 0.080 39` |

L steps are about 0.15 apart, evenly spaced, so each class is as distinct from its neighbor as every other. The ramp avoids `viridis` and `Blues`, the two most common defaults, both of which pass through the banned band.

#### Diverging ramps

For values around a meaningful midpoint (change from last year, above or below target), use two hues that differ in lightness as well as hue, with the midpoint on `--paper-2`. The default `RdBu` (red to blue) puts blue at one end; replace it with teal to orange.

| Class | Hex | Meaning |
|---|---|---|
| -3 | `#005356` | Far below |
| -2 | `#34898D` | Below |
| -1 | `#92C2C4` | Slightly below |
| 0 | `#EFECE4` | At midpoint |
| +1 | `#EAAE93` | Slightly above |
| +2 | `#D46E45` | Above |
| +3 | `#983D1D` | Far above |

Which end is "good" depends on the measure. Say it in the legend title ("Change in late deliveries, lower is better"), not with green and red.

#### Legends are swatches, not gradients

A continuous gradient bar under a map is a gradient (2.2). Draw the legend as one swatch per class, with the class range printed under each swatch.

```html
<ol class="legend" aria-label="Late deliveries per 1,000 orders">
  <li><span class="swatch" style="background:#FEE1D7"></span>0 to 4</li>
  <li><span class="swatch" style="background:#F2A48B"></span>5 to 9</li>
  <li><span class="swatch" style="background:#D15F38"></span>10 to 19</li>
  <li><span class="swatch" style="background:#933511"></span>20 to 39</li>
  <li><span class="swatch" style="background:#4E1C0B"></span>40 or more</li>
</ol>
```

```css
.legend { display: flex; gap: 0; margin: 0; padding: 0; list-style: none; font: 400 12px/1.3 var(--font-sans); color: var(--ink-2); }
.legend li { display: grid; gap: 4px; min-width: 72px; }
.legend .swatch { display: block; height: 12px; border: 1px solid var(--rule); }
```

#### Label directly

- With four series or fewer, put the label at the end of each line or inside each bar segment, and drop the legend. The eye stops jumping between key and data.
- Label text is `--ink` or `--ink-2`, with a short colored mark beside it. Text in the series color fails contrast for ochre and is hard to read for orange and teal.
- Print the value on the bar when there are fewer than about 12 bars. Gridlines can then go.

#### Chart chrome

- Gridlines: horizontal only, 1px `--rule`. No vertical gridlines on time series.
- Zero baseline: 1px `--ink`.
- Axis text: 12px `--ink-3` on `--paper`, tabular numerals.
- Tooltips: the inverted tooltip from 2.5, no shadow, no blur.
- Areas: a flat fill at the series color with `fill-opacity: 0.12`, or no fill. The gradient fill under a line, from the Recharts area chart example, is banned.

```slop
<defs>
  <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
    <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8}/>
    <stop offset="95%" stopColor="#8884d8" stopOpacity={0}/>
  </linearGradient>
</defs>
<Area type="monotone" dataKey="uv" stroke="#8884d8" fill="url(#colorUv)" />
```

```tsx
const series = {
  orange: "var(--chart-1)",
  graphite: "var(--chart-2)",
  teal: "var(--chart-3)",
} as const;

<AreaChart data={rows} margin={{ top: 8, right: 64, bottom: 8, left: 8 }}>
  <CartesianGrid vertical={false} stroke="var(--rule)" />
  <XAxis dataKey="month" tick={{ fill: "var(--ink-3)", fontSize: 12 }} axisLine={{ stroke: "var(--ink)" }} tickLine={false} />
  <YAxis tick={{ fill: "var(--ink-3)", fontSize: 12 }} axisLine={false} tickLine={false} />
  <Area type="linear" dataKey="paid" stroke={series.orange} strokeWidth={2} fill={series.orange} fillOpacity={0.12} isAnimationActive={false} />
</AreaChart>
```

```css
:root {
  --chart-1: #D8662A; --chart-2: #27241F; --chart-3: #429599;
  --chart-4: #E0AF3B; --chart-5: #973462; --chart-6: #3F5700;
}
:root[data-theme="dark"] {
  --chart-1: #F78955; --chart-2: #EFEAE2; --chart-3: #64C3C3;
  --chart-4: #F8CA65; --chart-5: #C1628A; --chart-6: #667F30;
}
```

`type="linear"` draws the data as measured; `monotone` smooths it and invents values between points. `isAnimationActive={false}` removes the 1500ms default draw-in animation, which runs on every data refresh.

#### Review checklist for 2.10

- No chart color comes from a library default. `#8884d8`, `#82ca9d`, `#1f77b4`, `#636efa` and `#36a2eb` do not appear.
- Categorical series use the six-color set, in a stable order, six at most.
- Sequential and diverging scales are stepped, with swatch legends.
- Series with four or fewer lines are labeled directly.
- Gridlines are horizontal `--rule`; no gradient area fills; no chart animation.
- Chart colors switch with the theme through tokens.

### 2.11 Color in code

The rules in this Part hold only if the code cannot express the banned patterns easily. Remove shadows, gradients, blur and the default palette at the config level, then add a linter and a grep step so anything that slips through fails CI.

#### Token file structure

Keep three layers in one file, in this order:

1. Primitives. Every raw value, named by hue and step: `--orange-700: #B4441C`. Only this layer contains hex values.
2. Roles. What each value is for: `--accent: var(--orange-700)`. Components read only this layer.
3. Themes. Role overrides per theme: `:root[data-theme="dark"] { --accent: var(--orange-500-dark); }`.

```css
/* tokens.css: the only file allowed to contain color literals */
:root {
  /* primitives */
  --stone-50: #F7F5F0;  --stone-100: #EFECE4; --stone-200: #E5E1D6; --stone-300: #D9D5CB;
  --stone-600: #6F6C64; --stone-700: #4A4843; --stone-900: #1A1A18;
  --orange-700: #B4441C;

  /* roles */
  --paper: var(--stone-50);   --paper-2: var(--stone-100); --paper-3: var(--stone-200);
  --rule: var(--stone-300);   --rule-strong: var(--stone-900);
  --ink: var(--stone-900);    --ink-2: var(--stone-700);   --ink-3: var(--stone-600);
  --accent: var(--orange-700); --accent-ink: #FFFFFF;
  --focus: var(--stone-900);
  --radius: 2px;
}
```

#### Tailwind v3: remove the defaults

Override the theme keys (not `extend`) so the default scales vanish, and turn off the plugins that generate shadows, rings, blur and gradients. Tailwind's `ring-*` utilities compile to `box-shadow` declarations, so they go too.

```js
// tailwind.config.js
module.exports = {
  content: ["./src/**/*.{html,js,jsx,ts,tsx,vue,svelte}"],
  theme: {
    colors: {
      transparent: "transparent",
      current: "currentColor",
      paper: { DEFAULT: "var(--paper)", 2: "var(--paper-2)", 3: "var(--paper-3)" },
      ink: { DEFAULT: "var(--ink)", 2: "var(--ink-2)", 3: "var(--ink-3)" },
      rule: { DEFAULT: "var(--rule)", strong: "var(--rule-strong)" },
      accent: { DEFAULT: "var(--accent)", ink: "var(--accent-ink)" },
      ok: "var(--ok)",
      warn: "var(--warn)",
      bad: "var(--bad)",
    },
    borderRadius: { none: "0", DEFAULT: "var(--radius)", full: "9999px" },
    boxShadow: { none: "none" },
    dropShadow: {},
    backgroundImage: {},
    backdropBlur: {},
    blur: {},
    fontFamily: {
      sans: ["IBM Plex Sans", "system-ui", "sans-serif"],
      serif: ["Source Serif 4", "Georgia", "serif"],
      mono: ["IBM Plex Mono", "ui-monospace", "monospace"],
    },
  },
  corePlugins: {
    boxShadowColor: false,
    dropShadow: false,
    backgroundImage: false,
    gradientColorStops: false,
    backdropFilter: false,
    backdropBlur: false,
    blur: false,
    ringWidth: false,
    ringColor: false,
    ringOpacity: false,
    ringOffsetWidth: false,
    ringOffsetColor: false,
  },
};
```

With `colors` replaced, `bg-indigo-600` and `text-gray-500` stop compiling, and an agent that writes them gets unstyled output that a reviewer sees at once. `rounded-full` stays only for avatars and switches; the lint step below checks where it is used.

#### Tailwind v4: the same in CSS

Tailwind v4 reads its theme from CSS. Reset whole namespaces with `initial`, then declare only the tokens.

```css
@import "tailwindcss";

@theme {
  --color-*: initial;
  --shadow-*: initial;
  --inset-shadow-*: initial;
  --drop-shadow-*: initial;
  --text-shadow-*: initial;
  --blur-*: initial;
  --radius-*: initial;

  --color-paper: #F7F5F0;
  --color-paper-2: #EFECE4;
  --color-paper-3: #E5E1D6;
  --color-ink: #1A1A18;
  --color-ink-2: #4A4843;
  --color-ink-3: #6F6C64;
  --color-rule: #D9D5CB;
  --color-accent: #B4441C;
  --radius-sm: 2px;

  --font-sans: "IBM Plex Sans", system-ui, sans-serif;
}
```

Version 4 generates gradient utilities (`bg-linear-to-r`, `bg-radial`, `bg-conic`) and ring utilities without reading the theme, so the reset cannot remove them. The grep step is what catches those.

#### Stylelint rules

```json
{
  "rules": {
    "property-disallowed-list": ["backdrop-filter", "-webkit-backdrop-filter", "text-shadow"],
    "declaration-property-value-disallowed-list": {
      "box-shadow": ["/^(?!none$).+/"],
      "filter": ["/drop-shadow/", "/blur/"],
      "background": ["/gradient/"],
      "background-image": ["/gradient/"],
      "border-image": ["/gradient/"],
      "mask-image": ["/gradient/"],
      "border-radius": ["/^(?:[5-9]|\\d{2,})(?:\\.\\d+)?px/", "/rem/", "/em$/"]
    },
    "function-disallowed-list": ["linear-gradient", "radial-gradient", "conic-gradient", "repeating-linear-gradient", "repeating-radial-gradient"],
    "color-named": "never",
    "color-no-hex": true
  },
  "overrides": [
    { "files": ["src/styles/tokens.css"], "rules": { "color-no-hex": null } }
  ]
}
```

`color-no-hex` everywhere except the token file forces every component to use roles. `border-radius: 50%` stays legal for avatars.

#### Grep commands

Run these in CI over source files. Each must return nothing. Exclude the token file and lint config where noted.

```bash
# box-shadow values other than none, plus Tailwind shadow-* and ring-* utilities
rg -n --pcre2 'box-shadow\s*:(?!\s*none\b)' src/
rg -n '\bshadow-(sm|md|lg|xl|2xl|inner)\b|\bring-[0-9a-z]' src/

# Gradients in CSS and in Tailwind classes (v3 and v4 names)
rg -n '(linear|radial|conic)-gradient' src/
rg -n '\bbg-(gradient|linear|radial|conic)\b|\b(from|via|to)-[a-z]+-[0-9]{2,3}\b' src/

# Blur and glass
rg -n 'backdrop-(blur|filter)|\bblur-(sm|md|lg|xl|2xl|3xl)\b|filter:\s*blur' src/

# Default palette leaks: blue-violet classes and their hex values
rg -n '\b(blue|indigo|violet|purple|fuchsia|sky|slate)-[0-9]{2,3}\b' src/
rg -ni '#(6366f1|4f46e5|8b5cf6|a855f7|3b82f6|2563eb|0f172a|020817|6b7280|8884d8|82ca9d)\b' src/

# Large radius and pills
rg -n '\brounded-(lg|xl|2xl|3xl)\b' src/
rg -n '\brounded-full\b' src/ | rg -v 'avatar|switch|radio'

# Status tells
rg -n 'animate-(pulse|ping)' src/
rg -n '>\s*LIVE\s*<' src/
```

#### A hue check for hex literals

Class names are not the only way blue gets in. A hex value pasted from a mockup slips past every class-based grep. This script flags any hex color whose OKLCH hue falls in the banned band with visible chroma.

```python
#!/usr/bin/env python3
"""Flag hex colors with OKLCH hue 235 to 335 and chroma above 0.02."""
import math, re, sys

HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")

def to_lin(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def oklch(hexstr):
    h = hexstr if len(hexstr) == 6 else "".join(ch * 2 for ch in hexstr)
    r, g, b = (to_lin(int(h[i:i + 2], 16)) for i in (0, 2, 4))
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return math.hypot(a, bb), math.degrees(math.atan2(bb, a)) % 360

bad = 0
for path in sys.argv[1:]:
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        for m in HEX.finditer(line):
            chroma, hue = oklch(m.group(1))
            if chroma > 0.02 and 235 <= hue <= 335:
                print(f"{path}:{n}: #{m.group(1)} hue {hue:.0f} chroma {chroma:.3f}")
                bad += 1
sys.exit(1 if bad else 0)
```

Run it as `python3 scripts/hue_check.py $(git ls-files '*.css' '*.tsx' '*.html' '*.svg')`. The chroma floor of 0.02 lets near-neutral grays through (Newsprint's paper at chroma 0.003) and still catches Tailwind `gray-500` (`#6B7280`, 0.023) and the middle steps of `slate` (0.035 to 0.041), along with every blue and indigo.

#### Agent instructions

When an AI agent writes UI code for a project, add the rules to the instruction file it reads (`CLAUDE.md`, `AGENTS.md`, `.cursorrules` or the equivalent) in plain, checkable form:

```text
Color and depth rules for this repo:
- Colors come from CSS variables in src/styles/tokens.css. Never write a hex value or a Tailwind palette class in a component.
- One accent: var(--accent). No blue, indigo, violet or purple anywhere.
- No box-shadow except none. No ring utilities. Focus is outline 2px solid var(--focus), offset 2px.
- No gradients of any kind. No backdrop-filter. No blur. No glow. No text-shadow.
- Border radius is var(--radius) (2px). No rounded-lg or larger. rounded-full only on avatars and switches.
- Depth: borders (1px var(--rule), var(--rule-strong) for floating layers) and surface tones (--paper, --paper-2, --paper-3).
- Status: word plus icon plus color. No pulsing dots, no LIVE pills.
- Run npm run lint:color before finishing. It must exit 0.
```

#### Review checklist for 2.11

- Hex values exist only in the token file.
- The Tailwind theme replaces `colors`, `boxShadow`, `backgroundImage` and `borderRadius` instead of extending them; ring and gradient plugins are off (v3) or caught by grep (v4).
- Stylelint blocks shadows, gradients, blur and large radii.
- The grep commands and the hue check run in CI and exit 0.
- The agent instruction file lists the color rules in checkable form.

### 2.12 Review checklist for Part 2

Run this list on every screen before it ships. The chapter checklists above hold the detail.

#### Palette and status

- Neutrals have a named hue and chroma under 0.012; surface steps are 0.025 to 0.035 apart in OKLCH L (0.04 to 0.05 in dark mode).
- One accent, OKLCH hue outside 235 to 335, under 10% of the screen; bright accents split into fill and text tokens.
- Every shipped text pairing passes 4.5:1 on each surface it sits on; control boundaries pass 3:1; `--ink-3` appears only on `--paper`.
- Three status hues, each shown with a word and a distinct icon shape. No pulsing dots, no LIVE pill. Deltas colored by meaning.

#### Effects and depth

- No gradients of any kind or hue, no blur, glass, glow, `text-shadow`, noise, neon, spotlight, tilt or shimmer.
- `box-shadow: none` everywhere; no `shadow-*` or `ring-*` classes.
- Depth comes from tone steps, borders, overlap, spacing and inversion. Floating layers are opaque with a 1px `--rule-strong` border.
- Hover changes a border or tone in 120ms or less; selection combines tone, edge and icon; every layer edge survives forced colors mode.

#### Borders and radius

- Borders are 1px or 2px in token colors (3px double for grand totals, 4px for one masthead rule); never translucent; never more than two bordered containers deep.
- One radius, 2px or 0. Circles only for avatars, radios, switches, swatches and data marks.

#### Dark mode and charts

- A separate measured dark token set; darkest surface at L 0.16 to 0.22; no `#000` surfaces, no `#FFF` text; `color-scheme` set before first paint.
- Charts use the six-color set or gray plus one, stepped ramps with swatch legends, direct labels, and no library default colors.

#### Code

- Hex values live only in the token file; Tailwind theme keys are replaced, not extended.
- Stylelint, the grep commands and the hue check exit 0 in CI, and the fingerprint scan from 2.1 finds zero tells.
