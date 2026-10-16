From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 072. `robust`

- Kind: adjective. Banned forms: `robust`, `robustly`, `robustness`.
- Why it reads as machine text: models call any code with a try/catch `robust`, and any platform the reader is meant to trust. The word fakes an engineering review that never happened: no load test, no failure injection, no uptime figure. In generated READMEs it sits in a row with "scalable" and "secure", three words that tell an evaluator nothing.
- Where it shows up: README openers, architecture docs, pull request descriptions.

```slop
A robust and scalable framework for building APIs.
Added robust error handling to the upload flow.
Our robust infrastructure keeps your data safe.
```

Replace with:

- The failure it survives: "retries failed uploads 3 times with exponential backoff". Use for error handling.
- The measured limit: "tested at 12,000 requests per second on one 4-core node". Use for performance.
- The uptime record: "99.95% uptime over the last 12 months, status page linked". Use for hosting.
- The test that tried to break it: "fuzzed with 2 million malformed inputs, no crashes". Use for parsers and protocols.
- Cut it when the sentence describes a feature and the adjective only adds praise.

Rewrites:

```slop
A robust and scalable framework for building APIs.
```

After: A Go framework for HTTP APIs. It serves 12,000 requests per second on one 4-core node.

```slop
Added robust error handling to the upload flow.
```

After: Uploads now retry 3 times with exponential backoff and show the server's error if the last attempt fails.

```slop
Our robust infrastructure keeps your data safe.
```

After: Data is stored in two regions, with nightly backups kept for 30 days.

- Literal use: for the statistical sense, name the method ("a median-based estimate that ignores outliers"), or put a library parameter such as `robust=True` in inline code.
