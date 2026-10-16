From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 157. `clean`

- Kind: adjective, also a verb. Banned forms: `clean`, `cleaner`, `cleanest`, `cleanly`, `cleaned`, `cleaning`, `cleans`, `cleanness`.
- Why it reads as machine text: It is the most common praise word in model-written design and code reviews: `clean UI`, `clean code`, `clean API`. It approves without naming what was removed or which rule the work follows. In design it usually describes the default: a white shadcn `Card` with `rounded-xl`, Inter, and an `indigo-500` button, which reads as unfinished.
- Where it shows up: design reviews, PR descriptions, landing page heroes, code review comments.

```slop
A clean, modern interface your team will love.
Refactored the module for cleaner code.
Love how clean this layout is.
```

Replace with:

- For design, what was removed and the rule that remains: "one accent color, 1px rules instead of cards, 24px between sections".
- For code, the measurable change: files split, lines removed, functions under a size limit, tests unchanged.
- For a review comment, the decision you approve and why it works.
- Cut it when the sentence praises without informing.

Rewrites:

```slop
A clean, modern interface your team will love.
```

After: One 66ch column, one accent color (#B4441C), and 1px rules between sections instead of cards.

```slop
Refactored the module for cleaner code.
```

After: Split `billing.ts` (1,100 lines) into four files and removed two unused exports. Tests unchanged.

```slop
Love how clean this layout is.
```

After: The 24px gap between groups and the single accent color make the primary action obvious. Approve.

- Literal use: for git, write "no uncommitted changes"; for data, write "deduplicated" or "validated" and name the checks; for a build, write "deleted the build output" (`make clean` stays in code).
