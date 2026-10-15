## Part 4. Components, A to M

25 components in alphabetical order. Each chapter has six sections: what the machine produces, rules, a reference build, states, copy, and a checklist.

Reference builds assume the canonical tokens on `:root`, `box-sizing: border-box`, and 16px body text at 1.5 line height. None use shadows, gradients or blur. Depth comes from 1px `var(--rule)` borders and the paper steps: `--paper` for the page, `--paper-2` for recessed surfaces, `--paper-3` for pressed and selected ones.

### 4.1 Accordions

#### What the machine produces

```slop
<div className="space-y-4">
  {faqs.map((faq) => (
    <div key={faq.q} className="rounded-2xl border border-gray-200 bg-white shadow-sm transition-all duration-300 hover:shadow-md">
      <button onClick={() => setOpen(open === faq.q ? null : faq.q)} className="flex w-full items-center justify-between px-6 py-5 text-left">
        <span className="text-lg font-semibold text-gray-900">{faq.q}</span>
        <div className="flex h-8 w-8 items-center justify-center rounded-full bg-indigo-50">
          <ChevronDown className={`h-5 w-5 text-indigo-600 transition-transform duration-300 ${open === faq.q ? "rotate-180" : ""}`} />
        </div>
      </button>
      {open === faq.q && <div className="px-6 pb-5 text-gray-600">{faq.a}</div>}
    </div>
  ))}
</div>
```

This is the landing-page FAQ from every Tailwind starter: each question is its own floating `rounded-2xl` card, the chevron sits in an `indigo-50` circle, and `transition-all duration-300` animates every property for twice the time the eye needs. The `<button>` has no `aria-expanded`, the panel has no id, and the state forces one item open at a time, so a reader cannot compare two answers.

#### Rules

1. Use `<details>` and `<summary>`. They give keyboard support, the expanded state and find-in-page for free. Reach for a scripted button with `aria-expanded` and `aria-controls` only when the panel content loads on demand.
2. Items are rows in one list, separated by a 1px `var(--rule)` line. No gap between items, no box around each item.
3. The summary row is at least 44px tall: 12px vertical padding, 16px text at weight 500.
4. The indicator is a 16px chevron or a plus and minus drawn in 1.5px strokes, placed before the label. No circle or tile behind it. It turns 90 degrees in 120ms `ease-out`, and not at all under reduced motion.
5. Allow several items open at once. If a design does need one open at a time, use the `name` attribute on each `<details>` (supported in Chromium 120, Safari 17.2 and Firefox 130) instead of state code.
6. Panel text runs to 66ch at most, indented 20px to line up with the label, with 16px below the last paragraph.
7. Give each item an id and open the one that matches `location.hash` on load (two lines of script), so support staff can link to a single answer.
8. Do not hide prices, cancellation terms or anything a person needs before paying inside a closed item.

#### Reference build

```html
<div class="acc">
  <details id="refund-window">
    <summary>Can I get a refund after 30 days?</summary>
    <div class="acc-body">
      <p>Yes, for annual plans. We refund the unused months, rounded down. Monthly plans are not refunded after the first 30 days.</p>
    </div>
  </details>
  <details id="file-types">
    <summary>Which file types can I import?</summary>
    <div class="acc-body">
      <p>CSV, XLSX and JSON, up to 50 MB per file.</p>
    </div>
  </details>
</div>
```

```css
.acc { max-width: 66ch; border-top: 1px solid var(--rule); }
.acc details { border-bottom: 1px solid var(--rule); }
.acc summary {
  display: flex; align-items: center; gap: 12px;
  min-height: 44px; padding: 12px 0;
  font: 500 16px/1.4 var(--font-sans); color: var(--ink);
  cursor: pointer; list-style: none;
}
.acc summary::-webkit-details-marker { display: none; }
.acc summary::before {
  content: ""; flex: none; width: 7px; height: 7px;
  border-right: 1.5px solid var(--ink-2); border-bottom: 1.5px solid var(--ink-2);
  transform: rotate(-45deg); transition: transform 120ms ease-out;
}
.acc details[open] > summary::before { transform: rotate(45deg); }
.acc summary:hover { text-decoration: underline; text-underline-offset: 3px; }
.acc summary:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.acc-body { padding: 0 0 16px 20px; color: var(--ink-2); }
.acc-body p { margin: 0 0 8px; }
@media (prefers-reduced-motion: reduce) {
  .acc summary::before { transition: none; }
}
```

