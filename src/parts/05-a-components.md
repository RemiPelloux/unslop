## Part 5. Components, N to Z, and Marketing Sections

This Part finishes the component catalogue from Part 4, then covers the sections of a marketing page. Reference builds use the tokens from Part 1.6 and no shadow, gradient or backdrop blur.

### 5.1 Navigation sidebars

#### What the machine produces

```slop
<aside className="flex h-screen w-72 flex-col bg-gradient-to-b from-slate-900 to-indigo-950 p-4 shadow-2xl">
  <div className="mb-8 flex items-center gap-2">
    <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600">
      <SparklesIcon className="h-5 w-5 text-white" />
    </div>
    <span className="text-xl font-bold text-white">Nexora</span>
  </div>
  <nav className="space-y-1">
    <a className="flex items-center gap-3 rounded-xl bg-indigo-500/20 px-4 py-3 text-white shadow-lg shadow-indigo-500/20">
      <HomeIcon className="h-5 w-5" /> Dashboard
    </a>
    <a className="flex items-center gap-3 rounded-xl px-4 py-3 text-slate-400 hover:bg-white/5">
      <ChartBarIcon className="h-5 w-5" /> Insights
      <span className="ml-auto rounded-full bg-gradient-to-r from-pink-500 to-orange-400 px-2 text-xs">New</span>
    </a>
  </nav>
  <div className="mt-auto rounded-2xl bg-gradient-to-br from-indigo-600 to-purple-700 p-4">
    <p className="font-semibold text-white">Upgrade to Pro</p>
    <p className="text-sm text-indigo-200">Unlock all features</p>
  </div>
</aside>
```

This is the dark application shell from the Tailwind UI catalogue, crossed with the shadcn `Sidebar` block. The logo is a gradient `rounded-xl` square holding a sparkle, the active item glows with `shadow-indigo-500/20`, a "New" pill sits on an item nobody asked about, and the bottom of the rail carries an upgrade card that has nothing to do with getting around the product. The dark rail beside a white content area doubles the number of surfaces the eye has to reconcile.

#### Rules

1. Width is 240px expanded and 56px collapsed. No other widths.
2. Background is `--paper-2` with a 1px `--rule` right border. The sidebar uses the same theme as the content. A dark rail on a light app is banned.
3. Items are 32px tall with 8px horizontal padding, 14px text, a 16px icon, and an 8px gap between icon and label.
4. The active item gets three signals: `--paper-3` background, a 2px `--ink` left bar, and weight 500. It also gets `aria-current="page"`. Never mark the active item with color alone.
5. At most 7 items per group and at most 3 groups. Group labels are 12px, `--ink-3`, sentence case, with 16px above them.
6. Counts are allowed only when they change what the user does next, such as unread messages. Show them as plain 12px monospace numerals. "New", "Beta" and "Hot" pills are banned.
7. Plan status and upgrade prompts live in Settings, Billing. Never put a promotional card in the rail.
8. Below 768px the sidebar becomes a drawer opened by a 40px menu button. The drawer enters with `transform: translateX` over 150ms `ease-out`, and with no motion under `prefers-reduced-motion: reduce`.
9. Collapsed, the labels stay in the DOM, clipped for screen readers, and each item shows a tooltip after 500ms of hover (see 5.14).

#### Reference build

```html
<nav class="side" aria-label="Main">
  <a class="side-brand" href="/">Ledgerline</a>
  <ul class="side-list">
    <li><a href="/inbox" aria-current="page"><svg class="i" aria-hidden="true"><use href="#i-inbox"/></svg><span class="side-text">Inbox</span><span class="side-count">12</span></a></li>
    <li><a href="/invoices"><svg class="i" aria-hidden="true"><use href="#i-file"/></svg><span class="side-text">Invoices</span></a></li>
  </ul>
  <p class="side-label" id="nav-reports">Reports</p>
  <ul class="side-list" aria-labelledby="nav-reports">
    <li><a href="/reports/aging"><svg class="i" aria-hidden="true"><use href="#i-clock"/></svg><span class="side-text">Aging</span></a></li>
    <li><a href="/reports/tax"><svg class="i" aria-hidden="true"><use href="#i-percent"/></svg><span class="side-text">Sales tax</span></a></li>
  </ul>
</nav>
```

