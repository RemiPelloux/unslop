#### 036. `ideate`

- Kind: verb. Banned forms: `ideate`, `ideates`, `ideated`, `ideating`, `ideation`.
- Why it reads as machine text: Design-thinking workshops made it the name of a phase, and models now use it for any brainstorm. It turns "think of ideas" into a process word that sounds billable. The output that matters, how many ideas and which one won, is missing from the sentence. Outside design teams, readers stop at it, because nobody uses it in speech.
- Where it shows up: design process docs, workshop agendas, product manager job ads, UX case studies.

```slop
We ideated several solutions during the workshop.
The team will ideate on ways to improve onboarding.
Ideation phase: 2 weeks.
```

Replace with:

- `brainstorm`, `come up with`, `sketch`, with the count.
- Name the method: "crazy eights", "a list of 30 headlines".
- Report which idea won and why.

Rewrites:

```slop
We ideated several solutions during the workshop.
```

After: In the workshop we sketched 24 layouts and picked 3 to test with users.

```slop
The team will ideate on ways to improve onboarding.
```

After: Each person brings three onboarding changes on Friday, and we vote on one to ship.

```slop
Ideation phase: 2 weeks.
```

After: Sketching: 2 weeks, ending with three clickable prototypes.

- Literal use: in clinical writing, keep the clinical term in inline code (`suicidal ideation`) as clinicians write it.

#### 037. `democratize`

- Kind: verb. Banned forms: `democratize`, `democratizes`, `democratized`, `democratizing`, `democratization`, and the `-ise` spellings.
- Why it reads as machine text: Tech marketing uses it to mean "make cheaper" or "make easier" while borrowing the moral weight of voting rights. Models copy `democratizing access to X` for trading apps, AI models, and design tools alike. It hides the price and the user count, the two facts that would back the claim. When the price is still $40 a month, readers notice the gap.
- Where it shows up: startup mission statements, funding announcements, open source launch posts.

```slop
We're democratizing access to financial data.
Our mission is to democratize AI.
No-code tools democratize software development.
```

Replace with:

- `make cheaper` or `make free`, with the old and new price.
- `make easier`, with the skill no longer needed.
- Name who can now use it and how many do.

Rewrites:

```slop
We're democratizing access to financial data.
```

After: Stock fundamentals for 8,000 US companies, free, with a CSV download.

```slop
Our mission is to democratize AI.
```

After: We publish model weights under Apache 2.0, small enough to run on one consumer GPU.

```slop
No-code tools democratize software development.
```

After: Store owners build order forms without writing code; they made 12,000 forms last month.

- Literal use: for politics, write "give voting rights to" or "hold elections in".

#### 038. `future-proof`

- Kind: verb and adjective. Banned forms: `future-proof`, `future proof`, `future-proofs`, `future-proofed`, `future-proofing`.
- Why it reads as machine text: Nobody can see what is coming, so the claim cannot be tested, which is why sales copy likes it. Models apply it to frameworks, careers, and laptops. In engineering it hides the real decision: which changes the design expects and which it does not. Buying guides that use it are often out of date within one product cycle.
- Where it shows up: architecture docs, hardware buying guides, career advice, consulting proposals.

```slop
Future-proof your codebase with our modular architecture.
A future-proof laptop with Wi-Fi 7.
Future-proofing your career in the age of AI.
```

Replace with:

- Name the change the design allows: "add a payment provider without touching checkout".
- Give support dates: "security updates until 2031".
- `plan for`, with the specific plan.

Rewrites:

```slop
Future-proof your codebase with our modular architecture.
```

After: Each payment provider is one file that implements `charge` and `refund`; adding Adyen took two days.

```slop
A future-proof laptop with Wi-Fi 7.
```

After: Wi-Fi 7 and two USB4 ports, and the maker promises OS updates until 2031.

```slop
Future-proofing your career in the age of AI.
```

After: Learn SQL and statistics; both have appeared in data job ads for 30 years.

- Literal use: there is no literal sense; write "still works when X changes" and name X.

#### 039. `unpack`

- Kind: verb. Banned forms: `unpack`, `unpacks`, `unpacked`, `unpacking`.
- Why it reads as machine text: Borrowed from therapy and humanities seminars (`let's unpack that`), it promises careful analysis of an idea. Models use it as a bridge into a list of obvious points. `There's a lot to unpack here` delays the answer by one sentence and announces effort instead of making it. Chat models produce it at the start of answers, so it marks the source.
- Where it shows up: explainer posts, podcast show notes, AI chat answers, newsletter intros.

```slop
Let's unpack what this means for developers.
In this article, we unpack the new EU AI Act.
There's a lot to unpack here.
```

Replace with:

- `explain`, `go through`.
- Instead of "a lot", say how many points and list them.
- Cut it and give the first point.

Rewrites:

```slop
Let's unpack what this means for developers.
```

After: For developers, two things change: tokens expire after 1 hour, and refresh needs a new scope.

```slop
In this article, we unpack the new EU AI Act.
```

After: This article lists which AI systems the EU AI Act bans, which it calls high-risk, and the deadline for each.

```slop
There's a lot to unpack here.
```

After: Three things changed in this release.

- Literal use: for archives, luggage, and destructuring, write "extract" or "destructure", or put the command in inline code (`tar -xzf`, `a, b = pair`).

#### 040. `immerse`

