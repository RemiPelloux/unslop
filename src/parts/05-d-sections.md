### 5.19 Call-to-action sections

#### What the machine produces

```slop
<section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 px-8 py-24 text-center shadow-2xl">
  <div className="absolute -top-24 left-1/2 h-96 w-96 -translate-x-1/2 rounded-full bg-white/20 blur-3xl" />
  <h2 className="text-5xl font-bold text-white">Ready to transform your workflow?</h2>
  <p className="mt-4 text-xl text-indigo-100">Join thousands of teams already building the future.</p>
  <div className="mt-10 flex justify-center gap-4">
    <button className="rounded-full bg-white px-8 py-4 font-semibold text-indigo-600 shadow-lg">Get started for free</button>
    <button className="rounded-full border border-white/30 px-8 py-4 text-white backdrop-blur">Book a demo</button>
  </div>
</section>
```

This is the closing band from Tailwind UI "CTA sections, brand panel": a three-stop gradient slab with a blurred white orb, a rhetorical question for a headline, and two pill buttons. The question and "Join thousands of teams" could close any page on the web.

#### Rules

1. The headline states the next step and what it costs: "Start a 14-day trial. Bring one month of bank statements."
2. One primary button and at most one text link. Never two equal buttons.
3. The band uses `--paper-2` with 1px `--rule` borders top and bottom, 96px vertical padding, left-aligned text at most 66ch.
4. Say what happens after the click in one 14px line under the button: "No card until day 14. Cancel in Settings."
5. One closing CTA per page. Repeating the hero button 4 times down the page is a template habit.
6. No questions, no "Ready to", no orbs, no full-bleed accent color.

#### Reference build

```html
<section class="cta" aria-labelledby="cta-h">
  <h2 id="cta-h">Start a 14-day trial. Bring one month of bank statements.</h2>
  <p>Import takes about 4 minutes. You will see matched and unmatched lines before you pay anything.</p>
  <a class="btn btn-fill" href="/signup">Start 14-day trial</a>
  <a class="cta-alt" href="/sales">or book a call with sales</a>
  <p class="cta-note">No card until day 14. Cancel in Settings.</p>
</section>
```

```css
.cta { padding: 96px max(16px, calc((100% - 1040px) / 2)); background: var(--paper-2); border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); }
.cta h2 { max-width: 24ch; margin: 0 0 16px; font-size: 32px; line-height: 1.2; }
.cta p { max-width: 66ch; margin: 0 0 24px; color: var(--ink-2); }
.cta .btn { display: inline-block; padding: 12px 20px; }
.cta-alt { margin-left: 16px; color: var(--ink); text-underline-offset: 3px; }
.cta-note { margin: 16px 0 0; font-size: 14px; }
```

#### Copy

```slop
Ready to transform your workflow?
Join thousands of teams already building the future.
Get started for free
Take your business to the next level
```

- Start a 14-day trial. Bring one month of bank statements.
- Start 14-day trial
- No card until day 14. Cancel in Settings.

#### Checklist

- Headline names the step and its cost. No question.
- One primary button, one optional text link.
- `--paper-2` band with borders, no gradient, no orb.
- One closing CTA per page.

### 5.20 FAQ sections

#### What the machine produces

```slop
<div className="mx-auto max-w-3xl space-y-4">
  <h2 className="bg-gradient-to-r from-indigo-500 to-purple-600 bg-clip-text text-center text-4xl font-bold text-transparent">Frequently Asked Questions</h2>
  {faqs.map(f => (
    <Disclosure as="div" className="rounded-2xl bg-white p-6 shadow-md">
      <Disclosure.Button className="flex w-full justify-between font-medium">{f.q}<ChevronDownIcon className="ui-open:rotate-180 transition duration-500" /></Disclosure.Button>
      <Disclosure.Panel className="mt-4 text-gray-500">{f.a}</Disclosure.Panel>
    </Disclosure>
  ))}
</div>
```

