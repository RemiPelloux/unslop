From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 244. `best practices`

- Kind: noun phrase. Banned forms: `best practices`. The singular `best practice` passes the linter but has the same problem.
- Why it reads as machine text: Models write `follow best practices` when they do not know the practice or do not want to state it. It is the most common empty instruction in generated code reviews and READMEs. It claims a consensus that rarely exists and hides which source, version or team agreed on it.
- Where it shows up: code review comments, README and contributing guides, security and SEO advice.

```slop
Make sure to follow best practices when handling user input.
This template follows industry best practices for accessibility.
We adhere to security best practices at every layer.
```

Replace with:

- The rule itself: "parameterize every SQL query".
- The source: "meets WCAG 2.2 AA", "passes OWASP ASVS level 2".
- "conventions" for team or language norms, with a link.
- Cut it when the list that follows states the rules.

Rewrites:

```slop
Make sure to follow best practices when handling user input.
```

After: Escape user input in templates, and pass it to SQL only as bound parameters.

```slop
This template follows industry best practices for accessibility.
```

After: The template meets WCAG 2.2 AA: 4.5:1 text contrast, visible focus rings, and a label on every input.

```slop
We adhere to security best practices at every layer.
```

After: We encrypt data at rest with AES-256, require SSO for staff, and rotate keys every 90 days.

- Literal use: when citing a published document with the phrase in its title, put the title in inline code.
