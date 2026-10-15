### 6.8 SaaS landing page

Chapters 6.8 to 6.19 rebuild twelve pages in the same order: the page as a generator writes it, every tell in it, the rebuild, and the reasoning. Emoji in the slop versions appear as `{emoji:rocket}`, because this handbook's linter rejects the real glyphs even inside bad examples. Each rebuild loads the base stylesheet from 6.1 and adds only page-specific CSS. Every number in a rebuild is a placeholder; ship the real figure with its date, or delete the line.

The product here is an invoicing tool for small studios.

#### The slop version

```slop
<header class="sticky top-0 z-50 border-b border-white/10 bg-white/70 backdrop-blur-xl"> ... </header>
<section class="relative overflow-hidden py-32 text-center">
  <div class="absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-indigo-200 via-white to-white"></div>
  <span class="inline-flex items-center gap-2 rounded-full border border-indigo-200 bg-indigo-50 px-4 py-1 text-sm text-indigo-700">
    <span class="h-2 w-2 animate-pulse rounded-full bg-green-500"></span> New: AI-powered invoicing is here {emoji:sparkles}
  </span>
  <h1 class="mt-6 text-6xl font-extrabold tracking-tight">Invoicing,
    <span class="bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-500 bg-clip-text text-transparent">reimagined.</span></h1>
  <p class="mx-auto mt-6 max-w-2xl text-xl text-gray-600">Streamline your billing workflow and unlock seamless payments
    with our all-in-one, cutting-edge platform. Empower your team to focus on what matters most.</p>
  <button class="rounded-full bg-indigo-600 px-8 py-4 text-white shadow-xl shadow-indigo-500/30">Start Free Trial {emoji:rocket}</button>
  <button class="rounded-full border px-8 py-4">Watch Demo</button>
  <p class="text-sm text-gray-500">No credit card required. Cancel anytime.</p>
  <img src="/dashboard-mockup.png" alt="Dashboard"
       class="rounded-2xl shadow-2xl ring-1 ring-gray-900/10 [transform:perspective(1200px)_rotateX(8deg)]" />
</section>
<p class="text-center text-sm uppercase tracking-widest text-gray-400">Trusted by 10,000+ innovative teams worldwide</p>
<div class="flex justify-center gap-12 opacity-50 grayscale"><!-- six logos --></div>
<section class="grid grid-cols-3 gap-8">
  <div class="rounded-2xl border p-8 shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">
    <div class="inline-flex rounded-xl bg-indigo-100 p-3">{emoji:lightning}</div>
    <h3>Lightning-Fast Invoices</h3><p>Create stunning invoices in seconds with our intuitive editor.</p>
  </div>
  <!-- Smart Reminders, Seamless Payments, Powerful Analytics, Enterprise-Grade Security, World-Class Support -->
</section>
<section class="bg-gradient-to-r from-indigo-600 to-purple-600 py-20 text-center text-white">
  <h2>Ready to transform your workflow?</h2><p>Join thousands of happy customers today!</p>
  <button class="rounded-full bg-white px-8 py-4 text-indigo-600 shadow-xl">Get Started Now</button>
</section>
```

#### Tells

1. Frosted sticky header (`bg-white/70 backdrop-blur-xl`) from the Tailwind UI marketing templates.
2. Radial indigo glow behind the hero.
3. Announcement pill with a pulsing green dot and `AI-powered`, on a product with no AI feature anywhere else on the page.
4. Headline in the shape "Noun, `reimagined`." with the last word in gradient text via `bg-clip-text`.
5. Subhead built from `streamline`, `unlock`, `seamless`, `all-in-one`, `cutting-edge`, `empower`, and "what matters most".
6. Everything centered, paragraphs included.
7. Pill buttons with a colored glow (`shadow-indigo-500/30`) and a rocket emoji.
8. "No credit card required" with no price anywhere on the page.
9. Mockup tilted with `rotateX(8deg)` in a `rounded-2xl shadow-2xl` frame, `alt="Dashboard"`.
10. Letter-spaced gray "Trusted by 10,000+" line over grayscale logos at 50 percent opacity.
11. Six features in a 3 by 2 grid of emoji tiles with title-cased adjective headings.
12. Cards that lift on hover with a 300ms `transition-all`, though they are not links.
13. Closing gradient banner with a rhetorical question and an exclamation mark.
14. Three labels for one action: "Start Free Trial", "Get Started Now", and the header's "Get Started Free".

