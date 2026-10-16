From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 307. `important to note`

- Kind: phrase. Banned forms: `important to note`, `it's important to note`, `it is important to remember`, `keep in mind that`.
- Why it reads as machine text: `It's important to note` claims priority for a statement and then buries it mid-paragraph. Chat models attach it to safety caveats and edge cases out of habit, so it appears on things that are not important. When everything is flagged, nothing is.
- Where it shows up: chat answers, how-to articles, and generated README warnings.

```slop
It's important to note that this command deletes all data.
It is important to remember that results may vary.
Keep in mind that the token expires after one hour.
```

Replace with:

- A warning placed before the step it affects, in its own block.
- The specific condition, in place of "results may vary".
- The fact stated in the step where the reader needs it.
- Cut it when the fact is not a risk; put it in the body.

Rewrites:

```slop
It's important to note that this command deletes all data.
```

After: Warning: `db:reset` deletes every table. Run `db:dump` first.

```slop
It is important to remember that results may vary.
```

After: Results depend on image size; above 4,000px the model misses small text.

```slop
Keep in mind that the token expires after one hour.
```

After: The token expires after 60 minutes. Call `refresh()` before then.

- Literal use: none. Put the important thing first.
