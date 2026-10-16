From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 054. `encapsulate`

- Kind: verb. Banned forms: `encapsulate`, `encapsulates`, `encapsulated`, `encapsulating`.
- Why it reads as machine text: It has a real meaning in object-oriented design, which gives models cover to use it for summaries: `this quote encapsulates our approach`. In docs it is used loosely for "wraps" or "contains", so the reader cannot tell whether the design term is meant. Both uses skip the content being summed up or hidden. Year-end posts that use it tend to name one abstract noun and no figures.
- Where it shows up: closing lines of essays, class and module docs, mission statements, year-end summaries.

```slop
This quote perfectly encapsulates our philosophy.
The Service class encapsulates all business logic.
One word encapsulates the year: growth.
```

Replace with:

- `sums up` for summaries, or just give the summary.
- `wraps`, `contains`, `hides` in code, and say what callers no longer see.
- Cut it.

Rewrites:

```slop
This quote perfectly encapsulates our philosophy.
```

After: We ship small changes daily and roll back within minutes when one breaks.

```slop
The Service class encapsulates all business logic.
```

After: `OrderService` holds the pricing and tax rules; controllers call `OrderService.place()` and never touch the tables.

```slop
One word encapsulates the year: growth.
```

After: Revenue grew 60% this year, and the team grew from 9 to 21 people.

- Literal use: for OOP and network packets, keep the term in inline code (`encapsulation`, `GRE encapsulation`).
