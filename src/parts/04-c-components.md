### 4.12 Data tables

#### What the machine produces

```slop
<div className="overflow-hidden rounded-xl border bg-white shadow-sm">
  <table className="w-full text-sm">
    <thead className="bg-gray-50 text-xs uppercase tracking-wider text-gray-500">
      <tr><th className="px-6 py-3 text-left">Customer</th><th className="px-6 py-3 text-center">Amount</th><th>Status</th><th /></tr>
    </thead>
    <tbody className="divide-y">
      <tr className="odd:bg-white even:bg-gray-50 hover:bg-indigo-50">
        <td className="flex items-center gap-3 px-6 py-4"><Avatar /> <div><p className="font-medium">Olivia Martin</p><p className="text-gray-500">olivia.martin@email.com</p></div></td>
        <td className="text-center">$1,999.00</td>
        <td><span className="rounded-full bg-green-100 px-2.5 py-0.5 text-green-700">Success</span></td>
        <td><MoreHorizontal /></td>
      </tr>
```

The shadcn data table demo: "Olivia Martin, olivia.martin@email.com, $1,999.00, Success". Uppercase tracked headers, centered amounts, zebra stripes and divider lines at once, a 64px row height from `py-4` plus a two-line cell, a pastel status pill and a "..." button with no label.

#### Rules

1. Numbers align right and use `font-variant-numeric: tabular-nums`. Text aligns left. Nothing is centered except single-character columns.
2. Units go in the header, not in every cell: "Amount (EUR)".
3. Row height 40px default, 32px compact, 48px only for rows with two-line cells. Cell padding 0 12px.
4. Header: `--paper-2` fill, 14px weight 600, sentence case, `position: sticky; top: 0`. No uppercase tracking.
5. Rows separated by 1px `--rule` lines. No zebra stripes when rules are present. No vertical rules below 8 columns.
6. Sortable headers are buttons inside `th`, with `aria-sort` on the `th` and a 12px arrow drawn in SVG showing the direction.
7. Row hover: `--paper-2`. Selected: `--paper-3` plus a checked checkbox in the first column.
8. Status is a word in a column, colored by token (see 4.4), not a pill.
9. On narrow screens, the table scrolls horizontally inside a container with `tabindex="0"` and a label; the first column sticks to the left.
10. Pagination names the range: "Rows 51 to 100 of 1,284". Changing pages keeps sort and filters.
11. Row actions: a labelled menu button ("Actions for invoice 1042") in the last column, 32px square.

#### Reference build

```html
<div class="table-wrap" tabindex="0" role="region" aria-label="Invoices, 1,284 rows">
  <table class="table">
    <thead>
      <tr>
        <th scope="col">Invoice</th>
        <th scope="col">Customer</th>
        <th scope="col" class="num" aria-sort="descending"><button type="button">Amount (EUR)</button></th>
        <th scope="col">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>1042</td><td>Halden Freight</td><td class="num">4,180.00</td><td class="bad">12 days late</td></tr>
      <tr><td>1041</td><td>Oru Studio</td><td class="num">960.50</td><td>Paid 9 Oct</td></tr>
    </tbody>
  </table>
</div>
<p class="table-range">Rows 1 to 50 of 1,284</p>
```

```css
.table-wrap { overflow-x: auto; border: 1px solid var(--rule); max-height: 70vh; }
.table-wrap:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.table { width: 100%; border-collapse: collapse; font-size: 14px; }
.table th, .table td { height: 40px; padding: 0 12px; text-align: left; border-bottom: 1px solid var(--rule); white-space: nowrap; }
.table thead th { position: sticky; top: 0; background: var(--paper-2); font-weight: 600; color: var(--ink); }
.table th:first-child, .table td:first-child { position: sticky; left: 0; background: var(--paper); }
.table thead th:first-child { background: var(--paper-2); z-index: 1; }
.table .num { text-align: right; font-variant-numeric: tabular-nums; }
.table th button { font: inherit; color: inherit; background: none; border: 0; padding: 0; cursor: pointer; }
.table th button:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.table tbody tr:hover td { background: var(--paper-2); }
.table tbody tr[aria-selected="true"] td { background: var(--paper-3); }
.table .bad { color: var(--bad); }
.table-range { font-size: 14px; color: var(--ink-2); font-variant-numeric: tabular-nums; }
```

