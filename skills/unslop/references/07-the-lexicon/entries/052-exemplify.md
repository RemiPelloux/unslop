From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 052. `exemplify`

- Kind: verb. Banned forms: `exemplify`, `exemplifies`, `exemplified`, `exemplifying`.
- Why it reads as machine text: A close cousin of `epitomize`, it appears in generated essays and review comments as praise without detail: `this function exemplifies good practice`. It points at an example and stops. The reader still does not know what to copy from it. In reviews, the author learns nothing to apply to the next PR.
- Where it shows up: code review comments, academic essays, documentation intros, award nominations.

```slop
This codebase exemplifies best practices in testing.
The following snippet exemplifies the pattern.
Her work exemplifies our commitment to excellence.
```

Replace with:

- `shows` or `is an example of`.
- Name the practice the example follows.
- For snippets, write "For example" and show the code.

Rewrites:

```slop
This codebase exemplifies best practices in testing.
```

After: Each module has its tests next to it, and every bug fix starts with a failing test.

```slop
The following snippet exemplifies the pattern.
```

After: In this snippet the cache is checked first, and the database is read only on a miss.

```slop
Her work exemplifies our commitment to excellence.
```

After: She rewrote the billing retries and cut failed charges from 3% to 0.4%.

- Literal use: there is no other sense; write "for example" or "such as".
