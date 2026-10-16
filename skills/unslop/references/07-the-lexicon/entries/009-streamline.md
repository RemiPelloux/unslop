From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 009. `streamline`

- Kind: verb. Banned forms: `streamline`, `streamlines`, `streamlined`, `streamlining`.
- Why it reads as machine text: It came from aerodynamic design through 1990s process consulting and now means "made better, somehow". Models pick it for any change to a process: fewer steps, faster steps, or no change at all. It hides the step count before and after, which is the one number the reader wants. Paired with `workflow` or `process`, it fills a hero line with no product in it.
- Where it shows up: release notes, PR titles, B2B landing pages, refactor commit messages.

```slop
Streamline your hiring process with automated scheduling.
Refactor: streamline the auth module.
Our streamlined onboarding gets you started in minutes.
```

Replace with:

- `cut`, `remove`, `merge`, with the count of steps.
- `simplify` only next to what got removed.
- In commits, name the change: "remove", "inline", "merge".
- `automate`, with the step that no longer needs a person.

Rewrites:

```slop
Streamline your hiring process with automated scheduling.
```

After: Candidates pick an interview slot from your calendar, with no email back and forth.

```slop
Refactor: streamline the auth module.
```

After: refactor(auth): merge `login.ts` and `session.ts` into `auth.ts`, remove the unused token cache.

```slop
Our streamlined onboarding gets you started in minutes.
```

After: Sign up, connect GitHub, deploy: three screens, about 2 minutes.

- Literal use: for fluid flow, write "low-drag" and give the drag coefficient.
