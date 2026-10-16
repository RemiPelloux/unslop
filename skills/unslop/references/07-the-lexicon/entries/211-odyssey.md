From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 211. `odyssey`

- Kind: noun. Banned forms: `odyssey`, `odysseys`.
- Why it reads as machine text: Models reach for `odyssey` when a prompt asks for a "story" or a "case study", because it is the grandest synonym for a long process in their training data. It dresses a three-week migration or a debugging session as Homer, which tells the reader the writer cared more about tone than about the timeline. The word also hides the length: no start date, no end date, no count of steps.
- Where it shows up: founder letters and about pages, case-study intros, blog posts that recap a migration or a bug hunt.

```slop
Our odyssey from a monolith to microservices taught us more than any textbook.
Join us on an odyssey through the history of the CSS box model.
What began as a simple bug fix became a three-week odyssey into the depths of our build pipeline.
```

Replace with:

- "migration", "rewrite", "project" when the thing is a piece of work with a scope.
- A date range ("from March to June 2024") when the length is the point.
- "history" when the text walks through past events in order.
- Cut it when the sentence works with the plain noun alone; "our move to microservices" says the same thing.

Rewrites:

```slop
Our odyssey from a monolith to microservices taught us more than any textbook.
```

After: Moving from one Rails app to 14 services took 11 months; these are the 6 mistakes that cost us the most time.

```slop
Join us on an odyssey through the history of the CSS box model.
```

After: This post traces the CSS box model from CSS1 in 1996 to `box-sizing` in CSS3.

```slop
What began as a simple bug fix became a three-week odyssey into the depths of our build pipeline.
```

After: A one-line bug fix took three weeks because the build cache kept serving the old bundle.

- Literal use: for Homer's poem, name it in inline code (`Odyssey`) or write "Homer's poem about Odysseus".
