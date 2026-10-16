From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 288. `incredibly`

- Kind: adverb. Banned forms: `incredibly`, `incredible`, `incredibly fast`, `incredibly easy`.
- Why it reads as machine text: `incredibly` means "not believable", and it is placed before claims that should be believed. Models use it as the default intensifier for speed and ease (`incredibly fast`, `incredibly easy`), where a number would carry the claim. Three uses on one landing page are common in generated copy.
- Where it shows up: performance claims, onboarding copy, and reviews.

```slop
The new build system is incredibly fast.
Setting up the SDK is incredibly easy.
Our team has been incredibly busy this quarter.
```

Replace with:

- The measured value with its baseline: "builds in 4s, down from 38s".
- A count of steps or minutes for ease.
- The work itself, listed, in place of "busy".
- Cut it when there is no number; then cut the claim it was propping up.

Rewrites:

```slop
The new build system is incredibly fast.
```

After: A cold build of the 900-file monorepo takes 4 seconds, down from 38.

```slop
Setting up the SDK is incredibly easy.
```

After: Install the package, add one API key, and call `init()`. Setup takes about 5 minutes.

```slop
Our team has been incredibly busy this quarter.
```

After: This quarter we shipped SSO, the audit log, and 3 regional data centers.

- Literal use: for a claim that is hard to believe, say so plainly: "This number looks wrong, so we ran it 3 times."
