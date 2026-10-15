## Part 1. Ground Rules

### 1.1 What this file is for

Language models and the starter kits they lean on produce the same interface every time. Indigo button. Rounded card with a soft shadow. A hero with a radial glow, a gradient headline, a pill that says "Now with AI", and two buttons. A grid of six features, each icon sitting in a pastel rounded square. A green dot next to the word LIVE. Copy that promises to `unlock` something `seamless`.

None of these choices is wrong on its own. Together they are a signature, and readers have learned to see it. Once a visitor spots the signature, they stop reading the product and start reading the process that made it. They assume nobody looked closely, and they are usually right.

This file replaces each default with a specific decision. It is long because the defaults are many, and because "make it look less generic" is not an instruction anyone, human or model, can follow. "Use a 1px `#D9D5CB` border and no shadow" is.

### 1.2 How to use it

With a coding agent:

1. Put this whole file in the agent's context, or put Part 1 and the agent instructions block from Part 6.7 in the system prompt and the rest in a docs folder the agent can search.
2. Tell the agent which parts apply to the task: Parts 2 to 6 for interface work, Parts 7 and 8 for any text a person will read, Part 9 before merging.
3. Run the checks in Part 9 on the agent's output. Do not trust a claim of compliance; grep for it.

With a person:

1. Read Part 1 in full. It takes ten minutes.
2. Skim the chapter headings of Parts 2 to 6 and read the ones that match what you are building this week.
3. Keep Part 7 open while writing copy. Search it for any word that feels like filler.

During review:

1. Run `scripts/lint.py` on Markdown, and the grep commands in Part 9 on source code.
2. Walk the page with the checklist at the end of each Part.
3. Reject on any hard rule. Discuss everything else.

### 1.3 The hard rules

These hold everywhere, with no exceptions for a deadline, a client request, or a framework default. Each is checked by a command in Part 9.

1. **No shadows.** `box-shadow`, `text-shadow`, `filter: drop-shadow()`, and every Tailwind `shadow-*` utility except `shadow-none` are banned. Separate layers with a 1px border and a tonal step in the background. Part 2.5.
2. **No gradients in blue, indigo, violet, purple or fuchsia.** Zero. Not in buttons, not in text, not in borders, not as a glow behind the hero. In practice this file bans gradients of every color in interface chrome, because the exceptions people ask for are almost always the same blue-to-purple sweep with a new name. Part 2.2.
3. **No emoji in the interface, in copy, in docs, in commit messages, or in code comments.** Icons come from one SVG set. Status comes from words. Part 3.7.
4. **No glowing status pills.** No green dot with "LIVE", "Online", "New" or "Beta" inside a rounded capsule. State the status in text with the time it was last true: "Connected. Last sync 14:02." Part 4.4.
5. **No banned words.** None of the 350 entries in Part 7 appear in shipped copy, in any form. If a sentence needs one of them to stand up, the sentence has nothing to say. Rewrite it with the specific claim, or delete it.
6. **No glass, glow, blur or neon.** `backdrop-filter`, frosted panels, outer glows, and animated borders are banned. Part 2.8.
7. **Radius is 0 or 2px.** Never above 4px on any rectangle. Circles are allowed only for avatars and radio buttons. Part 2.7.
8. **One accent color, outside the blue-violet band.** Hue between 235 and 335 degrees in OKLCH is off limits for the brand accent. Links may be underlined ink instead. Part 2.3.
9. **No em dashes, no exclamation marks in interface copy.** Use a period or a comma. Part 8.
10. **Show the real thing.** Real screenshots, real numbers with units and dates, real names with permission. No 3D blobs, no isometric illustrations, no stock photos of a smiling team around a laptop, no testimonials you cannot source. Part 3.8 and Part 5.

### 1.4 The soft rules

These are defaults. Break one when you can write down, in a sentence, what the break buys the reader.

1. Left-align text. Center only single lines: a short heading, a button label, a number in a stat.
2. Body text is 16px at 1.5 line height, at most 66 characters per line.
3. Use the spacing scale in 1.6. Group with space first, rules second, background third, borders on boxes last.
4. One typeface family for the interface, plus a mono. A serif for long reading is allowed.
5. Motion stays at or under 150ms, moves only opacity and transform, and stops completely under `prefers-reduced-motion: reduce`.
6. Headings say what the section contains. "Pricing", not "Simple, transparent pricing for teams of every size".
7. Buttons say what they do: "Create invoice", "Send 3 invites", "Delete project". Never "Get started" when something more exact exists.
8. Every number on a page has a unit, a source or a date.
9. Lists hold items that are actually parallel. Paragraphs hold reasoning.
10. A page has one primary action. Every other action is visibly secondary.

