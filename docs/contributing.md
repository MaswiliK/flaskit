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
│   ├── cli.py            # Typer CLI — argument parsing, Rich UI, optional files
│   └── generator.py      # Generator class — directory/file creation, item tracking
├── docs/                 # Documentation
│   └── assets/           # Logo and images
├── pyproject.toml        # Package metadata and dependencies
├── README.md
└── .gitignore
```

## Architecture Notes

- **`cli.py`** owns all user-facing I/O: argument parsing, validation, Rich progress/table/panel output, optional file generation, and the VS Code launch logic.
- **`generator.py`** owns project scaffolding: creating directories and writing files. It tracks everything it creates in `generated_items` (list of tuples) which the CLI consumes for the summary table.
- Generated file contents are **inline strings** in `generator.py`, not external template files. If you add a new generated file, add the content as a string directly in the appropriate `generate_*` method.
- The `generated_items` list contains Rich markup (color tags and emoji). This couples Generator to Rich, which is intentional — the CLI consumes it directly.

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
- Test both templates manually (`flaskit testmvp --template mvp` and `flaskit testsaas --template saas`) before submitting.
- Clean up generated test directories after testing.
