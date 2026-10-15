### 7.1 Entries 001 to 070: verbs

Entries 001 to 070 cover verbs and verb phrases. Each entry gives the forms the linter catches, where the word turns up, what to write instead, and three rewrites.

#### 001. `delve`

- Kind: verb. Banned forms: `delve`, `delves`, `delved`, `delving`.
- Why it reads as machine text: `delves` had one of the largest jumps of any word in PubMed abstracts after 2022, and the excess lines up with the release of chat models (Kobak et al., 2024). Before that it lived in Victorian prose and fantasy novels. It promises depth without naming what was examined, so the sentence after it usually summarizes the surface. If the post cannot name the file, function, or dataset that was examined, nothing was.
- Where it shows up: blog intros, README overviews, the first line of a PR description.

```slop
In this post, we delve into the internals of the React reconciler.
This PR delves into the flaky auth tests and fixes them.
Let's delve deeper into how caching works in our API.
```

Replace with:

- `look at` or `read` when someone examined code or documents.
- `test` / `measure` / `profile` when there was an experiment; name it.
- `compare` when two things were set side by side; give both results.
- Cut it when the sentence works with the verb removed: start with the finding.

Rewrites:

```slop
In this post, we delve into the internals of the React reconciler.
```

After: This post walks through how the React reconciler decides which components to render again.

```slop
This PR delves into the flaky auth tests and fixes them.
```

After: Fix two flaky auth tests; both waited on a 500ms timeout that CI sometimes exceeded.

```slop
Let's delve deeper into how caching works in our API.
```

After: The API caches `GET /users/:id` for 60 seconds in Redis, keyed by user ID.

- Literal use: for digging in soil or archives, write "dig" or "search". No exceptions in prose.

#### 002. `leverage`

- Kind: verb (also noun). Banned forms: `leverage`, `leverages`, `leveraged`, `leveraging`.
- Why it reads as machine text: It came from finance (borrowing to multiply returns) through management consulting, and in generated text it means "use" in a suit. Models reach for it whenever a sentence pairs a tool with a goal, so `leverage Redis` and `leverage our expertise` appear at the same rate. It hides whether anything was multiplied; usually the tool was just called. Swap in "use"; if the sentence loses nothing, keep "use".
- Where it shows up: architecture docs, product pages, résumés and cover letters.

```slop
We leverage Postgres full-text search to power product discovery.
This library leverages WebAssembly for fast image processing.
Leverage our analytics to make smarter decisions.
```

Replace with:

- `use` in almost every case.
- `build on`, `reuse`, `call` when you want to say which part does the work.
- Cut it when the tool name already carries the sentence.

Rewrites:

```slop
We leverage Postgres full-text search to power product discovery.
```

After: Product search runs on Postgres full-text search (`tsvector` with a GIN index), so there is no separate search server.

```slop
This library leverages WebAssembly for fast image processing.
```

After: The library decodes and resizes images in WebAssembly, so it runs in the browser with no server round trip.

```slop
Leverage our analytics to make smarter decisions.
```

After: The analytics page shows which campaigns brought in paying customers last month.

- Literal use: in finance, write "debt" or "borrowing" and give the ratio (debt to equity of 2 to 1); for mechanics, write "lever".

#### 003. `utilize`

- Kind: verb. Banned forms: `utilize`, `utilizes`, `utilized`, `utilizing`, `utilization`, and the `-ise` spellings.
- Why it reads as machine text: Three syllables where "use" has one. The US federal plain-language guidelines list it with "use" as the replacement, and model output still produces it because report and grant text is full of it. It adds formality and nothing else; no sentence changes meaning when "use" replaces it. Some editors defend a narrow sense (use for an unintended purpose), but generated text never means that.
- Where it shows up: design docs, API reference prose, academic and government writing.

```slop
The service utilizes a message queue to decouple producers and consumers.
Users can utilize the settings panel to configure notifications.
This function utilizes recursion to traverse the tree.
```

Replace with:

- `use` everywhere.
- Name the action when "use" is still vague: "reads from", "writes to", "calls".
- Cut it when the tool can be the subject of the sentence.

Rewrites:

```slop
The service utilizes a message queue to decouple producers and consumers.
```

After: Producers write to a RabbitMQ queue and consumers read from it, so either side can restart without losing jobs.

```slop
Users can utilize the settings panel to configure notifications.
```

After: Turn notifications on or off in Settings > Notifications.

```slop
This function utilizes recursion to traverse the tree.
```

After: This function walks the tree recursively.

- Literal use: for the metric, write "CPU usage" or "load", or quote the field name in inline code (`cpu_utilization`).

#### 004. `harness`

- Kind: verb (noun in the literal sense). Banned forms: `harness`, `harnesses`, `harnessed`, `harnessing`.
- Why it reads as machine text: `harness the power of` is a stock opener of generated marketing. The verb carries a picture of taming a wild force, which inflates whatever follows: a REST API, a spreadsheet. Models use it for "use" when the object is abstract (data, AI, community); nobody writes it about a cron job. The phrase also assumes the reader already agrees the thing is strong, which the page has not shown.
- Where it shows up: landing page hero copy, pitch decks, About pages, talk abstracts.

```slop
Harness the power of AI to write better emails.
Our platform harnesses real-time data to drive growth.
Developers can harness GPU acceleration with a single flag.
```

Replace with:

- `use` for the plain act.
- Say what the thing does: "drafts", "flags", "runs on".
- `run on` when the hardware or service is the point: "runs on a single A100".
- Cut it and lead with the result.

Rewrites:

```slop
Harness the power of AI to write better emails.
```

After: Draft a reply from the thread history, then edit it before you send.

```slop
Our platform harnesses real-time data to drive growth.
```

After: The dashboard updates every 5 seconds from the order stream.

