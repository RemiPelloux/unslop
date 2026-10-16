From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 324. `a wide range of`

- Kind: phrase. Banned forms: `a wide range of`, `a broad range of`, `a whole range of`.
- Why it reads as machine text: `a wide range of` stands in for a list the writer did not make or a count they did not check. Models produce it whenever a brief says a product supports many things. The reader cannot tell whether the range is 4 or 400.
- Where it shows up: feature pages, integration lists, and service descriptions.

```slop
We support a wide range of file formats.
The library works with a wide range of frameworks.
Our team has experience across a wide range of industries.
```

Replace with:

- The count and the top items: "42 formats, including PDF, DOCX, and HEIC".
- The full list, if it is under 8 items.
- The two or three industries with the most work, and the project count.
- Cut it when the list follows; the list proves the range.

Rewrites:

```slop
We support a wide range of file formats.
```

After: We read 42 formats, including PDF, DOCX, HEIC, and RAW files from 30 camera brands.

```slop
The library works with a wide range of frameworks.
```

After: The library works with React, Vue, Svelte, and plain JavaScript.

```slop
Our team has experience across a wide range of industries.
```

After: We have built 30 apps for banks and 12 for hospitals.

- Literal use: for a numeric range, give the range: "8 to 64 GB", "temperatures from -20 to 45 C".
