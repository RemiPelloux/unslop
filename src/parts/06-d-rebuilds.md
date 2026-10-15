### 6.13 Blog article page

#### The slop version

```slop
<div class="relative h-96">
  <img src="/hero-abstract-3d-shapes.png" class="h-full w-full object-cover" />
  <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>
  <span class="rounded-full bg-purple-600 px-3 py-1 text-xs">{emoji:fire} Trending</span>
  <h1 class="text-5xl font-bold text-white">Unlocking the Power of Edge Caching: A Comprehensive Guide {emoji:rocket}</h1>
  <p class="text-white/70">{emoji:calendar} Oct 3, 2026 . {emoji:clock} 8 min read</p>
</div>
<article class="prose prose-lg prose-indigo mx-auto">
  <div class="rounded-2xl border-l-4 border-indigo-500 bg-indigo-50 p-6">
    <strong>{emoji:pin} TL;DR:</strong> Edge caching is a game-changer for performance.</div>
  <p>In today's fast-paced digital landscape, performance is more than just a nice-to-have. It's crucial.
    In this article, we'll delve into the intricacies of edge caching.</p>
  <h2>{emoji:brain} Why Edge Caching Matters</h2> ...
  <h2>{emoji:key} Key Takeaways</h2>
  <ul><li>{emoji:check} Caching is essential</li><li>{emoji:check} Measure everything</li></ul>
  <p>In conclusion, edge caching is a powerful tool in your arsenal. Happy coding! {emoji:rocket}</p>
</article>
<div class="mx-auto flex max-w-sm gap-4 rounded-2xl p-6 shadow-lg">
  <img class="rounded-full" /><p>Alex Chen. Passionate about web performance and coffee {emoji:coffee}</p></div>
```

#### Tells

1. Abstract 3D stock render as the hero, darkened with a black-to-transparent gradient so white text stays legible.
2. "Trending" pill with a fire emoji on a post with no traffic data behind it.
3. Title in the "`Unlocking` `the Power of` X: A `Comprehensive` Guide" pattern.
4. Read-time estimate with clock emoji, the default output of most blog starters.
5. A TL;DR box in `indigo-50` that says nothing the title did not.
6. Opening paragraph built from `in today's`, `fast-paced`, `landscape`, `more than just`, `crucial`, `delve`, `intricacies`.
7. Emoji on every `h2`, and a "Key `Takeaways`" list of check marks.
8. Close with `in conclusion`, `arsenal` and `happy coding`.
9. Author card with a shadow, "passionate about X and coffee".
10. `prose-indigo` from the Tailwind Typography plugin, so links and bullets are indigo.

#### The rebuild

```html
<style>
  .post { padding-block: var(--s8); }
  .post header > * + * { margin-top: var(--s3); }
  .post .body { font-family: var(--font-serif); font-size: var(--t-18); line-height: 1.6; margin-top: var(--s7); }
  .post .body pre { font-size: var(--t-14); }
  .notes { margin-top: var(--s7); padding-top: var(--s4); border-top: 1px solid var(--rule); }
</style>

<article class="wrap post">
  <header>
    <p class="small"><a href="/writing">Writing</a></p>
    <h1>Cache keys that survive a deploy</h1>
    <p class="lede">We cut origin requests by 61 percent by taking the build hash out of three cache keys.
      This is what we changed, and the one case where it broke.</p>
    <p class="small muted">Ines Duarte, platform team. 3 October 2026.</p>
  </header>

  <div class="body prose">
    <p>Every deploy changed our build hash, and the hash was part of the cache key for HTML, the
      product JSON and the image manifest. A deploy at 14:00 emptied the edge cache for all three.
      For the next 20 minutes, origin served 9 times its normal request rate.</p>
    <h2>What we changed</h2>
    <p>We keyed the JSON and the manifest on content instead of on the build:</p>
    <pre><code>cache_key = sha256(path + response_body)[:16]   # was: path + BUILD_ID</code></pre>
    <p>HTML kept the build hash, because it references the new script bundle.<sup><a href="#n1" id="r1">1</a></sup></p>
    <h2>Where it broke</h2>
    <p>Two pages read a feature flag at render time. Their body did not change when the flag did,
      so the edge served the old version for up to an hour. We added the flag state to the key for those two routes.</p>
  </div>

  <footer class="notes small">
    <ol>
      <li id="n1">Scripts are named by content hash, so old HTML still finds its bundle. <a href="#r1">Back</a></li>
    </ol>
  </footer>
</article>
```

