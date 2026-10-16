From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 335. `feel free to`

- Kind: phrase. Banned forms: `feel free to`, `please feel free`, `you're welcome to`.
- Why it reads as machine text: `feel free to` grants permission the reader did not need. Chat assistants close almost every answer with `Feel free to ask if you have more questions`, and generated docs use it for every optional step. The phrase hides whether the action is required, optional, or a good idea.
- Where it shows up: chat closers, CONTRIBUTING files, and documentation for optional settings.

```slop
Feel free to ask if you have any other questions.
Feel free to open an issue or submit a pull request.
Feel free to adjust the timeout to suit your needs.
```

Replace with:

- The imperative, when you want the action: "Open an issue."
- A condition, when it depends: "If requests time out on slow networks, raise `timeout` to 30s."
- The process, for contributions: where, what format, who reviews.
- Cut it when it closes a chat answer; the user knows they can reply.

Rewrites:

```slop
Feel free to ask if you have any other questions.
```

After: (Delete the line. End on the answer.)

```slop
Feel free to open an issue or submit a pull request.
```

After: Report bugs as GitHub issues with steps to reproduce. PRs need one approving review and passing CI.

```slop
Feel free to adjust the timeout to suit your needs.
```

After: The default timeout is 10s. Raise it to 30s if you call the API from a mobile network.

- Literal use: none. Say whether the action is required or optional.
