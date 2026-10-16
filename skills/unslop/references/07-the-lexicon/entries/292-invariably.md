From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 292. `invariably`

- Kind: adverb. Banned forms: `invariably`, `invariably leads to`.
- Why it reads as machine text: `invariably` claims a rule with no exceptions from what is usually a handful of cases. Models reach for it to make advice sound like law (`invariably leads to bugs`). Readers who know one counterexample stop trusting the rest of the page.
- Where it shows up: engineering advice posts, code review comments, and management writing.

```slop
Skipping tests invariably leads to production bugs.
Large PRs invariably get rubber-stamped in review.
Users invariably ignore onboarding tooltips.
```

Replace with:

- A frequency with its sample: "in 9 of our last 12 incidents".
- "Always" when it is a rule of the system, and name the rule.
- "Often" or "usually" with an example, when you have no count.
- Cut it when the claim works as a tendency; most claims do.

Rewrites:

```slop
Skipping tests invariably leads to production bugs.
```

After: 9 of our last 12 incidents shipped in a PR with no new tests.

```slop
Large PRs invariably get rubber-stamped in review.
```

After: PRs over 800 lines got a median of 1 review comment; PRs under 200 got 6.

```slop
Users invariably ignore onboarding tooltips.
```

After: In session recordings, 4 of 5 new users closed the first tooltip within 2 seconds.

- Literal use: for a value that never changes, use the noun "invariant" and state it: "Invariant: `balance >= 0`."
