From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 156. `crisp`

- Kind: adjective. Banned forms: `crisp`, `crisper`, `crispest`, `crisply`, `crispness`.
- Why it reads as machine text: Design-review shorthand that models apply to type, icons and copy alike: `crisp typography`, `crisp UI`. It names a feeling of sharpness and hides the property that produces it: whole-pixel rendering, contrast ratio, stroke weight, sentence length. Dribbble captions pair it with `clean` so often the two read as one word.
- Where it shows up: design reviews, Dribbble-style captions, writing feedback.

```slop
Crisp typography and clean layouts throughout.
The icons look crisp on every display.
Keep the copy crisp.
```

Replace with:

- For type, size, weight and contrast: "Body 16px IBM Plex Sans, #1A1A18 on #F7F5F0, 16:1."
- For icons, grid, stroke and format: "20px grid, 1.5px stroke, SVG, so edges stay sharp at 2x and 3x."
- For copy, the length rule: "Button labels two words at most; error messages under 80 characters."
- Cut it when nothing measurable follows it.

Rewrites:

```slop
Crisp typography and clean layouts throughout.
```

After: Body text is 16px at 1.5 line height and 16:1 contrast; every page uses one 66ch column.

```slop
The icons look crisp on every display.
```

After: Icons are SVG on a 20px grid with 1.5px strokes on whole pixels, so they stay sharp at 1x, 2x and 3x.

```slop
Keep the copy crisp.
```

After: Keep button labels to two words and error messages under 80 characters.

- Literal use: for food, write "crunchy"; for pixel art scaling, the CSS value `image-rendering: crisp-edges` stays in code and the prose says "sharp edges, no smoothing".
