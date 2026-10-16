From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 169. `cohesive`

- Kind: adjective. Banned forms: `cohesive`, `cohesively`, `cohesiveness`.
- Why it reads as machine text: It is the stock approval and stock complaint in model-written design reviews: `the screens feel cohesive`, `make it more cohesive`. It claims consistency without naming the shared tokens or the rule that produces them. A designer reading the comment cannot act on it, so the next round changes colors at random.
- Where it shows up: design system pitches, design review comments, brand guidelines.

```slop
A cohesive design system across web and mobile.
The new screens don't feel cohesive yet.
A cohesive brand experience at every touchpoint.
```

Replace with:

- The shared source: one token file, one icon set, one component library, and who reads them.
- For review comments, the exact inconsistency and the value to match.
- For brand, the places and the shared elements, listed.
- Cut it when you cannot point to a token or a rule.

Rewrites:

```slop
A cohesive design system across web and mobile.
```

After: Web and iOS read the same token file: 10 spacing steps, 9 type sizes, one 2px radius.

```slop
The new screens don't feel cohesive yet.
```

After: Settings uses 12px gaps and an 8px radius; the rest of the app uses 16px and 2px. Match the rest.

```slop
A cohesive brand experience at every touchpoint.
```

After: Invoices, emails and the app use the same serif headings and the same single accent color.

- Literal use: in software design, the noun "cohesion" is the term ("each function in the module works on the same data"); in physics, write "cohesion" as well.
