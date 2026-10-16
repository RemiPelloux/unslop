From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 234. `complexities`

- Kind: noun. Banned forms: `complexities`. The singular `complexity` stays allowed for a measured property.
- Why it reads as machine text: `navigate the complexities of` is one of the most frequent strings in generated business text. The plural signals that the writer felt something was complicated without being able to say what. It pads the first line of answers about regulation, migrations and markets.
- Where it shows up: consultancy pages, guide intros, answers to legal or financial questions.

```slop
We help clients navigate the complexities of cross-border payments.
Despite the complexities involved, the migration went smoothly.
This course demystifies the complexities of machine learning.
```

Replace with:

- Each hard part, named: "currency conversion, local tax and 3-day settlement".
- "problems", "steps" or "rules", with a count.
- "complexity" in the singular, only for a measured property: "O(n log n) time complexity", "cyclomatic complexity of 14".
- Cut it when the sentence says only that a topic is hard.

Rewrites:

```slop
We help clients navigate the complexities of cross-border payments.
```

After: We handle currency conversion, VAT registration and settlement for clients selling in 30 countries.

```slop
Despite the complexities involved, the migration went smoothly.
```

After: The migration moved 2 TB across 40 tables with 9 minutes of downtime.

```slop
This course demystifies the complexities of machine learning.
```

After: The course teaches linear regression, decision trees and small neural networks, each with a Python notebook.

- Literal use: for computational cost, write the bound or class ("O(n^2)", "NP-hard") and use the singular "complexity".
