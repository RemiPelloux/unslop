### 8.7 Microcopy for messages and pages

#### Notifications

Generated notifications hide the event behind a teaser: "You have a new notification", "Important update about your account", "Don't miss out". The person has to open the message to learn whether it mattered, and after the third empty teaser they stop opening any.

- The subject, title or first line names the event, the actor and the object: "Hollis & Reed paid INV-0042 ($1,200)".
- Push titles stay under 40 characters and bodies under 100, because lock screens truncate there.
- Email subject lines stay under 60 characters and front-load the noun the person will search for later.
- One event per notification. Batch low-priority events into a daily digest the person can turn off.
- Every notification type has its own off switch, and the email footer links straight to it.
- No urgency words ("Act now", "Last chance") unless a real deadline exists, and then state the date.

```slop
You have a new notification!
Important update about your account
Don't miss out on what's happening in your workspace
Great news! Something exciting just happened.
```

```text
Hollis & Reed paid INV-0042 ($1,200)
INV-0039 is 7 days late. Reminder sent to dana@hollis.example.
Your card expires on 30 November. Update it to keep the Team plan.
3 invoices are due this week
```

#### Onboarding

The generated onboarding flow opens with `Welcome aboard! Let's get you set up for success`, runs an eight-step tooltip tour of the navigation, and asks for job title, company size and `how did you hear about us` before the person has seen the product.

- Ask only for what the first real task needs. Everything else can wait until it is used.
- Say how many steps there are: "Step 2 of 3".
- The first session ends with real output: a sent invoice, a deployed page, an imported file. Not with a tour.
- Use a checklist of 3 to 5 real tasks, each one linking to the screen where it happens. Let people dismiss the checklist.
- Every step has a visible "Skip" that does not need a confirmation.
- Welcome text is one sentence or nothing. The product name in the header already says where they are.

```slop
Welcome aboard! We're so excited to have you here.
Let's get you set up for success in just a few easy steps.
Ready to embark on your invoicing journey?
Tell us a bit about yourself so we can personalize your experience.
```

```text
Step 1 of 3. Add your business details. They appear on every invoice.
Step 2 of 3. Add your first client. You can import a CSV instead.
Step 3 of 3. Send a test invoice to yourself.

Set up Tidemark
[ ] Add your logo
[ ] Connect your bank
[ ] Turn on reminders
```

#### Tooltips

Generated tooltips restate the label in a longer sentence ("Click here to edit your settings"), or hold information the person needs and cannot reach on a touch screen.

- A tooltip adds what the label cannot hold: a definition, a keyboard shortcut, a reason a control is disabled.
- Icon-only buttons need an accessible name, and the tooltip shows that same name: "Archive", "Duplicate (D)".
- Under 80 characters and one sentence. Longer content belongs in help text or a linked doc.
- Never hide required information in a tooltip. Hover does not exist on phones, and focus-triggered tooltips are easy to miss.
- A disabled button's tooltip says why it is disabled and how to enable it.

```slop
Click here to edit your settings!
This is where the magic happens.
Hover over me for more info!
This button lets you easily duplicate your invoice with just one click.
```

```text
Duplicate (D)
Net 14: payment is due 14 days after the invoice date.
Add a client before sending.
Archived invoices stay searchable and are excluded from reports.
```

#### 404 pages

The generated 404 is a joke: an astronaut, "Houston, we have a problem", "Looks like you're lost in space", a button reading "Take me home". It wastes the one moment when the person needs help finding something.

- Say plainly that the page does not exist or has moved.
- Show the requested path, so a mistyped URL is visible.
- Offer a search field and 2 to 4 links to the pages most often wanted from that section.
- If the page was removed on purpose, say what replaced it, with a link.
- Return a real 404 status code. A 200 response with error text hides the problem from crawlers and monitoring.

```slop
Oops! Looks like you're lost in space.
Houston, we have a problem.
This page took a vacation. Let's get you back on track!
404: Page not found :(
```

