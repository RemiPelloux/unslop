From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 083. `essential`

- Kind: adjective. Banned forms: `essential`, `essentials`, `essentially`.
- Why it reads as machine text: `essential` is the most common way models mark an item as required, and it is often wrong: the `essential tools` list includes optional ones. It fakes editorial selection, as if someone had cut everything else. It also heads listicle titles like `10 Essential Tips`, the format readers now associate with filler.
- Where it shows up: listicle titles, setup guides, packing and shopping lists.

```slop
10 Essential VS Code Extensions for Every Developer.
Git is an essential tool for any developer.
Essential features include dark mode and notifications.
```

Replace with:

- Required or optional, stated as such: "Required: Node 20. Optional: Docker, for the local database." Use in setup guides.
- The count and whose list it is: "the 6 extensions I install on every new machine". Use for lists.
- What breaks without it: "without Git you cannot open a pull request". Use when necessity is the point.
- Cut it in feature lists and list the features.

Rewrites:

```slop
10 Essential VS Code Extensions for Every Developer.
```

After: 6 VS Code extensions I install on every new machine, and what each one does.

```slop
Git is an essential tool for any developer.
```

After: You need Git to clone the repository and open pull requests.

```slop
Essential features include dark mode and notifications.
```

After: Includes dark mode and push notifications.

- Literal use: for chemistry and nutrition terms, use inline code (`essential oil`, `essential amino acid`) or give the compound's name.