```css
.side {
  position: sticky; top: 0;
  width: 240px; height: 100vh; overflow-y: auto;
  padding: 12px 8px;
  background: var(--paper-2);
  border-right: 1px solid var(--rule);
  font: 14px/20px var(--font-sans);
}
.side-brand { display: block; padding: 6px 8px; margin-bottom: 16px; color: var(--ink); font-weight: 600; text-decoration: none; }
.side-list { list-style: none; margin: 0 0 16px; padding: 0; }
.side-list a {
  display: flex; align-items: center; gap: 8px;
  height: 32px; padding: 0 8px;
  border-left: 2px solid transparent;
  border-radius: var(--radius);
  color: var(--ink-2); text-decoration: none;
}
.side-list a:hover { background: var(--paper-3); color: var(--ink); }
.side-list a[aria-current="page"] { background: var(--paper-3); border-left-color: var(--ink); color: var(--ink); font-weight: 500; }
.side-list a:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.side-text { overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
.side-count { margin-left: auto; font: 12px var(--font-mono); color: var(--ink-3); }
.side-label { margin: 16px 0 4px; padding: 0 8px; font-size: 12px; color: var(--ink-3); }
.i { width: 16px; height: 16px; flex: none; fill: none; stroke: currentColor; stroke-width: 1.5; }
.side[data-collapsed] { width: 56px; }
.side[data-collapsed] :is(.side-text, .side-label, .side-count) { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
```

#### States

- Current: background, left bar and weight together, plus `aria-current="page"`.
- Collapsed: icons only, labels kept for screen readers, state stored per user so it survives reloads.
- Long labels: truncate with an ellipsis at one line and expose the full label in a tooltip.

#### Copy

```slop
Dashboard / Insights Hub / AI Studio / Magic Workspace
Upgrade to Pro. Unlock all features.
```

Name items after the objects inside them: Inbox, Invoices, Customers, Aging, Sales tax. Use "Home" only when the page shows a real summary. Put the plan name and seat count on the Billing page, in a sentence such as "Team plan, 8 of 10 seats used."

#### Checklist

- Width is 240px or 56px, background `--paper-2`, 1px right border.
- Active item has background, left bar, weight and `aria-current`.
- No pills, no upgrade card, no gradient logo tile.
- No more than 7 items in a group.
- Drawer below 768px, no motion with reduced motion set.

### 5.2 Notifications and toasts

#### What the machine produces

```slop
<div className="fixed right-4 top-4 z-50 w-96 rounded-xl border border-white/20 bg-white/80 p-4 shadow-2xl backdrop-blur-lg">
  <div className="flex items-start gap-3">
    <div className="rounded-full bg-gradient-to-br from-emerald-400 to-teal-500 p-2">
      <CheckCircleIcon className="h-5 w-5 text-white" />
    </div>
    <div>
      <p className="font-semibold text-gray-900">Success!</p>
      <p className="text-sm text-gray-500">Your changes have been saved successfully.</p>
    </div>
  </div>
  <div className="absolute bottom-0 left-0 h-1 animate-shrink rounded-b-xl bg-gradient-to-r from-indigo-500 to-purple-500" />
</div>
```

This is the `react-hot-toast` and `sonner` default with a glass card from the Tailwind UI notification panel. It stacks in the top-right corner, where it covers the save button and the account menu. It says `Success!` twice in two different words, uses an icon in a gradient circle, and drains a gradient countdown bar that tells the reader to hurry.

#### Rules

1. Toast only the result of an action the user just took that is not already visible. If the saved value is on screen, the toast is noise. Remove it.
2. Place toasts bottom-left, 24px from both edges, at most 400px wide. Show one at a time. A newer toast replaces the older one.
3. Success toasts stay for 6000ms. Hovering or focusing a toast pauses the timer. A toast with an action such as Undo stays for at least 10000ms. Error toasts never auto-dismiss.
4. Success uses a container with `role="status"` (polite). Errors use `role="alert"`. Render the live region empty on page load, then insert text into it.
5. One sentence at 14px, at most 2 lines. Name the object: "Invoice INV-2041 archived", not "Item archived".
6. Use an inverted surface: `--ink` background, `--paper` text, no border, `--radius` corners. The inversion separates it from the page without a shadow.
7. Enter with opacity 0 to 1 and `translateY(8px)` to 0 over 150ms. No exit animation over 100ms. No motion under reduced motion. No countdown bar.
8. The notification inbox behind a bell icon shows a numeral up to 99, then "99+". Unread rows get an 8px `--accent` square and weight 600 titles. Group by day.