#### The rebuild

```html
<style>
  .site-head { border-bottom: 1px solid var(--rule); padding-block: var(--s3); }
  .hero { padding-block: var(--s8) var(--s7); }
  .hero > * + * { margin-top: var(--s5); }
  .hero h1 { font-size: var(--t-56); max-width: 20ch; }
  .shot { max-width: none; margin-top: var(--s7); }
  .shot img { width: 100%; border: 1px solid var(--rule); }
  .features { display: grid; gap: var(--s5) var(--s7); max-width: none; margin-top: var(--s5);
              grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); }
  @media (max-width: 640px) { .hero h1 { font-size: var(--t-40); } }
</style>

<header class="site-head">
  <div class="wrap split">
    <a href="/" class="link-quiet"><strong>Billfold</strong></a>
    <nav aria-label="Main" class="cluster">
      <a href="/pricing">Pricing</a> <a href="/help">Help</a> <a href="/login">Log in</a>
      <a href="/signup" class="btn btn-sm btn-primary">Create account</a>
    </nav>
  </div>
</header>
<main>
  <section class="wrap hero">
    <h1>Invoices for studios of 2 to 40 people</h1>
    <p class="lede">Write an invoice, send it from your own address, get paid by bank transfer or card.
      Billfold sends the reminder on day 7, 14 and 30, so nobody on your team has to.</p>
    <div class="cluster">
      <a href="/signup" class="btn btn-primary">Create account</a>
      <a href="/sample-invoice.pdf" class="btn">Sample invoice (PDF, 84 KB)</a>
    </div>
    <p class="small muted">Free for your first 3 clients. $12 a month after that.</p>
    <figure class="shot">
      <img src="/img/invoice-editor.png" width="1600" height="1000"
           alt="Invoice editor with three line items, a 20 percent VAT row and a due date of 14 November.">
      <figcaption class="small muted">The invoice editor: line items, tax and due date on one screen.</figcaption>
    </figure>
  </section>
  <section class="section"><div class="wrap">
    <h2>What it does</h2>
    <dl class="features">
      <div><dt>Invoices in your format</dt>
        <dd>Your logo, numbering and payment terms. Exports PDF, and UBL for EU public-sector clients.</dd></div>
      <div><dt>Reminders on a schedule</dt>
        <dd>Day 7, day 14, final notice on day 30. Edit the wording or switch any of them off.</dd></div>
      <div><dt>Payments matched to invoices</dt>
        <dd>Bank transfers are matched by amount and reference. 94 percent matched without a click in September 2026.</dd></div>
      <div><dt>A monthly export for your accountant</dt>
        <dd>CSV or DATEV on the first of the month, or a read-only login.</dd></div>
    </dl>
  </div></section>
  <section class="section"><div class="wrap">
    <blockquote>
      <p>We used to chase eleven overdue invoices a month by hand. Now it is one or two, and the email is already written.</p>
      <p class="small muted">Priya Raman, studio manager, Northbank Architects. October 2026.</p>
    </blockquote>
  </div></section>
</main>
```

#### Notes

- **The headline names the customer and the object.** The wrong visitor leaves in one second, which saves both sides time. The 2 to 40 range comes from the customer list, not a guess.
- **Four features as a definition list.** Each description holds a number, a day count, or a named format. No icons; the terms are the headings.
- **The screenshot is flat and captioned.** The perspective tilt exists to hide that the image is a mockup.
- **One action, one label, everywhere.** "Create account" in the header and the hero. The secondary action downloads a sample invoice, which answers the first question a studio asks.
- **One sourced quote replaces the logo wall.** Name, role, company and month make it checkable.

