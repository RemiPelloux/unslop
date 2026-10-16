From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 280. `essentially`

- Kind: adverb, connective. Banned forms: `essentially`, and the adjective `essential` (its own entry).
- Why it reads as machine text: `essentially` lets a model simplify without saying what it left out. It opens sentences that restate the previous one in looser words (`Essentially, what this means is`), so it signals repetition. It is also a form of `essential`, which is banned on its own.
- Where it shows up: explanations of technical concepts, summaries, support answers.

```slop
Essentially, a closure is a function that remembers its scope.
The new plan is essentially the same as the old one.
Essentially, what this means is that you need to restart the server.
```

Replace with:

- The full definition, including the edge that the adverb skipped.
- "nearly" or "the same except", with the difference named.
- "basically" has the same problem; do not swap one for the other.
- Cut it when the sentence restates the last one; delete the restatement.

Rewrites:

```slop
Essentially, a closure is a function that remembers its scope.
```

After: A closure is a function together with the variables of the scope where it was created; it can read and change them after that scope returns.

```slop
The new plan is essentially the same as the old one.
```

After: The new plan matches the old one, except that support moves from email to chat.

```slop
Essentially, what this means is that you need to restart the server.
```

After: Restart the server to apply the change.

- Literal use: the word has no literal sense; state the definition, or write "in short" before a one-line summary.
