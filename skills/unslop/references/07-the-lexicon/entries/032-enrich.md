From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 032. `enrich`

- Kind: verb. Banned forms: `enrich`, `enriches`, `enriched`, `enriching`, `enrichment`.
- Why it reads as machine text: Two habits meet here: education copy (`enriching experiences`) and data pipeline jargon (`enrich the record`). Models use both, and both hide what was added. A record that went through that step has new fields; name them. In education copy it signals that the writer has not seen the syllabus.
- Where it shows up: course pages, data pipeline docs, CRM feature lists, school program descriptions.

```slop
An enriching learning experience for curious minds.
The pipeline enriches events with user metadata.
Enrich your content with AI-generated summaries.
```

Replace with:

- `add`, with the fields or content added.
- `join` or `look up` for data pipelines.
- Cut the adjective and describe the program.

Rewrites:

```slop
An enriching learning experience for curious minds.
```

After: A 6-week after-school course: build a weather station and log readings to a spreadsheet.

```slop
The pipeline enriches events with user metadata.
```

After: The pipeline looks up each event's `user_id` and adds `plan`, `country`, and `signup_date`.

```slop
Enrich your content with AI-generated summaries.
```

After: Each article gets a three-sentence summary at the top, generated and then checked by an editor.

- Literal use: for uranium, write "concentrated to 4% U-235"; for soil, write "fertilized" and name what was added.