```slop
Developers can harness GPU acceleration with a single flag.
```

After: Add `--gpu` to run the model on a CUDA device.

- Literal use: for test infrastructure, write "test runner" or "test setup", or put `harness` in inline code when it is a project name; for straps on animals or climbers, use inline code too.

#### 005. `unlock`

- Kind: verb. Banned forms: `unlock`, `unlocks`, `unlocked`, `unlocking`.
- Why it reads as machine text: It frames every feature as a gate the product opens, a frame taken from game design and freemium upsells (`unlock Pro`). Models apply it to abstract nouns with no lock: potential, value, growth. The sentence then never says what the user can do that they could not do before. Describing a paywall as a lock also makes the free plan sound like a cage.
- Where it shows up: pricing pages, onboarding screens, release notes, LinkedIn posts.

```slop
Unlock the full potential of your data.
Upgrade to Pro to unlock advanced features.
This release unlocks new possibilities for plugin authors.
```

Replace with:

- `lets you` or `you can now`, followed by the action.
- `includes` for plan comparisons: say what the plan includes.
- Cut it when the result can be named directly.

Rewrites:

```slop
Unlock the full potential of your data.
```

After: Filter, group, and export any table as CSV.

```slop
Upgrade to Pro to unlock advanced features.
```

After: Pro adds SSO, audit logs, and one year of history.

```slop
This release unlocks new possibilities for plugin authors.
```

After: Plugins can now register their own commands and read the open file.

- Literal use: for locks on a mutex, file, or phone, write "release the lock" or "open", and put the call in inline code (`mutex.unlock()`).

#### 006. `unleash`

- Kind: verb. Banned forms: `unleash`, `unleashes`, `unleashed`, `unleashing`.
- Why it reads as machine text: A dog-leash image that turns any feature into a released force: `unleash creativity`, `unleash the full potential`. Copywriters overused it through the 2000s, and models learned it from that copy, so it now dates text to hype templates. Nothing was held back, and the reader knows it. Pages that use it tend to stack it with `the full potential`, which doubles the empty promise.
- Where it shows up: launch posts, game and hardware marketing, hackathon announcements.

```slop
Unleash your creativity with 200 new templates.
Version 3 unleashes the full power of multi-core CPUs.
Unleash your team's potential with smarter workflows.
```

Replace with:

- Name the capability and the count: "200 templates for invoices and posters".
- `runs on`, `uses all` for performance claims, with a measurement.
- Cut it; the noun phrase after it is usually the real content.

Rewrites:

```slop
Unleash your creativity with 200 new templates.
```

After: 200 new templates for invoices, posters, and slide decks.

```slop
Version 3 unleashes the full power of multi-core CPUs.
```

After: Version 3 compresses on all cores; on 8 cores a 1 GB file takes 4 seconds instead of 22.

```slop
Unleash your team's potential with smarter workflows.
```

After: Assign tasks from a comment and see on the board who is blocked.

- Literal use: for animals, write "let off the lead" or "released".

#### 007. `elevate`

- Kind: verb. Banned forms: `elevate`, `elevates`, `elevated`, `elevating`.
- Why it reads as machine text: Fashion and hospitality copy shifted it from "lift" to "make fancier" (`elevate your style`), and models adopted it as the default verb for improvement. It implies a vertical scale of quality with no measurement on it. `Elevate your workflow` names no step that changed. In design reviews it often means "add more padding and a larger font", so say which.
- Where it shows up: SaaS hero sections, design portfolio intros, restaurant and hotel copy, Dribbble descriptions.

```slop
Elevate your workflow with AI-assisted code review.
These small details elevate the user experience.
Elevate your brand with a custom design system.
```

Replace with:

- `improve`, plus what changed and by how much.
- `raise` for a number: raise the timeout, raise the contrast ratio.
- Cut it and describe the detail itself.

Rewrites:

```slop
Elevate your workflow with AI-assisted code review.
```

After: Each PR gets review comments on likely bugs within 2 minutes of opening.

```slop
These small details elevate the user experience.
```

After: Buttons show a pressed state within 50ms, and focus returns to the trigger when a dialog closes.

```slop
Elevate your brand with a custom design system.
```

After: A component library in your colors and type, with Figma and React versions.

- Literal use: for privileges, write "run as admin" or "root access"; for height, write "raised" and give the number.

#### 008. `empower`

- Kind: verb. Banned forms: `empower`, `empowers`, `empowered`, `empowering`, `empowerment`.
- Why it reads as machine text: It moved from social work and HR into the mission statement of every B2B tool. Models attach it to "teams", "developers", and "creators" because the pattern `X empowers Y to Z` fits any product. It claims a transfer of power when the product adds a feature, and the "to Z" clause is the only part worth keeping. Users notice the gap between the verb and the feature and trust the page less.
- Where it shows up: mission statements, About pages, job ads, product taglines.

```slop
We empower developers to ship faster.
Our tools empower teams to collaborate seamlessly.
Empowering creators to build the future of content.
```

Replace with:

- `lets` or `helps`, followed by the specific action.
- Name the mechanism: "with preview deploys", "with shared drafts".
- Cut everything before "to" and keep the verb phrase.

Rewrites:

```slop
We empower developers to ship faster.
```

After: Every branch gets a preview URL, so reviewers can click through a change before merge.

```slop
Our tools empower teams to collaborate seamlessly.
```

After: Two people can edit the same doc and see each other's cursors.

```slop
Empowering creators to build the future of content.
```

After: Sell videos and courses from your own page; we take 5% per sale.

- Literal use: for legal authority, write "authorize" or "give the right to".

#### 009. `streamline`

