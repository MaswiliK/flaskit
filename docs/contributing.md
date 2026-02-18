# Contributing

Contributions are welcome. Here's how to get set up.

## Development Setup

```bash
git clone https://github.com/MaswiliK/flaskit.git
cd flaskit
pip install -e .
```

This installs the `flaskit` command pointing at your local source, so changes take effect immediately.

## Project Layout

```
flaskit/
├── flaskit/
│   ├── __init__.py       # Package marker
│   ├── cli.py            # Typer CLI — commands, Rich UI, optional files
│   └── generator.py      # Generator class — directory/file creation, item tracking
├── docs/                 # Documentation
│   └── assets/           # Logo and images
├── pyproject.toml        # Package metadata and dependencies
├── README.md
└── .gitignore
```

## Architecture Notes

- **`cli.py`** owns all user-facing I/O: the `create`, `demo`, and `up` commands, argument parsing, validation, Rich progress/table/panel output, optional file generation, VS Code launch logic, and autocompletion callbacks.
- **`generator.py`** owns project scaffolding: creating directories and writing files. It tracks everything it creates in `generated_items` (list of tuples) which the CLI consumes for the summary table.
- Generated file contents are **inline strings** in `generator.py`, not external template files. If you add a new generated file, add the content as a string directly in the appropriate `generate_*` method.
- The `generated_items` list contains Rich markup (color tags and emoji). This couples Generator to Rich, which is intentional — the CLI consumes it directly.

## Adding a New Command

1. Add a new `@app.command()` function in `cli.py`.
2. Document it in `README.md` under **Commands** and in `docs/getting-started.md`.

## Adding a New Template

1. Add a `generate_<name>(self, ...)` method to the `Generator` class in `generator.py`.
2. Add the template name to the `complete_template` callback and the validation check in `cli.py`.
3. Wire the new method into the `create` function's `if/else` block.
4. Update `entry_point` logic if the new template uses a different entry file.
5. Add a section to `docs/templates.md`.

## Adding a New Optional File

1. Add a new `typer.Option` flag to the `create` function in `cli.py`.
2. Add the file-writing logic in the "Extra optional files" section of `create`.
3. Update the README options table.

## Pull Requests

- Keep PRs focused on a single change.
- Test both templates manually (`flaskit create testmvp --template mvp` and `flaskit create testsaas --template saas`) before submitting.
- Run `cd testmvp && flaskit up --no-server` to verify the up command works end-to-end.
- Run `flaskit demo` to verify the demo flow still works.
- Clean up generated test directories after testing.

## Writing Commands that Execute Programs (Important)

Some commands (like `flaskit up`) need to run external programs such as `pip`, `flask`, or `alembic`.
To keep FlaskIt reliable across Windows, Linux, and macOS, follow these rules.

### 1. Never use global Python

Always run commands using the project's virtual environment Python, not `python` from PATH.

Use a helper to resolve the interpreter:

| OS          | Python path                  |
| ----------- | ---------------------------- |
| Linux/macOS | `.venv/bin/python`           |
| Windows     | `.venv\\Scripts\\python.exe` |

All subprocess commands must use this interpreter.

---

### 2. Do NOT use `shell=True`

Bad:

```python
subprocess.run("pip install -r requirements.txt", shell=True)
```

Good:

```python
subprocess.run(
    [venv_python, "-m", "pip", "install", "-r", "requirements.txt"],
    check=True
)
```

This prevents quoting bugs and improves security.

---

### 3. Always stop on failure

Use `check=True` in `subprocess.run`.
If a step fails, FlaskIt should stop and show the error instead of continuing.

---

### 4. Use `pathlib`, not string paths

Bad:

```python
".venv/bin/python"
```

Good:

```python
from pathlib import Path
venv_python = Path(".venv") / "bin" / "python"
```

Handle Windows with a small OS check.

---

### 5. Print progress clearly

Commands that take time must show step progress:

```
[1/6] Creating virtual environment...
[2/6] Installing dependencies...
...
```

FlaskIt is designed to feel guided, not silent.

---

### 6. The command must be idempotent

Running `flaskit up` twice should not break the project.

Examples:

* Do not overwrite `.env`
* Do not recreate an existing venv
* Do not delete user data

---

### 7. Test before submitting

From a clean directory:

```
flaskit create sample
cd sample
flaskit up
```

Then open:

http://127.0.0.1:5000

If it runs, the PR is ready 🚀
