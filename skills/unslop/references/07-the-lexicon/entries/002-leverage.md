From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 002. `leverage`

- Kind: verb (also noun). Banned forms: `leverage`, `leverages`, `leveraged`, `leveraging`.
- Why it reads as machine text: It came from finance (borrowing to multiply returns) through management consulting, and in generated text it means "use" in a suit. Models reach for it whenever a sentence pairs a tool with a goal, so `leverage Redis` and `leverage our expertise` appear at the same rate. It hides whether anything was multiplied; usually the tool was just called. Swap in "use"; if the sentence loses nothing, keep "use".
- Where it shows up: architecture docs, product pages, résumés and cover letters.

```slop
We leverage Postgres full-text search to power product discovery.
This library leverages WebAssembly for fast image processing.
Leverage our analytics to make smarter decisions.
```

Replace with:

- `use` in almost every case.
- `build on`, `reuse`, `call` when you want to say which part does the work.
- Cut it when the tool name already carries the sentence.

Rewrites:

```slop
We leverage Postgres full-text search to power product discovery.
```

After: Product search runs on Postgres full-text search (`tsvector` with a GIN index), so there is no separate search server.

```slop
This library leverages WebAssembly for fast image processing.
```

After: The library decodes and resizes images in WebAssembly, so it runs in the browser with no server round trip.

```slop
Leverage our analytics to make smarter decisions.
```

After: The analytics page shows which campaigns brought in paying customers last month.

- Literal use: in finance, write "debt" or "borrowing" and give the ratio (debt to equity of 2 to 1); for mechanics, write "lever".
