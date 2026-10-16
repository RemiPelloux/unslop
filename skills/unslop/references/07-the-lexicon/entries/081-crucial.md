From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 081. `crucial`

- Kind: adjective. Banned forms: `crucial`, `crucially`.
- Why it reads as machine text: `crucial` is the default intensifier models use for "important", most often in `it is crucial to` before an instruction. It sounds urgent but never says what happens if the reader ignores the advice. Generated tutorials put it on every second step, so it stops marking anything.
- Where it shows up: tutorials, onboarding checklists, policy summaries.

```slop
It is crucial to back up your database before upgrading.
The survey offers crucial insights into customer behavior.
Communication is crucial for remote teams.
```

Replace with:

- The consequence: "upgrading without a backup can lose every row since the last snapshot". Use for warnings.
- The imperative alone: "Back up the database before you upgrade." Use for instructions; the order of the steps is the emphasis.
- The finding: "62% of carts are abandoned on the shipping-cost page". Use for research summaries.
- The practice: "post a written update by 10:00 each day". Use for advice.
- Cut it whenever `it is crucial to` opens a sentence, and start with the verb.

Rewrites:

```slop
It is crucial to back up your database before upgrading.
```

After: Back up the database before you upgrade. The 4.0 migration cannot be undone.

```slop
The survey offers crucial insights into customer behavior.
```

After: 62% of carts are abandoned on the page that first shows shipping costs.

```slop
Communication is crucial for remote teams.
```

After: On a remote team, post a written update by 10:00 each day so nobody waits for a call to learn the status.

- Literal use: for the deciding experiment in science, write "the deciding test".
