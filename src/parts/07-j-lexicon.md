#### 316. `on the cusp`

- Kind: phrase. Banned forms: `on the cusp`, `on the cusp of`, `on the verge of`, `on the brink of`.
- Why it reads as machine text: `on the cusp of` places a result just ahead in time so the writer never has to say when it arrives. Models use it for breakthroughs and launches that have no date. The reader cannot tell whether `cusp` means next week or next decade.
- Where it shows up: research news, startup announcements, and investor updates.

```slop
We are on the cusp of a breakthrough in battery life.
The industry is on the cusp of a major shift to edge computing.
Our team is on the verge of launching something big.
```

Replace with:

- The date or the condition: "ships in March", "after the FDA review".
- The current status, named: "in private beta with 40 users".
- The specific result so far, with its number.
- Cut it when there is no date and no status; then there is no news.

Rewrites:

```slop
We are on the cusp of a breakthrough in battery life.
```

After: Our test cell holds 80% of its charge after 1,500 cycles; production samples are due in Q2.

```slop
The industry is on the cusp of a major shift to edge computing.
```

After: Three of our five largest customers asked to run inference on their own hardware this year.

```slop
Our team is on the verge of launching something big.
```

After: We launch shared workspaces on 12 November.

- Literal use: in geometry or astrology, `cusp` is a defined term; use it as a noun in that field only, in its technical sense.

#### 317. `pave the way`

- Kind: phrase. Banned forms: `pave the way`, `paves the way for`, `paving the way`, `lay the groundwork`.
- Why it reads as machine text: `paves the way for` describes a change by what it might enable later, so the change itself goes unnamed. Models use it to inflate a small step ("this refactor paves the way for future features"). The future features are never listed.
- Where it shows up: PR descriptions, roadmap posts, and grant applications.

```slop
This refactor paves the way for future improvements.
Her research paved the way for modern vaccines.
The new API lays the groundwork for a plugin system.
```

Replace with:

- "lets us" or "unblocks" followed by the named next step.
- "is required for" when the change is a prerequisite.
- The specific later result and the link between the two.
- Cut it when the future step is not planned; describe the change on its own terms.

Rewrites:

```slop
This refactor paves the way for future improvements.
```

After: This refactor splits `Editor` into 4 components, so we can lazy-load the toolbar next sprint.

```slop
Her research paved the way for modern vaccines.
```

After: Her 2005 paper showed how to stop the immune system attacking synthetic mRNA; both 2020 mRNA vaccines use that method.

```slop
The new API lays the groundwork for a plugin system.
```

After: The new API exposes hooks for save and export; plugins will register against them in v3.

- Literal use: for road work, write "pave the road" or "resurface the car park".

#### 318. `bridge the gap`

- Kind: phrase. Banned forms: `bridge the gap`, `bridges the gap between`, `bridging the gap`, `close the gap`.
- Why it reads as machine text: `bridges the gap between X and Y` names two groups and claims a connection without describing it. Models use it for any tool that sits between two roles, most often design and development. The mechanism, which is the only useful part, is left out.
- Where it shows up: product taglines, conference talk titles, and job descriptions.

```slop
Our tool bridges the gap between design and development.
This course bridges the gap between theory and practice.
We are bridging the gap between patients and doctors.
```

Replace with:

- The mechanism: what moves from one side to the other, and how.
- The specific thing learners do, for courses.
- The action either party takes, named.
- Cut it when you cannot name what crosses the gap.

Rewrites:

```slop
Our tool bridges the gap between design and development.
```

After: The plugin exports Figma color and spacing styles as CSS variables in one file.

```slop
This course bridges the gap between theory and practice.
```

After: Each week you read one paper and then implement its algorithm in Python.

```slop
We are bridging the gap between patients and doctors.
```

After: Patients book a video visit with a GP in under 10 minutes.

- Literal use: for a measured difference, give both numbers: "cut the gap between test and production timings from 300ms to 20ms".

#### 319. `stand out from the crowd`

- Kind: phrase. Banned forms: `stand out from the crowd`, `stand out from the competition`, `set yourself apart`.
- Why it reads as machine text: `stand out from the crowd` promises a difference and names neither the crowd nor the difference. Models write it for resume services, design agencies, and portfolio templates, so the same promise appears across every competitor. Copy that claims distinction in a stock phrase undercuts itself.
- Where it shows up: agency sites, resume advice, and app store descriptions.

```slop
Make your portfolio stand out from the crowd.
Our designs help your brand stand out from the competition.
Set yourself apart with a resume that gets noticed.
```

Replace with:

- The specific difference, named: what you have that the others do not.
- The outcome with a number: interview rate, click rate.
- The concrete service step.
- Cut it when the difference is not stated in the same sentence.

Rewrites:

```slop
Make your portfolio stand out from the crowd.
```

After: Show 3 projects, each with the problem, your role, and one result in numbers.

```slop
Our designs help your brand stand out from the competition.
```

After: We design packaging for coffee roasters; our last 5 clients moved into 2 national supermarket chains.

```slop
Set yourself apart with a resume that gets noticed.
```

After: We rewrite your resume around outcomes; clients report a 30% higher callback rate.

- Literal use: for visual contrast, give the values: "the button is #B4441C on #F7F5F0, the only orange on the page".

#### 320. `cut through the noise`

