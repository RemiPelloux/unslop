#### Toast with Sonner

```tsx
// components/ui/sonner.tsx
"use client";
import { Toaster as Sonner } from "sonner";

export function Toaster() {
  return (
    <Sonner
      position="bottom-right"
      duration={6000}
      visibleToasts={3}
      icons={{ success: null, info: null, warning: null, error: null }}
      toastOptions={{
        unstyled: true,
        classNames: {
          toast: "flex w-[356px] items-start gap-3 rounded-sm border border-rule-strong bg-paper p-4 text-sm text-ink",
          title: "font-medium",
          description: "mt-1 text-ink-2",
          actionButton: "ml-auto h-8 rounded-sm border border-ink px-3 font-medium hover:bg-paper-3",
          cancelButton: "h-8 px-2 text-ink-2 underline",
          error: "border-l-4 border-l-bad",
          warning: "border-l-4 border-l-warn",
          success: "border-l-4 border-l-ok",
        },
      }}
    />
  );
}
```

`unstyled: true` drops Sonner's built-in card styles, which include a shadow and an 8px radius. The default icons are set to `null`; the 4px left rule and the words carry the state. Duration goes from 4000ms to 6000ms because a toast with an Undo action needs time to read and reach. Never use `richColors`, which fills the toast with saturated green or red.

#### Input

```tsx
// components/ui/input.tsx
import * as React from "react";
import { cn } from "@/lib/utils";

export const Input = React.forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(
  ({ className, type = "text", ...props }, ref) => (
    <input
      ref={ref}
      type={type}
      className={cn(
        "flex h-10 w-full rounded-sm border border-ink-3 bg-paper px-3 text-base text-ink",
        "placeholder:text-ink-3",
        "focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus",
        "disabled:cursor-not-allowed disabled:bg-paper-2 disabled:text-ink-3",
        "aria-[invalid=true]:border-bad",
        "file:mr-3 file:border-0 file:bg-transparent file:text-sm file:font-medium",
        className,
      )}
      {...props}
    />
  ),
);
Input.displayName = "Input";
```

Height goes from 36px to 40px, which matches the button and clears the 24px minimum target in WCAG 2.5.8 with room for touch. The text is 16px at every breakpoint; below 16px, iOS Safari zooms the page when the field gets focus. Invalid state shows through `aria-invalid`, which screen readers also announce, so the visual and the semantic state cannot drift apart.

#### Leave the rest, then check

Components not listed here (Tabs, Select, Popover, Tooltip, Sheet, Command) carry the same `shadow-md rounded-md` pattern and the same zoom entrances. Apply the same four substitutions: border for shadow, `rounded-sm` for anything larger, outline for ring, no entrance animation. Then run the class check from 6.6 across `components/ui`. A run with zero findings is the definition of done.

### 6.5 Design tokens as data

Keep one source for the tokens and generate the CSS, the Tailwind values and the TypeScript constants from it. The shape below is Style Dictionary's: nested objects, each leaf holding `value`, `type`, and an optional `comment`. Keys are the canonical names, so the generated CSS variables match 6.1 exactly (`--paper-2`, not `--color-paper-2`).

#### Token files

```json
// tokens/base.json
{
  "radius": { "value": "2px", "type": "dimension", "comment": "0 or 2px. Never above 4px." },
  "font-sans": { "value": "\"IBM Plex Sans\", system-ui, -apple-system, \"Segoe UI\", sans-serif", "type": "fontFamily" },
  "font-serif": { "value": "\"Source Serif 4\", Georgia, \"Times New Roman\", serif", "type": "fontFamily" },
  "font-mono": { "value": "\"IBM Plex Mono\", ui-monospace, \"SFMono-Regular\", Menlo, monospace", "type": "fontFamily" },
  "s1": { "value": "4px" }, "s2": { "value": "8px" }, "s3": { "value": "12px" },
  "s4": { "value": "16px" }, "s5": { "value": "24px" }, "s6": { "value": "32px" },
  "s7": { "value": "48px" }, "s8": { "value": "64px" }, "s9": { "value": "96px" },
  "s10": { "value": "128px" },
  "t": {
    "12": { "value": "12px" }, "14": { "value": "14px" }, "16": { "value": "16px" },
    "18": { "value": "18px" }, "21": { "value": "21px" }, "24": { "value": "24px" },
    "32": { "value": "32px" }, "40": { "value": "40px" }, "56": { "value": "56px" }
  },
  "measure": { "value": "66ch", "type": "dimension" },
  "dur": { "value": "120ms", "type": "duration", "comment": "0 to 150ms, ease-out" }
}
```

