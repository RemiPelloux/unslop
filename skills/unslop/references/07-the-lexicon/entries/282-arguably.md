From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 282. `arguably`

- Kind: adverb. Banned forms: `arguably`, `arguably the best`, `arguably one of`.
- Why it reads as machine text: `arguably` lets a model make a ranking claim and withdraw it in the same word. It signals that an argument exists without making it. Model output pairs it with superlatives (`arguably the most popular`) because the training data rewards confident tone and penalizes unsupported claims, and this word satisfies both.
- Where it shows up: framework comparisons, "top 10" listicles, and the opening line of a README that ranks its own project.

```slop
Postgres is arguably the best open-source database available today.
This is arguably one of the most important changes in the release.
Tailwind is arguably the fastest way to style a React app.
```

Replace with:

- The evidence for the ranking: a benchmark, a download count, a survey with its year.
- "I think" or "We picked X because" when the claim is an opinion and the reader should know whose.
- A narrower true claim in place of the superlative: "the only one of the three with X".
- Cut it when you cannot name the argument; then the ranking goes too.

Rewrites:

```slop
Postgres is arguably the best open-source database available today.
```

After: We picked Postgres over MySQL for its JSONB indexes and row-level security.

```slop
This is arguably one of the most important changes in the release.
```

After: This change removes the 30-second lock on large tables during migration.

```slop
Tailwind is arguably the fastest way to style a React app.
```

After: With Tailwind we style a component without opening a second file; the tradeoff is long class strings.

- Literal use: in legal or academic text where a position can be argued, write "one could argue X, because Y" and supply Y.