#### States

- Hover: the label gets a 1px underline at 3px offset. No row fill; a filled band reads as selection.
- Focus-visible: 2px `var(--focus)` outline at 2px offset around the summary.
- Open: the chevron points down. The label keeps its weight.

#### Copy

```slop
What makes us different?
How does the magic work?
Is it secure?
```

Write the summary as the question a customer types into a search box, with the noun they use.

- Can I get a refund after 30 days?
- Which file types can I import?
- Where is my data stored? (Answer: Frankfurt, eu-central-1.)

#### Checklist

- Native `details` and `summary`, no click handler on a div.
- One bordered list, rows separated by 1px rules, no per-item cards.
- Summary at least 44px tall, chevron before the label, 120ms or no motion.
- Multiple items can be open, or the `name` attribute is used deliberately.

### 4.2 Alerts and banners

#### What the machine produces

```slop
<div className="bg-gradient-to-r from-indigo-600 to-purple-600 py-2 text-center text-sm text-white">
  <PartyPopper className="mr-2 inline h-4 w-4" /> We just launched v2.0! <a href="#" className="font-semibold underline">Check it out</a>
</div>

<div className="fixed right-4 top-4 z-50 flex items-start gap-3 rounded-xl border border-green-200 bg-green-50 p-4 shadow-lg animate-in slide-in-from-top-5">
  <CheckCircle2 className="h-5 w-5 text-green-500" />
  <div>
    <h3 className="font-semibold text-green-800">Success!</h3>
    <p className="text-sm text-green-700">Your changes have been saved successfully.</p>
  </div>
  <button className="ml-auto text-green-500 hover:text-green-700"><X className="h-4 w-4" /></button>
</div>
```

Two defaults stacked. The announcement bar is the `from-indigo-600 to-purple-600` strip that ships above every SaaS template. The toast is the shadcn and react-hot-toast pattern: top-right, `shadow-lg`, a slide-in, a `Success!` heading that adds nothing, and a body that says "successfully" after already saying success. Green 500 text on green 50 measures about 2.3:1, below the 4.5:1 minimum.

#### Rules

1. Put the message where the problem is: under the failed field, at the top of the failed table. A page-wide banner is only for account-wide states: billing failed, maintenance, read-only mode.
2. Banner: full width, 40px minimum height, 14px text, one sentence, at most one link and one dismiss button. Background `var(--paper-2)`, 1px bottom rule in the status color.
3. Inline alert: `var(--paper-2)` background, 1px border in the status color (`--bad`, `--warn`, `--ok`) or `--rule-strong` for neutral, 2px radius, 12px 16px padding. The first word is the status in weight 600 ("Error.", "Warning.", "Saved."), so the meaning survives without color.
4. Toasts confirm actions the person just took and nothing else. Bottom-left or bottom-center, 16px from the viewport edges, 360px wide at most. One visible at a time; queue the rest.
5. Toasts that only confirm stay 5 seconds and pause while hovered or focused. Toasts with an action ("Undo") stay 10 seconds. Errors never go in a toast; they stay on the page until fixed.
6. Use `role="status"` for confirmations and `role="alert"` only for errors that appear after the person acted. Never put `role="alert"` on content present at page load.

#### Reference build