- Kind: verb. Banned forms: `immerse`, `immerses`, `immersed`, `immersing`.
- Why it reads as machine text: Game and travel marketing use it for "you feel inside it", and models extend it to docs, courses, and dashboards. It claims a state of total attention the reader has not had yet. It hides what the person will see and do; `immersive` has its own entry for the same reason. Course pages that promise it rarely list the hours of practice.
- Where it shows up: game store pages, VR and audio product copy, course descriptions, travel writing.

```slop
Immerse yourself in a world of stunning visuals.
Immerse your users in a rich, interactive experience.
Students are fully immersed in the language from day one.
```

Replace with:

- Describe what is on screen or in the room.
- Give the hours, the format, the ratio.
- Cut it and start with the activity.

Rewrites:

```slop
Immerse yourself in a world of stunning visuals.
```

After: An open-world game set in 1920s Cairo, with a day and night cycle and about 40 hours of story.

```slop
Immerse your users in a rich, interactive experience.
```

After: Users drag the timeline to replay each step of the build.

```slop
Students are fully immersed in the language from day one.
```

After: Classes run only in Spanish, 4 hours a day, and students live with host families.

- Literal use: for liquids, write "dip", "submerge", or "soak", with the time.

#### 041. `captivate`

- Kind: verb. Banned forms: `captivate`, `captivates`, `captivated`, `captivating`.
- Why it reads as machine text: Models claim the reader's attention before earning it: `captivate your audience`, `a captivating story`. It reports an effect on people that nobody measured. In product copy it signals that the writer is describing a hope; the adjective `captivating` has its own entry. Book blurbs stack it with `gripping` and `unputdownable`, which readers have learned to skip.
- Where it shows up: presentation tips, book blurbs, portfolio intros, email marketing guides.

```slop
Captivate your audience with stunning slides.
Her story captivated readers around the world.
Design emails that captivate from the first line.
```

Replace with:

- `hold attention`, only with how it was measured.
- Report sales, reads, or completion rates.
- Describe the content that would do the work.

Rewrites:

```slop
Captivate your audience with stunning slides.
```

After: Put one claim and one number on each slide, in 32px type or larger.

```slop
Her story captivated readers around the world.
```

After: The memoir sold 400,000 copies in its first year and was translated into 21 languages.

```slop
Design emails that captivate from the first line.
```

After: Put the order status in the subject line and the tracking link in the first sentence.

- Literal use: for taking a prisoner, write "capture".

#### 042. `mesmerize`

- Kind: verb. Banned forms: `mesmerize`, `mesmerizes`, `mesmerized`, `mesmerizing`, and the `-ise` spellings.
- Why it reads as machine text: Named after Franz Mesmer, the 18th-century doctor of "animal magnetism", it now shows up in generated descriptions of animations, sunsets, and code visualizations. It replaces a description of motion with a claim that the viewer froze. Anyone who has watched the GIF knows they did not. It also tells readers to admire the effect before they have seen it.
- Where it shows up: Dribbble and CodePen descriptions, travel blogs, generative art posts, game trailers.

```slop
A mesmerizing particle animation built with Three.js.
The sunset over the bay was simply mesmerizing.
Mesmerize your visitors with scroll-triggered effects.
```

Replace with:

- Describe the motion: speed, count, what triggers it.
- Describe the scene in concrete terms.
- Cut it, then ask whether the effect is needed at all.

Rewrites:

```slop
A mesmerizing particle animation built with Three.js.
```

After: 20,000 particles drift toward the cursor at 60fps, built with Three.js.

```slop
The sunset over the bay was simply mesmerizing.
```

After: At 8 p.m. the sun dropped behind the hills and the water went copper, then gray.

```slop
Mesmerize your visitors with scroll-triggered effects.
```

After: Section headings fade in over 150ms as they enter the viewport, and not at all with reduced motion on.

- Literal use: for the history of hypnosis, write "hypnotize" or name Mesmer.

#### 043. `ignite`

- Kind: verb. Banned forms: `ignite`, `ignites`, `ignited`, `igniting`.
- Why it reads as machine text: Fire images cluster in generated motivational text: `ignite curiosity`, `ignite growth`, `ignite your team`. The word sells the start of something and never says what it becomes. It reads like a keynote poster, and the paragraph under it rarely contains a plan. Conference organizers like it as an event name, so a talk abstract that repeats it sounds like a press kit.
- Where it shows up: conference names and themes, course pages, leadership posts, campaign slogans.

```slop
Ignite your passion for coding.
This campaign ignited a conversation about privacy.
Ignite growth with targeted ads.
```

Replace with:

- `start` or `lead to`, with the result.
- Report the measurable effect.
- Cut it and describe the course or event.

Rewrites:

```slop
Ignite your passion for coding.
```

After: Build and deploy a small game in your first week.

```slop
This campaign ignited a conversation about privacy.
```

After: After the campaign, three newspapers covered the data leak and the company shortened its retention period to 30 days.

```slop
Ignite growth with targeted ads.
```

After: Ads shown only to people who visited the pricing page in the last 14 days.

- Literal use: for fire and engines, write "light" or "catch fire"; keep Apache's project name in inline code (`Ignite`).

#### 044. `propel`

- Kind: verb. Banned forms: `propel`, `propels`, `propelled`, `propelling`.
- Why it reads as machine text: A motion verb that makes a career or company move by the force of one cause: `propel your career`, `propelled us to the top`. Models use it for causal claims a careful writer would hedge. It hides the other causes and the time it took. Readers who know the field know that one skill or one strategy rarely explains a result.
- Where it shows up: résumés, press releases, case studies, career advice.

