From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 218. `paradigm`

- Kind: noun. Banned forms: `paradigm`, `paradigms`, and the phrase `paradigm shift`.
- Why it reads as machine text: `paradigm` entered business prose through Thomas Kuhn and stayed as a word that makes a small change sound like a scientific revolution. Models produce `a new paradigm for` and `paradigm shift` for any new feature, framework or workflow. The word hides what was there before and what is different now, which are the two facts the reader needs.
- Where it shows up: launch posts, framework READMEs, conference talk abstracts.

```slop
Server components represent a new paradigm for building web apps.
This is a paradigm shift in how teams think about deployment.
Our tool introduces a declarative paradigm for infrastructure.
```

Replace with:

- "approach", "model" or "way" when the plain noun does the job.
- A before and after pair: "before, X; now, Y".
- "style" for programming style: "functional style", "declarative style".
- Cut it when the sentence says only that the thing is new.

Rewrites:

```slop
Server components represent a new paradigm for building web apps.
```

After: Server components render on the server and send HTML, so the browser downloads less JavaScript for the static parts of a page.

```slop
This is a paradigm shift in how teams think about deployment.
```

After: Teams now deploy on every merge to `main` instead of once a week from a release branch.

```slop
Our tool introduces a declarative paradigm for infrastructure.
```

After: You describe the servers you want in a YAML file, and the tool creates, changes or deletes servers to match it.

- Literal use: for programming styles, name the style ("object-oriented", "functional"); for Kuhn's sense in the history of science, put `paradigm` in inline code.
