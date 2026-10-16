From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 082. `vital`

- Kind: adjective. Banned forms: `vital`, `vitally`, `vitals`.
- Why it reads as machine text: `vital` is a model's second choice after `crucial`, used to rotate synonyms through a long answer. It borrows the medical sense of life and death to make routine advice sound urgent. It also slips into technical text through `Core Web Vitals`, so put that metric name in inline code when you cite it.
- Where it shows up: health and wellness copy, security advice, web performance docs.

```slop
Sleep is vital for your overall well-being.
It is vital to keep your dependencies up to date.
Proper hydration plays a vital role in performance.
```

Replace with:

- The effect with a figure and source: "below 6 hours of sleep, reaction times slow". Use for health claims.
- The risk: "the CVE fixed in lodash 4.17.21 allows prototype pollution". Use for security advice.
- The metric by name: "Largest Contentful Paint under 2.5 s". Use for performance.
- Cut it when the advice stands on its own.

Rewrites:

```slop
Sleep is vital for your overall well-being.
```

After: Adults need 7 to 9 hours of sleep a night. Below 6, reaction times slow measurably.

```slop
It is vital to keep your dependencies up to date.
```

After: Update dependencies weekly, and run `npm audit` in CI so a known CVE fails the build.

```slop
Proper hydration plays a vital role in performance.
```

After: Losing 2% of body weight in water lowers endurance. Drink 500 ml two hours before exercise.

- Literal use: for medical signs, list them ("heart rate, blood pressure, temperature and breathing rate") or write `vital signs` in inline code.
