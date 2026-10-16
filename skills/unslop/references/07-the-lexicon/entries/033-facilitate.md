From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 033. `facilitate`

- Kind: verb. Banned forms: `facilitate`, `facilitates`, `facilitated`, `facilitating`.
- Why it reads as machine text: Bureaucratic and academic register for "help" or "allow", common in grant text and policy. Models use it to sound formal, and it blurs the subject: what does what, and how. When a person does this for a meeting, "run" or "lead" is shorter. It makes a sentence longer while hiding who acts.
- Where it shows up: design docs, academic abstracts, workshop descriptions, API docs.

```slop
This module facilitates communication between services.
The new API facilitates integration with third-party tools.
I facilitated a design sprint with stakeholders.
```

Replace with:

- `lets`, `helps`, `allows`, with the action.
- `run` or `lead` for meetings and workshops.
- Name the mechanism: "sends", "exposes", "proxies".

Rewrites:

```slop
This module facilitates communication between services.
```

After: This module sends messages between services over gRPC and retries failed calls 3 times.

```slop
The new API facilitates integration with third-party tools.
```

After: The API accepts webhooks from Zapier and Make and returns standard JSON errors.

```slop
I facilitated a design sprint with stakeholders.
```

After: I ran a 4-day design sprint with the support lead, two engineers, and the CFO.

- Literal use: for the job of running a workshop, write "moderator" or "workshop lead".
