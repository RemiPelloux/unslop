### 4.6 Buttons

#### What the machine produces

```slop
<button className="group inline-flex items-center gap-2 rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 px-8 py-4 font-semibold text-white shadow-lg shadow-indigo-500/50 transition-all duration-300 hover:scale-105 hover:shadow-xl">
  Get Started
  <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-1" />
</button>
<button className="rounded-xl border border-gray-300 bg-white/50 px-8 py-4 font-semibold text-gray-700 backdrop-blur-sm hover:bg-white">
  Learn More
</button>
```

The indigo to purple gradient, a colored glow from `shadow-indigo-500/50`, `hover:scale-105` that shifts the layout, an arrow that slides 4px right on hover, and Title Case labels that name no action. The second button is the glass ghost button that always rides next to it. Both then reappear in settings pages and dialogs, because the model reuses its only button.

#### Rules

1. Three sizes: 32px tall for dense toolbars and tables, 40px default, 48px for a single primary action on a marketing page. Horizontal padding 12px, 16px and 20px.
2. Text: 14px at 32px height, 15px or 16px at 40 and 48. Weight 500. Sentence case. No letter spacing.
3. Corners: `var(--radius)`, which is 0 or 2px. Never pill-shaped for a text button.
4. Three levels. Primary: `--accent` fill, `--accent-ink` text, one per view region. Secondary: transparent, 1px `--rule-strong` border, `--ink` text. Tertiary: text only, underlined. Destructive: `--bad` fill, only inside the confirmation step.
5. Hover changes color only: primary darkens by mixing 12% `--ink` into the accent. No scale, no lift, no glow, no icon slide. Transition 100ms `ease-out` on `background-color`.
6. Active: `translateY(1px)` for 0ms in, 100ms out.
7. Minimum target 24px by 24px (WCAG 2.5.8). On touch layouts, 44px by 44px, extended with padding if the visible button is smaller.
8. Labels are a verb plus the object: "Save invoice", "Send 3 reminders", "Delete project". Not "Submit", "OK", "Get started", "Learn more".
9. Prefer `aria-disabled="true"` with an explanation over the `disabled` attribute, so the button stays focusable and the reason is reachable.
10. Loading keeps the button's width fixed, swaps the label to "Saving..." and sets `aria-busy="true"`. Keep that state for at least 400ms even when the request returns in 80ms, so it does not flash.
11. Icon-only buttons are 32px or 40px squares with an `aria-label` and a tooltip after 500ms hover. Icons beside text are 16px and carry meaning (a download glyph on "Download CSV"), never a decorative arrow.

#### Reference build

```html
<button class="btn btn-primary" type="submit">Save invoice</button>
<button class="btn btn-secondary" type="button">Preview PDF</button>
<button class="btn btn-tertiary" type="button">Discard changes</button>
<button class="btn btn-primary" type="submit" aria-busy="true" style="inline-size: 9.5em">Saving...</button>
<button class="btn btn-icon" type="button" aria-label="Duplicate invoice">
  <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
    <rect x="5.5" y="5.5" width="8" height="8"/><path d="M10.5 2.5h-8v8"/>
  </svg>
</button>
```