```text
There is no page at /docs/reminders-v1.

The reminders guide moved to /docs/reminders. Search the docs, or go to one of these:
- Reminders
- Recurring invoices
- Pricing
```

#### Pricing labels

Generated pricing pages use the same three columns: Starter, Pro, Enterprise, a "Most popular" ribbon on the middle one, check marks against vague features ("Advanced analytics", "Priority support"), and a struck-through price with no explanation.

- One line holds the price, the unit, the period and the tax status: "$12 per seat per month, billed yearly, excl. VAT".
- Show the monthly price billed monthly next to the yearly rate, so the discount is checkable.
- Limits are numbers: "5 clients", "10 GB", "3 seats". Never "Generous limits".
- Say what happens at the limit: "At 6 clients you are asked to upgrade. Nothing is deleted."
- Feature rows name the feature as it appears in the product. "Advanced analytics" is not a feature; "Revenue by client report" is.
- Name plans after who they are for ("Solo", "Team", "Firm") or after their size. Avoid "Ultimate" and "Pro Max".
- "Most popular" only if it is true this month. A badge on every middle column is a template default.
- "Contact sales" appears with a price floor or a reason: "From $400 a month. Needs a call because we migrate your data."

```slop
Pro
$29/mo
Most Popular
Everything in Starter, plus:
Advanced analytics
Priority support
Unlimited possibilities
```

```text
Team
$12 per seat per month, billed yearly ($14 billed monthly). Prices exclude VAT.
Up to 25 seats and 500 clients.
Everything in Solo, plus:
Shared client list
Revenue by client report
Email support, answered within 4 working hours
```

### 8.8 Microcopy for publishing and code

#### Headlines and subheads

Generated hero headlines are interchangeable: `Supercharge your workflow`, `The future of invoicing is here`, `Work smarter, not harder`, `Where teams do their best work`. Any company could put them on any product.

- The headline names what the product does, using a noun a customer would type into a search box: "Invoicing for freelancers that chases late payments".
- Under 10 words. If it needs more, the subhead carries the rest.
- The subhead gives one concrete mechanism or fact: who it is for, how it works, what it costs.
- Apply the swap test: put a competitor's name in front of the headline. If it is still true, rewrite it.
- No `the future of`, no `reimagined`, no imperative slogans aimed at the reader's potential.

```slop
Supercharge your workflow.
The future of invoicing is here.
Work smarter, not harder.
Invoicing, reimagined for the modern team.
```

```text
Invoicing for freelancers that chases late payments for you
Tidemark emails clients on day 7, 14 and 30, in your name, and stops when they pay. $8 a month.
```

#### Meta descriptions

Generated meta descriptions open with `Discover`, `Unlock` or `Look no further`, and the same description is copied to every page of the site.

- 120 to 155 characters, so search results show it whole.
- Product name, what the page offers, and one specific fact.
- One description per page, written for that page.
- No imperative openers aimed at the reader, no claims of being the best.

```slop
Discover the ultimate invoicing solution. Unlock seamless payments and take your business to the next level with Tidemark.
Look no further! Tidemark is the all-in-one platform for all your needs.
```

```text
Tidemark sends invoices and emails late clients on day 7, 14 and 30. Plans start at $8 a month for up to 5 clients.
Tidemark pricing: Solo $8, Team $12 per seat, Firm from $400 a month. Prices exclude VAT. Yearly billing saves 15%.
```

#### Commit messages

Generated commits announce themselves (`This commit enhances...`), list every file touched, use emoji shortcodes, and end with a summary of the summary.

- Subject line in the imperative, under 50 characters, no final period: "Stop reminders after invoice is paid".
- If the repository uses Conventional Commits, keep the prefix and still write a real subject: "fix(reminders): stop after invoice is paid".
- Blank line, then a body wrapped at 72 characters that says why the change was made and what it affects. The diff already shows what changed line by line.
- Reference the issue: "Fixes #412".
- No emoji or shortcodes, no "various improvements", no "updated files", no closing offer.