- Kind: verb. Banned forms: `streamline`, `streamlines`, `streamlined`, `streamlining`.
- Why it reads as machine text: It came from aerodynamic design through 1990s process consulting and now means "made better, somehow". Models pick it for any change to a process: fewer steps, faster steps, or no change at all. It hides the step count before and after, which is the one number the reader wants. Paired with `workflow` or `process`, it fills a hero line with no product in it.
- Where it shows up: release notes, PR titles, B2B landing pages, refactor commit messages.

```slop
Streamline your hiring process with automated scheduling.
Refactor: streamline the auth module.
Our streamlined onboarding gets you started in minutes.
```

Replace with:

- `cut`, `remove`, `merge`, with the count of steps.
- `simplify` only next to what got removed.
- In commits, name the change: "remove", "inline", "merge".
- `automate`, with the step that no longer needs a person.

Rewrites:

```slop
Streamline your hiring process with automated scheduling.
```

After: Candidates pick an interview slot from your calendar, with no email back and forth.

```slop
Refactor: streamline the auth module.
```

After: refactor(auth): merge `login.ts` and `session.ts` into `auth.ts`, remove the unused token cache.

```slop
Our streamlined onboarding gets you started in minutes.
```

After: Sign up, connect GitHub, deploy: three screens, about 2 minutes.

- Literal use: for fluid flow, write "low-drag" and give the drag coefficient.

#### 010. `revolutionize`

- Kind: verb. Banned forms: `revolutionize`, `revolutionizes`, `revolutionized`, `revolutionizing`, and the `-ise` spellings.
- Why it reads as machine text: It claims a whole field will work differently once the product exists. Models produce it for small tools (a note app, a linter) because press releases trained the pattern `X revolutionizes Y`. Readers discount the whole page once they see it, since nobody can check the claim. Investors and reviewers read it as a sign the writer could not find a specific advantage.
- Where it shows up: startup press releases, pitch decks, Product Hunt taglines, cover letters.

```slop
We're revolutionizing the way teams manage projects.
This framework will revolutionize frontend development.
A revolutionary approach that revolutionizes data entry.
```

Replace with:

- Say what is different, compared with what the reader uses now.
- `replaces` when it does replace a step or a tool.
- Cut it; a plain description of the change carries more weight.

Rewrites:

```slop
We're revolutionizing the way teams manage projects.
```

After: Projects live in your Git repo as Markdown files, so tasks are versioned with the code.

```slop
This framework will revolutionize frontend development.
```

After: Components compile to plain DOM calls, with no virtual DOM and a 3 KB runtime.

```slop
A revolutionary approach that revolutionizes data entry.
```

After: Scan a receipt and the amount, date, and vendor fill in; you check them and save.

- Literal use: for political history, write "overthrow" or name the event.

#### 011. `supercharge`

- Kind: verb. Banned forms: `supercharge`, `supercharges`, `supercharged`, `supercharging`.
- Why it reads as machine text: It comes from engines (a compressor forcing extra air in) and became the verb for "faster" in productivity and AI marketing. Models attach it to workflows and growth, never to a measured speed. When a real speedup exists, a number says more. A slogan that needs this verb usually has no benchmark behind it.
- Where it shows up: browser extension listings, newsletter subject lines, AI tool landing pages.

```slop
Supercharge your productivity with keyboard shortcuts.
This plugin supercharges your terminal.
Supercharged search, now with AI.
```

Replace with:

- `speeds up`, with the measured gain.
- Name the feature: "adds fuzzy search", "adds tabs".
- Cut it and lead with the feature.

Rewrites:

```slop
Supercharge your productivity with keyboard shortcuts.
```

After: Every action has a shortcut; press `?` to see the list.

```slop
This plugin supercharges your terminal.
```

After: Adds tab completion for git branches and recent directories.

```slop
Supercharged search, now with AI.
```

After: Search now matches typos and synonyms, so "recieve" finds "receive".

- Literal use: for engines, write "forced induction" or put `supercharger` in inline code.

#### 012. `embark`

- Kind: verb. Banned forms: `embark`, `embarks`, `embarked`, `embarking`.
- Why it reads as machine text: A travel verb that makes a tutorial or a job change sound like a voyage. Models open with it (`embark on a journey`) to signal weight and drama. It delays the content by a clause and says nothing about the destination. Paired with `journey`, also banned, it is one of the clearest openers of generated tutorials.
- Where it shows up: tutorial intros, course descriptions, onboarding emails, personal blog posts.

```slop
Embark on your journey to mastering TypeScript.
Before we embark on the migration, let's review the plan.
She embarked on a new chapter as a product designer.
```

Replace with:

- `start`, `begin`.
- Name the first step instead of the trip.
- Cut it: "Before migrating" works on its own.

Rewrites:

```slop
Embark on your journey to mastering TypeScript.
```

After: This course covers TypeScript generics, narrowing, and declaration files in 12 lessons.

```slop
Before we embark on the migration, let's review the plan.
```

After: Before migrating, check that every table has a primary key.

```slop
She embarked on a new chapter as a product designer.
```

After: She moved from support to product design in 2023.

- Literal use: for ships and planes, write "board".

#### 013. `navigate`

- Kind: verb. Banned forms: `navigate`, `navigates`, `navigated`, `navigating`.
- Why it reads as machine text: Models use it for every difficulty (`navigate the complexities of`, `navigate challenges`). The image treats a problem as terrain and the writer as guide, which sounds wise and commits to nothing. In UI text it pushes out the plain verbs "go to" and "open". Chat models use it constantly in advice answers, so readers recognize the source at once.
- Where it shows up: advice posts, docs intros, UI instructions, career and HR writing.

```slop
Navigate the complexities of modern state management.
Navigate to Settings and click Billing.
We help founders navigate fundraising.
```

Replace with:

- `go to`, `open` in UI instructions.
- `handle`, `deal with`, `get through` for problems, or name the problem.
- `find` when the reader is looking for something in a list or a menu.
- Cut it and give the step.