#### Reference build

```html
<div class="toast-region" role="status" aria-live="polite"></div>

<!-- inserted by script after the action completes -->
<div class="toast">
  <p class="toast-text">Invoice INV-2041 archived.</p>
  <button type="button" class="toast-action">Undo</button>
  <button type="button" class="toast-close" aria-label="Dismiss">
    <svg class="i" aria-hidden="true"><use href="#i-x"/></svg>
  </button>
</div>
```

```css
.toast-region { position: fixed; left: 24px; bottom: 24px; z-index: 50; max-width: min(400px, calc(100vw - 48px)); }
.toast {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 8px 12px 16px;
  background: var(--ink); color: var(--paper);
  border-radius: var(--radius);
  font: 14px/20px var(--font-sans);
  animation: toast-in 150ms ease-out;
}
.toast-text { margin: 0; flex: 1; }
.toast-action { background: none; border: 0; padding: 4px 8px; color: var(--paper); font: inherit; font-weight: 600; text-decoration: underline; text-underline-offset: 3px; cursor: pointer; }
.toast-close { display: grid; place-items: center; width: 32px; height: 32px; background: none; border: 0; color: var(--paper); cursor: pointer; }
.toast button:focus-visible { outline: 2px solid var(--paper); outline-offset: 2px; }
.toast[data-tone="error"] { border-left: 4px solid var(--bad); }
@keyframes toast-in { from { opacity: 0; transform: translateY(8px); } }
@media (prefers-reduced-motion: reduce) { .toast { animation: none; } }
```

#### States

- Success: text only, no icon. The sentence carries the meaning.
- Error: `role="alert"`, 4px `--bad` left bar, a fix action where one exists, no timer.
- Offline queue: a single persistent toast, "Offline. 3 changes will sync when you reconnect."

#### Copy

```slop
Success! Your changes have been saved successfully.
Oops! Something went wrong. Please try again later.
Heads up! You've got new notifications.
Woohoo! You're all set.
```

- Invoice INV-2041 archived. Undo
- Could not send to ana@harbor.co. The address bounced. Edit address
- 3 files uploaded to Q3 receipts.
- Offline. 3 changes will sync when you reconnect.

#### Checklist

- Toast only for changes the user cannot already see.
- Bottom-left, one at a time, 400px max.
- Errors persist and use `role="alert"`.
- Timers pause on hover and focus. No countdown bar.
- Inverted `--ink` surface, no blur, no icon circle.

### 5.3 Onboarding flows and checklists

#### What the machine produces

```slop
<div className="fixed bottom-6 right-6 w-80 rounded-2xl bg-white p-6 shadow-2xl ring-1 ring-black/5">
  <div className="flex items-center gap-4">
    <svg className="h-14 w-14"><circle className="stroke-indigo-100" /><circle className="stroke-[url(#grad)]" strokeDasharray="20 100" /></svg>
    <div>
      <p className="font-bold">Welcome aboard, Alex!</p>
      <p className="text-sm text-gray-500">You're 20% of the way there</p>
    </div>
  </div>
  <ul className="mt-4 space-y-3">
    <li className="flex gap-2 line-through text-gray-400"><CheckCircleIcon className="text-emerald-500" /> Create your account</li>
    <li className="flex gap-2"><CircleIcon /> Explore the dashboard</li>
    <li className="flex gap-2"><CircleIcon /> Connect your favorite tools</li>
  </ul>
  <button className="mt-4 w-full rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 py-2 text-white">Let's go</button>
</div>
```

This is the floating checklist from Intercom and Appcues-style onboarding widgets, rebuilt with a progress ring in an SVG gradient. The first task is pre-checked ("Create your account") to inflate progress, the next one ("Explore the dashboard") cannot be completed because it is not an action, and the widget covers the bottom-right corner where most primary actions in a form sit. Product tours with pulsing hotspot dots and confetti on completion usually come with it.

#### Rules

