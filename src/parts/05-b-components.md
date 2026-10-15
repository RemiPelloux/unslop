### 5.6 Progress bars and steppers

#### What the machine produces

```slop
<div className="w-full rounded-full bg-gray-200 h-3 overflow-hidden">
  <div className="h-3 rounded-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 animate-pulse bg-[length:200%] shadow-[0_0_12px_rgba(139,92,246,0.6)]" style={{ width: '75%' }} />
</div>
<span className="mt-2 inline-block rounded-full bg-indigo-50 px-3 py-1 text-xs font-medium text-indigo-600">75% Complete</span>

<ol className="flex items-center">
  <li className="flex items-center"><span className="flex h-10 w-10 items-center justify-center rounded-full bg-gradient-to-r from-indigo-500 to-purple-600 text-white"><CheckIcon /></span><div className="h-0.5 w-24 bg-gradient-to-r from-indigo-500 to-purple-600" /></li>
  <li><span className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-200">3</span></li>
</ol>
```

The bar is the `rounded-full` progress from shadcn with a three-stop gradient, a pulse animation, and a purple glow. The percent pill reports a number with no unit of work behind it. The stepper is the Tailwind UI "Circles with text" pattern with the labels removed, so the user sees three numbered dots and no idea what step 3 is.

#### Rules

1. Use a determinate bar only when the fraction is real. If you cannot count the work, show a sentence with a count of what is done so far: "Imported 3,120 rows".
2. Bars are 4px tall inline and 8px tall as a page-level indicator. Track `--paper-3`, fill `--ink`. Radius 0 or `--radius`.
3. Show units of work, not only percent: "312 of 1,240 rows". Add time remaining only when your estimate is right within 20%.
4. Use the native `<progress>` element, or `role="progressbar"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax` and an accessible name.
5. Move the fill with `transform: scaleX()` over 150ms or less. No stripes, no pulse, no shimmer.
6. Announce progress to screen readers at 25%, 50%, 75% and done through a polite live region, not on every tick.
7. Steppers have at most 5 steps. Every step shows its label at all times. Current step text is weight 600 with a 2px `--ink` underline.
8. Completed steps are links back. Future steps are plain text until they are reachable.
9. Below 600px, collapse the stepper to one line: "Step 2 of 4: Billing".

#### Reference build

```html
<div class="prog">
  <label for="imp" class="prog-label">Importing transactions</label>
  <progress id="imp" max="1240" value="312">312 of 1,240</progress>
  <p class="prog-count">312 of 1,240 rows</p>
</div>

<ol class="steps" aria-label="Checkout">
  <li class="done"><a href="/checkout/account">1. Account</a></li>
  <li aria-current="step">2. Billing</li>
  <li>3. Review</li>
</ol>
<p class="steps-compact">Step 2 of 3: Billing</p>
```

```css
.prog { max-width: 480px; }
.prog-label { display: block; font-size: 14px; font-weight: 600; margin-bottom: 8px; }
.prog progress { appearance: none; display: block; width: 100%; height: 8px; border: 0; border-radius: var(--radius); background: var(--paper-3); color: var(--ink); }
.prog progress::-webkit-progress-bar { background: var(--paper-3); border-radius: var(--radius); }
.prog progress::-webkit-progress-value { background: var(--ink); border-radius: var(--radius); }
.prog progress::-moz-progress-bar { background: var(--ink); }
.prog-count { margin: 8px 0 0; font-size: 14px; color: var(--ink-2); font-variant-numeric: tabular-nums; }

.steps { display: flex; gap: 32px; list-style: none; margin: 0; padding: 0; border-bottom: 1px solid var(--rule); font-size: 14px; }
.steps li { padding: 12px 0; color: var(--ink-3); }
.steps li.done a { color: var(--ink-2); }
.steps li[aria-current="step"] { color: var(--ink); font-weight: 600; border-bottom: 2px solid var(--ink); margin-bottom: -1px; }
.steps-compact { display: none; font-size: 14px; font-weight: 600; }
@media (max-width: 600px) { .steps { display: none; } .steps-compact { display: block; } }
```

#### States

- Indeterminate: no bar. A 16px stroked spinner plus a count sentence, or the sentence alone.
- Paused: bar stays, text reads "Paused at 312 of 1,240 rows. Resume".
- Failed: fill turns `--bad`, text names the row or file that failed and offers "Retry from row 313".
- Done: replace the bar with a sentence and the next action: "Imported 1,240 rows. Review duplicates (4)".

