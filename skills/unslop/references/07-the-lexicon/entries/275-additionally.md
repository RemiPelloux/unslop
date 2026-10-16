From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 275. `additionally`

- Kind: adverb, connective. Banned forms: `additionally`.
- Why it reads as machine text: `additionally` is the model's formal version of "also", and it often opens a sentence that would read better joined to the one before. In generated docs, every feature paragraph after the first starts with it. It adds five syllables and no meaning.
- Where it shows up: feature lists written as prose, README files, emails.

```slop
Additionally, you can export reports as PDF.
Additionally, the plugin supports dark mode.
The service is HIPAA-compliant. Additionally, data is encrypted at rest.
```

Replace with:

- "also" in the middle of the sentence: "You can also export reports as PDF."
- One bulleted list, when there are 3 or more items.
- "and" to join two related facts.
- Cut it when the sentence starts a new paragraph; the break already signals a new point.

Rewrites:

```slop
Additionally, you can export reports as PDF.
```

After: Reports export as PDF or CSV.

```slop
Additionally, the plugin supports dark mode.
```

After: The plugin follows the system dark mode setting.

```slop
The service is HIPAA-compliant. Additionally, data is encrypted at rest.
```

After: The service is HIPAA-compliant and encrypts data at rest with AES-256.

- Literal use: the word has no literal sense; for an amount added, write "extra" or give the number.
