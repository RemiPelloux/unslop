From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 202. `unified`

- Kind: adjective (participle of "unify"). Banned forms: `unified`.
- Why it reads as machine text: Platform vocabulary: `unified platform`, `unified view`, `unified design language`. Models use it whenever two products merge or data comes from several sources. It hides what was joined, by which key, and what was left out. Two products sold as one often still have two logins and two invoices for the first year.
- Where it shows up: observability and CRM products, merger announcements, design system pitches.

```slop
A unified platform for observability.
Get a unified view of your customers.
A unified design language across all products.
```

Replace with:

- What is combined and how the parts link.
- Which sources feed the view and the match key.
- For design, the shared files and the apps that use them.
- Cut it when "one" says it: one query language, one login, one token file.

Rewrites:

```slop
A unified platform for observability.
```

After: Logs, metrics and traces in one query language. Each trace links to its logs by trace ID.

```slop
Get a unified view of your customers.
```

After: Orders, tickets and emails, matched by email address, in one timeline per customer.

```slop
A unified design language across all products.
```

After: All four apps use one token file, one icon set and one component library.

- Literal use: for the verb, write "merged" or "combined"; for one account system, write "single sign-on" or "one login".