### 6.9 Developer tool landing page

The product is a command-line tool that runs Postgres migrations without long table locks.

#### The slop version

```slop
<body class="bg-[#0a0a0f] text-white">
<section class="relative py-40 text-center">
  <div class="absolute left-1/2 top-0 h-[600px] w-[900px] -translate-x-1/2 rounded-full bg-violet-600/30 blur-[120px]"></div>
  <a class="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs backdrop-blur">{emoji:party} v2.0 is here. Read more</a>
  <h1 class="bg-gradient-to-b from-white to-white/40 bg-clip-text text-7xl font-bold tracking-tighter text-transparent">
    Database migrations.<br/>Without the fear.</h1>
  <p class="text-lg text-white/60">The next-gen, developer-first platform that empowers teams to ship blazing-fast,
    zero-downtime schema changes at scale. Built for the modern stack.</p>
  <a class="rounded-lg bg-white px-5 py-3 text-black">Get started</a>
  <a class="rounded-lg border border-white/10 bg-white/5 px-5 py-3">Book a demo</a>
  <div class="rounded-xl border border-white/10 bg-black/50 p-4 font-mono shadow-[0_0_80px_rgba(139,92,246,0.35)]">
    <span class="h-3 w-3 rounded-full bg-red-500"></span><span class="... bg-yellow-500"></span><span class="... bg-green-500"></span>
    <p><span class="text-violet-400">$</span> npx shiftly init</p>
    <p class="text-green-400">{emoji:check} Done in 0.3s {emoji:sparkles}</p>
  </div>
</section>
<section class="grid grid-cols-3 gap-4">
  <div class="col-span-2 rounded-3xl border border-white/10 bg-gradient-to-br from-white/10 to-transparent p-8">
    <h3>{emoji:lightning} Blazing Fast</h3><p>10x faster migrations powered by our proprietary engine.</p></div>
  <div class="rounded-3xl ...">{emoji:shield} Enterprise-ready</div>
  <div class="rounded-3xl ...">{emoji:globe} Works everywhere</div>
  <div class="col-span-2 rounded-3xl ...">{emoji:robot} AI-assisted rollbacks</div>
</section>
<p class="text-center text-white/40">Backed by the world's best investors</p>
```

#### Tells

1. Near-black `#0a0a0f` page forced on every visitor, regardless of their system setting.
2. A 900px violet blob with `blur-[120px]`: the glow behind every developer-tool hero since 2022.
3. Headline fading from white to 40 percent white through a gradient clip.
4. Copy with `next-gen`, `empower`, `blazing`, `modern`, "at scale", "developer-first", and an exclamation-free but claim-free "Without the fear".
5. A terminal with three traffic-light dots, a violet glow, and output that says "Done in 0.3s" with emoji. No real command output.
6. Bento grid of `rounded-3xl` translucent tiles, uneven spans chosen for looks.
7. "10x faster" with no baseline, no workload, no method.
8. "Book a demo" for a CLI that installs in one line.
9. Investor line in place of a licence, a version number, or a supported Postgres range.

#### The rebuild