```slop
These skills will propel your career forward.
Our new strategy propelled revenue to record highs.
AI-powered analytics that propel your business.
```

Replace with:

- `help` or `lead to`, with the chain of cause and effect.
- Report the change and the period.
- Cut it and say what the product does.

Rewrites:

```slop
These skills will propel your career forward.
```

After: Reading query plans is the skill our hiring managers ask about most in backend interviews.

```slop
Our new strategy propelled revenue to record highs.
```

After: Revenue reached $4.2M in Q2, our highest quarter so far, two quarters after we added annual billing.

```slop
AI-powered analytics that propel your business.
```

After: Reports on which products sell together, updated nightly.

- Literal use: for physical motion, write "push", "drive", or "move", and give the force or speed.

#### 045. `skyrocket`

- Kind: verb. Banned forms: `skyrocket`, `skyrockets`, `skyrocketed`, `skyrocketing`.
- Why it reads as machine text: It is used for any rise on a growth chart, usually with the axis cropped. Models write `sales skyrocketed` for a 20% change and a twentyfold change alike. The reader cannot tell which one happened, and the writer gets credit for both. Paired with a chart that starts its y-axis above zero, it is a common way to exaggerate a small change.
- Where it shows up: growth case studies, newsletter headlines, startup posts, ad copy.

```slop
Our signups skyrocketed after the launch.
Skyrocket your conversions with this one trick.
Cloud costs are skyrocketing.
```

Replace with:

- `rose`, `grew`, `doubled`, with the numbers and dates.
- Give the start and end values.
- Cut the verb and show the chart with labeled axes.

Rewrites:

```slop
Our signups skyrocketed after the launch.
```

After: Signups went from 40 a day to 900 a day in the week after launch.

```slop
Skyrocket your conversions with this one trick.
```

After: Moving the signup form above the fold raised conversion from 2.1% to 3.4%.

```slop
Cloud costs are skyrocketing.
```

After: Our AWS bill rose from $12,000 to $31,000 a month during 2024.

- Literal use: for fireworks, write "rocket" or "firework".

#### 046. `boost`

- Kind: verb and noun. Banned forms: `boost`, `boosts`, `boosted`, `boosting`, `booster`.
- Why it reads as machine text: A short, upbeat verb that models attach to productivity, morale, speed, and sales. It promises an increase with no size. `Boost performance` appears in changelogs where nobody ran a benchmark, and `up to 2x` hides that most users see no change. Short and harmless as it looks, it is one of the most frequent verbs in model-written app store text.
- Where it shows up: changelogs, app store descriptions, marketing emails, video titles.

```slop
Boost your productivity with these 10 VS Code extensions.
This update boosts performance by up to 2x.
A quick morale boost for the team.
```

Replace with:

- `increase` or `raise`, with the measured change.
- `faster`, with the benchmark and its conditions.
- `help`, only next to what helped and by how much.
- Cut it and name the thing done.

Rewrites:

```slop
Boost your productivity with these 10 VS Code extensions.
```

After: Ten VS Code extensions, each with the one task it saves you, such as renaming a symbol across files.

```slop
This update boosts performance by up to 2x.
```

After: Builds are up to 2 times faster on projects with more than 500 files; small projects see no change.

```slop
A quick morale boost for the team.
```

After: We took the team out for lunch after the release.

- Literal use: keep the C++ library in inline code (`Boost`); for vaccines, write "follow-up dose"; for power circuits, write "step-up converter".

#### 047. `fuel`

- Kind: verb and noun. Banned forms: `fuel`, `fuels`, `fueled`, `fueling`, `fuelled`, `fuelling`.
- Why it reads as machine text: Models write `fueled by` to explain causes in news-style summaries and `fuel your growth` in marketing. The image says something burns to drive something else, and the writer never names the engine. In bios the noun turns into the filler joke `fueled by coffee`. It also suggests the cause will run out, which the writer did not intend.
- Where it shows up: About pages, news summaries, founder bios, startup blog posts.

```slop
Fueled by coffee and open source.
Rising demand fueled the price increase.
Fuel your growth with actionable insights.
```

Replace with:

- `caused`, `led to`, `pushed up`, with the evidence.
- `pays for` or `funds` when money is meant.
- Cut the bio joke.

Rewrites:

```slop
Fueled by coffee and open source.
```

After: Built by four people in Lyon, on weekends, since 2021.

```slop
Rising demand fueled the price increase.
```

After: Prices rose 14% after orders doubled and the factory's output stayed flat.

```slop
Fuel your growth with actionable insights.
```

After: A weekly report of which pages bring in paying customers.

- Literal use: name the substance ("petrol", "diesel", "kerosene", "natural gas") or put the word in inline code (`fuel`).

#### 048. `intertwine`

- Kind: verb. Banned forms: `intertwine`, `intertwines`, `intertwined`, `intertwining`.
- Why it reads as machine text: Models use it for any two topics that relate: `design and engineering are deeply intertwined`. The image of twisted threads says they connect and skips how. Usually one depends on the other in a direction that could be stated in one clause. Essays that use it rarely reach the point of saying which side depends on which.
- Where it shows up: essays, think pieces, design philosophy posts, academic intros.

```slop
Performance and accessibility are deeply intertwined.
Our story is intertwined with the history of the web.
Intertwining data and design to create meaningful experiences.
```

Replace with:

