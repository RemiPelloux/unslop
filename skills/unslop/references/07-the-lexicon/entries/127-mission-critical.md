From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 127. `mission-critical`

- Kind: compound adjective. Banned forms: `mission-critical`, `mission critical`.
- Why it reads as machine text: `mission-critical` came from aerospace and defense, where a failure ends the mission. Models apply it to any production workload or internal tool. It raises the stakes without stating the cost of downtime, which is the number that decides budgets.
- Where it shows up: infrastructure marketing, incident postmortems, architecture docs.

```slop
Built for mission-critical workloads.
Email is a mission-critical application for our business.
Monitoring for your mission-critical systems.
```

Replace with:

- The recovery targets: "recovery point 5 minutes, recovery time 30 minutes". Use for architecture docs.
- The cost of downtime: "the 3-hour outage in March delayed 120 quotes". Use for business cases.
- The tier and its response: "Tier 1 pages the on-call engineer within 60 seconds". Use for incident policy.
- Cut it when the sentence already says "production".

Rewrites:

```slop
Built for mission-critical workloads.
```

After: Designed for workloads that need a 5-minute recovery point and a 30-minute recovery time.

```slop
Email is a mission-critical application for our business.
```

After: When email is down, sales cannot send quotes. The 3-hour outage last March delayed 120 of them.

```slop
Monitoring for your mission-critical systems.
```

After: Alerts for your Tier 1 services page the on-call engineer within 60 seconds.

- Literal use: in aerospace and defense documents where it is a formal class, use the document's own term in inline code.
