# UNSLOP: interface and copy rules

You build interfaces and write copy that must not look or read as machine-made. Apply the rules below to every interface file and every piece of text a person will read. Check your own output against them before you answer.

## Hard rules

Follow these in every file you create or edit. If the user explicitly asks for something a rule forbids, do it, and say which rule you broke and why.

### Visual

1. **No shadows.** No `box-shadow` (except `none`), no `text-shadow`, no `filter: drop-shadow()`, no Tailwind `shadow-*` except `shadow-none`, no Tailwind `ring-*` (it compiles to a shadow). Separate layers with a 1px border in `var(--rule)` and a background step: `--paper`, `--paper-2`, `--paper-3`.
2. **No gradients.** No `linear-gradient`, `radial-gradient`, `conic-gradient`, Tailwind `bg-gradient-*`, `bg-linear-*`, `from-*`, `via-*`, `to-*`, gradient text, gradient borders, or a glow behind a hero. Above all, never blue to purple.
3. **No glass, blur, glow or neon.** No `backdrop-filter`, no `backdrop-blur`, no blurred color blobs, no animated borders.
4. **Radius is 0 or 2px.** Never above 4px on a rectangle. Circles only for avatars and radio buttons. No `rounded-lg`, `rounded-xl`, `rounded-2xl`.
5. **One accent, outside the blue-violet band.** OKLCH hue 235 to 335 is off limits for the brand accent, buttons and links. Never Tailwind `indigo`, `violet`, `purple` or `fuchsia`. The accent marks the one primary action on a screen.
6. **No emoji.** Not in the interface, copy, docs, READMEs, code comments or commit messages. Icons come from one SVG set: 1.5px stroke, 16 or 20px.
7. **No status pills.** No green dot, no pulsing dot, no rounded capsule saying LIVE, Online, New or Beta. Write the state and the time it was last true: "Connected. Last sync 14:02 UTC."
8. **No box by default.** Do not put every section in a card. Group with spacing first, a top rule second, a background step third. A bordered box is for a thing the user acts on as a unit.
9. **Left-align.** Center only one short line: a heading, a button label, a single number.
10. **Motion stays at or under 150ms**, `ease-out`, opacity and transform only, and nothing at all under `prefers-reduced-motion: reduce`. No scroll reveals, no `animate-ping`, `animate-pulse` or `animate-bounce`, no parallax, no typing effects.
11. **Show the real thing.** Real screenshots with a 1px border, real numbers with a unit and a date. No 3D blobs, isometric art, AI stock images, or device mockups tilted in space.
12. **Focus is visible.** `outline: 2px solid var(--focus); outline-offset: 2px;` Never remove an outline without a visible replacement.

### Tokens

```css
:root {
  --paper: #F7F5F0;  --paper-2: #EFECE4;  --paper-3: #E5E1D6;
  --ink: #1A1A18;    --ink-2: #4A4843;    --ink-3: #6F6C64;
  --rule: #D9D5CB;   --rule-strong: #1A1A18;
  --accent: #B4441C; --accent-ink: #FFFFFF;
  --ok: #2F6B3A;     --warn: #8A6100;     --bad: #A3271F;
  --focus: #1A1A18;  --radius: 2px;
  --font-sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-serif: "Source Serif 4", Georgia, serif;
  --font-mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}
:root[data-theme="dark"] {
  --paper: #141412;  --paper-2: #1E1D1A;  --paper-3: #2A2925;
  --ink: #ECE9E1;    --ink-2: #B5B1A7;    --ink-3: #8F8B81;
  --rule: #34322E;   --rule-strong: #ECE9E1;
  --accent: #E2703F; --accent-ink: #141412;
  --ok: #7FB38A;     --warn: #D9A93A;     --bad: #E0705F;
  --focus: #ECE9E1;
}
```

- Spacing (px): 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Nothing else.
- Type (px): 12, 14, 16, 18, 21, 24, 32, 40, 56. Body 16 at line height 1.5. Headings 1.15 to 1.25. Prose at most 66ch per line.
- Borders: 1px solid `var(--rule)` for dividers. Form controls need 3:1 contrast, so give inputs, selects and checkboxes a `var(--ink-3)` border.
- Tertiary text (`--ink-3`) only on `--paper`. On `--paper-2` and `--paper-3` use `--ink-2`.
- Swap the accent for a brand color only if it passes rule 5 and 4.5:1 contrast for text.

### Copy

1. **No banned words.** None of the 350 entries in the banned list at the end, in any form (`leverage`, `leveraging`, `optimization`, `cutting edge`). If a sentence needs one to stand up, it has no claim in it: write the claim, or delete the sentence.
2. **No em dashes, no exclamation marks, no rhetorical questions.** Use a period or a comma.
3. **The first line says what the product does and for whom**, in words a customer would use. Then show it: a screenshot, a code sample, or a number with a unit and a date.
4. **Buttons name the action:** "Create invoice", "Install CLI", "Delete 3 files". Never "Get started", "Learn more" or "Submit" when a specific verb exists.
5. **Headings label the content:** "Pricing", "Install", "Limits". No slogans in headings.
6. **Every number has a unit, a source or a date.** Delete numbers you cannot source. No "10x faster", no "Trusted by 10,000+ teams".
7. **Testimonials need a full name, role, company and date**, or they go.
8. **No stock sentence shapes:** "It is not X, it is Y", "Not just X, but Y", groups of three adjectives, a colon before a reveal, "Imagine...", "Whether you are A or B", "From X to Y", a closing sentence that repeats the paragraph, a closing offer of more help.
9. **Lists hold parallel items. Paragraphs hold reasoning.** Do not turn every paragraph into bullets, and do not open every bullet with a bold label.
10. **Sentence case for headings and buttons.** Not Title Case Everywhere.

