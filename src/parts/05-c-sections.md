### 5.12 Testimonials

#### What the machine produces

```slop
<div className="grid gap-8 md:grid-cols-3">
  <div className="rounded-2xl bg-white p-8 shadow-xl ring-1 ring-gray-100">
    <div className="flex gap-1 text-yellow-400"><StarIcon /><StarIcon /><StarIcon /><StarIcon /><StarIcon /></div>
    <p className="mt-4 text-lg text-gray-700">"This tool is an absolute game-changer! Our productivity skyrocketed and the team loves it."</p>
    <div className="mt-6 flex items-center gap-3">
      <img src="https://i.pravatar.cc/100?img=47" className="h-12 w-12 rounded-full ring-2 ring-indigo-500" />
      <div><p className="font-semibold">Sarah Johnson</p><p className="text-sm text-gray-500">CEO at TechCorp</p></div>
    </div>
  </div>
  ...
</div>
```

This is the Tailwind UI testimonial grid filled by a model: avatars from `i.pravatar.cc`, five yellow stars copied from review widgets, and a placeholder name with a placeholder company. The quote praises the product in general terms and contains no fact a reader could check. Readers have seen "Sarah Johnson, CEO at TechCorp" so often that it now marks the whole page as fake.

#### Rules

1. Publish only quotes from named people who approved the exact wording in writing. Keep the approval on file with its date. No real quote, no section.
2. Each quote carries one checkable claim: a number, a task, a before and after. At most 60 words. Cut with "..." if needed. Never reword.
3. Attribution is full name, role, company, and a link to the case study when one exists. Use a photo only if the person supplied it. Otherwise show no image at all, and no initials in a colored circle.
4. Star ratings only from a named review site, with the score, the review count and a link: "4.6 from 212 reviews".
5. At most 3 quotes on a page. One long quote with a link to the full case study beats a wall of 12. No carousel, no marquee.
6. Quote text is `--font-serif` at 21px with 1.4 line height. Attribution is 14px sans. No 120px decorative quotation mark.

#### Reference build

```html
<figure class="quote">
  <blockquote><p>We closed March in 3 days instead of 9. The bank import matched 96% of our transactions without a single manual edit.</p></blockquote>
  <figcaption>Dana Okafor, Controller, Harbor Supply. <a href="/customers/harbor-supply">Read how they set it up</a></figcaption>
</figure>
```

```css
.quote { max-width: 66ch; margin: 48px 0; padding-left: 24px; border-left: 2px solid var(--ink); }
.quote blockquote { margin: 0; }
.quote p { margin: 0; font: 21px/1.4 var(--font-serif); color: var(--ink); }
.quote figcaption { margin-top: 16px; font: 14px/1.5 var(--font-sans); color: var(--ink-2); }
.quote a { color: var(--ink); text-underline-offset: 3px; }
```

#### States

- One quote: full width, as above.
- Two or three: stacked vertically, 48px apart. A three-column grid of quotes forces equal lengths and invites padding.

#### Copy

```slop
"An absolute game-changer for our team!"
"I can't imagine working without it. Five stars!"
"Seamless, intuitive, and powerful."
Sarah Johnson, CEO at TechCorp
```

- "We closed March in 3 days instead of 9." Dana Okafor, Controller, Harbor Supply
- "Support answered our SAML question in 40 minutes, on a Sunday." Luis Ferreira, IT lead, Norte Freight
- 4.6 from 212 reviews

#### Checklist

- Real person, approved wording, approval on file.
- One checkable claim per quote, 60 words or fewer.
- No stock avatars, no initials circles, no unsourced stars.
- Three quotes or fewer, no carousel.

### 5.13 Timelines and changelogs

#### What the machine produces

```slop
<div className="relative">
  <div className="absolute left-1/2 h-full w-1 bg-gradient-to-b from-indigo-500 via-purple-500 to-pink-500" />
  <div className="mb-12 flex w-1/2 justify-end pr-8">
    <div className="rounded-2xl bg-white p-6 shadow-xl">
      <span className="rounded-full bg-gradient-to-r from-emerald-400 to-cyan-400 px-3 py-1 text-xs text-white">New</span>
      <h3 className="mt-2 text-xl font-bold">Introducing AI Insights</h3>
      <p className="text-gray-500">We're thrilled to announce our most powerful release yet...</p>
    </div>
  </div>
</div>
```

