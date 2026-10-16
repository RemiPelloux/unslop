From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 066. `deep dive`

- Kind: noun and verb phrase. Banned forms: `deep dive`, `deep dives`, `deep-dive`, `deep diving`.
- Why it reads as machine text: Consulting and podcast language for "detailed look", now the title of a large share of generated technical posts. It sets an expectation of depth that a 900-word post rarely meets. It also says nothing about which part gets the detail. In calendars it marks a meeting with no agenda.
- Where it shows up: post titles, meeting agenda items, talk titles, Slack messages.

```slop
A deep dive into PostgreSQL indexing.
Let's schedule a deep dive on the Q3 numbers.
Deep dive: how we scaled to 1M users.
```

Replace with:

- Name the scope: "how B-tree, GIN, and BRIN indexes store data".
- `review`, `walkthrough`, `meeting` for calendar items.
- Cut it from titles; the topic is the title.

Rewrites:

```slop
A deep dive into PostgreSQL indexing.
```

After: How PostgreSQL B-tree, GIN, and BRIN indexes store rows on disk.

```slop
Let's schedule a deep dive on the Q3 numbers.
```

After: 30-minute meeting Thursday: why Q3 churn rose from 3% to 5%.

```slop
Deep dive: how we scaled to 1M users.
```

After: How we went from 1 database to 8 shards at 1M users.

- Literal use: for scuba, write "a dive below 30 m".