#### States

- Loading the first page: header renders at once; the body shows one row reading "Loading invoices" for up to 1 second, then rows of `--paper-2` blocks at real column widths.
- Empty: see 4.16. Headers stay visible.
- Error: one full-width row: "Could not load invoices. Retry." Filters remain applied.

#### Copy

```slop
Showing 1-10 of 100 results
No data available
Status: Success
```

- Rows 1 to 50 of 1,284
- No invoices match "Halden" and "Late". Clear filters
- Paid 9 Oct / 12 days late / Draft

#### Checklist

- Numbers right-aligned in tabular figures; units in headers.
- 40px rows, sticky `--paper-2` header, sentence case.
- Rules or stripes, never both.
- `aria-sort` on sortable headers; labelled row action buttons.

### 4.13 Date pickers

#### What the machine produces

```slop
<Popover>
  <PopoverTrigger asChild>
    <Button variant="outline" className="w-[280px] justify-start rounded-xl text-left font-normal">
      <CalendarIcon className="mr-2 h-4 w-4" />
      {date ? format(date, "PPP") : <span>Pick a date</span>}
    </Button>
  </PopoverTrigger>
  <PopoverContent className="w-auto rounded-2xl p-0 shadow-xl">
    <Calendar mode="single" selected={date} onSelect={setDate} classNames={{ day_selected: "rounded-full bg-indigo-600 text-white" }} />
  </PopoverContent>
</Popover>
```

The shadcn date picker, used for every date field including date of birth, where it starts at today and takes 40 clicks back to reach 1986. The trigger is a button, so the date cannot be typed or pasted. The selected day is an `indigo-600` circle.

#### Rules

1. Typing comes first. Every date field accepts text, shows the expected format above the field ("DD/MM/YYYY", matching the locale) and parses common variants (3/11/2026, 3 Nov 2026, 2026-11-03).
2. After parsing, echo the date in words under the field: "Tuesday 3 November 2026". This catches day and month swaps.
3. Dates far from today (birth dates, passport expiry) use three fields (day, month, year) or one text field. No calendar.
4. A calendar is for picking near-future dates where the weekday matters: bookings, deadlines. It opens from a 32px button next to the field, labelled "Choose date".
5. Grid cells 40px square, 14px tabular figures. The week starts on the locale's first day.
6. Today: 1px `--rule-strong` border. Selected: `--ink` fill with `--paper` text. Ranges: `--paper-3` fill between the ends. Unavailable: `--ink-3` text with a strike-through and `aria-disabled`.
7. Keyboard per the WAI-ARIA date picker dialog pattern: arrows move by day and week, Page Up and Down by month, Home and End to week edges, Enter selects, Esc closes.
8. State limits in text before the person hits them: "Delivery dates from 20 Oct to 20 Dec".

#### Reference build

```html
<div class="field">
  <label for="due">Due date</label>
  <p class="hint" id="due-hint">DD/MM/YYYY. From 20 Oct to 20 Dec 2026.</p>
  <div class="date-row">
    <input id="due" class="input" inputmode="numeric" autocomplete="off" aria-describedby="due-hint due-echo" value="03/11/2026">
    <button class="btn btn-secondary btn-sm" type="button" aria-haspopup="dialog">Choose date</button>
  </div>
  <p class="echo" id="due-echo" aria-live="polite">Tuesday 3 November 2026</p>
</div>
```

```css
.date-row { display: flex; gap: 8px; align-items: center; }
.date-row .input { width: 12ch; }
.echo { margin: 4px 0 0; font-size: 14px; color: var(--ink-2); }
.cal button { width: 40px; height: 40px; border: 1px solid transparent; border-radius: var(--radius); background: none; }
.cal button[aria-current="date"] { border-color: var(--rule-strong); }
.cal button[aria-selected="true"] { background: var(--ink); color: var(--paper); }
```

#### States

- Valid: the echo line shows the full date.
- Unparseable: "Could not read 31/02/2026. February has 28 days in 2026." in `--bad` under the field, on blur.
- Out of range: "Choose a date between 20 Oct and 20 Dec." with the range repeated, not "Invalid date".

#### Copy

```slop
Pick a date
Invalid date
Select date range
```

