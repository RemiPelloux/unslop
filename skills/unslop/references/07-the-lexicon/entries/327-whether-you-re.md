From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 327. `whether you're`

- Kind: phrase. Banned forms: `whether you're`, `whether you are a`, `whether you're a beginner or a pro`.
- Why it reads as machine text: `Whether you're a beginner or a seasoned pro` names two poles of an audience to claim it serves everyone. Models write this two-pole sentence at the top of tutorials and product pages because briefs rarely name a reader. A text written for everyone fits nobody, and the phrase admits it.
- Where it shows up: tutorial intros, course pages, and product heroes.

```slop
Whether you're a beginner or a seasoned pro, this guide has something for you.
Whether you're building a blog or an enterprise app, our framework scales.
Whether you're on the go or at your desk, stay connected.
```

Replace with:

- The one reader you wrote for, named: "This guide is for developers who know Git and have never used rebase."
- Two paths with labels, if you serve two audiences: "New to Git: start at 2.1. Already use it: skip to 4."
- The actual limits: smallest and largest supported case, in numbers.
- Cut it when the poles are invented; pick the reader.

Rewrites:

```slop
Whether you're a beginner or a seasoned pro, this guide has something for you.
```

After: This guide is for developers who use Git daily and have never run `git rebase -i`.

```slop
Whether you're building a blog or an enterprise app, our framework scales.
```

After: Sites built with the framework range from 3 pages to 40,000; build time grows about linearly.

```slop
Whether you're on the go or at your desk, stay connected.
```

After: The app syncs between phone and desktop within 2 seconds.

- Literal use: in a form or a branching instruction, write the condition as "If you are X, do Y."