```html
<style>
  .hero { padding-block: var(--s8) var(--s7); }
  .hero > * + * { margin-top: var(--s4); }
  .hero h1 { font-family: var(--font-mono); font-weight: 500; }
  .plan code { font-size: var(--t-14); }
</style>

<main class="wrap">
  <section class="hero">
    <h1>pgshift</h1>
    <p class="lede">Runs Postgres schema migrations without locking busy tables. It splits each
      <code>ALTER TABLE</code> into steps that hold a lock for under 50 ms, and stops before
      running anything it cannot split.</p>
    <pre><code>npm install -g pgshift     # or: brew install pgshift</code></pre>
    <p class="small muted">Version 2.0.3, 2 October 2026. Postgres 13 to 17. MIT licence.</p>
    <div class="cluster">
      <a class="btn btn-primary" href="/docs/quickstart">Read the quickstart</a>
      <a class="btn" href="https://github.com/pgshift/pgshift">Source on GitHub</a>
    </div>
  </section>

  <section class="section">
    <h2>A plan, before anything runs</h2>
    <p><code>pgshift plan</code> reads a migration and prints the steps with their lock level.
      Nothing touches the database until <code>pgshift apply</code>.</p>
    <pre class="plan"><code>$ pgshift plan migrations/0042_orders_status.sql
target   orders  41.2M rows  18 GB
step 1   ADD COLUMN status text                   ACCESS EXCLUSIVE   2 ms
step 2   backfill status, batches of 10,000       none               ~14 min
step 3   ADD CONSTRAINT status_nn NOT VALID       ACCESS EXCLUSIVE   3 ms
step 4   VALIDATE CONSTRAINT status_nn            SHARE UPDATE EXCL  reads and writes continue
step 5   CREATE INDEX CONCURRENTLY                none               ~6 min
longest lock: 3 ms</code></pre>
  </section>

  <section class="section">
    <h2>What it does with each change</h2>
    <table>
      <thead><tr><th>Change</th><th>pgshift</th></tr></thead>
      <tbody>
        <tr><td>Add column with default</td><td>Adds it nullable, backfills in batches, then sets the default and NOT NULL.</td></tr>
        <tr><td>Add index</td><td>Uses <code>CONCURRENTLY</code>. Drops and retries once if the build fails.</td></tr>
        <tr><td>Rename column</td><td>Refuses. Prints the expand, migrate, contract steps to do it in three deploys.</td></tr>
        <tr><td>Change column type</td><td>Refuses when Postgres would rewrite the table. Runs in place when it would not.</td></tr>
      </tbody>
    </table>
  </section>

</main>
```

#### Notes

- **The terminal block is real output.** Developers trust a page in proportion to how much of the actual tool it shows. A plan with lock levels and row counts says more than any adjective.
- **Dark mode follows the system.** The base stylesheet switches on `prefers-color-scheme`. Forcing near-black on everyone is a style choice copied from other dev-tool sites, not a reader preference.
- **The refusals are on the front page.** "Refuses to rename a column" is the line that makes the rest credible.
- **Version, date, supported range and licence sit under the install line.** These are the four facts an engineer checks before reading anything else.

### 6.10 Analytics dashboard

The rebuild uses the Tailwind v3 config from 6.2. Its chart follows the single-series rules: one 2px ink line, a recessive grid, no legend, and a table view of the same numbers.

#### The slop version

```slop
<div className="min-h-screen bg-gray-50 p-8">
  <h1 className="text-3xl font-bold">Welcome back, Alex! {emoji:wave}</h1>
  <p className="text-gray-500">Here's what's happening with your business today.</p>
  <div className="mt-8 grid grid-cols-4 gap-6">
    {stats.map((s) => (
      <div className="rounded-2xl bg-white p-6 shadow-sm ring-1 ring-gray-100">
        <span className="rounded-xl bg-indigo-50 p-3 text-indigo-600">{s.icon}</span>
        <span className="rounded-full bg-green-100 px-2 py-0.5 text-xs text-green-700">{s.change}</span>
        <p className="text-sm text-gray-500">{s.label}</p>
        <p className="text-3xl font-bold">{s.value}</p>
      </div>
    ))}
  </div>
  <div className="col-span-2 rounded-2xl bg-white p-6 shadow-sm">
    <h2>Revenue Overview</h2>
    <AreaChart data={data}>
      <defs><linearGradient id="fill"><stop stopColor="#6366f1" stopOpacity={0.4} /><stop stopOpacity={0} /></linearGradient></defs>
      <Area dataKey="revenue" stroke="#6366f1" fill="url(#fill)" />
    </AreaChart>
  </div>
  <div className="rounded-2xl bg-gradient-to-br from-violet-500 to-indigo-600 p-6 text-white shadow-lg">
    <h2>{emoji:sparkles} AI Insights</h2>
    <p>Your revenue is up 20.1%! Consider leveraging this momentum to boost engagement.</p>
    <button className="rounded-full bg-white/20 px-4 py-2 backdrop-blur">Explore insights</button>
  </div>
</div>
// stats: Total Revenue $45,231.89 +20.1% from last month; Subscriptions +2350 +180.1%;
//        Sales +12,234 +19%; Active Now +573 +201 since last hour
```

