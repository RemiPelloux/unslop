### 4.19 Forms and text inputs

#### What the machine produces

```slop
<form onSubmit={handleSubmit} className="space-y-6 rounded-2xl bg-white p-8 shadow-xl">
  <div className="relative">
    <Mail className="absolute left-4 top-3.5 h-5 w-5 text-gray-400" />
    <input type="email" placeholder="Enter your email" className="peer w-full rounded-xl border border-gray-200 py-3 pl-12 pr-4 placeholder-transparent focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/20" />
    <label className="absolute left-12 top-3 text-sm text-gray-500 transition-all peer-placeholder-shown:text-base peer-focus:-top-2.5 peer-focus:text-xs">Email</label>
  </div>
  <button className="w-full rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 py-3 text-white">Submit</button>
</form>
```

A floating label that shrinks into the border on focus, an envelope icon that repeats the word "Email", a `gray-200` border that measures about 1.3:1 against white, the `ring-4 ring-indigo-500/20` halo, a gradient "Submit", and a form floating in a `shadow-xl` card. Errors arrive as a toast after submit.

#### Rules

1. Labels sit above the input, 14px weight 500, 4px gap. Never inside the field, never only as a placeholder.
2. Input height 40px, 0 12px padding, 16px text. Below 16px, iOS Safari zooms the page on focus.
3. Border 1px `--ink-3` (4.6:1 on `--paper`). WCAG 1.4.11 asks 3:1 for the boundary of a control; `--rule` does not reach it.
4. Field width follows the expected answer: postcode 8ch, year 6ch, IBAN 34ch, email 32ch. Not every field at 100%.
5. Hints go between label and input in 14px `--ink-2`, linked with `aria-describedby`.
6. Mark optional fields with "(optional)" in the label. Do not scatter red asterisks.
7. Validate on blur and on submit, never on each keystroke. Remove an error as soon as the input becomes valid.
8. Errors go under the field in `--bad`, starting with what to do: "Enter an IBAN that starts with 2 letters". Set `aria-invalid="true"` and add the error id to `aria-describedby`.
9. On submit with more than 2 errors, show a summary at the top listing each error as a link to its field, and move focus to the summary.
10. Set `autocomplete`, `inputmode` and `type` on every field: `email`, `tel`, `postal-code`, `one-time-code`.
11. Keep the submit button enabled; let the click run validation and show what is missing.

#### Reference build

```html
<div class="field">
  <label for="iban">IBAN</label>
  <p class="hint" id="iban-hint">On your bank statement. 22 characters for Germany.</p>
  <input class="input" id="iban" name="iban" autocomplete="off" spellcheck="false"
         aria-describedby="iban-hint iban-err" aria-invalid="true" style="width: 34ch" value="DE89 3704">
  <p class="error" id="iban-err">Enter the full IBAN. This one has 8 of 22 characters.</p>
</div>
<div class="field">
  <label for="ref">Reference <span class="opt">(optional)</span></label>
  <input class="input" id="ref" name="ref" style="width: 24ch">
</div>
```

```css
.field { display: grid; gap: 4px; margin-bottom: 24px; }
.field label { font: 500 14px/1.4 var(--font-sans); color: var(--ink); }
.field .opt { font-weight: 400; color: var(--ink-2); }
.hint { margin: 0; font-size: 14px; color: var(--ink-2); max-width: 60ch; }
.input {
  max-width: 100%; height: 40px; padding: 0 12px;
  font: 16px var(--font-sans); color: var(--ink); background: var(--paper);
  border: 1px solid var(--ink-3); border-radius: var(--radius);
}
.input::placeholder { color: var(--ink-3); }
.input:hover { border-color: var(--ink); }
.input:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.input[aria-invalid="true"] { border-color: var(--bad); border-width: 2px; padding: 0 11px; }
.input:disabled, .input[readonly] { background: var(--paper-2); border-color: var(--rule); color: var(--ink-2); }
.error { margin: 0; font-size: 14px; color: var(--bad); }
```

The error border goes to 2px so the change is visible without color; the padding drops by 1px so the text does not shift.

#### States

