From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 089. `dynamic`

- Kind: adjective. Banned forms: `dynamic`, `dynamically`, `dynamics`.
- Why it reads as machine text: `dynamic` has an exact meaning in programming, and models blur it with the advertising sense of "lively". In copy it describes teams, markets and dashboards and says nothing about any of them. In technical docs it hides whether a value is computed at runtime, fetched from a server or edited by the user, which are three different things.
- Where it shows up: job listings, dashboard feature lists, framework docs.

```slop
Join our dynamic team in a fast-paced environment.
Create dynamic dashboards that update in real time.
A dynamic platform for dynamic businesses.
```

Replace with:

- The team facts: "8 engineers, release every Tuesday, on call one week in six". Use for job listings.
- The refresh rule: "charts reload every 30 seconds from the live database". Use for dashboards.
- The runtime behavior: "routes are read from `routes.json` at startup". Use for technical docs.
- Cut it in pairs and repeats, where it adds rhythm and no meaning.

Rewrites:

```slop
Join our dynamic team in a fast-paced environment.
```

After: Join a team of 8 engineers. We release every Tuesday, and each person is on call one week in six.

```slop
Create dynamic dashboards that update in real time.
```

After: Charts reload every 30 seconds from the production database, without a page refresh.

```slop
A dynamic platform for dynamic businesses.
```

After: Accounting software for shops with 1 to 50 staff.

- Literal use: for a value computed at runtime, write "computed at runtime" or name the mechanism in inline code, such as `import()` or a framework's `dynamic` option.