#### Notes

- **The summary is the first paragraph, and it contains the result.** 61 percent, three keys, one failure. A separate TL;DR box only exists when the opening fails to do this.
- **Serif at 18px and 1.6 line height for the body, sans for the interface around it.** Long reading benefits from the larger size; 66ch still holds.
- **No hero image.** An abstract render tells the reader nothing about cache keys. A diagram of the request path would earn its place; stock art does not.
- **The failure case gets its own heading.** It is the most useful section for a reader about to try the same change, and the most credible part of the post.

### 6.14 Pricing page

Part 5.5 covers the pricing table as a component. This chapter is the page around it: the toggle, the plan copy, and the billing questions.

#### The slop version

```slop
<h2 class="text-center text-4xl font-bold">Simple, transparent pricing {emoji:money}</h2>
<p class="text-center">Choose the perfect plan for your needs. No hidden fees!</p>
<div class="inline-flex rounded-full bg-gray-100 p-1">
  <button class="rounded-full bg-white shadow">Monthly</button>
  <button>Yearly <span class="rounded-full bg-green-100 px-2 text-xs text-green-700">Save 20%</span></button>
</div>
<div class="grid grid-cols-3 items-center gap-8">
  <div class="rounded-2xl border p-8 shadow-sm"><h3>Starter</h3><p class="text-5xl font-bold">$19<span>/mo</span></p>
    <ul><li>{emoji:check} Up to 5 projects</li><li>{emoji:check} Basic analytics</li><li>{emoji:check} Email support</li></ul>
    <button class="rounded-full border">Get Started</button></div>
  <div class="relative scale-105 rounded-2xl bg-gradient-to-b from-indigo-500 to-purple-600 p-[2px] shadow-2xl">
    <span class="absolute -top-4 rounded-full bg-gradient-to-r from-pink-500 to-orange-400 px-4 text-xs">{emoji:star} Most Popular</span>
    <div class="rounded-2xl bg-white p-8"><h3>Pro</h3><p class="text-5xl font-bold">$49<span>/mo</span></p>
      <ul><li>{emoji:check} Unlimited projects</li><li>{emoji:check} Advanced analytics</li>
          <li>{emoji:check} Priority support</li><li>{emoji:check} AI-powered insights</li></ul>
      <button class="w-full rounded-full bg-indigo-600 text-white shadow-lg">Start Free Trial</button></div></div>
  <div class="rounded-2xl border p-8 shadow-sm"><h3>Enterprise</h3><p class="text-5xl font-bold">Custom</p>
    <ul><li>{emoji:check} Everything in Pro</li><li>{emoji:check} Dedicated success manager</li>
        <li>{emoji:check} Enterprise-grade security</li></ul><button>Contact Sales</button></div>
</div>
<details><summary>Can I cancel anytime?</summary>Absolutely! Cancel anytime, no questions asked. {emoji:smile}</details>
```

#### Tells

1. "Simple, transparent pricing" with a money emoji: the heading on most SaaS template pricing pages.
2. A pill toggle with a green "Save 20%" capsule, while the yearly price never shows the yearly total.
3. The middle plan scaled to 105 percent inside a 2px indigo-to-purple gradient border with `shadow-2xl`.
4. A "Most Popular" badge in a second gradient, pink to orange, with a star emoji. Nobody states who it is popular with.
5. Feature lines that cannot be compared: "Basic analytics" against "Advanced analytics", "Email support" against "Priority support".
6. `AI-powered` `insights` as a Pro line item, with no description.
7. Enterprise priced "Custom" and listing `enterprise-grade` security, so the security on the other plans is something less.
8. Three button labels for one kind of action.
9. An FAQ answer of "Absolutely" plus an exclamation mark and an emoji.

#### The rebuild