The FAQ from a landing template: centered gradient heading, each question in its own shadowed card, a chevron that spins over 500ms. The questions are written by marketing ("Is it easy to use?") and answered with a yes.

#### Rules

1. Questions come from support tickets and sales calls. Keep a source for each. "Is it easy to use?" is not a question anyone asks.
2. Answer in the first sentence: "Yes, up to 10,000 rows per file." Then details. At most 80 words, with a link for more.
3. Use native `<details>` and `<summary>`. Rows are separated by 1px `--rule` lines. No cards.
4. Question text 16px weight 600 in `--ink`, answer 16px `--ink-2` at most 66ch. Marker is a 16px stroked plus that turns into a minus, with no rotation animation.
5. At most 10 questions. Group by topic under 18px headings when there are more.
6. Each question has an anchor so support can link to it.

#### Reference build

```html
<section class="faq" aria-labelledby="faq-h">
  <h2 id="faq-h">Questions</h2>
  <details id="csv-limit">
    <summary>Is there a limit on CSV imports?</summary>
    <p>Yes, 10,000 rows per file and 20 files per hour. Larger files can be split with the import tool. <a href="/docs/import#limits">Import limits</a></p>
  </details>
  <details id="leave">
    <summary>What happens to our data if we cancel?</summary>
    <p>It stays read-only for 90 days, then we delete it. You can export everything as CSV or PDF at any point.</p>
  </details>
</section>
```

```css
.faq { max-width: 66ch; margin: 0 auto; padding: 96px 16px; }
.faq h2 { font-size: 32px; margin: 0 0 24px; }
.faq details { border-top: 1px solid var(--rule); }
.faq details:last-of-type { border-bottom: 1px solid var(--rule); }
.faq summary { display: flex; justify-content: space-between; gap: 16px; padding: 16px 0; font-weight: 600; cursor: pointer; list-style: none; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; font: 400 21px/1 var(--font-mono); color: var(--ink-2); }
.faq details[open] summary::after { content: "-"; }
.faq summary:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.faq p { margin: 0 0 16px; color: var(--ink-2); }
```

#### Copy

```slop
Frequently Asked Questions
Is it easy to use?
Absolutely! Our intuitive interface makes it a breeze.
Still have questions? Don't hesitate to reach out!
```

- Questions
- What happens to our data if we cancel?
- Yes, 10,000 rows per file and 20 files per hour.
- Not answered here? Email support@ledgerline.example. We reply within 4 working hours.

#### Checklist

- Real questions with a source, first sentence answers.
- Native `details`, rows with rules, no cards.
- 10 questions or fewer, each with an anchor.
- No spinning chevron.

### 5.21 Comparison tables

#### What the machine produces

```slop
<table className="w-full overflow-hidden rounded-2xl shadow-xl">
  <thead className="bg-gradient-to-r from-indigo-500 to-purple-600 text-white">
    <tr><th>Feature</th><th>Us</th><th>Competitor A</th><th>Competitor B</th></tr>
  </thead>
  <tbody>
    <tr><td>AI-powered insights</td><td><CheckCircleIcon className="text-emerald-500" /></td><td><XCircleIcon className="text-red-400" /></td><td><XCircleIcon className="text-red-400" /></td></tr>
    <tr><td>Seamless integrations</td><td><CheckCircleIcon className="text-emerald-500" /></td><td><XCircleIcon className="text-red-400" /></td><td><MinusIcon /></td></tr>
  </tbody>
</table>
```

The versus table from a "Why us" page: a gradient header, green checks in our column and red crosses in every other, and rows chosen so we win each one. Readers discount it to zero, and the claims are often out of date within a quarter.

#### Rules

