From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 285. `indeed`

- Kind: adverb, connective. Banned forms: `indeed`, `Indeed,`, `yes indeed`, `very X indeed`.
- Why it reads as machine text: `indeed` confirms what the previous sentence already said, so it signals a repeat. Chat models use `Indeed,` to open an agreement with the user, and generated essays use it to start a sentence that restates the thesis with an example. Few people use the word in speech, so it reads as borrowed formality.
- Where it shows up: the first word of a chat reply that agrees with the user, the middle of an essay paragraph, and code review replies.

```slop
Indeed, the function does mutate its input.
This approach is indeed faster, as the benchmarks show.
The error is very confusing indeed.
```

Replace with:

- "Yes" when you are answering a question.
- The evidence itself, with no confirming word before it.
- "In fact" only when you correct a wrong belief, and say what the belief was.
- Cut it when the sentence before already made the point.

Rewrites:

```slop
Indeed, the function does mutate its input.
```

After: Yes. `sortUsers` sorts the array in place, so callers see their list reordered.

```slop
This approach is indeed faster, as the benchmarks show.
```

After: The batched insert runs in 180ms against 2.1s for the loop.

```slop
The error is very confusing indeed.
```

After: The error says "undefined is not a function" and names no file, so it is hard to trace.

- Literal use: none. The confirming sense is the only sense.
