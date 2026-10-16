From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 317. `pave the way`

- Kind: phrase. Banned forms: `pave the way`, `paves the way for`, `paving the way`, `lay the groundwork`.
- Why it reads as machine text: `paves the way for` describes a change by what it might enable later, so the change itself goes unnamed. Models use it to inflate a small step ("this refactor paves the way for future features"). The future features are never listed.
- Where it shows up: PR descriptions, roadmap posts, and grant applications.

```slop
This refactor paves the way for future improvements.
Her research paved the way for modern vaccines.
The new API lays the groundwork for a plugin system.
```

Replace with:

- "lets us" or "unblocks" followed by the named next step.
- "is required for" when the change is a prerequisite.
- The specific later result and the link between the two.
- Cut it when the future step is not planned; describe the change on its own terms.

Rewrites:

```slop
This refactor paves the way for future improvements.
```

After: This refactor splits `Editor` into 4 components, so we can lazy-load the toolbar next sprint.

```slop
Her research paved the way for modern vaccines.
```

After: Her 2005 paper showed how to stop the immune system attacking synthetic mRNA; both 2020 mRNA vaccines use that method.

```slop
The new API lays the groundwork for a plugin system.
```

After: The new API exposes hooks for save and export; plugins will register against them in v3.

- Literal use: for road work, write "pave the road" or "resurface the car park".