1. Compare facts a buyer can check: limits, prices, supported formats, contract terms. Every competitor cell has a source link and a "checked on" date.
2. Include rows where you lose. A table with no losses is not believed.
3. Cells hold text or numbers: "10,000 rows", "CSV, OFX", "Not offered". No green checks against red crosses.
4. Header row `--paper-2` with a 1px `--ink` bottom border. Body rows separated by 1px `--rule`. First column left-aligned and sticky on narrow screens. Numbers right-aligned in tabular numerals.
5. Use `<th scope="col">` and `<th scope="row">`, and a `<caption>` that states the date.
6. Highlight your own column with `--paper-2` background only.

#### Reference build

```html
<div class="cmp-wrap">
  <table class="cmp">
    <caption>Checked against public pricing pages on 1 Oct 2026</caption>
    <thead><tr><th scope="col">Plan for 10 users</th><th scope="col" class="ours">Ledgerline Team</th><th scope="col">Other tool A</th></tr></thead>
    <tbody>
      <tr><th scope="row">Price per year</th><td class="ours num">$2,880</td><td class="num">$2,400</td></tr>
      <tr><th scope="row">Bank import formats</th><td class="ours">CSV, OFX, CAMT.053</td><td>CSV</td></tr>
      <tr><th scope="row">Rows per import</th><td class="ours num">10,000</td><td class="num">50,000</td></tr>
    </tbody>
  </table>
</div>
```

```css
.cmp-wrap { overflow-x: auto; border: 1px solid var(--rule); }
.cmp { width: 100%; min-width: 560px; border-collapse: collapse; font-size: 14px; }
.cmp caption { caption-side: bottom; padding: 12px 16px; text-align: left; color: var(--ink-3); font-size: 12px; }
.cmp th, .cmp td { padding: 12px 16px; text-align: left; border-top: 1px solid var(--rule); vertical-align: top; }
.cmp thead th { background: var(--paper-2); border-top: 0; border-bottom: 1px solid var(--ink); font-weight: 600; }
.cmp tbody th { position: sticky; left: 0; background: var(--paper); font-weight: 500; }
.cmp .ours { background: var(--paper-2); }
.cmp .num { text-align: right; font-variant-numeric: tabular-nums; }
```

#### Copy

```slop
Why we're the obvious choice
AI-powered insights
Competitor A: Limited
```

- Checked against public pricing pages on 1 Oct 2026
- Rows per import: 10,000 (Other tool A: 50,000)
- Not offered

#### Checklist

- Checkable facts with sources and dates.
- At least one row you lose.
- Text in cells, no check and cross icons.
- Real table markup with scoped headers and a dated caption.

### 5.22 Error pages

#### What the machine produces

```slop
<div className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-br from-indigo-50 via-white to-purple-50">
  <h1 className="bg-gradient-to-r from-indigo-500 to-purple-600 bg-clip-text text-[12rem] font-black text-transparent">404</h1>
  <img src="/astronaut-floating.svg" className="w-64 animate-bounce" />
  <h2 className="text-3xl font-bold">Oops! Lost in space?</h2>
  <p className="text-gray-500">The page you're looking for doesn't exist or has been moved.</p>
  <button className="mt-8 rounded-full bg-gradient-to-r from-indigo-500 to-purple-600 px-8 py-3 text-white shadow-lg">Take me home</button>
</div>
```

The 404 from template packs: a 192px gradient "404", a bouncing astronaut illustration, a joke headline, and one button home. The 500 page is usually the same layout with "Houston, we have a problem". Neither says what happened or what the user can do besides leave.

#### Rules

1. Keep the site header and navigation on error pages so the user can continue from where they are.
2. The heading says what happened in plain words: "This page does not exist", "Something failed on our side". The status code goes in 14px `--ink-3` text, not 192px.
3. Offer the 2 or 3 most likely next steps as links: search, the parent page, the home page.
4. For 404s on old URLs, add redirects. Log every 404 with its referrer and fix the top 20 each month.
5. For 500s, show a reference ID the user can quote to support, the time in UTC, and a link to the status page. Never show a stack trace.
6. For 503 maintenance, give the end time in the user's time zone.
7. No jokes, no illustrations, no animation. The user is already annoyed.
8. Return the real HTTP status. A 404 page served with 200 pollutes search indexes.

