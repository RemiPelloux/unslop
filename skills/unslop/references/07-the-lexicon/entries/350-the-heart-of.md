From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 350. `the heart of`

- Kind: phrase. Banned forms: `the heart of`, `at the heart of`, `heart and soul`.
- Why it reads as machine text: `at the heart of` claims centrality for a value or component without showing it. Models write `At the heart of our platform is a commitment to X`, where X is a value every company lists. For components, the phrase replaces a diagram or a dependency count.
- Where it shows up: About pages, architecture overviews, and travel copy (`in the heart of the city`).

```slop
At the heart of our platform is a commitment to privacy.
The scheduler lies at the heart of the system.
Our hotel is located in the heart of Lisbon.
```

Replace with:

- The policy or mechanism that shows the value: "We store no message content; it is encrypted on your device."
- The dependency fact: "Every job passes through the scheduler; if it stops, nothing runs."
- The location with a distance: "200m from Rossio station."
- Cut it when the value is not backed by a policy.

Rewrites:

```slop
At the heart of our platform is a commitment to privacy.
```

After: Messages are encrypted on your device; our servers never see the content.

```slop
The scheduler lies at the heart of the system.
```

After: Every job passes through the scheduler; if it stops, no job runs.

```slop
Our hotel is located in the heart of Lisbon.
```

After: The hotel is in Baixa, 200m from Rossio station.

- Literal use: for an actual heart, drop the "of" construction: write "a patient's heart" or "the heart" and name the part, "the left ventricle".