```html
<style>
  .plans th[scope="col"] { vertical-align: bottom; }
  .plans .price { font-family: var(--font-mono); font-size: var(--t-24); font-weight: 500; }
  .plans td:not(:first-child), .plans th[scope="col"] { width: 22%; }
  .billing { display: grid; gap: var(--s5); margin-top: var(--s5); }
</style>

<main class="wrap stack" style="--stack: var(--s7); padding-block: var(--s8)">
  <header class="stack">
    <h1>Pricing</h1>
    <p class="lede">Prices in USD, per workspace, before tax. Pay monthly, or yearly for two months free.</p>
  </header>

  <table class="plans">
    <thead>
      <tr><th></th><th scope="col">Free</th><th scope="col">Team</th><th scope="col">Business</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">Monthly</th><td class="price">$0</td><td class="price">$40</td><td class="price">$120</td></tr>
      <tr><th scope="row">Yearly</th><td>$0</td><td>$400 ($33.33 a month)</td><td>$1,200 ($100 a month)</td></tr>
      <tr><th scope="row">Members</th><td>3</td><td>15</td><td>Unlimited</td></tr>
      <tr><th scope="row">Projects</th><td>5</td><td>Unlimited</td><td>Unlimited</td></tr>
      <tr><th scope="row">History kept</th><td>30 days</td><td>1 year</td><td>Forever, plus export</td></tr>
      <tr><th scope="row">SAML single sign-on</th><td>No</td><td>No</td><td>Yes</td></tr>
      <tr><th scope="row">Support reply, working days</th><td>Forum</td><td>Within 1 day</td><td>Within 4 hours</td></tr>
      <tr><th scope="row"></th>
        <td><a class="btn" href="/signup">Create workspace</a></td>
        <td><a class="btn btn-primary" href="/signup?plan=team">Create workspace</a></td>
        <td><a class="btn" href="/signup?plan=business">Create workspace</a></td></tr>
    </tbody>
  </table>

  <section>
    <h2>Billing questions</h2>
    <dl class="billing">
      <div><dt>What happens when we reach a limit?</dt>
        <dd>Nothing breaks. We email the workspace owners, and new members or projects wait until you upgrade or remove some.</dd></div>
      <div><dt>Can we cancel?</dt>
        <dd>Yes, from Settings, Billing. Monthly plans stop at the end of the month. Yearly plans are refunded for the unused whole months.</dd></div>
    </dl>
  </section>
</main>
```

#### Notes

- **A table, because pricing is a comparison.** Rows hold the same attribute across plans, so a reader moves one eye line to compare. Three cards force them to hold numbers in memory.
- **Every row is a quantity or a yes or no.** "Within 4 hours, working days" replaces "Priority support". "History kept" replaces "Advanced analytics".
- **Yearly shows the total and the arithmetic.** "Two months free" plus $400 against $40 a month is checkable in one glance. "Save 20%" was not even right; 2 of 12 months is 16.7 percent.
- **The recommended plan gets the accent button, nothing else.** No scale, no badge, no border. One accent per page holds here too.

### 6.15 Mobile app marketing page

The app shows tide times for coastal ports and works without signal.

#### The slop version

```slop
<section class="relative overflow-hidden bg-gradient-to-br from-sky-400 via-blue-500 to-indigo-600 py-24 text-white">
  <div class="absolute -right-40 top-0 h-[500px] w-[500px] rounded-full bg-cyan-300/40 blur-3xl"></div>
  <h1 class="text-6xl font-extrabold">Ride the wave {emoji:wave}</h1>
  <p class="text-xl text-white/80">Your all-in-one ocean companion. Effortlessly plan every adventure with stunning,
    real-time tide insights at your fingertips.</p>
  <div class="flex gap-4"><img src="/app-store.svg" class="h-14 shadow-xl" /><img src="/google-play.svg" class="h-14 shadow-xl" /></div>
  <p>{emoji:star}{emoji:star}{emoji:star}{emoji:star}{emoji:star} 4.9 . Loved by 50,000+ adventurers</p>
  <img src="/iphone-mockup-3d.png" class="absolute right-10 top-20 w-80 rotate-12 drop-shadow-2xl animate-float" />
</section>
<section class="grid grid-cols-3 gap-8 text-center">
  <div><div class="mx-auto h-16 w-16 rounded-2xl bg-gradient-to-br from-cyan-400 to-blue-600">{emoji:ocean}</div>
    <h3>Real-Time Data</h3><p>Stay ahead with live updates.</p></div>
  <!-- {emoji:map} Smart Maps, {emoji:bell} Instant Alerts -->
</section>
<a class="fixed bottom-6 right-6 rounded-full bg-blue-600 px-6 py-4 text-white shadow-2xl animate-bounce">Download Now!</a>
```