#### Reference build

```html
<main class="err">
  <p class="err-code">Error 500</p>
  <h1>Something failed on our side</h1>
  <p>Your last change was not saved. Try again in a minute. If it fails twice, send support the reference below.</p>
  <dl class="err-ref"><dt>Reference</dt><dd><code>req_7f3a91c2</code></dd><dt>Time</dt><dd>15 Oct 2026, 14:22 UTC</dd></dl>
  <ul><li><a href="javascript:location.reload()">Try again</a></li><li><a href="https://status.example.com">Service status</a></li><li><a href="/invoices">Back to invoices</a></li></ul>
</main>
```

```css
.err { max-width: 66ch; margin: 0 auto; padding: 96px 16px; }
.err-code { margin: 0 0 8px; font-size: 14px; color: var(--ink-3); }
.err h1 { margin: 0 0 16px; font-size: 32px; line-height: 1.2; }
.err p { color: var(--ink-2); }
.err-ref { display: grid; grid-template-columns: max-content 1fr; gap: 4px 16px; margin: 24px 0; padding: 16px; background: var(--paper-2); border: 1px solid var(--rule); font-size: 14px; }
.err-ref dt { color: var(--ink-2); }
.err-ref dd { margin: 0; }
.err ul { padding-left: 16px; line-height: 2; }
.err a { color: var(--ink); text-underline-offset: 3px; }
```

#### Copy

```slop
Oops! Lost in space?
Houston, we have a problem.
Something went wrong. Please try again later.
Take me home
```

- This page does not exist. It may have been renamed when we moved the docs in June.
- Something failed on our side. Your last change was not saved.
- Down for maintenance until 16:00 your time (15:00 UTC).
- Reference req_7f3a91c2

#### Checklist

- Header and navigation kept.
- Plain heading, small status code, real HTTP status.
- Next steps as links, reference ID on 500s.
- No jokes, illustrations or bouncing.

### 5.23 Auth screens

#### What the machine produces

```slop
<div className="grid min-h-screen lg:grid-cols-2">
  <div className="hidden bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 p-12 lg:flex lg:flex-col lg:justify-end">
    <p className="text-2xl text-white">"This platform changed everything for us."</p>
  </div>
  <div className="flex items-center justify-center">
    <div className="w-full max-w-md rounded-3xl bg-white/80 p-10 shadow-2xl backdrop-blur">
      <h1 className="text-3xl font-bold">Welcome back!</h1>
      <div className="mt-6 grid grid-cols-4 gap-3">{['Google','GitHub','Apple','X'].map(p => <button className="rounded-xl border p-3 shadow-sm"><Logo name={p} /></button>)}</div>
      <input className="mt-6 w-full rounded-xl border p-3" placeholder="Email" />
      <input className="mt-3 w-full rounded-xl border p-3" type="password" placeholder="Password" onPaste={e => e.preventDefault()} />
      <button className="mt-6 w-full rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 py-3 text-white"><SparklesIcon /> Sign in with magic link</button>
    </div>
  </div>
</div>
```

This is the shadcn "Authentication" example: a split screen with a gradient art panel and an anonymous quote, a glass card, four icon-only provider buttons, and placeholder-only fields. Blocking paste breaks password managers, and the icon-only buttons have no accessible names.

#### Rules

1. One column, 400px maximum, on `--paper`, with the product name at the top. No split-screen art panel.
2. Every field has a visible label. Use `autocomplete="email"`, `current-password` on sign-in and `new-password` on sign-up. Never block paste.
3. Show or hide the password with a text button, "Show", inside the field. No confirm-password field.
4. State password rules before typing: "At least 12 characters." No rainbow strength meter.
5. Offer at most 3 identity providers, as full-width outlined buttons with the name in text: "Continue with Google".
6. Password reset never confirms whether an account exists: "If an account exists for ana@harbor.co, we sent a link. It expires in 30 minutes."
7. After 5 failed attempts, say when the user can try again: "Try again at 14:40, or reset your password."
8. Pick "Sign in" or "Log in" and use the same verb for signing out.