Rewrites:

```slop
Navigate the complexities of modern state management.
```

After: When to keep state in a component, in a URL parameter, or in a store.

```slop
Navigate to Settings and click Billing.
```

After: Open Settings > Billing.

```slop
We help founders navigate fundraising.
```

After: We review your deck and introduce you to five investors who fund your stage.

- Literal use: for router APIs, put the call in inline code (`router.navigate('/home')`); in prose, write "go to" or "move to".

#### 014. `foster`

- Kind: verb. Banned forms: `foster`, `fosters`, `fostered`, `fostering`.
- Why it reads as machine text: Codes of conduct and values pages made `foster a culture of` a fixed phrase, and models repeat it for trust, inclusion, and teamwork. It names a hoped-for mood and no action that produces it. The reader cannot tell what the project does differently. A real code of conduct lists behaviors and consequences and needs no such verb.
- Where it shows up: codes of conduct, CONTRIBUTING files, company values, grant proposals.

```slop
We aim to foster a welcoming and inclusive community.
Pair programming fosters knowledge sharing.
This initiative fosters a culture of innovation.
```

Replace with:

- Name the rule or the practice: "we reply to every first PR within 3 days".
- `helps`, `leads to`, with the effect.
- Cut it when the practice can stand alone.

Rewrites:

```slop
We aim to foster a welcoming and inclusive community.
```

After: Maintainers reply to first-time contributors within 3 days and label 20 issues `good first issue` each release.

```slop
Pair programming fosters knowledge sharing.
```

After: When two people write the code, two people can fix it at 2 a.m.

```slop
This initiative fosters a culture of innovation.
```

After: Each engineer gets one day a month for any project and demos it on Friday.

- Literal use: for child or pet care, put the term in inline code (`foster parent`) or write "temporary carer".

#### 015. `cultivate`

- Kind: verb. Banned forms: `cultivate`, `cultivates`, `cultivated`, `cultivating`.
- Why it reads as machine text: The gardening image suggests patient growth, so models use it for relationships, mindsets, and audiences. It turns a list of tasks into a virtue. The reader learns what the writer values and not what they did. It also casts the writer as the gardener and the users as the crop, which reads as condescending.
- Where it shows up: leadership posts, résumé bullets, community manager job ads, newsletter advice.

```slop
Cultivate meaningful relationships with your users.
I cultivated a high-performing team of 12 engineers.
Cultivate a growth mindset to accelerate your career.
```

Replace with:

- `build` or `grow`, only next to the method.
- In résumés, `hired`, `trained`, `kept`, with counts.
- Cut it and state the habit.

Rewrites:

```slop
Cultivate meaningful relationships with your users.
```

After: Call five customers a month and read every support ticket tagged "bug".

```slop
I cultivated a high-performing team of 12 engineers.
```

After: I hired 7 of the 12 engineers on the team; two years later, 11 were still there.

```slop
Cultivate a growth mindset to accelerate your career.
```

After: Ask for written feedback after each project and pick one thing to change.

- Literal use: for farming, write "grow" or "farm".

#### 016. `underscore`

- Kind: verb. Banned forms: `underscore`, `underscores`, `underscored`, `underscoring`.
- Why it reads as machine text: `underscores` sits next to `delves` and `showcasing` on the list of words whose frequency jumped in 2024 scientific abstracts. Models use it to attach weight to a point they just made (`This underscores the importance of testing`), which repeats the point and adds a vague moral. The sentence it starts can almost always go. Writers who state a finding plainly never need a second sentence that points at it.
- Where it shows up: report conclusions, postmortems, research summaries, AI-written PR reviews.

```slop
This incident underscores the importance of monitoring.
The results underscore the need for further research.
Her talk underscored how vital accessibility is.
```

Replace with:

- `shows`, followed by what it shows.
- State the action item instead of the moral.
- `confirms`, only when an earlier claim was tested and held.
- Cut the sentence when it repeats the one before.

Rewrites:

```slop
This incident underscores the importance of monitoring.
```

After: Disk usage sat at 100% for 40 minutes before anyone noticed; add an alert at 85%.

```slop
The results underscore the need for further research.
```

After: The study had 40 patients; a larger trial is needed before clinical use.

```slop
Her talk underscored how vital accessibility is.
```

After: Her talk showed that 3 of our 5 checkout forms failed with a screen reader.

- Literal use: for the character, show it in inline code (`_`, as in `snake_case`).

#### 017. `showcase`

- Kind: verb and noun. Banned forms: `showcase`, `showcases`, `showcased`, `showcasing`.
- Why it reads as machine text: `showcasing` was among the words with the largest excess frequency in 2024 scientific abstracts. In generated prose it turns any example into an exhibit (`this project showcases my skills`), which says the work exists and nothing about what it does. Recruiters skim past it because every bootcamp portfolio uses the same line.
- Where it shows up: portfolio pages, GitHub profile READMEs, demo apps, case studies.

```slop
This project showcases my skills in React and Node.
The demo showcases the power of our API.
A showcase of beautiful, responsive layouts.
```

Replace with:

- `shows` or `demonstrates`, with what exactly.
- Describe the project: what it does, who used it, one number.
- For the noun, `gallery`, `examples`, `demo`.

Rewrites:

```slop
This project showcases my skills in React and Node.
```

After: A budgeting app in React and Node; 300 people used it during my bootcamp.

```slop
The demo showcases the power of our API.
```

After: The demo builds a shipping label from an address in one API call.

```slop
A showcase of beautiful, responsive layouts.
```

After: 14 layouts, each tested at 320px, 768px, and 1280px wide.

- Literal use: for a glass cabinet in a shop or museum, write "display case".

#### 018. `spearhead`