- Hover: border to `--ink`. Focus-visible: 2px outline at 2px offset.
- Invalid: 2px `--bad` border plus the error line. Valid again: both removed at once; no green tick.
- Disabled and read-only: `--paper-2` fill, `--rule` border. Read-only text stays selectable.

#### Copy

```slop
Please enter a valid email address.
This field is required.
Enter your email
```

- Enter an email address with an @, like name@company.com
- Enter your postcode. We use it to work out VAT.
- IBAN (on your bank statement)

#### Checklist

- Labels above, 16px input text, 40px fields.
- Field boundary at 3:1 or more.
- Widths match the answer length.
- Errors under fields, on blur and submit, with a summary past 2 errors.

### 4.20 Headers and top navigation

#### What the machine produces

```slop
<header className="sticky top-0 z-50 border-b border-white/20 bg-white/70 backdrop-blur-lg">
  <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
    <span className="bg-gradient-to-r from-indigo-500 to-purple-600 bg-clip-text text-xl font-bold text-transparent">Acme</span>
    <nav className="hidden gap-8 md:flex">{["Features", "Pricing", "About", "Blog"].map((l) => <a className="text-sm text-gray-600 hover:text-gray-900">{l}</a>)}</nav>
    <div className="flex gap-3"><Button variant="ghost">Sign in</Button><Button className="rounded-full">Get Started</Button></div>
  </div>
</header>
```

The frosted sticky header (`bg-white/70 backdrop-blur-lg`), a wordmark in `bg-clip-text` gradient, centered links with no current-page marker, and a pill "Get Started". Text over translucent blur changes contrast with whatever scrolls behind it.

#### Rules

1. Height 56px in apps, 64px on marketing pages. Solid `--paper` fill, 1px `--rule` bottom border. No blur, no transparency.
2. At most 6 top-level links. Labels are nouns for places: "Pricing", "Docs", "Customers".
3. The current section gets `aria-current="page"`, `--ink` text and a 2px `--ink` bar along the header's bottom edge.
4. One call to action on the right, secondary style in apps, primary on marketing pages. "Sign in" is a text link.
5. A skip link is the first focusable element: "Skip to content", visible on focus.
6. Below the width where the links fit, replace them with a button labelled "Menu" that opens a full-width panel. Not a lone hamburger icon.

#### Reference build

```html
<a class="skip" href="#main">Skip to content</a>
<header class="hdr">
  <a class="hdr-logo" href="/"><img src="/logo.svg" alt="Halden" width="88" height="20"></a>
  <nav aria-label="Main">
    <ul class="hdr-nav">
      <li><a href="/product">Product</a></li>
      <li><a href="/pricing" aria-current="page">Pricing</a></li>
      <li><a href="/docs">Docs</a></li>
    </ul>
  </nav>
  <div class="hdr-end"><a href="/login">Sign in</a><a class="btn btn-primary btn-sm" href="/signup">Start trial</a></div>
</header>
```

```css
.skip { position: absolute; left: 16px; top: -48px; padding: 8px 12px; background: var(--ink); color: var(--paper); z-index: 10; }
.skip:focus { top: 8px; }
.hdr {
  position: sticky; top: 0; z-index: 5; display: flex; align-items: center; gap: 32px;
  height: 64px; padding: 0 24px; background: var(--paper); border-bottom: 1px solid var(--rule);
}
.hdr-nav { display: flex; gap: 24px; margin: 0; padding: 0; list-style: none; }
.hdr-nav a { display: flex; align-items: center; height: 64px; font-size: 15px; color: var(--ink-2); text-decoration: none; border-bottom: 2px solid transparent; margin-bottom: -1px; }
.hdr-nav a:hover { color: var(--ink); }
.hdr-nav a[aria-current="page"] { color: var(--ink); border-bottom-color: var(--ink); }
.hdr a:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.hdr-end { margin-left: auto; display: flex; align-items: center; gap: 16px; font-size: 15px; }
.hdr-end > a:first-child { color: var(--ink); }
```

#### States

- Link hover: `--ink-2` to `--ink`. Current: ink plus 2px bar.
- Menu open (narrow screens): the button reads "Close menu", `aria-expanded="true"`, and the panel sits under the header on `--paper` with 48px rows.
- Signed in: the right side becomes the account avatar button (4.3) with an accessible name.

#### Copy

