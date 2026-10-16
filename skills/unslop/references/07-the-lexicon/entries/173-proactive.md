From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 173. `proactive`

- Kind: adjective. Banned forms: `proactive`, `proactively`.
- Why it reads as machine text: Support, security and hiring copy uses it, and models write `we proactively monitor` for any system with alerts. It says action comes before the problem without naming the signal or how early. In job ads it means `do work nobody assigned`, unstated.
- Where it shows up: SLA pages, job ads, incident follow-ups.

```slop
We proactively monitor your infrastructure 24/7.
Looking for a proactive self-starter.
Proactive security to stop threats before they happen.
```

Replace with:

- The trigger and the response: which metric, which threshold, who responds, how fast.
- The behavior you expect from the hire, in one sentence.
- The controls and their deadlines.
- Cut it when "before" plus the event says it plainly.

Rewrites:

```slop
We proactively monitor your infrastructure 24/7.
```

After: An alert fires when disk use passes 80 percent; on-call responds within 15 minutes at any hour.

```slop
Looking for a proactive self-starter.
```

After: You will find and file bugs in the areas you own without waiting to be assigned them.

```slop
Proactive security to stop threats before they happen.
```

After: Every pull request gets a dependency scan, and critical CVEs are patched within 48 hours.

- Literal use: none. Write "early" or "before X happens", and name X.