```css
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  height: 40px; padding: 0 16px;
  font: 500 15px/1 var(--font-sans); letter-spacing: 0; white-space: nowrap;
  border: 1px solid transparent; border-radius: var(--radius);
  cursor: pointer; transition: background-color 100ms ease-out, transform 100ms ease-out;
}
.btn-primary { background: var(--accent); color: var(--accent-ink); }
.btn-primary:hover { background: color-mix(in srgb, var(--accent) 88%, var(--ink)); }
.btn-secondary { background: transparent; color: var(--ink); border-color: var(--rule-strong); }
.btn-secondary:hover { background: var(--paper-2); }
.btn-tertiary { background: transparent; color: var(--ink); padding: 0 4px; text-decoration: underline; text-underline-offset: 3px; }
.btn-tertiary:hover { text-decoration-thickness: 2px; }
.btn-icon { width: 40px; padding: 0; background: transparent; color: var(--ink); border-color: var(--rule); }
.btn-icon:hover { background: var(--paper-2); border-color: var(--rule-strong); }
.btn:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.btn:active { transform: translateY(1px); transition-duration: 0ms; }
.btn[aria-disabled="true"], .btn:disabled { opacity: 0.45; cursor: not-allowed; }
.btn[aria-disabled="true"]:active { transform: none; }
.btn[aria-busy="true"] { cursor: progress; }
.btn-sm { height: 32px; padding: 0 12px; font-size: 14px; }
.btn-lg { height: 48px; padding: 0 20px; font-size: 16px; }
@media (prefers-reduced-motion: reduce) { .btn { transition: none; } .btn:active { transform: none; } }
```

#### States

- Hover: color step only, 100ms. Active: 1px down, no duration on press.
- Focus-visible: 2px `--focus` outline at 2px offset. Never `outline: none` without a replacement.
- Disabled: 45% opacity, `not-allowed` cursor, reason written beside it ("Add at least one line item to save").
- Loading: fixed width, "Saving...", `aria-busy`, at least 400ms.

#### Copy

```slop
Get Started
Learn More
Submit
```

- Save invoice
- Send 3 reminders
- Start 14-day trial (no card)

A good label still makes sense when it is the only thing a person reads in the dialog. "Delete project and 214 files" does; "Confirm" does not.

#### Checklist

- Heights 32, 40, 48; radius 0 or 2px.
- One primary per region; the rest secondary or tertiary.
- Hover is a color step; no scale, glow, gradient or sliding arrow.
- Labels name the action and the object.

### 4.7 Cards

#### What the machine produces

```slop
<div className="grid grid-cols-1 gap-8 md:grid-cols-3">
  {features.map((f) => (
    <div key={f.title} className="group rounded-2xl border border-gray-100 bg-white p-8 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
      <div className="mb-6 flex h-12 w-12 items-center justify-center rounded-xl bg-indigo-100">
        <f.icon className="h-6 w-6 text-indigo-600" />
      </div>
      <h3 className="mb-2 text-xl font-semibold text-gray-900">{f.title}</h3>
      <p className="text-gray-600">{f.description}</p>
      <div className="mt-6 rounded-xl border border-gray-100 bg-gray-50 p-4">
        <div className="rounded-lg bg-white p-3 shadow-sm">{f.stat}</div>
      </div>
    </div>
  ))}
</div>
```

Three failures in one grid. The icon sits in a 48px `rounded-xl bg-indigo-100` tile, the most recognizable mark of a generated feature section. The card lifts 4px with `hover:-translate-y-1 hover:shadow-xl` even though nothing in it is clickable. And there are three nested enclosures: card, grey panel, white chip, each with its own border radius and padding, so 30% of the width is spent on frames.

#### Rules

1. A card holds one object a person can act on as a unit: a project, an invoice, a listing. Marketing paragraphs and feature lists are not objects. Set them as headings and text in a grid with no boxes.
2. One level of enclosure. Inside a card, separate parts with a 1px `--rule` line or 16px of space, never with another bordered or filled box.
3. No icon tiles. If an icon earns a place, it is 20px, stroke 1.5px, `--ink-2`, inline before the heading or above it with 8px of space. No colored square or circle behind it.
4. Card: 1px `--rule` border, `var(--radius)` corners, `--paper` fill or one tonal step down to `--paper-2`. Padding 16px in dense grids, 24px otherwise.
5. No hover lift, no hover scale, no hover border glow. A card that is a link changes its border to `--rule-strong` and underlines its title. Duration 0ms or 100ms.
6. One link per card, on the title, stretched over the card with a pseudo-element. Do not wrap the card in an `<a>` that also contains buttons; nested interactive elements break keyboard and screen reader use.
7. Title 18px weight 600, metadata 14px `--ink-2`, numbers in tabular figures. Put the fact a person scans for (amount, date, status) in the same position on every card.

