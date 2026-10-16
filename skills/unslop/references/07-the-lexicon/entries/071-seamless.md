From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 071. `seamless`

- Kind: adjective. Banned forms: `seamless`, `seamlessly`, `seamlessness`.
- Why it reads as machine text: models attach `seamless` to every integration, handoff and sync, and `seamlessly integrates with` is one of the most repeated strings in generated product copy. It borrows the language of tailoring to suggest that nothing breaks where two systems meet. It never names that boundary, and it hides the steps that remain, such as an OAuth prompt or a field-mapping screen.
- Where it shows up: integration pages, onboarding emails, README feature lists.

```slop
Seamlessly integrates with your existing tools.
Enjoy a seamless experience across all your devices.
Our API ensures seamless data synchronization.
```

Replace with:

- The step count: "connects to GitHub in two clicks, with no API key". Use when setup is short enough to count.
- The step that no longer happens: "no second login when you switch from Mail to Calendar". Use for single sign-on and shared sessions.
- The delay: "edits reach your other devices within 2 seconds". Use for sync claims.
- The named list: "works with Slack, Linear and Jira". Use when the claim was about compatibility.
- Cut it when the sentence still says what connects to what without it.

Rewrites:

```slop
Seamlessly integrates with your existing tools.
```

After: Imports issues from GitHub, Linear and Jira. Setup takes one OAuth prompt per service.

```slop
Enjoy a seamless experience across all your devices.
```

After: Drafts sync between phone and laptop within 2 seconds of the last keystroke.

```slop
Our API ensures seamless data synchronization.
```

After: The API writes each change to both databases in one transaction, so a failed write changes neither.

- Literal use: for a garment or surface with no joins, write "without seams" or "knitted in one piece".