- Kind: phrase. Banned forms: `cut through the noise`, `cuts through the clutter`, `rise above the noise`.
- Why it reads as machine text: `cut through the noise` claims a filter without describing what it filters or by what rule. Models use it for newsletters, dashboards, and analytics tools. The phrase itself is one of the stock lines that makes up the noise.
- Where it shows up: newsletter signups, monitoring tool pages, and marketing plans.

```slop
Our newsletter cuts through the noise to bring you what matters.
The dashboard helps your team cut through the noise.
Cut through the clutter with smart notifications.
```

Replace with:

- The filter rule: what is shown and what is hidden.
- The count: "5 links a week", "one alert per incident".
- The source and the selection method.
- Cut it when there is no stated rule.

Rewrites:

```slop
Our newsletter cuts through the noise to bring you what matters.
```

After: Every Friday, 5 links on database engineering, each with a two-line summary.

```slop
The dashboard helps your team cut through the noise.
```

After: The dashboard shows only services with errors above 1% in the last hour.

```slop
Cut through the clutter with smart notifications.
```

After: Related alerts are grouped into one notification per incident.

- Literal use: for audio, name the method: "the noise gate removes hum below -40 dB".

#### 321. `ahead of the curve`

- Kind: phrase. Banned forms: `ahead of the curve`, `stay ahead of the curve`, `stay ahead`.
- Why it reads as machine text: `ahead of the curve` claims early adoption without naming what was adopted or when. Models use it in course pages and consulting copy that sell anxiety about falling behind. The curve is never drawn.
- Where it shows up: newsletters, course pages, and consulting pitches.

```slop
Stay ahead of the curve with our weekly AI briefing.
Our clients are always ahead of the curve.
This framework keeps your team ahead of the curve.
```

Replace with:

- What the reader learns, and how soon after it happens.
- The specific early move a client made, with its date.
- The concrete feature the framework has that others lack.
- Cut it when there is no date; "ahead" needs a time to be ahead of.

Rewrites:

```slop
Stay ahead of the curve with our weekly AI briefing.
```

After: Each Monday: the model releases and papers from the past week, in 10 minutes of reading.

```slop
Our clients are always ahead of the curve.
```

After: Two of our clients moved to passkeys in 2023, before their banks did.

```slop
This framework keeps your team ahead of the curve.
```

After: The framework supports React Server Components and streaming without a plugin.

- Literal use: for a chart or a grading curve, name the axis and value: "scores above the median".

#### 322. `push the boundaries`

- Kind: phrase. Banned forms: `push the boundaries`, `pushing the envelope`, `push the limits`.
- Why it reads as machine text: `push the boundaries` claims a limit was moved without naming the limit or the new position. Models use it for creative work and engineering alike. Most work described this way is ordinary work done well.
- Where it shows up: portfolio sites, design award entries, and company values pages.

```slop
We push the boundaries of what's possible on the web.
Her work pushes the boundaries of typography.
Our engineers push the limits of performance every day.
```

Replace with:

- The specific limit and the new value: "a 3D scene in 60 KB of JavaScript".
- What was done that others had not done, with a source.
- A number for performance.
- Cut it when the work is good but not new; say what it is.

Rewrites:

```slop
We push the boundaries of what's possible on the web.
```

After: Our product page renders a 3D model in 60 KB of JavaScript and runs at 60 fps on a 2019 phone.

```slop
Her work pushes the boundaries of typography.
```

After: She designed a variable font with a width axis that adjusts to the reader's screen size.

```slop
Our engineers push the limits of performance every day.
```

After: Our matching engine handles 2 million orders per second on 4 servers.

- Literal use: for a property line or a UI hit area, name the edge: "the drag handle extends 8px past the card border".

#### 323. `outside the box`

- Kind: phrase. Banned forms: `outside the box`, `think outside the box`, `out-of-the-box thinking`.
- Why it reads as machine text: `think outside the box` announces an unusual idea and delivers none. It is one of the oldest business clichés, and models use it in job ads and team values lists. The phrase is itself inside the box it names.
- Where it shows up: job descriptions, workshop invitations, and pitch decks.

```slop
We're looking for engineers who think outside the box.
Our team takes an outside-the-box approach to problem solving.
This workshop teaches you to think outside the box.
```

Replace with:

- The unusual idea, stated: what was tried that is not the default.
- The kind of problem candidates will solve, with an example.
- The exercise the workshop runs.
- Cut it when no unusual idea follows.

Rewrites:

```slop
We're looking for engineers who think outside the box.
```

After: You will cut our cloud bill; last year an engineer saved 30% by moving batch jobs to spot instances.

```slop
Our team takes an outside-the-box approach to problem solving.
```

After: Before writing code, we test each feature as a paper prototype with 5 users.

```slop
This workshop teaches you to think outside the box.
```

After: In this workshop you write 20 headline options in 10 minutes, then cut to 3.

- Literal use: for software defaults, write "by default" or "with no setup": "works with no config". For packaging, write "in the box" with the contents.

#### 324. `a wide range of`

- Kind: phrase. Banned forms: `a wide range of`, `a broad range of`, `a whole range of`.
- Why it reads as machine text: `a wide range of` stands in for a list the writer did not make or a count they did not check. Models produce it whenever a brief says a product supports many things. The reader cannot tell whether the range is 4 or 400.
- Where it shows up: feature pages, integration lists, and service descriptions.