- Kind: verb. Banned forms: `spearhead`, `spearheads`, `spearheaded`, `spearheading`.
- Why it reads as machine text: A military image that résumé guides pushed for years as a "strong action verb", so models trained on those guides apply it to anything a person took part in. It inflates the role without stating scope: team size, budget, outcome. Hiring managers ask what exactly you did after reading it, which the bullet should have said.
- Where it shows up: résumés, LinkedIn profiles, performance reviews, hiring press releases.

```slop
Spearheaded the migration to Kubernetes.
She spearheads our sustainability initiatives.
Spearheading cross-functional efforts to improve retention.
```

Replace with:

- `led`, `ran`, `started`, with scope.
- Name your part: "wrote the plan", "did the cutover".
- Add the result and its number.

Rewrites:

```slop
Spearheaded the migration to Kubernetes.
```

After: Led the move of 40 services to Kubernetes over 6 months with 3 engineers and no customer-facing downtime.

```slop
She spearheads our sustainability initiatives.
```

After: She runs the program that cut office energy use by 18% in 2024.

```slop
Spearheading cross-functional efforts to improve retention.
```

After: Worked with support and sales on an exit survey; monthly churn fell from 4% to 3%.

- Literal use: for weapons or military history, write "spear tip" or "lead unit".

#### 019. `bolster`

- Kind: verb. Banned forms: `bolster`, `bolsters`, `bolstered`, `bolstering`.
- Why it reads as machine text: Financial news (`bolstered by strong earnings`) and policy writing use it, and models carry it into technical text to mean "make stronger" without saying how. `Bolster security` could mean a password rule or a full rewrite. It also hints that the thing was weak before, a claim the writer rarely means to make.
- Where it shows up: security notes, release notes, investor updates, grant applications.

```slop
This release bolsters security across the platform.
New hires will bolster our engineering team.
Strong Q3 results bolstered investor confidence.
```

Replace with:

- `add` or `strengthen`, with the specific change.
- `increase`, with a number.
- Cut it and list the changes.

Rewrites:

```slop
This release bolsters security across the platform.
```

After: Passwords now need 12 characters, sessions expire after 8 idle hours, and admin actions require 2FA.

```slop
New hires will bolster our engineering team.
```

After: Three engineers join in March, two on billing and one on the mobile app.

```slop
Strong Q3 results bolstered investor confidence.
```

After: Revenue rose 22% in Q3, and the share price went up 9% the next day.

- Literal use: for the long cushion, write "cushion" or "long pillow".

#### 020. `amplify`

- Kind: verb. Banned forms: `amplify`, `amplifies`, `amplified`, `amplifying`, `amplifier`.
- Why it reads as machine text: Advocacy and social media writing use it for "share more widely", and models stretch it to impact, reach, and results. It suggests a multiplier with no factor attached. In technical text it collides with the audio sense. Engineers who read it about software look for a gain figure that never comes.
- Where it shows up: marketing plans, DevRel posts, social media strategy docs, mission statements.

```slop
Amplify your reach with scheduled posts.
Caching amplifies the performance of your app.
We amplify the voices of open source maintainers.
```

Replace with:

- `increase` or `reach more people`, with a number.
- Name the effect with its unit: "cuts p95 latency from 900ms to 120ms".
- `share`, `repost`, `pay`, for what an organization actually does.
- `repeat` or `retweet`, when that is the actual action.

Rewrites:

```slop
Amplify your reach with scheduled posts.
```

After: Schedule posts for the hours your followers are online, based on the last 30 days.

```slop
Caching amplifies the performance of your app.
```

After: Caching the product list cut median page load from 900ms to 120ms.

```slop
We amplify the voices of open source maintainers.
```

After: We publish a monthly interview with a maintainer and pay each one $500.

- Literal use: for audio and signals, write "gain" or "make louder" and give the dB; put `amplifier` in inline code.

#### 021. `catalyze`

- Kind: verb. Banned forms: `catalyze`, `catalyzes`, `catalyzed`, `catalyzing`, `catalyse`.
- Why it reads as machine text: A chemistry term (speed up a reaction without being used up) that foundation reports and accelerator blogs took to mean "cause" or "start". Models pair it with change, growth, and partnerships to make a modest event sound decisive. It names no mechanism, the opposite of its chemical meaning. It lets a funder take credit for outcomes without showing the chain from money to result.
- Where it shows up: impact reports, accelerator descriptions, conference blurbs, grant proposals.

```slop
This grant will catalyze innovation in rural healthcare.
The hackathon catalyzed new partnerships across teams.
Our API catalyzes growth for small businesses.
```

Replace with:

- `start`, `cause`, `lead to`, with the result.
- `fund` or `pay for` when money is the mechanism.
- Cut it and give the sequence of events.

Rewrites:

```slop
This grant will catalyze innovation in rural healthcare.
```

After: The grant pays for telehealth carts in 12 rural clinics for two years.

```slop
The hackathon catalyzed new partnerships across teams.
```

After: Two hackathon projects, the CSV importer and the status page, are now owned by the platform team.

```slop
Our API catalyzes growth for small businesses.
```

After: Shops take card payments on any phone, with no terminal to buy.

- Literal use: in chemistry, write "speeds up the reaction" and name the compound that does it.

#### 022. `illuminate`

- Kind: verb. Banned forms: `illuminate`, `illuminates`, `illuminated`, `illuminating`.
- Why it reads as machine text: The light image flatters the writer: the text does not explain, it sheds light. Models use it in summaries (`This study illuminates...`) and in praise (`an illuminating talk`). It promises understanding and skips the finding. Chat models open summaries with it often enough that teachers grading essays now flag it.
- Where it shows up: book and paper summaries, talk descriptions, docs intros, review comments.

