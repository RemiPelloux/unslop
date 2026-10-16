From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 241. `holy grail`

- Kind: noun phrase. Banned forms: `holy grail`, `Holy Grail`.
- Why it reads as machine text: The phrase names a goal everyone wants and nobody reaches, and models use it for layout problems, metrics and products (`the holy grail of productivity`). It treats a problem with known partial answers as mythical, which hides the approaches that already exist. In CSS writing it is also a real layout name, which models then stretch to cover anything.
- Where it shows up: tech blogs, product marketing, research summaries.

```slop
Zero-downtime deploys are the holy grail of DevOps.
Finding product-market fit is the holy grail for every startup.
Inbox zero, the holy grail of productivity, is finally within reach.
```

Replace with:

- "hard goal" or "long-standing goal", with why it is hard.
- The existing approaches and their limits.
- "ideal" for a target state, followed by how close you are.
- Cut it when the topic is a known technique with documentation.

Rewrites:

```slop
Zero-downtime deploys are the holy grail of DevOps.
```

After: Zero-downtime deploys need blue-green or rolling releases, plus database migrations that work with both the old and the new code.

```slop
Finding product-market fit is the holy grail for every startup.
```

After: One common test for product-market fit is whether 40% of surveyed users say they would be very disappointed to lose the product.

```slop
Inbox zero, the holy grail of productivity, is finally within reach.
```

After: The app files newsletters and receipts into folders, so most people's inbox drops below 20 messages.

- Literal use: for the CSS pattern, write `holy grail layout` in inline code or "three-column layout with header and footer"; for the Arthurian object, write "the Grail".