1. At most 5 tasks. Each task completes when the user does the real thing in the product, detected by the product. Never offer "Mark as done".
2. Never pre-complete a task to make progress look further along. Account creation is not a task.
3. Show progress as "2 of 5 done". No percent, no ring, no bar under 5 steps.
4. Place the checklist inline at the top of the home page, inside a 1px `--rule` border. Floating corner widgets are banned.
5. The checklist is dismissible from the first visit. Dismissal persists per user. A "Setup guide" link in the help menu brings it back.
6. Each task has a verb title, one line saying what it does for the user, and one button that goes straight to the place where it happens.
7. Ask at most 3 questions between sign-up and the product. Each answer must change something visible, such as currency, time zone, or which sample data loads.
8. Product tours are banned over 3 steps. No pulsing hotspot dots, no confetti, no mascot.

#### Reference build

```html
<section class="setup" aria-labelledby="setup-h">
  <header class="setup-head">
    <h2 id="setup-h">Set up Ledgerline</h2>
    <p class="setup-count">2 of 5 done</p>
    <button type="button" class="setup-hide">Hide</button>
  </header>
  <ol class="setup-list">
    <li data-done>
      <span class="box" aria-hidden="true"><svg viewBox="0 0 16 16"><path d="M3.5 8.5l3 3 6-7"/></svg></span>
      <div><p class="t">Connect a bank account</p><p class="d">Done. Imported 412 transactions from the last 90 days.</p></div>
    </li>
    <li>
      <span class="box" aria-hidden="true"></span>
      <div><p class="t">Send your first invoice</p><p class="d">Pick a customer, add line items, and email a PDF.</p></div>
      <a class="setup-go" href="/invoices/new">New invoice</a>
    </li>
  </ol>
</section>
```

```css
.setup { border: 1px solid var(--rule); background: var(--paper); margin-bottom: 32px; }
.setup-head { display: flex; align-items: baseline; gap: 16px; padding: 16px 24px; border-bottom: 1px solid var(--rule); }
.setup-head h2 { margin: 0; font-size: 18px; line-height: 1.25; }
.setup-count { margin: 0; color: var(--ink-2); font-size: 14px; font-variant-numeric: tabular-nums; }
.setup-hide { margin-left: auto; background: none; border: 0; color: var(--ink-2); font: inherit; font-size: 14px; text-decoration: underline; cursor: pointer; }
.setup-list { list-style: none; margin: 0; padding: 0; }
.setup-list li { display: grid; grid-template-columns: 16px 1fr auto; gap: 16px; align-items: start; padding: 16px 24px; border-top: 1px solid var(--rule); }
.setup-list li:first-child { border-top: 0; }
.box { width: 16px; height: 16px; margin-top: 2px; border: 1px solid var(--ink-3); border-radius: var(--radius); }
.box svg { width: 14px; height: 14px; fill: none; stroke: var(--paper); stroke-width: 1.5; }
li[data-done] .box { background: var(--ink); border-color: var(--ink); }
li[data-done] .t { color: var(--ink-2); }
.t { margin: 0; font-weight: 600; }
.d { margin: 4px 0 0; color: var(--ink-2); font-size: 14px; }
.setup-go { align-self: center; padding: 6px 12px; border: 1px solid var(--ink); border-radius: var(--radius); color: var(--ink); font-size: 14px; text-decoration: none; }
```

#### States

- Done: filled `--ink` box with a stroked path, title in `--ink-2`, description replaced with what happened ("Imported 412 transactions"). No strikethrough.
- All done: the section collapses to one line, "Setup done. Hide", and removes itself after the next visit.
- Dismissed: gone, recoverable from the help menu.
- Blocked: when a task needs an admin, say so and name the admin: "Needs an owner. Ask Priya Nair."

#### Copy

```slop
Welcome aboard, Alex! Let's get you started on your journey.
You're 20% of the way there. Keep it up!
Explore the dashboard
Customize your workspace to make it yours
You're crushing it!
```

- Set up Ledgerline: 2 of 5 done
- Connect a bank account. Imports the last 90 days of transactions.
- Send your first invoice. Pick a customer, add line items, email a PDF.
- Setup done. Hide

#### Checklist