```slop
This guide illuminates the inner workings of the JavaScript event loop.
The postmortem illuminated several gaps in our process.
An illuminating conversation about the state of design.
```

Replace with:

- `explains` or `shows`, with the claim.
- `found`, for investigations, followed by the findings.
- Cut it and state the point that was learned.

Rewrites:

```slop
This guide illuminates the inner workings of the JavaScript event loop.
```

After: This guide explains why `setTimeout(fn, 0)` runs after pending promise callbacks.

```slop
The postmortem illuminated several gaps in our process.
```

After: The postmortem found that nobody owned certificate renewal and the expiry alert went to a disabled inbox.

```slop
An illuminating conversation about the state of design.
```

After: Two design leads on why their teams stopped shipping style guides as PDFs.

- Literal use: for lighting, write "light" or "lit" and give the lux when it matters.

#### 023. `resonate`

- Kind: verb. Banned forms: `resonate`, `resonates`, `resonated`, `resonating`.
- Why it reads as machine text: Models use it to claim an emotional effect on readers with no evidence (`this message resonates with users`). It is how marketing reports a feeling it did not measure. It also closes generated advice as a soft hedge (`I hope this resonates`). Research reports that use it usually skipped the step of counting responses.
- Where it shows up: brand guidelines, user research summaries, LinkedIn posts, cover letters.

```slop
This message really resonates with our target audience.
Your mission resonates deeply with me.
Choose colors that resonate with your brand.
```

Replace with:

- Report the evidence: "6 of 8 people in testing chose it".
- `matches` or `fits` for brand rules, with the rule.
- In letters, give the specific reason in one sentence.

Rewrites:

```slop
This message really resonates with our target audience.
```

After: In the survey, 41% picked this headline as their reason to sign up, more than any other.

```slop
Your mission resonates deeply with me.
```

After: I want to work on tax software because I filed my parents' returns for ten years and hated every form.

```slop
Choose colors that resonate with your brand.
```

After: Use the brand orange `#B4441C` for one action per screen and gray for the rest.

- Literal use: for physics and acoustics, write "vibrates at" and give the frequency in Hz.

#### 024. `transcend`

- Kind: verb. Banned forms: `transcend`, `transcends`, `transcended`, `transcending`.
- Why it reads as machine text: A word from theology and philosophy that models apply to genres, borders, and product categories (`transcends traditional boundaries`). It sets up a grand frame the content cannot fill. Readers cannot test any part of it. It is praise that cannot be wrong, which makes it worthless as information.
- Where it shows up: art and music reviews, brand manifestos, product category claims, keynote copy.

```slop
Good design transcends trends.
Our platform transcends the limitations of traditional CRMs.
Music that transcends genres and borders.
```

Replace with:

- `outlasts` or `goes beyond`, only with what is passed and how.
- Name the limit that was removed.
- Cut it and describe what the thing is.

Rewrites:

```slop
Good design transcends trends.
```

After: Pages set in 16px black text on white were readable in 2005 and still are.

```slop
Our platform transcends the limitations of traditional CRMs.
```

After: Unlike most CRMs, contacts sync both ways with Gmail and Outlook and keep custom fields.

```slop
Music that transcends genres and borders.
```

After: She mixes Malian guitar with Detroit techno and sings in Bambara and French.

- Literal use: in maths, keep `transcendental number` in inline code.

#### 025. `reimagine`

- Kind: verb. Banned forms: `reimagine`, `reimagines`, `reimagined`, `reimagining`, `re-imagine`.
- Why it reads as machine text: Every redesign announcement and model-written product description uses it (`we reimagined the inbox`). It claims a fresh start and lets the writer skip the list of what changed. Users of the old version want that list. Agencies use it so often that it no longer signals any size of change.
- Where it shows up: redesign announcements, App Store "What's New" notes, agency case studies, game remakes.

```slop
We've reimagined the inbox from the ground up.
Reimagining how teams work together.
The classic game, reimagined for a new generation.
```

Replace with:

- `redesigned`, plus the list of changes.
- `rebuilt` when the code was rewritten.
- `new version` or `remake` for games and media.

Rewrites:

```slop
We've reimagined the inbox from the ground up.
```

After: The new inbox groups mail by sender, hides newsletters by default, and moves search to the top.

```slop
Reimagining how teams work together.
```

After: Comments, tasks, and files for one project now sit in the same thread.

```slop
The classic game, reimagined for a new generation.
```

After: A remake of the 1998 game with new art, the original levels, and online co-op.

- Literal use: for thinking about something again, write "rethink".

#### 026. `redefine`

- Kind: verb. Banned forms: `redefine`, `redefines`, `redefined`, `redefining`.
- Why it reads as machine text: `Redefining X` is a tagline template that claims a category means something new because this product exists. Models fill it in for cars, laptops, and to-do apps alike. The definition that supposedly changed is never stated, old or new. It also ages badly: the next model of the same product makes the claim look silly.
- Where it shows up: taglines, keynote slides, ad copy, About pages.

```slop
Redefining what a laptop can be.
This app redefines productivity.
A camera that redefines mobile photography.
```

Replace with:

- State the old expectation and the new fact.
- Give the spec that is unusual.
- Cut the tagline and use the spec as the headline.

Rewrites:

```slop
Redefining what a laptop can be.
```

After: A 13-inch laptop that weighs 980 g and runs 20 hours on one charge.

```slop
This app redefines productivity.
```

After: A to-do list with one rule: anything older than 7 days gets archived.

```slop
A camera that redefines mobile photography.
```

After: A 1-inch sensor in a phone, the same size as in many compact cameras.

- Literal use: for code, write "define again" or "override", and quote the directive in inline code (`#undef` then `#define`).

#### 027. `reshape`

