## Part 8. Sentences, Structure and Microcopy

A page with flat surfaces, one accent and a 2px radius still reads as generated when the hero says `Unlock seamless workflows`. Readers spot machine copy before they notice the shadows, because they read the words first. This part covers the words: the sentence patterns that mark copy as model output, the punctuation and formatting rules that follow from them, microcopy for each interface context, and voice.

Conventions for this part. Every bad example sits in a `slop` fence. Every rewrite sits in a `text` fence or in plain prose, and you can paste it. Examples use a fictional invoicing product called Tidemark so that the rewrites can carry real-looking facts. Replace those facts with your own; never ship the sample numbers.

### 8.1 How tells work

A single tell proves nothing. People write "not this, but that" and lists of three every day. The signal is density and placement. When the same construction appears in every paragraph, in the same slot (first sentence, last sentence, every heading), the reader stops reading the content and starts reading the template.

Use these thresholds when you edit or review copy:

- One instance of a given tell per 500 words is style. Leave it.
- Two instances of the same tell per 500 words is a habit. Rewrite one.
- Three or more instances of any tells in a single paragraph is a template. Rewrite the paragraph from its facts.

Models produce these patterns for three concrete reasons. First, the training data is heavy with landing pages, keynote scripts, SEO blog posts and social threads, which use the same moves to sound persuasive. Second, preference tuning rewards answers that sound complete and confident, so constructions that signal "a point is being made" score well even when no point is made. Third, decoding favors high-probability continuations, and phrases like "Here is why" or "The result:" are among the safest bridges between two sentences. None of these reasons involves your reader.

The fastest edit procedure for a draft full of tells:

1. Delete the first and last sentence of every paragraph. Reread. If nothing is lost, leave them deleted. This removes most openers and summaries in one pass.
2. Replace each adjective with a number, a name or a noun. If you cannot, delete the adjective.
3. Read the text aloud at speaking pace. Anything you would not say to a colleague across a desk gets rewritten.
4. Run `scripts/lint.py` and the searches in Part 9 to catch what your ear missed.

### 8.2 Tells of framing and argument

These tells shape how a sentence makes its claim. Each one substitutes a rhetorical move for a fact.

#### The false contrast: "It is not X, it is Y"

The sentence denies a claim nobody made, then asserts the real one. Variants include "X isn't just A. It's B.", "This is not about A. It is about B." and the clipped "Less A, more B." The negated half exists only to make the second half feel like a reveal.

Models produce it because it is the most common move in keynote and landing page copy, and because the negated half costs nothing: it needs no evidence and adds no information. Preference tuning rewards it because it reads as an opinion with conviction.

```slop
Tidemark isn't an invoicing tool. It's a new way to run your business.
This is not a redesign. It is a rethink of how teams collaborate.
Onboarding isn't about features. It's about confidence.
We don't sell software. We sell peace of mind.
```

```text
Tidemark sends invoices, records payments and reminds late clients by email.
The new editor saves every 2 seconds and shows who else is typing.
The first screen asks for one thing: the name of your first client.
Tidemark costs $12 a month. Cancel from Settings at any time.
```

Rule: state the positive claim alone. Keep a contrast only when the negated half is a misconception your readers hold, you can name it, and you give evidence against it. Once per page at most.

#### "Not just X, but Y"

An escalation that claims more scope than the sentence delivers. Variants: `not only A but also B`, `more than just a tool`, `A, B, and so much more`, `and beyond`. The second item is almost always vaguer than the first, so the sentence ends weaker than it started.

Models use it to sound generous. When a prompt says "describe the product", the model has one concrete feature and an instruction to sound large, so it adds an abstract second half.

```slop
Tidemark is not just an invoicing tool, but a complete financial command center.
It's more than just a calendar. It's your team's heartbeat.
Not only faster, but smarter.
Track expenses, send invoices, and so much more.
```

```text
Tidemark sends invoices and emails late clients after 7, 14 and 30 days.
The calendar shows each person's working hours in their own time zone.
Search returns results in under 100ms on workspaces with 50,000 documents.
Track expenses, send invoices and export to Xero or DATEV.
```

