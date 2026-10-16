From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 212. `symphony`

- Kind: noun. Banned forms: `symphony`, `symphonies`.
- Why it reads as machine text: `symphony` appears when a model needs to say that several parts work together and wants it to sound coordinated and pleasant. It is the music cousin of `tapestry` and `orchestrate`, and it turns up in the same feature pages. The metaphor claims the parts are in tune without saying which parts they are, what they pass to each other, or what happens when one fails.
- Where it shows up: feature overviews of integrations, food and travel copy (`a symphony of flavors`), architecture write-ups.

```slop
Our scheduler, queue and workers come together in a symphony of automation.
Each dish is a symphony of flavors from the Mediterranean coast.
The dashboard brings a symphony of data to your fingertips.
```

Replace with:

- For systems, name the parts and the order they run in: "the scheduler enqueues a job, a worker picks it up within 2 s".
- For food, name the ingredients.
- "together" or "in sequence" when a short connector is enough.
- Cut it when the sentence is only there to sound pleasant; the list of parts already says they combine.

Rewrites:

```slop
Our scheduler, queue and workers come together in a symphony of automation.
```

After: The scheduler enqueues each job at its cron time, and one of 8 workers runs it within 2 seconds.

```slop
Each dish is a symphony of flavors from the Mediterranean coast.
```

After: Each dish uses ingredients from the Aegean coast: lemon, oregano, sumac and grilled octopus.

```slop
The dashboard brings a symphony of data to your fingertips.
```

After: The dashboard shows revenue, signups and error rate on one screen, refreshed every 60 seconds.

- Literal use: for an orchestral work, name the piece ("Beethoven's Ninth", "Mahler 5") or put `symphony` in inline code.
