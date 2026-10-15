### 3.9 Motion

#### The budget

Every transition lasts 0 to 150ms, eases out, and animates only `opacity` and `transform`. Under `prefers-reduced-motion: reduce`, nothing moves at all.

| Interaction | Duration | Property |
| --- | --- | --- |
| Button press, checkbox, toggle | 0ms | state change is instant |
| Hover color or underline change | 0 to 100ms | `color`, `background-color` (paint only, no layout) |
| Menu, popover, tooltip open | 100 to 150ms | `opacity`, `transform: translateY(4px)` to 0 |
| Menu, popover, tooltip close | 0 to 100ms | `opacity` |
| Toast enter | 150ms | `opacity`, `transform: translateY(8px)` to 0 |
| Disclosure caret | 100ms | `transform: rotate()` |
| Dialog open | 0 to 150ms | `opacity` |

Hover color changes are listed because they are paint-only and cheap; the "opacity and transform only" rule covers anything that moves.

```css
:root {
  --dur-0: 0ms;
  --dur-1: 100ms;
  --dur-2: 150ms;
  --ease-out: cubic-bezier(0.2, 0, 0, 1);
}

.popover {
  transition: opacity var(--dur-2) var(--ease-out), transform var(--dur-2) var(--ease-out);
}
.popover[data-state="closed"] { opacity: 0; transform: translateY(4px); pointer-events: none; }
.popover[data-state="open"]   { opacity: 1; transform: none; }

a, .button { transition: color var(--dur-1) var(--ease-out), background-color var(--dur-1) var(--ease-out); }
```

Name the properties. `transition-all duration-300` (the Tailwind snippet in most generated components) animates every property that changes, including `height`, `padding` and `border-width`, which forces layout on every frame, and 300ms is twice the budget. Interfaces that respond in under 100ms read as direct; at 300ms the reader waits for the UI.

#### What may move

Motion is allowed when it tells the reader where something came from or that something is happening:

- A menu or popover appears near its trigger.
- A toast enters at the edge where it will stay.
- A caret rotates when a section expands.
- A progress bar fills, a spinner turns during a wait over 1 second. Show the spinner only after 400ms so fast requests never flash it, and pair it with text (`Saving…`).
- A row that was just added is marked with a static `--paper-3` background that clears after a few seconds. No pulsing.

Skeleton screens use static `--paper-2` blocks the shape of the content. The shimmering skeleton is an animated gradient and is banned twice over.

#### What never moves

```slop
<section data-aos="fade-up" data-aos-delay="200">...</section>
<motion.div initial={{ opacity: 0, y: 40 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }}>
<div class="animate-bounce">Scroll down</div>
<img class="animate-float" src="/blob.png">
<div class="bg-[length:200%_200%] animate-gradient bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500">
<h1><Typewriter words={["faster", "smarter", "better"]} loop cursor /></h1>
<span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-green-400 opacity-75"></span>
<div class="transition-transform duration-300 hover:scale-105">...</div>
```

- **Fade-up on scroll for every section** (AOS, Framer Motion `whileInView`, GSAP ScrollTrigger). Content is invisible until the script runs and the element enters the viewport. If the script fails, or a print, reader view or screenshot tool renders the page, the sections stay blank. Readers who scroll fast see empty space. This is the most common generated-page motion.
- **Floating** (`animate-bounce`, custom `float` keyframes that bob an image up and down). Endless motion in the reader's peripheral vision while they try to read.
- **Parallax**. Background and foreground scrolling at different speeds is a documented trigger for vestibular disorders, and it costs scroll performance on low-end phones.
- **Animated gradients**, moving glows, cursor-following spotlights on cards, shimmering borders, rotating conic borders.
- **Typing-effect headlines.** The headline is the one sentence that must be readable at once; a typewriter delays it and screen readers may announce partial words.
- **Confetti** (`canvas-confetti`) after sign-up or payment. A success message is text.
- **Count-up numbers** that roll from 0 to the value. The reader waits to read a number that was known at render.
- **Infinite logo marquees.** A moving row of customer logos cannot be read and cannot be paused without extra controls (WCAG 2.2.2 requires a pause for motion over 5 seconds).
- **Hover scale and tilt on cards** (`hover:scale-105`, 3D tilt libraries). The card is not more clickable for growing.
- **Pulsing status dots** (`animate-ping`). See 3.7.
- **Page transitions** over 150ms. If you use the View Transitions API, set the duration to 150ms or less and disable it under reduced motion.

#### Reduced motion

Respect `prefers-reduced-motion: reduce` globally, then again in JavaScript for anything scripted.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
}
```

The duration is 0.01ms rather than 0 so that code listening for `transitionend` and `animationend` still receives the event; to the eye it is instant.

```ts
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
export const motionOK = () => !reduce.matches;