### 1.5 The signature, in one table

The table lists the patterns that most often mark an interface as generated, the default each comes from, and the replacement this file uses. The details live in the Part named in the last column.

| Pattern | Usual source | Replace with | Part |
| --- | --- | --- | --- |
| `bg-indigo-600` primary button | Tailwind docs and UI kits | Accent `#B4441C` or ink `#1A1A18` fill, 2px radius | 2.3, 4.6 |
| `rounded-2xl shadow-lg` card | Tailwind UI, shadcn `Card` | 1px rule, `--paper-2` fill, or no box at all | 2.5, 4.7 |
| Blue-to-purple gradient headline | Landing page templates | Solid ink, size and weight for hierarchy | 2.2, 3.2 |
| Radial glow behind the hero | Vercel-style templates | Nothing. Or a real product screenshot with a 1px border | 4.21 |
| "Now with AI" pill above the headline | AI landing templates | A dated line in the changelog | 4.21 |
| Six features in icon tiles | Every SaaS template | Three to five features as rows, with screenshots and numbers | 5.16 |
| Green dot plus LIVE | Status pill components | "Running since 09:41" in text | 4.4 |
| Emoji as bullets or section icons | Model-written READMEs | Plain list markers, or nothing | 3.7 |
| Inter at every size, tracking tight | Next.js starters | A chosen face, default tracking | 3.1 |
| Glass card with backdrop blur | Dribbble trends | Opaque `--paper-2` surface with a 1px rule | 2.8 |
| Fade-up on every section | Animation libraries | Static content | 3.9 |
| Five-star testimonial with stock avatar | Template filler | Sourced quote with name, role, company, date | 5.12 |
| "10x faster" stat row | Marketing filler | One measured number with method and date | 5.18 |
| Everything centered | Hero templates | A shared left edge | 3.5 |

### 1.6 Tokens at a glance

The whole file uses one set of tokens. Copy them as written, then change the accent if you have a brand color that passes the rules in Part 2.3.

```css
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
}

*, *::before, *::after { box-shadow: none; }

:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
```

| Scale | Values |
| --- | --- |
| Spacing (px) | 4, 8, 12, 16, 24, 32, 48, 64, 96, 128 |
| Type (px) | 12, 14, 16, 18, 21, 24, 32, 40, 56 |
| Line height | 1.5 body, 1.15 to 1.25 headings |
| Measure | 66ch for prose |
| Border | 1px solid `var(--rule)` |
| Radius | 0 or 2px, never above 4px |
| Motion | 0 to 150ms, `ease-out`, opacity and transform only |
| Icons | One SVG set, 16 or 20px, 1.5px stroke |

### 1.7 How the rules are worded

Each rule in this file has the same shape, so an agent can apply it without interpretation:

- **The default it replaces**, named by source: a Tailwind class, a component library default, a template, a habit of model output.
- **The replacement**, with values: hex, px, ms, ratio, count.
- **The check**: a grep pattern, a lint rule, or a question with a yes or no answer.

When a rule seems to conflict with a framework, the rule wins and the framework gets configured. Part 6 shows the configuration for Tailwind v3 and v4, shadcn/ui, plain CSS, and design token JSON.

When two rules in this file conflict, the more specific one wins: a chapter rule beats a Part rule, and a Part rule beats this ground-rules Part. Accessibility rules beat every visual rule.

### 1.8 What this file does not do

It does not pick a brand for you. The canonical tokens are a working default, chosen to be plainly unlike the generated look: warm paper, near-black ink, one burnt orange accent. Swap them for your own as long as the new values pass the same checks.

It does not ban taste. A product can be playful, loud, dense or sparse and still follow every rule here. The rules remove the defaults that read as nobody deciding. They leave every real decision to you.

It does not promise that following it makes a product good. It promises the product will not look like it was made by not looking.

### 1.9 Checklist for Part 1

- The agent or reviewer has read 1.3 and 1.4.
- The tokens in 1.6 are in the codebase, or a documented replacement set is.
- `box-shadow` other than `none` returns zero results in source.
- Gradient functions return zero results in source.
- Emoji ranges return zero results in source and copy.
- No status pill with a dot exists in the component library.
- Shipped copy passes `scripts/lint.py` or the equivalent string check from Part 9.