#### Reference build

```html
<ul class="cards">
  <li class="card">
    <h3 class="card-title"><a href="/invoices/1042">Invoice 1042</a></h3>
    <p class="card-meta">Halden Freight. Due 28 Oct 2026</p>
    <hr class="card-rule">
    <dl class="card-facts">
      <div><dt>Amount</dt><dd>EUR 4,180.00</dd></div>
      <div><dt>Status</dt><dd class="is-late">12 days late</dd></div>
    </dl>
    <button class="btn btn-secondary btn-sm card-action" type="button">Send reminder</button>
  </li>
</ul>
```

```css
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px; margin: 0; padding: 0; list-style: none; }
.card {
  position: relative; display: flex; flex-direction: column; gap: 8px;
  padding: 16px; background: var(--paper); border: 1px solid var(--rule); border-radius: var(--radius);
  transition: border-color 100ms ease-out;
}
.card-title { margin: 0; font: 600 18px/1.25 var(--font-sans); }
.card-title a { color: var(--ink); text-decoration: none; }
.card-title a::after { content: ""; position: absolute; inset: 0; }
.card:hover { border-color: var(--rule-strong); }
.card:hover .card-title a { text-decoration: underline; text-underline-offset: 3px; }
.card-title a:focus-visible { outline: none; }
.card:has(.card-title a:focus-visible) { outline: 2px solid var(--focus); outline-offset: 2px; }
.card-meta { margin: 0; font-size: 14px; color: var(--ink-2); }
.card-rule { width: 100%; margin: 8px 0; border: 0; border-top: 1px solid var(--rule); }
.card-facts { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 0; font-variant-numeric: tabular-nums; }
.card-facts dt { font-size: 12px; color: var(--ink-3); }
.card-facts dd { margin: 0; font-size: 14px; color: var(--ink); }
.card-facts .is-late { color: var(--bad); }
.card-action { position: relative; z-index: 1; align-self: start; margin-top: 8px; }
@media (prefers-reduced-motion: reduce) { .card { transition: none; } }
```

#### States

- Hover: border to `--rule-strong`, title underline. Nothing moves.
- Focus-visible: the whole card gets the 2px outline through `:has()`, so the focus area matches the click area.
- Selected (in a picker): `--paper-3` fill and `aria-selected` or a checked checkbox in the card's top-left.

#### Copy

```slop
Lightning Fast
Built for speed. Our platform delivers blazing performance at scale.
Secure by Default
```

- Exports in under 2 seconds. 10,000 rows to CSV in 1.4 s on the median account.
- SSO with SAML and SCIM. Okta, Entra ID and Google Workspace tested.

Headings in a feature grid state the fact. The text below gives the number or the condition.

#### Checklist

- Cards only for objects a person acts on; feature copy set without boxes.
- One enclosure level; no card in a card.
- No icon in a rounded colored square.
- No lift, scale or glow on hover; border and underline only.

### 4.8 Charts and stat tiles

#### What the machine produces

```slop
<Card>
  <CardHeader className="flex flex-row items-center justify-between pb-2">
    <CardTitle className="text-sm font-medium">Total Revenue</CardTitle>
    <DollarSign className="h-4 w-4 text-muted-foreground" />
  </CardHeader>
  <CardContent>
    <div className="text-2xl font-bold">$45,231.89</div>
    <p className="text-xs text-green-500">+20.1% from last month</p>
  </CardContent>
</Card>
<AreaChart data={data}>
  <defs>
    <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
      <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8} />
      <stop offset="95%" stopColor="#8884d8" stopOpacity={0} />
    </linearGradient>
  </defs>
  <Area type="monotone" dataKey="uv" stroke="#8884d8" fill="url(#colorUv)" />
</AreaChart>
```

