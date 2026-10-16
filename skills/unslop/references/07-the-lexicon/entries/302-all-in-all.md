From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 302. `all in all`

- Kind: closer. Banned forms: `all in all`, `All in all,`, `all things considered`.
- Why it reads as machine text: `All in all` is a folksy wrap-up that weighs pros and cons without showing the weights. Models use it to end reviews with a verdict that matches the average sentiment of the text above. The verdict is usually "good, with room to improve".
- Where it shows up: product reviews, retrospectives, and chat answers comparing tools.

```slop
All in all, it was a successful launch.
All in all, Svelte is a great choice for small projects.
All things considered, the trip was worth it.
```

Replace with:

- The verdict with the deciding factor: "Svelte, because the bundle is 40% smaller."
- The result against the goal: "We aimed for 500 signups and got 820."
- The one thing that tipped the decision.
- Cut it when the verdict is already clear from the text above.

Rewrites:

```slop
All in all, it was a successful launch.
```

After: The launch brought 820 signups against a goal of 500, with 2 support tickets.

```slop
All in all, Svelte is a great choice for small projects.
```

After: For a 5-page site, pick Svelte: the bundle is 40% smaller and there is no virtual DOM to learn.

```slop
All things considered, the trip was worth it.
```

After: The trip cost 2 days and closed the Lyon contract.

- Literal use: none. Give the deciding factor.