```slop
We support a wide range of file formats.
The library works with a wide range of frameworks.
Our team has experience across a wide range of industries.
```

Replace with:

- The count and the top items: "42 formats, including PDF, DOCX, and HEIC".
- The full list, if it is under 8 items.
- The two or three industries with the most work, and the project count.
- Cut it when the list follows; the list proves the range.

Rewrites:

```slop
We support a wide range of file formats.
```

After: We read 42 formats, including PDF, DOCX, HEIC, and RAW files from 30 camera brands.

```slop
The library works with a wide range of frameworks.
```

After: The library works with React, Vue, Svelte, and plain JavaScript.

```slop
Our team has experience across a wide range of industries.
```

After: We have built 30 apps for banks and 12 for hospitals.

- Literal use: for a numeric range, give the range: "8 to 64 GB", "temperatures from -20 to 45 C".

#### 325. `a wide array of`

- Kind: phrase. Banned forms: `a wide array of`, `an array of`, `a broad array of`.
- Why it reads as machine text: `a wide array of` is the formal twin of "range", and models alternate the two within a page to avoid repeating themselves. The word "array" adds an air of precision to a phrase that has none. In technical writing it also collides with the data structure.
- Where it shows up: course catalogs, "Our services" pages, and generated documentation intros.

```slop
The platform offers a wide array of customization options.
Students can choose from a wide array of electives.
The SDK provides a wide array of helper functions.
```

Replace with:

- The specific options a user will look for first: colors, fonts, layout.
- A count with a link to the full list.
- The three helpers most people need, by name.
- Cut it when the next sentence lists the items.

Rewrites:

```slop
The platform offers a wide array of customization options.
```

After: You can change the logo, the accent color, the font, and the email sender name.

```slop
Students can choose from a wide array of electives.
```

After: Students choose 4 of 26 electives; the full list is on the course page.

```slop
The SDK provides a wide array of helper functions.
```

After: The SDK includes `retry()`, `paginate()`, and `signRequest()`, plus 18 smaller helpers.

- Literal use: for the data structure, give its type and size: "an array of 4,096 `u32` entries". For hardware, "a solar array of 24 panels".

#### 326. `look no further`

- Kind: opener. Banned forms: `look no further`, `search no more`, `you've come to the right place`.
- Why it reads as machine text: `Look no further` answers a question the reader did not ask and claims to end a search the page has not ended. It is a classifieds and SEO opener, and models reproduce it at the top of product and service pages. The sentence before it is usually a rhetorical question about the reader's needs.
- Where it shows up: SEO landing pages, local business sites, and app store blurbs.

```slop
Looking for a reliable hosting provider? Look no further.
Look no further for the perfect React component library.
If you need a plumber in Leeds, you've come to the right place.
```

Replace with:

- The offer, stated in the first sentence: who you are, what you do, where.
- The specific proof: uptime, price, coverage area.
- A direct call to action with the next step.
- Cut it when the headline already says what you sell.

Rewrites:

```slop
Looking for a reliable hosting provider? Look no further.
```

After: Managed Postgres hosting in Frankfurt with 99.95% uptime over the past 12 months.

```slop
Look no further for the perfect React component library.
```

After: 48 accessible React components, styled with CSS variables and no runtime dependency.

```slop
If you need a plumber in Leeds, you've come to the right place.
```

After: Plumbers in Leeds, same-day visits, call-out fee 60 pounds.

- Literal use: none.

#### 327. `whether you're`

- Kind: phrase. Banned forms: `whether you're`, `whether you are a`, `whether you're a beginner or a pro`.
- Why it reads as machine text: `Whether you're a beginner or a seasoned pro` names two poles of an audience to claim it serves everyone. Models write this two-pole sentence at the top of tutorials and product pages because briefs rarely name a reader. A text written for everyone fits nobody, and the phrase admits it.
- Where it shows up: tutorial intros, course pages, and product heroes.

```slop
Whether you're a beginner or a seasoned pro, this guide has something for you.
Whether you're building a blog or an enterprise app, our framework scales.
Whether you're on the go or at your desk, stay connected.
```

Replace with:

- The one reader you wrote for, named: "This guide is for developers who know Git and have never used rebase."
- Two paths with labels, if you serve two audiences: "New to Git: start at 2.1. Already use it: skip to 4."
- The actual limits: smallest and largest supported case, in numbers.
- Cut it when the poles are invented; pick the reader.

Rewrites:

```slop
Whether you're a beginner or a seasoned pro, this guide has something for you.
```

After: This guide is for developers who use Git daily and have never run `git rebase -i`.

```slop
Whether you're building a blog or an enterprise app, our framework scales.
```

After: Sites built with the framework range from 3 pages to 40,000; build time grows about linearly.

```slop
Whether you're on the go or at your desk, stay connected.
```

After: The app syncs between phone and desktop within 2 seconds.

- Literal use: in a form or a branching instruction, write the condition as "If you are X, do Y."

#### 328. `more than just`

- Kind: phrase. Banned forms: `more than just`, `not just a`, `so much more than`.
- Why it reads as machine text: `more than just a X` sets up a category so it can claim to exceed it, and then the extra is rarely named. Models use this reframe in product taglines and About pages (`more than just a to-do app`). It is a variant of the "not X, but Y" shape, which the house style bans.
- Where it shows up: taglines, About pages, and feature launch posts.

