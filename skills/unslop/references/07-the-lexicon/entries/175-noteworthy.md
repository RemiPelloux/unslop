From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 175. `noteworthy`

- Kind: adjective. Banned forms: `noteworthy`, `noteworthiness`.
- Why it reads as machine text: Models open summary bullets with it (`Noteworthy changes include`) and use it to flag a point without saying why it matters. It is a cousin of `notably` and `worth noting`. It asks for attention and gives no reason.
- Where it shows up: release notes, meeting summaries, code review comments.

```slop
Noteworthy changes in this release include improved performance.
One noteworthy aspect of the design is its use of color.
It's noteworthy that tests now pass on Windows.
```

Replace with:

- Sort by consequence and label the category: "Breaking", "Fixed", "Faster".
- Say what the point means for the reader.
- State the fact and drop the preamble.
- Cut it when `It's noteworthy that` comes before a statement. Delete those four words.

Rewrites:

```slop
Noteworthy changes in this release include improved performance.
```

After: Breaking: `config.load()` now returns a Promise. Faster: cold start dropped from 1.9s to 0.7s.

```slop
One noteworthy aspect of the design is its use of color.
```

After: Status colors are the only saturated colors on the page, so errors stand out.

```slop
It's noteworthy that tests now pass on Windows.
```

After: Tests now pass on Windows.

- Literal use: none.