- 5 tasks or fewer, each detected from real use.
- No pre-checked tasks, no percent ring.
- Inline at the top of home, not a floating corner widget.
- Dismissible on the first visit, recoverable from help.
- No tour over 3 steps, no pulsing dots, no confetti.

### 5.4 Pagination

#### What the machine produces

```slop
<div className="flex items-center justify-between">
  <p className="text-sm text-gray-500">Showing <span className="font-medium">1</span> to <span className="font-medium">10</span> of <span className="font-medium">97</span> results</p>
  <nav className="flex gap-2">
    <button className="flex items-center gap-1 rounded-full px-4 py-2 shadow-sm hover:bg-gray-50"><ChevronLeftIcon className="h-4 w-4" /> Previous</button>
    <button className="h-10 w-10 rounded-full bg-gradient-to-r from-indigo-500 to-purple-500 text-white shadow-md">1</button>
    <button className="h-10 w-10 rounded-full hover:bg-gray-100">2</button>
    <span className="px-2">...</span>
    <button className="h-10 w-10 rounded-full hover:bg-gray-100">10</button>
    <button className="flex items-center gap-1 rounded-full px-4 py-2 shadow-sm hover:bg-gray-50">Next <ChevronRightIcon className="h-4 w-4" /></button>
  </nav>
</div>
```

This is the Tailwind UI "Card footer with page buttons" with pill buttons and a gradient current page. Every page number is a `<button>`, so no page has a URL, the back button does nothing useful, and nobody can share "page 4". "Previous" is enabled on page 1 and does nothing when pressed.

#### Rules

1. Pick the pattern by task. Numbered pages for lists people return to by position (support queues, search results, audit logs). "Load more" for feeds. Infinite scroll only when the page has no footer and nobody needs to come back to a position.
2. Every page is a link with the page in the URL: `?page=4`. Never a `<button>` with local state.
3. Show first, last, current, and one neighbour on each side. That fixes the row at 7 slots, so its width never jumps. The ellipsis is text, not a control.
4. Targets are at least 32px square with 4px gaps. WCAG 2.5.8 asks for 24px. Use 32px.
5. The current page is a `<span aria-current="page">` with `--ink` background and `--paper` text. It is not a link.
6. Previous and Next are text links. At either end, render them as `<span aria-disabled="true">` in `--ink-3`, not as enabled buttons.
7. The range reads "41 to 60 of 1,284" in tabular numerals, left of the pager. Use thousands separators.
8. Page size options are 25, 50 and 100. Default to 50. Keep the choice in the URL.
9. After a page change, move focus to the table caption or heading and scroll the table top into view.

#### Reference build

```html
<div class="pager-bar">
  <p class="pager-range">41 to 60 of 1,284</p>
  <nav class="pager" aria-label="Pages">
    <a href="?page=2" rel="prev">Previous</a>
    <a href="?page=1">1</a>
    <span class="gap">...</span>
    <a href="?page=2">2</a>
    <span aria-current="page">3</span>
    <a href="?page=4">4</a>
    <span class="gap">...</span>
    <a href="?page=65">65</a>
    <a href="?page=4" rel="next">Next</a>
  </nav>
</div>
```

```css
.pager-bar { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px; padding: 12px 0; border-top: 1px solid var(--rule); font: 14px/20px var(--font-sans); }
.pager-range { margin: 0; color: var(--ink-2); font-variant-numeric: tabular-nums; }
.pager { display: flex; gap: 4px; align-items: center; font-variant-numeric: tabular-nums; }
.pager a, .pager span {
  display: inline-grid; place-items: center;
  min-width: 32px; height: 32px; padding: 0 8px;
  border: 1px solid transparent; border-radius: var(--radius);
  color: var(--ink); text-decoration: none;
}
.pager a:hover { border-color: var(--rule); background: var(--paper-2); }
.pager a:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.pager [aria-current="page"] { background: var(--ink); color: var(--paper); font-weight: 600; }
.pager [aria-disabled="true"] { color: var(--ink-3); }
.pager .gap { min-width: 16px; padding: 0; color: var(--ink-3); }
@media (max-width: 480px) { .pager a:not([rel]), .pager .gap { display: none; } }
```

#### States

