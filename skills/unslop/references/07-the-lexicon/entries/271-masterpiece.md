From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 271. `masterpiece`

- Kind: noun. Banned forms: `masterpiece`, `masterpieces`.
- Why it reads as machine text: Models give the label `masterpiece` to well-made things in reviews, product copy and even code review (`a masterpiece of engineering`). It is the highest possible rating applied to ordinary work, so it reads as flattery. It hides what is good about the work.
- Where it shows up: product reviews, portfolio copy, praise in pull request comments.

```slop
This watch is a masterpiece of Swiss engineering.
Your refactor is a masterpiece.
The new campus is an architectural masterpiece.
```

Replace with:

- The qualities, named: precision, materials, measured performance.
- "well made" or "good", with the reason.
- In code review, the specific change you liked and why.
- Cut it when the praise has no reason.

Rewrites:

```slop
This watch is a masterpiece of Swiss engineering.
```

After: The watch movement keeps time within 2 seconds a day and has 28 jewels.

```slop
Your refactor is a masterpiece.
```

After: Splitting `parseOrder` into 3 functions made the tests readable, and the error cases are now covered.

```slop
The new campus is an architectural masterpiece.
```

After: The campus uses timber frames and planted roofs, and its 6 buildings share one heat pump plant.

- Literal use: for the guild sense or in art history, write "major work" or put `masterpiece` in inline code.