```slop
It's more than just a to-do app.
We're more than just an agency; we're your partner.
Our coffee is more than just a drink.
```

Replace with:

- The category, then the specific extra: "A to-do app with a shared calendar."
- What you do for the client, with a duration or count.
- The product facts: origin, roast, price.
- Cut it when the extra is a feeling; name a feature or drop the line.

Rewrites:

```slop
It's more than just a to-do app.
```

After: A to-do app that blocks time on your calendar for each task.

```slop
We're more than just an agency; we're your partner.
```

After: We run your ads and join your weekly planning call; average client stay is 4 years.

```slop
Our coffee is more than just a drink.
```

After: Single-origin beans from Huila, Colombia, roasted on Tuesdays and shipped Wednesdays.

- Literal use: for a minimum, use a number: "more than 3 retries", "over 10 GB".

#### 329. `imagine a world`

- Kind: opener. Banned forms: `imagine a world`, `imagine a world where`, `imagine if`, `what if you could`.
- Why it reads as machine text: `Imagine a world where` opens a pitch with a fantasy so the product can arrive as its fulfillment. Models produce it for keynote openers and landing pages. The imagined world is a feature list in the future tense.
- Where it shows up: pitch decks, keynote scripts, and the first paragraph of launch posts.

```slop
Imagine a world where deployments never fail.
Imagine a world where your inbox manages itself.
What if you could build an app in minutes, not months?
```

Replace with:

- The current problem, stated with its cost.
- The proposed change and what it does now, not in an imagined world.
- The measured time, for "minutes not months" claims.
- Cut it when the next sentence is the product; start there.

Rewrites:

```slop
Imagine a world where deployments never fail.
```

After: Failed deploys cost our customers 6 hours a month on average. The new canary step rolls back in 30 seconds.

```slop
Imagine a world where your inbox manages itself.
```

After: The app files newsletters and receipts into folders, so your inbox shows only mail from people.

```slop
What if you could build an app in minutes, not months?
```

After: A form-based internal tool takes about 2 hours to build with the template.

- Literal use: in fiction or a design brief that asks for speculation, describe the world in plain present tense: "In this scenario, cars have no drivers."

#### 330. `picture this`

- Kind: opener. Banned forms: `picture this`, `picture this:`, `imagine this`, `envision this`.
- Why it reads as machine text: `Picture this:` opens a staged scenario, usually a frustrated user at 2am, so the product can enter as the fix. Models use it to fake a story at the top of a blog post. The scenario is generic, so the reader does not see themselves in it.
- Where it shows up: blog post openers, sales emails, and conference talks.

```slop
Picture this: it's 2am and production is down.
Picture this: your team ships features twice as fast.
Imagine this: you open your laptop and your tasks are already sorted.
```

Replace with:

- A real case, dated, with the details: who, when, what broke.
- The measured result, stated as fact.
- The feature in plain present tense.
- Cut it when the scenario is invented; use a real one or none.

Rewrites:

```slop
Picture this: it's 2am and production is down.
```

After: At 02:14 on 9 May our payments API went down for 47 minutes because a certificate expired.

```slop
Picture this: your team ships features twice as fast.
```

After: After moving to trunk-based development, the team went from 6 releases a month to 14.

```slop
Imagine this: you open your laptop and your tasks are already sorted.
```

After: Each morning the app sorts your tasks by due date and blocks out meetings.

- Literal use: to ask a reader to look at an image, refer to it: "Figure 3 shows the request path."

#### 331. `here's the thing`

- Kind: opener. Banned forms: `here's the thing`, `here's the kicker`, `here's why`, `here's what`.
- Why it reads as machine text: `Here's the thing:` builds suspense before a point that could have been the first sentence. It is a spoken tic copied into writing, and models use it to signal candor. The house style also bans the colon reveal it introduces.
- Where it shows up: opinion posts, LinkedIn posts, and chat replies that push back.

```slop
Here's the thing: most apps don't need a microservices architecture.
Here's the kicker: it's completely free.
Here's why that matters: users notice slow pages.
```

Replace with:

- The point, as the first sentence.
- The fact placed with the others, at its normal weight.
- The cause and effect in one sentence with "because".
- Cut it every time; the clause after it stands alone.

Rewrites:

```slop
Here's the thing: most apps don't need a microservices architecture.
```

After: An app with one team and under 100,000 users runs fine as a single service.

```slop
Here's the kicker: it's completely free.
```

After: The plan is free for up to 3 users.

```slop
Here's why that matters: users notice slow pages.
```

After: When the page took over 3 seconds, half of mobile visitors left before it loaded.

- Literal use: when handing someone an object in dialogue, write "This is the cable you asked for."

#### 332. `the best part`

- Kind: phrase. Banned forms: `the best part`, `the best part?`, `best of all`, `and the best part is`.
- Why it reads as machine text: `The best part?` sets up a reveal with a fragment question and a one-line answer, usually the price or a feature. Models use the shape in marketing and social posts. The rhetorical question is banned by house style, and the reveal is usually a fact that belongs in a list.
- Where it shows up: product launches, social posts, and newsletter promos.