- `depends on`, `affects`, `is part of`, with the direction.
- `linked`, only next to the link.
- Name the shared cause.

Rewrites:

```slop
Performance and accessibility are deeply intertwined.
```

After: Large JavaScript bundles make pages slow to respond on cheap phones, and screen reader users feel that delay on every key press.

```slop
Our story is intertwined with the history of the web.
```

After: We started in 1998 as a hosting company and shipped our first browser extension in 2004.

```slop
Intertwining data and design to create meaningful experiences.
```

After: We read the support tickets every week and change one screen based on them.

- Literal use: for threads, wires, and plants, write "twisted together" or "wrapped around".

#### 049. `underpin`

- Kind: verb. Banned forms: `underpin`, `underpins`, `underpinned`, `underpinning`.
- Why it reads as machine text: A building term (support a wall from below) that models use to claim one thing is the base of another: `the principles that underpin our work`. It suggests depth and leaves the principles unlisted. In technical text the sentence usually means "uses"; the noun `underpinning` has its own entry. Strategy docs use it to make a list of opinions look like a foundation.
- Where it shows up: values pages, architecture overviews, academic papers, strategy docs.

```slop
The principles that underpin our design system.
Strong fundamentals underpin every successful engineer.
PostgreSQL underpins our entire data platform.
```

Replace with:

- `is based on`, `uses`, `runs on`.
- List the principles themselves.
- Cut it and say what depends on what.

Rewrites:

```slop
The principles that underpin our design system.
```

After: Our design system has three rules: 4px spacing steps, one accent color, no shadows.

```slop
Strong fundamentals underpin every successful engineer.
```

After: Engineers who can read a stack trace and write a failing test fix bugs faster.

```slop
PostgreSQL underpins our entire data platform.
```

After: Every service writes to one PostgreSQL 16 cluster, and analytics reads from a replica.

- Literal use: for foundations, write "support from below" and name the method ("mass concrete pour").

#### 050. `encompass`

- Kind: verb. Banned forms: `encompass`, `encompasses`, `encompassed`, `encompassing`.
- Why it reads as machine text: Models use it in scope statements (`our services encompass strategy, design, and development`) to sound broad. It promises coverage and never states the limits. `all-encompassing` is the same claim with even less information. Job descriptions that use it often go on to list three roles' worth of duties.
- Where it shows up: agency pages, course syllabi, job descriptions, policy scope sections.

```slop
Our services encompass strategy, design, and development.
The course encompasses everything you need to know about Rust.
An all-encompassing platform for modern teams.
```

Replace with:

- `includes`, `covers`.
- List the items, then what is out of scope.
- `spans` for ranges of time or numbers, with the two ends.
- Cut it and make the list the sentence.

Rewrites:

```slop
Our services encompass strategy, design, and development.
```

After: We design and build web apps; we do not run ads or SEO.

```slop
The course encompasses everything you need to know about Rust.
```

After: The course covers ownership, borrowing, traits, and async; it skips macros and `unsafe`.

```slop
An all-encompassing platform for modern teams.
```

After: Chat, docs, and tasks in one app, for teams of 5 to 50.

- Literal use: for geography, write "covers" with the boundary: "the park covers 400 square km".

#### 051. `epitomize`

- Kind: verb. Banned forms: `epitomize`, `epitomizes`, `epitomized`, `epitomizing`, and the `-ise` spellings.
- Why it reads as machine text: A school-essay verb that models use to make one example stand for a whole quality: `this project epitomizes our commitment to quality`. The example then never gets described. The reader learns the label and not the work. It is common in generated cover letters, where it praises the company back to itself.
- Where it shows up: award citations, case studies, performance reviews, cover letters.

```slop
This app epitomizes great UX.
Sarah epitomizes our company values.
The Bauhaus chair epitomizes modernist design.
```

Replace with:

- `is an example of` or `is typical of`, then say why.
- In reviews, name the action.
- Cut it and describe the example.

Rewrites:

```slop
This app epitomizes great UX.
```

After: The app asks for one permission at a time, at the moment it needs it, and works offline.

```slop
Sarah epitomizes our company values.
```

After: Sarah answered every on-call page within 5 minutes this quarter and wrote the runbook for the payments outage.

```slop
The Bauhaus chair epitomizes modernist design.
```

After: The Wassily chair is bent steel tube and stretched fabric straps, with no wooden frame and no padding.

- Literal use: there is no other sense; write "sum up" or "is the clearest example of".

#### 052. `exemplify`

- Kind: verb. Banned forms: `exemplify`, `exemplifies`, `exemplified`, `exemplifying`.
- Why it reads as machine text: A close cousin of `epitomize`, it appears in generated essays and review comments as praise without detail: `this function exemplifies good practice`. It points at an example and stops. The reader still does not know what to copy from it. In reviews, the author learns nothing to apply to the next PR.
- Where it shows up: code review comments, academic essays, documentation intros, award nominations.

```slop
This codebase exemplifies best practices in testing.
The following snippet exemplifies the pattern.
Her work exemplifies our commitment to excellence.
```

Replace with:

- `shows` or `is an example of`.
- Name the practice the example follows.
- For snippets, write "For example" and show the code.

Rewrites:

```slop
This codebase exemplifies best practices in testing.
```

After: Each module has its tests next to it, and every bug fix starts with a failing test.

```slop
The following snippet exemplifies the pattern.
```

After: In this snippet the cache is checked first, and the database is read only on a miss.

```slop
Her work exemplifies our commitment to excellence.
```

