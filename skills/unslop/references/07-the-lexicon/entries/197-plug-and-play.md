From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 197. `plug-and-play`

- Kind: adjective. Banned forms: `plug-and-play`, `plug and play`.
- Why it reads as machine text: A hardware term that models reuse for SDKs, components and even new hires. It hides configuration, compatibility and version limits. The first integration error proves it wrong, and the developer who hit it remembers the README.
- Where it shows up: SDK docs, component libraries, job ads.

```slop
A plug-and-play SDK for payments.
Plug-and-play components for React.
We need a plug-and-play senior engineer.
```

Replace with:

- The install command and the minimum configuration, as code.
- Compatibility: framework versions, dependencies, size.
- For hiring, what the person must already know, and when they start on-call.
- For hardware add-ons, the ports, drivers and operating systems supported.
- Cut it when you can show the three lines of setup. Show them.

Rewrites:

```slop
A plug-and-play SDK for payments.
```

After: Run `npm i @acme/pay`, add your publishable key, and render `<Checkout />`.

```slop
Plug-and-play components for React.
```

After: Works with React 18 and 19, needs no CSS framework, and adds about 4 KB gzipped per component.

```slop
We need a plug-and-play senior engineer.
```

After: You have run Postgres in production and can join the on-call rotation in your third week.

- Literal use: for USB devices detected by the operating system, write "detected automatically", or put the spec name in inline code (`Plug and Play`).
