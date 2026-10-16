From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 163. `lightning-fast`

- Kind: adjective. Banned forms: `lightning-fast`, `lightning fast`.
- Why it reads as machine text: Same family as `blazing`, common in SaaS hero copy for search, deploys and support. Models write it before anyone has measured anything. It claims speed and gives the reader nothing to hold the vendor to.
- Where it shows up: hero copy, search features, support pages.

```slop
Lightning-fast search across all your docs.
Deploy in lightning-fast time.
Lightning-fast support from real humans.
```

Replace with:

- Search: index size and latency at a percentile.
- Deploys: median and p95 time from push to live.
- Support: the first-reply commitment, with hours and time zone.
- Cut it when the number is unflattering. Fix the speed, then publish the number.

Rewrites:

```slop
Lightning-fast search across all your docs.
```

After: Search returns results in under 100ms at p95 across up to 200,000 pages.

```slop
Deploy in lightning-fast time.
```

After: Median 38 seconds from `git push` to live; p95 is 2 minutes.

```slop
Lightning-fast support from real humans.
```

After: A support engineer replies within 2 business hours, Monday to Friday, 09:00 to 18:00 CET.

- Literal use: for weather, write "lightning" by itself and keep speed claims out of the sentence.