After: She rewrote the billing retries and cut failed charges from 3% to 0.4%.

- Literal use: there is no other sense; write "for example" or "such as".

#### 053. `embody`

- Kind: verb. Banned forms: `embody`, `embodies`, `embodied`, `embodying`, `embodiment`.
- Why it reads as machine text: Models use it to say a person or product is a quality in physical form: `embodies our values`, `embodies simplicity`. The claim sounds deep and gives nothing to check. Product pages use it to avoid listing what the product does. It also asks the reader to accept a metaphysical claim about a logo or a chair.
- Where it shows up: brand guidelines, product descriptions, award text, team bios.

```slop
Our new logo embodies who we are.
This chair embodies Scandinavian simplicity.
Every feature embodies our design philosophy.
```

Replace with:

- `shows`, `has`, `follows`, with the specific trait.
- Describe the object.
- Cut the abstract claim.

Rewrites:

```slop
Our new logo embodies who we are.
```

After: The new logo is a single-weight wordmark in black, readable at 16px.

```slop
This chair embodies Scandinavian simplicity.
```

After: An ash wood chair with four legs, no screws, and a woven paper-cord seat.

```slop
Every feature embodies our design philosophy.
```

After: Each feature ships with keyboard support and an empty state that says what to do next.

- Literal use: in cognitive science or patent claims, keep the term in inline code (`embodied cognition`, `in one embodiment`).

#### 054. `encapsulate`

- Kind: verb. Banned forms: `encapsulate`, `encapsulates`, `encapsulated`, `encapsulating`.
- Why it reads as machine text: It has a real meaning in object-oriented design, which gives models cover to use it for summaries: `this quote encapsulates our approach`. In docs it is used loosely for "wraps" or "contains", so the reader cannot tell whether the design term is meant. Both uses skip the content being summed up or hidden. Year-end posts that use it tend to name one abstract noun and no figures.
- Where it shows up: closing lines of essays, class and module docs, mission statements, year-end summaries.

```slop
This quote perfectly encapsulates our philosophy.
The Service class encapsulates all business logic.
One word encapsulates the year: growth.
```

Replace with:

- `sums up` for summaries, or just give the summary.
- `wraps`, `contains`, `hides` in code, and say what callers no longer see.
- Cut it.

Rewrites:

```slop
This quote perfectly encapsulates our philosophy.
```

After: We ship small changes daily and roll back within minutes when one breaks.

```slop
The Service class encapsulates all business logic.
```

After: `OrderService` holds the pricing and tax rules; controllers call `OrderService.place()` and never touch the tables.

```slop
One word encapsulates the year: growth.
```

After: Revenue grew 60% this year, and the team grew from 9 to 21 people.

- Literal use: for OOP and network packets, keep the term in inline code (`encapsulation`, `GRE encapsulation`).

#### 055. `burgeon`

- Kind: verb. Banned forms: `burgeon`, `burgeons`, `burgeoned`, `burgeoning`.
- Why it reads as machine text: Almost nobody says it aloud. Models produce `burgeoning field` and `burgeoning industry` as fixed pairs meaning "growing", which makes an intro sound like an analyst report. It hides the growth rate and the start date. Its usual partners are `field`, `industry`, and `market`, which makes it easy to spot.
- Where it shows up: report intros, market analyses, grant applications, essays on tech trends.

```slop
The burgeoning field of quantum computing.
A burgeoning community of open source contributors.
Interest in Rust has burgeoned in recent years.
```

Replace with:

- `growing`, with the rate.
- Give a count and a date.
- Cut the adjective; the topic does not need it.

Rewrites:

```slop
The burgeoning field of quantum computing.
```

After: Quantum computing, where the largest machines passed 1,000 qubits in 2023.

```slop
A burgeoning community of open source contributors.
```

After: 340 people opened a PR in the last 12 months, up from 90 the year before.

```slop
Interest in Rust has burgeoned in recent years.
```

After: Rust has been the most loved or most admired language in the Stack Overflow survey every year since 2016.

- Literal use: for plants, write "buds" or "sprouts".

#### 056. `flourish`

- Kind: verb and noun. Banned forms: `flourish`, `flourishes`, `flourished`, `flourishing`.
- Why it reads as machine text: Models use it to claim that something is healthy and growing: `communities flourish`, `your business will flourish`. It describes an outcome as a mood and leaves out the measure. As a noun (`a design flourish`) it hides what the decoration actually is. Coaching copy uses it as a promise of outcome that no coach could guarantee.
- Where it shows up: community posts, coaching copy, history summaries, design critiques.

```slop
Watch your business flourish with our tools.
The open source community has flourished since 2020.
A small flourish that adds personality to the UI.
```

Replace with:

- `grow`, with the measure.
- For the noun, name the detail.
- Cut it.

Rewrites:

```slop
Watch your business flourish with our tools.
```

After: Shops that turn on automatic reorders run out of stock 40% less often.

```slop
The open source community has flourished since 2020.
```

After: The project had 12 regular contributors in 2020 and 85 in 2024.

```slop
A small flourish that adds personality to the UI.
```

After: The empty inbox shows a hand-drawn mailbox at 120px in `--ink-3`.

- Literal use: for handwriting or music, write "decorative stroke" or "fanfare"; keep the charting tool's name in inline code (`Flourish`).

#### 057. `thrive`

