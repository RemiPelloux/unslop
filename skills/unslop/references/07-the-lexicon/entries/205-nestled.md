From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 205. `nestled`

- Kind: verb participle used as an adjective. Banned forms: `nestled`.
- Why it reads as machine text: Travel and property copy (`nestled in the hills`) that models use for any location, and in design notes for any element placed inside another. It sounds cozy and hides distance and direction, and the listing photo rarely shows the road. In UI specs it hides the alignment and spacing values a developer needs.
- Where it shows up: hotel and rental listings, office pages, layout descriptions.

```slop
A cozy cabin nestled in the Alps.
Our office is nestled in the heart of Berlin.
The search bar sits nestled in the top navigation.
```

Replace with:

- Location with altitude, distance and travel time.
- Address area and transit time.
- For layout, position, alignment, width and gap.
- Cut it when the location follows. "In" works.

Rewrites:

```slop
A cozy cabin nestled in the Alps.
```

After: A wooden cabin at 1,400 m, a 20-minute drive from Chamonix.

```slop
Our office is nestled in the heart of Berlin.
```

After: Our office is in Mitte, a 3-minute walk from the nearest U8 station.

```slop
The search bar sits nestled in the top navigation.
```

After: Search sits in the top bar, right-aligned, 320px wide, 16px from the account menu.

- Literal use: for animals settled in a nest, write "in the nest" or "huddled".
