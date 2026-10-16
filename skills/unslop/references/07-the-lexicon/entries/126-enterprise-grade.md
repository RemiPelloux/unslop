From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

#### 126. `enterprise-grade`

- Kind: compound adjective. Banned forms: `enterprise-grade`, `enterprise grade`.
- Why it reads as machine text: `enterprise-grade` claims a product meets the demands of large companies but never lists the demands. Models use it for security, support and scale. Enterprise buyers work from a checklist, and the word skips every item on it.
- Where it shows up: pricing pages, security pages, upgrade prompts in developer tools.

```slop
Enterprise-grade security for teams of all sizes.
Get enterprise-grade features on every plan.
Enterprise-grade reliability you can trust.
```

Replace with:

- The checklist items: "SAML SSO, SCIM provisioning, audit log export, EU data residency". Use for security and admin.
- The contract terms: "99.9% SLA with service credits, 1-hour response for severity 1". Use for support.
- The limits: "up to 50,000 users per workspace". Use for scale.
- Cut it when the plan table already lists the features.

Rewrites:

```slop
Enterprise-grade security for teams of all sizes.
```

After: SAML single sign-on and audit logs on every plan, including the 5-seat one.

```slop
Get enterprise-grade features on every plan.
```

After: SCIM provisioning, EU data residency and audit log export on every plan.

```slop
Enterprise-grade reliability you can trust.
```

After: A 99.9% uptime SLA with service credits, and a 1-hour response for severity 1 incidents.

- Literal use: none; a buyer needs the list, so give the list.