#### Tells

1. "Welcome back, Alex" with a wave emoji, taking the top 100px of a screen people open to check numbers.
2. Four KPI cards, each `rounded-2xl shadow-sm ring-1`, each with an icon in an `indigo-50` tile.
3. The figures are the shadcn dashboard example's, unchanged: $45,231.89, +20.1%, +2350, +573 "Active Now".
4. Green change pills with no period stated. "From last month" compares a partial month to a full one.
5. Every delta green and upward, including ones where up is bad.
6. Area chart filled with an indigo-to-transparent `linearGradient`, stroked `#6366f1` (Tailwind `indigo-500`).
7. An "AI `Insights`" card on a violet-to-indigo gradient with a glass button, whose content is a restated number plus `leveraging` and `boost engagement`.
8. No date range, no data freshness, no table view of the chart.

#### The rebuild

```tsx
type Kpi = { label: string; now: string; prev: string; delta: string; better: boolean };

const kpis: Kpi[] = [
  { label: "Revenue", now: "$48,210", prev: "$44,980", delta: "+7.2%", better: true },
  { label: "New subscriptions", now: "312", prev: "341", delta: "-8.5%", better: false },
  { label: "Cancellations", now: "41", prev: "39", delta: "+2", better: false },
  { label: "Refunds", now: "$1,140", prev: "$1,620", delta: "-29.6%", better: true },
];

export function Overview({ days }: { days: { date: string; revenue: number }[] }) {
  const max = Math.max(...days.map((d) => d.revenue));
  const pts = days.map((d, i) => `${(i / (days.length - 1)) * 100},${100 - (d.revenue / max) * 90}`).join(" ");

  return (
    <main className="mx-auto max-w-page px-6 py-8">
      <header className="flex flex-wrap items-baseline justify-between gap-4 border-b border-rule pb-4">
        <h1 className="text-2xl font-semibold">Overview</h1>
        <p className="text-sm text-ink-2">
          1 to 14 Oct 2026 against 17 to 30 Sep. Data as of 09:00 UTC. <a href="?range" className="underline">Change</a>
        </p>
      </header>

      <dl className="grid grid-cols-2 border-b border-rule md:grid-cols-4">
        {kpis.map((k) => (
          <div key={k.label} className="border-r border-rule px-4 py-4 last:border-r-0">
            <dt className="text-sm text-ink-2">{k.label}</dt>
            <dd className="mt-1 font-mono text-2xl tabular-nums">{k.now}</dd>
            <dd className="text-sm tabular-nums">
              <span className={k.better ? "text-ok" : "text-bad"}>{k.delta}</span>{" "}
              <span className="text-ink-3">from {k.prev}</span>
            </dd>
          </div>
        ))}
      </dl>

      <p className="border-b border-rule py-3 text-sm">
        New subscriptions fell 8.5 percent. 24 of the 29 missing signups were on the Annual plan,
        after the price change on 3 Oct. <a href="/reports/annual" className="underline">See the Annual plan report</a>
      </p>

      <section className="py-8" aria-labelledby="rev">
        <h2 id="rev" className="text-lg font-semibold">Revenue per day, USD</h2>
        <svg viewBox="0 0 100 100" preserveAspectRatio="none" className="mt-4 h-48 w-full" role="img"
             aria-label={`Daily revenue, ${days[0].date} to ${days[days.length - 1].date}. Table below.`}>
          {[10, 55, 100].map((y) => <line key={y} x1="0" x2="100" y1={y} y2={y} stroke="var(--rule)" strokeWidth="1" vectorEffect="non-scaling-stroke" />)}
          <polyline points={pts} fill="none" stroke="var(--ink)" strokeWidth="2" vectorEffect="non-scaling-stroke" />
        </svg>
        <details className="mt-3 text-sm">
          <summary className="cursor-pointer">Show as table</summary>
          <table className="mt-2">
            <thead><tr><th>Date</th><th className="text-right">Revenue</th></tr></thead>
            <tbody>{days.map((d) => (
              <tr key={d.date}><td>{d.date}</td><td className="text-right tabular-nums">${d.revenue.toLocaleString("en-US")}</td></tr>
            ))}</tbody>
          </table>
        </details>
      </section>
    </main>
  );
}
```