Rule: name the second thing concretely or cut it. "And more" means the list is unfinished. Finish the list or end the sentence.

#### Tricolons and groups of three

Three adjectives, three parallel clauses, three short imperative sentences, three bullet points, three feature cards. "Fast, simple and secure." "Plan. Build. Ship." The cadence of three is the default rhythm of generated copy, and it shows up far more often than two or four.

The rule of three is drilled into speechwriting and advertising, and models learned that three items sound finished. Layout templates add pressure: the Tailwind UI feature section is `grid-cols-3`, so the copy is written to fill exactly three slots whatever the product actually has.

```slop
Fast, secure, and reliable.
Plan smarter. Build faster. Ship with confidence.
Simple to use, easy to scale, and built to last.
Collaborate in real time, track progress effortlessly, and deliver results that matter.
```

```text
Pages load in 0.8 seconds on a 4G connection.
Plan the sprint in Tidemark, then ship it. Releases link back to their tasks.
Setup takes 10 minutes. It runs on one Postgres database.
Two people can edit the same invoice, and each sees the other's cursor.
```

Rule: count the items you actually have. Two facts get two items; four facts get four. Never pad a list to three and never trim one to three. In front of a noun, use at most one adjective, and prefer a number.

#### The colon reveal

A short setup, a colon or question mark, then the payoff: "The result: ...", "The secret? ...", "One word: speed." It builds suspense for a sentence that does not need any.

Newsletter and social thread writing uses it to keep readers scrolling, and models absorbed the cadence. The setup phrases ("The result", "The catch", "The bottom line") are high-probability bridges that let the model emphasize without adding a fact.

```slop
The result: a workflow that finally makes sense.
The secret? Consistency.
One word: speed.
The bottom line: your team ships faster.
```

```text
After the switch, month-end close took 2 days instead of 5.
Teams that sent invoices on the same weekday each month were paid 6 days sooner on average.
Builds take 40 seconds, down from 3 minutes.
```

Rule: put the payoff in the subject or verb of a normal sentence. Use a colon to introduce a list, a quotation, an example or a definition. Never use it for suspense.

#### Rhetorical question openers

A section or page that opens with a question the reader did not ask, answered in the next sentence. "Tired of juggling spreadsheets?" "What if your inbox could sort itself?" "Ever wondered why your builds are slow?"

Copywriting formulas such as problem, agitate, solve open with a question, and so do most SEO blog introductions. A model told to `make it engaging` reaches for the question first because it is the most common opening in that register.

```slop
Tired of chasing late payments?
What if your documentation wrote itself?
Ever wondered why your builds are so slow?
Why settle for less?
```

```text
Tidemark emails clients when an invoice is 7 days late.
The CLI generates reference pages from your OpenAPI file.
Most slow builds re-download dependencies on every run. Cache the lockfile hash.
```

Rule: open with the answer. Questions belong where the reader asked them: FAQ headings, search placeholders, form fields and confirmation dialogs.

#### "Imagine..."

A second-person fantasy before the product appears. `Imagine never losing a receipt again.` `Picture this: it is Friday at 5pm and your inbox is empty.` The reader is asked to invent the benefit the copy failed to state.

Ad scripts and keynote openings use the move to set a scene. A model with no facts to report can generate a scene indefinitely, which makes this a reliable filler.

```slop
Imagine a world where meetings run themselves.
Picture this: it's Friday at 5pm and your inbox is empty.
Imagine never losing a receipt again.
What if invoicing just... happened?
```

```text
Tidemark posts meeting notes to the channel within a minute of the call ending.
Forward a receipt to receipts@tidemark.example and it is attached to the matching expense.
Recurring invoices go out on the date you set, with the hours from your timesheet.
```

Rule: describe the state the product produces, in the present tense, with the mechanism that produces it. Readers can imagine without instruction.

#### "Here is why"

A sentence that announces the next sentence. `Here's why that matters.` `Here's how it works:` `Here's the thing.` `And that's exactly why we built Tidemark.` It delays the content by one sentence and adds nothing.

