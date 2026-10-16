From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 336. `don't hesitate`

- Kind: phrase. Banned forms: `don't hesitate`, `do not hesitate to`, `don't hesitate to reach out`.
- Why it reads as machine text: `Don't hesitate to reach out` assumes the reader was hesitating and offers contact without saying how or when anyone will answer. Models end support replies and emails with it. It is customer-service boilerplate and readers skip it.
- Where it shows up: email closers, support replies, and "Contact" sections of docs.

```slop
If you have any questions, don't hesitate to reach out.
Please do not hesitate to contact our support team.
Don't hesitate to let me know if anything is unclear.
```

Replace with:

- The channel and the response time: "Email support@ (reply within 1 working day)."
- A specific prompt for what to send: "Send the request ID from the error page."
- Nothing, when the reader already knows how to reply.
- Cut it when it closes an email; the reply button is enough.

Rewrites:

```slop
If you have any questions, don't hesitate to reach out.
```

After: Questions go to #billing-help in Slack; Ana answers before noon.

```slop
Please do not hesitate to contact our support team.
```

After: Email support@example.com with your account ID. We reply within 1 working day.

```slop
Don't hesitate to let me know if anything is unclear.
```

After: (Delete the line. If one step is likely to confuse, explain that step.)

- Literal use: none.