#### Reference build

```html
<main class="auth">
  <p class="auth-brand">Ledgerline</p>
  <h1>Sign in</h1>
  <a class="btn-outline auth-sso" href="/sso/google">Continue with Google</a>
  <p class="auth-or">or with email</p>
  <form method="post" action="/signin">
    <label for="em">Email</label>
    <input id="em" name="email" type="email" autocomplete="email" required>
    <label for="pw">Password</label>
    <div class="pw"><input id="pw" name="password" type="password" autocomplete="current-password" required><button type="button" aria-controls="pw" aria-pressed="false">Show</button></div>
    <button type="submit" class="btn-fill">Sign in</button>
  </form>
  <p class="auth-links"><a href="/reset">Reset password</a> <a href="/signup">Create an account</a></p>
</main>
```

```css
.auth { max-width: 400px; margin: 0 auto; padding: 64px 16px; }
.auth-brand { margin: 0 0 32px; font-weight: 600; }
.auth h1 { margin: 0 0 24px; font-size: 24px; }
.auth label { display: block; margin: 16px 0 4px; font-size: 14px; font-weight: 600; }
.auth input { width: 100%; height: 40px; padding: 0 12px; border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper); font: 16px var(--font-sans); }
.auth input:focus-visible, .auth button:focus-visible, .auth a:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.pw { position: relative; }
.pw input { padding-right: 64px; }
.pw button { position: absolute; right: 4px; top: 4px; height: 32px; padding: 0 8px; background: none; border: 0; color: var(--ink-2); font: 14px var(--font-sans); cursor: pointer; }
.auth .btn-fill, .auth-sso { display: block; width: 100%; margin-top: 24px; padding: 10px; text-align: center; border-radius: var(--radius); }
.auth-or { margin: 24px 0 0; font-size: 14px; color: var(--ink-3); }
.auth-links { display: flex; justify-content: space-between; margin-top: 24px; font-size: 14px; }
```

#### Copy

```slop
Welcome back!
Oops! Invalid credentials.
We couldn't find an account with that email.
Sign in with magic link
```

- Sign in
- Email or password is wrong. Check both, or reset your password.
- If an account exists for ana@harbor.co, we sent a link. It expires in 30 minutes.

#### Checklist

- One 400px column, visible labels, correct `autocomplete`.
- Paste allowed, "Show" as text, no confirm field.
- Provider buttons named in text, 3 or fewer.
- Reset never reveals whether an account exists.

### 5.24 Chat and AI assistant interfaces

#### What the machine produces

```slop
<button className="fixed bottom-6 right-6 flex h-14 w-14 items-center justify-center rounded-full bg-gradient-to-br from-violet-500 to-fuchsia-500 shadow-2xl shadow-purple-500/50 animate-pulse">
  <SparklesIcon className="h-6 w-6 text-white" />
</button>
<div className="fixed bottom-24 right-6 w-96 rounded-3xl bg-white/90 shadow-2xl backdrop-blur-xl">
  <div className="rounded-t-3xl bg-gradient-to-r from-violet-600 to-indigo-600 p-4 text-white">AI Assistant <span className="text-xs">Powered by AI</span></div>
  <div className="space-y-3 p-4">
    <div className="ml-auto w-fit rounded-2xl rounded-br-sm bg-gradient-to-r from-violet-500 to-purple-600 px-4 py-2 text-white">How many invoices are overdue?</div>
    <div className="flex gap-1"><span className="h-2 w-2 animate-bounce rounded-full bg-purple-400" /><span className="h-2 w-2 animate-bounce rounded-full bg-purple-400 [animation-delay:150ms]" /><span className="h-2 w-2 animate-bounce rounded-full bg-purple-400 [animation-delay:300ms]" /></div>
  </div>
  <input placeholder="Ask me anything..." className="m-4 rounded-full border px-4 py-2" />
</div>
```