This is the zigzag timeline from template marketplaces: a gradient spine down the middle, cards alternating left and right, and colored pills for "New", "Improved" and "Fixed". Alternating sides makes dates impossible to scan, and the entries open with excitement before saying what changed.

#### Rules

1. One column. The date sits in a fixed 128px left column. Newest first.
2. Write dates as "8 Oct 2026" and versions in `--font-mono`. Never "2 weeks ago" on a changelog.
3. One entry per release. The title says what changed in user terms: "Bank rules can match on amount ranges".
4. Group items under plain headings: Added, Changed, Fixed, Removed. No colored pills.
5. Each item is one sentence that starts with the thing that changed and links to its docs.
6. Every entry has an anchor. Publish an Atom or RSS feed.
7. In-app activity timelines use rows of time (12px mono), actor, action and object, grouped under a day heading. The spine, if any, is 1px `--rule`, with 8px square markers in `--ink`.

#### Reference build

```html
<article class="log" id="v4-12">
  <p class="log-date"><time datetime="2026-10-08">8 Oct 2026</time><br><code>v4.12</code></p>
  <div class="log-body">
    <h3>Bank rules can match on amount ranges</h3>
    <h4>Added</h4>
    <ul><li>Bank rules accept a minimum and maximum amount. <a href="/docs/rules#amount">Docs</a></li></ul>
    <h4>Fixed</h4>
    <ul><li>CSV export no longer drops the last row when a memo contains a line break.</li></ul>
  </div>
</article>
```

```css
.log { display: grid; grid-template-columns: 128px minmax(0, 66ch); gap: 24px; padding: 32px 0; border-top: 1px solid var(--rule); }
.log-date { margin: 0; font-size: 14px; color: var(--ink-2); }
.log-date code { font: 12px var(--font-mono); color: var(--ink-3); }
.log h3 { margin: 0 0 16px; font-size: 21px; line-height: 1.25; }
.log h4 { margin: 16px 0 4px; font-size: 12px; font-weight: 600; color: var(--ink-2); }
.log ul { margin: 0; padding-left: 16px; line-height: 1.6; }
@media (max-width: 600px) { .log { grid-template-columns: 1fr; gap: 8px; } }
```

#### States

- Breaking change: an item under Changed that starts with "Breaking:" and says what to do before the date it takes effect.
- Rolled back: keep the entry, strike nothing, and add a dated note under it saying what was reverted.

#### Copy

```slop
Introducing AI Insights: our most powerful release yet!
We're thrilled to announce...
Various bug fixes and performance improvements.
```

- Bank rules can match on amount ranges
- Fixed: CSV export no longer drops the last row when a memo contains a line break.
- Breaking: the v1 invoices API stops accepting requests on 1 Feb 2027. Move to v2 first.

#### Checklist

- Single column, fixed date column, newest first.
- Absolute dates, versions in mono.
- Added, Changed, Fixed, Removed as text headings.
- No "Various bug fixes". Each fix is named.

### 5.14 Tooltips and popovers

#### What the machine produces

```slop
<Tooltip>
  <TooltipTrigger><InformationCircleIcon className="h-4 w-4 text-gray-400" /></TooltipTrigger>
  <TooltipContent className="rounded-xl bg-gradient-to-br from-gray-900 to-indigo-900 px-4 py-3 text-white shadow-2xl">
    <p className="font-semibold">Pro tip</p>
    <p className="text-sm">Your API key is only shown once. <a href="/docs" className="underline">Learn more</a></p>
  </TooltipContent>
</Tooltip>
<PopoverContent className="w-80 rounded-2xl border-white/20 bg-white/70 p-6 shadow-2xl backdrop-blur-xl">...</PopoverContent>
```