```slop
Get Started
Solutions
Resources
```

- Product / Pricing / Docs / Customers
- Sign in / Start trial
- Skip to content

#### Checklist

- Solid paper header, 1px bottom rule, no blur.
- 6 links at most, nouns, current page marked.
- One call to action; sign in as a link.
- Skip link first; "Menu" button with text on narrow screens.

### 4.21 Hero sections

#### What the machine produces

```slop
<section className="relative overflow-hidden bg-slate-950 py-32 text-center">
  <div className="absolute left-1/2 top-0 h-[600px] w-[1200px] -translate-x-1/2 rounded-full bg-indigo-500/30 blur-3xl" />
  <span className="inline-flex items-center gap-2 rounded-full border border-indigo-500/30 bg-indigo-500/10 px-4 py-1.5 text-sm text-indigo-300">
    <Sparkles className="h-4 w-4" /> Now with AI <ArrowRight className="h-4 w-4" />
  </span>
  <h1 className="mt-8 bg-gradient-to-r from-white via-indigo-200 to-purple-400 bg-clip-text text-6xl font-bold tracking-tight text-transparent md:text-7xl">
    Build the future of work, faster
  </h1>
  <p className="mx-auto mt-6 max-w-2xl text-lg text-slate-400">The all-in-one platform that helps teams ship faster with AI-powered workflows.</p>
  <div className="mt-10 flex justify-center gap-4">
    <Button size="lg" className="rounded-full bg-indigo-500 shadow-lg shadow-indigo-500/50">Get Started Free</Button>
    <Button size="lg" variant="outline" className="rounded-full">Watch Demo</Button>
  </div>
  <img src="/dashboard.png" className="mx-auto mt-16 rounded-2xl border border-white/10 shadow-2xl [transform:perspective(1200px)_rotateX(12deg)]" />
</section>
```

Five defaults stacked: a radial indigo glow (`blur-3xl` on a `bg-indigo-500/30` blob), a "Now with AI" pill with sparkles and an arrow, a headline in `bg-clip-text` gradient that names no product, two pill buttons ("Get Started Free" and "Watch Demo"), and a dashboard screenshot tilted with `rotateX` and floating on `shadow-2xl`. Readers skip it the way they skip banner ads.

#### Rules

1. The headline says what the product does and for whom, in 10 words or fewer: "Invoicing for freight companies that bill by the pallet." Left-aligned, 40px to 56px, weight 600, line height 1.1, max 20ch per line, solid `--ink`.
2. One supporting sentence, 18px or 21px, `--ink-2`, max 52ch, with a number or a constraint in it.
3. One primary button and, at most, one text link. The link leads somewhere specific ("See pricing", "Read the API docs"), not "Watch demo".
4. No pill above the headline. If there is news, write one line of text with a date as a link: "12 Oct: CSV import with tax lines".
5. No glow, no grid backdrop, no noise texture, no blob. The background is `--paper`.
6. The image is the product at real size, or a cropped detail at 1:1 pixels, inside a 1px `--rule` border. No tilt, no perspective, no floating, no browser chrome mockup.
7. Height follows content. Not `min-height: 100vh`; the next section should show above the fold at 1440 by 900.
8. Proof, if any, is specific and sourced: "Used by 412 freight firms in 9 countries" with the count updated from data, not "Trusted by thousands".

#### Reference build

```html
<section class="hero">
  <div class="hero-text">
    <p class="hero-news"><a href="/changelog#2026-10-12">12 Oct: CSV import with tax lines</a></p>
    <h1>Invoicing for freight companies that bill by the pallet.</h1>
    <p class="hero-sub">Turn delivery notes into invoices with VAT per country. 412 firms in 9 countries send 38,000 invoices a month with it.</p>
    <div class="hero-actions">
      <a class="btn btn-primary btn-lg" href="/signup">Start 14-day trial</a>
      <a href="/pricing">See pricing</a>
    </div>
  </div>
  <figure class="hero-shot">
    <img src="/shots/invoice-1042.png" width="1200" height="760" alt="Invoice editor showing 14 pallet lines grouped by delivery note, with German and Austrian VAT totals.">
  </figure>
</section>
```

