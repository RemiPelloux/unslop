From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 299. `in conclusion`

- Kind: closer. Banned forms: `in conclusion`, `In conclusion,`, `to conclude`.
- Why it reads as machine text: `In conclusion,` comes from the school essay template, and models trained on essays reproduce it at the top of the last paragraph. The paragraph that follows restates the points above in the same order. A reader can skip it without losing anything, which they will.
- Where it shows up: the last paragraph of a generated blog post, chat answers longer than 300 words, and reports.

```slop
In conclusion, choosing the right database depends on your needs.
In conclusion, accessibility should be part of every project.
To conclude, the new pipeline offers many benefits.
```

Replace with:

- Nothing. End on the last new fact or the last step.
- A decision or recommendation, stated as the final line: "Use Postgres unless you need X."
- A summary at the top (TL;DR) instead of the bottom, for long documents.
- Cut it when the final paragraph only restates; cut the paragraph too.

Rewrites:

```slop
In conclusion, choosing the right database depends on your needs.
```

After: Use Postgres unless you need more than 50,000 writes per second; then test Cassandra.

```slop
In conclusion, accessibility should be part of every project.
```

After: Add an axe check to CI so contrast and label errors fail the build.

```slop
To conclude, the new pipeline offers many benefits.
```

After: The new pipeline deploys in 6 minutes instead of 25 and rolls back in one command.

- Literal use: for the closing section of a paper, use the heading "Conclusions" and state findings, not a recap.