#### Tells

1. Sky-to-indigo gradient background with a cyan blur blob: the blue-violet band the hard rules ban.
2. Pun headline with a wave emoji.
3. `all-in-one`, `effortlessly`, `stunning`, `insights`, "at your fingertips", and "real-time" for predictions computed years ahead.
4. Store badges with `shadow-xl`, which both store brand guidelines prohibit altering.
5. A five-star emoji row, a 4.9 with no store or date, and "50,000+ adventurers".
6. A 3D phone mockup rotated 12 degrees, floating on a loop, with `drop-shadow-2xl`.
7. Three features with gradient icon tiles and two-word headings.
8. A fixed "Download Now" button that bounces forever.

#### The rebuild

```html
<style>
  .app-hero { padding-block: var(--s8) var(--s7); }
  .app-hero > * + * { margin-top: var(--s4); }
  .badges img { height: 40px; width: auto; }
  .shots { display: grid; gap: var(--s5); grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); max-width: none; list-style: none; padding: 0; }
  .shots img { border: 1px solid var(--rule); }
  .shots p { margin-top: var(--s2); }
</style>

<main class="wrap">
  <section class="app-hero">
    <h1>Tideline</h1>
    <p class="lede">Tide times and heights for 690 ports in Britain and Ireland. The whole year downloads
      on first launch, so it works at sea, with no signal.</p>
    <p class="cluster badges">
      <a href="https://apps.apple.com/app/id0000000000"><img src="/img/app-store.svg" alt="Download on the App Store"></a>
      <a href="https://play.google.com/store/apps/details?id=com.example.tideline"><img src="/img/google-play.png" alt="Get it on Google Play"></a>
    </p>
    <p class="small muted">Free for one port. All ports: $4.99 once. iOS 16 or later, Android 10 or later. 22 MB.</p>
  </section>

  <section class="section">
    <h2>Screens</h2>
    <ul class="shots">
      <li><img src="/img/today.png" width="390" height="844" alt="Today screen for Padstow: high water 06:12, 5.9 m; low 12:31, 1.1 m.">
        <p class="small">Today: next high and low water, and the height now.</p></li>
      <li><img src="/img/week.png" width="390" height="844" alt="Seven-day tide curve with spring tides marked.">
        <p class="small">Seven days at a glance, with spring and neap tides marked.</p></li>
    </ul>
  </section>

  <section class="section prose">
    <h2>Where the numbers come from</h2>
    <p>Predictions are licensed from the UK and Irish hydrographic offices and updated each January.
      They do not include surge from weather; on stormy days the sea can run 0.5 m higher or lower.</p>
    <h2>Privacy</h2>
    <p>No account and no tracking. Location is used once, on your phone, to suggest the nearest port.</p>
  </section>
</main>
```

#### Notes

- **Official store badges, unaltered, at 40px high.** Apple and Google publish the artwork and the rules; adding a shadow or a glow violates both.
- **Screenshots at device aspect ratio, flat, with a caption each.** The rotated 3D mockup hides the interface the visitor came to judge.
- **The limits are on the page.** "Does not include surge" is the sentence a sailor needs, and leaving it out would be a safety problem, not a marketing choice.
- **Price, platform versions and download size in one muted line.** These decide whether someone can install the app at all.

### 6.16 Admin settings area

The rebuild uses the Button and Input components from 6.4.

#### The slop version