```css
.hero { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 48px; align-items: start; padding: 64px 24px 96px; max-width: 1280px; margin: 0 auto; }
.hero h1 { margin: 0; font: 600 clamp(40px, 5vw, 56px)/1.1 var(--font-sans); color: var(--ink); max-width: 20ch; letter-spacing: -0.01em; }
.hero-news { margin: 0 0 24px; font-size: 14px; }
.hero-news a { color: var(--ink-2); text-underline-offset: 3px; }
.hero-sub { margin: 24px 0 32px; font-size: 21px; line-height: 1.45; color: var(--ink-2); max-width: 52ch; }
.hero-actions { display: flex; align-items: center; gap: 24px; }
.hero-actions > a:last-child { color: var(--ink); text-underline-offset: 3px; }
.hero-shot { margin: 0; border: 1px solid var(--rule); background: var(--paper-2); }
.hero-shot img { display: block; width: 100%; height: auto; }
@media (max-width: 900px) { .hero { grid-template-columns: 1fr; padding-top: 48px; } }
```

#### States

- Primary button: as 4.6. Text link: underline thickens to 2px on hover.
- Image loading: the figure reserves space with `width` and `height`, so nothing jumps; `--paper-2` shows until the image arrives.
- Narrow screens: one column, headline at 40px, image below the actions.

#### Copy

```slop
Now with AI
Build the future of work, faster
The all-in-one platform that helps teams ship faster with AI-powered workflows.
```

- Invoicing for freight companies that bill by the pallet.
- Turn delivery notes into invoices with VAT per country.
- Start 14-day trial / See pricing

#### Checklist

- Headline names the product's job and audience, 10 words or fewer, solid ink.
- One button, one text link.
- No pill, no glow, no grid backdrop, no gradient text.
- Real screenshot, flat, 1px border, no tilt.

### 4.22 Links

#### What the machine produces

```slop
<p className="text-gray-600">
  To learn more about our pricing, <a href="/pricing" className="font-medium text-indigo-600 hover:text-indigo-500">click here</a>.
</p>
<a href="/docs" className="group inline-flex items-center gap-1 text-sm font-semibold text-indigo-600">
  Learn more <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
</a>
```

Links told apart by `indigo-600` color alone, underline removed by Tailwind's preflight, "click here" as link text, and "Learn more" with a sliding arrow. Out of context, a screen reader's link list reads "click here, Learn more, Learn more, Learn more".

#### Rules

1. Links in running text are underlined. Color alone fails WCAG 1.4.1 unless the contrast between link and body text is 3:1, which `--accent` against `--ink` is not.
2. Underline 1px at `text-underline-offset: 0.2em`. Hover thickens it to 2px. No color change needed.
3. Link text names the destination: "the pricing page", "invoice 1042", "Read the API rate limits". Never "click here", "here", "this link".
4. Navigation and button-like links may drop the underline only where position makes them obvious: header, footer columns, tabs.
5. Name the file and size for downloads: "Annual report (PDF, 2.4 MB)".
6. Open links in the same tab. Use a new tab only for help pages opened from inside a form being filled, and say so: "(opens in new tab)".

#### Reference build

```html
<p>Prices are on <a href="/pricing">the pricing page</a>. The <a href="/files/report-2025.pdf">2025 annual report (PDF, 2.4 MB)</a> lists every fee change.</p>
```

```css
a { color: var(--ink); text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 0.2em; }
a:hover { text-decoration-thickness: 2px; }
a:visited { color: var(--ink-2); }
a:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; text-decoration: none; }
a:active { color: var(--accent); }
```

#### States

- Hover: 2px underline. Focus-visible: outline replaces the underline. Active: accent for the press.
- Visited: `--ink-2` in documentation and long reading pages only.
- Broken or disabled: do not render as a link; write plain text and say why if it matters.

#### Copy

```slop
Click here
Learn more
Read more
```

- the pricing page
- 2025 annual report (PDF, 2.4 MB)
- Read the API rate limits

#### Checklist

- Underlined in running text; 1px, 2px on hover.
- Link text names the destination.
- File type and size on downloads.
- Same tab by default; new tab announced.

### 4.23 Lists

#### What the machine produces