#### Copy

```slop
75% Complete
Almost there! Hang tight while we work our magic...
Step 2
You're crushing it!
```

- 312 of 1,240 rows
- About 2 minutes left
- Step 2 of 3: Billing
- Imported 1,240 rows. Review duplicates (4)

#### Checklist

- Determinate only when the work is countable.
- 4px or 8px, `--ink` on `--paper-3`, no stripes or glow.
- Count of real units beside the bar.
- Stepper labels always visible, 5 steps or fewer.
- Compact stepper text below 600px.

### 5.7 Search

#### What the machine produces

```slop
<div className="relative mx-auto max-w-2xl">
  <div className="absolute -inset-1 rounded-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 opacity-30 blur-lg" />
  <div className="relative flex items-center rounded-full bg-white/90 px-6 py-4 shadow-xl backdrop-blur">
    <MagnifyingGlassIcon className="h-5 w-5 text-gray-400" />
    <input className="ml-3 flex-1 bg-transparent outline-none" placeholder="Search anything..." />
    <kbd className="rounded-md border px-2 py-1 text-xs text-gray-400">Cmd K</kbd>
    <button className="ml-2 flex items-center gap-1 rounded-full bg-gradient-to-r from-violet-500 to-fuchsia-500 px-4 py-2 text-sm text-white">
      <SparklesIcon className="h-4 w-4" /> Ask AI
    </button>
  </div>
</div>
```

This is the docs-site search from the Algolia DocSearch and Mintlify defaults, inflated into a hero element. A blurred gradient glow sits behind a pill input, `outline-none` removes the focus ring, the placeholder promises "anything", and an "Ask AI" button with a sparkle sits inside the field so that the Enter key has two possible meanings.

#### Rules

1. Inputs are 36px tall in toolbars and 40px as a page's main search. 1px `--rule` border, `--radius` corners, 16px stroked icon inset 12px from the left.
2. The input has a label: visible, or `aria-label` when the icon and placement make the purpose obvious. Wrap it in `<search>` or `<form role="search">`.
3. The placeholder names what is searchable: "Search invoices by number, customer or amount". Never "Search anything".
4. Live results update 200ms after the last keystroke. Searches that hit a server show results after 300ms and keep the previous results visible while loading.
5. Report the count in a polite live region: "14 results for acme". When filters are on, say how many: "14 results, 2 filters on".
6. Mark matched text with `<mark>` styled as `--paper-3` background, `--ink` text, weight 600. Not yellow.
7. Show a keyboard shortcut as text in `<kbd>`: "/" or "Ctrl K" ("Cmd K" on macOS). Hide it on touch devices with `@media (hover: none)`.
8. Command palettes are 640px wide, placed 12vh from the top, over an overlay of `rgb(26 26 24 / 0.4)` with no blur. Rows are 36px. Show at most 8 rows before scrolling.
9. Escape closes the palette and returns focus to the element that opened it. Arrow keys move the active row. Enter runs it. The pattern is a combobox (see 5.8).

#### Reference build

```html
<search class="search">
  <form action="/invoices" method="get">
    <label for="q" class="sr-only">Search invoices</label>
    <svg class="i search-icon" aria-hidden="true"><use href="#i-search"/></svg>
    <input id="q" name="q" type="search" autocomplete="off"
           placeholder="Number, customer or amount" value="acme">
    <kbd class="search-key">/</kbd>
  </form>
</search>
<p class="search-count" role="status">14 results for "acme"</p>
<ul class="results">
  <li><a href="/invoices/2041"><mark>Acme</mark> Freight, INV-2041, $4,120.00</a></li>
</ul>
```

```css
.search form { position: relative; max-width: 480px; }
.search input {
  width: 100%; height: 40px; padding: 0 40px 0 36px;
  border: 1px solid var(--rule); border-radius: var(--radius);
  background: var(--paper); color: var(--ink); font: 16px var(--font-sans);
}
.search input::placeholder { color: var(--ink-3); }
.search input:hover { border-color: var(--ink-3); }
.search input:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; border-color: var(--ink); }
.search-icon { position: absolute; left: 12px; top: 12px; color: var(--ink-3); pointer-events: none; }
.search-key { position: absolute; right: 8px; top: 8px; padding: 2px 6px; border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper-2); font: 12px var(--font-mono); color: var(--ink-2); }
@media (hover: none) { .search-key { display: none; } }
.search-count { margin: 12px 0 8px; font-size: 14px; color: var(--ink-2); }
.results { list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--rule); }
.results a { display: block; padding: 12px 0; border-bottom: 1px solid var(--rule); color: var(--ink); text-decoration: none; }
.results a:hover { background: var(--paper-2); }
.results mark { background: var(--paper-3); color: var(--ink); font-weight: 600; }
```

