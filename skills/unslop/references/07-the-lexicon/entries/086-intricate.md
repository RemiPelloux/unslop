From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 086. `intricate`

- Kind: adjective. Banned forms: `intricate`, `intricately`.
- Why it reads as machine text: models use `intricate` for patterns, systems and plots, usually beside "details" or "web". It treats complexity as praise but never says how many parts there are or how they connect. In code explanations it often covers for logic the writer did not trace.
- Where it shows up: craft and product descriptions, fiction blurbs, code walkthroughs.

```slop
The codebase is an intricate web of dependencies.
The rug features intricate hand-woven patterns.
The plot is an intricate tapestry of betrayal and loyalty.
```

Replace with:

- The count: "the service imports 14 packages, 3 of them in a cycle". Use for systems.
- The measurable detail: "120 knots per square inch, dyed with madder and indigo". Use for craft.
- The structure: "two timelines, 1962 and 2012, that meet in the last chapter". Use for plots.
- Cut it when the noun already implies many parts.

Rewrites:

```slop
The codebase is an intricate web of dependencies.
```

After: The billing service imports 14 internal packages, and 3 of them import each other.

```slop
The rug features intricate hand-woven patterns.
```

After: Hand-knotted wool at 120 knots per square inch, dyed with madder and indigo.

```slop
The plot is an intricate tapestry of betrayal and loyalty.
```

After: The novel alternates between 1962 and 2012, and the two timelines meet in the last chapter.

- Literal use: when you mean hard to follow, say which part is hard: "the retry logic is spread across 3 files".