```html
<div class="banner" role="region" aria-label="Account notice" data-tone="warn">
  <p>Your card ending 4421 was declined on 14 Oct. Service stops on 28 Oct. <a href="/billing">Update card</a></p>
  <button class="banner-close" type="button" aria-label="Dismiss notice">Dismiss</button>
</div>

<div class="alert" data-tone="bad" role="alert">
  <p><strong>Error.</strong> 3 of 120 rows were not imported because the date column is empty. <a href="#row-14">Go to row 14</a></p>
</div>

<div class="toast" role="status">
  <p>Invoice 1042 deleted.</p>
  <button type="button">Undo</button>
</div>
```

```css
[data-tone="bad"]  { --tone: var(--bad); }
[data-tone="warn"] { --tone: var(--warn); }
[data-tone="ok"]   { --tone: var(--ok); }

.banner {
  display: flex; align-items: center; justify-content: space-between; gap: 16px;
  min-height: 40px; padding: 8px 16px;
  background: var(--paper-2); border-bottom: 1px solid var(--tone, var(--rule-strong));
  font-size: 14px; color: var(--ink);
}
.banner p { margin: 0; max-width: 90ch; }
.banner-close {
  font: inherit; color: var(--ink-2); background: none; border: 0;
  padding: 4px 8px; cursor: pointer; text-decoration: underline;
}

.alert {
  max-width: 66ch; padding: 12px 16px;
  background: var(--paper-2); border: 1px solid var(--tone, var(--rule-strong));
  border-radius: var(--radius); color: var(--ink);
}
.alert p { margin: 0; }
.alert strong { color: var(--tone); font-weight: 600; }

.toast {
  position: fixed; left: 16px; bottom: 16px; max-width: 360px;
  display: flex; align-items: center; gap: 16px; padding: 12px 16px;
  background: var(--ink); color: var(--paper); border-radius: var(--radius);
  animation: toast-in 120ms ease-out;
}
.toast p { margin: 0; }
.toast button { font: inherit; font-weight: 600; color: var(--paper); background: none; border: 0; text-decoration: underline; cursor: pointer; }
:is(.banner, .toast) button:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.toast button:focus-visible { outline-color: var(--paper); }
@keyframes toast-in { from { opacity: 0; } to { opacity: 1; } }
@media (prefers-reduced-motion: reduce) { .toast { animation: none; } }
```

#### States

- Hover and focus on a toast: the dismiss timer pauses and resumes 1 second after the pointer leaves.
- Error resolved: the inline alert is removed, and a `role="status"` line says what changed ("All 120 rows imported.").
- Dismissed: gone for that account, stored server-side, until its condition changes.

#### Copy

```slop
Success! Your changes have been saved successfully.
Oops! Something went wrong. Please try again later.
Heads up! We're making some exciting changes.
```

- Saved. Last edit 14:32.
- Could not save. The server did not answer within 30 seconds. Your text is still here. Try again.
- Maintenance on Sunday 19 Oct, 02:00 to 03:00 UTC. Sync will pause; nothing is lost.

Order: what happened, what it means for the person, what to do.

#### Checklist

- Message placed next to what it is about; banner reserved for account-wide state.
- Status word as first word, not color alone; text contrast at least 4.5:1.
- One banner, one toast visible at a time.
- Errors stay on the page; toasts carry confirmations and undo only.

### 4.3 Avatars

#### What the machine produces

```slop
<div className="flex -space-x-3">
  {users.map((u) => (
    <div className="relative rounded-full bg-gradient-to-tr from-pink-500 to-violet-500 p-0.5">
      <img src={`https://i.pravatar.cc/150?u=${u.id}`} className="h-10 w-10 rounded-full ring-2 ring-white" />
      <span className="absolute bottom-0 right-0 h-3 w-3 rounded-full bg-green-400 ring-2 ring-white" />
    </div>
  ))}
  <div className="flex h-10 w-10 items-center justify-center rounded-full bg-indigo-100 text-xs font-medium text-indigo-600 ring-2 ring-white">+5</div>
