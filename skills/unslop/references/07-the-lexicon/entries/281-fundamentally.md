From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 281. `fundamentally`

- Kind: adverb. Banned forms: `fundamentally`, sentence-initial `Fundamentally,`.
- Why it reads as machine text: Models put `fundamentally` in front of a definition to make it sound deeper than it is, as in `X is fundamentally about Y`. The sentence that follows is usually a paraphrase of the topic name, so the word adds pitch and no fact. Generated explainers open section after section this way.
- Where it shows up: the first line of an explainer section, the "Overview" of an architecture doc, and pitch copy about what a product is.

```slop
React is fundamentally a library for building user interfaces.
Fundamentally, caching is about trading memory for speed.
The outage was fundamentally a problem of ownership between two teams.
```

Replace with:

- A direct definition with a verb that does work: "renders", "stores", "blocks". Use it when the sentence defines a thing.
- The cause, named: "The cause was X." Use it when you separate a symptom from its source.
- A number that shows the tradeoff, when the sentence claims one.
- Cut it when the sentence stays true without it, which is nearly always.

Rewrites:

```slop
React is fundamentally a library for building user interfaces.
```

After: React renders a UI tree from component state and patches the DOM when that state changes.

```slop
Fundamentally, caching is about trading memory for speed.
```

After: The cache keeps 2 GB of query results in memory so repeat requests skip a 40ms database call.

```slop
The outage was fundamentally a problem of ownership between two teams.
```

After: Neither team owned the billing webhook, so nobody fixed it when it began failing on 3 March.

- Literal use: for the physics or music term, write "fundamental frequency"; it names a measured quantity and is not an intensifier.