- Kind: verb. Banned forms: `thrive`, `thrives`, `thrived`, `thriving`, `throve`.
- Why it reads as machine text: It is the verb of every careers page and wellness app: `a place where you can thrive`. Models use it as the end state of any advice, which is why it shows up in the last sentence. It names no outcome you could check; `thriving` has its own entry. Investor letters use it to describe companies that are in fact shrinking.
- Where it shows up: careers pages, onboarding emails, self-help posts, investor letters.

```slop
Join a team where you can thrive.
Businesses that adapt will thrive in 2025.
Help your plants thrive with smart watering.
```

Replace with:

- `do well`, only with the measure.
- Name what the place offers: pay, hours, promotion path.
- Describe the result.
- `grow`, `survive`, `stay open`, with a number and a period.

Rewrites:

```slop
Join a team where you can thrive.
```

After: Salary bands are public, everyone gets 30 days of leave, and promotions are reviewed twice a year.

```slop
Businesses that adapt will thrive in 2025.
```

After: Shops that added online ordering in 2024 kept 12% more customers than those that did not.

```slop
Help your plants thrive with smart watering.
```

After: The sensor waters each pot when soil moisture drops below 30%.

- Literal use: for biology, write "grows well" or "survives", with the conditions.

#### 058. `garner`

- Kind: verb. Banned forms: `garner`, `garners`, `garnered`, `garnering`.
- Why it reads as machine text: A press-release verb for "got": `garnered attention`, `garnered over 10,000 stars`. It is rare in speech, so readers notice it, and models produce it at a far higher rate than people do. It makes a count sound earned by charm and adds a syllable over "got". The README that leads with stars instead of what the project does has its order wrong anyway.
- Where it shows up: project READMEs, news summaries, LinkedIn posts, résumés.

```slop
The project has garnered over 10,000 GitHub stars.
Her research garnered international recognition.
The post garnered significant attention online.
```

Replace with:

- `got`, `received`, `has`.
- Give the number and the source.
- Cut it when the count is the only content.

Rewrites:

```slop
The project has garnered over 10,000 GitHub stars.
```

After: 10,000 GitHub stars.

```slop
Her research garnered international recognition.
```

After: Her thesis won the 2023 ACM Doctoral Dissertation Award.

```slop
The post garnered significant attention online.
```

After: The post got 80,000 views in two days and 300 comments on Hacker News.

- Literal use: for grain and harvests, write "gather" or "store".

#### 059. `boast`

- Kind: verb. Banned forms: `boast`, `boasts`, `boasted`, `boasting`.
- Why it reads as machine text: Real estate and travel listings made `boasts` the verb for "has" (`the apartment boasts a balcony`), and models adopted it for product specs and libraries. It reads as a listing written to sell. It also makes the object sound rarer than it is. Applied to an open source library, it sounds like a sales pitch for something free.
- Where it shows up: product descriptions, library READMEs, real estate and hotel listings, city guides.

```slop
The library boasts over 200 components.
The new MacBook boasts an impressive 18-hour battery life.
The city boasts a vibrant food scene.
```

Replace with:

- `has`, `includes`, `comes with`.
- Give the number and the comparison.
- Cut it and use a list.

Rewrites:

```slop
The library boasts over 200 components.
```

After: 200 components, each with React and Vue versions.

```slop
The new MacBook boasts an impressive 18-hour battery life.
```

After: Apple rates the battery at 18 hours of video playback.

```slop
The city boasts a vibrant food scene.
```

After: The city has 3 covered markets and about 40 taco stands within 1 km of the center.

- Literal use: for a person bragging, write "brag" or quote what they said.

#### 060. `herald`

- Kind: verb and noun. Banned forms: `herald`, `heralds`, `heralded`, `heralding`.
- Why it reads as machine text: A medieval image (a messenger announcing the king) that models use for any release: `heralds a new era`. It claims historical weight at the moment of announcement, before anyone can know. The sentence after it is vague about what the era is. Most releases it describes are forgotten within a year, which makes the word look worse in hindsight.
- Where it shows up: launch posts, tech news summaries, keynote recaps, op-eds.

```slop
This release heralds a new era of web development.
The deal was heralded as a turning point for the industry.
Heralding the next chapter of our company.
```

Replace with:

- `announces`, `marks`, `starts`, only with the fact.
- Report who said what: "three analysts called it".
- Cut it and describe the release.

Rewrites:

```slop
This release heralds a new era of web development.
```

After: Version 5 drops support for IE11 and ships ES modules only.

```slop
The deal was heralded as a turning point for the industry.
```

After: Three analysts called the deal a turning point; the share price rose 11% that week.

```slop
Heralding the next chapter of our company.
```

After: We are moving into hardware, and our first device ships in March.

- Literal use: put a newspaper's name in inline code (`The Miami Herald`).

#### 061. `usher`

- Kind: verb. Banned forms: `usher`, `ushers`, `ushered`, `ushering`.
- Why it reads as machine text: `usher in a new era` is a fixed phrase in generated history and tech writing. It credits one event with a large change and says nothing about the change itself. Models put it in the last paragraph of an essay to make it sound like a conclusion. Like `herald`, it is a word about ceremony, and ceremony is not a feature.
- Where it shows up: tech history posts, product announcements, keynotes, AI-written essays.

```slop
The iPhone ushered in a new era of mobile computing.
This update ushers in a faster, more intuitive experience.
We're ushering in the future of payments.
```

Replace with:

- `started` or `led to`, with what followed.
- Describe the change with a date and a number.
- `opened` or `began`, with a date, for an event that started something.
- Cut the phrase.