Assistant tuning rewards answers that sign their structure, and thread-style writing uses the announcement as a hook before each point. It is cheap to generate and scores as "clear".

```slop
We rebuilt the sync engine. Here's why that matters.
Here's the thing: most teams don't need another dashboard.
Here's how it works:
And that's exactly why we built Tidemark.
```

```text
We rebuilt the sync engine, so edits made offline now merge without conflicts.
Most teams already have a dashboard. Tidemark sends a weekly email instead.
Connect your bank. Tidemark matches each payment to its invoice.
We built Tidemark after spending a full day each month on our own invoices.
```

Rule: delete the announcing sentence and start with the reason. "How it works" may stay as a heading above a numbered procedure.

#### The summary sentence that restates the paragraph

The last sentence repeats the paragraph in vaguer words. `In short, your data is always safe.` `Simply put, Tidemark saves you time.` `The takeaway? Small changes add up.` At section level it becomes a closing paragraph that starts with `In conclusion`.

School essay structure (topic sentence, support, conclusion) is all over the training data, and raters prefer answers that close neatly. The model ends every unit with a wrap-up whether the unit needs one or not.

```slop
Exports run nightly and are stored for 90 days. In short, your data is always safe.
Simply put, Tidemark saves you time.
The takeaway? Small changes add up.
All in all, it's a win-win for everyone.
```

```text
Exports run nightly and are stored for 90 days in a second region.
Tidemark fills in client details from your last invoice to that client.
Moving the default due date from 30 days to 14 cut the share of late invoices from 31% to 22%.
```

Rule: end the paragraph on its last new fact. A paragraph long enough to need a summary is long enough to split.

#### The "Whether you are A or B" opener

An opener that claims two opposite audiences at once: `Whether you're a solo founder or a Fortune 500 company...`, `for teams of all sizes`, `from beginners to experts`. Writing for everyone means the reader cannot tell whether the product is for them.

Prompts rarely specify the audience, so the model covers every possibility in one clause. The construction is also a standard SEO introduction.

```slop
Whether you're a freelancer or a Fortune 500 company, Tidemark scales with you.
Whether you're just starting out or a seasoned pro, there's something for everyone.
Built for teams of all sizes.
Loved by startups and enterprises alike.
```

```text
Tidemark is for freelancers and agencies with up to 50 active clients.
The free plan covers 5 clients and unlimited invoices.
Used by 2,300 accounting firms in Germany and Austria.
```

Rule: name one audience. If two audiences use the product differently, give each its own page or section and write each one for that reader.

#### "From X to Y" ranges

A range that implies full coverage of a process or market: "from idea to launch", "from onboarding to offboarding", "from solo creators to global teams". Two endpoints stand in for everything in between, and the reader is left to assume the middle exists.

The construction is a shortcut to sounding complete, the sentence-level version of the `end-to-end` claim. It also has a fixed rhythm that models reuse, often twice in one paragraph.

```slop
From idea to launch, we've got you covered.
Everything you need, from planning to payroll.
From first commit to production, all in one place.
From solo creators to global enterprises.
```

```text
Write the spec, assign the tasks, publish the release notes. Payroll is a separate product.
Tidemark covers invoicing and expenses. Payroll exports to Personio as a CSV.
Push to main and the preview deploys in about 90 seconds.
```

Rule: list the steps you actually cover and say where coverage ends. A stated limit is more believable than an implied infinity.

#### Sign-posting

Sentences about the text instead of the subject: "Let's break it down.", "In this guide, we'll explore...", "Without further ado", "Now let's take a closer look at...", "First things first." They describe the reading experience while the reader is having it.

Tutorial blogs and chat assistants use sign-posts to sound guided, and they pad length at almost no cost. Models emit them at every section boundary.

```slop
Let's break it down.
In this guide, we'll explore everything you need to know about invoicing.
Without further ado, let's dive in.
Now, let's take a closer look at the dashboard.
```

```text
An invoice needs four fields: client, line items, due date and currency.
The dashboard has two panels. Unpaid invoices are on the left, paid on the right.
```