```slop
feat: :sparkles: Enhanced the reminder system with improved logic

This commit introduces several improvements to the reminder functionality,
making it more robust and efficient. Updated reminders.ts, queue.ts and
tests. Overall, this provides a better experience for users.
```

```text
fix(reminders): stop after invoice is paid

Reminders were queued at invoice creation and never cancelled, so a
client who paid on day 6 still got the day 7 email. The payment
webhook now deletes pending reminder jobs for the invoice.

Fixes #412
```

#### Pull request descriptions

Generated PR descriptions have the same skeleton: a Summary heading, a Changes list of bold-label bullets, an Impact section full of adjectives, and "Let me know if you have any questions" at the bottom. They describe the diff the reviewer is about to read and leave out what the reviewer cannot see.

- First line: what the change does and why, in one or two sentences.
- How to test it: the exact commands or steps, and the expected result.
- Risk: what could break, what you did not test, whether it needs a migration or a flag.
- Screenshots for any visual change, before and after, at the same viewport width.
- Leave out anything the diff already shows. Leave out headings for empty sections.

```slop
## Summary
This PR introduces a comprehensive overhaul of the reminder system.

## Changes
- **Reminders:** Enhanced reminder logic for better reliability.
- **Tests:** Added robust test coverage.

## Impact
This change will significantly improve the user experience.

Let me know if you have any questions!
```

```text
Stops payment reminders once an invoice is paid. Clients who paid early were still getting the day 7 email (#412).

The payment webhook now deletes pending reminder jobs for the invoice. Jobs already picked up by a worker check the invoice status before sending.

To test: run `make seed`, mark INV-0003 as paid, then run `make reminders-due`. No email should be queued for INV-0003.

Risk: reminder jobs created before this deploy are not cancelled by the webhook. The status check in the worker covers them. No migration.
```

#### README intros

The generated README opens with the project name, a rocket, a wall of badges and `A blazing-fast, lightweight, modern library for building amazing apps`. The reader still does not know what it does or whether to install it.

- First sentence: what the project is and what it does, in plain nouns: "`tidemark-pdf` renders invoices to PDF from a JSON file."
- Second: who it is for or what it replaces, if that is not obvious.
- Then the install command and the smallest working example, both copy-pasteable.
- Status in one line: maintained or not, supported versions, license.
- At most 3 badges (build, version, license). No emoji in the title or headings.

```slop
# tidemark-pdf
A blazing-fast, lightweight, and modern PDF generation library that empowers developers to create stunning invoices with ease.

## Features
- **Fast:** Lightning-fast rendering
- **Flexible:** Endlessly customizable
- **Developer-friendly:** Intuitive API
```

```text
# tidemark-pdf

tidemark-pdf renders invoices to PDF from a JSON file. It handles multi-page line items, VAT summaries and right-to-left scripts.

npm install tidemark-pdf

npx tidemark-pdf invoice.json --out invoice.pdf

Node 20 or later. MIT license. Maintained by the Tidemark team; issues are answered within a week.
```

#### Release notes

Release notes are for the people who use the product. Generated ones start with "We're thrilled to announce", group everything under "New features" and "Improvements", and describe changes in the vocabulary of the codebase.

- Lead with the change that affects the most people, in their terms: what they can now do, or what stopped happening.
- One short paragraph per change: what changed, who it affects, anything they need to do.
- Date and version at the top. Link to docs for anything that needs explaining.
- Say what was removed or changed incompatibly, plainly, with the date it takes effect.
- No "thrilled", "excited" or "proud". No "various bug fixes and performance improvements" as a line on its own; name the fixes or leave the line out.

```slop
We're thrilled to announce Tidemark 4.2, our most powerful release yet!
New features: Enhanced reminders, improved dashboard, and more.
Various bug fixes and performance improvements.
```