"Total Revenue, $45,231.89, +20.1% from last month" is the first tile of the shadcn dashboard example, reproduced with the same numbers in thousands of generated apps. The chart is the Recharts documentation area chart with its `colorUv` gradient and `#8884d8` lavender. `type="monotone"` smooths the line, which invents values between real points.

#### Rules

1. A stat tile has three lines: label (14px, `--ink-2`), value (32px, weight 500, tabular figures), comparison (14px). No icon in the corner.
2. The comparison names both the absolute change and the period: "+EUR 7,602 vs September (+20.1%)". A percentage alone hides whether the base was 10 or 10 million.
3. Color the comparison by meaning, not by sign. Churn going up is bad; costs going down is good. When the metric has no direction, leave it `--ink-2`.
4. State freshness on the row of tiles, once: "Figures to 14 Oct 23:59 UTC".
5. At most 4 tiles in a row, 5 on a 1440px screen. Separate them with 1px vertical rules or 16px gaps, not with a card per tile.
6. Bar charts start at zero. Line charts may start elsewhere, with the axis labelled.
7. Lines are 1.5px to 2px, straight segments between points. No `monotone` smoothing, no area fill, no gradient.
8. Gridlines are horizontal only, 1px `--rule`, 3 to 5 of them. No vertical gridlines on time series.
9. Tooltips show the exact value with units and the exact date. Every chart has a data table available under it, in a `<details>` titled "Show data".
10. No pie or donut past 5 slices. No 3D. No dual y-axes.

#### Reference build

```html
<section class="stats" aria-labelledby="stats-h">
  <h2 id="stats-h" class="stats-h">October to date <span>Figures to 14 Oct 23:59 UTC</span></h2>
  <dl class="stat-row">
    <div class="stat">
      <dt>Revenue</dt>
      <dd class="stat-value">EUR 45,231</dd>
      <dd class="stat-delta is-good">+EUR 7,602 vs Sep (+20.1%)</dd>
    </div>
    <div class="stat">
      <dt>Churned accounts</dt>
      <dd class="stat-value">31</dd>
      <dd class="stat-delta is-bad">+9 vs Sep (+40.9%)</dd>
    </div>
  </dl>
  <figure class="chart">
    <svg viewBox="0 0 320 120" role="img" aria-label="Daily revenue, 1 to 14 October, from EUR 2,900 to EUR 3,640">
      <g class="grid"><line x1="0" y1="20" x2="320" y2="20"/><line x1="0" y1="60" x2="320" y2="60"/><line x1="0" y1="100" x2="320" y2="100"/></g>
      <polyline class="series" points="0,82 24,76 49,79 73,70 98,66 122,71 147,58 171,52 196,55 220,47 245,40 269,44 294,33 318,28"/>
      <text x="318" y="20" text-anchor="end">EUR 3,640</text>
    </svg>
    <figcaption>Daily revenue, EUR. Source: billing ledger.</figcaption>
  </figure>
</section>
```

```css
.stats-h { font: 600 16px/1.25 var(--font-sans); margin: 0 0 12px; }
.stats-h span { font-weight: 400; font-size: 14px; color: var(--ink-3); margin-left: 8px; }
.stat-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); margin: 0; border-top: 1px solid var(--rule); }
.stat { padding: 16px 16px 16px 0; }
.stat + .stat { padding-left: 16px; border-left: 1px solid var(--rule); }
.stat dt { font-size: 14px; color: var(--ink-2); }
.stat dd { margin: 0; }
.stat-value { font: 500 32px/1.15 var(--font-sans); font-variant-numeric: tabular-nums; color: var(--ink); margin-top: 4px; }
.stat-delta { font-size: 14px; color: var(--ink-2); font-variant-numeric: tabular-nums; }
.stat-delta.is-good { color: var(--ok); }
.stat-delta.is-bad { color: var(--bad); }
.chart { margin: 24px 0 0; }
.chart svg { width: 100%; height: auto; overflow: visible; }
.chart .grid line { stroke: var(--rule); stroke-width: 1; }
.chart .series { fill: none; stroke: var(--ink); stroke-width: 2; stroke-linejoin: round; }
.chart text { font: 12px var(--font-sans); fill: var(--ink-2); }
.chart figcaption { font-size: 12px; color: var(--ink-3); margin-top: 8px; }
```

