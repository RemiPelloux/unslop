From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 232. `interplay`

- Kind: noun. Banned forms: `interplay`, `interplays`.
- Why it reads as machine text: Models write `the interplay between X and Y` to sound analytic when they have not worked out how X and Y affect each other. It promises a two-way relation and then delivers a list that treats each side alone. Generated essays on almost any topic use it to fill the topic sentence.
- Where it shows up: essay and report intros, design rationales, research summaries.

```slop
This article explores the interplay between typography and color.
The interplay of caching and consistency is often misunderstood.
Good UX emerges from the interplay of form and function.
```

Replace with:

- The relation as a cause: "text at 24px and up needs 3:1 contrast instead of 4.5:1".
- "how X affects Y", one direction at a time.
- "trade-off" when gaining one costs the other.
- Cut it when the article then treats X and Y separately anyway.

Rewrites:

```slop
This article explores the interplay between typography and color.
```

After: Light text on a colored background needs a heavier weight to stay readable; this article gives the weights and sizes.

```slop
The interplay of caching and consistency is often misunderstood.
```

After: A longer cache TTL means faster reads and staler data; at 60 seconds, a user can see an old price for a full minute.

```slop
Good UX emerges from the interplay of form and function.
```

After: A button looks clickable when it has a border, a label that names the action, and a hover state.

- Literal use: when two forces in a system act on each other, write "interaction" and describe both directions.
