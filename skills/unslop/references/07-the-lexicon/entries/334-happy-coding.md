From UNSLOP, Part 7. The Lexicon. All chapters: `references/INDEX.md`.

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
