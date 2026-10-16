---
name: unslop
description: Design and copy rules for interfaces and text that must not look or read as machine-made. Use when building, styling or reviewing any user interface (HTML, CSS, Tailwind, React, Vue, Svelte, shadcn/ui), picking colors, type, spacing, icons or components, writing landing pages, UI copy, error messages, docs, READMEs, release notes or commit messages, or when asked to make something look or sound less generic or less like AI output. Bans box shadows, gradients, glass and blur, emoji, glowing status pills and 350 overused words, and ships scripts that check for all of them. Not for backend code with no text a person reads.
metadata:
  version: "1.0.0"
  source: "https://github.com/remipelloux/unslop"
---

# UNSLOP

Rules for interfaces and copy that do not carry the generated look: no indigo buttons, no `rounded-2xl shadow-lg` cards, no gradient headlines, no emoji, no LIVE pills, no `seamless` or `unlock`. Every rule has values and a check.

This file holds the rules you need on every task. The full handbook (1,256,340 characters) is split into chapters under `references/`. Read only the chapters the task touches. All paths below are relative to the folder this file is in.

## Workflow

1. **Before writing interface code:** apply the hard rules and tokens below. For each component or page type in the task, open its chapter from the index at the end of this file (for example a pricing page: `5.5`, `6.14`).
2. **Before writing copy:** apply the copy rules below. The most frequent banned words are listed here; the full list of 350 is `references/banned-words.txt`. When a word feels like filler, search for it there, then read its entry through `references/lexicon-index.md`.
3. **Before you finish:** run the checks and fix everything they report.

```sh
python3 scripts/scan.py path/to/changed/files   # CSS, HTML, JSX, TSX, Vue, Svelte, locale JSON, Markdown
python3 scripts/lint.py path/to/file.md          # Markdown only, stricter on prose
```

Report the output in your reply. Never claim compliance you did not check. A line that must break a rule on purpose takes an `unslop-ignore` comment and a reason.

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

1. **No banned words.** None of the 350 entries in `references/banned-words.txt`, in any form (`leverage`, `leveraging`, `optimization`, `cutting edge`). If a sentence needs one to stand up, it has no claim in it: write the claim, or delete the sentence.
2. **No em dashes, no exclamation marks, no rhetorical questions.** Use a period or a comma.
3. **The first line says what the product does and for whom**, in words a customer would use. Then show it: a screenshot, a code sample, or a number with a unit and a date.
4. **Buttons name the action:** "Create invoice", "Install CLI", "Delete 3 files". Never "Get started", "Learn more" or "Submit" when a specific verb exists.
5. **Headings label the content:** "Pricing", "Install", "Limits". No slogans in headings.
6. **Every number has a unit, a source or a date.** Delete numbers you cannot source. No "10x faster", no "Trusted by 10,000+ teams".
7. **Testimonials need a full name, role, company and date**, or they go.
8. **No stock sentence shapes:** "It is not X, it is Y", "Not just X, but Y", groups of three adjectives, a colon before a reveal, "Imagine...", "Whether you are A or B", "From X to Y", a closing sentence that repeats the paragraph, a closing offer of more help.
9. **Lists hold parallel items. Paragraphs hold reasoning.** Do not turn every paragraph into bullets, and do not open every bullet with a bold label.
10. **Sentence case for headings and buttons.** Not Title Case Everywhere.

## Most frequent banned words

These are the entries models produce most. Any form counts. The other entries are in `references/banned-words.txt`.

