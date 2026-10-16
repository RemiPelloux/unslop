From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 215. `linchpin`

- Kind: noun. Banned forms: `linchpin`, `linchpins`, `lynchpin`.
- Why it reads as machine text: `linchpin` is the model's choice when it wants to say one part holds the rest together. It sounds like engineering, yet nobody writing an incident review uses it; they write "single point of failure" or name the dependency. In praise of people (`she was the linchpin of the team`) it replaces any account of what the person did.
- Where it shows up: architecture overviews, farewell posts and performance reviews, strategy decks.

```slop
Redis is the linchpin of our caching strategy.
Maria was the linchpin of the platform team for five years.
Clear documentation is the linchpin of developer adoption.
```

Replace with:

- "single point of failure" when losing the part takes the system down, which is often the more honest framing.
- "depends on", with the dependent parts named.
- What the person did, as a list of results.
- Cut it when the claim is a slogan with no data under it.

Rewrites:

```slop
Redis is the linchpin of our caching strategy.
```

After: Every read path goes through Redis; when it is down, p95 latency rises from 40 ms to 900 ms.

```slop
Maria was the linchpin of the platform team for five years.
```

After: Maria ran the on-call rotation, owned the deploy pipeline, and reviewed about 1,200 pull requests in five years.

```slop
Clear documentation is the linchpin of developer adoption.
```

After: In our 2024 survey, 61% of new users said the quickstart page was the reason they kept using the API after the first week.

- Literal use: for the pin through an axle, write "axle pin".