This is the shadcn `Tooltip` holding information the user cannot afford to miss, plus a link that nobody can reach because the tooltip closes when the pointer leaves the icon. Info icons get scattered beside every label, and popovers get the same glass treatment as modals, with `backdrop-blur-xl` over `bg-white/70`.

#### Rules

1. A tooltip holds a short label for an icon-only control, or the full text of a truncated value. At most 80 characters. No links, no buttons, nothing the user must know.
2. Show it after 500ms of hover and at once on keyboard focus. Hide it on Escape, on blur, and 100ms after the pointer leaves both trigger and tooltip. The pointer must be able to move onto it (WCAG 1.4.13).
3. Style: `--ink` background, `--paper` text, 12px/16px, 4px by 8px padding, `--radius` corners, 240px maximum width, 8px from the trigger. Flip to the other side at the viewport edge.
4. For an icon button, the tooltip text equals its `aria-label`. For extra information, connect it with `aria-describedby`.
5. Touch screens get no tooltips. Icon-only controls on touch need a visible text label.
6. If a screen needs more than 3 info icons, write the help text into the page under the labels.
7. Popovers hold interactive content: filters, date pickers, short forms. `--paper` background, 1px `--ink` border, 16px padding, 320px maximum width. No blur.
8. Use the HTML `popover` attribute or a non-modal dialog. Focus moves into the popover on open. Escape closes it and returns focus to the trigger.

#### Reference build

```html
<span class="tip-wrap">
  <button type="button" class="icon-btn" aria-label="Duplicate invoice" aria-describedby="tip-dup">
    <svg class="i" aria-hidden="true"><use href="#i-copy"/></svg>
  </button>
  <span role="tooltip" id="tip-dup" class="tip">Duplicate invoice</span>
</span>

<button type="button" popovertarget="filters" class="btn-outline">Filters (2)</button>
<div id="filters" popover class="pop">
  <form>...</form>
</div>
```

```css
.tip-wrap { position: relative; display: inline-block; }
.tip { position: absolute; left: 50%; bottom: calc(100% + 8px); transform: translateX(-50%); max-width: 240px; padding: 4px 8px; background: var(--ink); color: var(--paper); font: 12px/16px var(--font-sans); border-radius: var(--radius); white-space: nowrap; opacity: 0; pointer-events: none; transition: opacity 100ms ease-out; }
.tip-wrap:hover .tip { opacity: 1; pointer-events: auto; transition-delay: 500ms; }
.tip-wrap:focus-within .tip { opacity: 1; transition-delay: 0ms; }
@media (hover: none) { .tip { display: none; } }
@media (prefers-reduced-motion: reduce) { .tip { transition: none; } }
.pop { margin: 0; padding: 16px; width: 320px; max-width: calc(100vw - 32px); background: var(--paper); color: var(--ink); border: 1px solid var(--ink); border-radius: var(--radius); }
.pop::backdrop { background: transparent; }
```

Escape-to-close needs a few lines of script. CSS cannot do it.

#### States

- Truncated text: the tooltip appears only when the text is actually cut off. Check `scrollWidth > clientWidth` before attaching it.
- Popover open: the trigger gets `aria-expanded="true"` and a `--paper-3` background.

#### Copy

```slop
Pro tip: Your API key is only shown once!
Hover for more info
Learn more
```

- Duplicate invoice
- Due 14 Nov 2026 (net 30)
- Filters (2)

#### Checklist

- Tooltips hold labels, never required information or links.
- 500ms hover delay, instant on focus, hoverable, Escape closes.
- `--ink` tooltip, `--paper` popover with 1px `--ink` border.
- No info icon farms, no blur, no tooltips on touch.

### 5.15 User menus and account switchers

#### What the machine produces

```slop
<DropdownMenu>
  <DropdownMenuTrigger className="relative rounded-full p-0.5 bg-gradient-to-tr from-indigo-500 to-pink-500">
    <img src={user.avatar} className="h-9 w-9 rounded-full border-2 border-white" />
    <span className="absolute bottom-0 right-0 h-3 w-3 rounded-full bg-green-500 ring-2 ring-white" />
  </DropdownMenuTrigger>
  <DropdownMenuContent className="w-64 rounded-xl shadow-xl">
    <DropdownMenuItem><UserIcon /> Profile</DropdownMenuItem>
    <DropdownMenuItem className="bg-gradient-to-r from-indigo-500 to-purple-600 text-white"><SparklesIcon /> Upgrade to Pro</DropdownMenuItem>
    <DropdownMenuItem className="text-red-600"><ArrowRightOnRectangleIcon /> Log out</DropdownMenuItem>
  </DropdownMenuContent>
</DropdownMenu>
```