#### States

- Hover on a chart: a 1px `--ink-3` vertical rule at the nearest point and a tooltip with the value and date. No enlarged glowing dot.
- Loading: the tile prints its label and "Loading" in place of the value; the chart area keeps its height with the axis drawn.
- No data: "No revenue recorded in October yet." inside the chart frame, axes still visible.
- Error: "Could not load revenue. Retry." with the last known value and its date.

#### Copy

```slop
Total Revenue
$45,231.89
+20.1% from last month
```

- Revenue, October to date
- EUR 45,231
- +EUR 7,602 vs September (+20.1%)

#### Checklist

- Tiles: label, value, absolute and relative change with the period.
- Delta color by meaning; freshness stated once.
- No icons in tiles, no card per tile.
- Straight 2px lines, no area fill, no smoothing, horizontal gridlines only.

### 4.9 Checkboxes, radios and switches

#### What the machine produces

```slop
<div onClick={() => setOn(!on)} className={`relative h-7 w-14 cursor-pointer rounded-full transition-colors duration-300 ${on ? "bg-gradient-to-r from-indigo-500 to-purple-500" : "bg-gray-200"}`}>
  <div className={`absolute top-0.5 h-6 w-6 rounded-full bg-white shadow-md transition-transform duration-300 ${on ? "translate-x-7" : "translate-x-0.5"}`} />
</div>
<span className="text-sm text-gray-600">I agree to the Terms of Service</span>
```

A switch made of two divs with a click handler: no role, no keyboard access, no label association, a 300ms slide and a gradient track. It is used for consent, which is a checkbox decision applied on submit.

#### Rules

1. Use native `<input type="checkbox">` and `<input type="radio">`, styled with `accent-color: var(--accent)`. If you rebuild the visual with `appearance: none`, keep the input element.
2. Box size 16px to 20px. The clickable area is the whole `<label>`, at least 24px tall, with 8px between control and text.
3. Checkbox: independent yes or no choices, applied when the form is saved. Consent, opt-ins and filters are checkboxes.
4. Radio: 2 to 5 mutually exclusive options, all visible. Past 5, use a select (4.15). Always one option preselected unless no answer is a valid answer.
5. Switch: a setting that takes effect the moment it changes, with no save button. Use `<input type="checkbox" role="switch">`. Track 36px by 20px, thumb 14px, a printed "On" or "Off" next to it.
6. Group related controls in `<fieldset>` with a `<legend>` that asks the question.
7. Never pre-check consent, marketing or data-sharing boxes. In the EU this is not valid consent (CJEU, Planet49, 2019).
8. The thumb moves in 100ms `ease-out`, or instantly under reduced motion.

#### Reference build

```html
<fieldset class="choice">
  <legend>Send invoices by</legend>
  <label><input type="radio" name="send" value="email" checked> Email, as PDF attachment</label>
  <label><input type="radio" name="send" value="link"> Email, as link to the portal</label>
  <label><input type="radio" name="send" value="post"> Post (EUR 1.20 per letter)</label>
</fieldset>

<label class="check"><input type="checkbox" name="news"> Email me product changes, about 1 per month</label>

<label class="switch">
  <input type="checkbox" role="switch" checked>
  <span class="switch-track" aria-hidden="true"></span>
  <span class="switch-label">Auto-send reminders</span>
  <span class="switch-state" aria-hidden="true"></span>
</label>
```