Rule: cut every sentence that describes the document. Headings do the sign-posting; a table of contents does the rest.

#### The closing offer

Assistant residue at the end of text that is no longer a chat: `Let me know if you have any questions.`, `Feel free to reach out.`, `Hope this helps.`, `Happy coding.` It turns up in READMEs, docs, onboarding emails, commit messages and even interface copy.

Assistant tuning ends each turn with an offer to continue. When that output is pasted into a product or a repository, the offer comes with it and addresses the reader as a chat partner who cannot reply.

```slop
Let me know if you'd like me to adjust anything.
Feel free to reach out if you have any questions.
I hope this helps. Happy coding.
Don't hesitate to contact our friendly support team.
```

```text
Questions go to support@tidemark.example. We answer within one working day.
To report a bug, open an issue and include the version from Settings > About.
```

Rule: end product text with a contact route and a response time, or with nothing. In docs, code comments and commit messages, never address the reader as if they could answer back in the same window.

#### Sycophantic openers

Praise or agreement before the content: `Great question.`, `Absolutely.`, `You're absolutely right.`, `Certainly.` In interfaces it becomes cheerleading: `Awesome. You've added an item.`, `Nice work.`, `You're all set, superstar.`

Preference tuning rewards an agreeable tone, so the model leads with approval. The habit leaks into PR replies, docs written in chat, and success toasts.

```slop
Great question. Invoices can be edited until they're sent.
Absolutely. Here's an updated version of the component.
Awesome job. You've created your first project.
You're absolutely right, and that's a great catch.
```

```text
Invoices can be edited until they are sent.
Updated the component. The button now disables while the request runs.
Project created.
Fixed. The off-by-one was in the pagination offset.
```

Rule: start with the answer or the result. Praise the reader only where a person would, which in product copy is almost never. A person saving a form does not want to be congratulated.

### 8.3 Tells of texture

These tells sit inside sentences rather than in their framing. They survive a rewrite of the argument and need a second pass at the word level.

#### Em dash chains

The em dash used as an all-purpose connector: one or two per paragraph, often in pairs around an aside, often in front of a punchline. One dash in a long essay is unremarkable. A dash in every paragraph of a landing page is the most widely recognized marker of model output in English, and many readers now stop trusting a page at the second one.

Models learned the dash from edited magazine and book prose, where it is common, then use it at several times that rate because it lets a sentence keep going without choosing a relationship between its clauses. A comma, colon or period would each force a decision; the dash avoids it.

This file may not contain the dash character itself, so the slop examples below show each em dash as two hyphens.

```slop
Tidemark isn't just fast -- it's fast where it counts -- on your phone, offline, everywhere.
We built it for one reason -- you.
Sync -- the hard part -- is finally solved.
Your invoices, your clients, your rules -- all in one place.
```

```text
Tidemark works offline on your phone and syncs when you reconnect.
We built it because our own invoicing took a full day each month.
Sync is the hard part. Edits made offline now merge without conflicts.
Invoices, clients and payment rules live in one workspace.
```

Rule: no em dashes and no en dashes, in copy or in code comments. Choose the relationship. A break gets a period, a pause gets a comma, an aside gets parentheses, a list or definition gets a colon. Ranges use "to": "9 to 5", "pages 4 to 9", "Monday to Friday". Hyphens stay for compound words and ISO dates such as 2026-10-15.

#### Hedging stacks

Two or more hedges on a single claim: "can potentially help", "may possibly reduce", "could help to improve", "might be able to", "in some cases it may". Hype and hedging often appear together, which gives sentences like "can potentially transform the way you work", a large claim with its own escape hatch.

Safety tuning teaches models to avoid overclaiming, so they add a hedge to anything that sounds like a promise. Marketing training pushes the other way. The result is a sentence that claims a lot and commits to nothing.

```slop
This can potentially help improve your team's productivity.
Caching may possibly reduce load times in some cases.
It might be worth considering whether you could perhaps simplify the form.
Tidemark can help you potentially get paid faster.
```

