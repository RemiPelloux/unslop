From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 034. `optimize`

- Kind: verb. Banned forms: `optimize`, `optimizes`, `optimized`, `optimizing`, `optimization`, `optimizer`, and the `-ise` spellings.
- Why it reads as machine text: In code it has a real meaning (reduce a measured cost), but models use it as a general word for "improved": `optimized for performance`, `optimized workflow`. Without the metric and the before and after values, nobody can check the claim. Pages that say `fully optimized` rarely show a profile. SEO copy uses it as praise, which strips the last trace of the technical sense.
- Where it shows up: PR titles, commit messages, SEO copy, résumé bullets.

```slop
Optimized the database queries for better performance.
Fully optimized for mobile devices.
Optimize your workflow with smart automations.
```

Replace with:

- `make X faster` or `cut X`, with numbers and the method.
- For screen sizes, name the widths you tested.
- In commits, name the change: "add index on `orders.user_id`".
- `tune` for a config change, with the parameter and its old and new value.

Rewrites:

```slop
Optimized the database queries for better performance.
```

After: Added an index on `orders.user_id`; the order history query went from 1.8 s to 40ms.

```slop
Fully optimized for mobile devices.
```

After: Tested at 360px and 414px wide; tap targets are at least 44 by 44px.

```slop
Optimize your workflow with smart automations.
```

After: Rules file each invoice in the right folder and remind the client after 14 days.

- Literal use: for compilers and solvers, keep the term in inline code (`-O2`, `scipy.optimize.minimize`) or write "minimize the cost function".