```slop
delve, leverage, utilize, harness, unlock, unleash, elevate, empower,
streamline, revolutionize, supercharge, embark, navigate, foster, cultivate, underscore,
showcase, spearhead, bolster, amplify, reimagine, redefine, reshape, curate,
embrace, enhance, enrich, facilitate, optimize, maximize, democratize, future-proof,
unpack, immerse, captivate, ignite, propel, skyrocket, boost, fuel,
encompass, embody, thrive, garner, boast, elucidate, disrupt, level up,
dive into, deep dive, lean into, reach out, weave, orchestrate, seamless, robust,
comprehensive, cutting-edge, innovative, groundbreaking, game-changing, transformative, revolutionary, pivotal,
crucial, vital, essential, paramount, intricate, nuanced, holistic, dynamic,
vibrant, meticulous, unparalleled, compelling, stunning, remarkable, exceptional, invaluable,
intuitive, user-friendly, frictionless, effortless, delightful, sleek, elegant, modern,
next-gen, state-of-the-art, world-class, best-in-class, enterprise-grade, powerful, premium, bespoke,
tailored, immersive, engaging, impactful, actionable, insightful, diverse, vast,
crisp, clean, beautiful, magical, cohesive, granular, ai-powered, data-driven,
end-to-end, all-in-one, unified, curated, handcrafted, tapestry, testament, realm,
landscape, journey, ecosystem, paradigm, synergy, game-changer, insight, superpower,
solution, innovation, magic, furthermore, moreover, additionally, ultimately, essentially,
indeed, truly, in today's, the power of, the future of, with ease, made simple, take your,
when it comes to, whether you're, more than just, look no further
```

## Reference index

Each chapter is one file. Sizes are in thousands of characters, so you can judge the cost of reading one.

### Part 1. Ground Rules

| Chapter | File | Size |
| --- | --- | --- |
| 1.1 What this file is for | `references/01-ground-rules/01.01-what-this-file-is-for.md` | 1k |
| 1.2 How to use it | `references/01-ground-rules/01.02-how-to-use-it.md` | 1k |
| 1.3 The hard rules | `references/01-ground-rules/01.03-the-hard-rules.md` | 2k |
| 1.4 The soft rules | `references/01-ground-rules/01.04-the-soft-rules.md` | 1k |
| 1.5 The signature, in one table | `references/01-ground-rules/01.05-the-signature-in-one-table.md` | 2k |
| 1.6 Tokens at a glance | `references/01-ground-rules/01.06-tokens-at-a-glance.md` | 2k |
| 1.7 How the rules are worded | `references/01-ground-rules/01.07-how-the-rules-are-worded.md` | 1k |
| 1.8 What this file does not do | `references/01-ground-rules/01.08-what-this-file-does-not-do.md` | 1k |
| 1.9 Checklist for Part 1 | `references/01-ground-rules/01.09-checklist-for-part-1.md` | 1k |

### Part 2. Color, Surfaces and Depth

| Chapter | File | Size |
| --- | --- | --- |
| 2.0 Overview | `references/02-color-surfaces-and-depth/02.00-overview.md` | 1k |
| 2.1 Why generated interfaces all look alike | `references/02-color-surfaces-and-depth/02.01-why-generated-interfaces-all-look-alike.md` | 9k |
| 2.2 The gradient ban | `references/02-color-surfaces-and-depth/02.02-the-gradient-ban.md` | 11k |
| 2.3 Building a palette that is not the default | `references/02-color-surfaces-and-depth/02.03-building-a-palette-that-is-not-the-default.md` | 21k |
| 2.4 Semantic color | `references/02-color-surfaces-and-depth/02.04-semantic-color.md` | 9k |
| 2.5 Depth without shadows | `references/02-color-surfaces-and-depth/02.05-depth-without-shadows.md` | 14k |
| 2.6 Borders and rules | `references/02-color-surfaces-and-depth/02.06-borders-and-rules.md` | 9k |
| 2.7 Corner radius | `references/02-color-surfaces-and-depth/02.07-corner-radius.md` | 5k |
| 2.8 Glass, blur, glow, noise and neon | `references/02-color-surfaces-and-depth/02.08-glass-blur-glow-noise-and-neon.md` | 5k |
| 2.9 Dark mode done by hand | `references/02-color-surfaces-and-depth/02.09-dark-mode-done-by-hand.md` | 7k |
| 2.10 Data and chart color | `references/02-color-surfaces-and-depth/02.10-data-and-chart-color.md` | 9k |
| 2.11 Color in code | `references/02-color-surfaces-and-depth/02.11-color-in-code.md` | 9k |
| 2.12 Review checklist for Part 2 | `references/02-color-surfaces-and-depth/02.12-review-checklist-for-part-2.md` | 2k |