```slop
The best part? It's completely free.
And the best part is, you don't need to write any code.
Best of all, it integrates with the tools you already use.
```

Replace with:

- The fact in the place where readers look for it: price in the pricing line, requirements in the setup section.
- The list of integrations, named.
- The setup step count, for "no code" claims.
- Cut it when the reveal is one feature among several; list it with them.

Rewrites:

```slop
The best part? It's completely free.
```

After: Free for teams of up to 5.

```slop
And the best part is, you don't need to write any code.
```

After: You set it up by connecting a spreadsheet and choosing columns; no code is needed.

```slop
Best of all, it integrates with the tools you already use.
```

After: It connects to Slack, Linear, and GitHub.

- Literal use: for the portion of something, name the part: "the second half of the talk", "the chapter on indexes".

#### 333. `i hope this helps`

- Kind: closer. Banned forms: `i hope this helps`, `hope this helps`, `I hope this clarifies`, `I hope you found this useful`.
- Why it reads as machine text: `I hope this helps` is the default last line of a chat assistant answer, appended whether the answer was a fix, a list, or a refusal. It adds no information and asks the reader to absorb a pleasantry at the point they want to act. When agents leave it in code comments or commit messages, it shows that chat output was pasted without edits.
- Where it shows up: the last line of chat replies, Stack Overflow answers, and code comments written by assistants.

```slop
Let me know if you have any other questions. I hope this helps!
// Hope this helps! This function handles the edge case you mentioned.
I hope this clarifies the difference between `let` and `const`.
```

Replace with:

- The last step or the verification command, as the final line: "Run `npm test` to confirm."
- The one open question that changes the answer: "If you are on Node 16, use option B instead."
- In code comments, the reason for the code and nothing else.
- Cut it every time; end on the answer.

Rewrites:

```slop
Let me know if you have any other questions. I hope this helps!
```

After: Run `npm run build` again; the error should be gone. If it remains, send the full stack trace.

```slop
// Hope this helps! This function handles the edge case you mentioned.
```

After: `// Returns null for empty input; callers in checkout rely on this.`

```slop
I hope this clarifies the difference between `let` and `const`.
```

After: Use `const` unless you reassign the variable; `let` is for counters and loop state.

- Literal use: none in technical text. In a personal letter, say what you hope for specifically: "I hope the move to Lyon goes smoothly."

#### 334. `happy coding`

- Kind: closer. Banned forms: `happy coding`, `happy hacking`, `happy building`, `happy debugging`.
- Why it reads as machine text: `Happy coding!` is the sign-off of generated tutorials and chat answers, added after the last code block. It came from forum and blog culture and models copy it as a friendly default. In a README or a code comment it reads as filler a reviewer will delete.
- Where it shows up: tutorial endings, README files, chat replies with code, and generated code comments.

```slop
That's it! You've built your first REST API. Happy coding!
# Happy hacking! Feel free to modify this script.
Now you're ready to deploy. Happy building!
```

Replace with:

- A next step link: "Next: add authentication (part 3)."
- In a script header, what the script does and how to run it.
- A summary of what is now running and where, for deploy guides.
- Cut it every time; the reader does not need a sign-off from a document.

Rewrites:

```slop
That's it! You've built your first REST API. Happy coding!
```

After: The API now serves `GET /books` and `POST /books` on port 3000. Part 3 adds authentication.

```slop
# Happy hacking! Feel free to modify this script.
```

After: `# Resizes every PNG in ./in to 1200px wide. Usage: ./resize.sh in out`

```slop
Now you're ready to deploy. Happy building!
```

After: Run `fly deploy`; the app will be live at `your-app.fly.dev` in about 2 minutes.

- Literal use: none.

#### 335. `feel free to`

- Kind: phrase. Banned forms: `feel free to`, `please feel free`, `you're welcome to`.
- Why it reads as machine text: `feel free to` grants permission the reader did not need. Chat assistants close almost every answer with `Feel free to ask if you have more questions`, and generated docs use it for every optional step. The phrase hides whether the action is required, optional, or a good idea.
- Where it shows up: chat closers, CONTRIBUTING files, and documentation for optional settings.

```slop
Feel free to ask if you have any other questions.
Feel free to open an issue or submit a pull request.
Feel free to adjust the timeout to suit your needs.
```

Replace with:

- The imperative, when you want the action: "Open an issue."
- A condition, when it depends: "If requests time out on slow networks, raise `timeout` to 30s."
- The process, for contributions: where, what format, who reviews.
- Cut it when it closes a chat answer; the user knows they can reply.

Rewrites:

```slop
Feel free to ask if you have any other questions.
```

After: (Delete the line. End on the answer.)

```slop
Feel free to open an issue or submit a pull request.
```

After: Report bugs as GitHub issues with steps to reproduce. PRs need one approving review and passing CI.

```slop
Feel free to adjust the timeout to suit your needs.
```

After: The default timeout is 10s. Raise it to 30s if you call the API from a mobile network.

- Literal use: none. Say whether the action is required or optional.

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

#### 337. `great question`

- Kind: opener. Banned forms: `great question`, `good question`, `that's a great question`, `excellent question`.
- Why it reads as machine text: `Great question!` is the sycophantic opener tuned into chat assistants by preference training, where raters rewarded warmth. It praises the question before answering it, so every question gets the same grade. In a pull request reply or code comment it reads as a bot talking.
- Where it shows up: the first line of chat answers, support replies, and replies to code review comments.