```json
// tokens/color.light.json
{
  "paper": { "value": "#F7F5F0", "type": "color" },
  "paper-2": { "value": "#EFECE4", "type": "color" },
  "paper-3": { "value": "#E5E1D6", "type": "color" },
  "ink": { "value": "#1A1A18", "type": "color" },
  "ink-2": { "value": "#4A4843", "type": "color" },
  "ink-3": { "value": "#6F6C64", "type": "color" },
  "rule": { "value": "#D9D5CB", "type": "color" },
  "rule-strong": { "value": "#1A1A18", "type": "color" },
  "accent": { "value": "#B4441C", "type": "color" },
  "accent-ink": { "value": "#FFFFFF", "type": "color" },
  "ok": { "value": "#2F6B3A", "type": "color" },
  "warn": { "value": "#8A6100", "type": "color" },
  "bad": { "value": "#A3271F", "type": "color" },
  "focus": { "value": "#1A1A18", "type": "color" }
}
```

```json
// tokens/color.dark.json
{
  "paper": { "value": "#141412", "type": "color" },
  "paper-2": { "value": "#1E1D1A", "type": "color" },
  "paper-3": { "value": "#2A2925", "type": "color" },
  "ink": { "value": "#ECE9E1", "type": "color" },
  "ink-2": { "value": "#B5B1A7", "type": "color" },
  "ink-3": { "value": "#8F8B81", "type": "color" },
  "rule": { "value": "#34322E", "type": "color" },
  "rule-strong": { "value": "#ECE9E1", "type": "color" },
  "accent": { "value": "#E2703F", "type": "color" },
  "accent-ink": { "value": "#141412", "type": "color" },
  "ok": { "value": "#7FB38A", "type": "color" },
  "warn": { "value": "#D9A93A", "type": "color" },
  "bad": { "value": "#E0705F", "type": "color" },
  "focus": { "value": "#ECE9E1", "type": "color" }
}
```

Strip the `//` filename lines before saving; JSON has no comments.

#### Build config

```js
// sd.config.mjs (Style Dictionary 4)
import StyleDictionary from "style-dictionary";

// Values are already final CSS. The only transform is the name.
const css = (destination, selector) => ({
  transforms: ["name/kebab"],
  buildPath: "build/",
  files: [{ destination, format: "css/variables", options: { selector, outputReferences: false } }],
});

const light = new StyleDictionary({
  source: ["tokens/base.json", "tokens/color.light.json"],
  platforms: {
    css: css("tokens.css", ":root"),
    js: {
      transforms: ["name/camel"],
      buildPath: "build/",
      files: [
        { destination: "tokens.js", format: "javascript/es6" },
        { destination: "tokens.d.ts", format: "typescript/es6-declarations" },
      ],
    },
  },
});

const dark = new StyleDictionary({
  source: ["tokens/color.dark.json"],
  platforms: { css: css("tokens-dark.css", ':root[data-theme="dark"]') },
});

await light.buildAllPlatforms();
await dark.buildAllPlatforms();
```

The default `css` transform group includes `size/rem`, which rewrites `16px` as `1rem` and fails on values like `66ch`. Listing transforms explicitly avoids both. If a token ever needs a computed value, add the transform for that one type instead of switching groups.

