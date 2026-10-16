From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 119. `modern`

- Kind: adjective. Banned forms: `modern`, `modernize`, `modernization`.
- Why it reads as machine text: `modern` is the most frequent design adjective in model output, as in `modern UI`, `modern stack` and `modern teams`. It ages the day it is written and describes nothing a reader can check. In design prompts it reliably produces the same look: Inter, an `indigo-500` accent and `rounded-2xl` cards with soft shadows.
- Where it shows up: design prompts, tech-stack READMEs, SaaS hero lines.

```slop
A modern, responsive landing page.
Built with a modern tech stack.
Modern tools for modern teams.
```

Replace with:

- The design spec: "IBM Plex Sans at 16 px, 2px radius, one accent #B4441C, borders not shadows". Use for design prompts.
- The named stack and versions: "React 19, Vite 6, Postgres 17". Use for READMEs.
- The audience and the job: "invoicing for freelancers who bill by the hour". Use for hero lines.
- Cut it every time; the word is never the claim.

Rewrites:

```slop
A modern, responsive landing page.
```

After: A landing page in IBM Plex Sans at 16 px, one burnt-orange accent, 1px borders, no shadows, readable at 320 px wide.

```slop
Built with a modern tech stack.
```

After: Built with React 19, Vite 6 and Postgres 17.

```slop
Modern tools for modern teams.
```

After: Time tracking and invoicing for freelancers who bill by the hour.

- Literal use: for a historical period, give the dates ("since 1945"); for a proper name such as `Modern Greek`, use inline code.
