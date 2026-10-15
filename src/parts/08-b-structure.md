### 8.4 Tells of layout

Structure carries tells too. A page can contain no banned word and no false contrast and still look generated because every answer is a bulleted list with bold labels under a title-case heading that makes a pun.

#### Bulleted everything

Every explanation becomes a list. Reasons, arguments and stories get broken into fragments with no connectives, so "because", "so" and "but" disappear and the reader has to rebuild the logic. Lists nest three levels deep. Some bullets hold a single word.

Chat interfaces render Markdown, and assistants were tuned to be "scannable", so lists became the default container for any content. Lists also hide missing logic: two fragments placed next to each other imply a relationship the writer never had to state.

```slop
Benefits:
- Faster invoicing
- Better cash flow
- Happier clients
- Peace of mind

Why we changed the pricing:
- Costs
  - Infrastructure
  - Support
- Fairness
- Simplicity
```

```text
We raised the Team plan from $12 to $15 per seat because storage costs doubled after we moved backups to a second region. Solo stays at $8. Existing customers keep their current price until March 2027.
```

Rule: use a list only when the items are parallel and independent: steps in order, requirements, options, specifications. Reasons, trade-offs and history go in sentences joined by "because", "so" and "but". A one-item list is a sentence. If list items run past two lines each, they are paragraphs.

#### Bold-label bullets

Each bullet starts with a bolded label and a colon, followed by a sentence that restates the label: `Speed: Tidemark is blazing fast.` The label and the sentence say the same thing twice. In chat answers and generated READMEs this is the default list format, and it is easy to spot from across a room.

Assistants produce it because it looks organized in a chat window and gives each item an apparent heading. It also lets the model generate a list of abstract nouns first and fill in sentences after.

```slop
- **Speed:** Tidemark is blazing fast.
- **Security:** Your data is protected with enterprise-grade security.
- **Simplicity:** An intuitive interface anyone can use.
- **Support:** Our team is here to help 24/7.
```

```text
- Pages load in under a second on a 4G connection.
- Data is encrypted at rest with AES-256 and backed up hourly to a second region.
- Support answers within 4 hours, Monday to Friday, 08:00 to 18:00 CET.
```

Rule: drop the label when the sentence already says it. Keep labels only in reference material where readers scan for a term (options, parameters, glossary entries), and then use a table or a definition list instead of bold text in a bullet.

#### Title case everywhere

Headings, buttons, navigation items, menu entries and toasts all in title case: "Get Started With Your Free Trial", "Manage Team Settings", "Your Invoice Has Been Sent Successfully". It reads as a press release and makes interface text look shouted.

Marketing templates and headline style guides use title case, and models apply it to anything that looks like a heading or a label. Component libraries reinforce it, since their demo buttons say "Sign Up" and "Learn More".

```slop
Get Started With Your Free Trial
Manage Your Team Settings
Your Invoice Has Been Sent Successfully
Frequently Asked Questions
```

```text
Start a free trial
Team settings
Invoice sent
Questions about billing
```

Rule: sentence case for all interface text and all headings. Capitalize the first word and proper nouns only. Product names and legal names keep their registered form.

#### Headings that are puns

Clever headings that hide what the section contains: `Show Me the Money`, `Sync or Swim`, `Where the Magic Happens`, `Ctrl+Alt+Delight`. A reader scanning headings to find the pricing section cannot tell which one it is.

Asked to be "fun" or "memorable", a model reaches for an idiom or a pop-culture line and bends it toward the topic. It picks the most predictable pun available, which is why the same ones appear on thousands of pages.

```slop
Show Me the Money
Sync or Swim
Where the Magic Happens
Ctrl+Alt+Delight
Invoice, Invoice, Baby
```

```text
Pricing
Offline sync
How payment matching works
Keyboard shortcuts
Recurring invoices
```

Rule: a heading names what the section contains, so a reader who sees only the headings can find what they need. If a joke belongs anywhere, it goes in the body, written by a person, once per page.

### 8.5 Punctuation and formatting rules

