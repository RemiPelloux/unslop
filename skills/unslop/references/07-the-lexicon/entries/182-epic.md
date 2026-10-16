From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 182. `epic`

- Kind: adjective and noun. Banned forms: `epic`, `epics`, `epically`.
- Why it reads as machine text: Gaming and social-media slang that models use for guides, launches and pull requests. It clashes with technical register and signals hype before content. As a size word it hides the size.
- Where it shows up: tutorial titles, launch teasers, review comments.

```slop
An epic guide to Kubernetes networking.
Get ready for an epic product launch.
This PR is epic, thanks.
```

Replace with:

- The scope and length: word count, topics, diagrams.
- For a launch, what ships and on which date.
- In review, the effect of the change.
- For a big piece of work, its size: files touched, weeks spent, people involved.
- Cut it when the title already says "guide". Add the scope instead.

Rewrites:

```slop
An epic guide to Kubernetes networking.
```

After: Kubernetes networking: Services, Ingress and CNI plugins, in 9,000 words and 14 diagrams.

```slop
Get ready for an epic product launch.
```

After: On 4 November we release offline mode and the Linux app.

```slop
This PR is epic, thanks.
```

After: This cuts CI from 22 minutes to 9. Thanks.

- Literal use: for the Jira issue type, put it in inline code (`Epic`) or write "parent ticket"; for a long poem that tells a story, name the work (the Iliad, Beowulf).