#### Notes

- **The KPI row is one strip, divided by 1px rules.** Four cards with four icons repeat the same frame four times. A `dl` strip reads as one row of figures and takes 40 percent less height.
- **Each delta names its period and its baseline.** "+7.2% from $44,980" can be checked. The color follows whether the change is good, so a rise in cancellations is red.
- **The AI card becomes one sentence with numbers and a link.** If a model or an analyst found the cause, state the cause. If nobody did, show nothing.
- **One series, one ink line, no fill.** A single series needs no legend; the heading names it. The table under `details` is the accessible view and the export for anyone who wants the figures.
- **Freshness is in the header.** "Data as of 09:00 UTC" answers the first question anyone asks about a dashboard number.

### 6.11 Personal portfolio

#### The slop version

```slop
<section class="flex min-h-screen flex-col items-center justify-center text-center">
  <img src="/avatar.png" class="h-32 w-32 rounded-full shadow-2xl ring-4 ring-purple-500 ring-offset-4" />
  <h1 class="text-6xl font-bold">Hi, I'm
    <span class="bg-gradient-to-r from-purple-400 to-pink-600 bg-clip-text text-transparent">Alex</span> {emoji:wave}</h1>
  <p class="typewriter text-2xl text-gray-400">Full-Stack Developer | UI/UX Enthusiast | Lifelong Learner</p>
  <p class="max-w-xl text-gray-500">A passionate developer crafting beautiful, user-centric digital experiences
    that make an impact. I love turning complex problems into elegant solutions.</p>
  <a class="rounded-full bg-purple-600 px-6 py-3 shadow-lg shadow-purple-500/50">View My Work</a>
  <div class="absolute bottom-10 animate-bounce">{emoji:down arrow}</div>
</section>
<section id="skills"><h2>My Skills {emoji:tools}</h2>
  <p>React</p><div class="h-2 rounded-full bg-gray-200"><div class="h-2 w-[95%] rounded-full bg-gradient-to-r from-purple-500 to-pink-500"></div></div>
  <!-- TypeScript 90%, Node.js 85%, Figma 80% -->
</section>
<section id="projects" class="grid grid-cols-3 gap-6">
  <div class="rounded-2xl bg-white/5 p-6 backdrop-blur transition duration-500 hover:scale-105">
    <img src="/project1.png" class="rounded-xl" /><h3>E-Commerce Platform</h3>
    <p>A full-stack e-commerce solution built with cutting-edge technologies.</p>
    <span class="rounded-full bg-purple-500/20 px-3 py-1 text-xs">React</span> <span ...>Node</span> <span ...>MongoDB</span>
  </div>
</section>
```

#### Tells

