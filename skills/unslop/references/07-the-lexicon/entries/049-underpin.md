From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 049. `underpin`

- Kind: verb. Banned forms: `underpin`, `underpins`, `underpinned`, `underpinning`.
- Why it reads as machine text: A building term (support a wall from below) that models use to claim one thing is the base of another: `the principles that underpin our work`. It suggests depth and leaves the principles unlisted. In technical text the sentence usually means "uses"; the noun `underpinning` has its own entry. Strategy docs use it to make a list of opinions look like a foundation.
- Where it shows up: values pages, architecture overviews, academic papers, strategy docs.

```slop
The principles that underpin our design system.
Strong fundamentals underpin every successful engineer.
PostgreSQL underpins our entire data platform.
```

Replace with:

- `is based on`, `uses`, `runs on`.
- List the principles themselves.
- Cut it and say what depends on what.

Rewrites:

```slop
The principles that underpin our design system.
```

After: Our design system has three rules: 4px spacing steps, one accent color, no shadows.

```slop
Strong fundamentals underpin every successful engineer.
```

After: Engineers who can read a stack trace and write a failing test fix bugs faster.

```slop
PostgreSQL underpins our entire data platform.
```

After: Every service writes to one PostgreSQL 16 cluster, and analytics reads from a replica.

- Literal use: for foundations, write "support from below" and name the method ("mass concrete pour").
