From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 214. `cornerstone`

- Kind: noun. Banned forms: `cornerstone`, `cornerstones`.
- Why it reads as machine text: Models use `cornerstone` to mark something as important without ranking it against anything. `X is the cornerstone of Y` is one of the most common sentence templates in generated essays and company values pages. When every value on the page gets the label, it stops ranking anything, and it never says whether the writer means first in time, most depended on, or just liked.
- Where it shows up: company values pages, docs intros (`Security is the cornerstone of...`), essay openings.

```slop
Trust is the cornerstone of everything we build.
Type safety is a cornerstone of our engineering culture.
The useState hook is the cornerstone of React state management.
```

Replace with:

- "first rule" or "main reason" when the claim is about priority, then say what it outranks.
- The concrete practice: "every PR needs a passing type check".
- "depends on" when you mean dependency: "every report depends on this table".
- Cut it when the sentence states a value with no practice behind it.

Rewrites:

```slop
Trust is the cornerstone of everything we build.
```

After: We sign every release, publish a public changelog, and report incidents within 24 hours.

```slop
Type safety is a cornerstone of our engineering culture.
```

After: CI blocks any merge that adds a `@ts-ignore` or fails `tsc --strict`.

```slop
The useState hook is the cornerstone of React state management.
```

After: Most component state in React lives in `useState`; switch to `useReducer` when one update changes 3 or more fields.

- Literal use: for the stone at a building's corner, write "foundation stone", as in "the foundation stone was laid in 1902".