#### States

- Empty input: show recent searches or nothing. No "Try searching for something awesome".
- Typing: previous results stay at full opacity until new ones arrive.
- No results: repeat the query, offer to clear filters, offer the closest action: "No invoices match "acme ltd". Clear 2 filters, or create a customer named Acme Ltd."
- Error: "Search is not responding. Your filters still work." Keep filters usable.

#### Copy

```slop
Search anything...
Ask AI
No results found. Try a different search!
Oops, we couldn't find what you're looking for.
```

- Number, customer or amount
- 14 results for "acme"
- No invoices match "acme ltd". Clear 2 filters.
- Recent: INV-2041, Harbor Supply, overdue

#### Checklist

- Input has a label and a visible focus ring.
- Placeholder lists the searchable fields.
- Count announced in a live region.
- `<mark>` in `--paper-3`, not yellow.
- No glow, no pill, no AI button inside the field.
- Palette has no blur and returns focus on Escape.

### 5.8 Selects and comboboxes

#### What the machine produces

```slop
<Listbox value={selected} onChange={setSelected}>
  <Listbox.Button className="relative w-full rounded-xl bg-white py-3 pl-4 pr-10 text-left shadow-md ring-1 ring-gray-200 focus:outline-none">
    <span className="text-gray-400">Select an option...</span>
    <ChevronUpDownIcon className="absolute right-3 top-3 h-5 w-5 text-gray-400" />
  </Listbox.Button>
  <Listbox.Options className="absolute mt-2 max-h-80 w-full overflow-auto rounded-xl bg-white/95 py-2 shadow-2xl ring-1 ring-black/5 backdrop-blur">
    {options.map(o => (
      <Listbox.Option key={o.id} value={o} className="ui-active:bg-gradient-to-r ui-active:from-indigo-500 ui-active:to-purple-500 ui-active:text-white mx-2 rounded-lg px-3 py-2">
        {o.name} <CheckIcon className="ui-selected:block hidden text-indigo-600" />
      </Listbox.Option>
    ))}
  </Listbox.Options>
</Listbox>
```

This is the Headless UI `Listbox` example as published, with a gradient active row added. It replaces a native `<select>` for a list of six options, removes the focus ring with `focus:outline-none`, and floats the list on `shadow-2xl` plus a blur. The placeholder "Select an option..." gives no hint of what the options are.

#### Rules

1. Use radio buttons for 2 to 5 options that fit on screen. Use a native `<select>` for 6 to 15 known options. Use a combobox above 15 options or when the user may type a value that is not in the list.
2. The closed field is 40px tall with a 1px `--rule` border, `--radius` corners, and a 16px stroked chevron 12px from the right edge.
3. The open list sits on `--paper` with a 1px `--ink` border. The darker border separates it from the page. It is at most 8 rows tall (8 x 32px), then scrolls.
4. Options are 32px tall with 12px side padding. The keyboard-active option gets `--paper-3`. The selected option gets a 16px stroked check SVG on the left and `aria-selected="true"`.
5. A combobox follows the ARIA 1.2 pattern: an `<input role="combobox">` with `aria-expanded`, `aria-controls` and `aria-activedescendant`, and a `role="listbox"` popup. Focus never leaves the input.
6. Filtering matches the start of any word, ignores case and accents, and bolds the matched part. Results appear within 100ms for local data.
7. When nothing matches, say so and offer to create the value if creation is allowed.
8. Multi-select shows chosen values as removable tokens, each with an accessible name such as "Remove Harbor Supply". Past 3 tokens, collapse to "Harbor, Acme and 4 more".
9. Prefer a sensible default over a placeholder. When there is no default, the placeholder names the choice: "Choose a currency".

#### Reference build

