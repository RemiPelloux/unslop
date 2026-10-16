From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 233. `intricacies`

- Kind: noun. Banned forms: `intricacies`. The singular `intricacy` passes the linter but has the same problem, and `intricate` has its own entry.
- Why it reads as machine text: `the intricacies of` is a model's way of saying "the details of" with an extra claim that the details are hard. It appears in openings that promise depth and then explain at a beginner level. The word is almost always plural and almost never followed by a list.
- Where it shows up: tutorial intros, course descriptions, job ads (`understand the intricacies of distributed systems`).

```slop
In this guide, we'll explore the intricacies of React's rendering cycle.
You'll need to master the intricacies of Kubernetes networking.
Understanding the intricacies of tax law is key for founders.
```

Replace with:

- "details", "rules" or "edge cases", then list them.
- "how X works" for the intro of an explanation.
- The 2 or 3 hard parts, named.
- Cut it when the following sections already cover the details.

Rewrites:

```slop
In this guide, we'll explore the intricacies of React's rendering cycle.
```

After: This guide covers when React re-renders a component, why `useEffect` runs twice in strict mode, and how `memo` skips a render.

```slop
You'll need to master the intricacies of Kubernetes networking.
```

After: You will configure Services, Ingress rules and NetworkPolicies, and debug DNS from inside pods.

```slop
Understanding the intricacies of tax law is key for founders.
```

After: Founders need 3 tax rules: when to register for VAT, how stock options are taxed, and when the R&D credit claim is due.

- Literal use: the word has no technical sense; write "details" and list them.
