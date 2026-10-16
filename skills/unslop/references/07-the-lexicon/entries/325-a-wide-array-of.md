From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 325. `a wide array of`

- Kind: phrase. Banned forms: `a wide array of`, `an array of`, `a broad array of`.
- Why it reads as machine text: `a wide array of` is the formal twin of "range", and models alternate the two within a page to avoid repeating themselves. The word "array" adds an air of precision to a phrase that has none. In technical writing it also collides with the data structure.
- Where it shows up: course catalogs, "Our services" pages, and generated documentation intros.

```slop
The platform offers a wide array of customization options.
Students can choose from a wide array of electives.
The SDK provides a wide array of helper functions.
```

Replace with:

- The specific options a user will look for first: colors, fonts, layout.
- A count with a link to the full list.
- The three helpers most people need, by name.
- Cut it when the next sentence lists the items.

Rewrites:

```slop
The platform offers a wide array of customization options.
```

After: You can change the logo, the accent color, the font, and the email sender name.

```slop
Students can choose from a wide array of electives.
```

After: Students choose 4 of 26 electives; the full list is on the course page.

```slop
The SDK provides a wide array of helper functions.
```

After: The SDK includes `retry()`, `paginate()`, and `signRequest()`, plus 18 smaller helpers.

- Literal use: for the data structure, give its type and size: "an array of 4,096 `u32` entries". For hardware, "a solar array of 24 panels".