```html
<label for="cur" class="f-label">Currency</label>
<div class="select"><select id="cur"><option>EUR, Euro</option><option selected>USD, US dollar</option><option>GBP, Pound sterling</option></select></div>

<label for="cust" class="f-label">Customer</label>
<div class="cbx">
  <input id="cust" role="combobox" aria-expanded="true" aria-controls="cust-list"
         aria-autocomplete="list" aria-activedescendant="cust-2" value="har">
  <ul id="cust-list" role="listbox" class="cbx-list">
    <li id="cust-1" role="option" aria-selected="false"><b>Har</b>bor Supply</li>
    <li id="cust-2" role="option" aria-selected="true" class="active"><b>Har</b>low and Sons</li>
  </ul>
</div>
```

```css
.f-label { display: block; margin: 16px 0 4px; font-size: 14px; font-weight: 600; }
.select { position: relative; max-width: 320px; }
.select select, .cbx input {
  appearance: none; width: 100%; height: 40px; padding: 0 36px 0 12px;
  border: 1px solid var(--rule); border-radius: var(--radius);
  background: var(--paper); color: var(--ink); font: 16px var(--font-sans);
}
.select::after { content: ""; position: absolute; right: 14px; top: 15px; width: 6px; height: 6px; border: solid var(--ink-2); border-width: 0 1.5px 1.5px 0; transform: rotate(45deg); pointer-events: none; }
.select select:focus-visible, .cbx input:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.cbx { position: relative; max-width: 320px; }
.cbx-list { position: absolute; left: 0; right: 0; top: 44px; z-index: 20; max-height: 258px; overflow-y: auto; margin: 0; padding: 0; list-style: none; background: var(--paper); border: 1px solid var(--ink); border-radius: var(--radius); }
.cbx-list li { display: flex; align-items: center; height: 32px; padding: 0 12px; font-size: 14px; cursor: default; }
.cbx-list li.active { background: var(--paper-3); }
.cbx-list li[aria-selected="true"] { font-weight: 600; }
.cbx-list b { font-weight: 700; }
```

#### States

- Closed, open, keyboard-active option, selected option, disabled option (text `--ink-3`, `aria-disabled="true"`, still reachable by arrow keys).
- Loading remote results: keep the last list and add a row "Searching..." at the top. Do not clear the list.
- No match: one row, "No customer named "harx". Create Harx" when creation is allowed.

#### Copy

```slop
Select an option...
No results found :(
```

- Choose a currency
- No customer named "harx". Create Harx
- Harbor, Acme and 4 more

#### Checklist

- Radio, native select or combobox, chosen by option count.
- List on `--paper` with a 1px `--ink` border, 8 rows maximum.
- ARIA 1.2 combobox roles and `aria-activedescendant`.
- Focus ring kept. No blur, no gradient active row.

### 5.9 Settings pages

#### What the machine produces

```slop
<div className="grid grid-cols-2 gap-6">
  <div className="rounded-2xl bg-white p-6 shadow-lg">
    <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-gradient-to-br from-indigo-500 to-purple-600"><BellIcon className="text-white" /></div>
    <h3 className="font-semibold">Notifications</h3>
    <p className="text-sm text-gray-500">Manage how you receive updates</p>
    <Switch checked className="mt-4 bg-indigo-600 shadow-inner" />
  </div>
  ...
  <div className="col-span-2 rounded-2xl border border-red-200 bg-gradient-to-r from-red-50 to-pink-50 p-6">
    <h3 className="font-semibold text-red-600">Danger Zone</h3>
    <button className="mt-4 rounded-xl bg-red-600 px-4 py-2 text-white shadow">Delete</button>
  </div>
</div>
<div className="fixed bottom-6 right-6"><button className="rounded-full bg-gradient-to-r from-indigo-500 to-purple-600 px-6 py-3 text-white shadow-xl">Save changes</button></div>
```

This is the settings screen from a dashboard starter kit: a grid of cards, one per topic, each with an icon in a gradient circle and a vague description. A floating "Save changes" button sits beside switches that may or may not already have saved. The "Danger Zone" card is pink and the button inside says "Delete" without naming what is deleted.

#### Rules

