From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 254. `harmony`

- Kind: noun. Banned forms: `harmony`, `harmonies`. The adjective `harmonious` has its own entry.
- Why it reads as machine text: Models use `harmony` for things that fit together and for calm among people. In design writing, `visual harmony` and `color harmony` stand in for actual rules about spacing, scale and contrast. The word names a good feeling about the result and hides how it was reached.
- Where it shows up: design system docs, color and type advice, team culture copy.

```slop
The palette creates visual harmony across the interface.
Our tools work in harmony with your existing stack.
We believe in harmony between work and life.
```

Replace with:

- The rule: "one accent color, used only for primary actions".
- "consistent", with what is consistent: the spacing scale, the type scale.
- "works with", plus the named tools.
- Cut it when the sentence is about mood; state the policy instead.

Rewrites:

```slop
The palette creates visual harmony across the interface.
```

After: The palette has one accent, `#B4441C`, used only for primary buttons and links; everything else is ink on paper.

```slop
Our tools work in harmony with your existing stack.
```

After: The CLI reads your existing `package.json` scripts and `.env` files; nothing has to move.

```slop
We believe in harmony between work and life.
```

After: No meetings after 4 pm, and every on-call week ends with a day off.

- Literal use: in music theory, name the chords or intervals, or put `harmony` in inline code; for color schemes, name the scheme ("complementary", "analogous").