</div>
```

The Instagram-story gradient ring, `i.pravatar.cc` stock faces, a green presence dot that nobody wired to presence data, and `-space-x-3` overlap with `ring-2 ring-white`. The `img` has no `alt`.

#### Rules

1. Four sizes: 24px in dense lists and table cells, 32px in comments and menus, 40px in headers, 64px on a profile page.
2. People are circles. Organizations, workspaces and bots are squares with `var(--radius)`, so the shape tells the reader which kind of entity it is.
3. Photos get a 1px inner border so a white background in the photo does not bleed into `--paper`: `outline: 1px solid var(--rule); outline-offset: -1px`.
4. The fallback is initials: first letter of the given name and of the family name, 2 letters at most, 40% of the avatar size, weight 500, `var(--ink)` on `var(--paper-3)`. One neutral color for everyone, not a rainbow of hashed hues.
5. Show a presence indicator only when the product tracks presence and refreshes it at least every 60 seconds. Then pair it with text in the tooltip or next to the name: "Active", "Away since 14:10". No pulsing.
6. Stacks show at most 3 avatars, overlapping by 25% of their width, then a text count: "and 12 others" as a link to the full list. The count is text, not a fourth fake circle.
7. `alt` is the person's name. When the name is printed right next to the image, use `alt=""` so a screen reader does not read the name twice.
8. No placeholder services (`i.pravatar.cc`, `randomuser.me`) in production, least of all beside a customer quote.

#### Reference build

```html
<span class="avatar" style="--size: 32px">
  <img src="/u/1187.jpg" alt="" width="32" height="32">
</span>
<span class="avatar" style="--size: 32px" aria-hidden="true">MK</span>
<span class="name">Mira Kowalski</span>

<div class="stack">
  <span class="avatar" style="--size: 24px"><img src="/u/1.jpg" alt="Ana Ruiz" width="24" height="24"></span>
  <span class="avatar" style="--size: 24px"><img src="/u/2.jpg" alt="Tom Berg" width="24" height="24"></span>
  <span class="avatar" style="--size: 24px" title="Li Wen">LW</span>
  <a href="/members">and 12 others</a>
</div>
```

```css
.avatar {
  --size: 32px;
  display: inline-grid; place-items: center; flex: none;
  width: var(--size); height: var(--size); border-radius: 50%;
  overflow: hidden; vertical-align: middle;
  background: var(--paper-3); color: var(--ink);
  font: 500 calc(var(--size) * 0.4)/1 var(--font-sans);
}
.avatar img {
  width: 100%; height: 100%; object-fit: cover; border-radius: inherit;
  outline: 1px solid var(--rule); outline-offset: -1px;
}
.avatar-org { border-radius: var(--radius); }
.stack { display: flex; align-items: center; }
.stack .avatar + .avatar { margin-left: calc(var(--size) * -0.25); }
.stack .avatar { outline: 2px solid var(--paper); }
.stack a { margin-left: 8px; font-size: 14px; color: var(--ink-2); }
```

#### States

- Loading: the initials fallback renders first and the photo replaces it when loaded. No grey pulsing circle.
- Broken image: catch the `error` event and swap to initials.
- Interactive avatar: 2px focus outline at 2px offset, and a name on the button: "Account menu for Mira Kowalski".

#### Copy

```slop
<img alt="avatar">
<img alt="User profile picture">
+5
```

- `alt=""` when the name is adjacent; `alt="Mira Kowalski"` when it is not.
- "and 12 others", linking to the member list.
- "Active", "Away since 14:10", "Last seen 3 days ago". Only when real.

#### Checklist

- Circles for people, 2px squares for organizations.
- Initials on one neutral `--paper-3` fill, never a hashed rainbow.
- No presence dot without presence data and a text label.
- Stacks capped at 3 plus a text count.

### 4.4 Badges, tags and status indicators

#### What the machine produces

```slop
<span className="inline-flex items-center gap-1.5 rounded-full bg-green-500/10 px-3 py-1 text-xs font-medium uppercase tracking-wider text-green-500 ring-1 ring-inset ring-green-500/20">
  <span className="relative flex h-2 w-2">
    <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-green-400 opacity-75"></span>
    <span className="relative inline-flex h-2 w-2 rounded-full bg-green-500"></span>
  </span>
  Live
