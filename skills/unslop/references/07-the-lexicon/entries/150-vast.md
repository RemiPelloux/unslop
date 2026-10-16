From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 150. `vast`

- Kind: adjective. Banned forms: `vast`, `vastly`, `vastness`.
- Why it reads as machine text: Models use it for size that nobody measured: `vast amounts of data`, `a vast library`. It makes a scale claim in the voice of nature writing. `vastly` turns a comparison into a feeling (`vastly faster`).
- Where it shows up: data pipeline copy, catalog pages, benchmark summaries.

```slop
Process vast amounts of data in real time.
Access our vast library of components.
The new engine is vastly faster.
```

Replace with:

- Size with units and rate: "4 TB a day, about 50,000 events per second".
- The count: "310 components".
- The ratio and the benchmark: "3.2x faster on TPC-H at scale factor 10".
- Cut it when the reader does not need the size at all.

Rewrites:

```slop
Process vast amounts of data in real time.
```

After: Ingests 50,000 events per second and makes each one queryable within 2 seconds.

```slop
Access our vast library of components.
```

After: Use any of 310 components, each with Figma and React versions.

```slop
The new engine is vastly faster.
```

After: The new engine runs TPC-H at scale factor 10 in 41 seconds, down from 132.

- Literal use: for physical size, give the measurement: "1,200 square kilometres".
