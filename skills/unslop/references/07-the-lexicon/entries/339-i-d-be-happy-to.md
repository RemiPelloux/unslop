From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 339. `i'd be happy to`

- Kind: opener. Banned forms: `i'd be happy to`, `I'd be glad to`, `I'm happy to help`, `happy to help`.
- Why it reads as machine text: `I'd be happy to help!` opens a chat answer by announcing willingness before doing the work. Assistants tuned for politeness put it at the top of nearly every reply. The reader asked for the help, so the offer delays it.
- Where it shows up: the first line of chat replies, support macros, and agent status messages.

```slop
I'd be happy to help you write a SQL query for that.
I'd be glad to explain how OAuth works.
Happy to help! Here's a function that sorts the list.
```

Replace with:

- The work itself, from the first word: the query, the explanation, the function.
- A one-line clarifying question, if the request is ambiguous.
- A note of scope, when you will only do part: "This covers the login flow; signup is separate."
- Cut it every time.

Rewrites:

```slop
I'd be happy to help you write a SQL query for that.
```

After: `SELECT user_id, COUNT(*) FROM orders WHERE created_at > now() - interval '30 days' GROUP BY user_id;`

```slop
I'd be glad to explain how OAuth works.
```

After: In OAuth, your app sends the user to the provider, the provider returns a code, and your server swaps the code for a token.

```slop
Happy to help! Here's a function that sorts the list.
```

After: This function sorts by `lastName`, then `firstName`, without changing the original array.

- Literal use: to accept a request from a colleague, write "Yes, I'll do it by Thursday."