#### CSS-in-JS

Do not copy hex values into a JavaScript theme object. A `ThemeProvider` that swaps objects re-renders the whole tree on a theme change and duplicates the source of truth. Reference the CSS variables instead, and let `data-theme` on the root element do the switching.

```ts
// src/tokens.ts
const v = (name: string) => `var(--${name})` as const;

export const t = {
  color: {
    paper: v("paper"), paper2: v("paper-2"), paper3: v("paper-3"),
    ink: v("ink"), ink2: v("ink-2"), ink3: v("ink-3"),
    rule: v("rule"), ruleStrong: v("rule-strong"),
    accent: v("accent"), accentInk: v("accent-ink"),
    ok: v("ok"), warn: v("warn"), bad: v("bad"), focus: v("focus"),
  },
  space: { 1: "4px", 2: "8px", 3: "12px", 4: "16px", 5: "24px", 6: "32px", 7: "48px", 8: "64px", 9: "96px", 10: "128px" },
  text: { xs: "12px", sm: "14px", base: "16px", lg: "18px", xl: "21px", "2xl": "24px", "3xl": "32px", "4xl": "40px", "5xl": "56px" },
  font: { sans: v("font-sans"), serif: v("font-serif"), mono: v("font-mono") },
  radius: "2px",
  measure: "66ch",
  focusRing: { outline: `2px solid ${v("focus")}`, outlineOffset: "2px" },
  motion: { duration: "120ms", easing: "ease-out" },
} as const;
```

```tsx
// Panel.tsx (styled-components or Emotion, same syntax)
import styled from "styled-components";
import { t } from "./tokens";

export const Panel = styled.section`
  background: ${t.color.paper2};
  border: 1px solid ${t.color.rule};
  border-radius: ${t.radius};
  padding: ${t.space[5]};

  & + & {
    margin-top: ${t.space[4]};
  }

  &:focus-within {
    border-color: ${t.color.ruleStrong};
  }
`;
```

The `space` and `text` maps are literal pixel values because they never change by theme. Colors and fonts are variable references because they do. The key names (`paper2`, `ink3`) follow camelCase for JavaScript; the variable names stay kebab-case so the CSS and the JavaScript point at the same custom property.

### 6.6 Lint rules that enforce it

Three layers: stylelint for stylesheets, ESLint for JSX, and a dependency-free Node script that runs on any file type in CI. All three read the same lexicon file, `banned-words.txt` (one entry per line, `#` for comments; Part 7 holds the full list).

#### stylelint

```json
{
  "extends": ["stylelint-config-standard"],
  "rules": {
    "property-disallowed-list": [
      "text-shadow",
      "backdrop-filter",
      "-webkit-backdrop-filter"
    ],
    "declaration-property-value-allowed-list": {
      "box-shadow": ["none"],
      "transition-property": ["/^(none|opacity|transform)(,\\s*(opacity|transform))*$/"],
      "/^border(-(top|bottom)-(left|right))?-radius$/": ["0", "2px", "4px", "50%", "/^var\\(--radius\\)$/"]
    },
    "function-disallowed-list": [
      "linear-gradient",
      "radial-gradient",
      "conic-gradient",
      "repeating-linear-gradient",
      "repeating-radial-gradient",
      "repeating-conic-gradient",
      "drop-shadow"
    ],
    "declaration-property-value-disallowed-list": {
      "/^(transition|transition-duration|animation|animation-duration)$/": [
        "/\\b(15[1-9]|1[6-9]\\d|[2-9]\\d{2}|\\d{4,})ms\\b/",
        "/\\b\\d*\\.?\\d+s\\b/",
        "/\\ball\\b/"
      ],
      "/color|background|border|fill|stroke|outline/": [
        "/#(6366f1|4f46e5|4338ca|818cf8|8b5cf6|7c3aed|6d28d9|a78bfa|a855f7|9333ea|7e22ce|c084fc|d946ef|c026d3)\\b/i"
      ]
    },
    "color-named": "never"
  }
}
```