These rules apply to interface copy, marketing pages, documentation, commit messages and this handbook. The linter enforces the first three.

#### Dashes

- No em dash (U+2014) and no en dash (U+2013), anywhere, including code comments and alt text.
- A break between two thoughts is a period. A pause is a comma. An aside is in parentheses. A list, example or definition follows a colon.
- Ranges use "to": "9:00 to 17:00", "pages 4 to 9", "$8 to $15 per seat". In tables, "to" also works: "1 to 5 users".
- The hyphen stays for compound modifiers ("14-day trial"), ISO dates (2026-10-15), identifiers (INV-0042) and code.
- Negative numbers in financial tables use a minus sign or parentheses, never a dash. Pick one convention per product.

#### Exclamation marks

- Zero in interface copy. That includes success messages, empty states, onboarding, and above all error messages, where an exclamation mark reads as alarm or mockery.
- Zero in marketing headlines and buttons.
- Zero in documentation and commit messages.
- Personal email from a named person to a customer may contain one, if that person would write one. Never more than one per message.
- User-generated content is displayed as written.

#### Emoji

- None in interface text, headings, buttons, navigation, toasts, commit messages, PR titles, changelogs or docs.
- None as bullet markers, status indicators or section icons. A green circle is not a status; the word "Running" next to a 16px SVG icon is.
- None in code comments or log output. Logs are searched with grep; pictographs break searches and alignment.
- Icons come from one SVG set at 16 or 20px with a 1.5px stroke, always next to a text label or with an accessible name.
- Emoji typed by users (messages, reactions, names) are content. Render them unchanged. A reactions feature is a feature; decorating your own copy with emoji is a tell.

#### Bold and italics

- At most one bold phrase per screen of body text, and never a whole sentence.
- In step-by-step documentation, bold the visible name of a control the reader must find: "Select **Send invoice**." That is the only routine use.
- No bold labels at the start of bullets (see 8.4).
- Italics mark a term at the point where it is defined, or a title. Never use italics for emphasis in interface copy; screen readers ignore it and many fonts render it faintly.
- No underline except on links. No all-caps words for emphasis.

#### Headings

- Sentence case, no trailing period, under 8 words.
- A heading is a noun phrase ("Payment reminders") or an imperative ("Connect your bank"). Questions only on FAQ pages, where each heading is a question a customer actually asked.
- No colon subtitles ("Invoicing: A Complete Guide"). Pick the half that names the content.
- No skipped levels. One `h1` per page. Visual size follows the type scale (40, 32, 24, 21px for `h1` to `h4` on desktop), not the heading level alone.
- Never use a heading for emphasis. If text is not the title of the content below it, it is not a heading.

#### Lists

- Numbered lists for sequences the reader follows in order. Bulleted lists for unordered sets. Prose for everything else.
- 2 to 9 items. Over 9, group them under subheadings or use a table.
- Items are grammatically parallel: all imperatives, all noun phrases, or all full sentences.
- Fragments take no final period. Full sentences take periods. Do not mix the two in one list.
- Nest at most one level. A second level of nesting means the content wants a table or subheadings.
- No introductory sentence that says "The following list shows". The heading or the sentence before already does that.

#### Quotation marks, ellipses and ampersands

- Interface and marketing text uses typographic quotes and apostrophes. Code, config and commit messages use straight ones. Never mix the two in the same string.
- The ellipsis means "this continues" or "text was removed". Use it in loading text for an operation in progress ("Importing…") and in a menu item that opens a dialog ("Export…"). Never use it for suspense, and never trail a sentence off with one.
- "And" in prose and headings. The ampersand is for proper names (Hollis & Reed) and space-starved table headers.
- Slashes for real alternatives only ("and/or" is not one). Write "invoices or quotes".

#### Capitals and numbers in text

- Acronyms stay uppercase (PDF, VAT, API). Everything else is sentence case, including small uppercase labels: an eyebrow line set in caps with letter spacing above every heading is a template tell, and the heading should stand alone.
- No "NEW", "BETA" or "LIVE" pills. If something is new, say what changed and when in the release notes; if something is live, show the timestamp of the last update.
- Write numbers as digits in interface copy, including one to nine: "3 invoices", "2 minutes". Prose in long-form documents may spell out one to nine. Pick one rule per document and keep it.

