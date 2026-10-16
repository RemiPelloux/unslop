From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 306. `worth noting`

- Kind: phrase. Banned forms: `worth noting`, `it's worth noting that`, `it is worth noting`, `worth mentioning`.
- Why it reads as machine text: `It's worth noting that` spends five words to say the next clause matters. Models insert it before caveats and side facts, often several times in one reply. The phrase signals that the writer has not decided where the fact belongs.
- Where it shows up: chat answers, documentation caveats, and pull request descriptions.

```slop
It's worth noting that this API is deprecated.
It is worth noting that the free plan has a rate limit.
Worth mentioning: the build may take longer on Windows.
```

Replace with:

- The fact, stated where it applies.
- A labeled warning block in docs ("Warning" or "Note") when the reader must not miss it.
- The fact moved to the first line, if it changes the answer.
- Cut it when the clause after it can stand alone, which is always.

Rewrites:

```slop
It's worth noting that this API is deprecated.
```

After: This API is deprecated and will be removed in v5. Use `fetchUsers()` instead.

```slop
It is worth noting that the free plan has a rate limit.
```

After: The free plan allows 60 requests per minute.

```slop
Worth mentioning: the build may take longer on Windows.
```

After: On Windows the build takes about 4 minutes because file watching is slower.

- Literal use: none. If the fact matters, state it where it applies.
