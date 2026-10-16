From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 170. `sophisticated`

- Kind: adjective. Banned forms: `sophisticated`.
- Why it reads as machine text: Models use it to call an algorithm, an attack or a palette advanced without saying what it does. Incident reports use `a sophisticated attack` to excuse breaches that began with a phished password. In design copy it means muted colors and a serif.
- Where it shows up: incident reports, ML feature pages, brand descriptions.

```slop
We were targeted by a sophisticated cyberattack.
Our sophisticated algorithm finds the best matches.
A sophisticated palette of muted tones.
```

Replace with:

- For incidents, the entry point, the date and the missing control.
- For algorithms, the method and the evaluation result on held-out data.
- For palettes, the hex values and their roles.
- Cut it when you cannot name a single thing that makes it advanced.

Rewrites:

```slop
We were targeted by a sophisticated cyberattack.
```

After: On 3 March an attacker signed in with a support engineer's phished password. MFA was not enforced on that tool; it is now.

```slop
Our sophisticated algorithm finds the best matches.
```

After: An XGBoost model ranks matches on 40 features; top-3 accuracy is 82 percent on held-out data.

```slop
A sophisticated palette of muted tones.
```

After: Warm grey paper (#F7F5F0), near-black ink (#1A1A18), and one burnt orange accent (#B4441C).

- Literal use: none. For a person's taste, describe what they choose.
