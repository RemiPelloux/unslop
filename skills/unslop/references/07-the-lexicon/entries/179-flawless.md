From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 179. `flawless`

- Kind: adjective. Banned forms: `flawless`, `flawlessly`.
- Why it reads as machine text: An absolute claim (no flaws) that models attach to migrations, launches and checkouts. Engineers read it as `nobody looked`, and an incident a week later makes the post read as dishonest. It replaces the error rate and the test matrix, which are the numbers that would earn trust.
- Where it shows up: migration retrospectives, device support claims, checkout pages.

```slop
The migration went flawlessly.
Flawless performance on any device.
A flawless checkout experience.
```

Replace with:

- Migration facts: data moved, time taken, data lost, downtime, how you verified.
- The test matrix: OS versions, browsers, oldest device.
- For checkout, step count and payment error rate.
- Cut it when there were problems. Report them.

Rewrites:

```slop
The migration went flawlessly.
```

After: We moved 2.1 TB in 6 hours with 14 minutes of read-only mode. Row counts and checksums matched on every table.

```slop
Flawless performance on any device.
```

After: Tested on iOS 17 and later, Android 12 and later, and the last two versions of Chrome, Firefox and Safari.

```slop
A flawless checkout experience.
```

After: Checkout is two steps. 0.4 percent of payments fail, and each failure shows its reason next to the field.

- Literal use: for gemstones, use the grade from the certificate, such as "FL clarity".