### 8.6 Microcopy for controls and forms

Microcopy is the text inside the interface: button labels, field labels, messages. It is short, so every word shows. Generated microcopy is easy to spot because it is cheerful at the wrong moments and vague at the useful ones. Each context below gives the default slop, the rules, and a rewrite.

#### Buttons and calls to action

Generated buttons use generic verbs (`Submit`, `Continue`, `Get started`) or benefit slogans (`Unlock your potential`). Neither tells the person what will happen when they press it.

- Verb plus object, 1 to 3 words, sentence case: "Create invoice", "Send 3 reminders", "Export CSV".
- The label says what happens next. "Start 14-day trial" is better than "Get started" unless the next screen is the start of something.
- A dialog's primary button repeats the dialog's verb. A dialog titled "Delete invoice?" has a button labeled "Delete invoice".
- Name the count and the object on bulk and destructive actions: "Delete 12 invoices".
- Link text says where it goes: "Read the pricing FAQ", never "Click here" or a bare "Learn more".
- No arrow glyphs, no "->" appended to the label, no exclamation marks, no first-person mix ("Start my trial" next to "Your account").
- One primary button per view. A page with three filled accent buttons has no primary action.

```slop
Get Started
Submit
Unlock Your Potential
Let's Go!
Learn More ->
[Yes] [No]
```

```text
Create invoice
Send 3 reminders
Start 14-day trial
Read the pricing FAQ
[Delete invoice] [Keep invoice]
```

#### Form labels and help text

Generated forms put instructions in placeholders, mark every field with an asterisk, and open help text with "Please". Placeholders vanish on the first keystroke, so the instruction disappears at the moment the person needs it.

- The label is a short noun phrase above the field: "Work email", not "Enter your email address".
- Never use a placeholder as the label. A placeholder may show an example format, prefixed "e.g.", in `--ink-3`.
- Help text sits under the field, in 14px `--ink-2`, and states constraints before the person breaks them: "At least 12 characters."
- If most fields are required, mark the optional ones with "(optional)" and drop the asterisks.
- Explain why you ask for data people hesitate to give: "We send receipts here." under an email field, "Used only for tax on EU invoices." under a VAT number.
- No "Please", no exclamation marks, no adjectives about the input ("strong", "awesome").

```slop
Label: Enter your email address here
Placeholder: Your amazing project name...
Help: Please make sure your password is strong and secure!
Label: Company Name*
```

```text
Label: Work email
Help: We send invoices and receipts here.

Label: Project name
Placeholder: e.g. Q3 audit for Hollis & Reed

Label: Password
Help: At least 12 characters.

Label: VAT number (optional)
Help: Used only for tax on EU invoices.
```

#### Error messages

Generated errors are either cute (`Oops! Something went wrong`) or raw (`Error 422: Unprocessable Entity`). The cute ones hide the cause; the raw ones expose it in a language the person does not speak. Both leave them stuck.

- Structure: what failed, why (if known), what to do now. Usually two short sentences.
- Place the message next to the field or control that failed, in `--bad`, with an icon and text. Color alone is not enough.
- Use the person's terms ("card", "file", "date"), not the system's ("payload", "entity", "token").
- No blame ("You entered an invalid date"). State the requirement instead ("Enter a date after 1 January 2026").
- No apology theatre and no jokes. "Sorry" is allowed once, when the failure is ours.
- Keep what the person typed. Never clear a form because one field failed.
- Include an error code after the human text when support will need it.

```slop
Oops! Something went wrong.
Invalid input.
Uh-oh, looks like we hit a snag. Please try again later!
Error 422: Unprocessable Entity
We're sorry, but an unexpected error has occurred.
```

