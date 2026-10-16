From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 122. `state-of-the-art`

- Kind: compound adjective. Banned forms: `state-of-the-art`, `state of the art`.
- Why it reads as machine text: `state-of-the-art` has an exact use in machine learning papers, the best published result on a benchmark, and models spread it to products, clinics and security. In marketing it claims the top current level with no benchmark. In research it often appears without a date, which matters because records on popular benchmarks fall every few months.
- Where it shows up: ML paper abstracts, clinic and hospital pages, security pages.

```slop
Our state-of-the-art model outperforms existing approaches.
A state-of-the-art facility with the latest equipment.
State-of-the-art security for your peace of mind.
```

Replace with:

- The benchmark, score and date: "81.2 on MMLU, 1.4 points above the best published result as of March 2025". Use for ML.
- The named equipment: "a 3 tesla MRI scanner installed in 2024". Use for facilities.
- The controls: "authenticator app or hardware key; SOC 2 Type II report on request". Use for security.
- Cut it when you have no comparison to show.

Rewrites:

```slop
Our state-of-the-art model outperforms existing approaches.
```

After: Our model scores 81.2 on MMLU, 1.4 points above the best published result as of March 2025.

```slop
A state-of-the-art facility with the latest equipment.
```

After: The clinic has a 3 tesla MRI scanner, installed in 2024.

```slop
State-of-the-art security for your peace of mind.
```

After: Sign-in requires an authenticator app or a hardware key. Our SOC 2 Type II report is available on request.

- Literal use: in a results table, write "best published result as of" a date, or keep the abbreviation `SOTA` in inline code.