1. Layout is a 200px section list on the left and a form column at most 640px wide on the right. Below 768px, the section list becomes its own page.
2. Each setting is a row: label 14px weight 600, description 14px `--ink-2` at most 66ch, control on the right or below. Rows are separated by a 1px `--rule` border with 24px vertical padding. No cards.
3. Pick one save model per section. Switches and selects apply at once and show "Saved" beside the control for 2000ms. Text fields save with a button at the end of their section. Never mix both in one section.
4. Switches are only for settings that apply at once. Inside a form that needs a save button, use checkboxes.
5. Destructive actions sit last, in their own section titled with the action ("Delete workspace"). The button is outlined in `--bad` and names the object. Confirmation asks the user to type the workspace name.
6. Every section and setting has an anchor (`#email-digest`), so support can link straight to it.
7. Workspace-level settings show who last changed them and when: "Changed by Priya Nair on 3 Oct".

#### Reference build

```html
<section id="email" aria-labelledby="email-h" class="set-sec">
  <h2 id="email-h">Email</h2>
  <div class="set-row">
    <div><p class="set-label" id="digest-l">Daily digest</p>
      <p class="set-desc" id="digest-d">One email at 08:00 with yesterday's payments and overdue invoices.</p></div>
    <button type="button" role="switch" aria-checked="true" class="switch" aria-labelledby="digest-l" aria-describedby="digest-d"><span></span></button>
    <span class="set-saved" role="status">Saved</span>
  </div>
</section>
```

```css
.set-sec { max-width: 640px; padding-bottom: 32px; }
.set-sec h2 { font-size: 18px; margin: 32px 0 0; padding-bottom: 12px; border-bottom: 1px solid var(--ink); }
.set-row { display: grid; grid-template-columns: 1fr auto; gap: 4px 24px; align-items: center; padding: 24px 0; border-bottom: 1px solid var(--rule); }
.set-label { margin: 0; font-size: 14px; font-weight: 600; }
.set-desc { margin: 4px 0 0; font-size: 14px; color: var(--ink-2); max-width: 66ch; }
.set-saved { grid-column: 2; font-size: 12px; color: var(--ok); justify-self: end; }
.set-saved:empty { display: none; }
.switch { position: relative; width: 36px; height: 20px; padding: 0; border: 1px solid var(--ink-3); border-radius: var(--radius); background: var(--paper-3); cursor: pointer; }
.switch span { position: absolute; top: 2px; left: 2px; width: 14px; height: 14px; border-radius: var(--radius); background: var(--paper); border: 1px solid var(--ink-3); transition: transform 120ms ease-out; }
.switch[aria-checked="true"] { background: var(--ink); border-color: var(--ink); }
.switch[aria-checked="true"] span { transform: translateX(16px); border-color: var(--ink); }
.switch:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) { .switch span { transition: none; } }
```

The switch is square, with the same 2px radius as every other control. The `rounded-full` pill track is a shadcn default, not a requirement.

#### States

- Saving: the "Saved" slot reads "Saving..." and the control stays enabled.
- Save failed: the control reverts, and the slot reads "Not saved. Retry" in `--bad`.
- Locked by an admin: control disabled, description adds "Set by your workspace owner."
- Unsaved text changes when leaving: one confirm dialog listing the fields that would be lost.

#### Copy

```slop
Danger Zone
Manage how you receive updates
Delete
Your preferences have been updated successfully!
```

- Delete workspace
- Daily digest. One email at 08:00 with yesterday's payments and overdue invoices.
- Saved
- Type "harbor-supply" to delete this workspace and its 1,284 invoices.

#### Checklist

- Rows with 1px borders, no cards, no icon circles.
- One save model per section.
- Switches only for settings that apply at once.
- Destructive section names the object and asks for typed confirmation.
- Anchors on every setting.

### 5.10 Sliders

#### What the machine produces

```slop
<div className="relative pt-8">
  <div className="absolute -top-1 left-[60%] -translate-x-1/2 rounded-lg bg-gradient-to-r from-indigo-500 to-purple-600 px-2 py-1 text-xs text-white shadow-lg">$600</div>
  <input type="range" className="h-2 w-full appearance-none rounded-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500
    [&::-webkit-slider-thumb]:h-6 [&::-webkit-slider-thumb]:w-6 [&::-webkit-slider-thumb]:appearance-none
    [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-white [&::-webkit-slider-thumb]:shadow-[0_0_0_4px_rgba(99,102,241,0.3)]" />
</div>
```

This is the custom range from a dozen Tailwind snippet sites: a three-stop gradient track, a white thumb ringed in an indigo glow, and a floating value bubble that sits exactly under the user's thumb on a phone. Most of these snippets paint the filled part of the track with a `linear-gradient` background that is recomputed on every input event.