</span>

<span className="rounded-full bg-gradient-to-r from-violet-500 to-fuchsia-500 px-2.5 py-0.5 text-xs font-semibold text-white">NEW</span>
<span className="rounded-full bg-blue-100 px-2.5 py-0.5 text-xs text-blue-700">Design</span>
<span className="rounded-full bg-amber-100 px-2.5 py-0.5 text-xs text-amber-700">Research</span>
```

The first element is copied almost verbatim from the `animate-ping` example in the Tailwind documentation, where it decorates a notification button. Models paste it onto dashboards, landing pages, pricing tables and AI chat headers, with the word "Live" next to it. Below it: the gradient "NEW" pill and one pastel `rounded-full` chip per category, the shadcn `Badge` with hues picked from the Tailwind palette in order.

#### The green-dot LIVE pill, specifically

This handbook bans the green-dot status pill outright. A product that ships one has told the reader the interface was assembled, not designed. The reasons are concrete.

1. It asserts a state nobody checks. The pill is static markup. It says "Live" when the socket closed 20 minutes ago, when the tab was asleep, when the API returns yesterday's batch. A status the code does not compute is decoration pretending to be data.
2. It carries no evidence. "Live" answers nothing a person monitoring a system needs: live since when, how fresh is the last value, how would I know if it stopped. A timestamp answers all three.
3. It moves forever. `animate-ping` loops at 1 second per cycle with no end. WCAG 2.2.2 requires a way to pause any motion that starts automatically and lasts more than 5 seconds, and this handbook allows only 0ms to 150ms transitions in response to a change.
4. It is color alone. Green against grey is the pair people with deuteranopia, about 5% of men, confuse first. The word next to it is in uppercase at 12px with `tracking-wider`, the least readable setting of the least informative word.
5. It is the same pill on every product: crypto tickers, AI chat apps, analytics dashboards and status pages all carry it.

#### What to show instead

Write the state as plain text and attach the evidence: a timestamp, an age, or a count.

- A feed or dashboard: "Updated 14:32:05 UTC (3 s ago)". The age ticks every second under 1 minute, then every minute.
- A connection: "Connected. Last event 14:32:05." When it drops: "Reconnecting, attempt 2 of 5." When it gives up: "Offline since 14:28. Retry."
- A batch source dressed up as real time: say what it is. "Data as of 06:00 today. Next refresh 06:00 tomorrow."
- A real broadcast or stream: "Streaming since 19:00 (1 h 12 min)" in the player chrome, as text, square corners, no dot, no loop.
- A stale feed: after 2 times the expected interval without data, the text changes and takes the `--warn` color: "No new data since 14:28 (4 min)." The person learns the system stopped without needing to notice that a dot stopped pulsing.

| State | Text to show | Color token | Live region |
| --- | --- | --- | --- |
| Receiving data | Connected. Last event 14:32:05 (3 s ago) | `--ink-2` | announce on entry only |
| Late | No new data since 14:28 (4 min) | `--warn` | polite |
| Reconnecting | Reconnecting, attempt 2 of 5 | `--warn` | polite |
| Down | Offline since 14:28. Retry | `--bad` | assertive once |
| Paused by user | Paused at 14:30. Resume | `--ink-2` | polite |
| Batch | Data as of 06:00 today | `--ink-2` | none |

#### Rules

1. Status is text first. A color token may tint the word; a shape never replaces it.
2. No dots, no pulse, no ping, no glow. If a table column needs a scannable mark, put the status word in the column and let the color sit on the word.
3. Every claim of freshness carries a time. Use `<time datetime="...">` with an ISO value and print a local, absolute time; add the relative age in parentheses.
4. Put `role="status"` on the state word only. The ticking age stays outside the live region, or a screen reader announces every second.
5. Tags (user-assigned labels) are 20px tall, 12px text in sentence case, 0 6px padding, 1px `var(--rule)` border, `var(--radius)` corners, `var(--ink-2)` text. All tags share one style. Category hues are not a design; they are a palette walked in order.
6. Show at most 3 tags on a row in a list, then "+2" as text that expands on click.
7. Count badges hold digits only. 18px tall, minimum 18px wide, 12px tabular figures, `var(--ink)` fill with `var(--paper)` text. Cap at "99+". Hide at zero; do not print "0".
8. A "New" label on a menu item or feature expires 30 days after release. Write it as text in `var(--accent)`, no pill, no gradient, no uppercase.

#### Reference build

```html
<p class="feed" data-state="ok">
  <span class="feed-state" role="status">Connected, last event at</span>
  <time class="feed-time" datetime="2026-10-15T14:32:05Z">14:32:05 UTC</time>
  <span class="feed-age">(3 s ago)</span>
