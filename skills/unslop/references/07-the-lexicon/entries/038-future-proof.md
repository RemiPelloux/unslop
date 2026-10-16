From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 038. `future-proof`

- Kind: verb and adjective. Banned forms: `future-proof`, `future proof`, `future-proofs`, `future-proofed`, `future-proofing`.
- Why it reads as machine text: Nobody can see what is coming, so the claim cannot be tested, which is why sales copy likes it. Models apply it to frameworks, careers, and laptops. In engineering it hides the real decision: which changes the design expects and which it does not. Buying guides that use it are often out of date within one product cycle.
- Where it shows up: architecture docs, hardware buying guides, career advice, consulting proposals.

```slop
Future-proof your codebase with our modular architecture.
A future-proof laptop with Wi-Fi 7.
Future-proofing your career in the age of AI.
```

Replace with:

- Name the change the design allows: "add a payment provider without touching checkout".
- Give support dates: "security updates until 2031".
- `plan for`, with the specific plan.

Rewrites:

```slop
Future-proof your codebase with our modular architecture.
```

After: Each payment provider is one file that implements `charge` and `refund`; adding Adyen took two days.

```slop
A future-proof laptop with Wi-Fi 7.
```

After: Wi-Fi 7 and two USB4 ports, and the maker promises OS updates until 2031.

```slop
Future-proofing your career in the age of AI.
```

After: Learn SQL and statistics; both have appeared in data job ads for 30 years.

- Literal use: there is no literal sense; write "still works when X changes" and name X.
