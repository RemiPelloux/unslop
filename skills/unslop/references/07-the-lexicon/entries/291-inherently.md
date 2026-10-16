From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 291. `inherently`

- Kind: adverb. Banned forms: `inherently`, `inherently insecure`, `inherently complex`.
- Why it reads as machine text: `inherently` claims a property is built into a thing, which would need a reason, and then gives none. Models use it to end a debate (`inherently insecure`) without showing the mechanism. The claim is often false: the property comes from a default, not from the thing.
- Where it shows up: security advice, architecture debates, and arguments against a tool.

```slop
Storing tokens in localStorage is inherently insecure.
Distributed systems are inherently complex.
Microservices are inherently harder to debug than a monolith.
```

Replace with:

- The mechanism: what makes it so, in one clause starting with "because".
- The specific failure mode the property causes.
- A condition: "when X" or "unless Y", if the property depends on setup.
- Cut it when the reason follows; the reason carries the claim.

Rewrites:

```slop
Storing tokens in localStorage is inherently insecure.
```

After: Any script on the page can read localStorage, so one XSS bug exposes every token.

```slop
Distributed systems are inherently complex.
```

After: With 3 replicas, a write can succeed on one node and fail on two, and the client has to handle both.

```slop
Microservices are inherently harder to debug than a monolith.
```

After: A request that crosses 6 services needs a trace ID to follow; a monolith has one stack trace.

- Literal use: in philosophy or law, "inherent" as a defined term is fine; outside those fields, give the reason.
