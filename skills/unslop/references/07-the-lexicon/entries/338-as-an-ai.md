From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 338. `as an ai`

- Kind: opener. Banned forms: `as an ai`, `as an AI language model`, `as a large language model`, `I'm just an AI`.
- Why it reads as machine text: `As an AI language model, I cannot` is the refusal and disclaimer template of early chat assistants, and it now marks text as pasted from a chat window. It puts the speaker's nature ahead of the information, and often precedes an answer the model gives anyway. In code comments and docs it is a sign nobody edited the output.
- Where it shows up: chat refusals, generated reviews and essays, and code comments from assistants.

```slop
As an AI language model, I don't have personal opinions, but here are some options.
// As an AI, I cannot run this code, but it should work.
As an AI, I don't have access to real-time data.
```

Replace with:

- The limit, stated as a fact about the task: "I have not run this code."
- What the reader can do to check: the command, the source, the date of the data.
- A recommendation with its reason, when asked for an opinion.
- Cut it when the sentence after it stands on its own.

Rewrites:

```slop
As an AI language model, I don't have personal opinions, but here are some options.
```

After: For a team of 3 with no ops staff, use a managed host such as Render; self-host only if cost is the main concern.

```slop
// As an AI, I cannot run this code, but it should work.
```

After: Not yet run. Check with `pytest tests/test_parse.py` before merging.

```slop
As an AI, I don't have access to real-time data.
```

After: My data ends in June 2026; check the vendor's pricing page for current prices.

- Literal use: when a product must disclose that a bot replies, say so in a label: "Replies on this page are written by a bot and checked by staff within 24 hours."