```slop
Great question! The difference between `==` and `===` is type coercion.
That's a great question, and one that many developers ask.
Good question! Let me explain how the event loop works.
```

Replace with:

- The answer as the first sentence.
- If the question exposes a gap in docs, say so and link the fix: "The docs don't cover this; I added a section."
- In review replies, the answer or the change you made.
- Cut it every time.

Rewrites:

```slop
Great question! The difference between `==` and `===` is type coercion.
```

After: `==` converts types before comparing, so `0 == ""` is true; `===` does not convert, so `0 === ""` is false.

```slop
That's a great question, and one that many developers ask.
```

After: The cache does not invalidate on deploy; you have to call `purge()` in the release script.

```slop
Good question! Let me explain how the event loop works.
```

After: The event loop runs one task, then all queued microtasks, then renders, then picks the next task.

- Literal use: when a question changes the plan, say what it changed: "Your question about time zones found a bug; fix in #412."

#### 338. `as an ai`

- Kind: opener. Banned forms: `as an ai`, `as an AI language model`, `as a large language model`, `I'm just an AI`.
- Why it reads as machine text: `As an AI language model, I cannot` is the refusal and disclaimer template of early chat assistants, and it now marks text as pasted from a chat window. It puts the speaker's nature ahead of the information, and often precedes an answer the model gives anyway. In code comments and docs it is a sign nobody edited the output.
- Where it shows up: chat refusals, generated reviews and essays, and code comments from assistants.

```slop
As an AI language model, I don't have personal opinions, but here are some options.
// As an AI, I cannot run this code, but it should work.
As an AI, I don't have access to real-time data.
```

Replace with:

- The limit, stated as a fact about the task: "I have not run this code."
- What the reader can do to check: the command, the source, the date of the data.
- A recommendation with its reason, when asked for an opinion.
- Cut it when the sentence after it stands on its own.

Rewrites:

```slop
As an AI language model, I don't have personal opinions, but here are some options.
```

After: For a team of 3 with no ops staff, use a managed host such as Render; self-host only if cost is the main concern.

```slop
// As an AI, I cannot run this code, but it should work.
```

After: Not yet run. Check with `pytest tests/test_parse.py` before merging.

```slop
As an AI, I don't have access to real-time data.
```

After: My data ends in June 2026; check the vendor's pricing page for current prices.

- Literal use: when a product must disclose that a bot replies, say so in a label: "Replies on this page are written by a bot and checked by staff within 24 hours."

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

#### 340. `crafted with`

- Kind: phrase. Banned forms: `crafted with`, `crafted with love`, `crafted with care`, `made with love`.
- Why it reads as machine text: `Crafted with care` borrows the language of handwork for software and offers a feeling in place of a fact. Generated footers and landing pages carry it (`Crafted with love in Berlin`), usually next to a heart icon. It says nothing about quality that a reader could test.
- Where it shows up: site footers, About pages, and app store descriptions.

```slop
Crafted with love in San Francisco.
Every detail is crafted with care for the modern developer.
A note-taking app crafted with simplicity in mind.
```

Replace with:

- The plain credit: "Made by a team of 4 in Berlin."
- The specific detail that shows care: test coverage, accessibility audit, support hours.
- The design rule, stated: "No setting has more than 2 options."
- Cut it from footers; the company name and year are enough.

Rewrites:

```slop
Crafted with love in San Francisco.
```

After: Made by Lark Labs, San Francisco, 2026.

```slop
Every detail is crafted with care for the modern developer.
```

After: Every component passes WCAG 2.2 AA and ships with TypeScript types.

```slop
A note-taking app crafted with simplicity in mind.
```

After: A note-taking app with one text field, tags, and search.

- Literal use: for physical goods, name the method: "hand-stitched leather, 8 stitches per inch".

#### 341. `designed with you in mind`

- Kind: phrase. Banned forms: `designed with you in mind`, `built with you in mind`, `with you in mind`.
- Why it reads as machine text: `designed with you in mind` addresses a reader the copy has not identified. Models use it in place of naming the audience or the design decision made for them. Every product says it, so it distinguishes none.
- Where it shows up: product heroes, packaging copy, and onboarding screens.

```slop
Every feature is designed with you in mind.
A banking app built with you in mind.
Our new dashboard was designed with you in mind.
```

Replace with:

- The audience, named, and one decision made for them.
- The user research behind a change: "After 30 interviews with nurses, we moved X."
- The specific change, described.
- Cut it when no audience or decision follows.

Rewrites:

```slop
Every feature is designed with you in mind.
```

After: Built for freelance designers: invoices in your currency, with your logo, sent in 2 clicks.

```slop
A banking app built with you in mind.
```

After: A banking app for people paid in more than one currency.

```slop
Our new dashboard was designed with you in mind.
```

After: The new dashboard puts unpaid invoices first, because 9 of 12 users we interviewed checked them daily.

- Literal use: none.

#### 342. `built for the future`

- Kind: phrase. Banned forms: `built for the future`, `built for tomorrow`, `designed for the future`.
- Why it reads as machine text: `built for the future` promises longevity without a support policy, a version plan, or a date. Models use it in platform and infrastructure copy where buyers worry about lock-in. The claim cannot be checked until it is too late.
- Where it shows up: infrastructure product pages, architecture proposals, and real estate listings.