- Due date (DD/MM/YYYY)
- Tuesday 3 November 2026
- Choose a date between 20 Oct and 20 Dec.

#### Checklist

- Typed input with a visible format; parsed variants; date echoed in words.
- No calendar for birth dates or dates years away.
- 40px cells, today outlined, selected filled with ink.
- Keyboard per the APG date picker dialog.

### 4.14 Dialogs and modals

#### What the machine produces

```slop
<div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-sm animate-in fade-in duration-300" />
<div className="fixed left-1/2 top-1/2 z-50 w-full max-w-md -translate-x-1/2 -translate-y-1/2 rounded-2xl bg-white p-6 shadow-2xl animate-in zoom-in-95 duration-300">
  <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-red-100">
    <AlertTriangle className="h-6 w-6 text-red-600" />
  </div>
  <h2 className="mt-4 text-center text-lg font-semibold">Are you absolutely sure?</h2>
  <p className="mt-2 text-center text-sm text-gray-500">This action cannot be undone.</p>
  <div className="mt-6 flex gap-3"><Button variant="outline">Cancel</Button><Button variant="destructive">Continue</Button></div>
</div>
```

The shadcn `AlertDialog` copy ("Are you absolutely sure? This action cannot be undone.") with a blurred scrim, a 300ms zoom, centered text and an icon in a red circle. "Continue" does not say what will be deleted. The dialog is a div, so focus can escape to the page behind.

#### Rules

1. Use `<dialog>` with `showModal()`. It traps focus, makes the page inert, closes on Esc and has a `::backdrop`.
2. Widths: 480px for confirmations, 640px for short forms, 800px maximum.
3. 1px `--rule-strong` border, `--paper` fill, `var(--radius)`. Scrim `rgb(20 20 18 / 0.5)`. No blur.
4. Title 21px weight 600, left-aligned, naming the object: "Delete invoice 1042?"
5. Body states the consequence in numbers: what is lost, what is kept, whether it can be undone.
6. Buttons right-aligned, 8px apart, cancel first, action last. The action label repeats the verb and the object.
7. Initial focus: the first field in a form dialog; the cancel button in a destructive confirmation.
8. Esc and the cancel button close. A click on the scrim closes only when nothing is typed.
9. On close, focus returns to the element that opened the dialog.
10. Open with a 120ms opacity change. No zoom, no slide.
11. Prefer undo over confirmation for reversible actions. Confirm only what cannot be undone.

#### Reference build

```html
<dialog class="dialog" id="del" aria-labelledby="del-title" aria-describedby="del-body">
  <form method="dialog">
    <h2 id="del-title">Delete invoice 1042?</h2>
    <p id="del-body">The PDF and 3 payment reminders are deleted. The customer record and the ledger entry stay. You cannot undo this.</p>
    <div class="dialog-actions">
      <button class="btn btn-secondary" value="cancel" autofocus>Cancel</button>
      <button class="btn btn-danger" value="delete">Delete invoice 1042</button>
    </div>
  </form>
</dialog>
```

```css
.dialog {
  width: min(480px, calc(100vw - 32px)); max-height: 85vh; padding: 24px;
  color: var(--ink); background: var(--paper);
  border: 1px solid var(--rule-strong); border-radius: var(--radius);
}
.dialog[open] { animation: dialog-in 120ms ease-out; }
.dialog::backdrop { background: rgb(20 20 18 / 0.5); }
.dialog h2 { margin: 0 0 8px; font: 600 21px/1.25 var(--font-sans); }
.dialog p { margin: 0; color: var(--ink-2); max-width: 60ch; }
.dialog-actions { display: flex; justify-content: flex-end; gap: 8px; margin-top: 24px; }
.btn-danger { background: var(--bad); color: var(--accent-ink); }
.btn-danger:hover { background: color-mix(in srgb, var(--bad) 88%, var(--ink)); }
@keyframes dialog-in { from { opacity: 0; } to { opacity: 1; } }
@media (prefers-reduced-motion: reduce) { .dialog[open] { animation: none; } }
```

#### States

- Submitting: the action button shows "Deleting..." with `aria-busy`; cancel stays enabled until the request is sent.
- Error: the message appears inside the dialog above the buttons, in `--bad`, and the dialog stays open.
- Unsaved changes: Esc asks once, in place: "Discard changes to this form? Discard / Keep editing".

