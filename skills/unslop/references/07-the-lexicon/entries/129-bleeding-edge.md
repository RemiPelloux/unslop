From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 129. `bleeding-edge`

- Kind: compound adjective. Banned forms: `bleeding-edge`, `bleeding edge`.
- Why it reads as machine text: `bleeding-edge` is the developer-flavored version of `cutting-edge`, used by models to sound like an insider. It originally meant unstable pre-release software, which is the opposite of what a sales page wants to say. Readers cannot tell which sense the writer meant.
- Where it shows up: developer tool landing pages, release channel docs, hiring posts.

```slop
Stay on the bleeding edge with our nightly builds.
Work with bleeding-edge technologies.
A bleeding-edge framework for building web apps.
```

Replace with:

- The release channel and its risk: "nightly builds from `main`, breaking changes about weekly". Use for release docs.
- The tech list with versions: "Rust, WebGPU, Postgres 17". Use for hiring.
- What the framework does by default: "renders on the server and streams HTML". Use for framework pages.
- Cut it when the reader would rather know the stability guarantee.

Rewrites:

```slop
Stay on the bleeding edge with our nightly builds.
```

After: Nightly builds come straight from `main`. Expect a breaking change about once a week.

```slop
Work with bleeding-edge technologies.
```

After: You will work in Rust and WebGPU, with Postgres 17 for storage.

```slop
A bleeding-edge framework for building web apps.
```

After: A web framework that renders on the server by default and streams HTML as each part is ready.

- Literal use: when you mean unstable, write "pre-release" or "unstable" and name the channel in inline code, as in `nightly`.