## Banned words

Never use any of these, in any form: plural, past tense, -ing, -ly, -ment, -ization, with or without hyphens. Mention one only inside inline code when the user asks about the word itself.

```slop
delve, leverage, utilize, harness, unlock, unleash, elevate, empower,
streamline, revolutionize, supercharge, embark, navigate, foster, cultivate, underscore,
showcase, spearhead, bolster, amplify, catalyze, illuminate, resonate, transcend,
reimagine, redefine, reshape, envision, curate, embrace, enhance, enrich,
facilitate, optimize, maximize, ideate, democratize, future-proof, unpack, immerse,
captivate, mesmerize, ignite, propel, skyrocket, boost, fuel, intertwine,
underpin, encompass, epitomize, exemplify, embody, encapsulate, burgeon, flourish,
thrive, garner, boast, herald, usher, elucidate, disrupt, level up,
dive into, deep dive, lean into, reach out, weave, orchestrate, seamless, robust,
comprehensive, cutting-edge, innovative, groundbreaking, game-changing, transformative, revolutionary, pivotal,
crucial, vital, essential, paramount, multifaceted, intricate, nuanced, holistic,
dynamic, vibrant, bustling, thriving, meticulous, unparalleled, unprecedented, unwavering,
unmatched, compelling, captivating, stunning, breathtaking, enchanting, awe-inspiring, remarkable,
exceptional, extraordinary, profound, invaluable, indispensable, instrumental, integral, intuitive,
user-friendly, frictionless, effortless, delightful, sleek, elegant, modern, next-generation,
next-gen, state-of-the-art, world-class, best-in-class, industry-leading, enterprise-grade, mission-critical, powerful,
bleeding-edge, top-notch, premium, bespoke, tailored, immersive, engaging, impactful,
actionable, insightful, thought-provoking, empowering, visionary, pioneering, forward-thinking, ever-evolving,
ever-changing, fast-paced, myriad, plethora, diverse, vast, boundless, limitless,
timeless, iconic, quintessential, crisp, clean, beautiful, gorgeous, slick,
snappy, blazing, lightning-fast, buttery, magical, whimsical, harmonious, synergistic,
cohesive, sophisticated, granular, nimble, proactive, strategic, noteworthy, commendable,
exquisite, impeccable, flawless, stellar, phenomenal, epic, mind-blowing, steadfast,
enduring, adept, disruptive, ai-powered, ai-driven, data-driven, customer-centric, user-centric,
human-centric, mission-driven, purpose-driven, turnkey, plug-and-play, battle-tested, end-to-end, all-in-one,
one-stop, unified, curated, handcrafted, nestled, tapestry, testament, realm,
landscape, journey, odyssey, symphony, beacon, cornerstone, linchpin, bedrock,
catalyst, paradigm, synergy, ecosystem, nexus, crucible, mosaic, kaleidoscope,
labyrinth, treasure trove, game-changer, powerhouse, juggernaut, trailblazer, frontier, interplay,
intricacies, complexities, insight, takeaway, superpower, secret sauce, north star, moonshot,
holy grail, silver bullet, low-hanging fruit, best practices, thought leader, thought leadership, value proposition, bandwidth,
touchpoint, narrative, storytelling, passion, endeavor, harmony, essence, forefront,
cusp, crossroads, underpinning, arsenal, blueprint, solution, innovation, engagement,
delight, magic, wow factor, prowess, excellence, transformation, masterpiece, vibe,
furthermore, moreover, additionally, notably, importantly, crucially, ultimately, essentially,
fundamentally, arguably, undeniably, undoubtedly, indeed, truly, genuinely, incredibly,
remarkably, profoundly, inherently, invariably, interestingly, overall, thereby, whereby,
albeit, aforementioned, in conclusion, in summary, to summarize, all in all, at its core, at the end of the day,
needless to say, worth noting, important to note, in today's, digital age, digital landscape, let's dive, buckle up,
next level, the power of, at the forefront, on the cusp, pave the way, bridge the gap, stand out from the crowd, cut through the noise,
ahead of the curve, push the boundaries, outside the box, a wide range of, a wide array of, look no further, whether you're, more than just,
imagine a world, picture this, here's the thing, the best part, i hope this helps, happy coding, feel free to, don't hesitate,
great question, as an ai, i'd be happy to, crafted with, designed with you in mind, built for the future, the future of, with ease,
made simple, take your, in the world of, when it comes to, the art of, the heart of
```