This is the shadcn `DropdownMenu` demo with an Instagram-style gradient ring on the avatar and a green online dot that tells the user they are online. An upgrade item is dressed as the primary action, and "Log out" is red as if signing out destroyed data. Workspace switchers built from the same kit show each workspace as a letter in its own gradient tile.

#### Rules

1. The trigger is a 32px avatar, square with `--radius` corners: the user's photo, or initials in `--ink` on `--paper-3`. Its accessible name is "Account: Priya Nair".
2. The menu header shows name, email, and the current workspace with the user's role, as text.
3. Order the items: Profile, Settings, Billing (owners only), Keyboard shortcuts, Help, then Sign out after a 1px `--rule` separator. At most 8 items.
4. Build it as a disclosure button controlling a list of links unless every item is an action. Use `role="menu"` only for action menus, with arrow-key handling to match.
5. The account switcher lists workspaces by name with the user's role in 12px `--ink-3`. The current one gets a 16px check SVG and `aria-current="true"`. Past 8 workspaces, add a filter field.
6. Workspace tiles are 20px squares with one letter in `--ink` on `--paper-3`, or the workspace's uploaded logo. No generated colors.
7. "Sign out" is plain `--ink` text. It is not destructive. When the user has more than one account signed in, say which one: "Sign out of Harbor Supply".
8. No presence dot on the user's own avatar.

#### Reference build

```html
<div class="acct">
  <button type="button" class="acct-btn" aria-expanded="true" aria-controls="acct-menu" aria-label="Account: Priya Nair">PN</button>
  <div id="acct-menu" class="acct-menu">
    <div class="acct-head"><p class="n">Priya Nair</p><p class="e">priya@harborsupply.com</p><p class="e">Harbor Supply, Owner</p></div>
    <ul>
      <li><a href="/profile">Profile</a></li>
      <li><a href="/settings">Settings</a></li>
      <li><a href="/settings/billing">Billing</a></li>
      <li><a href="/help">Help</a></li>
    </ul>
    <form action="/signout" method="post"><button type="submit">Sign out</button></form>
  </div>
</div>
```

```css
.acct { position: relative; }
.acct-btn { width: 32px; height: 32px; border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper-3); color: var(--ink); font: 600 12px var(--font-sans); cursor: pointer; }
.acct-btn:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.acct-menu { position: absolute; right: 0; top: 40px; width: 256px; background: var(--paper); border: 1px solid var(--ink); border-radius: var(--radius); font-size: 14px; z-index: 30; }
.acct-head { padding: 12px 16px; border-bottom: 1px solid var(--rule); }
.acct-head p { margin: 0; }
.acct-head .n { font-weight: 600; }
.acct-head .e { color: var(--ink-2); font-size: 12px; }
.acct-menu ul { list-style: none; margin: 0; padding: 4px 0; }
.acct-menu a, .acct-menu form button { display: block; width: 100%; padding: 8px 16px; color: var(--ink); text-align: left; text-decoration: none; background: none; border: 0; font: inherit; cursor: pointer; }
.acct-menu a:hover, .acct-menu form button:hover { background: var(--paper-2); }
.acct-menu form { border-top: 1px solid var(--rule); padding: 4px 0; }
```

#### States

- Closed, open, item hover, item focus. Escape closes and returns focus to the avatar.
- Switching workspace: the whole page reloads into the new workspace. Show its name in the page title at once.
- Impersonation by support staff: a full-width `--warn` bar above the app, "Viewing as Priya Nair. Actions are logged. Stop".

#### Copy

```slop
Log out
Upgrade to Pro
Hey, Priya!
My Awesome Workspace
```