- Kind: verb. Banned forms: `reshape`, `reshapes`, `reshaped`, `reshaping`.
- Why it reads as machine text: Think pieces and analyst reports pair it with industries (`AI is reshaping the workforce`). Models copy the frame to suggest a large change in progress without saying who changed what. It is a forecast dressed as an observation. It turns the writer into a commentator on forces instead of a reporter of facts.
- Where it shows up: opinion pieces, market reports, blog intros, conference themes.

```slop
AI is reshaping the software industry.
Remote work has reshaped how we design offices.
These trends are reshaping customer expectations.
```

Replace with:

- `changes`, with the specific change and its source.
- Give a number with a date.
- Cut the scene-setting sentence and start with the evidence.

Rewrites:

```slop
AI is reshaping the software industry.
```

After: In our 2025 survey, 62% of developers used an AI assistant at least once a week.

```slop
Remote work has reshaped how we design offices.
```

After: Since 2021 our office went from 120 desks to 40, and meeting room bookings doubled.

```slop
These trends are reshaping customer expectations.
```

After: Half of support tickets now arrive through chat, up from 15% two years ago.

- Literal use: for arrays, put the call in inline code (`np.reshape(a, (3, 4))`) and write "change the shape to 3 by 4".

#### 028. `envision`

- Kind: verb. Banned forms: `envision`, `envisions`, `envisioned`, `envisioning`.
- Why it reads as machine text: Vision statements and founder letters use it for a future that a roadmap would have to put dates on. Models produce `we envision a world where` as an opener for any product. It replaces commitments with wishes. Readers of an RFC need scope and dates, and this verb supplies neither.
- Where it shows up: mission statements, RFC motivation sections, founder letters, roadmap pages.

```slop
We envision a world where every developer has access to AI.
I envision this feature becoming the core of the product.
The team envisions a seamless experience across devices.
```

Replace with:

- `plan`, `want`, `expect`, with a date.
- In RFCs, write the goals and the non-goals.
- Cut the vision and state what ships next.

Rewrites:

```slop
We envision a world where every developer has access to AI.
```

After: By 2027 we want the free plan to include 500 completions a month.

```slop
I envision this feature becoming the core of the product.
```

After: If 30% of active users open this view by Q3, we will make it the default.

```slop
The team envisions a seamless experience across devices.
```

After: Drafts sync between phone and desktop within 2 seconds.

- Literal use: for picturing something in the mind, write "imagine" or "picture".

#### 029. `curate`

- Kind: verb. Banned forms: `curate`, `curates`, `curated`, `curating`.
- Why it reads as machine text: Museums do this; models say lists, playlists, feeds, and starter kits are `curated` to suggest taste where there was a search query or a scrape. The adjective has its own entry; the verb hides the same missing facts: who picked, from how many, by what rule. Fully automated feeds now call themselves `curated`, which removed what meaning the word had.
- Where it shows up: awesome-lists, newsletters, marketplace pages, template galleries.

```slop
We curate the best resources for frontend developers.
A hand-curated list of 50 design tools.
Our team curates every product before it goes live.
```

Replace with:

- `pick`, `select`, `choose`, with the rule.
- `edit` for newsletters.
- `review` for a quality check, with the criteria.

Rewrites:

```slop
We curate the best resources for frontend developers.
```

After: Each week we pick five frontend articles, all published in the last 7 days and all with code.

```slop
A hand-curated list of 50 design tools.
```

After: 50 design tools, each used by one of us on a paid project in the last year.

```slop
Our team curates every product before it goes live.
```

After: Two reviewers test each product for a week and check the seller's return policy.

- Literal use: for museums, write "organized the exhibition"; keep the job title in inline code (`curator`).

#### 030. `embrace`

- Kind: verb. Banned forms: `embrace`, `embraces`, `embraced`, `embracing`.
- Why it reads as machine text: Models use it for adopting anything: change, TypeScript, chaos. The physical image adds warmth to a technical decision and removes the reason for it. A decision needs a reason, and this word supplies an attitude in its place. It also frames disagreement as fear of change, which shuts down any talk about costs.
- Where it shows up: engineering blog posts, keynotes, onboarding docs, self-help openers.

```slop
It's time to embrace TypeScript.
We embrace failure as a learning opportunity.
Embrace the power of serverless.
```

Replace with:

- `adopt`, `switch to`, `start using`, with the reason.
- `accept` for an attitude, then name the practice.
- `try`, when the decision is still an experiment; give the end date.
- Cut it and give the decision with its date.

Rewrites:

```slop
It's time to embrace TypeScript.
```

After: We moved the frontend to TypeScript in May after three outages caused by undefined fields.

```slop
We embrace failure as a learning opportunity.
```

After: Every incident gets a blameless review within 5 working days.

```slop
Embrace the power of serverless.
```

After: The resize job runs on Lambda; we pay about $4 a month instead of $70 for an idle server.

- Literal use: for a hug, write "hug".

#### 031. `enhance`

- Kind: verb. Banned forms: `enhance`, `enhances`, `enhanced`, `enhancing`, `enhancement`, `enhancements`.
- Why it reads as machine text: It is the default verb for improvement in generated release notes and PR descriptions. It tells the reader something got better and leaves out what, by how much, and for whom. `Enhanced performance` with no number is the classic case. Issue trackers use `enhancement` as a label, and models copy that label into prose.
- Where it shows up: changelogs, PR titles, feature lists, issue labels.

```slop
Enhanced performance and stability.
This PR enhances the search experience.
AI-enhanced photo editing.
```

Replace with:

- `improve`, with the number.
- Say what changed: "added", "fixed", "faster".
- In changelogs, one line per change, each with its own verb.
- `fix` for bugs; a fixed bug is not an improvement in general terms.

Rewrites:

```slop
Enhanced performance and stability.
```

After: Startup time down from 3.1 s to 1.4 s; fixed the crash when opening files over 2 GB.