1. Full-viewport centered hero holding a name and nothing else, with a bouncing arrow to say "scroll".
2. Avatar with a purple ring, ring offset and `shadow-2xl`.
3. First name in a purple-to-pink gradient, followed by a wave emoji.
4. Typewriter effect cycling three titles separated by pipes, one of them "Lifelong Learner".
5. Bio of `passionate`, `crafting`, `beautiful`, `user-centric`, `elegant`, `solution`, with no employer, city or result.
6. Skill bars with percentages. 95 percent of React is not a measurable quantity.
7. Project cards that scale to 105 percent over 500ms, a glass background, and generic titles ("E-Commerce Platform").
8. Stack shown as pill tags in place of what the project achieved.

#### The rebuild

```html
<style>
  .intro { padding-block: var(--s8) var(--s7); }
  .intro > * + * { margin-top: var(--s4); }
  .work { list-style: none; padding: 0; max-width: none; }
  .work > li { display: grid; gap: var(--s2) var(--s7); padding-block: var(--s6); border-top: 1px solid var(--rule); }
  @media (min-width: 880px) { .work > li { grid-template-columns: 1fr 1fr; } }
  .work img { border: 1px solid var(--rule); }
</style>

<main class="wrap">
  <header class="intro">
    <h1>Alex Moreau</h1>
    <p class="lede">Front-end engineer in Lyon. I build the forms, tables and editors inside business
      software. Now at Fieldnote, a route planner for delivery fleets. Before that, four years at Qonto.</p>
    <p class="cluster">
      <a href="mailto:alex@moreau.dev">alex@moreau.dev</a>
      <a href="/cv.pdf">CV, one page (PDF)</a>
      <a href="https://github.com/amoreau">GitHub</a>
    </p>
  </header>

  <section>
    <h2>Selected work</h2>
    <ol class="work">
      <li>
        <div class="stack">
          <h3><a href="/work/route-editor">Route editor, Fieldnote</a></h3>
          <p class="small faint">2025 to now. Lead engineer on a team of 3.</p>
          <p>Replaced a 40-column spreadsheet import with an editor dispatchers use directly.
            Planning a 60-stop day went from about 50 minutes to 12, measured over six weeks with 14 dispatchers.</p>
        </div>
        <img src="/img/route-editor.png" width="1200" height="800"
             alt="Route editor: a list of 60 stops on the left, a map with three colored routes on the right.">
      </li>
    </ol>
  </section>

  <section class="section">
    <h2>Tools</h2>
    <p>TypeScript, React, Postgres and Playwright every day. CSS by hand. Every form I ship works with a keyboard alone.</p>
  </section>
</main>
```

#### Notes

- **Name, job, city, employer, in the first two lines.** A recruiter decides in the time it takes to read them.
- **Projects carry a role, a date range, and one measured result.** "Planning time from 50 to 12 minutes" is the whole case. The stack goes in the case study, not on the card.
- **No skill bars.** A list of tools used daily is honest. A percentage of a framework is not.
- **Contact is a visible email address, not a form.** It works with every mail client and needs no backend.

### 6.12 Documentation home

#### The slop version

```slop
<div class="bg-gradient-to-b from-indigo-50 to-white py-20 text-center">
  <h1 class="text-5xl font-bold">Welcome to the Relay Docs {emoji:books}</h1>
  <p>Everything you need to build amazing things with Relay. Let's dive in!</p>
  <div class="relative mx-auto mt-8 max-w-xl rounded-2xl shadow-xl">
    <input placeholder="Search documentation..." class="w-full rounded-2xl px-6 py-4" /><kbd>{emoji:command}K</kbd>
  </div>
</div>
<div class="mx-auto grid max-w-6xl grid-cols-3 gap-6">
  <a class="rounded-2xl border p-6 shadow-sm transition hover:border-indigo-500 hover:shadow-lg">
    <div class="rounded-xl bg-indigo-100 p-3">{emoji:rocket}</div>
    <h3>Getting Started</h3><p>Learn the basics and get up and running in minutes.</p></a>
  <!-- {emoji:book} Guides: "Deep dive into core concepts"
       {emoji:gear} API Reference: "Comprehensive reference for every endpoint"
       {emoji:plug} Integrations: "Seamlessly connect your favorite tools"
       {emoji:bulb} Examples: "Get inspired by what others have built"
       {emoji:speech} Community: "Join our vibrant community" -->
</div>
```

