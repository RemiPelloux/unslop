From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 293. `interestingly`

- Kind: adverb. Banned forms: `interestingly`, `Interestingly,`, `interestingly enough`.
- Why it reads as machine text: `interestingly` tells the reader how to feel about the next fact instead of making the fact interesting. Models use it as a transition when the next point has no logical link to the last. It is a filler slot for "here is another thing".
- Where it shows up: data summaries, research write-ups, and chat answers that list findings.

```slop
Interestingly, mobile users converted at a higher rate.
Interestingly enough, the bug only appears in Safari.
The results were interestingly mixed across regions.
```

Replace with:

- The expectation it breaks: "We expected X; we saw Y."
- A causal link: "because", "so", or "which means".
- The fact alone, with its numbers, so the reader judges it.
- Cut it when nothing was expected; the fact stands without a frame.

Rewrites:

```slop
Interestingly, mobile users converted at a higher rate.
```

After: Mobile users converted at 3.1% against 2.4% on desktop, the reverse of last year.

```slop
Interestingly enough, the bug only appears in Safari.
```

After: The bug only appears in Safari, which does not support `:has()` inside `@supports` before 15.4.

```slop
The results were interestingly mixed across regions.
```

After: Signups rose 12% in Europe and fell 4% in North America.

- Literal use: none. Interest is the reader's to decide.