```text
Tidemark 4.2, 14 October 2026

Reminders stop when a client pays. Before, a client who paid on day 6 could still get the day 7 email.

The invoice list loads in under a second for accounts with 10,000 invoices. It took up to 6 seconds.

Removed: the old PDF template "Classic". Invoices already sent keep it. New invoices use "Plain" from 1 November.
```

#### Changelog entries

A changelog is for developers and integrators. It is a dated, versioned list of changes, grouped by type. Generated changelogs merge it with marketing, inflate every line, and paste commit subjects in bulk.

- Follow the Keep a Changelog groups: Added, Changed, Deprecated, Removed, Fixed, Security.
- Newest version first, with an ISO date: `## 4.2.0 (2026-10-14)`.
- One line per change, starting with the thing that changed, linking the issue or PR.
- Breaking changes are marked and explain the migration in one line.
- No adjectives, no emoji category markers, no "Misc".

```slop
## v4.2.0
### New Features
- :rocket: Supercharged reminders engine
- :sparkles: Improved dashboard experience
### Misc
- Various fixes
```

```text
## 4.2.0 (2026-10-14)

### Fixed
- Reminder jobs are cancelled when an invoice is paid (#412).

### Changed
- `GET /invoices` returns 100 items per page instead of 50 (#398).

### Removed
- BREAKING: the `classic` PDF template. Pass `template: "plain"` instead (#377).
```

### 8.9 Voice

Generated copy has a voice, and it is the same voice everywhere: upbeat, general and slightly breathless. Removing the tells in this part leaves text that is plain. Voice is what makes plain text sound like a particular company.

#### Sound like a specific person or team

Decide who is talking. "The two engineers who built Tidemark" and "a large finance software vendor" produce different sentences from the same facts. Write it down and give every writer and every model prompt the same page.

A voice sheet fits on one screen:

- Who is speaking, in one sentence: "The people who build Tidemark, writing to freelancers who would rather be doing their real work."
- Five words or phrases you use, taken from real support tickets and sales calls ("late invoice", "chase", "paid", "client").
- Five you never use, beyond the banned list (for Tidemark: "users", "accounts receivable", "workflow", "platform", "experience").
- Three opinions the team holds and will state: "Reminders should be polite. Invoices should fit on one page. Prices should be on the website."
- Two samples of real text in the target voice: one support reply, one release note, written by people on the team.

Then run the swap test on every page: replace the product name with a competitor's. Copy that still reads as true is generic, and generic is what models produce by default. Copy that becomes false belongs to you.

Collect the team's own language. Support replies, sales call notes and internal chat are full of the phrases customers actually use. Put the best ones in the voice sheet and in prompts, and models will copy them instead of their defaults.

#### Reading level

- Interface copy: grade 6 to 8 on the Flesch-Kincaid scale. Short words, one idea per sentence.
- Marketing and onboarding: grade 7 to 9. Average sentence length 12 to 18 words, no sentence over 30.
- Technical docs: as high as the subject needs, but sentence length stays under 25 words on average. Hard concepts get short sentences.
- Keep the domain terms your readers use. Accountants know what "accrual" means; replacing it with a vague paraphrase reads as condescending. Explain a term once, where it first appears.
- Measure with a tool such as the `textstat` Python package, and treat the score as a check, not a target. A readable page with a grade 10 score is fine.

#### Contractions

- Use them in interface copy and marketing: "you'll", "can't", "it's", "we're". People speak in contractions, and text without them reads as a translated manual.
- Write "do not" and "cannot" in full for warnings where the negative must not be missed: "This cannot be undone."
- Avoid stacked or rare contractions ("it'll've", "mightn't") and contractions of nouns ("Tidemark'll").
- Pick a rule per document and keep it. This handbook uses few contractions because it is a reference; a product's onboarding should use more.

#### Second person

- Address the reader as "you". Refer to the company as "we" and to the product by name.
- Labels use "your" or no pronoun at all: "Your invoices" or "Invoices". Never "My invoices" in one place and "Your settings" in another.
- Never call the reader "the user" in text they read. "Users" belongs in internal documents.
- "We" appears in interface copy only when people at the company did or will do something: "We emailed you a receipt." System actions are described without a pronoun: "Receipt sent."
- Do not tell the reader how they feel ("You'll love...", "You're going to be amazed"). Describe the product and let them decide.

