From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 162. `blazing`

- Kind: adjective, usually in `blazing fast`. Banned forms: `blazing`, `blazingly`.
- Why it reads as machine text: `Blazingly fast` became a running joke on Rust and JavaScript READMEs, and models reproduce it whenever a library is about speed. It promises speed with no benchmark, no hardware and no baseline. Experienced readers skip to the benchmarks section and often find none. Some projects now drop the phrase from their README because issue threads mock it.
- Where it shows up: README taglines, package descriptions, CLI help text.

```slop
A blazing fast bundler written in Rust.
Blazingly fast JSON parsing.
Enjoy blazing page loads.
```

Replace with:

- Benchmark with baseline and hardware: "1.4s vs 9.8s for webpack 5 on the 10,000-module benchmark, M2, 16 GB".
- Throughput with the input named: "1.2 GB/s on one core, parsing `canada.json`".
- Page load metrics at a percentile, with the device and network.
- Cut it when there is no comparison. "Fast" without a baseline says nothing either.

Rewrites:

```slop
A blazing fast bundler written in Rust.
```

After: A bundler written in Rust. It builds our 10,000-module benchmark in 1.4s; webpack 5 takes 9.8s on the same M2 laptop.

```slop
Blazingly fast JSON parsing.
```

After: Parses JSON at 1.2 GB/s on one core (`canada.json`, Ryzen 7 7700).

```slop
Enjoy blazing page loads.
```

After: LCP is 1.1s at p75 on a mid-range Android phone over 4G.

- Literal use: for fire, write "burning" or "on fire"; for heat, give the temperature.
