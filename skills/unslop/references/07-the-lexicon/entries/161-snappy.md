From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 161. `snappy`

- Kind: adjective. Banned forms: `snappy`, `snappier`, `snappiest`, `snappily`, `snappiness`.
- Why it reads as machine text: Developer-marketing word for responsiveness. Models write `snappier search` in release notes in place of a latency number. It is a feeling about speed and hides the p50 or p95 a reader could compare.
- Where it shows up: release notes, README feature lists, UI feedback.

```slop
Search is now much snappier.
A snappy, lightweight alternative to Electron apps.
Make the button feel snappier.
```

Replace with:

- Latency percentiles with the input size: "p95 from 640ms to 180ms on a 50,000-document index".
- Install size and memory: "12 MB download, 60 MB RAM at idle".
- For UI, the interaction spec: time to pressed state, duration, easing.
- Cut it when you have no number. Measure first.

Rewrites:

```slop
Search is now much snappier.
```

After: Search p95 dropped from 640ms to 180ms on a 50,000-document index.

```slop
A snappy, lightweight alternative to Electron apps.
```

After: A 12 MB native app that uses 60 MB of RAM at idle; the Electron version used 410 MB.

```slop
Make the button feel snappier.
```

After: Show the pressed state within 50ms, and replace the 300ms `ease-in-out` with 120ms `ease-out`.

- Literal use: for a short remark, write "short" or "terse"; for an irritable dog, write "irritable".