```slop
<ul className="space-y-4">
  <li className="flex items-start gap-3"><CheckCircle2 className="h-6 w-6 flex-none text-green-500" /><span><strong>Seamless Integration:</strong> Connect with your favorite tools effortlessly.</span></li>
  <li className="flex items-start gap-3"><CheckCircle2 className="h-6 w-6 flex-none text-green-500" /><span><strong>Advanced Analytics:</strong> Gain actionable insights in real time.</span></li>
  <li className="flex items-start gap-3"><CheckCircle2 className="h-6 w-6 flex-none text-green-500" /><span><strong>Enterprise Security:</strong> Bank-level encryption keeps your data safe.</span></li>
</ul>
```

Green check-circle icons as bullets, 16px of space between one-line items, and the language-model list signature: a bold Title Case label, a colon, then a sentence that restates the label.

#### Rules

1. Use `<ul>` with the native disc or a 6px hyphen marker, `<ol>` only when order matters (steps, rankings), `<dl>` for term and value pairs.
2. Marker in `--ink-3`, indent 1.25em, 4px between single-line items, 8px between multi-line items.
3. No icons as bullets. A check mark claims a verified result; a feature list is not one.
4. Do not open every item with "Bold label: sentence".
5. Items share grammar: all noun phrases or all sentences starting with a verb.
6. 3 to 7 items. Longer lists get subheadings or become a table.

#### Reference build

```html
<ul class="list">
  <li>Imports CSV, XLSX and JSON up to 50 MB</li>
  <li>Calculates VAT for 27 EU countries and Switzerland</li>
  <li>Sends reminders 3, 10 and 30 days after the due date</li>
</ul>
<dl class="pairs">
  <div><dt>Plan</dt><dd>Team, 12 seats</dd></div>
  <div><dt>Renews</dt><dd>1 Feb 2027</dd></div>
</dl>
```

```css
.list { margin: 0 0 16px; padding-left: 1.25em; max-width: 66ch; }
.list li { margin-bottom: 4px; padding-left: 4px; }
.list li::marker { color: var(--ink-3); }
.list.is-dash { list-style: none; padding-left: 0; }
.list.is-dash li { position: relative; padding-left: 1.25em; }
.list.is-dash li::before { content: ""; position: absolute; left: 0; top: 0.75em; width: 6px; border-top: 1px solid var(--ink-3); }
.pairs { display: grid; gap: 8px; margin: 0; }
.pairs div { display: grid; grid-template-columns: 12ch 1fr; gap: 16px; }
.pairs dt { color: var(--ink-2); }
.pairs dd { margin: 0; color: var(--ink); }
```

#### States

- Lists are static. Interactive lists (selectable rows) follow 4.12 and 4.25.

#### Copy

```slop
Seamless Integration: Connect with your favorite tools effortlessly.
Advanced Analytics: Gain actionable insights in real time.
Enterprise Security: Bank-level encryption keeps your data safe.
```

- Imports CSV, XLSX and JSON up to 50 MB
- Calculates VAT for 27 EU countries and Switzerland
- Encrypts data at rest with AES-256; keys rotate every 90 days

#### Checklist

- Native markers in `--ink-3`; no icon bullets.
- 4px between short items.
- No "Bold label:" on every item.
- Parallel grammar; 3 to 7 items.

### 4.24 Loading and skeletons

#### What the machine produces

```slop
<div className="flex h-screen items-center justify-center">
  <div className="h-12 w-12 animate-spin rounded-full border-4 border-indigo-500 border-t-transparent" />
</div>
<div className="space-y-3">
  <div className="h-4 w-3/4 animate-pulse rounded-full bg-gray-200" />
  <div className="relative h-4 w-1/2 overflow-hidden rounded-full bg-gray-200 before:absolute before:inset-0 before:-translate-x-full before:animate-[shimmer_2s_infinite] before:bg-gradient-to-r before:from-transparent before:via-white/60 before:to-transparent" />
</div>
```

A full-screen spinner for a request that takes 120ms, and `animate-pulse` bars with rounded ends at fixed widths unrelated to the content that will replace them, with a shimmer gradient sweeping across. Both loop forever and say nothing about progress.

#### Rules