#### Copy

```slop
Are you absolutely sure?
This action cannot be undone.
Continue
```

- Delete invoice 1042?
- The PDF and 3 payment reminders are deleted. The ledger entry stays. You cannot undo this.
- Cancel / Delete invoice 1042

#### Checklist

- Native `dialog` with `showModal`, focus returned on close.
- 480, 640 or 800px; solid scrim; no blur, no zoom.
- Title names the object; body gives consequences in numbers.
- Action label repeats verb and object.

### 4.15 Dropdown menus

#### What the machine produces

```slop
<Listbox value={selected} onChange={setSelected}>
  <Listbox.Button className="relative w-full rounded-xl border bg-white py-3 pl-4 pr-10 text-left shadow-sm focus:ring-4 focus:ring-indigo-500/20">
    {selected?.name ?? "Select an option..."}
    <ChevronUpDownIcon className="absolute right-3 top-3.5 h-5 w-5 text-gray-400" />
  </Listbox.Button>
  <Transition>
    <Listbox.Options className="absolute mt-2 max-h-60 w-full overflow-auto rounded-xl bg-white py-1 shadow-lg ring-1 ring-black/5">
      {options.map((o) => <Listbox.Option value={o} className="ui-active:bg-indigo-600 ui-active:text-white">{o.name}<CheckIcon className="text-indigo-600" /></Listbox.Option>)}
    </Listbox.Options>
  </Transition>
</Listbox>
```

The Headless UI listbox from the Tailwind UI examples, rebuilt for a field with 3 options that should have been radio buttons. `ring-4 ring-indigo-500/20` is the halo focus ring of every Tailwind form, and the active row inverts to solid `indigo-600`.

#### Rules

1. Match the control to the option count: 2 to 5, radio buttons (4.9); 6 to 15, a native `<select>`; more than 15, or options people search by name, a combobox. Action menus are in 4.25.
2. Style the native select: `appearance: none`, 40px tall, 1px `--ink-3` border, 2px radius, 12px left padding, 32px right padding for the chevron.
3. The placeholder is a real first option with an empty value: "Choose a country". Required selects do not preselect a guess.
4. Custom listbox panels: at least the trigger's width, at most 320px tall, 1px `--rule-strong` border, `--paper` fill, 4px gap below the trigger.
5. Option rows 36px, 14px text. The selected option shows a 16px check drawn in SVG on the left and weight 600. The keyboard-active option gets `--paper-3`. No solid accent fill on the active row.
6. Group long lists with non-selectable headings (`optgroup` natively). Put the 3 to 5 most used options in a "Frequent" group at the top.
7. Flip above the trigger when there is less than 320px below it.

#### Reference build

```html
<div class="field">
  <label for="country">Country</label>
  <div class="select">
    <select id="country" name="country" required autocomplete="country">
      <option value="">Choose a country</option>
      <optgroup label="Frequent">
        <option value="DE">Germany</option>
        <option value="FR">France</option>
      </optgroup>
      <optgroup label="All countries">
        <option value="AT">Austria</option>
        <option value="BE">Belgium</option>
      </optgroup>
    </select>
  </div>
</div>
```

```css
.select { position: relative; max-width: 320px; }
.select select {
  appearance: none; width: 100%; height: 40px; padding: 0 32px 0 12px;
  font: 16px var(--font-sans); color: var(--ink); background: var(--paper);
  border: 1px solid var(--ink-3); border-radius: var(--radius); cursor: pointer;
}
.select::after {
  content: ""; position: absolute; right: 14px; top: 50%; width: 6px; height: 6px;
  border-right: 1.5px solid var(--ink-2); border-bottom: 1.5px solid var(--ink-2);
  transform: translateY(-70%) rotate(45deg); pointer-events: none;
}
.select select:hover { border-color: var(--ink); }
.select select:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.select select:invalid { color: var(--ink-3); }
.select select[aria-invalid="true"] { border-color: var(--bad); }
.select select:disabled { opacity: 0.45; cursor: not-allowed; }
```

#### States

