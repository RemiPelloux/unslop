From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 297. `albeit`

- Kind: conjunction. Banned forms: `albeit`, `albeit with`, `albeit slowly`.
- Why it reads as machine text: `albeit` tucks a concession into a short tail so the main claim keeps its weight and the limitation goes unread. Models use it to sound balanced while saying little about the cost (`albeit with some limitations`). The word is rare in spoken English and stands out in casual text.
- Where it shows up: comparison tables, review summaries, and changelogs.

```slop
The feature works, albeit with some limitations.
Performance improved, albeit slightly.
The new API is faster, albeit less flexible.
```

Replace with:

- "but" followed by the specific limitation.
- Two sentences when the limitation matters as much as the claim.
- The number, when "slightly" is the concession.
- Cut it when the concession is vague; name it or delete it.

Rewrites:

```slop
The feature works, albeit with some limitations.
```

After: Export works for files under 50 MB. Larger files time out.

```slop
Performance improved, albeit slightly.
```

After: Median response time fell from 210ms to 195ms.

```slop
The new API is faster, albeit less flexible.
```

After: The new API is 3 times faster but cannot filter on nested fields.

- Literal use: none. "Although" and "but" cover every case.