#### Rules

1. Use a slider when relative position matters more than the exact number: volume, zoom, opacity, a rough budget. When the exact number matters, use a number input, or pair the slider with one.
2. Show the current value as text beside the label, in tabular numerals, with its unit: "Opacity 60%".
3. Track 4px tall, `--paper-3`. Thumb 16px with a 2px `--ink` border and `--paper` fill. The hit area is at least 24px tall on pointer devices and 44px on touch.
4. Use the native `<input type="range">` with `accent-color: var(--ink)`. Do not paint progress with a gradient background.
5. Label the ends with min and max in 12px `--ink-3`.
6. Keyboard: arrows move 1 step, Page Up and Page Down move 10 steps, Home and End go to the ends. The native input does this already.
7. Set `aria-valuetext` when the number alone is unclear: "60 percent", "3 days".
8. Avoid two-thumb ranges outside filters. In a filter, pair them with two number inputs labelled "Minimum" and "Maximum".
9. No floating value bubble. The value lives in the label.

#### Reference build

```html
<div class="rng">
  <div class="rng-head"><label for="op">Opacity</label><output for="op" id="op-out">60%</output></div>
  <input id="op" type="range" min="0" max="100" step="5" value="60" aria-valuetext="60 percent">
  <div class="rng-ends" aria-hidden="true"><span>0%</span><span>100%</span></div>
</div>
```

```css
.rng { max-width: 320px; font-size: 14px; }
.rng-head { display: flex; justify-content: space-between; margin-bottom: 4px; }
.rng-head label { font-weight: 600; }
.rng-head output { font-variant-numeric: tabular-nums; color: var(--ink); }
.rng input { width: 100%; height: 24px; margin: 0; accent-color: var(--ink); cursor: pointer; }
.rng input:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.rng-ends { display: flex; justify-content: space-between; font-size: 12px; color: var(--ink-3); }
@media (pointer: coarse) { .rng input { height: 44px; } }
```

```js
const r = document.getElementById('op'), o = document.getElementById('op-out');
r.addEventListener('input', () => { o.value = r.value + '%'; r.setAttribute('aria-valuetext', r.value + ' percent'); });
```

#### States

- Default, hover (cursor only), focus (2px outline), dragging (no change in thumb size), disabled (`--ink-3` label, `accent-color: var(--ink-3)`).
- Out of range typed value in the paired input: clamp on blur and say so under the field, "Maximum is 100%".
- Snapped steps: when only a few values are valid (1, 3, 7, 30 days), use a segmented control instead (see 5.11).

#### Copy

```slop
Drag to adjust
Slide to unlock your perfect budget
```

- Opacity 60%
- Budget per month, $200 to $5,000
- Maximum is 100%

#### Checklist

- Native range with `accent-color`, no gradient fill trick.
- Value and unit in the label.
- 24px hit area, 44px on touch.
- Paired number input when exact values matter.
- No floating bubble, no glow ring.

### 5.11 Tabs and segmented controls

#### What the machine produces

```slop
<Tabs defaultValue="overview">
  <TabsList className="relative rounded-full bg-gray-100 p-1 shadow-inner">
    <motion.div layoutId="pill" className="absolute inset-y-1 rounded-full bg-gradient-to-r from-indigo-500 to-purple-500 shadow-lg" />
    <TabsTrigger value="overview" className="relative z-10 rounded-full px-6 py-2 data-[state=active]:text-white">Overview</TabsTrigger>
    <TabsTrigger value="analytics" className="relative z-10 rounded-full px-6 py-2">Analytics</TabsTrigger>
  </TabsList>
</Tabs>
<div className="rounded-full bg-gray-100 p-1">
  <button className="rounded-full bg-white px-4 py-1 shadow">Monthly</button>
  <button className="rounded-full px-4 py-1">Yearly <span className="ml-1 rounded-full bg-emerald-100 px-2 text-xs text-emerald-700">-20%</span></button>
</div>
```

This is the shadcn `Tabs` component with a Framer Motion `layoutId` pill sliding between triggers, a pattern copied from a popular Vercel demo. Tabs and segmented control end up looking identical, so the reader cannot tell "switch the whole view" from "change one parameter".

#### Rules

