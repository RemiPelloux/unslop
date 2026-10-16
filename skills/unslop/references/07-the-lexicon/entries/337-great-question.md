From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 337. `great question`

- Kind: opener. Banned forms: `great question`, `good question`, `that's a great question`, `excellent question`.
- Why it reads as machine text: `Great question!` is the sycophantic opener tuned into chat assistants by preference training, where raters rewarded warmth. It praises the question before answering it, so every question gets the same grade. In a pull request reply or code comment it reads as a bot talking.
- Where it shows up: the first line of chat answers, support replies, and replies to code review comments.

```slop
Great question! The difference between `==` and `===` is type coercion.
That's a great question, and one that many developers ask.
Good question! Let me explain how the event loop works.
```

Replace with:

- The answer as the first sentence.
- If the question exposes a gap in docs, say so and link the fix: "The docs don't cover this; I added a section."
- In review replies, the answer or the change you made.
- Cut it every time.

Rewrites:

```slop
Great question! The difference between `==` and `===` is type coercion.
```

After: `==` converts types before comparing, so `0 == ""` is true; `===` does not convert, so `0 === ""` is false.

```slop
That's a great question, and one that many developers ask.
```

After: The cache does not invalidate on deploy; you have to call `purge()` in the release script.

```slop
Good question! Let me explain how the event loop works.
```

After: The event loop runs one task, then all queued microtasks, then renders, then picks the next task.

- Literal use: when a question changes the plan, say what it changed: "Your question about time zones found a bug; fix in #412."