### Part 3. Type, Space, Layout, Icons and Motion

| Chapter | File | Size |
| --- | --- | --- |
| 3.0 Overview | `references/03-type-space-layout-icons-and-motion/03.00-overview.md` | 1k |
| 3.1 Typefaces | `references/03-type-space-layout-icons-and-motion/03.01-typefaces.md` | 17k |
| 3.2 Type scale and hierarchy | `references/03-type-space-layout-icons-and-motion/03.02-type-scale-and-hierarchy.md` | 14k |
| 3.3 Text details | `references/03-type-space-layout-icons-and-motion/03.03-text-details.md` | 14k |
| 3.4 Spacing system | `references/03-type-space-layout-icons-and-motion/03.04-spacing-system.md` | 9k |
| 3.5 Layout and grid | `references/03-type-space-layout-icons-and-motion/03.05-layout-and-grid.md` | 12k |
| 3.6 Responsive behavior | `references/03-type-space-layout-icons-and-motion/03.06-responsive-behavior.md` | 11k |
| 3.7 Icons | `references/03-type-space-layout-icons-and-motion/03.07-icons.md` | 9k |
| 3.8 Images and illustration | `references/03-type-space-layout-icons-and-motion/03.08-images-and-illustration.md` | 8k |
| 3.9 Motion | `references/03-type-space-layout-icons-and-motion/03.09-motion.md` | 6k |
| 3.10 Accessibility as design quality | `references/03-type-space-layout-icons-and-motion/03.10-accessibility-as-design-quality.md` | 6k |
| 3.11 Review checklist for Part 3 | `references/03-type-space-layout-icons-and-motion/03.11-review-checklist-for-part-3.md` | 4k |

### Part 4. Components, A to M

| Chapter | File | Size |
| --- | --- | --- |
| 4.0 Overview | `references/04-components-a-to-m/04.00-overview.md` | 1k |
| 4.1 Accordions | `references/04-components-a-to-m/04.01-accordions.md` | 5k |
| 4.2 Alerts and banners | `references/04-components-a-to-m/04.02-alerts-and-banners.md` | 6k |
| 4.3 Avatars | `references/04-components-a-to-m/04.03-avatars.md` | 4k |
| 4.4 Badges, tags and status indicators | `references/04-components-a-to-m/04.04-badges-tags-and-status-indicators.md` | 8k |
| 4.5 Breadcrumbs | `references/04-components-a-to-m/04.05-breadcrumbs.md` | 3k |
| 4.6 Buttons | `references/04-components-a-to-m/04.06-buttons.md` | 6k |
| 4.7 Cards | `references/04-components-a-to-m/04.07-cards.md` | 5k |
| 4.8 Charts and stat tiles | `references/04-components-a-to-m/04.08-charts-and-stat-tiles.md` | 6k |
| 4.9 Checkboxes, radios and switches | `references/04-components-a-to-m/04.09-checkboxes-radios-and-switches.md` | 5k |
| 4.10 Code blocks | `references/04-components-a-to-m/04.10-code-blocks.md` | 4k |
| 4.11 Command palettes | `references/04-components-a-to-m/04.11-command-palettes.md` | 4k |
| 4.12 Data tables | `references/04-components-a-to-m/04.12-data-tables.md` | 5k |
| 4.13 Date pickers | `references/04-components-a-to-m/04.13-date-pickers.md` | 4k |
| 4.14 Dialogs and modals | `references/04-components-a-to-m/04.14-dialogs-and-modals.md` | 4k |
| 4.15 Dropdown menus | `references/04-components-a-to-m/04.15-dropdown-menus.md` | 4k |
| 4.16 Empty states | `references/04-components-a-to-m/04.16-empty-states.md` | 3k |
| 4.17 File upload | `references/04-components-a-to-m/04.17-file-upload.md` | 5k |
| 4.18 Footers | `references/04-components-a-to-m/04.18-footers.md` | 4k |
| 4.19 Forms and text inputs | `references/04-components-a-to-m/04.19-forms-and-text-inputs.md` | 5k |
| 4.20 Headers and top navigation | `references/04-components-a-to-m/04.20-headers-and-top-navigation.md` | 4k |
| 4.21 Hero sections | `references/04-components-a-to-m/04.21-hero-sections.md` | 5k |
| 4.22 Links | `references/04-components-a-to-m/04.22-links.md` | 3k |
| 4.23 Lists | `references/04-components-a-to-m/04.23-lists.md` | 3k |
| 4.24 Loading and skeletons | `references/04-components-a-to-m/04.24-loading-and-skeletons.md` | 4k |
| 4.25 Menus and context menus | `references/04-components-a-to-m/04.25-menus-and-context-menus.md` | 5k |

