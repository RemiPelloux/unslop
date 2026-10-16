From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 301. `to summarize`

- Kind: closer, transition. Banned forms: `to summarize`, `to sum up`, `summarizing`.
- Why it reads as machine text: `To summarize,` is the same closing move as `in summary` with a verb in front, and models alternate the two to avoid repeating themselves. It announces a recap the reader did not ask for. In chat answers it often follows a bulleted list and repeats the bullets as prose.
- Where it shows up: chat replies, tutorial endings, and meeting notes.

```slop
To summarize, you need to update your config and restart the server.
To sum up, the redesign improves usability and performance.
To summarize the discussion, we agreed to revisit this later.
```

Replace with:

- The steps as a numbered list, once, with no prose recap.
- The specific change, measured.
- Decisions and owners, for meeting notes: "Decision: X. Owner: Ana. Date: 20 Oct."
- Cut it when the summary would repeat the last 5 lines.

Rewrites:

```slop
To summarize, you need to update your config and restart the server.
```

After: Set `cache: false` in `vite.config.ts`, then restart the dev server.

```slop
To sum up, the redesign improves usability and performance.
```

After: The redesign cuts the settings page from 4 tabs to 1 and loads it in 300ms.

```slop
To summarize the discussion, we agreed to revisit this later.
```

After: No decision. Ana will bring cost numbers to the 28 October review.

- Literal use: in a docstring for a function that condenses data, write what it returns: "Returns a one-line digest per log file."
