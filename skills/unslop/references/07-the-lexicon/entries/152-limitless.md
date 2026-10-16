From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 152. `limitless`

- Kind: adjective. Banned forms: `limitless`, `limitlessly`, `limitlessness`.
- Why it reads as machine text: Models use it on pricing pages and API docs, where it becomes a promise the fair-use clause breaks. Motivational copy uses it for "potential". In both places it replaces a number the reader needs.
- Where it shows up: pricing tables, API marketing, self-help copy.

```slop
Limitless API calls on every plan.
Your potential is limitless.
Enjoy limitless projects and collaborators.
```

Replace with:

- The quota and what happens at it: "100,000 calls a day; above that, requests return 429 until 00:00 UTC."
- "No cap on X" only when true, with the fair-use rule if one exists.
- The next step the reader can take, in place of a motivational line.
- Cut it when there is a limit. There always is one.

Rewrites:

```slop
Limitless API calls on every plan.
```

After: Every plan includes 100,000 API calls a day. Above that, requests return HTTP 429 until midnight UTC.

```slop
Your potential is limitless.
```

After: Finish the first module in about 40 minutes; it ends with a working form.

```slop
Enjoy limitless projects and collaborators.
```

After: No cap on projects or collaborators. Storage is 100 GB per workspace.

- Literal use: for a config value that disables a cap, write "no limit" and show the setting, such as `max_connections = 0`.