Rewrites:

```slop
The iPhone ushered in a new era of mobile computing.
```

After: Within five years of the 2007 iPhone, most new smartphones had a touch screen and no hardware keyboard.

```slop
This update ushers in a faster, more intuitive experience.
```

After: Pages open about twice as fast, and the menu has 6 items instead of 14.

```slop
We're ushering in the future of payments.
```

After: Pay by bank transfer at checkout; the money arrives in seconds and the fee is 0.5%.

- Literal use: for theaters and weddings, write "show to their seats" or "guide".

#### 062. `elucidate`

- Kind: verb. Banned forms: `elucidate`, `elucidates`, `elucidated`, `elucidating`.
- Why it reads as machine text: Academic register for "explain", rare outside journal articles, which is why it stands out in a README or a chat answer. Models use it to sound scholarly (`to elucidate this concept`). It promises a clear explanation and often comes before a muddy one. A writer who explains well rarely announces it first.
- Where it shows up: academic abstracts, documentation intros, AI chat answers, technical essays.

```slop
To elucidate this concept, consider the following example.
This paper elucidates the mechanisms of memory consolidation.
Allow me to elucidate the differences between these approaches.
```

Replace with:

- `explain`, `show`, `clarify`.
- In papers, state the mechanism found.
- Cut the lead-in and give the example.

Rewrites:

```slop
To elucidate this concept, consider the following example.
```

After: Take a function that calls its callback twice.

```slop
This paper elucidates the mechanisms of memory consolidation.
```

After: This paper reports that mice whose sleep spindles were blocked after training remembered the maze worse the next day.

```slop
Allow me to elucidate the differences between these approaches.
```

After: Polling asks the server every 5 seconds; webhooks send a request only when something changes.

- Literal use: there is no other sense; write "explain".

#### 063. `disrupt`

- Kind: verb. Banned forms: `disrupt`, `disrupts`, `disrupted`, `disrupting`, `disruption`, `disruptor`.
- Why it reads as machine text: Clayton Christensen's theory from the 1990s described cheap products that take a market from below. Startup culture turned it into "change an industry", and models use it for any new company. It claims a market effect that has not happened yet; `disruptive` has its own entry. Incumbents in the markets it names usually still lead them years later.
- Where it shows up: pitch decks, startup About pages, tech news, conference talk titles.

```slop
We're disrupting the insurance industry.
A startup poised to disrupt healthcare.
Disrupt the status quo with bold ideas.
```

Replace with:

- Say what you sell, to whom, at what price, against the old option.
- `compete with`, with the competitor's name.
- `replace`, when buyers drop an old product for yours; give the count.
- Cut it.

Rewrites:

```slop
We're disrupting the insurance industry.
```

After: Renters insurance from $5 a month, bought in 2 minutes on your phone, with claims paid by bank transfer.

```slop
A startup poised to disrupt healthcare.
```

After: A startup that sells blood tests directly to patients at a third of the clinic price.

```slop
Disrupt the status quo with bold ideas.
```

After: Each quarter, pitch one change to how we work; we try the most voted one for a month.

- Literal use: for interruptions such as an outage or a strike, write "interrupt", "stop", or "delay", with the duration.

#### 064. `level up`

- Kind: phrasal verb. Banned forms: `level up`, `levels up`, `leveled up`, `levelled up`, `leveling up`.
- Why it reads as machine text: Video game slang that marketing and coaching copy adopted for "improve", and models put it in titles (`Level up your CSS`). It implies a discrete jump in skill from reading one post. It sounds casual while saying nothing about what the reader will be able to do. In job ads it turns a promotion path into a game and hides the criteria.
- Where it shows up: tutorial titles, newsletter subject lines, course ads, video thumbnails.

```slop
Level up your CSS skills with these 5 tips.
Ready to level up your career?
This course will help you level up as a developer.
```

Replace with:

- Name the skill: "write grid layouts without media queries".
- `learn` or `get better at`, with the topic.
- Cut it and state the outcome.

Rewrites:

```slop
Level up your CSS skills with these 5 tips.
```

After: Five CSS grid techniques for layouts that work without media queries.

```slop
Ready to level up your career?
```

After: A 6-week course on system design interviews, with 4 mock interviews.

```slop
This course will help you level up as a developer.
```

After: After this course you can profile a slow Node service and find the hot function.

- Literal use: in a game's own UI, quote the string in inline code (`LEVEL UP`); in prose, write "reached level 12".

#### 065. `dive into`

- Kind: phrasal verb. Banned forms: `dive into`, `dives into`, `dived into`, `dove into`, `diving into`.
- Why it reads as machine text: It is the tutorial opener of generated text: `Let's dive into the code`. It adds a burst of energy and delays the first useful sentence. Its sibling `let's dive` is banned too, and readers have seen both often enough that they mark the whole post. Video scripts use it as a transition between a sponsor read and the content.
- Where it shows up: blog posts, tutorial intros, video scripts, AI chat answers.

```slop
Let's dive into the code.
In this tutorial, we'll dive into React Server Components.
Before we dive into the details, here's a quick overview.
```

Replace with:

- `cover`, `look at`, `explain`.
- If an overview is needed, give it without the announcement.
- Cut it and show the code.

Rewrites:

```slop
Let's dive into the code.
```

After: The order handler is in `src/routes/order.ts`.

```slop
In this tutorial, we'll dive into React Server Components.
```

After: This tutorial builds a product page with React Server Components and streams the reviews in last.