#### Numbers

- Digits for all numbers in interface copy, including 1 to 9: "3 invoices", "2 minutes ago".
- Thousands separators for numbers of 5 digits and more, following the reader's locale: 10,000 or 10 000 or 10.000.
- Dates that cannot be misread: "1 October 2026" or "Oct 1, 2026", by locale. Never 01/10/26. ISO dates (2026-10-01) in logs, changelogs and file names.
- Times include the time zone when people in more than one zone see them: "09:00 CET".
- Relative times ("3 minutes ago") for the last 24 hours, absolute dates after that. Show the absolute timestamp on hover and to screen readers.
- Currency with its symbol in single-currency products, with its ISO code when several currencies can appear: "EUR 1,200".
- Round in headlines only when the rounding is honest and stated nearby: "2,300 firms" above a footnote with "2,314 as of 1 October 2026".
- Units follow one style per product. This handbook writes durations as in CSS (300ms) and file sizes with a space (10 MB).

### 8.10 A full rewrite, start to finish

The tells rarely appear alone. Below is a feature section of the kind a model writes when asked for "a features section for an invoicing app", followed by the edit, step by step.

```slop
## Invoicing, Reimagined

Tired of chasing payments? You're not alone. Whether you're a freelancer or a growing agency, getting paid shouldn't feel like a full-time job -- and with Tidemark, it doesn't.

Tidemark isn't just an invoicing tool. It's your financial command center. From creating invoices to tracking payments, we've got you covered.

- **Smart Reminders:** Automatically follow up with clients so you don't have to.
- **Seamless Integrations:** Connect effortlessly with the tools you already love.
- **Powerful Insights:** Make data-driven decisions with real-time analytics.

The result? More time for what matters. Join 10,000+ businesses who trust Tidemark to get paid faster.
```

Tell count for those 100 or so words: a pun-adjacent title-case heading, a rhetorical question opener, a "Whether you are" opener, an em dash, a false contrast, a "From X to Y" range, three bold-label bullets (a tricolon of features), adverb inflation twice, a colon reveal, fake specificity, and eight banned words. Nothing in it is wrong in a way a fact-checker could catch. Nothing in it is true in a way a reader could use.

The edit, in order:

1. List the facts. Ask the product team what the feature does, in numbers. For this section the answers were: reminders go out on day 7, 14 and 30 in the sender's name; they stop when the bank feed shows the payment; there is a Xero and DATEV export; 2,314 teams were active on 1 October 2026; the median customer got paid 5 days sooner after turning reminders on, measured over 6 months for 1,100 accounts.
2. Throw away the draft. Editing generated sentences one word at a time keeps their shape, and the shape is the problem.
3. Write one sentence per fact, in the order a customer would ask about them.
4. Pick a heading that names the section.
5. Read it aloud and cut anything you would not say to a customer on the phone.

```text
## Payment reminders

Tidemark emails your client when an invoice is 7 days late, again at 14 days, and once more at 30. Each reminder is written in your name and sent from your address, and you get a copy.

Reminders stop as soon as the payment shows up in your bank feed, so nobody gets chased for money they already sent.

Across 1,100 accounts over six months, the median invoice was paid 5 days sooner after reminders were turned on.

Paid invoices export to Xero and DATEV.
```

The rewrite is about the same length and contains five checkable facts where the original contained none. It has no list, because the facts are a sequence and a consequence, which sentences carry better. The paragraph lengths vary from one line to three. The customer count is gone because this section is about reminders; it belongs near the pricing table, with its date.

### 8.11 Prompting a model for plain copy

Most slop comes from prompts that ask for tone instead of supplying facts. `Write a punchy, engaging hero section` gets the defaults, because tone words are all the model has to work from. Give it facts, a reader and constraints, and the output changes.