#### Tells

1. "Welcome to the docs" heading with a books emoji and "`Let's dive` in" under it.
2. Gradient band from `indigo-50` behind the search.
3. Search box with `rounded-2xl shadow-xl` floating mid-page.
4. Six category cards with emoji tiles, all the same size, so the quickstart has the same weight as "Community".
5. Card descriptions that restate the card title: "API Reference: `Comprehensive` reference".
6. No version, no install command, no last-updated date, no link to the changelog.

#### The rebuild

```html
<style>
  .docs { display: grid; gap: var(--s7); padding-block: var(--s7); }
  @media (min-width: 960px) { .docs { grid-template-columns: 220px 1fr; } }
  .side { font-size: var(--t-14); }
  .side ul { list-style: none; padding: 0; }
  .start { counter-reset: step; list-style: none; padding: 0; }
  .start li { padding-block: var(--s3); border-top: 1px solid var(--rule); }
  .groups { display: grid; gap: var(--s6); grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); max-width: none; }
  .groups ul { list-style: none; padding: 0; font-size: var(--t-14); }
</style>

<div class="wrap docs">
  <nav class="side" aria-label="Documentation">
    <label for="ver">Version</label>
    <select id="ver"><option>3.4 (current)</option><option>3.3</option><option>2.x (end of life)</option></select>
    <form role="search" class="field">
      <label for="q">Search</label>
      <input id="q" type="search" placeholder="Event name, error code, endpoint">
      <p class="hint">Press <kbd>/</kbd> to focus.</p>
    </form>
  </nav>

  <main class="stack" style="--stack: var(--s6)">
    <header class="stack">
      <h1>Relay documentation</h1>
      <p class="lede">Relay delivers webhooks for you: it signs them, retries failures for 72 hours,
        and keeps a searchable log of every attempt.</p>
      <p class="small muted">Version 3.4. Updated 9 October 2026. <a href="/changelog">Changelog</a></p>
    </header>

    <section>
      <h2>Start here</h2>
      <ol class="start">
        <li><a href="/docs/quickstart">Send your first webhook</a> <span class="muted">10 minutes. Node, Python or curl.</span></li>
        <li><a href="/docs/verify">Verify signatures on the receiving end</a> <span class="muted">5 minutes.</span></li>
        <li><a href="/docs/retries">Choose a retry policy</a> <span class="muted">Defaults and when to change them.</span></li>
      </ol>
      <pre><code>npm install @relay/node</code></pre>
    </section>

    <section class="groups">
      <div><h3>Guides</h3><ul>
        <li><a href="/docs/guides/fan-out">Fan out one event to many endpoints</a></li>
        <li><a href="/docs/guides/replay">Replay failed deliveries</a></li>
        <li><a href="/docs/guides/rotate">Rotate signing secrets without downtime</a></li></ul></div>
      <div><h3>Reference</h3><ul>
        <li><a href="/docs/api">HTTP API</a></li><li><a href="/docs/cli">CLI</a></li>
        <li><a href="/docs/errors">Error codes</a></li><li><a href="/docs/limits">Rate limits and quotas</a></li></ul></div>
    </section>
  </main>
</div>
```

#### Notes

- **The first paragraph says what the product does in one sentence**, because a large share of docs visitors arrive from search and have never seen the marketing site.
- **"Start here" is an ordered list with time estimates.** It has an order, so it is an `ol`, and the times let a reader pick a task that fits the next ten minutes.
- **The other links are task titles, grouped under three plain headings.** "Rotate signing secrets without downtime" is something a reader searches for. "Guides" with a book emoji is not.
- **Version and update date sit under the title.** Stale docs are the most common support complaint; showing the date admits it up front.