```slop
Our platform is built for the future.
A database built for tomorrow's workloads.
This architecture is designed for the future of your business.
```

Replace with:

- The support window: "Each major version gets 3 years of security fixes."
- The scaling limit tested: "tested to 10 TB and 50,000 writes per second".
- The exit path: export formats, open standards used.
- Cut it when no policy or test stands behind it.

Rewrites:

```slop
Our platform is built for the future.
```

After: Each major version gets 3 years of security fixes, and data exports as standard SQL dumps.

```slop
A database built for tomorrow's workloads.
```

After: A database tested to 10 TB and 50,000 writes per second on one node.

```slop
This architecture is designed for the future of your business.
```

After: This design supports 10 times today's order volume before the queue needs a second partition.

- Literal use: none. State the time span.

#### 343. `the future of`

- Kind: phrase. Banned forms: `the future of`, `the future of work`, `the future is here`, `the future is now`.
- Why it reads as machine text: `The future of X` names a product category as a destiny instead of describing the product. Models write it as a headline (`The future of payments`) because it claims importance without a fact. Readers have seen it on every launch since the 1990s.
- Where it shows up: headlines, keynote titles, and investor decks.

```slop
Welcome to the future of payments.
This is the future of work.
The future of web development is here.
```

Replace with:

- What the product does, as the headline: "Pay suppliers in 40 currencies from one account."
- The specific change in how people work, measured.
- The specific release and what it adds.
- Cut it when you cannot name the change.

Rewrites:

```slop
Welcome to the future of payments.
```

After: Pay suppliers in 40 currencies from one account, settled the same day.

```slop
This is the future of work.
```

After: Our 60 staff work from 14 countries and meet in person twice a year.

```slop
The future of web development is here.
```

After: Version 5 renders pages on the server and streams them to the browser in chunks.

- Literal use: for an actual forecast, title it with the date and the subject: "Energy prices, 2027 to 2030: our forecast".

#### 344. `with ease`

- Kind: phrase. Banned forms: `with ease`, `easily`, `effortlessly`.
- Why it reads as machine text: `with ease` claims that a task is simple without counting the steps. Models append it to any feature verb (`manage your projects with ease`). The reader who struggles then blames themselves, and the support load rises.
- Where it shows up: feature lists, onboarding copy, and tutorial intros.

```slop
Manage your invoices with ease.
Deploy your app with ease using our CLI.
Easily import your data from any source.
```

Replace with:

- The step count or the time: "Deploy in one command."
- The specific sources, listed, for import claims.
- The verb alone, with the feature name.
- Cut it when there is no number for the ease.

Rewrites:

```slop
Manage your invoices with ease.
```

After: Create, send, and track invoices from one list.

```slop
Deploy your app with ease using our CLI.
```

After: Deploy with one command: `ship deploy`.

```slop
Easily import your data from any source.
```

After: Import from CSV, Excel, Airtable, or a Postgres connection string.

- Literal use: none. Give the step count.

#### 345. `made simple`

- Kind: phrase. Banned forms: `made simple`, `made easy`, `simplified`.
- Why it reads as machine text: `X made simple` is a headline fragment that names a category and claims to fix its difficulty in two words. Models produce it for product taglines (`Invoicing made simple`) because it fits any noun. Dozens of products share each version.
- Where it shows up: taglines, book titles, and course names.

```slop
Invoicing made simple.
Kubernetes made easy for developers.
Accounting, simplified.
```

Replace with:

- A verb headline that names what the user does: "Send an invoice in 30 seconds."
- The scope of the simplification: what was removed or automated.
- The audience and the outcome.
- Cut it when the noun is the whole tagline; write a sentence.

Rewrites:

```slop
Invoicing made simple.
```

After: Send an invoice in 30 seconds; we chase late payers for you.

```slop
Kubernetes made easy for developers.
```

After: Deploy to Kubernetes from a `Procfile`; we write the manifests.

```slop
Accounting, simplified.
```

After: Bookkeeping for freelancers: connect your bank and we sort transactions into tax categories.

- Literal use: for a math or code operation, name it: "the reduced fraction", "the refactored function".

#### 346. `take your`

- Kind: phrase. Banned forms: `take your`, `take your X to the next level`, `take your business further`.
- Why it reads as machine text: `Take your X to Y` frames the product as a vehicle and the reader's work as cargo going somewhere better. Models use it as a call to action in every industry (`Take your workflow to new heights`). The destination is never a place the reader can check.
- Where it shows up: call-to-action buttons, hero subheads, and course ads.

```slop
Take your workflow to new heights.
Take your career further with our certification.
Take your photos from good to great.
```

Replace with:

- The result, measured: "Close tickets in half the time."
- What the certificate qualifies the reader to do, and its cost.
- The specific edit the tool makes.
- Cut it when there is no destination you can name.

Rewrites:

```slop
Take your workflow to new heights.
```

After: Replace your morning status meeting with a 5-line written update.

```slop
Take your career further with our certification.
```

After: The certificate prepares you for the AWS architect associate exam; it costs 300 pounds and takes 8 weeks.

```slop
Take your photos from good to great.
```

After: Fix exposure, straighten horizons, and remove dust spots in one pass.