```css
.choice { margin: 0; padding: 0; border: 0; }
.choice legend { padding: 0; margin-bottom: 8px; font-weight: 600; }
.choice label, .check { display: flex; align-items: center; gap: 8px; min-height: 32px; cursor: pointer; }
.choice input, .check input { width: 18px; height: 18px; margin: 0; accent-color: var(--accent); }
:is(.choice, .check) input:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }

.switch { display: inline-flex; align-items: center; gap: 8px; min-height: 32px; cursor: pointer; }
.switch input { position: absolute; opacity: 0; width: 36px; height: 20px; margin: 0; }
.switch-track {
  position: relative; width: 36px; height: 20px; flex: none;
  background: var(--paper-3); border: 1px solid var(--ink-3); border-radius: 10px;
}
.switch-track::after {
  content: ""; position: absolute; top: 2px; left: 2px; width: 14px; height: 14px;
  background: var(--ink-2); border-radius: 50%; transition: transform 100ms ease-out;
}
.switch input:checked + .switch-track { background: var(--accent); border-color: var(--accent); }
.switch input:checked + .switch-track::after { transform: translateX(16px); background: var(--accent-ink); }
.switch input:focus-visible + .switch-track { outline: 2px solid var(--focus); outline-offset: 2px; }
.switch input:disabled ~ * { opacity: 0.45; cursor: not-allowed; }
.switch-state { font-size: 14px; color: var(--ink-2); min-width: 2.5em; }
.switch-state::before { content: "Off"; }
.switch input:checked ~ .switch-state::before { content: "On"; }
@media (prefers-reduced-motion: reduce) { .switch-track::after { transition: none; } }
```

The track border is `--ink-3`, which measures 4.6:1 on `--paper`, so the off state passes the 3:1 non-text contrast rule (WCAG 1.4.11).

#### States

- Focus-visible: 2px outline at 2px offset around the box or the track.
- Checked, unchecked, indeterminate: each visible without color (check mark, empty box, dash).
- Disabled: 45% opacity plus text saying why ("Requires a verified domain").
- Error: a `--bad` line under the legend, linked to the group with `aria-describedby`.

#### Copy

```slop
I agree to the Terms of Service and Privacy Policy and consent to receive marketing communications
Enable notifications
Toggle dark mode
```

- I accept the Terms of Service (link opens in this tab)
- Email me product changes, about 1 per month
- Auto-send reminders 3 days after the due date

Split combined consent into separate boxes, one decision each.

#### Checklist

- Native inputs, real labels, `fieldset` and `legend` for groups.
- Checkbox for submit-time choices, switch only for instant settings.
- Radios for 2 to 5 options, one preselected when valid.
- No pre-checked consent; combined consent split.

### 4.10 Code blocks

#### What the machine produces

```slop
<div className="overflow-hidden rounded-2xl bg-gradient-to-br from-slate-900 to-slate-800 shadow-2xl ring-1 ring-white/10">
  <div className="flex items-center gap-2 border-b border-white/10 px-4 py-3">
    <div className="h-3 w-3 rounded-full bg-red-500" />
    <div className="h-3 w-3 rounded-full bg-yellow-500" />
    <div className="h-3 w-3 rounded-full bg-green-500" />
    <span className="ml-auto text-xs text-slate-400">terminal</span>
  </div>
  <pre className="p-6 font-mono text-sm text-green-400">
    <TypeAnimation sequence={["$ npm install acme-sdk", 1000]} />
  </pre>
</div>
```

The fake macOS window with three traffic-light dots, a slate gradient, `shadow-2xl`, green-on-black terminal text and a typing animation. It shows one line of code inside 60px of decoration, and the `$` prompt is copied along with the command when someone selects it.

#### Rules

