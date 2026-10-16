From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 276. `notably`

- Kind: adverb, connective. Banned forms: `notably`, `most notably`.
- Why it reads as machine text: `notably` tells the reader that the next item matters more than the others without saying why. Models use it to introduce an example or to fake emphasis. When every paragraph has one, the reader can no longer tell what deserves attention.
- Where it shows up: summaries, comparison posts, release notes.

```slop
Several large companies use it, notably two of the biggest US banks.
Notably, the update includes a new caching layer.
The model performed well, most notably on reasoning tasks.
```

Replace with:

- "including" or "such as" for examples.
- Why it matters: "the cache halves p95 latency".
- The most important item placed first, with no adverb.
- Cut it when the sentence works without it, which is nearly always.

Rewrites:

```slop
Several large companies use it, notably two of the biggest US banks.
```

After: About 300 companies use it in production, including two of the five largest US banks.

```slop
Notably, the update includes a new caching layer.
```

After: The update adds a caching layer that cuts p95 latency from 200 ms to 90 ms.

```slop
The model performed well, most notably on reasoning tasks.
```

After: The model scored highest on the reasoning tasks, 71% against a 58% average.

- Literal use: the word has no technical sense; "notable" (worth notice) is allowed when followed by the reason.