```text
Card declined. Your bank did not give a reason. Try another card or call your bank.
Enter a date after 1 January 2026.
Not saved. You are offline. Your changes are kept on this device and save when you reconnect.
The file is 14 MB. The limit is 10 MB.
Sorry, this failed on our side (error 5021). Try again in a minute. If it fails again, email support@tidemark.example and include the code.
```

#### Empty states

The generated empty state is a large illustration, a joke ("It's lonely in here"), and a button that says "Get started". The person learns nothing about what the screen is for.

- Say what will appear here and how it gets here, in one or two sentences.
- Offer the one action that fills the screen, as a single button.
- Separate three cases: first use (nothing created yet), cleared (everything done), and no results (a search or filter matched nothing). For no results, repeat the query and offer to clear the filters.
- No illustrations of floating people, no "Nothing to see here", no "yet" with an exclamation mark.
- An empty table keeps its column headers, so the person sees what data will appear.

```slop
Nothing to see here... yet!
It's a little lonely in here. Let's change that!
Your journey starts now. Create your first masterpiece.
No data
```

```text
No invoices yet. Invoices you create or import appear here.
[Create invoice]

No results for "hollis". Check the spelling or clear the Paid filter.
[Clear filters]

No reminders due. A reminder appears here when an invoice is 7 days late.
```

#### Confirmation dialogs

Generated confirmations ask "Are you sure?" and offer "OK" and "Cancel". The person has to remember what they clicked to know what "OK" will do.

- The title names the action and the object as a question: "Delete invoice INV-0042?"
- The body states the consequence and whether it can be undone, with counts: "The invoice and its 3 payment records are deleted."
- Buttons repeat the verb: "Delete invoice" and "Cancel". Never "Yes", "No" or "OK".
- For reversible actions, skip the dialog. Do the action and offer Undo for at least 10 seconds.
- For actions that destroy a workspace or an account, ask the person to type the name of the thing.
- The destructive button uses `--bad`, not the accent color, and it is not the default focus.

```slop
Are you sure?
This action cannot be undone. Are you sure you want to proceed?
[OK] [Cancel]

Whoa there! Are you really, really sure?
```

```text
Delete invoice INV-0042?
The invoice and its 3 payment records are deleted. Your client keeps the PDF they already received. This cannot be undone.
[Delete invoice] [Cancel]

Archived 12 invoices. [Undo]
```

#### Loading text

Generated loading text tries to entertain: rotating jokes, `Hang tight`, `Working our magic`. The jokes repeat on the third visit, and none of them tell the person how long to wait.

- Under 1 second: show nothing. A spinner that flashes for 200ms reads as a glitch.
- 1 to 3 seconds: a skeleton or a 16px spinner, no text.
- Over 3 seconds: one line saying what is happening, in the present participle: "Importing clients…"
- Over 10 seconds: show progress as a count or a percentage and let the person leave the page. Say how they will learn it finished.
- No jokes, no rotating messages, no "Almost there" when you do not know that.

```slop
Hang tight! We're working our magic...
Brewing something special for you...
Almost there! Good things take time.
Reticulating splines...
```

```text
Importing clients… 140 of 240
Generating 12 PDFs. You can leave this page. We will email you when they are ready.
Checking the bank feed. This usually takes under 10 seconds.
```

#### Success messages

Generated success messages celebrate: `Success!`, `Woohoo! Your invoice is on its way!`, confetti for saving a form. Routine actions do not need celebration, and celebrating them makes the rare real milestone feel the same.

- Past-tense verb and object, 1 to 4 words: "Invoice sent", "Changes saved".
- Add the one next fact or action when it helps: who received it, where to find it, an Undo.
- Autosave shows "Saved" next to the control or in the header, not a toast.
- A toast stays at least 5 seconds, 10 if it contains an action, and pauses while hovered or focused.
- No exclamation marks, no "Success", no "successfully" (the past tense already says it worked), no confetti.

```slop
Success!
Woohoo! Your invoice is on its way!
Awesome! Changes saved successfully.
You did it! Your profile is looking great.
```

```text
Invoice sent to dana@hollis.example. [View]
Saved
Logo updated. Clients see it on invoices you send from now on.
```
