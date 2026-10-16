From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 073. `comprehensive`

- Kind: adjective. Banned forms: `comprehensive`, `comprehensively`.
- Why it reads as machine text: `comprehensive` is how a model introduces a guide, test suite or product tier without stating its scope. It promises completeness, which no reader can check, so they discount it at once. Generated docs open with `This comprehensive guide covers` and then cover five topics.
- Where it shows up: tutorial intros, test plan summaries, pricing tier descriptions.

```slop
This comprehensive guide covers everything you need to know about Docker.
We added comprehensive test coverage for the billing module.
A comprehensive suite of tools for growing teams.
```

Replace with:

- The count: "covers 14 commands, from `docker build` to `docker compose down`". Use for guides.
- The coverage figure: "line coverage for `billing/` went from 41% to 88%". Use for tests.
- The scope and its edge: "covers Linux and macOS; Windows is out of scope". Use when readers need to know what is missing.
- The named parts: "invoicing, payroll and expense reports". Use for product suites.
- Cut it when the list that follows already shows the scope.

Rewrites:

```slop
This comprehensive guide covers everything you need to know about Docker.
```

After: This guide covers 14 Docker commands for building, running and debugging containers on Linux and macOS.

```slop
We added comprehensive test coverage for the billing module.
```

After: Added 63 tests for `billing/`. Line coverage is now 88%, up from 41%.

```slop
A comprehensive suite of tools for growing teams.
```

After: Invoicing, payroll and expense reports in one account, for teams of 5 to 200.

- Literal use: when an insurance product or exam has the word in its official name, quote the name in inline code, as in `comprehensive coverage`.
