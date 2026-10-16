From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 198. `battle-tested`

- Kind: adjective. Banned forms: `battle-tested`, `battle tested`.
- Why it reads as machine text: Infrastructure and open-source marketing uses it for any library with users, and models apply it to processes too. It claims proven reliability and hides the evidence: years in production, traffic, adopters, incident history. A library with a 0.x version number and the word in its README contradicts itself.
- Where it shows up: README headers, infrastructure product pages, deployment docs.

```slop
A battle-tested queue for production workloads.
Battle-tested by thousands of companies.
Our battle-tested deployment process.
```

Replace with:

- The production record: since when, how much traffic, at whom.
- Adoption with a source: download counts, an adopters file.
- For a process, the safeguards and how often they fired.
- Cut it when you have no production record yet. Say it is new.

Rewrites:

```slop
A battle-tested queue for production workloads.
```

After: In production since 2017; the three largest users each run about 2 billion jobs a day.

```slop
Battle-tested by thousands of companies.
```

After: 3.4 million weekly npm downloads; 40 public companies are listed in `ADOPTERS.md`.

```slop
Our battle-tested deployment process.
```

After: Each release goes to 5 percent of traffic for 30 minutes and rolls back if errors pass 1 percent. That happened 3 times in 2025.

- Literal use: for military equipment, write "used in combat" and name the conflict.