- `box-shadow` may only be `none`. The other three properties are banned outright.
- `function-disallowed-list` catches every gradient function, including ones hidden in `border-image` or `mask`, and the `drop-shadow` filter.
- Durations must be written in milliseconds and stay at or under 150ms; the seconds form (`0.3s`) is rejected because it hides 300ms in a shape that reads short. `transition: all` is rejected.
- The hex list holds the 400 to 700 steps of Tailwind's `indigo`, `violet`, `purple` and `fuchsia`. These are the values that leak in when someone pastes from a Tailwind UI snippet that was compiled to plain CSS.
- The radius list allows `50%` for avatars and radio buttons. Grep for `50%` in review and confirm each use is one of those two.

#### Shared lexicon and class rules

```js
// scripts/unslop-rules.mjs
import fs from "node:fs";

export const EMOJI =
  /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{2190}-\u{21FF}\u{2300}-\u{23FF}\u{FE0F}\u{200D}\u{20E3}]/u;

function forms(w) {
  if (w.includes(" ")) return [w];
  const out = new Set([w]);
  for (const s of ["s", "es", "d", "ed", "ing", "ly", "er", "ers", "est", "ment", "ness"]) out.add(w + s);
  if (w.endsWith("e")) for (const s of ["ing", "ingly", "ely"]) out.add(w.slice(0, -1) + s);
  if (w.endsWith("y")) for (const s of ["ies", "ied", "ily", "ier", "iest"]) out.add(w.slice(0, -1) + s);
  if (w.endsWith("ize")) for (const s of ["ization", "ise", "ised", "ising", "isation"]) out.add(w.slice(0, -3) + s);
  return [...out];
}

const esc = (s) =>
  s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&").replace(/-/g, "[-\\s]+").replace(/ /g, "\\s+").replace(/'/g, "['\u2019]");

export function loadLexicon(file = new URL("../banned-words.txt", import.meta.url)) {
  const entries = fs.readFileSync(file, "utf8")
    .split("\n").map((l) => l.trim().toLowerCase()).filter((l) => l && !l.startsWith("#"));
  const alts = entries.flatMap(forms).sort((a, b) => b.length - a.length).map(esc);
  return new RegExp(`(?<![A-Za-z0-9])(?:${alts.join("|")})(?![A-Za-z0-9])`, "i");
}

// Tailwind classes. "s[h]adow" is spelled with a character class so this
// file passes its own check.
const V = "(?:^|\\s)(?:[\\w\\[\\]=&-]+:)*";
export const CLASS_RULES = [
  [new RegExp(V + "(?:inset-|drop-|text-)?s[h]adow(?:-(?!none(?:\\s|$))\\S+)?(?=\\s|$)"), "Shadow utility"],
  [new RegExp(V + "bg-(?:gradient|linear|radial|conic)\\b"), "gradient utility"],
  [new RegExp(V + "(?:from|via|to)-\\S+"), "gradient color stop"],
  [new RegExp(V + "backdrop-\\S+"), "backdrop filter utility"],
  [new RegExp(V + "ring(?:-\\S+)?(?=\\s|$)"), "Ring utility (box-shadow based); use outline"],
  [new RegExp(V + "rounded(?:-[trblse]{1,2})?-(?:lg|xl|2xl|3xl|full)(?=\\s|$)"), "radius above 4px"],
  [new RegExp(V + "animate-(?:ping|pulse|bounce)\\b"), "attention animation"],
  [new RegExp(V + "\\w+-(?:indigo|violet|purple|fuchsia)-\\d{2,3}\\b"), "indigo/violet/purple palette"],
  [new RegExp(V + "duration-(?:15[1-9]|1[6-9]\\d|[2-9]\\d{2}|\\d{4,})\\b"), "duration over 150ms"],
  [new RegExp(V + "transition-all\\b"), "transition-all"],
];

export const CSS_RULES = [
  [/box-shadow\s*:\s*(?!none\b)/i, "box-shadow"],
  [/text-shadow\s*:\s*(?!none\b)/i, "text-shadow"],
  [/drop-shadow\s*\(/i, "drop-shadow filter"],
  [/(?:repeating-)?(?:linear|radial|conic)-gradient\s*\(/i, "CSS gradient"],
  [/backdrop-filter\s*:\s*(?!none\b)/i, "backdrop-filter"],
];

export function checkClasses(str) {
  return CLASS_RULES.filter(([re]) => re.test(str)).map(([, msg]) => msg);
}
```

