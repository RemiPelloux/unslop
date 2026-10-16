From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 298. `aforementioned`

- Kind: adjective. Banned forms: `aforementioned`, `the aforementioned`, `abovementioned`, `said` as in "said function".
- Why it reads as machine text: `aforementioned` points back at something instead of naming it, which makes the reader scroll up. It is legal register applied to software. Models use it to avoid repeating a noun, though repeating the noun is clearer.
- Where it shows up: long docs that refer back to earlier sections, support replies, and generated reports.

```slop
The aforementioned function should be called before rendering.
Please refer to the aforementioned documentation.
To avoid the aforementioned issues, pin your dependencies.
```

Replace with:

- The noun again: "`initTheme()`", "the timeout issue".
- "this" or "that" when the referent is in the previous sentence.
- A link to the section, when the referent is far away.
- Cut it when "the" alone points clearly enough.

Rewrites:

```slop
The aforementioned function should be called before rendering.
```

After: Call `initTheme()` before the first render.

```slop
Please refer to the aforementioned documentation.
```

After: See the "Auth tokens" section of the API reference.

```slop
To avoid the aforementioned issues, pin your dependencies.
```

After: Pin your dependencies to avoid the lockfile drift described in step 2.

- Literal use: none outside contracts. Name the thing.