el.scrollIntoView({ behavior: motionOK() ? "smooth" : "auto", block: "nearest" });
```

```tsx
import { MotionConfig } from "framer-motion";

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <MotionConfig reducedMotion="user" transition={{ duration: 0.15, ease: [0.2, 0, 0, 1] }}>
      {children}
    </MotionConfig>
  );
}
```

In Tailwind, put motion behind the `motion-safe:` variant: `motion-safe:transition-opacity motion-safe:duration-150`. Spinners under reduced motion become static text: `Loading…`.

### 3.10 Accessibility as design quality

Accessibility is part of the visual spec. A focus ring, a contrast ratio and a target size are design values with numbers, and generated UIs fail them in the same places every time.

#### Focus rings

```css
:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
:focus:not(:focus-visible) { outline: none; }

/* Inside a container that clips overflow, draw the ring inward */
.table-scroll :focus-visible, .tabs :focus-visible { outline-offset: -2px; }
```

- `--focus` is `--ink` in light mode and the light ink in dark mode: 16:1 against `--paper`, far past the 3:1 minimum for focus indicators.
- Never remove the outline without replacing it. `focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2`, the Tailwind default pattern, draws the ring with `box-shadow`, and forced-colors mode (Windows contrast themes) sets `box-shadow` to none. The ring vanishes for exactly the people who need it most. `outline` survives.
- With the 2px offset, the ring sits on `--paper` even around an accent button, so one ring style works on every control.
- Every interactive element shows the ring: links, buttons, inputs, tabs, table rows that open, scroll containers with `tabindex="0"`.

#### Contrast

| Pair | Ratio | Verdict |
| --- | --- | --- |
| `--ink` on `--paper` | 16.0:1 | body text |
| `--ink-2` on `--paper` | 8.4:1 | secondary text |
| `--ink-3` on `--paper` | 4.8:1 | metadata, placeholders; passes 4.5:1 |
| `--ink-3` on `--paper-2` | 4.4:1 | fails for small text: use `--ink-2` in table headers and code captions |
| `--accent` on `--paper` | 5.1:1 | accent text and links |
| `--accent-ink` on `--accent` | 5.5:1 | primary button label |
| `--rule` on `--paper` | 1.3:1 | decoration only |
| Tailwind `gray-400` on white | 2.5:1 | the generated placeholder color; fails |

Ratios use the WCAG 2 formula. Requirements: 4.5:1 for text under 24px (or under 18.66px bold), 3:1 for larger text, and 3:1 for the boundaries of controls and for focus indicators (WCAG 1.4.11).

The `--rule` line matters here. A text input whose only boundary is a 1px `--rule` border at 1.3:1 does not show where to type. Inputs, checkboxes, radios and select boxes use `--ink-3` for their border (4.8:1); `--rule` is for dividers between content.

```css
input, select, textarea { border: 1px solid var(--ink-3); background: var(--paper); border-radius: var(--radius); }
input::placeholder { color: var(--ink-3); opacity: 1; }
```

Firefox lowers placeholder opacity by default; `opacity: 1` keeps the measured ratio. Placeholders are hints, never labels.

#### Semantics

The visual layer sits on top of correct HTML. Generated components regularly ship `<div onClick>` buttons, headings chosen by size, and inputs without labels.

- Actions are `<button type="button">`; navigation is `<a href>`. A div with a click handler has no keyboard access, no role and no focus.
- One `h1` per page; heading levels do not skip. Pick the level by outline, the size by class (3.2).
- Landmarks: `header`, `nav` (with `aria-label` when there are several), `main` (one), `footer`.
- Every input has a visible `<label for>`. Help and error text connect through `aria-describedby`.
- Data tables use `<th scope>` and a `<caption>`.
- Async status messages ("Saved", "3 results") go in an `aria-live="polite"` region that exists before the message arrives.
- The `html` element carries the right `lang`.
- Color never carries meaning alone: errors have text and an icon, chart series have labels, required fields say "required".

```html
<div class="field">
  <label for="iban">IBAN</label>
  <input id="iban" name="iban" autocomplete="off" aria-describedby="iban-help iban-err" aria-invalid="true">
  <p id="iban-help" class="help">Starts with a two-letter country code.</p>
  <p id="iban-err" class="error">This IBAN has 21 characters; German IBANs have 22.</p>
</div>
<p class="sr-only" aria-live="polite" id="save-status"></p>
```

#### Skip link and visually hidden text

```html
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header>...</header>
  <main id="main" tabindex="-1">...</main>
</body>
```

```css
.skip-link {
  position: absolute;
  left: var(--space-8);
  top: var(--space-8);
  padding: var(--space-8) var(--space-12);
  background: var(--ink);
  color: var(--paper);
  border-radius: var(--radius);
  transform: translateY(-200%);
}
.skip-link:focus-visible { transform: none; }

.sr-only {
  position: absolute;
  width: 1px; height: 1px;
  margin: -1px; padding: 0;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}