1. Under 300ms: show nothing.
2. 300ms to 1 second: keep the old content, set `aria-busy="true"` on the region, and show a short text line: "Loading invoices".
3. Over 1 second for a first load: a static skeleton that matches the real layout (table rows at real column widths, the card grid at real card size) in `--paper-2` blocks with `var(--radius)` corners.
4. No pulse, no shimmer, no spinner loop. Skeletons are still. If the wait has no known length, print the elapsed time once per second after 3 seconds: "Still loading (6 s)".
5. When progress is known, show it as a number and a bar: "Exporting 4,210 of 12,000 rows (35%)".
6. Over 10 seconds: offer "Cancel", and say what continues in the background: "You can leave this page. We will email the file."
7. Announce completion once with `role="status"` ("Loaded 50 invoices"), not each tick.

#### Reference build

```html
<section aria-busy="true" aria-labelledby="inv-h">
  <h2 id="inv-h">Invoices</h2>
  <p class="loading-text" role="status">Loading invoices <span class="elapsed"></span></p>
  <div class="sk-table" aria-hidden="true">
    <div class="sk-row"><span style="width: 6ch"></span><span style="width: 18ch"></span><span class="sk-num" style="width: 9ch"></span></div>
    <div class="sk-row"><span style="width: 6ch"></span><span style="width: 14ch"></span><span class="sk-num" style="width: 8ch"></span></div>
  </div>
  <p class="progress-line">Exporting 4,210 of 12,000 rows (35%)</p>
  <progress max="12000" value="4210">35%</progress>
</section>
```

```css
.loading-text { font-size: 14px; color: var(--ink-2); }
.sk-row { display: flex; align-items: center; gap: 24px; height: 40px; padding: 0 12px; border-bottom: 1px solid var(--rule); }
.sk-row span { display: block; height: 12px; background: var(--paper-2); border-radius: var(--radius); }
.sk-row .sk-num { margin-left: auto; }
.progress-line { margin: 16px 0 4px; font-size: 14px; font-variant-numeric: tabular-nums; }
progress { appearance: none; width: 100%; max-width: 480px; height: 4px; border: 0; background: var(--paper-3); }
progress::-webkit-progress-bar { background: var(--paper-3); }
progress::-webkit-progress-value { background: var(--ink); }
progress::-moz-progress-bar { background: var(--ink); }
```

The `.elapsed` span is filled once per second after 3 seconds, with the same `setInterval` pattern as the feed status in 4.4.

#### States

- Loaded: skeleton replaced in one frame; `aria-busy` removed; status says what loaded.
- Slow: elapsed seconds, then cancel at 10 seconds.
- Failed: the text line turns into the error with a retry button; the skeleton is removed so it does not look like it is still trying.

#### Copy

```slop
Loading...
Hang tight! We're getting things ready for you.
Almost there...
```

- Loading invoices
- Still loading (6 s)
- Exporting 4,210 of 12,000 rows (35%)

#### Checklist

- Nothing under 300ms; text from 300ms; skeleton past 1 second.
- Skeletons match real layout and do not move.
- No pulse, shimmer or spinner loop; elapsed time instead.
- Known progress as number and bar; cancel past 10 seconds.

### 4.25 Menus and context menus

#### What the machine produces

```slop
<DropdownMenu>
  <DropdownMenuTrigger asChild><Button variant="ghost" size="icon"><MoreHorizontal /></Button></DropdownMenuTrigger>
  <DropdownMenuContent className="w-56 rounded-xl shadow-lg animate-in zoom-in-95">
    <DropdownMenuLabel>My Account</DropdownMenuLabel>
    <DropdownMenuItem><User className="mr-2 h-4 w-4" />Profile<DropdownMenuShortcut>Shift Cmd P</DropdownMenuShortcut></DropdownMenuItem>
    <DropdownMenuItem><CreditCard className="mr-2 h-4 w-4" />Billing</DropdownMenuItem>
    <DropdownMenuItem className="text-red-600"><Trash className="mr-2 h-4 w-4" />Delete</DropdownMenuItem>
    <DropdownMenuItem><Settings className="mr-2 h-4 w-4" />Settings</DropdownMenuItem>
  </DropdownMenuContent>
</DropdownMenu>
```

