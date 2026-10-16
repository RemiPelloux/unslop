From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 147. `myriad`

- Kind: adjective and noun. Banned forms: `myriad`, `myriads`.
- Why it reads as machine text: Models reach for it to avoid counting, and `a myriad of` draws usage complaints from editors as well. It sounds literary in technical text. It hides a number the writer could count, and a count is shorter than the phrase.
- Where it shows up: feature lists, docs intros, project retrospectives.

```slop
The library supports a myriad of formats.
There are myriad ways to configure the CLI.
We faced a myriad of challenges during the migration.
```

Replace with:

- The count: "reads 14 formats".
- The list, if it is short: "CSV, Parquet and JSON Lines".
- The two that matter plus the count of the rest: "CSV, Parquet and 12 others (see the table)".
- Cut it when nothing follows it. Write the list or delete the sentence.

Rewrites:

```slop
The library supports a myriad of formats.
```

After: The library reads 14 formats, including CSV, Parquet and JSON Lines.

```slop
There are myriad ways to configure the CLI.
```

After: The CLI reads flags, then environment variables, then `~/.toolrc`; the first one set wins.

```slop
We faced a myriad of challenges during the migration.
```

After: The migration ran three months late because two services wrote to the same table.

- Literal use: for the old sense of ten thousand, write "10,000".
