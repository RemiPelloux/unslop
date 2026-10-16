From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 296. `whereby`

- Kind: relative adverb. Banned forms: `whereby`, `a process whereby`, `a system whereby`.
- Why it reads as machine text: `whereby` introduces a clause that defines a process, and it comes with a vague noun in front (`a mechanism whereby`). The construction delays the verb and hides who acts. Models use it to sound formal when describing any workflow.
- Where it shows up: policy pages, architecture docs, and glossary definitions.

```slop
We use a system whereby each request is assigned a unique ID.
This is a process whereby users verify their email.
The protocol defines a mechanism whereby nodes agree on a leader.
```

Replace with:

- An active sentence with the actor as subject: "The gateway assigns each request an ID."
- "in which" or "where" if you must keep the clause.
- A numbered list when the process has steps.
- Cut it when the noun before it ("system", "process") adds nothing.

Rewrites:

```slop
We use a system whereby each request is assigned a unique ID.
```

After: The gateway assigns each request a UUID and passes it in the `X-Request-Id` header.

```slop
This is a process whereby users verify their email.
```

After: To verify an email, the user clicks a link we send that expires after 24 hours.

```slop
The protocol defines a mechanism whereby nodes agree on a leader.
```

After: Nodes elect a leader by majority vote; a node that hears no heartbeat for 300ms starts an election.

- Literal use: none outside legal drafting. Use "where" or "in which".