- First page: Previous is a disabled span. Last page: Next is a disabled span.
- One page only: hide the pager, keep the range text ("12 invoices").
- Narrow screens: below 480px show only Previous, the current page, and Next, with "Page 3 of 65" as the current label.
- Loading the next page: keep the old rows visible at full opacity and set `aria-busy="true"` on the table until the new rows arrive.
- "Load more": a full-width 40px outlined button that reads "Show 50 more (1,224 left)".

#### Copy

```slop
Showing 1 to 10 of 97 results
Load more awesome content
You've reached the end! 
```

- 41 to 60 of 1,284
- Page 3 of 65
- Show 50 more (1,224 left)
- End of list. 1,284 invoices.

#### Checklist

- Each page has a URL.
- Seven slots, fixed width, ellipsis as text.
- 32px targets, current page as a span with `aria-current`.
- Disabled ends rendered disabled.
- Focus moves to the table after a page change.

### 5.5 Pricing tables

#### What the machine produces

```slop
<div className="grid grid-cols-3 gap-8 items-center">
  <div className="rounded-3xl bg-white p-8 shadow-lg">...Starter, $0/mo, Basic features, Get started...</div>
  <div className="relative scale-105 rounded-3xl bg-gradient-to-b from-indigo-500 to-purple-600 p-[2px] shadow-2xl shadow-purple-500/30">
    <span className="absolute -top-4 left-1/2 -translate-x-1/2 rounded-full bg-gradient-to-r from-pink-500 to-violet-500 px-4 py-1 text-sm text-white">Most popular</span>
    <div className="rounded-3xl bg-white p-8">
      <h3 className="text-lg font-semibold">Pro</h3>
      <p className="mt-4 text-5xl font-bold">$29<span className="text-base text-gray-500">/mo</span></p>
      <ul className="mt-6 space-y-3">
        <li className="flex gap-2"><CheckIcon className="text-emerald-500" /> Everything in Starter</li>
        <li className="flex gap-2"><CheckIcon className="text-emerald-500" /> Unlimited projects</li>
        <li className="flex gap-2"><CheckIcon className="text-emerald-500" /> Advanced analytics</li>
        <li className="flex gap-2"><CheckIcon className="text-emerald-500" /> Priority support</li>
      </ul>
      <button className="mt-8 w-full rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 py-3 text-white">Get started</button>
    </div>
  </div>
  <div className="rounded-3xl bg-white p-8 shadow-lg">...Enterprise, Custom...</div>
</div>
```

This is the three-tier pricing block from every SaaS template: Starter, Pro, Enterprise at $0, $29 and "Custom". The middle card is scaled to 105%, wrapped in a 2px gradient ring with a purple glow, and topped with a gradient "Most popular" pill. Each card is a list of green check icons beside phrases that say nothing measurable ("Basic features", "Advanced analytics"), and every button reads "Get started" regardless of what happens on click.

#### Rules

1. Name plans after who buys them: Solo, Team, Company. Not Starter, Pro and Enterprise, and never `Premium`.
2. Write the price with its currency, amount, unit and billing basis in one place: "$24 per user per month, billed yearly ($288 per user)". A bare "$24/mo" hides the unit and the commitment.
3. If you offer a monthly and a yearly price, default the toggle to the one most customers buy and state the difference as an amount: "Yearly saves $72 per user". No "Save 20%" pill.
4. Every limit is a number: "3 projects", "10 GB storage", "90 days of history". Never "Generous storage" or "Advanced analytics".
5. Plan summaries list differences only, at most 6 lines each, starting from "Everything in Solo, plus". The full matrix goes into a comparison table below (see 5.21).
6. Mark the recommended plan with a line of text above it ("Most teams of 5 to 50 pick this") and a 1px `--ink` border on that column. No scale, no ring, no glow, no pill. If you cannot say who it is recommended for, recommend nothing.
7. Inside the comparison table, write "Included", a number, or a dash. If you use an icon, it is a 16px stroked SVG with a text label for screen readers. No green checks against grey crosses.
8. One button per plan, labelled with what happens: "Start 14-day trial", "Create free account", "Book a call with sales". One filled button for the recommended plan, outlined buttons for the rest.
9. Prices are 32px in tabular numerals, plan names 18px, summaries 14px. Align price baselines across columns.
10. Say what ends a free plan and what happens to data after a downgrade, in one sentence each, under the table.

#### Reference build