#### ESLint

```js
// eslint.config.js (flat config, ESLint 9)
import tseslint from "typescript-eslint";
import { EMOJI, loadLexicon, checkClasses } from "./scripts/unslop-rules.mjs";

const BANNED = loadLexicon();
const COPY_ATTRS = new Set(["alt", "title", "placeholder", "aria-label", "aria-description", "label", "description"]);

const unslop = {
  rules: {
    copy: {
      meta: { type: "problem", schema: [] },
      create(context) {
        const check = (node, text) => {
          if (EMOJI.test(text)) context.report({ node, message: "Emoji in user-facing text." });
          const m = text.match(BANNED);
          if (m) context.report({ node, message: `Banned word "${m[0]}" in user-facing text.` });
          if (/!(\s|$)/.test(text)) context.report({ node, message: "Exclamation mark in user-facing text." });
        };
        return {
          JSXText(node) { check(node, node.value); },
          JSXAttribute(node) {
            const name = node.name.name;
            const v = node.value;
            if (!v) return;
            const str = v.type === "Literal" ? v.value
              : v.expression?.type === "Literal" ? v.expression.value
              : v.expression?.type === "TemplateLiteral" ? v.expression.quasis.map((q) => q.value.cooked).join(" ")
              : null;
            if (typeof str !== "string") return;
            if (name === "className" || name === "class") {
              for (const msg of checkClasses(str)) context.report({ node, message: `Class rule: ${msg}.` });
            } else if (COPY_ATTRS.has(name)) {
              check(node, str);
            }
          },
        };
      },
    },
    classes: {
      meta: { type: "problem", schema: [] },
      create(context) {
        return {
          // cn("..."), cva("...", { variants }), clsx("...")
          "CallExpression[callee.name=/^(cn|cva|clsx|twMerge)$/] Literal"(node) {
            if (typeof node.value !== "string") return;
            for (const msg of checkClasses(node.value)) context.report({ node, message: `Class rule: ${msg}.` });
          },
        };
      },
    },
  },
};

export default tseslint.config(
  ...tseslint.configs.recommended,
  {
    files: ["**/*.{jsx,tsx}"],
    plugins: { unslop },
    rules: { "unslop/copy": "error", "unslop/classes": "error" },
  },
);
```

The `copy` rule reads JSX text and the attributes a person sees or hears. It does not read every string literal, because error codes and analytics event names would produce noise. Strings that live in a locale file are covered by the Node script below.

#### Node script for CI

```js
#!/usr/bin/env node
// scripts/unslop-check.mjs. Usage: node scripts/unslop-check.mjs src content locales
import fs from "node:fs";
import path from "node:path";
import { EMOJI, loadLexicon, checkClasses, CSS_RULES } from "./unslop-rules.mjs";

const BANNED = loadLexicon();
const SKIP = new Set(["node_modules", ".git", "dist", "build", ".next", "coverage"]);
const problems = [];

function walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (SKIP.has(e.name)) continue;
    const p = path.join(dir, e.name);
    e.isDirectory() ? walk(p) : checkFile(p);
  }
}

function copyFrom(line, ext) {
  if (ext === ".json") return [...line.matchAll(/:\s*"((?:[^"\\]|\\.)*)"/g)].map((m) => m[1]);
  if ([".md", ".mdx", ".txt"].includes(ext)) return [line.replace(/`[^`]*`/g, " ")];
  const text = [...line.matchAll(/>([^<>{}]+)</g)].map((m) => m[1]);
  const attrs = [...line.matchAll(/\b(?:alt|title|placeholder|aria-label|label)=["']([^"']+)["']/g)].map((m) => m[1]);
  return [...text, ...attrs];
}

