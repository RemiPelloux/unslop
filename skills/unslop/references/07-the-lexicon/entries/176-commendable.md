From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 176. `commendable`

- Kind: adjective. Banned forms: `commendable`, `commendably`.
- Why it reads as machine text: Models use it in performance-review feedback and code review (`commendable effort`). It grades the author instead of describing the work, in the tone of a school report card. It often comes right before a "but", so readers learn to skip to the criticism.
- Where it shows up: code review comments, peer feedback, summaries of a colleague's work.

```slop
Your commitment to test coverage is commendable.
A commendable effort, but a few changes are needed.
The team's response to the outage was commendable.
```

Replace with:

- The thing done and its effect: what changed, and what it caught or saved.
- For a review with requests, the requests themselves, numbered, with no grade in front.
- For incidents, the timeline: detection, rollback, communication.
- For praise you mean, the reason it matters to the next person who reads the code.
- Cut it when it softens criticism. State the change you need.

Rewrites:

```slop
Your commitment to test coverage is commendable.
```

After: Coverage on `billing/` went from 40 to 85 percent, and the new tests caught the rounding bug in #412.

```slop
A commendable effort, but a few changes are needed.
```

After: Three changes before merge: 1. handle the empty list, 2. rename `doIt`, 3. add a test for the timeout.

```slop
The team's response to the outage was commendable.
```

After: The team detected the outage in 4 minutes, rolled back in 11, and updated the status page every 15.

- Literal use: none.