1. Tabs switch between views of the same object. A segmented control changes one parameter of the current view (unit, period, filter). Never style the two the same way.
2. Use at most 7 tabs. Past that, the content needs a sidebar or separate pages.
3. Tabs are 40px tall, 14px text, 16px horizontal padding, on a 1px `--rule` baseline. The selected tab gets `--ink` text, weight 600, and a 2px `--ink` underline that overlaps the baseline.
4. Reserve the bold width so tabs do not shift when selected: render the label twice and hide the bold copy with zero height.
5. In-page tabs use `role="tablist"`, `role="tab"` with `aria-selected` and `aria-controls`, and `role="tabpanel"`. Arrow keys move between tabs, Home and End jump to the ends, and only the selected tab is in the Tab order.
6. Tabs that change the URL path are links in a `<nav>` with `aria-current="page"`, not ARIA tabs.
7. Segmented controls hold 2 to 4 options, are 32px tall, and are built from radio inputs. The group has a 1px `--ink` border, segments are divided by 1px `--ink` lines, and the checked segment is `--ink` with `--paper` text.
8. Indicator motion is 150ms or less, transform only, and none under reduced motion. No sliding pill.
9. On narrow screens, tabs scroll horizontally on one row. Never wrap tabs onto two rows.

#### Reference build

```html
<div role="tablist" aria-label="Invoice" class="tabs">
  <button role="tab" id="t1" aria-selected="true" aria-controls="p1" data-label="Details">Details</button>
  <button role="tab" id="t2" aria-selected="false" aria-controls="p2" tabindex="-1" data-label="Payments">Payments <span class="tab-n">3</span></button>
  <button role="tab" id="t3" aria-selected="false" aria-controls="p3" tabindex="-1" data-label="History">History</button>
</div>
<div role="tabpanel" id="p1" aria-labelledby="t1" tabindex="0">...</div>

<fieldset class="seg"><legend class="sr-only">Period</legend>
  <label><input type="radio" name="period" value="m" checked><span>Month</span></label>
  <label><input type="radio" name="period" value="q"><span>Quarter</span></label>
  <label><input type="radio" name="period" value="y"><span>Year</span></label>
</fieldset>
```

```css
.tabs { display: flex; gap: 8px; border-bottom: 1px solid var(--rule); overflow-x: auto; }
.tabs [role="tab"] { position: relative; display: inline-flex; flex-direction: column; align-items: center; height: 40px; justify-content: center; padding: 0 16px; margin-bottom: -1px; background: none; border: 0; border-bottom: 2px solid transparent; color: var(--ink-2); font: 14px var(--font-sans); white-space: nowrap; cursor: pointer; }
.tabs [role="tab"]::after { content: attr(data-label); height: 0; overflow: hidden; visibility: hidden; font-weight: 600; }
.tabs [aria-selected="true"] { color: var(--ink); font-weight: 600; border-bottom-color: var(--ink); }
.tabs [role="tab"]:focus-visible { outline: 2px solid var(--focus); outline-offset: -2px; }
.tab-n { font: 12px var(--font-mono); color: var(--ink-3); }
.seg { display: inline-flex; margin: 0; padding: 0; border: 1px solid var(--ink); border-radius: var(--radius); }
.seg label + label { border-left: 1px solid var(--ink); }
.seg input { position: absolute; opacity: 0; }
.seg span { display: block; height: 30px; line-height: 30px; padding: 0 12px; font-size: 14px; cursor: pointer; }
.seg input:checked + span { background: var(--ink); color: var(--paper); }
.seg input:focus-visible + span { outline: 2px solid var(--focus); outline-offset: 2px; }
```

The tab focus ring uses a -2px offset so the scroll container does not clip it.

#### States

- Selected, hover (`--ink` text), focus, disabled (`--ink-3`, `aria-disabled`, skipped by arrows only if it can never become active).
- Panel loading: switch tabs at once and show the panel's own loading state. Never block tab selection on a fetch.

#### Copy

```slop
Overview / Analytics / Insights / More
Yearly -20%
```

- Details / Payments 3 / History
- Month / Quarter / Year
- Billed yearly, $288 per user

#### Checklist

- Tabs and segmented controls look different.
- 7 tabs or fewer, single row, 2px underline on a 1px baseline.
- Bold width reserved, no layout shift.
- Full ARIA tab pattern with roving tabindex.
- No sliding gradient pill.
