From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 348. `when it comes to`

- Kind: phrase. Banned forms: `when it comes to`, `when it comes down to`, `in terms of`.
- Why it reads as machine text: `When it comes to X,` fronts the topic before the sentence starts, and the main clause then has a weak subject ("it", "there"). Models use the shape to change topics between paragraphs without a real transition. It adds four words and moves the subject to the wrong place.
- Where it shows up: comparison articles, advice posts, and chat answers.

```slop
When it comes to performance, Go is hard to beat.
When it comes to styling, there are many options.
When it comes to testing, it's best to start small.
```

Replace with:

- The topic as the subject of the sentence: "Go compiles to one binary and starts in 10ms."
- The options, listed, for "many options" lines.
- The instruction, directly: "Write one test for the checkout total first."
- Cut it when the topic is already the subject of the paragraph.

Rewrites:

```slop
When it comes to performance, Go is hard to beat.
```

After: Our Go service handles 4 times the requests of the Python one on the same hardware.

```slop
When it comes to styling, there are many options.
```

After: Style React with CSS modules, Tailwind, or a CSS-in-JS library; we use CSS modules.

```slop
When it comes to testing, it's best to start small.
```

After: Start with one test for the checkout total, the function that loses money when it breaks.

- Literal use: for an event that may happen, write "if" or "when" with a plain verb: "When the order arrives, scan the code."