### Part 5. Components, N to Z, and Marketing Sections

| Chapter | File | Size |
| --- | --- | --- |
| 5.0 Overview | `references/05-components-n-to-z-and-marketing-sections/05.00-overview.md` | 1k |
| 5.1 Navigation sidebars | `references/05-components-n-to-z-and-marketing-sections/05.01-navigation-sidebars.md` | 6k |
| 5.2 Notifications and toasts | `references/05-components-n-to-z-and-marketing-sections/05.02-notifications-and-toasts.md` | 5k |
| 5.3 Onboarding flows and checklists | `references/05-components-n-to-z-and-marketing-sections/05.03-onboarding-flows-and-checklists.md` | 6k |
| 5.4 Pagination | `references/05-components-n-to-z-and-marketing-sections/05.04-pagination.md` | 5k |
| 5.5 Pricing tables | `references/05-components-n-to-z-and-marketing-sections/05.05-pricing-tables.md` | 8k |
| 5.6 Progress bars and steppers | `references/05-components-n-to-z-and-marketing-sections/05.06-progress-bars-and-steppers.md` | 5k |
| 5.7 Search | `references/05-components-n-to-z-and-marketing-sections/05.07-search.md` | 5k |
| 5.8 Selects and comboboxes | `references/05-components-n-to-z-and-marketing-sections/05.08-selects-and-comboboxes.md` | 5k |
| 5.9 Settings pages | `references/05-components-n-to-z-and-marketing-sections/05.09-settings-pages.md` | 5k |
| 5.10 Sliders | `references/05-components-n-to-z-and-marketing-sections/05.10-sliders.md` | 4k |
| 5.11 Tabs and segmented controls | `references/05-components-n-to-z-and-marketing-sections/05.11-tabs-and-segmented-controls.md` | 5k |
| 5.12 Testimonials | `references/05-components-n-to-z-and-marketing-sections/05.12-testimonials.md` | 4k |
| 5.13 Timelines and changelogs | `references/05-components-n-to-z-and-marketing-sections/05.13-timelines-and-changelogs.md` | 4k |
| 5.14 Tooltips and popovers | `references/05-components-n-to-z-and-marketing-sections/05.14-tooltips-and-popovers.md` | 4k |
| 5.15 User menus and account switchers | `references/05-components-n-to-z-and-marketing-sections/05.15-user-menus-and-account-switchers.md` | 5k |
| 5.16 Feature grids | `references/05-components-n-to-z-and-marketing-sections/05.16-feature-grids.md` | 4k |
| 5.17 Logo walls and social proof | `references/05-components-n-to-z-and-marketing-sections/05.17-logo-walls-and-social-proof.md` | 4k |
| 5.18 Stats and KPI rows | `references/05-components-n-to-z-and-marketing-sections/05.18-stats-and-kpi-rows.md` | 4k |
| 5.19 Call-to-action sections | `references/05-components-n-to-z-and-marketing-sections/05.19-call-to-action-sections.md` | 3k |
| 5.20 FAQ sections | `references/05-components-n-to-z-and-marketing-sections/05.20-faq-sections.md` | 3k |
| 5.21 Comparison tables | `references/05-components-n-to-z-and-marketing-sections/05.21-comparison-tables.md` | 3k |
| 5.22 Error pages | `references/05-components-n-to-z-and-marketing-sections/05.22-error-pages.md` | 4k |
| 5.23 Auth screens | `references/05-components-n-to-z-and-marketing-sections/05.23-auth-screens.md` | 5k |
| 5.24 Chat and AI assistant interfaces | `references/05-components-n-to-z-and-marketing-sections/05.24-chat-and-ai-assistant-interfaces.md` | 5k |
| 5.25 Dashboards as a whole | `references/05-components-n-to-z-and-marketing-sections/05.25-dashboards-as-a-whole.md` | 4k |

