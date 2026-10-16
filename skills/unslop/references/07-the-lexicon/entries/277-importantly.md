From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 277. `importantly`

- Kind: adverb, connective. Banned forms: `importantly`, `more importantly`, `most importantly`.
- Why it reads as machine text: `importantly` is a model's flag for "pay attention here", most often as `more importantly` or `most importantly`. It ranks without explaining, and in generated text it marks a point no more important than the rest. If the point matters, the reader needs the consequence, not the label.
- Where it shows up: instructions, summaries, persuasive answers.

```slop
Importantly, you must back up your data before upgrading.
More importantly, the change improves accessibility.
Most importantly, have fun with it.
```

Replace with:

- The consequence: "the upgrade deletes the old index, so back up first".
- The most important point placed first in the paragraph or list.
- A warning callout in docs, with the failure stated.
- Cut it when the point is not the most important one, which is most of the time.

Rewrites:

```slop
Importantly, you must back up your data before upgrading.
```

After: Back up your data before upgrading; the upgrade rewrites the database and cannot be undone.

```slop
More importantly, the change improves accessibility.
```

After: The change adds a label to every form field, so screen readers announce each one.

```slop
Most importantly, have fun with it.
```

After: Delete the line; a closing pep talk adds nothing to a tutorial.

- Literal use: the word has no literal sense; "important" as an adjective is allowed when the sentence says why.
