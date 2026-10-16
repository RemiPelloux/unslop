From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 300. `in summary`

- Kind: closer. Banned forms: `in summary`, `In summary,`, `in sum`.
- Why it reads as machine text: `In summary,` marks a paragraph that repeats the answer, and chat models attach one to nearly every long reply. The summary sits at the end, after the reader has already read everything it repeats. It often adds a vague benefit the body never claimed.
- Where it shows up: chat answers, generated documentation pages, and code review summaries.

```slop
In summary, hooks make React components easier to reuse.
In summary, there are several ways to fix this error.
In summary, the PR looks good with a few minor changes.
```

Replace with:

- The answer in the first sentence, so no summary is needed.
- A TL;DR line at the top of long pages.
- A list of the specific changes requested, for reviews.
- Cut it when the body is under a screen long.

Rewrites:

```slop
In summary, hooks make React components easier to reuse.
```

After: Move the fetch logic into `useUser()` and both pages can share it.

```slop
In summary, there are several ways to fix this error.
```

After: Fix it by adding `"type": "module"` to package.json; if you cannot, rename the file to `.mjs`.

```slop
In summary, the PR looks good with a few minor changes.
```

After: Approve after two changes: rename `tmp2` and add a test for the empty list.

- Literal use: for a section that sums up a report, title it "Summary" and place it first.