- Hover: border from `--ink-3` to `--ink`.
- Focus-visible: 2px outline at 2px offset, no colored halo.
- Placeholder showing: `--ink-3` text via `:invalid` on a required select.
- Error: `--bad` border plus a text line below (see 4.19).

#### Copy

```slop
Select an option...
Please select
-- Select --
```

- Choose a country
- Choose a VAT rate (19%, 7% or 0%)
- Frequent / All countries

#### Checklist

- Radios for up to 5, native select to 15, combobox beyond.
- Native select styled, not replaced, where possible.
- Placeholder is an empty first option; no preselected guess on required fields.
- Selected marked with check and weight; active row in `--paper-3`.

### 4.16 Empty states

#### What the machine produces

```slop
<div className="flex flex-col items-center justify-center py-24 text-center">
  <div className="mb-6 flex h-24 w-24 animate-bounce items-center justify-center rounded-full border-2 border-dashed border-indigo-200 bg-indigo-50">
    <Rocket className="h-10 w-10 text-indigo-500" />
  </div>
  <h3 className="text-xl font-semibold">No projects yet</h3>
  <p className="mt-2 text-gray-500">Get started by creating your first project. It only takes a few seconds!</p>
  <Button className="mt-6 bg-gradient-to-r from-indigo-500 to-purple-500">+ Create Project</Button>
</div>
```

A bouncing rocket in a dashed indigo circle, centered in 192px of vertical padding, with copy that says "get started" and a promise about seconds. The same block appears for a new account, for a search with no matches and for a failed load, which are three different situations.

#### Rules

1. Write a separate state for each cause: first use, no results for a filter, everything done (inbox zero), no permission, failed to load.
2. Keep the frame. An empty table keeps its header row; an empty list keeps its toolbar and filters. The empty message sits where the first row would be.
3. Left-align the message with the content, 16px text, max 52ch.
4. Three parts at most: what will appear here, why it is empty now, one action. Two sentences and one button.
5. No illustrations taller than 120px, no animation, no mascots.
6. For filtered results, print the active filters and offer "Clear filters" plus the closest broad search.
7. For first use, offer the fastest real path in: import from a file, connect an account, or a sample dataset that is labelled as sample and removable in one click.
8. For no permission, name who can grant it: "Ask an admin (Mira Kowalski) for Billing access."

#### Reference build

```html
<table class="table">
  <thead><tr><th scope="col">Invoice</th><th scope="col">Customer</th><th scope="col" class="num">Amount (EUR)</th></tr></thead>
  <tbody>
    <tr><td colspan="3" class="empty">
      <p><strong>No invoices match Halden Freight and Late.</strong> 214 invoices exist for other filters.</p>
      <button class="btn btn-secondary btn-sm" type="button">Clear filters</button>
    </td></tr>
  </tbody>
</table>
```

```css
.empty { height: auto; padding: 24px 12px; white-space: normal; }
.empty p { margin: 0 0 12px; max-width: 52ch; color: var(--ink-2); }
.empty strong { color: var(--ink); font-weight: 600; }
```

#### States

- First use: action is primary.
- No results: action is secondary; the filters stay editable above.
- Done: no action at all. "All 38 invoices for October are paid."
- Error: "Could not load invoices. Retry." with the error code in `--ink-3`.

#### Copy

```slop
No data yet
Nothing to see here!
It looks like you don't have any projects yet. Get started by creating your first project.
```

- Invoices you create or import appear here. Import a CSV from your old tool, or create one.
- No invoices match Halden Freight and Late. Clear filters
- All 38 invoices for October are paid.

#### Checklist

- One state per cause, each with its own text.
- Table headers, toolbars and filters stay visible.
- Left-aligned, two sentences, one action.
- No large illustration, no animation.

### 4.17 File upload

#### What the machine produces

```slop
<div className="flex flex-col items-center justify-center rounded-2xl border-2 border-dashed border-gray-300 bg-gray-50 p-12 transition hover:border-indigo-500 hover:bg-indigo-50">
  <div className="mb-4 rounded-full bg-indigo-100 p-4"><CloudUpload className="h-8 w-8 text-indigo-600" /></div>
  <p className="text-lg font-medium">Drag & drop your files here</p>
  <p className="text-sm text-gray-500">or <span className="text-indigo-600 underline">click to browse</span></p>
  <p className="mt-2 text-xs text-gray-400">Supports: PNG, JPG, GIF up to 10MB</p>
  <div className="mt-4 h-2 w-full rounded-full bg-gray-200"><div className="h-2 rounded-full bg-gradient-to-r from-indigo-500 to-purple-500" style={{ width: `${progress}%` }} /></div>
</div>
```

