From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 070. `orchestrate`

- Kind: verb. Banned forms: `orchestrate`, `orchestrates`, `orchestrated`, `orchestrating`, `orchestration`, `orchestrator`.
- Why it reads as machine text: Two habits again: generated résumés (`orchestrated a company-wide launch`) and infrastructure copy (`orchestrate your containers`). The musical image suggests one conductor in control of many parts. In résumés it inflates coordination; in docs it hides which tool schedules what. Agent frameworks use it for a loop that calls tools in order, which is easier to describe as a loop.
- Where it shows up: résumés, DevOps product pages, architecture docs, AI agent frameworks.

```slop
Orchestrated a cross-team product launch across 5 regions.
Orchestrate your microservices with ease.
The agent orchestrates multiple tools to complete tasks.
```

Replace with:

- `coordinated`, `planned`, `ran` in résumés, with scope.
- Name the scheduler or the control flow: "Kubernetes schedules", "a loop calls".
- `runs`, `calls`, `starts`, in order.
- `schedule`, for jobs with a time or a trigger.

Rewrites:

```slop
Orchestrated a cross-team product launch across 5 regions.
```

After: Ran the launch plan for 5 regions: 14 teams, one shared checklist, all live on the same day.

```slop
Orchestrate your microservices with ease.
```

After: Kubernetes restarts failed containers and spreads replicas across 3 zones.

```slop
The agent orchestrates multiple tools to complete tasks.
```

After: The agent calls search, reads the top 3 pages, writes the answer, and stops after 10 steps.

- Literal use: for music, write "arrange" or "score for orchestra"; for container schedulers, name the tool (Kubernetes, Nomad) or keep the term in inline code (`orchestration`).
