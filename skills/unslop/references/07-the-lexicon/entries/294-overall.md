From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 294. `overall`

- Kind: adverb, adjective. Banned forms: `overall`, `Overall,`, `overall experience`, `overall performance`.
- Why it reads as machine text: `Overall,` opens the summary sentence of a generated paragraph, the one that restates the paragraph at lower resolution. As an adjective (`overall experience`) it claims to cover everything and so names nothing. Model reviews and reports end almost every section with it.
- Where it shows up: the last sentence of a paragraph, review verdicts, and performance reports.

```slop
Overall, the migration went smoothly.
The overall user experience has improved significantly.
Overall performance is good, with a few exceptions.
```

Replace with:

- The result with its measure: "The migration finished in 4 hours with no downtime."
- The specific parts that changed, by name.
- The exceptions first, since they are the news.
- Cut it when the paragraph already made the point.

Rewrites:

```slop
Overall, the migration went smoothly.
```

After: The migration finished in 4 hours, 2 under the window, with no failed writes.

```slop
The overall user experience has improved significantly.
```

After: Search now returns in 200ms and the settings page loads without a spinner.

```slop
Overall performance is good, with a few exceptions.
```

After: Every page loads under 1s except Reports (3.2s) and Billing (2.6s).

- Literal use: for a total dimension in a spec, write "total width" or "outer width" and give the value: "outer width 1,280px".