The react-dropzone demo: a dashed `rounded-2xl` box with a cloud icon in a circle, "click to browse" as a span that is not a button, limits in `gray-400` at 12px (about 2.5:1), and one gradient progress bar for all files together.

#### Rules

1. The control is a real `<input type="file">` behind a visible button, "Choose files". Drag and drop is an addition on top, not the only path; on touch devices it does not exist.
2. State limits before upload, in `--ink-2` at 14px: types, size per file, file count. "PDF or PNG, up to 20 MB each, 10 files at most."
3. Set `accept` to the same types, and validate type and size on the client before sending.
4. Drop zone: 1px solid `--rule` border on `--paper-2`, 24px padding, left-aligned text. On `dragover`, `--paper-3` fill and `--rule-strong` border.
5. One row per file: name, size, progress as a percentage and a 4px bar, and a per-file "Cancel" or "Remove" button.
6. Errors are per file and say why: "scan-03.tiff: TIFF is not accepted. Convert to PDF or PNG." The other files continue.
7. Do not clear the list on an error, and do not lose the files on a failed form submit.

#### Reference build

```html
<div class="upload" data-drag="false">
  <label class="btn btn-secondary" for="files">Choose files</label>
  <input id="files" type="file" multiple accept=".pdf,.png,application/pdf,image/png" class="visually-hidden" aria-describedby="files-limits">
  <p id="files-limits">Or drop them here. PDF or PNG, up to 20 MB each, 10 files at most.</p>
</div>
<ul class="files">
  <li><span class="f-name">contract-2026.pdf</span><span class="f-size">4.2 MB</span>
    <progress max="100" value="64">64%</progress><span class="f-pct">64%</span>
    <button type="button" class="btn-tertiary btn">Cancel</button></li>
  <li class="is-error"><span class="f-name">scan-03.tiff</span>
    <span class="f-msg">TIFF is not accepted. Convert to PDF or PNG.</span>
    <button type="button" class="btn-tertiary btn">Remove</button></li>
</ul>
```

```css
.upload { display: flex; flex-wrap: wrap; align-items: center; gap: 12px 16px; padding: 24px; background: var(--paper-2); border: 1px solid var(--rule); border-radius: var(--radius); }
.upload[data-drag="true"] { background: var(--paper-3); border-color: var(--rule-strong); }
.upload p { margin: 0; font-size: 14px; color: var(--ink-2); }
.upload:focus-within { outline: 2px solid var(--focus); outline-offset: 2px; }
.visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
.files { margin: 8px 0 0; padding: 0; list-style: none; font-size: 14px; }
.files li { display: grid; grid-template-columns: 1fr auto 120px 4ch auto; align-items: center; gap: 12px; min-height: 40px; border-bottom: 1px solid var(--rule); }
.files .f-size, .files .f-pct { color: var(--ink-2); font-variant-numeric: tabular-nums; text-align: right; }
.files progress { width: 120px; } /* bar colors as in 4.24 */
.files .is-error { grid-template-columns: 1fr 2fr auto; }
.files .f-msg { color: var(--bad); }
```

#### States

- Drag over: `--paper-3` and strong border, no scale.
- Uploading: per-file percentage, cancel available.
- Done: the bar is replaced by the text "Uploaded".
- Error: per-file reason in `--bad` and a remove button; other files continue.

#### Copy

```slop
Drag & drop your files here or click to browse
Supports: PNG, JPG, GIF up to 10MB
Upload failed
```

- Choose files
- Or drop them here. PDF or PNG, up to 20 MB each, 10 files at most.
- scan-03.tiff: TIFF is not accepted. Convert to PDF or PNG.

#### Checklist

- Native file input behind a real button; drop is optional.
- Limits printed before upload at 4.5:1 contrast; `accept` set.
- One row per file with size, percentage and cancel.
- Errors per file with the reason; nothing cleared on failure.

### 4.18 Footers

#### What the machine produces

