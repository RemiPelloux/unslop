From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 093. `meticulous`

- Kind: adjective. Banned forms: `meticulous`, `meticulously`.
- Why it reads as machine text: `meticulous` is self-praise that models write into cover letters and studio pages, and into accounts of their own work (`I meticulously reviewed`). It asserts care while giving no evidence of it. A reader cannot check care; they can check an error rate or a checklist.
- Where it shows up: cover letters, studio "About" pages, assistants describing their own process.

```slop
I am a meticulous professional with a keen eye for detail.
Every product is meticulously crafted by hand.
I have meticulously reviewed your code for errors.
```

Replace with:

- The error rate or audit result: "no billing errors across 3,000 invoices in 2024". Use for CVs.
- The process step: "one person stitches each bag and a second checks it against 12 points". Use for products.
- What was checked and what was not: "read all 4 changed files and ran the tests; did not check the migrations". Use for code review.
- Cut it when describing yourself, and give the record.

Rewrites:

```slop
I am a meticulous professional with a keen eye for detail.
```

After: I processed 3,000 invoices in 2024, and the annual audit found no billing errors.

```slop
Every product is meticulously crafted by hand.
```

After: One person stitches each bag, and a second checks it against a 12-point list before it ships.

```slop
I have meticulously reviewed your code for errors.
```

After: I read all 4 changed files and ran the tests. Two fail, both in `parse_date`. I did not check the SQL migrations.

- Literal use: there is no separate literal sense; write "careful" and attach the evidence: "every figure was checked against the source PDF".
