From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 342. `built for the future`

- Kind: phrase. Banned forms: `built for the future`, `built for tomorrow`, `designed for the future`.
- Why it reads as machine text: `built for the future` promises longevity without a support policy, a version plan, or a date. Models use it in platform and infrastructure copy where buyers worry about lock-in. The claim cannot be checked until it is too late.
- Where it shows up: infrastructure product pages, architecture proposals, and real estate listings.

```slop
Our platform is built for the future.
A database built for tomorrow's workloads.
This architecture is designed for the future of your business.
```

Replace with:

- The support window: "Each major version gets 3 years of security fixes."
- The scaling limit tested: "tested to 10 TB and 50,000 writes per second".
- The exit path: export formats, open standards used.
- Cut it when no policy or test stands behind it.

Rewrites:

```slop
Our platform is built for the future.
```

After: Each major version gets 3 years of security fixes, and data exports as standard SQL dumps.

```slop
A database built for tomorrow's workloads.
```

After: A database tested to 10 TB and 50,000 writes per second on one node.

```slop
This architecture is designed for the future of your business.
```

After: This design supports 10 times today's order volume before the queue needs a second partition.

- Literal use: none. State the time span.
