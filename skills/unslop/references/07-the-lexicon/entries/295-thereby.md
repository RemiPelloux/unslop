From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 295. `thereby`

- Kind: adverb, connective. Banned forms: `thereby`, `, thereby reducing`, `, thereby ensuring`.
- Why it reads as machine text: `thereby` hangs a consequence on the end of a sentence as an "-ing" clause, so one sentence carries an action and its effect. Models produce this shape constantly (`X does Y, thereby reducing Z`) because it packs a claim of benefit into the tail where it is rarely checked. The register is legal, not technical.
- Where it shows up: design docs, PR descriptions, and generated commit messages.

```slop
The cache stores results in memory, thereby reducing database load.
We added retries, thereby improving reliability.
The new flow removes a step, thereby ensuring a smoother checkout.
```

Replace with:

- Two sentences: the action, then the effect with its number.
- "so" between the clauses when the effect is short.
- The effect alone, if the action is obvious from context.
- Cut it when the consequence is a vague benefit; state the measured one or drop it.

Rewrites:

```slop
The cache stores results in memory, thereby reducing database load.
```

After: The cache stores results in memory. Database reads fell from 1,200 to 300 per second.

```slop
We added retries, thereby improving reliability.
```

After: We retry failed uploads 3 times with backoff, so a dropped connection no longer loses the file.

```slop
The new flow removes a step, thereby ensuring a smoother checkout.
```

After: The new flow drops the address confirmation page; checkout is now 3 screens.

- Literal use: in a contract, keep the drafting style your lawyer uses; in product and code text, use "so".