```slop
<footer className="border-t bg-gradient-to-b from-white to-gray-50">
  <div className="mx-auto grid max-w-7xl grid-cols-2 gap-8 px-6 py-16 md:grid-cols-6">
    <div className="col-span-2">
      <Logo />
      <p className="mt-4 text-sm text-gray-500">Making the world a better place through constructing elegant hierarchies.</p>
      <div className="mt-6 flex gap-4">{socials.map((s) => <a className="rounded-full bg-gray-100 p-2 hover:bg-indigo-100"><s.icon className="h-5 w-5" /></a>)}</div>
    </div>
  </div>
  <p className="py-8 text-center text-xs text-gray-400">&copy; 2024 Acme Inc. All rights reserved. Made with <Heart className="inline h-3 w-3 text-red-500" /> in San Francisco</p>
</footer>
```

The Tailwind UI footer with its own placeholder tagline (`Making the world a better place through constructing elegant hierarchies`, a line from the TV series Silicon Valley), social icons in grey circles, four columns of links that lead to `#`, a hardcoded copyright year and "Made with a heart".

#### Rules

1. The footer holds what people scroll to the bottom to find: contact, legal pages, system status, the company's legal name and address, and a short site map. Nothing promotional.
2. At most 4 link columns, each with a 14px weight 600 heading and up to 7 links. Links 14px, 32px row pitch so touch targets clear 24px.
3. Background `--paper-2` with a 1px `--rule` top border. 48px top padding, 32px bottom.
4. Social links are text ("GitHub", "LinkedIn"), or 20px stroke icons with an `aria-label`. No circles.
5. The legal line names the entity and where it is registered where required: "Halden Software GmbH, Torstrasse 12, 10119 Berlin. HRB 123456 B." Germany and Austria require an imprint page; link it as "Imprint".
6. Compute the copyright year from the build or server date. "All rights reserved" has no legal effect under the Berne Convention; leave it out.
7. Remove every link that points to `#`.

#### Reference build

```html
<footer class="footer">
  <nav class="footer-cols" aria-label="Footer">
    <div><h2>Product</h2><ul><li><a href="/pricing">Pricing</a></li><li><a href="/changelog">Changelog</a></li><li><a href="https://status.halden.example">Status</a></li></ul></div>
    <div><h2>Company</h2><ul><li><a href="/about">About</a></li><li><a href="/jobs">Jobs (3 open)</a></li><li><a href="mailto:hello@halden.example">hello@halden.example</a></li></ul></div>
    <div><h2>Legal</h2><ul><li><a href="/terms">Terms</a></li><li><a href="/privacy">Privacy</a></li><li><a href="/imprint">Imprint</a></li></ul></div>
  </nav>
  <p class="footer-legal">&copy; 2026 Halden Software GmbH, Torstrasse 12, 10119 Berlin. HRB 123456 B.</p>
</footer>
```

```css
.footer { background: var(--paper-2); border-top: 1px solid var(--rule); padding: 48px 16px 32px; font-size: 14px; }
.footer-cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 32px; max-width: 1080px; margin: 0 auto; }
.footer h2 { margin: 0 0 8px; font: 600 14px/1.25 var(--font-sans); color: var(--ink); }
.footer ul { margin: 0; padding: 0; list-style: none; }
.footer li { line-height: 32px; }
.footer a { color: var(--ink-2); text-underline-offset: 3px; }
.footer a:hover { color: var(--ink); }
.footer a:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.footer-legal { max-width: 1080px; margin: 32px auto 0; padding-top: 16px; border-top: 1px solid var(--rule); color: var(--ink-3); }
```

#### States

- Links: underlined, `--ink-2`, `--ink` on hover, 2px outline on focus-visible.

#### Copy

```slop
Made with love in San Francisco
© 2024 Acme Inc. All rights reserved.
Stay in the loop! Subscribe to our newsletter.
```

- Halden Software GmbH, Torstrasse 12, 10119 Berlin. HRB 123456 B.
- Status (all systems running at 14:30 UTC)
- Monthly changelog, 1 email. Unsubscribe in one click.

#### Checklist

- Contact, legal, status, address; no slogans.
- 4 columns at most, 14px links on 32px rows.
- Social links as text or labelled 20px icons.
- Year computed; "All rights reserved" removed.