```html
<section class="plans" aria-labelledby="plans-h">
  <h2 id="plans-h">Pricing</h2>
  <p class="plans-basis">Prices per user per month, billed yearly. Monthly billing costs $6 more per user.</p>
  <div class="plans-grid">
    <article class="plan">
      <h3>Solo</h3>
      <p class="price"><span class="amt">$0</span> for one person</p>
      <ul><li>1 user</li><li>3 active projects</li><li>30 days of history</li></ul>
      <a class="btn btn-outline" href="/signup">Create free account</a>
    </article>
    <article class="plan plan-rec" aria-describedby="rec-note">
      <p class="rec" id="rec-note">Most teams of 5 to 50 pick this</p>
      <h3>Team</h3>
      <p class="price"><span class="amt">$24</span> per user</p>
      <ul><li>Everything in Solo, plus</li><li>Unlimited projects</li><li>2 years of history</li><li>SAML single sign-on</li></ul>
      <a class="btn btn-fill" href="/signup?plan=team">Start 14-day trial</a>
    </article>
    <article class="plan">
      <h3>Company</h3>
      <p class="price"><span class="amt">$41</span> per user</p>
      <ul><li>Everything in Team, plus</li><li>Audit log export</li><li>99.9% uptime in contract</li><li>Named support engineer</li></ul>
      <a class="btn btn-outline" href="/sales">Book a call with sales</a>
    </article>
  </div>
  <p class="plans-foot">Solo ends when you add a second user. Downgrading keeps all data read-only for 90 days.</p>
</section>
```

```css
.plans { max-width: 1040px; margin: 0 auto; padding: 64px 16px; }
.plans h2 { font-size: 32px; line-height: 1.2; margin: 0 0 8px; }
.plans-basis, .plans-foot { color: var(--ink-2); font-size: 14px; max-width: 66ch; }
.plans-grid { display: grid; grid-template-columns: repeat(3, 1fr); margin-top: 32px; border: 1px solid var(--rule); }
.plan { display: flex; flex-direction: column; gap: 16px; padding: 32px 24px; border-left: 1px solid var(--rule); background: var(--paper); }
.plan:first-child { border-left: 0; }
.plan-rec { outline: 1px solid var(--ink); outline-offset: -1px; background: var(--paper-2); }
.rec { margin: 0; font-size: 14px; font-weight: 600; color: var(--ink); }
.plan h3 { margin: 0; font-size: 18px; }
.price { margin: 0; color: var(--ink-2); font-size: 14px; }
.amt { display: block; font-size: 32px; line-height: 1.2; color: var(--ink); font-weight: 600; font-variant-numeric: tabular-nums; }
.plan ul { margin: 0; padding: 0 0 0 16px; font-size: 14px; line-height: 1.6; flex: 1; }
.btn { display: block; padding: 10px 16px; text-align: center; border-radius: var(--radius); font-weight: 600; text-decoration: none; }
.btn-fill { background: var(--accent); color: var(--accent-ink); border: 1px solid var(--accent); }
.btn-outline { background: transparent; color: var(--ink); border: 1px solid var(--ink); }
.btn:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
@media (max-width: 768px) {
  .plans-grid { grid-template-columns: 1fr; }
  .plan { border-left: 0; border-top: 1px solid var(--rule); }
  .plan-rec { order: -1; border-top: 0; }
}
```

#### States

- Billing toggle: a two-option segmented control (see 5.11) labelled "Yearly" and "Monthly". Switching updates every price and the basis line together. No animation on the numbers.
- Current plan (signed-in view): replace that plan's button with the text "Your plan" and a link "Manage in Billing".

#### Copy

```slop
Most popular
Best value
Pro: Unlock premium features and supercharge your workflow
Get started
```

- Most teams of 5 to 50 pick this
- Team: unlimited projects, 2 years of history, SAML single sign-on
- Start 14-day trial. No card until day 14.
- Book a call with sales. From $18,000 per year.

#### Checklist

- Plan names describe buyers. No `Premium`.
- Every price has unit and billing basis. Every limit is a number.
- Recommended plan marked with a sentence and a 1px `--ink` border only.
- No scale, ring, glow or gradient pill.
- Buttons say what happens next.
- Free plan limits and downgrade behaviour stated under the table.