### Part 6. Stack Setup and Full Page Rebuilds

| Chapter | File | Size |
| --- | --- | --- |
| 6.0 Overview | `references/06-stack-setup-and-full-page-rebuilds/06.00-overview.md` | 1k |
| 6.1 Base stylesheet | `references/06-stack-setup-and-full-page-rebuilds/06.01-base-stylesheet.md` | 12k |
| 6.2 Tailwind v3 configuration | `references/06-stack-setup-and-full-page-rebuilds/06.02-tailwind-v3-configuration.md` | 7k |
| 6.3 Tailwind v4 configuration | `references/06-stack-setup-and-full-page-rebuilds/06.03-tailwind-v4-configuration.md` | 5k |
| 6.4 shadcn/ui | `references/06-stack-setup-and-full-page-rebuilds/06.04-shadcn-ui.md` | 13k |
| 6.5 Design tokens as data | `references/06-stack-setup-and-full-page-rebuilds/06.05-design-tokens-as-data.md` | 6k |
| 6.6 Lint rules that enforce it | `references/06-stack-setup-and-full-page-rebuilds/06.06-lint-rules-that-enforce-it.md` | 10k |
| 6.7 Instructions for coding agents | `references/06-stack-setup-and-full-page-rebuilds/06.07-instructions-for-coding-agents.md` | 5k |
| 6.8 SaaS landing page | `references/06-stack-setup-and-full-page-rebuilds/06.08-saas-landing-page.md` | 8k |
| 6.9 Developer tool landing page | `references/06-stack-setup-and-full-page-rebuilds/06.09-developer-tool-landing-page.md` | 6k |
| 6.10 Analytics dashboard | `references/06-stack-setup-and-full-page-rebuilds/06.10-analytics-dashboard.md` | 7k |
| 6.11 Personal portfolio | `references/06-stack-setup-and-full-page-rebuilds/06.11-personal-portfolio.md` | 5k |
| 6.12 Documentation home | `references/06-stack-setup-and-full-page-rebuilds/06.12-documentation-home.md` | 5k |
| 6.13 Blog article page | `references/06-stack-setup-and-full-page-rebuilds/06.13-blog-article-page.md` | 5k |
| 6.14 Pricing page | `references/06-stack-setup-and-full-page-rebuilds/06.14-pricing-page.md` | 6k |
| 6.15 Mobile app marketing page | `references/06-stack-setup-and-full-page-rebuilds/06.15-mobile-app-marketing-page.md` | 5k |
| 6.16 Admin settings area | `references/06-stack-setup-and-full-page-rebuilds/06.16-admin-settings-area.md` | 6k |
| 6.17 AI product landing page | `references/06-stack-setup-and-full-page-rebuilds/06.17-ai-product-landing-page.md` | 7k |
| 6.18 Open source project README rendered as a site | `references/06-stack-setup-and-full-page-rebuilds/06.18-open-source-project-readme-rendered-as-a-site.md` | 5k |
| 6.19 E-commerce product page | `references/06-stack-setup-and-full-page-rebuilds/06.19-e-commerce-product-page.md` | 6k |
| 6.20 Checklist for Part 6 | `references/06-stack-setup-and-full-page-rebuilds/06.20-checklist-for-part-6.md` | 1k |

### Part 7. The Lexicon