```slop
This PR enhances the search experience.
```

After: Search now matches partial words and shows results as you type.

```slop
AI-enhanced photo editing.
```

After: Remove backgrounds and fix exposure in one click, with undo for each step.

- Literal use: keep GitHub's label and the web term in inline code (`enhancement`, `progressive enhancement`); for images, write "upscale" or "sharpen".

#### 032. `enrich`

- Kind: verb. Banned forms: `enrich`, `enriches`, `enriched`, `enriching`, `enrichment`.
- Why it reads as machine text: Two habits meet here: education copy (`enriching experiences`) and data pipeline jargon (`enrich the record`). Models use both, and both hide what was added. A record that went through that step has new fields; name them. In education copy it signals that the writer has not seen the syllabus.
- Where it shows up: course pages, data pipeline docs, CRM feature lists, school program descriptions.

```slop
An enriching learning experience for curious minds.
The pipeline enriches events with user metadata.
Enrich your content with AI-generated summaries.
```

Replace with:

- `add`, with the fields or content added.
- `join` or `look up` for data pipelines.
- Cut the adjective and describe the program.

Rewrites:

```slop
An enriching learning experience for curious minds.
```

After: A 6-week after-school course: build a weather station and log readings to a spreadsheet.

```slop
The pipeline enriches events with user metadata.
```

After: The pipeline looks up each event's `user_id` and adds `plan`, `country`, and `signup_date`.

```slop
Enrich your content with AI-generated summaries.
```

After: Each article gets a three-sentence summary at the top, generated and then checked by an editor.

- Literal use: for uranium, write "concentrated to 4% U-235"; for soil, write "fertilized" and name what was added.

#### 033. `facilitate`

- Kind: verb. Banned forms: `facilitate`, `facilitates`, `facilitated`, `facilitating`.
- Why it reads as machine text: Bureaucratic and academic register for "help" or "allow", common in grant text and policy. Models use it to sound formal, and it blurs the subject: what does what, and how. When a person does this for a meeting, "run" or "lead" is shorter. It makes a sentence longer while hiding who acts.
- Where it shows up: design docs, academic abstracts, workshop descriptions, API docs.

```slop
This module facilitates communication between services.
The new API facilitates integration with third-party tools.
I facilitated a design sprint with stakeholders.
```

Replace with:

- `lets`, `helps`, `allows`, with the action.
- `run` or `lead` for meetings and workshops.
- Name the mechanism: "sends", "exposes", "proxies".

Rewrites:

```slop
This module facilitates communication between services.
```

After: This module sends messages between services over gRPC and retries failed calls 3 times.

```slop
The new API facilitates integration with third-party tools.
```

After: The API accepts webhooks from Zapier and Make and returns standard JSON errors.

```slop
I facilitated a design sprint with stakeholders.
```

After: I ran a 4-day design sprint with the support lead, two engineers, and the CFO.

- Literal use: for the job of running a workshop, write "moderator" or "workshop lead".

#### 034. `optimize`

- Kind: verb. Banned forms: `optimize`, `optimizes`, `optimized`, `optimizing`, `optimization`, `optimizer`, and the `-ise` spellings.
- Why it reads as machine text: In code it has a real meaning (reduce a measured cost), but models use it as a general word for "improved": `optimized for performance`, `optimized workflow`. Without the metric and the before and after values, nobody can check the claim. Pages that say `fully optimized` rarely show a profile. SEO copy uses it as praise, which strips the last trace of the technical sense.
- Where it shows up: PR titles, commit messages, SEO copy, résumé bullets.

```slop
Optimized the database queries for better performance.
Fully optimized for mobile devices.
Optimize your workflow with smart automations.
```

Replace with:

- `make X faster` or `cut X`, with numbers and the method.
- For screen sizes, name the widths you tested.
- In commits, name the change: "add index on `orders.user_id`".
- `tune` for a config change, with the parameter and its old and new value.

Rewrites:

```slop
Optimized the database queries for better performance.
```

After: Added an index on `orders.user_id`; the order history query went from 1.8 s to 40ms.

```slop
Fully optimized for mobile devices.
```

After: Tested at 360px and 414px wide; tap targets are at least 44 by 44px.

```slop
Optimize your workflow with smart automations.
```

After: Rules file each invoice in the right folder and remind the client after 14 days.

- Literal use: for compilers and solvers, keep the term in inline code (`-O2`, `scipy.optimize.minimize`) or write "minimize the cost function".

#### 035. `maximize`

- Kind: verb. Banned forms: `maximize`, `maximizes`, `maximized`, `maximizing`, `maximization`, and the `-ise` spellings.
- Why it reads as machine text: Models use it as an intensifier for vague goals: impact, ROI, potential. In maths it names a target function and the limits on it; in generated copy it has neither. The reader cannot tell what was measured or what the ceiling is. It pairs with `ROI`, `engagement`, and `productivity`, nouns that rarely come with a figure.
- Where it shows up: sales pages, productivity advice, strategy decks, ad copy.

```slop
Maximize your ROI with data-driven insights.
Tips to maximize your productivity.
Maximize engagement with personalized emails.
```

Replace with:

- `increase`, with the measure and the target.
- Name the steps instead of the goal.
- Cut it and state the result someone measured.

Rewrites:

```slop
Maximize your ROI with data-driven insights.
```

After: Customers who used the budget report cut ad spend by 18% with no drop in sales.

```slop
Tips to maximize your productivity.
```

After: Block two hours each morning with notifications off, and answer email at 11 and 4.

```slop
Maximize engagement with personalized emails.
```

After: Emails with the customer's last order in the subject line got twice the clicks.

- Literal use: for windows, write "full screen"; in maths, write "find the largest value of" or use inline code (`argmax`).
