From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 266. `magic`

- Kind: noun, also used as an adjective. Banned forms: `magic`, `magics`. The adjective `magical` has its own entry.
- Why it reads as machine text: Models attach `magic` to any automated step: `let the magic happen`, `like magic`, `AI magic`. The word hides the mechanism, which is the one thing a technical reader needs in order to trust the output and debug it. It also signals that the writer may not know how the thing works.
- Where it shows up: copy for AI features, onboarding screens, docs that skip the mechanism.

```slop
Just upload your CSV and let the magic happen.
Our AI works its magic on your photos.
Here's where the magic happens: the build() function.
```

Replace with:

- What happens, step by step: "we detect column types, then match them to your fields".
- "automatically", with what is automatic.
- The function or model, named, with its limits.
- Cut it when the next sentence explains the mechanism.

Rewrites:

```slop
Just upload your CSV and let the magic happen.
```

After: Upload a CSV; we detect column types from the first 100 rows, match them to your fields, and ask you to confirm.

```slop
Our AI works its magic on your photos.
```

After: The model removes noise and corrects exposure; it does not change faces or add objects.

```slop
Here's where the magic happens: the build() function.
```

After: The `build()` function reads the config, compiles each page, and writes the output to `dist/`.

- Literal use: for stage acts, write "conjuring" or "illusion"; in code, write `magic number`, `magic bytes` or `__magic__` in inline code; for the card game, write `Magic: The Gathering` in inline code.
