From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 001. `delve`

- Kind: verb. Banned forms: `delve`, `delves`, `delved`, `delving`.
- Why it reads as machine text: `delves` had one of the largest jumps of any word in PubMed abstracts after 2022, and the excess lines up with the release of chat models (Kobak et al., 2024). Before that it lived in Victorian prose and fantasy novels. It promises depth without naming what was examined, so the sentence after it usually summarizes the surface. If the post cannot name the file, function, or dataset that was examined, nothing was.
- Where it shows up: blog intros, README overviews, the first line of a PR description.

```slop
In this post, we delve into the internals of the React reconciler.
This PR delves into the flaky auth tests and fixes them.
Let's delve deeper into how caching works in our API.
```

Replace with:

- `look at` or `read` when someone examined code or documents.
- `test` / `measure` / `profile` when there was an experiment; name it.
- `compare` when two things were set side by side; give both results.
- Cut it when the sentence works with the verb removed: start with the finding.

Rewrites:

```slop
In this post, we delve into the internals of the React reconciler.
```

After: This post walks through how the React reconciler decides which components to render again.

```slop
This PR delves into the flaky auth tests and fixes them.
```

After: Fix two flaky auth tests; both waited on a 500ms timeout that CI sometimes exceeded.

```slop
Let's delve deeper into how caching works in our API.
```

After: The API caches `GET /users/:id` for 60 seconds in Redis, keyed by user ID.

- Literal use: for digging in soil or archives, write "dig" or "search". No exceptions in prose.