1. Block: `--paper-2` background, 1px `--rule` border, `var(--radius)` corners, 16px padding, `var(--font-mono)` at 14px with 1.5 line height. Follow the page theme; do not force a dark block on a light page.
2. No window chrome, no traffic-light dots, no typing animation, no glow.
3. Long lines scroll horizontally inside the block (`overflow-x: auto`).
4. A label row above the block gives the filename or language when it helps: `src/config.ts`, 12px `--ink-2`, 1px rule below it.
5. Copy button: text "Copy", top-right inside the label row, 28px tall. After a click it reads "Copied" for 2000ms, announced through `role="status"`. It copies the code without prompts, line numbers or output lines.
6. Shell examples put the prompt in CSS (`::before`), never in the text, so selection and copy get the command alone.
7. Syntax colors: at most 4 hues plus `--ink`, each at 4.5:1 or better on `--paper-2`. Comments in `--ink-3`, not italic grey at 3:1.
8. Inline code: `--paper-2` background, 0 4px padding, 0.9em, 2px radius, no border.

#### Reference build

```html
<figure class="code">
  <figcaption class="code-head">
    <span>Install</span>
    <button class="code-copy" type="button" data-copy="npm install @halden/sdk@4.2.0">Copy</button>
    <span class="code-status visually-hidden" role="status"></span>
  </figcaption>
  <pre><code><span class="sh">npm install @halden/sdk@4.2.0</span></code></pre>
</figure>
```

```css
.code { margin: 16px 0; border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper-2); }
.code-head {
  display: flex; align-items: center; justify-content: space-between; gap: 8px;
  padding: 4px 8px 4px 16px; border-bottom: 1px solid var(--rule);
  font: 12px/1.5 var(--font-sans); color: var(--ink-2);
}
.code-copy {
  height: 28px; padding: 0 8px; font: 500 12px var(--font-sans); color: var(--ink);
  background: transparent; border: 1px solid var(--rule); border-radius: var(--radius); cursor: pointer;
}
.code-copy:hover { border-color: var(--rule-strong); }
.code-copy:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.code pre { margin: 0; padding: 16px; overflow-x: auto; tab-size: 2; }
.code code { font: 14px/1.5 var(--font-mono); color: var(--ink); }
.code .sh::before { content: "$ "; color: var(--ink-3); user-select: none; }
:not(pre) > code { padding: 0 4px; font-size: 0.9em; background: var(--paper-2); border-radius: var(--radius); }
```

#### States

- Copy hover: border to `--rule-strong`. Focus-visible: 2px outline.
- Copied: the label changes for 2000ms; no toast, no check glyph.
- Copy failed: the code is selected and the status says "Press Ctrl C to copy".

#### Copy

```slop
Get started in seconds
// Magic happens here
Copied to clipboard!
```

- Install (Node 18 or later)
- `// Retries 3 times with 500ms backoff`
- Copied

#### Checklist

- Block follows the page theme on `--paper-2`, 14px mono, 1.5 line height.
- No window dots, no typing effect, no gradient frame.
- Prompts and line numbers excluded from selection and copy.
- "Copy" becomes "Copied" for 2 seconds, announced politely.

### 4.11 Command palettes

#### What the machine produces

```slop
<Dialog open={open}>
  <div className="fixed inset-0 bg-black/40 backdrop-blur-sm" />
  <Command className="fixed left-1/2 top-1/4 w-full max-w-2xl -translate-x-1/2 rounded-2xl border border-white/10 bg-white/80 shadow-2xl backdrop-blur-xl">
    <div className="flex items-center gap-2 px-4">
      <Sparkles className="h-5 w-5 text-violet-500" />
      <Command.Input placeholder="Ask AI anything or search..." className="h-14 bg-transparent" />
      <kbd className="rounded-md bg-gray-100 px-2 text-xs"><CommandIcon className="inline h-3 w-3" />K</kbd>
    </div>
  </Command>
</Dialog>
```

The cmdk demo with a frosted `bg-white/80 backdrop-blur-xl` panel, `shadow-2xl`, and a sparkles icon that turns the search field into "Ask AI anything".

#### Rules

