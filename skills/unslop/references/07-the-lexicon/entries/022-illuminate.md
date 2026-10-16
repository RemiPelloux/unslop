From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 022. `illuminate`

- Kind: verb. Banned forms: `illuminate`, `illuminates`, `illuminated`, `illuminating`.
- Why it reads as machine text: The light image flatters the writer: the text does not explain, it sheds light. Models use it in summaries (`This study illuminates...`) and in praise (`an illuminating talk`). It promises understanding and skips the finding. Chat models open summaries with it often enough that teachers grading essays now flag it.
- Where it shows up: book and paper summaries, talk descriptions, docs intros, review comments.

```slop
This guide illuminates the inner workings of the JavaScript event loop.
The postmortem illuminated several gaps in our process.
An illuminating conversation about the state of design.
```

Replace with:

- `explains` or `shows`, with the claim.
- `found`, for investigations, followed by the findings.
- Cut it and state the point that was learned.

Rewrites:

```slop
This guide illuminates the inner workings of the JavaScript event loop.
```

After: This guide explains why `setTimeout(fn, 0)` runs after pending promise callbacks.

```slop
The postmortem illuminated several gaps in our process.
```

After: The postmortem found that nobody owned certificate renewal and the expiry alert went to a disabled inbox.

```slop
An illuminating conversation about the state of design.
```

After: Two design leads on why their teams stopped shipping style guides as PDFs.

- Literal use: for lighting, write "light" or "lit" and give the lux when it matters.