</p>

<ul class="tags" aria-label="Tags">
  <li class="tag">Freight</li>
  <li class="tag">Q4 audit</li>
  <li><button class="tag tag-more" type="button">+2</button></li>
</ul>

<a class="nav-item" href="/inbox">Inbox <span class="count" aria-label="14 unread">14</span></a>
```

```css
.feed { margin: 0; font-size: 14px; color: var(--ink-2); font-variant-numeric: tabular-nums; }
.feed-state { color: var(--ink); font-weight: 500; }
.feed[data-state="late"] .feed-state { color: var(--warn); }
.feed[data-state="down"] .feed-state { color: var(--bad); }

.tags { display: flex; flex-wrap: wrap; gap: 4px; margin: 0; padding: 0; list-style: none; }
.tag {
  display: inline-flex; align-items: center; height: 20px; padding: 0 6px;
  font: 400 12px/1 var(--font-sans); color: var(--ink-2);
  border: 1px solid var(--rule); border-radius: var(--radius); background: transparent;
}
.tag-more { cursor: pointer; }
.tag-more:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }

.count {
  display: inline-grid; place-items: center; min-width: 18px; height: 18px; padding: 0 5px;
  font: 500 12px/1 var(--font-sans); font-variant-numeric: tabular-nums;
  background: var(--ink); color: var(--paper); border-radius: 9px;
}
```

```js
const feed = document.querySelector(".feed");
const [stateEl, timeEl, ageEl] = feed.querySelectorAll(".feed-state, .feed-time, .feed-age");
let last = Date.now();

function setState(key, text) {
  if (feed.dataset.state !== key) { feed.dataset.state = key; stateEl.textContent = text; }
}
function onEvent(ts) {
  last = ts;
  timeEl.dateTime = new Date(ts).toISOString();
  timeEl.textContent = new Date(ts).toISOString().slice(11, 19) + " UTC";
  setState("ok", "Connected, last event at");
}
setInterval(() => {
  const s = Math.round((Date.now() - last) / 1000);
  ageEl.textContent = s < 60 ? `(${s} s ago)` : `(${Math.floor(s / 60)} min ago)`;
  if (s > 30) setState("late", "No new data since");
}, 1000);
```

Events arrive every 15 seconds, so the stale threshold is 30. Late, the line reads "No new data since 14:28:05 UTC (4 min ago)". The state word changes once per transition, so the live region speaks once.

#### States

- Tag hover (only when tags are links or filters): border goes to `--rule-strong`, text to `--ink`. No fill.
- Tag selected as a filter: `--paper-3` fill, `--ink` text, and `aria-pressed="true"` on the button.
- Removable tag: a trailing 1.5px SVG cross with `aria-label="Remove tag Freight"`.

#### Copy

```slop
LIVE
NEW
Beta
```

- Updated 14:32:05 UTC (3 s ago)
- No new data since 14:28 (4 min)
- New in October: tax lines in CSV export

#### Checklist

- No green dot, no `animate-ping`, no pulsing anything.
- Every "live" or "current" claim replaced by a time and an age.
- Stale threshold set at 2 times the expected interval, with a text change.
- One neutral tag style; no per-category pastel hues.

### 4.5 Breadcrumbs

#### What the machine produces

```slop
<nav className="flex items-center space-x-2 rounded-full bg-gray-100 px-4 py-2 text-sm">
  <a href="/"><HomeIcon className="h-4 w-4 text-gray-500" /></a>
  <ChevronRight className="h-4 w-4 text-gray-400" />
  <a href="/dashboard" className="text-gray-500 hover:text-indigo-600">Dashboard</a>
  <ChevronRight className="h-4 w-4 text-gray-400" />
  <a href="/dashboard/settings" className="font-medium text-indigo-600">Settings</a>