- Sign out
- Sign out of Harbor Supply
- Harbor Supply, Owner
- Switch workspace

#### Checklist

- Square 32px avatar, no gradient ring, no own presence dot.
- Header names the user, email, workspace and role.
- At most 8 items, Sign out last and not red.
- Workspace tiles plain or real logos.

### 5.16 Feature grids

#### What the machine produces

```slop
<div className="grid grid-cols-1 gap-8 md:grid-cols-3">
  {[
    { icon: BoltIcon, title: 'Lightning Fast', desc: 'Experience blazing-fast performance that scales with your business.' },
    { icon: ShieldCheckIcon, title: 'Secure by Default', desc: 'Enterprise-grade security to keep your data safe.' },
    { icon: PuzzlePieceIcon, title: 'Seamless Integrations', desc: 'Connect with all your favorite tools in one click.' },
    { icon: SparklesIcon, title: 'AI-Powered', desc: 'Harness the power of AI to work smarter, not harder.' },
    { icon: UsersIcon, title: 'Real-time Collaboration', desc: 'Work together with your team, anywhere.' },
    { icon: LifebuoyIcon, title: '24/7 Support', desc: 'Our dedicated team is always here to help.' },
  ].map(f => (
    <div className="rounded-2xl p-6 shadow-sm hover:shadow-xl transition">
      <div className="flex h-12 w-12 items-center justify-center rounded-full bg-indigo-100"><f.icon className="h-6 w-6 text-indigo-600" /></div>
      <h3 className="mt-4 font-semibold">{f.title}</h3><p className="text-gray-500">{f.desc}</p>
    </div>
  ))}
</div>
```

This is the most recognisable block in machine-made marketing: six tiles in a 3 by 2 grid, each a Heroicon in an `indigo-100` circle, an adjective title, and one sentence any product could claim. Six is chosen because it fills the grid, not because the product has six things to say. "Fast", "Secure" and "24/7 Support" are table stakes and tell the reader nothing.

#### Rules

1. The number of features equals what the product has worth saying. Three described properly, each with a screenshot, beat six tiles.
2. A feature title states what the product does to a named object: "Match bank lines to open invoices". No adjective titles.
3. The body is 2 or 3 sentences and contains a number, a limit or a mechanism: "Matches on amount, date within 5 days, and reference. 96% of lines match without edits in our median account."
4. No icon circles. If an icon helps scanning, it is 20px, stroked, `--ink`, inline with the title. A cropped real screenshot is better than any icon.
5. Lay out features as rows: title in the left third, text and screenshot in the right two thirds, 1px `--rule` between rows, 48px vertical padding.
6. Link each feature to its docs page.
7. Move table stakes (encryption, uptime, support hours) to a specs list or the FAQ, with numbers.
8. No hover lift, no hover glow. Rows are not clickable unless the whole row is one link.

#### Reference build

```html
<section class="feat" aria-labelledby="feat-h">
  <h2 id="feat-h">What it does</h2>
  <div class="feat-row">
    <h3>Match bank lines to open invoices</h3>
    <div>
      <p>Matches on amount, date within 5 days, and reference number. In the median account, 96% of lines match without edits.</p>
      <img src="/img/match-1x.png" width="640" height="360" alt="Bank line for $4,120.00 matched to invoice INV-2041 from Acme Freight">
      <p><a href="/docs/matching">How matching works</a></p>
    </div>
  </div>
</section>
```

```css
.feat { max-width: 1040px; margin: 0 auto; padding: 96px 16px; }
.feat h2 { font-size: 32px; margin: 0 0 32px; }
.feat-row { display: grid; grid-template-columns: 1fr 2fr; gap: 32px; padding: 48px 0; border-top: 1px solid var(--rule); }
.feat-row h3 { margin: 0; font-size: 21px; line-height: 1.25; }
.feat-row p { margin: 0 0 16px; max-width: 66ch; color: var(--ink-2); }
.feat-row img { display: block; width: 100%; height: auto; border: 1px solid var(--rule); margin-bottom: 16px; }
.feat-row a { color: var(--ink); text-underline-offset: 3px; }
@media (max-width: 768px) { .feat-row { grid-template-columns: 1fr; gap: 16px; } }
```