```slop
Before we dive into the details, here's a quick overview.
```

After: The service has three parts: the API, the job queue, and the worker.

- Literal use: for swimming, write "dive in" or "jump in".

#### 066. `deep dive`

- Kind: noun and verb phrase. Banned forms: `deep dive`, `deep dives`, `deep-dive`, `deep diving`.
- Why it reads as machine text: Consulting and podcast language for "detailed look", now the title of a large share of generated technical posts. It sets an expectation of depth that a 900-word post rarely meets. It also says nothing about which part gets the detail. In calendars it marks a meeting with no agenda.
- Where it shows up: post titles, meeting agenda items, talk titles, Slack messages.

```slop
A deep dive into PostgreSQL indexing.
Let's schedule a deep dive on the Q3 numbers.
Deep dive: how we scaled to 1M users.
```

Replace with:

- Name the scope: "how B-tree, GIN, and BRIN indexes store data".
- `review`, `walkthrough`, `meeting` for calendar items.
- Cut it from titles; the topic is the title.

Rewrites:

```slop
A deep dive into PostgreSQL indexing.
```

After: How PostgreSQL B-tree, GIN, and BRIN indexes store rows on disk.

```slop
Let's schedule a deep dive on the Q3 numbers.
```

After: 30-minute meeting Thursday: why Q3 churn rose from 3% to 5%.

```slop
Deep dive: how we scaled to 1M users.
```

After: How we went from 1 database to 8 shards at 1M users.

- Literal use: for scuba, write "a dive below 30 m".

#### 067. `lean into`

- Kind: phrasal verb. Banned forms: `lean into`, `leans into`, `leaned into`, `leant into`, `leaning into`.
- Why it reads as machine text: Self-help and startup language for "accept and do more of", common since the 2013 book "Lean In". Models use it as advice for anything uncomfortable or distinctive: `lean into the discomfort`, `lean into your strengths`. It gives an attitude and no action. It turns a decision with costs into a mood, so nobody discusses the costs.
- Where it shows up: career advice, brand strategy, retrospectives, design critiques.

```slop
Lean into your strengths as a designer.
We decided to lean into the retro aesthetic.
Lean into the discomfort of learning something new.
```

Replace with:

- `focus on`, `do more of`, `commit to`, with the specific choice.
- Name what you will stop doing to make room.
- Cut it and state the plan.

Rewrites:

```slop
Lean into your strengths as a designer.
```

After: Take the projects that need typography and turn down the ones that need 3D.

```slop
We decided to lean into the retro aesthetic.
```

After: We kept the pixel font and the 4-color palette across the site, the app, and the packaging.

```slop
Lean into the discomfort of learning something new.
```

After: Practice for 30 minutes a day and expect the first two weeks to feel slow.

- Literal use: for the body, write "lean against" or "lean forward".

#### 068. `reach out`

- Kind: phrasal verb. Banned forms: `reach out`, `reaches out`, `reached out`, `reaching out`.
- Why it reads as machine text: It is the default contact verb in generated emails and support copy: `feel free to reach out`. It is softer than "contact" or "email" and says nothing about the channel. Readers then have to hunt for the address themselves. Corporate email spread it, and models learned it from millions of support replies.
- Where it shows up: email sign-offs, support pages, README footers, sales emails.

```slop
Feel free to reach out if you have any questions.
I'm reaching out to see if you'd be interested in a quick call.
Reach out to our team for enterprise pricing.
```

Replace with:

- `email`, `call`, `message`, `open an issue`, with the address or link.
- `contact` when the channel varies.
- `ask`, when you want something from the reader; say what.
- Cut the polite closer and give the address.

Rewrites:

```slop
Feel free to reach out if you have any questions.
```

After: Send questions to support@example.com; we reply within one working day.

```slop
I'm reaching out to see if you'd be interested in a quick call.
```

After: I would like 20 minutes on Tuesday or Wednesday to show you how we handle invoice reminders.

```slop
Reach out to our team for enterprise pricing.
```

After: For more than 100 seats, email sales@example.com for a quote.

- Literal use: for the arm, write "reach for" or "hold out a hand".

#### 069. `weave`

- Kind: verb. Banned forms: `weave`, `weaves`, `weaved`, `weaving`, `wove`, `woven`.
- Why it reads as machine text: A textile image models use for combining things: `weave together data and design`, `seamlessly woven into your workflow`. It sounds handmade and hides how the parts connect. It belongs to the same family as `tapestry`, which is also banned. When a writer says a value is built into everything, ask where it is checked; if no step checks it, the claim is decoration.
- Where it shows up: writing advice, product pages, essay intros, portfolio case studies.

```slop
We weave data and storytelling into every report.
Accessibility is woven into everything we build.
The novel weaves together three generations of one family.
```

Replace with:

- `combine`, `include`, `connect`, with how.
- For processes, name the step where it happens.
- For fiction, describe the structure.

Rewrites:

```slop
We weave data and storytelling into every report.
```

After: Each report has a chart, a two-paragraph explanation, and one recommended action.

```slop
Accessibility is woven into everything we build.
```

After: Every PR runs axe checks, and every new component gets a keyboard test before review.

```slop
The novel weaves together three generations of one family.
```

After: The novel alternates chapters between a grandmother in 1950, her daughter in 1980, and her granddaughter in 2015.

- Literal use: for textiles and baskets, write "interlace the threads" or put the term in inline code (`weaving`).

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
