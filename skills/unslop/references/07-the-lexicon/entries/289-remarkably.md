From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 289. `remarkably`

- Kind: adverb. Banned forms: `remarkably`, `Remarkably,`, `remarkably simple`.
- Why it reads as machine text: `remarkably` marks a surprise without saying what was expected. Models use it to dress an ordinary result as a finding, as in `Remarkably, the change reduced errors.` The reader cannot judge the surprise because the baseline is missing.
- Where it shows up: postmortems, research summaries, and product updates.

```slop
Remarkably, the fix reduced error rates across the board.
The API is remarkably simple to integrate.
The model performs remarkably well on long documents.
```

Replace with:

- The expectation and the result: "We expected a 5% drop; errors fell 60%."
- The integration measured in lines of code or calls.
- The score and the benchmark name.
- Cut it when there was no expectation to break.

Rewrites:

```slop
Remarkably, the fix reduced error rates across the board.
```

After: We expected the retry fix to help checkout only, but 5xx errors fell 60% on every endpoint.

```slop
The API is remarkably simple to integrate.
```

After: A working integration is 12 lines: create a client, sign the request, read the JSON.

```slop
The model performs remarkably well on long documents.
```

After: On 50-page contracts the model finds 91% of the clauses a lawyer marked.

- Literal use: to say something deserves comment, write "unusual" or "unexpected" and state the usual case.