The shadcn `DropdownMenu` demo, down to the "My Account" label: an unlabelled "..." trigger, an icon on every row, a zoom-in animation, and a red "Delete" that sits between two harmless items where a slip of the pointer reaches it.

#### Rules

1. Use the WAI-ARIA menu button pattern: a `<button aria-haspopup="menu" aria-expanded>` and a `role="menu"` list of `role="menuitem"` elements.
2. The trigger has a name that includes the object: "Actions for invoice 1042". A visible label ("Actions") beats an icon alone.
3. Items 32px tall, 14px text, 12px horizontal padding. Panel at least 180px wide, 1px `--rule-strong` border, `--paper` fill, 4px from the trigger.
4. Icons on every item or on none.
5. Groups separated by a 1px `--rule` line with 4px of space. 3 groups and 12 items at most; beyond that, the menu is a page.
6. Destructive items go last, in their own group, in `--bad` text. They open a confirmation (4.14) or run with undo.
7. Shortcuts right-aligned, 12px mono, `--ink-3`, written as text: "Ctrl D", "Shift Ctrl P". Match the platform: "Cmd D" on macOS.
8. Keyboard: Enter, Space and Down open and focus the first item; Up and Down move and wrap; Home and End jump; letters jump by first letter; Esc closes and returns focus to the trigger.
9. Every context menu action is also reachable from a visible control or menu. Right-click is a shortcut, never the only path.
10. Position inside the viewport; flip up or left when it would overflow. One level of submenu at most.

#### Reference build

```html
<div class="menu-wrap">
  <button class="btn btn-secondary btn-sm" id="inv-1042-btn" aria-haspopup="menu" aria-expanded="true" aria-controls="inv-1042-menu">Actions<span class="visually-hidden"> for invoice 1042</span></button>
  <ul class="menu" id="inv-1042-menu" role="menu" aria-labelledby="inv-1042-btn">
    <li role="none"><button role="menuitem" tabindex="-1">Edit<kbd>E</kbd></button></li>
    <li role="none"><button role="menuitem" tabindex="-1">Duplicate<kbd>Ctrl D</kbd></button></li>
    <li role="none"><button role="menuitem" tabindex="-1">Download PDF</button></li>
    <li role="separator"></li>
    <li role="none"><button role="menuitem" tabindex="-1" class="is-bad">Delete invoice</button></li>
  </ul>
</div>
```

```css
.menu-wrap { position: relative; display: inline-block; }
.menu {
  position: absolute; top: calc(100% + 4px); left: 0; min-width: 180px; z-index: 20;
  margin: 0; padding: 4px 0; list-style: none;
  background: var(--paper); border: 1px solid var(--rule-strong); border-radius: var(--radius);
}
.menu [role="menuitem"] {
  display: flex; align-items: center; gap: 16px; width: 100%; height: 32px; padding: 0 12px;
  font: 14px var(--font-sans); color: var(--ink); text-align: left; background: none; border: 0; cursor: pointer;
}
.menu [role="menuitem"]:hover { background: var(--paper-2); }
.menu [role="menuitem"]:focus-visible { background: var(--paper-3); outline: 2px solid var(--focus); outline-offset: -2px; }
.menu [role="menuitem"][aria-disabled="true"] { color: var(--ink-3); cursor: not-allowed; }
.menu kbd { margin-left: auto; font: 12px var(--font-mono); color: var(--ink-3); }
.menu [role="separator"] { margin: 4px 0; border-top: 1px solid var(--rule); }
.menu .is-bad { color: var(--bad); }
```

#### States

- Hover: `--paper-2`. Keyboard focus: `--paper-3` with an inset 2px outline.
- Disabled item: `--ink-3`, `aria-disabled`, still focusable, with the reason in a tooltip ("Paid invoices cannot be edited").
- Checkable item: `role="menuitemcheckbox"` with `aria-checked`, a 16px SVG check on the left.

#### Copy

```slop
My Account
Delete
More options
```

- Actions for invoice 1042
- Duplicate / Download PDF / Delete invoice
- Ctrl D

#### Checklist

- Menu button pattern with roles and keyboard support.
- Trigger names the object; text label preferred over "...".
- 32px items, icons on all or none, 12 items and 3 groups at most.
- Destructive item last, separated, confirmed or undoable.
