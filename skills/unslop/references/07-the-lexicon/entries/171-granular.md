From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 171. `granular`

- Kind: adjective. Banned forms: `granular`, `granularly`.
- Why it reads as machine text: Permissions and analytics marketing (`granular controls`, `granular insights`) that models use when they mean `more than one setting`. It claims fine detail without stating the unit. Swapping in `granularity` keeps the same gap.
- Where it shows up: permissions pages, analytics features, logging tickets.

```slop
Granular permissions for every team member.
Get granular insights into user behavior.
We need more granular logging.
```

Replace with:

- The unit of control and the levels: "per project and per environment: view, deploy, admin".
- The unit of data and the retention: "per session, kept 13 months".
- For logging, the fields and the trigger.
- Cut it when "per X" says it in fewer words.

Rewrites:

```slop
Granular permissions for every team member.
```

After: Set permissions per project and per environment: view, deploy or admin.

```slop
Get granular insights into user behavior.
```

After: See each session's page views and clicks, kept for 13 months.

```slop
We need more granular logging.
```

After: Log request ID, user ID and duration for every database query over 100ms.

- Literal use: for sand, sugar or film stock, write "grainy" or give the grain size: "0.5 mm grains".
