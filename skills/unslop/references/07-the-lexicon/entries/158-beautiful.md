From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 158. `beautiful`

- Kind: adjective. Banned forms: `beautiful`, `beautifully`.
- Why it reads as machine text: Models use it as the default praise for dashboards, docs, charts and code (`beautiful dashboards`, `beautifully designed`). It is a taste claim no one can test, and on landing pages it usually sits beside a purple gradient hero and a mockup tilted 12 degrees. It hides what the reader would see.
- Where it shows up: hero headlines, README taglines, design feedback.

```slop
Beautiful dashboards in minutes.
Beautifully designed, built for developers.
This chart is beautiful, ship it.
```

Replace with:

- What the thing shows, and how long it takes: "Revenue, churn and runway on one page, from your Stripe data, in about 5 minutes."
- The design decisions: typeface, palette, smallest supported width.
- For review, the property that works: labels, axis, color use.
- Cut it when a screenshot sits next to the sentence. The screenshot is the evidence.

Rewrites:

```slop
Beautiful dashboards in minutes.
```

After: Revenue, churn and runway on one page, built from your Stripe data in about 5 minutes.

```slop
Beautifully designed, built for developers.
```

After: Set in IBM Plex, one accent color, keyboard shortcuts for every action, and a layout that works at 320px.

```slop
This chart is beautiful, ship it.
```

After: Direct labels instead of a legend, and the y axis starts at zero. Approve.

- Literal use: for the Python HTML parser, write `BeautifulSoup` in inline code; for a person or a place, describe what you saw.