This is the AI widget every product added in 2023 and 2024: a pulsing violet sparkle bubble in the corner, a chat panel with a purple header, gradient user bubbles, and three bouncing dots that pretend someone is typing. The sparkle and the purple come from early AI product launches and now mean "bolted on".

#### Rules

1. Name the feature by what it does with the user's data: "Ask about invoices". Never "AI Assistant", never a sparkle icon.
2. Put it in the page as a 400px side panel or inline under the thing it answers about. No floating corner bubble, no pulse.
3. Use the product's own palette. `--accent` appears only on the send button. No purple, no gradients.
4. Messages are full-width blocks, not bubbles. Each has a 12px speaker label, "You" or "Assistant". User messages sit on `--paper-2`, answers on `--paper`. Text is 16px at 66ch.
5. Stream text as it arrives. Before the first token, describe the real step: "Reading 214 invoices". No typing dots.
6. While streaming, the send button becomes "Stop". Stopping keeps the partial answer, marked "Stopped".
7. Any answer drawn from the user's records cites them as links: "INV-2041, INV-2057".
8. An answer that proposes a change shows the change as a diff and an "Apply" button. Nothing changes without that click.
9. The composer grows to 8 lines. Enter sends, Shift+Enter adds a line. Show that hint once, in 12px `--ink-3`.
10. Show at most 3 suggested questions, only in the empty state, and make them about the current page.
11. The transcript is `role="log"`. Announce a finished answer, not each token.

#### Reference build

```html
<aside class="ask" aria-labelledby="ask-h">
  <h2 id="ask-h">Ask about invoices</h2>
  <div class="ask-log" role="log" aria-live="polite">
    <div class="msg msg-you"><p class="who">You</p><p>How many invoices are overdue?</p></div>
    <div class="msg"><p class="who">Assistant</p><p>7 invoices are overdue, $18,240.00 in total. The oldest is INV-2041 from Acme Freight, 41 days late.</p>
      <p class="src">Sources: <a href="/invoices?status=overdue">7 overdue invoices</a></p></div>
  </div>
  <form class="ask-form"><label for="ask-q" class="sr-only">Question</label>
    <textarea id="ask-q" rows="1" placeholder="Ask about amounts, customers or dates"></textarea>
    <button type="submit" class="btn-fill">Send</button></form>
</aside>
```

```css
.ask { display: flex; flex-direction: column; width: 400px; max-width: 100%; height: 100%; border-left: 1px solid var(--rule); background: var(--paper); }
.ask h2 { margin: 0; padding: 12px 16px; font-size: 14px; font-weight: 600; border-bottom: 1px solid var(--rule); }
.ask-log { flex: 1; overflow-y: auto; }
.msg { padding: 16px; border-bottom: 1px solid var(--rule); }
.msg-you { background: var(--paper-2); }
.msg p { margin: 0 0 8px; max-width: 66ch; }
.who { font-size: 12px; color: var(--ink-3); }
.src { font-size: 14px; color: var(--ink-2); }
.ask-form { display: flex; gap: 8px; align-items: flex-end; padding: 12px 16px; border-top: 1px solid var(--rule); }
.ask-form textarea { flex: 1; min-height: 40px; max-height: 192px; padding: 8px 12px; border: 1px solid var(--rule); border-radius: var(--radius); font: 16px/1.5 var(--font-sans); resize: none; field-sizing: content; }
.ask-form .btn-fill { height: 40px; padding: 0 16px; }
```

#### Copy

```slop
Hi there! I'm your AI-powered assistant. How can I help you today?
Ask me anything...
Great question! Let me dive into that for you.
As an AI, I cannot...
```

- Ask about invoices
- Reading 214 invoices
- 7 invoices are overdue, $18,240.00 in total.
- I can only see invoices in Harbor Supply. Payroll data is not connected.

#### Checklist

