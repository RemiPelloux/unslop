From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 164. `buttery`

- Kind: adjective, usually in `buttery smooth`. Banned forms: `buttery`, `butteriness`.
- Why it reads as machine text: Phone reviews and app marketing use `buttery smooth` for scrolling, and models copy it into frontend release notes. It describes a feeling of frame pacing. It hides the frame rate, the dropped-frame count and the device it was measured on.
- Where it shows up: scrolling and animation claims, phone reviews, release notes.

```slop
Buttery smooth scrolling on every device.
The new list view feels buttery.
Buttery 120Hz animations throughout the app.
```

Replace with:

- Frame data from a trace: fps, dropped frames, device, list length.
- The technique that produces it: "rows are virtualized; 40 are in the DOM at once".
- Motion limits: duration, properties animated, behavior on 60Hz and 120Hz screens.
- Cut it when you have not run a trace.

Rewrites:

```slop
Buttery smooth scrolling on every device.
```

After: Scrolling a 10,000-row list holds 60 fps on a Pixel 6a; a 30-second trace dropped 0.3 percent of frames.

```slop
The new list view feels buttery.
```

After: The list view now virtualizes rows, so only 40 are in the DOM at a time instead of 10,000.

```slop
Buttery 120Hz animations throughout the app.
```

After: Transitions run at the display's refresh rate, up to 120Hz, and animate only opacity and transform.

- Literal use: for food, write "rich" or say "made with butter".