```slop
<div className="space-y-8 p-8">
  <h1 className="text-3xl font-bold">Settings {emoji:gear}</h1>
  <div className="rounded-2xl bg-white p-8 shadow-lg">
    <h2 className="text-xl font-semibold">{emoji:bust} Profile</h2>
    <Input placeholder="Enter your workspace name" className="rounded-xl shadow-sm" />
    <div className="flex justify-between"><span>Enable AI Assistant {emoji:sparkles}</span>
      <Switch className="data-[state=checked]:bg-gradient-to-r data-[state=checked]:from-indigo-500 data-[state=checked]:to-purple-500" /></div>
    <div className="flex justify-between"><span>Email notifications</span><Switch /></div>
  </div>
  <div className="rounded-2xl border-2 border-red-500 bg-red-50 p-8 shadow-[0_0_30px_rgba(239,68,68,0.3)]">
    <h2 className="text-red-600">{emoji:warning} Danger Zone</h2>
    <p>These actions are irreversible. Please proceed with caution!</p>
    <Button variant="destructive" onClick={() => confirm("Are you sure?") && deleteWorkspace()}>Delete Workspace</Button>
  </div>
  <Button className="fixed bottom-8 right-8 rounded-full bg-gradient-to-r from-indigo-600 to-purple-600 shadow-2xl">
    Save Changes {emoji:sparkles}</Button>
</div>
// onSave: toast.success("Settings saved successfully! {emoji:party}")
```

#### Tells

1. Emoji on the page title and on each group heading.
2. Every group in a `rounded-2xl shadow-lg` card, so the page is a stack of floating boxes.
3. A placeholder used as the label. It disappears on the first keystroke and fails WCAG 3.3.2.
4. Switches inside a form that also has a Save button, so nobody knows whether a toggle took effect.
5. A switch filled with an indigo-to-purple gradient when on.
6. "Danger Zone" in a red box with a red glow, `irreversible` and "proceed with caution" with an exclamation mark.
7. `window.confirm("Are you sure?")`, which names neither the object nor the consequence.
8. A floating gradient Save button that saves every section at once.
9. A success toast that says "successfully" with a party emoji.

#### The rebuild