#### States

- No screenshot available: text only. Never fill the slot with an abstract illustration or a 3D blob.
- Feature in beta: say "Beta, available on Team and Company plans" in the body text, not in a pill.

#### Copy

```slop
Lightning Fast
Seamless Integrations
AI-Powered
Harness the power of AI to work smarter, not harder.
Everything you need, all in one place.
```

- Match bank lines to open invoices
- Send reminders on day 1, 7 and 14 after the due date
- Export a VAT return as the CSV your tax office accepts

#### Checklist

- As many features as there are real ones, not six by default.
- Titles are verbs on objects. Bodies have numbers.
- No icon circles, no hover lift.
- Rows with screenshots and docs links.

### 5.17 Logo walls and social proof

#### What the machine produces

```slop
<p className="text-center text-sm font-semibold uppercase tracking-widest text-gray-500">Trusted by 10,000+ teams worldwide</p>
<div className="relative overflow-hidden [mask-image:linear-gradient(to_right,transparent,black_20%,black_80%,transparent)]">
  <div className="flex animate-marquee gap-16 grayscale opacity-60">
    <img src="/logos/google.svg" /><img src="/logos/microsoft.svg" /><img src="/logos/spotify.svg" />
    <img src="/logos/airbnb.svg" /><img src="/logos/stripe.svg" /><img src="/logos/notion.svg" />
  </div>
</div>
<div className="mt-8 flex items-center justify-center -space-x-2">
  {avatars.map(a => <img src={a} className="h-10 w-10 rounded-full ring-2 ring-white" />)}
  <span className="ml-4 text-sm">Join 5,000+ happy users</span>
</div>
```

This is the "Trusted by" strip from every landing template: logos of companies that are not customers, desaturated with `grayscale opacity-60`, scrolling in an infinite marquee behind a gradient edge mask, then an overlapping stack of stock avatars. The round number with a plus sign ("10,000+") signals that nobody counted.

#### Rules

1. Show only logos of current paying customers who gave written permission. Remove a logo within 30 days of a customer leaving.
2. Use 4 to 8 logos in one static row. No marquee, no carousel, no edge fade mask.
3. Normalise logos by visual weight, not by box. Start at 24px tall and adjust each one by eye so they read at the same size. Render them as single-color SVG using `fill: currentColor` in `--ink-2`.
4. The line above states an exact count and a date: "Used by 1,140 finance teams as of October 2026, including". No plus signs, no "worldwide".
5. Link a logo only when a case study exists, and say so in the alt text: "Harbor Supply case study".
6. Avatar stacks are banned.

#### Reference build

```html
<section class="logos" aria-labelledby="logos-h">
  <p id="logos-h">Used by 1,140 finance teams as of October 2026, including</p>
  <ul>
    <li><a href="/customers/harbor-supply"><svg role="img" aria-label="Harbor Supply case study" height="24" width="112"><use href="#logo-harbor"/></svg></a></li>
    <li><svg role="img" aria-label="Norte Freight" height="22" width="104"><use href="#logo-norte"/></svg></li>
    <li><svg role="img" aria-label="Calder Dental" height="26" width="96"><use href="#logo-calder"/></svg></li>
  </ul>
</section>
```

```css
.logos { max-width: 1040px; margin: 0 auto; padding: 48px 16px; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); }
.logos p { margin: 0 0 24px; font-size: 14px; color: var(--ink-2); }
.logos ul { display: flex; flex-wrap: wrap; align-items: center; gap: 24px 48px; margin: 0; padding: 0; list-style: none; color: var(--ink-2); }
.logos svg { display: block; fill: currentColor; }
.logos a { color: var(--ink-2); }
.logos a:hover { color: var(--ink); }
.logos a:focus-visible { outline: 2px solid var(--focus); outline-offset: 4px; }
```

#### States

- Fewer than 4 permitted logos: drop the strip and use one named quote (see 5.12) instead.
- Dark theme: logos inherit `--ink-2` from the dark tokens. Never ship a second, inverted raster set.

