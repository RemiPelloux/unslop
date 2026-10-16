From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 273. `furthermore`

- Kind: adverb, connective. Banned forms: `furthermore`.
- Why it reads as machine text: `furthermore` is one of the connectives models put at the start of the second or third paragraph of an answer, in a register nobody uses in speech. It signals "here is another point" without saying how the point relates to the last one. Stacked with `moreover` and `additionally`, it dresses a list as an argument.
- Where it shows up: essay-style answers, cover letters, documentation written as prose.

```slop
Furthermore, the API supports pagination.
The tool is fast. Furthermore, it is free.
Furthermore, it is important to consider security implications.
```

Replace with:

- Start with the claim: "The API supports pagination."
- "and" or "also" inside the sentence when the two points belong together.
- A bulleted list when you have 3 or more parallel points.
- Cut it when the next sentence plainly adds to the last; the reader already knows it is an addition.

Rewrites:

```slop
Furthermore, the API supports pagination.
```

After: The API paginates results with a `cursor` parameter, 100 items per page.

```slop
The tool is fast. Furthermore, it is free.
```

After: The tool is fast and free.

```slop
Furthermore, it is important to consider security implications.
```

After: Uploads accept any file type, so scan files before you serve them to other users.

- Literal use: the word has no technical sense; inside quoted legal text, keep the quote in inline code.