```tsx
import { useState } from "react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { renameWorkspace, setDigest, deleteWorkspace } from "@/lib/api";

const nav = [["general", "General"], ["email", "Email"], ["delete", "Delete workspace"]];

export function WorkspaceSettings({ ws }: { ws: { name: string; slug: string; digest: boolean; counts: string } }) {
  const [name, setName] = useState(ws.name);
  const [typed, setTyped] = useState("");
  const dirty = name.trim() !== ws.name;

  return (
    <div className="mx-auto grid max-w-page gap-12 px-6 py-8 md:grid-cols-[192px_1fr]">
      <nav aria-label="Settings" className="text-sm">
        <ul>{nav.map(([id, label]) => (
          <li key={id}><a href={`#${id}`} className="block py-1 text-ink-2 hover:text-ink">{label}</a></li>
        ))}</ul>
      </nav>

      <main>
        <h1 className="text-2xl font-semibold">Workspace settings</h1>

        <section id="general" className="mt-8 border-t border-rule pt-6">
          <h2 className="text-lg font-semibold">General</h2>
          <form className="mt-4 max-w-measure"
                onSubmit={async (e) => { e.preventDefault(); await renameWorkspace(name); toast(`Workspace renamed to ${name}.`); }}>
            <label htmlFor="ws-name" className="text-sm font-medium">Workspace name</label>
            <Input id="ws-name" value={name} onChange={(e) => setName(e.target.value)} aria-describedby="ws-name-hint" />
            <p id="ws-name-hint" className="mt-1 text-sm text-ink-2">Shown in emails and on invoices. 2 to 60 characters.</p>
            <div className="mt-4 flex items-center gap-3">
              <Button type="submit" variant="primary" disabled={!dirty}>Save name</Button>
              {dirty && <span className="text-sm text-ink-2">Not saved yet</span>}
            </div>
          </form>
        </section>

        <section id="email" className="mt-12 border-t border-rule pt-6">
          <h2 className="text-lg font-semibold">Email</h2>
          <label className="mt-4 flex items-start gap-3 font-normal">
            <input type="checkbox" defaultChecked={ws.digest} className="mt-1"
                   onChange={async (e) => { await setDigest(e.target.checked); toast(e.target.checked ? "Weekly digest on." : "Weekly digest off."); }} />
            <span>Send a weekly digest on Monday at 08:00<br /><span className="text-sm text-ink-2">Saves as soon as you change it.</span></span>
          </label>
        </section>

        <section id="delete" className="mt-12 border-t border-bad pt-6">
          <h2 className="text-lg font-semibold">Delete workspace</h2>
          <p className="mt-2 max-w-measure text-sm">
            Deletes {ws.counts}. We keep a backup for 30 days, then it is gone for good.
          </p>
          <label htmlFor="confirm" className="mt-4 text-sm font-medium">Type <code>{ws.slug}</code> to confirm</label>
          <Input id="confirm" value={typed} onChange={(e) => setTyped(e.target.value)} autoComplete="off" className="max-w-xs" />
          <Button variant="danger" className="mt-3" disabled={typed !== ws.slug} onClick={() => deleteWorkspace(ws.slug)}>
            Delete {ws.name}
          </Button>
        </section>
      </main>
    </div>
  );
}
```

#### Notes

- **Sections are separated by a top rule and 48px, not by cards.** The page is one document with three headings; the left nav jumps between them.
- **Each section saves on its own.** A text field gets an explicit "Save name" button and a "Not saved yet" note. The checkbox saves on change and says so under its label. One rule per control, stated in the interface.
- **A checkbox, not a switch, for the digest.** Switches suggest a device turning on. A checkbox reads as a preference, and it carries its label as one clickable unit.
- **The delete section names the cost.** `ws.counts` renders "14 projects, 212 invoices and the files of 9 members". Typing the slug proves intent better than an "Are you sure" prompt, and the button label repeats the workspace name.

### 6.17 AI product landing page

The worst offender. Nearly every pattern in this handbook shows up on one page. The product reads contract drafts and flags clauses that differ from a legal team's own playbook.

#### The slop version

```slop
<body class="bg-black text-white">
<div class="pointer-events-none fixed inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(124,58,237,0.35),transparent_60%)]"></div>
<nav class="fixed top-4 left-1/2 -translate-x-1/2 rounded-full border border-white/10 bg-white/5 px-6 py-3 backdrop-blur-2xl"> ... </nav>
<section class="py-40 text-center">
  <span class="inline-flex items-center gap-2 rounded-full border border-green-500/30 bg-green-500/10 px-3 py-1 text-xs text-green-400">
    <span class="relative flex h-2 w-2"><span class="absolute h-full w-full animate-ping rounded-full bg-green-400"></span>
    <span class="h-2 w-2 rounded-full bg-green-500"></span></span> LIVE . Nova 2.0 now in public beta</span>
  <h1 class="text-7xl font-semibold tracking-tighter">{emoji:sparkles} Introducing <span class="bg-gradient-to-r from-blue-400 via-violet-500 to-fuchsia-500 bg-clip-text text-transparent">Nova AI</span></h1>
  <p class="text-xl text-white/60">Your AI-powered legal copilot. Harness the power of next-gen AI to supercharge contract
    review, unlock hidden insights, and transform the way your team works. The future of legal is here.</p>
  <div class="mx-auto h-64 w-64 animate-spin-slow rounded-full bg-gradient-to-tr from-violet-600 via-blue-500 to-cyan-400 blur-2xl"></div>
  <button class="rounded-full bg-gradient-to-r from-violet-600 to-indigo-600 px-8 py-4 shadow-[0_0_40px_rgba(124,58,237,0.6)]">Join the Waitlist {emoji:rocket}</button>
  <div class="rounded-2xl border border-white/10 bg-white/5 p-6 text-left backdrop-blur-xl">
    <p class="text-white/50">You: Review this NDA</p>
    <p>Nova: <span class="typing-dots">...</span> {emoji:sparkles} I've analyzed your document and found 3 key insights!</p>
  </div>
</section>
<section class="grid grid-cols-3 gap-4"> <!-- glass bento: {emoji:brain} Smart Analysis, {emoji:lightning} 10x Faster,
  {emoji:lock} Enterprise-Grade Security, {emoji:globe} 100+ Languages, {emoji:robot} Autonomous Agents --> </section>