#### Copy

```slop
Trusted by 10,000+ teams worldwide
Join 5,000+ happy users
Loved by industry leaders
```

- Used by 1,140 finance teams as of October 2026, including
- Harbor Supply closed March in 3 days. Read the case study

#### Checklist

- Real customers, written permission, dated count.
- 4 to 8 logos, static, single color.
- No marquee, no fade mask, no avatar stack, no plus signs.

### 5.18 Stats and KPI rows

#### What the machine produces

```slop
<div className="grid grid-cols-2 gap-8 md:grid-cols-4">
  {[['10x', 'Faster workflows'], ['99.9%', 'Uptime'], ['500K+', 'Happy users'], ['24/7', 'Support']].map(([n, l]) => (
    <div className="rounded-2xl bg-white p-6 text-center shadow-lg">
      <p className="bg-gradient-to-r from-indigo-500 to-purple-600 bg-clip-text text-5xl font-extrabold text-transparent"><CountUp end={n} /></p>
      <p className="mt-2 text-gray-500">{l}</p>
    </div>
  ))}
</div>
```

This is the stats band from SaaS templates: four numbers in gradient text that count up on scroll. "10x" has no baseline, "99.9%" has no period or scope, "500K+" is a rounded guess, and "24/7" is not a statistic. The `CountUp` animation means a screenshot taken mid-scroll shows the wrong numbers.

#### Rules

1. Every number carries its unit, period and scope: "99.95% API uptime, January to September 2026".
2. Comparative claims name the baseline: "Month-end close in 3 days, down from 9, median of 40 customers who switched in 2025". No bare multipliers.
3. Write the counted number: "1,140", not "1K+". Plus signs are banned.
4. Link each figure to its source: the status page, the study, the methods note.
5. At most 4 stats in a row, separated by 1px `--rule` lines. Value 32px `--ink`, tabular numerals, weight 600. Label 14px `--ink-2` below, at most 2 lines.
6. No gradient text, no count-up animation, no cards.
7. In product dashboards, a KPI shows value, change with sign and period ("+4.1% vs September"), and color only when the direction is good or bad for that metric. Churn going up is `--bad`. Keep the sign in the text so color is never the only signal.

#### Reference build

```html
<dl class="stats">
  <div><dt>API uptime, Jan to Sep 2026</dt><dd>99.95%</dd><dd class="src"><a href="https://status.example.com">Status history</a></dd></div>
  <div><dt>Median month-end close after switching, was 9 days</dt><dd>3 days</dd></div>
  <div><dt>Finance teams using it, October 2026</dt><dd>1,140</dd></div>
</dl>
```

```css
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); margin: 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); }
.stats > div { display: flex; flex-direction: column-reverse; justify-content: flex-end; padding: 24px; border-left: 1px solid var(--rule); }
.stats > div:first-child { border-left: 0; }
.stats dt { margin-top: 8px; font-size: 14px; line-height: 1.4; color: var(--ink-2); }
.stats dd { margin: 0; font-size: 32px; line-height: 1.15; font-weight: 600; color: var(--ink); font-variant-numeric: tabular-nums; }
.stats dd.src { order: -1; margin-top: 8px; font-size: 12px; font-weight: 400; }
.stats a { color: var(--ink-2); }
```

`column-reverse` keeps the label first for screen readers and puts the number first for the eye.

#### States

- Number not yet measured: leave the stat out. Never ship "XX%" or a rounded guess.
- Stale number: show the "as of" date in the label, and review every stat each quarter.
- Dashboard KPI with no prior period: show the value alone and "No September data" in place of the change.

#### Copy

```slop
10x faster
99.9% uptime
500K+ happy users
24/7 support
Skyrocket your ROI
```

- 99.95% API uptime, January to September 2026
- Month-end close in 3 days, down from 9
- 1,140 finance teams, October 2026
- Revenue $84,120, +4.1% vs September

#### Checklist

- Unit, period, scope and source on every number.
- No multipliers without baseline, no plus signs.
- No gradient text, no count-up, no cards.
- Direction-aware color with the sign in text.