1. Open with Ctrl K on Windows and Linux, Cmd K on macOS, and from a visible "Search or run a command" button in the header.
2. Panel: 640px wide at most, top edge at 15vh. 1px `--rule-strong` border, `--paper` fill, `var(--radius)`.
3. Scrim: `rgb(20 20 18 / 0.4)`, no blur.
4. Input: 48px tall, 16px text, no icon unless it is a 16px search glyph.
5. Results: rows 40px tall, at most 8 visible, then the list scrolls. Each row: label, then the context in `--ink-3` ("Invoice 1042, Halden Freight"), then the shortcut right-aligned in 12px mono.
6. Empty query shows the 5 most recent commands, then 3 pinned ones.
7. Filter 1,000 items in under 50ms per keystroke; past that, debounce at 120ms.
8. Keys: Up and Down move and wrap, Enter runs, Esc clears the input, and Esc on an empty input closes. Focus returns to the element that had it before.
9. Pattern: `role="combobox"` on the input, `role="listbox"` on the list, `aria-activedescendant` pointing at the active option. Focus stays in the input.

#### Reference build

```html
<dialog class="palette" aria-label="Command palette">
  <input class="palette-input" role="combobox" aria-expanded="true" aria-controls="palette-list"
         aria-activedescendant="cmd-2" aria-autocomplete="list" placeholder="Search or run a command" autocomplete="off">
  <ul class="palette-list" id="palette-list" role="listbox">
    <li class="palette-head" role="presentation">Recent</li>
    <li id="cmd-1" role="option" aria-selected="false">New invoice <kbd>N</kbd></li>
    <li id="cmd-2" role="option" aria-selected="true">Go to <b>Inv</b>oice 1042 <span class="ctx">Halden Freight</span></li>
    <li id="cmd-3" role="option" aria-selected="false">Export <b>inv</b>oices as CSV <kbd>Ctrl E</kbd></li>
  </ul>
</dialog>
```

```css
.palette {
  width: min(640px, calc(100vw - 32px)); margin: 15vh auto 0; padding: 0;
  background: var(--paper); color: var(--ink);
  border: 1px solid var(--rule-strong); border-radius: var(--radius);
}
.palette::backdrop { background: rgb(20 20 18 / 0.4); }
.palette-input {
  width: 100%; height: 48px; padding: 0 16px; border: 0; border-bottom: 1px solid var(--rule);
  font: 16px var(--font-sans); color: var(--ink); background: transparent;
}
.palette-input:focus-visible { outline: 2px solid var(--focus); outline-offset: -2px; }
.palette-list { max-height: 320px; overflow-y: auto; margin: 0; padding: 4px 0; list-style: none; }
.palette-head { padding: 8px 16px 4px; font-size: 12px; color: var(--ink-3); }
[role="option"] { display: flex; align-items: center; gap: 8px; height: 40px; padding: 0 16px; cursor: pointer; }
[role="option"] b { font-weight: 600; }
[role="option"] .ctx { color: var(--ink-3); font-size: 14px; }
[role="option"] kbd { margin-left: auto; font: 12px var(--font-mono); color: var(--ink-3); }
[role="option"]:hover { background: var(--paper-2); }
[role="option"][aria-selected="true"] { background: var(--paper-3); }
```

#### States

- Active option: `--paper-3` fill. Hovered option: `--paper-2`.
- No results: one line with the query quoted and one fallback action.
- Slow command: the row shows "Running..." for up to 1 second, then the palette closes and the page shows the result.

#### Copy

```slop
Ask AI anything...
What would you like to do today?
No results found.
```

- Search or run a command
- No commands match "invocie". Search all records for "invocie"
- Go to Invoice 1042, Halden Freight

#### Checklist

- Ctrl K and Cmd K, plus a visible header button.
- Solid panel, plain scrim, no blur, 640px max.
- Recent commands on an empty query.
- Combobox and listbox roles, active descendant, focus returned on close.