</nav>
```

Breadcrumbs inside a grey pill, a house icon with no accessible name, chevron icons read aloud by screen readers as images, and the current page styled as an indigo link that reloads itself.

#### Rules

1. Add breadcrumbs only when the hierarchy is 3 or more levels deep and people land on deep pages from search or links.
2. Markup: `<nav aria-label="Breadcrumb">` containing an `<ol>`. The last item is the current page, written as text with `aria-current="page"`, not a link.
3. Separator: a slash or a 1.5px chevron drawn in CSS, with no accessible text. Use `content: "/" / ""` so the separator is skipped by screen readers.
4. 14px text, `--ink-2` for ancestors, `--ink` for the current page. 8px gap on each side of the separator. No container background.
5. The first item is a word ("Projects", "Home"), not an icon alone.
6. Show at most 5 levels. Deeper trails collapse the middle into a button labelled "..." with `aria-label="Show 3 more levels"` that opens a menu of the hidden items.
7. Under 480px, show only the parent as a back link: "Back to Invoices".

#### Reference build

```html
<nav class="crumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/projects">Projects</a></li>
    <li><a href="/projects/halden">Halden Freight</a></li>
    <li><a href="/projects/halden/invoices">Invoices</a></li>
    <li><span aria-current="page">Invoice 1042</span></li>
  </ol>
  <a class="crumbs-back" href="/projects/halden/invoices">Back to Invoices</a>
</nav>
```

```css
.crumbs { font-size: 14px; }
.crumbs ol { display: flex; flex-wrap: wrap; align-items: center; margin: 0; padding: 0; list-style: none; }
.crumbs li { display: inline-flex; align-items: center; color: var(--ink-2); }
.crumbs li + li::before { content: "/" / ""; margin: 0 8px; color: var(--ink-3); }
.crumbs a { color: var(--ink-2); text-decoration: underline; text-decoration-color: var(--rule); text-underline-offset: 3px; }
.crumbs a:hover { color: var(--ink); text-decoration-color: currentColor; }
.crumbs a:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.crumbs [aria-current="page"] { color: var(--ink); }
.crumbs-back { display: none; }
@media (max-width: 480px) {
  .crumbs ol { display: none; }
  .crumbs-back { display: inline; color: var(--ink); }
}
```

#### States

- Hover: ancestor text goes from `--ink-2` to `--ink` and the underline goes from `--rule` to full ink.
- Current: no hover, no pointer cursor, no underline.
- Collapsed: the "..." button opens a menu (see 4.25) listing the hidden levels.

#### Copy

```slop
Home > Dashboard > Settings > General Settings > Settings
Back
```

- Projects / Halden Freight / Invoices / Invoice 1042
- Back to Invoices

#### Checklist

- Only on hierarchies 3 or more levels deep.
- `nav` with `aria-label`, an ordered list, `aria-current` on the last item.
- Separators hidden from assistive tech; no chevron icons with alt text.
- No pill background; 14px, two ink levels.