<p class="text-center text-white/40">Trusted by 10,000+ forward-thinking teams</p>
<blockquote class="rounded-2xl bg-white/5 p-8 backdrop-blur">"Nova is a total game-changer for our team!" . Sarah J., Legal Lead</blockquote>
```

#### Tells

1. Fixed violet radial glow over a black page, plus a floating pill-shaped glass nav with `backdrop-blur-2xl`.
2. A "LIVE" pill with an `animate-ping` green dot, attached to a beta announcement.
3. "Introducing" with sparkles, and the product name in a blue-violet-fuchsia gradient.
4. The subhead: `ai-powered`, copilot, `harness` `the power of`, `next-gen`, `supercharge`, `unlock`, `insights`, `transform`, `the future of`.
5. A spinning gradient orb with `blur-2xl` as the hero visual. It shows nothing about contracts.
6. A glowing gradient pill button that leads to a waitlist, so the visitor cannot try anything.
7. A fake chat with typing dots that ends in "3 key `insights`" and never shows one.
8. A glass bento grid of claims with no numbers behind them: "10x Faster", "100+ Languages", "Autonomous Agents".
9. "Trusted by 10,000+ `forward-thinking` teams" on a product in beta.
10. A `game-changer` quote from "Sarah J." with no company.
11. No mention of accuracy, failure cases, data handling, or price: the four things a legal buyer must know.

#### The rebuild

```html
<style>
  .hero { padding-block: var(--s8) var(--s7); }
  .hero > * + * { margin-top: var(--s4); }
  .example { display: grid; gap: var(--s5); max-width: none; }
  @media (min-width: 880px) { .example { grid-template-columns: 1fr 1fr; } }
  .flag { border-left: 2px solid var(--accent); padding-left: var(--s4); }
</style>

<main class="wrap">
  <section class="hero">
    <h1>Redline</h1>
    <p class="lede">Redline reads an NDA or a services agreement and marks every clause that differs
      from your team's playbook, with the playbook text next to it. A lawyer still decides what to change.</p>
    <div class="cluster">
      <a class="btn btn-primary" href="/try">Check a contract (no account needed)</a>
      <a class="btn" href="/report-2026-09.pdf">Accuracy report, September 2026 (PDF)</a>
    </div>
    <p class="small muted">$9 per document up to 40 pages. Volume pricing from 200 documents a month.</p>
  </section>

  <section class="section">
    <h2>One clause, as Redline shows it</h2>
    <div class="example">
      <div class="panel-sunk">
        <p class="small faint">Draft, clause 7.2</p>
        <p class="serif">The Receiving Party's liability under this Agreement shall not exceed the fees paid in the twelve (12) months preceding the claim.</p>
      </div>
      <div class="flag">
        <p><strong>Differs from playbook rule L-3</strong></p>
        <p>Your playbook excludes confidentiality breaches from any liability cap. This clause caps all liability, including breaches of clause 4.</p>
        <p class="small muted">Suggested wording from your playbook is in the document view.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <h2>How often it is right</h2>
    <table>
      <thead><tr><th>Clause type</th><th class="num">Deviations in test set</th><th class="num">Found</th><th class="num">Missed</th></tr></thead>
      <tbody>
        <tr><td>Liability cap</td><td class="num">212</td><td class="num">203</td><td class="num">9</td></tr>
        <tr><td>Governing law</td><td class="num">148</td><td class="num">148</td><td class="num">0</td></tr>
        <tr><td>Indemnity</td><td class="num">171</td><td class="num">157</td><td class="num">14</td></tr>
      </tbody>
    </table>
    <p class="small muted">400 contracts reviewed by two lawyers, then by Redline, September 2026. 61 false flags in total.
      Method and full results in the accuracy report.</p>
  </section>

  <section class="section prose">
    <h2>Your documents</h2>
    <p>Stored in Frankfurt, deleted 30 days after upload, or at once on request. Redline sends text to a
      third-party language model under a contract that forbids training on it. The subprocessor list is
      at <a href="/subprocessors">/subprocessors</a>.</p>
  </section>
</main>
```

#### Notes

- **The model is not the subject.** The page describes what happens to a contract. "AI" does not appear in the headline, because the buyer is buying fewer missed clauses, not a technology.
- **One real example replaces the chat demo.** Draft text on a recessed surface, the flag beside it with a 2px accent rule, the playbook rule cited by its ID. A visitor sees the output format before signing up.
- **Accuracy is a table with misses in it.** Legal buyers will ask. Answering with 14 missed indemnity deviations out of 171 builds more trust than "99% accurate" with no denominator.
- **Data handling is a section, not a badge.** Location, retention, training terms, subprocessors: four facts, one paragraph.
