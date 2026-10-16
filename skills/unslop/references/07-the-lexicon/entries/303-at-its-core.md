From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 303. `at its core`

- Kind: opener. Banned forms: `at its core`, `at their core`, `at the core of`.
- Why it reads as machine text: `At its core,` promises that the sentence after it is the one definition that matters, then gives a broad paraphrase. Models start explainers with it (`At its core, Kubernetes is a container orchestrator`) because it frames a definition as a reveal. The reader learns nothing that the product name did not already say.
- Where it shows up: the first sentence of an explainer, "About" pages, and onboarding copy.

```slop
At its core, Kubernetes is a system for managing containers.
At its core, our product is about helping teams collaborate.
At the core of the design is a commitment to simplicity.
```

Replace with:

- The definition, starting with the subject and a concrete verb.
- The one action the product performs, for whom.
- The specific design rule, stated as a rule.
- Cut it when what follows is a definition; definitions need no frame.

Rewrites:

```slop
At its core, Kubernetes is a system for managing containers.
```

After: Kubernetes starts containers on a pool of machines and restarts them when they fail.

```slop
At its core, our product is about helping teams collaborate.
```

After: Teams use the app to review designs and leave comments pinned to a layer.

```slop
At the core of the design is a commitment to simplicity.
```

After: Each screen has one primary action and no more than 5 inputs.

- Literal use: for a CPU, write "per core" or "on each core"; for a reactor or an apple, "the core" without the "at its" frame.