- Named by task, placed in the page, no corner bubble.
- No sparkle, no purple, no gradient, no typing dots.
- Block messages with speaker labels, sources linked.
- Changes shown as diffs and applied only on click.

### 5.25 Dashboards as a whole

#### What the machine produces

```slop
<h1 className="text-3xl font-bold">Good morning, Alex</h1>
<div className="mt-6 grid grid-cols-4 gap-6">
  <Card className="rounded-2xl shadow-lg"><div className="rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 p-3"><CurrencyDollarIcon /></div><p className="text-3xl font-bold">$45,231.89</p><span className="rounded-full bg-emerald-100 px-2 text-emerald-700">+20.1%</span></Card>
  ...
</div>
<div className="mt-6 grid grid-cols-3 gap-6">
  <Card className="col-span-2"><AreaChart fill="url(#indigoFade)" /></Card>
  <Card><DonutChart data={eightSlices} /></Card>
  <Card className="col-span-3"><SparklesIcon /> AI Insights: Revenue is trending up.</Card>
</div>
```

This is the shadcn "Dashboard" example with its `$45,231.89` and `+20.1% from last month`, extended by a model: a greeting, four KPI cards with icons in gradient circles, an area chart with a fading indigo fill, an eight-slice donut, and an `AI Insights` card that restates the chart. Every panel is a shadowed card, so nothing has more weight than anything else.

#### Rules

1. Start from the 3 questions the user asks every day, and give each one panel. Track clicks and remove any panel nobody opened in 30 days.
2. Title the page with its scope and range: "Overview, 1 to 15 Oct 2026". No greeting.
3. One date range control at the top drives every panel. Each comparison names its period.
4. At most 4 KPIs in one row, built as in 5.18. Every number links to the filtered list behind it.
5. Panels are regions with a 1px `--rule` border and a 40px header on `--paper-2`, laid out on a 12-column grid with 24px gutters. No cards, no shadows.
6. Use line and bar charts. Donuts only for 2 or 3 parts. Area fills are flat `--paper-3` or nothing. Chart rules live in 4.8, and chart color in 2.10.
7. Each panel loads on its own, with a placeholder the size of its final content.
8. Show freshness as text: "Updated 14:05". No "LIVE" pill and no green pulsing dot.

#### Reference build

```html
<header class="dash-head"><h1>Overview, 1 to 15 Oct 2026</h1><p>Updated 14:05</p></header>
<div class="dash">
  <section class="panel span-8" aria-labelledby="p-cash"><h2 id="p-cash">Cash in and out, by week</h2><div class="panel-body">...</div></section>
  <section class="panel span-4" aria-labelledby="p-over"><h2 id="p-over">Overdue invoices</h2>
    <div class="panel-body"><table>...</table><a href="/invoices?status=overdue">View all 7</a></div></section>
</div>
```

```css
.dash-head { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 24px; }
.dash-head h1 { margin: 0; font-size: 24px; }
.dash-head p { margin: 0; font-size: 14px; color: var(--ink-3); }
.dash { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 24px; }
.span-8 { grid-column: span 8; } .span-4 { grid-column: span 4; }
.panel { border: 1px solid var(--rule); background: var(--paper); }
.panel h2 { margin: 0; height: 40px; line-height: 40px; padding: 0 16px; font-size: 14px; font-weight: 600; background: var(--paper-2); border-bottom: 1px solid var(--rule); }
.panel-body { padding: 16px; }
@media (max-width: 960px) { .span-8, .span-4 { grid-column: 1 / -1; } }
```

#### Copy

```slop
Good morning, Alex
AI Insights: Revenue is trending up.
+20.1% from last month
LIVE
```

- Overview, 1 to 15 Oct 2026
- Overdue invoices: 7, $18,240.00
- Revenue $84,120, +4.1% vs 1 to 15 Sep
- Updated 14:05

#### Checklist

- Each panel answers a named daily question.
- Scope and range in the title, one range control.
- Bordered panels on a 12-column grid, no cards.
- Numbers link to their lists. No greeting, no LIVE pill.