Give the model a fact sheet. Each line is a claim the copy may make, with its number and source. The model may use only these claims.

```text
Product: Tidemark, invoicing for freelancers and agencies up to 50 clients.
Reader: a freelancer who invoices 5 to 20 clients a month and chases payments by hand.
Fact: reminders on day 7, 14 and 30 after the due date, sent in the user's name.
Fact: reminders stop when the bank feed shows the payment.
Fact: median invoice paid 5 days sooner with reminders on (1,100 accounts, Apr to Sep 2026).
Fact: Solo plan $8 a month, 5 clients. Team plan $12 per seat per month.
Not a fact: anything about AI, security certifications or customer counts.
```

Then state the rules the copy must follow, as plain instructions:

```text
Write the hero headline and subhead for the pricing page.
Use only the facts above. If a sentence needs a fact that is not listed, leave the sentence out.
Headline under 10 words, sentence case, names what the product does.
Subhead one or two sentences with one number from the facts.
No questions, no colons used for suspense, no lists of three adjectives.
No exclamation marks, no emoji, no em dashes.
Do not use any word listed in banned-words.txt (attached).
Return three options, each under 30 words in total, and nothing else.
```

After generation, run the checks anyway:

- Run `scripts/lint.py` on the result. Models drift back to the lexicon over long outputs.
- Run the sentence searches in 9.3. The banned list catches words; the searches catch shapes.
- Check every number against the fact sheet. Models will round, combine and invent when a sentence seems to want a number.
- Read the three options aloud and pick the one that sounds most like the samples in the voice sheet. Then edit it by hand. A person signs off on every line that ships.

### 8.12 Quick reference

One row per tell from 8.2 to 8.4. The marker column lists the surface forms to search for; Part 9 turns them into commands.

| Tell | Typical markers | Fix |
| --- | --- | --- |
| False contrast | `isn't just`, `It's not about`, `We don't sell` | State the positive claim alone |
| Not just X, but Y | `not only`, `and so much more`, `and beyond` | Name the second thing or cut it |
| Groups of three | three adjectives, three clipped imperatives | Use the real count of items |
| Colon reveal | `The result:`, `The secret?`, `One word:` | Put the payoff in a normal sentence |
| Rhetorical opener | a question as the first sentence | Open with the answer |
| Imagine | `Imagine`, `What if` | Describe the state and the mechanism |
| Here is why | `Here's why`, `Here's how`, `That's exactly why` | Delete the announcement |
| Summary sentence | `In short`, `Simply put`, `All in all` | End on the last new fact |
| Whether you are A or B | `Whether you`, `teams of all sizes` | Name one audience |
| From X to Y | `from idea to launch` | List real steps and the limit |
| Sign-posting | `Let's break it down`, `In this guide` | Cut sentences about the text |
| Closing offer | `Let me know if`, `Hope this helps` | Contact route and response time, or nothing |
| Sycophantic opener | `Great question`, `Absolutely`, `Awesome` | Start with the answer |
| Em dash chains | U+2014, U+2013 | Period, comma, parentheses or colon |
| Hedging stacks | `can potentially`, `may possibly` | One named hedge or none |
| Fake specificity | `10,000+`, `up to`, `3x`, `Studies show` | Source, date and method, or remove |
| Adverb inflation | `seamlessly`, `simply`, `easily`, `incredibly` | Delete it, add the missing fact |
| Uniform paragraphs | equal blocks of 3 to 4 sentences | Let length follow content |
| Bulleted everything | lists of reasons, nested lists | Sentences with because, so, but |
| Bold-label bullets | `- **Label:**` | Drop the label or use a table |
| Title case | `Get Started With` | Sentence case |
| Pun headings | idioms, film lines | Name the content |

The table is a lookup aid, not a checklist to apply mechanically. A page can avoid every marker above and still say nothing. The test that matters is whether each sentence gives the reader a fact they can use, in words a person on the team would say.
