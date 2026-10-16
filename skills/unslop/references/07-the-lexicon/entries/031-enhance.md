From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 031. `enhance`

- Kind: verb. Banned forms: `enhance`, `enhances`, `enhanced`, `enhancing`, `enhancement`, `enhancements`.
- Why it reads as machine text: It is the default verb for improvement in generated release notes and PR descriptions. It tells the reader something got better and leaves out what, by how much, and for whom. `Enhanced performance` with no number is the classic case. Issue trackers use `enhancement` as a label, and models copy that label into prose.
- Where it shows up: changelogs, PR titles, feature lists, issue labels.

```slop
Enhanced performance and stability.
This PR enhances the search experience.
AI-enhanced photo editing.
```

Replace with:

- `improve`, with the number.
- Say what changed: "added", "fixed", "faster".
- In changelogs, one line per change, each with its own verb.
- `fix` for bugs; a fixed bug is not an improvement in general terms.

Rewrites:

```slop
Enhanced performance and stability.
```

After: Startup time down from 3.1 s to 1.4 s; fixed the crash when opening files over 2 GB.

```slop
This PR enhances the search experience.
```

After: Search now matches partial words and shows results as you type.

```slop
AI-enhanced photo editing.
```

After: Remove backgrounds and fix exposure in one click, with undo for each step.

- Literal use: keep GitHub's label and the web term in inline code (`enhancement`, `progressive enhancement`); for images, write "upscale" or "sharpen".