| Chapter | File | Size |
| --- | --- | --- |
| 7.0 How the ban works | `references/07-the-lexicon/07.00-how-the-ban-works.md` | 3k |
| 7.1 Entries 001 to 070: verbs | `references/07-the-lexicon/07.01-entries-001-to-070-verbs.md` | 5k |
| 7.2 Entries 071 to 140: adjectives, part one | `references/07-the-lexicon/07.02-entries-071-to-140-adjectives-part-one.md` | 6k |
| 7.3 Entries 141 to 210: adjectives, part two, and first nouns | `references/07-the-lexicon/07.03-entries-141-to-210-adjectives-part-two-and-first-nouns.md` | 6k |
| 7.4 Entries 211 to 280: nouns and first connectives | `references/07-the-lexicon/07.04-entries-211-to-280-nouns-and-first-connectives.md` | 6k |
| 7.5 Entries 281 to 350: adverbs, connectives and stock phrases | `references/07-the-lexicon/07.05-entries-281-to-350-adverbs-connectives-and-stock-phrases.md` | 6k |

### Part 8. Sentences, Structure and Microcopy

| Chapter | File | Size |
| --- | --- | --- |
| 8.0 Overview | `references/08-sentences-structure-and-microcopy/08.00-overview.md` | 1k |
| 8.1 How tells work | `references/08-sentences-structure-and-microcopy/08.01-how-tells-work.md` | 2k |
| 8.2 Tells of framing and argument | `references/08-sentences-structure-and-microcopy/08.02-tells-of-framing-and-argument.md` | 14k |
| 8.3 Tells of texture | `references/08-sentences-structure-and-microcopy/08.03-tells-of-texture.md` | 7k |
| 8.4 Tells of layout | `references/08-sentences-structure-and-microcopy/08.04-tells-of-layout.md` | 4k |
| 8.5 Punctuation and formatting rules | `references/08-sentences-structure-and-microcopy/08.05-punctuation-and-formatting-rules.md` | 5k |
| 8.6 Microcopy for controls and forms | `references/08-sentences-structure-and-microcopy/08.06-microcopy-for-controls-and-forms.md` | 9k |
| 8.7 Microcopy for messages and pages | `references/08-sentences-structure-and-microcopy/08.07-microcopy-for-messages-and-pages.md` | 6k |
| 8.8 Microcopy for publishing and code | `references/08-sentences-structure-and-microcopy/08.08-microcopy-for-publishing-and-code.md` | 8k |
| 8.9 Voice | `references/08-sentences-structure-and-microcopy/08.09-voice.md` | 5k |
| 8.10 A full rewrite, start to finish | `references/08-sentences-structure-and-microcopy/08.10-a-full-rewrite-start-to-finish.md` | 3k |
| 8.11 Prompting a model for plain copy | `references/08-sentences-structure-and-microcopy/08.11-prompting-a-model-for-plain-copy.md` | 2k |
| 8.12 Quick reference | `references/08-sentences-structure-and-microcopy/08.12-quick-reference.md` | 2k |

### Part 9. Audit and Enforcement

| Chapter | File | Size |
| --- | --- | --- |
| 9.0 Overview | `references/09-audit-and-enforcement/09.00-overview.md` | 1k |
| 9.1 Auditing an existing product | `references/09-audit-and-enforcement/09.01-auditing-an-existing-product.md` | 4k |
| 9.2 Search commands for visual tells | `references/09-audit-and-enforcement/09.02-search-commands-for-visual-tells.md` | 5k |
| 9.3 Search commands for verbal tells | `references/09-audit-and-enforcement/09.03-search-commands-for-verbal-tells.md` | 5k |
| 9.4 What scripts/lint.py checks | `references/09-audit-and-enforcement/09.04-what-scripts-lint-py-checks.md` | 7k |
| 9.5 CI integration | `references/09-audit-and-enforcement/09.05-ci-integration.md` | 5k |
| 9.6 Pre-commit hook | `references/09-audit-and-enforcement/09.06-pre-commit-hook.md` | 2k |
| 9.7 Review rubric | `references/09-audit-and-enforcement/09.07-review-rubric.md` | 3k |
| 9.8 Ship checklist for a page | `references/09-audit-and-enforcement/09.08-ship-checklist-for-a-page.md` | 3k |
