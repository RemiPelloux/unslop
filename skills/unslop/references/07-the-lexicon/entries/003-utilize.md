From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 003. `utilize`

- Kind: verb. Banned forms: `utilize`, `utilizes`, `utilized`, `utilizing`, `utilization`, and the `-ise` spellings.
- Why it reads as machine text: Three syllables where "use" has one. The US federal plain-language guidelines list it with "use" as the replacement, and model output still produces it because report and grant text is full of it. It adds formality and nothing else; no sentence changes meaning when "use" replaces it. Some editors defend a narrow sense (use for an unintended purpose), but generated text never means that.
- Where it shows up: design docs, API reference prose, academic and government writing.

```slop
The service utilizes a message queue to decouple producers and consumers.
Users can utilize the settings panel to configure notifications.
This function utilizes recursion to traverse the tree.
```

Replace with:

- `use` everywhere.
- Name the action when "use" is still vague: "reads from", "writes to", "calls".
- Cut it when the tool can be the subject of the sentence.

Rewrites:

```slop
The service utilizes a message queue to decouple producers and consumers.
```

After: Producers write to a RabbitMQ queue and consumers read from it, so either side can restart without losing jobs.

```slop
Users can utilize the settings panel to configure notifications.
```

After: Turn notifications on or off in Settings > Notifications.

```slop
This function utilizes recursion to traverse the tree.
```

After: This function walks the tree recursively.

- Literal use: for the metric, write "CPU usage" or "load", or quote the field name in inline code (`cpu_utilization`).
