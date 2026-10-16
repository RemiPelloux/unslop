From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 259. `underpinning`

- Kind: noun. Banned forms: `underpinning`, `underpinnings`. The verb `underpin` has its own entry.
- Why it reads as machine text: `the underpinnings of` is a model's phrase for the theory or structure behind something. It sounds rigorous, like an engineering drawing, and then usually introduces a summary at a basic level. It hides which ideas or components the writer means.
- Where it shows up: explainer intros, academic-style essays, architecture overviews.

```slop
This chapter explores the theoretical underpinnings of reinforcement learning.
The technical underpinnings of the platform are built on Kubernetes.
Understanding the psychological underpinnings of habit formation helps designers.
```

Replace with:

- "basis", "theory" or "foundations" for ideas, then name them.
- "runs on" or "is built from" for systems, with the component list.
- "causes" or "reasons" for behavior.
- Cut it when the next sentence names the theory.

Rewrites:

```slop
This chapter explores the theoretical underpinnings of reinforcement learning.
```

After: This chapter covers Markov decision processes, the Bellman equation and policy gradients.

```slop
The technical underpinnings of the platform are built on Kubernetes.
```

After: The platform runs on Kubernetes 1.30, with Postgres for state and NATS for messages.

```slop
Understanding the psychological underpinnings of habit formation helps designers.
```

After: Habits form when a cue, an action and a reward repeat in the same order; designers control where the cue appears.

- Literal use: in a construction spec for supporting a foundation, put `underpinning` in inline code or write "foundation support".
