From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 311. `let's dive`

- Kind: opener. Banned forms: `let's dive`, `let's dive in`, `let's jump in`, `let's get started`.
- Why it reads as machine text: `Let's dive in` closes an introduction that should not exist and announces the content instead of starting it. Chat models and generated tutorials use it as the bridge between a preamble and the first heading. The "let's" adds a fake sense of doing it together.
- Where it shows up: tutorials, YouTube scripts turned into posts, and chat answers longer than a few paragraphs.

```slop
Now that we've covered the basics, let's dive in.
Let's dive into the code and see how it works.
Ready to get started? Let's jump in.
```

Replace with:

- The first step, as a heading or an imperative: "Install the CLI."
- A one-line scope at the top: "This guide covers setup and the first deploy."
- Nothing; delete the introduction it closes.
- Cut it when the next line is the content; it always is.

Rewrites:

```slop
Now that we've covered the basics, let's dive in.
```

After: Step 1: install the CLI with `npm i -g fly`.

```slop
Let's dive into the code and see how it works.
```

After: The handler in `api/upload.ts` reads the file, checks its type, and writes it to S3.

```slop
Ready to get started? Let's jump in.
```

After: Create a project with `npm create vite@latest`.

- Literal use: for swimming, write "dive" in a sentence about the water: "Dive from the 3m board."