- Literal use: for an instruction about carrying an object, use another verb: "Bring your passport to the desk", "There is no time limit."

#### 347. `in the world of`

- Kind: opener. Banned forms: `in the world of`, `in the realm of`, `in the space of`.
- Why it reads as machine text: `In the world of X,` opens a sentence by naming a field as if it were a separate place, so the writer can state a generality about it. Models use it to begin articles and sections (`In the world of web development, speed matters`). The field is the topic of the whole page, so naming it again adds nothing.
- Where it shows up: blog openers, section intros, and LinkedIn posts.

```slop
In the world of web development, performance is everything.
In the world of startups, speed matters.
In the world of finance, trust is key.
```

Replace with:

- The claim, scoped by a subject: "On e-commerce sites, each extra second of load time lowers conversion."
- The specific evidence for the generality.
- Nothing, if the field is the topic of the page.
- Cut it when the sentence after it is a platitude; cut the platitude too.

Rewrites:

```slop
In the world of web development, performance is everything.
```

After: On our store, conversion fell 7% for every extra second of load time.

```slop
In the world of startups, speed matters.
```

After: We had 9 months of runway, so we cut the launch scope to 3 features.

```slop
In the world of finance, trust is key.
```

After: Customers can see every fee before they confirm a transfer.

- Literal use: for geography, name the place: "in 40 countries".

#### 348. `when it comes to`

- Kind: phrase. Banned forms: `when it comes to`, `when it comes down to`, `in terms of`.
- Why it reads as machine text: `When it comes to X,` fronts the topic before the sentence starts, and the main clause then has a weak subject ("it", "there"). Models use the shape to change topics between paragraphs without a real transition. It adds four words and moves the subject to the wrong place.
- Where it shows up: comparison articles, advice posts, and chat answers.

```slop
When it comes to performance, Go is hard to beat.
When it comes to styling, there are many options.
When it comes to testing, it's best to start small.
```

Replace with:

- The topic as the subject of the sentence: "Go compiles to one binary and starts in 10ms."
- The options, listed, for "many options" lines.
- The instruction, directly: "Write one test for the checkout total first."
- Cut it when the topic is already the subject of the paragraph.

Rewrites:

```slop
When it comes to performance, Go is hard to beat.
```

After: Our Go service handles 4 times the requests of the Python one on the same hardware.

```slop
When it comes to styling, there are many options.
```

After: Style React with CSS modules, Tailwind, or a CSS-in-JS library; we use CSS modules.

```slop
When it comes to testing, it's best to start small.
```

After: Start with one test for the checkout total, the function that loses money when it breaks.

- Literal use: for an event that may happen, write "if" or "when" with a plain verb: "When the order arrives, scan the code."

#### 349. `the art of`

- Kind: phrase. Banned forms: `the art of`, `master the art of`, `the fine art of`.
- Why it reads as machine text: `the art of X` dresses a skill as a craft tradition so a guide can promise mastery. Models produce it for titles (`Mastering the art of prompt engineering`), applying it to tasks with a checklist. The phrase implies talent where the content teaches steps.
- Where it shows up: course titles, blog headlines, and book subtitles.

```slop
Master the art of writing clean code.
The art of the perfect pull request.
Learn the fine art of giving feedback.
```

Replace with:

- The skill as a task, with its scope: "How to split a 1,000-line PR into 4."
- The specific steps the guide teaches, named.
- The outcome the reader will have afterward.
- Cut it when the guide is a checklist; title it as one.

Rewrites:

```slop
Master the art of writing clean code.
```

After: Name functions after what they return, keep them under 40 lines, and test each one.

```slop
The art of the perfect pull request.
```

After: How to write a pull request: under 400 lines, one change, and a description with a test plan.

```slop
Learn the fine art of giving feedback.
```

After: Give feedback in three parts: what you saw, its effect, and what to change.

- Literal use: for actual art, name the artist or period: "Bauhaus posters", "work by Anni Albers".

#### 350. `the heart of`

- Kind: phrase. Banned forms: `the heart of`, `at the heart of`, `heart and soul`.
- Why it reads as machine text: `at the heart of` claims centrality for a value or component without showing it. Models write `At the heart of our platform is a commitment to X`, where X is a value every company lists. For components, the phrase replaces a diagram or a dependency count.
- Where it shows up: About pages, architecture overviews, and travel copy (`in the heart of the city`).

```slop
At the heart of our platform is a commitment to privacy.
The scheduler lies at the heart of the system.
Our hotel is located in the heart of Lisbon.
```

Replace with:

- The policy or mechanism that shows the value: "We store no message content; it is encrypted on your device."
- The dependency fact: "Every job passes through the scheduler; if it stops, nothing runs."
- The location with a distance: "200m from Rossio station."
- Cut it when the value is not backed by a policy.

Rewrites:

```slop
At the heart of our platform is a commitment to privacy.
```

After: Messages are encrypted on your device; our servers never see the content.

```slop
The scheduler lies at the heart of the system.
```

After: Every job passes through the scheduler; if it stops, no job runs.

```slop
Our hotel is located in the heart of Lisbon.
```

After: The hotel is in Baixa, 200m from Rossio station.

- Literal use: for an actual heart, drop the "of" construction: write "a patient's heart" or "the heart" and name the part, "the left ventricle".
