From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 118. `elegant`

- Kind: adjective. Banned forms: `elegant`, `elegantly`.
- Why it reads as machine text: `elegant` is the praise models give to code, fonts and answers. In engineering it approves code without naming the virtue, which might be fewer lines, fewer branches or no shared state. In design copy it pairs with `minimal` and `timeless` as generic luxury.
- Where it shows up: code review comments, font and template marketplaces, wedding copy.

```slop
An elegant solution to a complex problem.
This elegant serif font is perfect for branding.
The code is clean and elegant.
```

Replace with:

- The code property: "3 nested loops replaced by one dictionary lookup, 40 lines to 12". Use for code.
- The font specs: "high-contrast serif, 6 weights, small caps and old-style figures". Use for type.
- The readability rule it meets: "each function under 20 lines, no shared mutable state". Use for review comments.
- Cut it when you mean "I like it", and say what to keep.

Rewrites:

```slop
An elegant solution to a complex problem.
```

After: Replaces 3 nested loops with one dictionary lookup, cutting the function from 40 lines to 12.

```slop
This elegant serif font is perfect for branding.
```

After: A high-contrast serif in 6 weights, with small caps and old-style figures.

```slop
The code is clean and elegant.
```

After: Each function is under 20 lines, and none of them share mutable state.

- Literal use: in mathematics, say what makes the proof short: "a proof with no case analysis".