```

#### Forced colors, zoom and text spacing

- Because depth in this system comes from borders, components keep their shape in forced-colors mode, where backgrounds and shadows are replaced. Check for borders set to `transparent`: they render in the system color, which is usually what you want for buttons.
- Use system colors for custom indicators in forced colors:

```css
@media (forced-colors: active) {
  .status svg { color: CanvasText; }
  .tab[aria-selected="true"] { outline: 2px solid Highlight; }
}
```

- The page must work at 200 percent zoom and with WCAG 1.4.12 text spacing (line height 1.5, letter spacing 0.12em, word spacing 0.16em). Never set fixed heights on boxes that hold text; use `min-height`.

#### Targets and reduced motion

Target sizes are in 3.6 (44px touch, 24px minimum). Reduced motion is in 3.9. Both are accessibility rules and design rules at once, and both are tested in review with numbers, not impressions.

### 3.11 Review checklist for Part 3

Run this before merging any UI change. Each line is a yes or no.

Type:

- [ ] One sans family, at most one serif for long-form, one mono. All through `--font-sans`, `--font-serif`, `--font-mono`.
- [ ] At most five font files, at most two preloaded, all self-hosted WOFF2 with a metric-matched fallback.
- [ ] Weights are 400 and 600 (500 only in dense apps). No 300 and below, no 700 and above.
- [ ] Every font size is on the scale: 12, 14, 16, 18, 21, 24, 32, 40, 56. Body is 16.
- [ ] Body line height 1.5; headings 1.15 to 1.25; all line heights on the 4px grid.
- [ ] Negative letter spacing only at 32px and above, never past -0.02em. Uppercase only on 12px labels.
- [ ] Prose at most 66ch wide. Headings balanced.
- [ ] Landing h1 at most 56px and a real sentence about the product.
- [ ] Tabular numerals in tables and changing numbers; numeric columns right-aligned.

Text:

- [ ] No centered paragraphs. No gradient text. No accent-colored words in headings.
- [ ] Curly quotes, the ellipsis character, non-breaking spaces before units, unambiguous dates in `<time>`.
- [ ] Links in text are underlined.
- [ ] No emoji anywhere: bullets, headings, status, buttons, toasts, commit messages.

Space and layout:

- [ ] Every spacing value is one of 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. No arbitrary values.
- [ ] Inner space is smaller than outer space on every screen. Labels sit closer to their own fields.
- [ ] Section spacing varies with the relationship between sections; not `py-24` everywhere.
- [ ] No nested cards. Grouping is done with space and 1px rules first.
- [ ] One shared left edge per column. No centered section headings over left-aligned content.
- [ ] No row of three equal icon cards. Splits are uneven where importance is uneven.
- [ ] Grid tracks use `minmax(0, 1fr)`. Data screens use the full window width.

Responsive:

- [ ] Works at 320px with no horizontal page scroll. Breakpoints in em, two or three of them.
- [ ] Touch targets 44px; nothing under 24px anywhere.
- [ ] Tables keep their columns and scroll in a labeled, focusable container.
- [ ] Nav with five or fewer links is not collapsed; larger navs use a plain disclosure.

Icons and images:

- [ ] One icon set, stroke 1.5px, 16 or 20px, `currentColor`, `aria-hidden` when beside text.
- [ ] No icons in colored circles or squares. No icon before every heading.
- [ ] Real screenshots with realistic data, 1px border, no shadow, no tilt, no fake browser chrome.
- [ ] No 3D blobs, isometric stock, AI-generated images or background glows.
- [ ] Every image has width, height and useful alt text.

Motion and access:

- [ ] Every transition is 150ms or less, names its properties, and animates only opacity and transform.
- [ ] No scroll-triggered reveals, floating, parallax, typing effects, confetti, count-ups, marquees or pulsing dots.
- [ ] Reduced motion stops everything.
- [ ] Focus ring is the canonical outline on every interactive element.
- [ ] Text contrast at least 4.5:1; control borders at least 3:1.
- [ ] Real buttons, real links, labeled inputs, one `main`, a skip link.

A quick search catches most violations in a Tailwind codebase:

```bash
rg -n --glob '*.{tsx,jsx,html,vue,svelte}' \
  -e 'text-(5xl|6xl|7xl|8xl|9xl)' -e 'font-(light|extrabold|black)' \
  -e 'tracking-tight' -e 'bg-clip-text' -e '\bshadow' \
  -e 'animate-(bounce|ping|pulse)' -e 'whileInView' -e 'data-aos' \
  -e 'duration-(300|500|700|1000)' -e 'transition-all' \
  -e '\[[0-9]+px\]' -e 'rounded-(xl|2xl|3xl)' -e 'focus:outline-none'
```

Each hit is a question for the author, not an automatic fix. Most will be replaced by a token from this Part.
