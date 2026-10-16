From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 242. `silver bullet`

- Kind: noun phrase. Banned forms: `silver bullet`, `silver bullets`.
- Why it reads as machine text: Models write `there is no silver bullet` as a reflex hedge, and `a silver bullet for X` as a claim to deny or, in marketing, to make. The phrase comes from Fred Brooks's 1986 essay, which lends it borrowed authority. Both uses are filler: the denial hides which partial fixes help, and the claim is never true.
- Where it shows up: closing paragraphs of advice posts, architecture debates, vendor pitches.

```slop
There is no silver bullet for technical debt.
Microservices are not a silver bullet.
Our platform is the silver bullet for slow page loads.
```

Replace with:

- "no single fix", then the 2 or 3 fixes that do help.
- The trade-off: "microservices add network calls and deploy overhead".
- For a product claim, the measured result on a stated workload.
- Cut it when the hedge closes a paragraph that already listed the options.

Rewrites:

```slop
There is no silver bullet for technical debt.
```

After: Technical debt shrinks when teams budget 20% of each sprint for it and delete dead code first.

```slop
Microservices are not a silver bullet.
```

After: Microservices let each team deploy alone, at the cost of network calls, distributed tracing and more on-call work.

```slop
Our platform is the silver bullet for slow page loads.
```

After: On our test set of 50 store pages, the CDN cut median load time from 3.1 s to 1.4 s.

- Literal use: when citing Brooks, give the essay title in inline code, `No Silver Bullet` (1986); for werewolf folklore, put `silver bullet` in inline code.