```text
Teams using the shared inbox answered tickets 2 hours sooner at the median.
Caching the API response cut median load time from 1.4s to 0.6s.
Cut the form to four fields.
Clients who get a reminder on day 7 pay 5 days sooner on average.
```

Rule: one hedge per claim, and only when you can name the uncertainty: "on Chrome 120 and later", "for accounts created after March", "in our test with 40 users". Otherwise state the claim plainly or delete it.

#### Fake specificity

Numbers, names and sources that look precise and are invented or unverifiable: "Trusted by 10,000+ teams", "Save 10 hours a week", "3x faster", "99.99% uptime", "Studies show". Testimonials from "Sarah K., Product Manager" with a stock avatar. A row of famous company logos with no customer story behind any of them.

Prompts tell models to "be specific", and the model satisfies the instruction with plausible numbers. The signature is the round number with a plus sign or an "up to", and the source that cannot be checked.

```slop
Trusted by 10,000+ teams worldwide.
Save up to 10 hours every week.
3x faster than the competition.
"Tidemark changed how we work." -- Sarah K., Product Manager
Studies show that automated reminders increase on-time payments by 80%.
```

```text
Used by 2,314 teams as of 1 October 2026.
In our March 2026 survey of 412 customers, the median time saved was 3 hours a month.
Renders a 10,000-row table in 120ms on a 2020 MacBook Air. Version 2 took 380ms.
"We stopped writing reminder emails by hand." Dana Okafor, finance lead at Hollis and Reed.
```

Rule: every number states its source, its date and its method, or it comes out. An odd number such as 2,314 is fine when it is real; an invented round one is never fine. Testimonials use a full name, a role and an organization, with written permission. Without data, describe the mechanism instead of a result.

#### Adverb inflation

Adverbs propping up verbs and adjectives: `seamlessly integrates`, `effortlessly reorder`, `incredibly fast`, `truly unique`, `simply drag`, `easily manage`, `instantly see`. Remove them and the sentence usually means the same thing, which shows they were never carrying weight.

Intensifiers raise perceived enthusiasm, and marketing training rewards enthusiasm. "Simply" and "easily" come from documentation, where writers use them to signal that a step is short.

```slop
Seamlessly integrates with your existing tools.
Simply drag and drop to effortlessly reorder tasks.
An incredibly fast, truly delightful experience.
Easily manage your team's permissions.
```

```text
Connects to Slack, GitHub and Google Drive.
Drag a task to reorder it.
Opens in 300ms on a mid-range Android phone.
Set permissions per project: view, comment or edit.
```

Rule: delete the adverb. If the sentence gets weaker, the adverb was hiding a missing fact; add the fact. Never write "simply", "just" or "easily" in instructions. For the reader who is stuck, the step was not simple, and the word tells them the fault is theirs.

#### Uniform paragraph length

Every paragraph runs three or four sentences and 50 to 80 words. Each opens with a topic sentence and closes with a summary. Sentences cluster between 15 and 22 words. On screen the text forms blocks of equal height, like a wall of identical bricks.

Models generate at a steady length because nothing in the prompt asks them to vary it. A person writes a one-line paragraph when one fact deserves its own line and a long one when an argument needs room.

```slop
Invoicing is one of the most time-consuming tasks for small businesses. Between tracking hours, chasing payments, and reconciling accounts, it can take days each month. That's why we built Tidemark.

Tidemark automates the entire invoicing process from start to finish. It connects to your bank, tracks every payment, and sends reminders automatically. The result is less admin and more time for what matters.

Getting started takes just minutes. Simply connect your bank account, import your clients, and send your first invoice. It's that easy.
```

```text
Tidemark sends invoices and chases the late ones.

Connect your bank and Tidemark marks each invoice as paid when the money arrives. If an invoice is 7 days late, the client gets a reminder written in your name and you get a copy. After 30 days the reminders stop and Tidemark tells you, because by then a phone call works better than a fourth email.

Setup takes about 10 minutes.
```

Rule: let length follow content. On a 600-word page the longest paragraph should be at least three times the length of the shortest. Mix sentence lengths, and include some under 8 words. A one-sentence paragraph is allowed and often right.