function checkFile(file) {
  const ext = path.extname(file);
  const markup = [".html", ".jsx", ".tsx", ".vue", ".svelte", ".astro"].includes(ext);
  const styles = [".css", ".scss", ".less"].includes(ext) || markup;
  const copy = markup || [".md", ".mdx", ".txt", ".json"].includes(ext);
  if (!styles && !copy) return;

  let fence = false;
  fs.readFileSync(file, "utf8").split("\n").forEach((line, i) => {
    const at = `${file}:${i + 1}`;
    if (/^\s*(```|~~~)/.test(line)) { fence = !fence; return; }
    if (EMOJI.test(line)) problems.push(`${at}: emoji`);
    if (styles) for (const [re, msg] of CSS_RULES) if (re.test(line)) problems.push(`${at}: ${msg}`);
    if (markup) {
      for (const m of line.matchAll(/\bclass(?:Name)?=["'`]([^"'`]+)["'`]/g)) {
        for (const msg of checkClasses(m[1])) problems.push(`${at}: ${msg}`);
      }
    }
    if (copy && !fence) {
      for (const s of copyFrom(line, ext)) {
        const m = s.match(BANNED);
        if (m) problems.push(`${at}: banned word "${m[0]}"`);
      }
    }
  });
}

for (const target of process.argv.slice(2)) {
  fs.statSync(target).isDirectory() ? walk(target) : checkFile(target);
}
for (const p of problems) console.log(p);
console.log(`${problems.length} problems`);
process.exit(problems.length ? 1 : 0);
```

Wire all three into `package.json` and run them in CI on every pull request:

```json
{
  "scripts": {
    "lint:css": "stylelint \"src/**/*.{css,scss}\"",
    "lint:js": "eslint .",
    "lint:unslop": "node scripts/unslop-check.mjs src content locales",
    "lint": "npm run lint:css && npm run lint:js && npm run lint:unslop"
  }
}
```

### 6.7 Instructions for coding agents

Paste the block below into the file your agent reads on every task. Then paste the word list under it. The block is about 600 words, which fits comfortably in a system prompt; longer versions get skimmed by models the same way they get skimmed by people.

- Claude Code: `CLAUDE.md` at the repository root.
- Codex and other agents that follow the convention: `AGENTS.md` at the root.
- Cursor: `.cursor/rules/unslop.mdc`, with front matter `alwaysApply: true` and `globs: ["**/*.{tsx,jsx,html,css,md,mdx}"]`. The older single `.cursorrules` file still works.
- GitHub Copilot: `.github/copilot-instructions.md`.

```text
# Interface and copy rules (UNSLOP)

Follow these in every file you create or edit. If the task explicitly asks
for something these rules forbid, do it, and say which rule you broke.

Visual
- No box-shadow, text-shadow, drop-shadow filter, or Tailwind shadow-*
  utility except shadow-none. Separate layers with a 1px border
  (var(--rule)) and a background step: --paper, --paper-2, --paper-3.
- No gradients of any kind. No linear-gradient, radial-gradient,
  conic-gradient, Tailwind bg-linear, bg-gradient, from-, via-, to- classes,
  gradient text, or glow behind a hero.
- No backdrop-filter, glass panels, blur, neon, or animated borders.
- Radius is 0 or 2px, never above 4px. Circles only for avatars and radios.
- Colors come from the tokens in unslop-base.css or the Tailwind config.
  Never indigo, violet, purple, fuchsia or blue for brand, buttons or links.
  One accent color per screen, on the one primary action.
- Fonts: IBM Plex Sans for interface, IBM Plex Mono for code and figures,
  Source Serif 4 for long reading. Sizes 12 14 16 18 21 24 32 40 56px.
  Body 16px, line height 1.5, lines at most 66ch.
- Spacing 4 8 12 16 24 32 48 64 96 128px. Nothing else.
- Focus: outline 2px solid var(--focus), offset 2px. Never Tailwind ring-* utilities.
  Never remove the outline without a visible replacement.
- Motion: 150ms or less, ease-out, opacity and transform only, nothing under
  prefers-reduced-motion. No scroll reveals. No animate-ping, animate-pulse,
  animate-bounce.
- Icons: one SVG set, 1.5px stroke, 16 or 20px. No emoji anywhere: interface,
  copy, code comments, commit messages, docs.
- No status pills, no dots. No "LIVE", "New", "Beta" capsules. Write the
  state and the time: "Deployed 14:02 UTC".
- Left-align. Center only one short line.
- Do not put every section in a card. Use a top rule and spacing. A box is
  for a thing the user acts on as a unit.

Copy
- First line says what the product does and for whom, in words a customer
  uses. Then show it: screenshot, code sample, or a number with unit and date.
- Buttons name the action: "Create invoice", "Install CLI", "Delete 3 files".
  Never "Get started", "Learn more", "Submit" when a specific verb exists.
- Headings label content: "Pricing", "Install", "Limits".
- No exclamation marks, no em dashes, no rhetorical questions, no
  "Introducing", no "Welcome back" banners, no "Trusted by 10,000+ teams".
- Every number has a unit, a source or a date. Delete numbers you cannot source.
- Testimonials need a full name, role, company and date, or they go.
- Never use the words in the list below, in any form. If a sentence needs
  one, it has no claim in it: write the claim or delete the sentence.

Before you finish
- Run: npm run lint (stylelint, eslint, scripts/unslop-check.mjs).
- Report the output. Do not claim compliance you did not check.
```

The word list, to paste directly under the block. These are the 148 entries agents produce most often; the other 202 are in Part 7 and in `banned-words.txt`, which the lint script reads.

```slop
Banned words (any form):
delve, leverage, utilize, harness, unlock, unleash, elevate, empower,
streamline, revolutionize, supercharge, embark, navigate, foster, cultivate,
underscore, showcase, spearhead, bolster, amplify, reimagine, redefine,
reshape, curate, embrace, enhance, enrich, facilitate, optimize, maximize,
democratize, future-proof, unpack, immerse, captivate, ignite, propel,
skyrocket, boost, fuel, encompass, embody, thrive, garner, boast, elucidate,
disrupt, level up, dive into, deep dive, lean into, reach out, weave,
orchestrate, seamless, robust, comprehensive, cutting-edge, innovative,
groundbreaking, game-changing, transformative, revolutionary, pivotal,
crucial, vital, essential, paramount, intricate, nuanced, holistic, dynamic,
vibrant, meticulous, unparalleled, compelling, stunning, remarkable,
exceptional, invaluable, intuitive, user-friendly, frictionless, effortless,
delightful, sleek, elegant, modern, next-gen, state-of-the-art, world-class,
best-in-class, enterprise-grade, powerful, premium, bespoke, tailored,
immersive, engaging, impactful, actionable, insightful, diverse, vast,
crisp, clean, beautiful, magical, cohesive, granular, ai-powered,
data-driven, end-to-end, all-in-one, unified, curated, handcrafted,
tapestry, testament, realm, landscape, journey, ecosystem, paradigm,
synergy, game-changer, insight, superpower, solution, innovation, magic,
furthermore, moreover, additionally, ultimately, essentially, indeed, truly,
in today's, the power of, the future of, with ease, made simple,
take your, when it comes to, whether you're, more than just, look no further
```
