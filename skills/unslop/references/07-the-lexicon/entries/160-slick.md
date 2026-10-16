From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 160. `slick`

- Kind: adjective. Banned forms: `slick`, `slicker`, `slickest`, `slickly`, `slickness`, `slicks`.
- Why it reads as machine text: App-review slang for "polished" that models use for transitions, onboarding and pitch decks. Readers also hear its second meaning, too smooth to trust, so it undercuts its own claim. It hides the duration, the step count or the visual decision.
- Where it shows up: app reviews, launch posts, design critique.

```slop
A slick onboarding flow gets users started fast.
Slick animations make every interaction feel premium.
The pitch deck looks slick.
```

Replace with:

- Steps and time: "three screens, about 40 seconds, no email confirmation before first use".
- Motion values: duration, easing, properties animated, reduced-motion behavior.
- For decks, the rule: "one claim per slide, numbers set at 56px".
- Cut it when it is the whole review.

Rewrites:

```slop
A slick onboarding flow gets users started fast.
```

After: Three screens and about 40 seconds to a working project; email confirmation waits until the first invite.

```slop
Slick animations make every interaction feel premium.
```

After: Menus fade in over 120ms with `ease-out`, opacity only, and do not animate under `prefers-reduced-motion`.

```slop
The pitch deck looks slick.
```

After: Each slide makes one claim, and the key number on each is set at 56px.

- Literal use: for oil on water, write "oil film"; for a wet road, write "slippery".
