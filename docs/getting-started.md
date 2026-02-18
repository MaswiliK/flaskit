# Getting Started

## Prerequisites

- Python 3.8 or higher
- pip

## Installation

Install from PyPI:

```bash
pip install flaskit
```

Or install from source for development:

```bash
git clone https://github.com/MaswiliK/flaskit.git
cd flaskit
pip install -e .
```

Verify the installation:

```bash
flaskit --help
```

## Quick Demo

The fastest way to see FlaskIt in action:

```bash
flaskit demo
```

This scaffolds a `hello-flaskit/` MVP project, installs Flask if it's missing, and starts the dev server at `http://127.0.0.1:5000`. Press `Ctrl+C` to stop. The generated project stays on disk for you to explore.

## Creating Projects

### MVP project

```bash
flaskit create myapp
```

### SaaS project

```bash
flaskit create myapp --template saas --db postgresql
```

### Include optional files

Add common project files in a single command:

```bash
flaskit create myapp --template saas --gitignore --readme --dockerfile --env-file
```

| Flag           | Generates                                          |
|----------------|----------------------------------------------------|
| `--gitignore`  | `.gitignore` with Python defaults                  |
| `--readme`     | `README.md` with project name                      |
| `--dockerfile` | `Dockerfile` using `python:3.10-slim`              |
| `--env-file`   | `.env` with `FLASK_APP`, `FLASK_ENV`, and `DB_URL` |

### Open in VS Code

Pass `--vscode` to launch VS Code automatically after generation:

```bash
flaskit create myapp --vscode
```

FlaskIt detects `code`, `code-oss`, and `codium` commands across Windows, macOS, and Linux.

## Bootstrapping with `flaskit up`

After creating a project, run `flaskit up` from inside it to get fully running in one step:

```bash
flaskit create myapp --template saas --db sqlite
cd myapp
flaskit up
```

`flaskit up` runs six steps in order:

| Step | What it does |
|------|--------------|
| 1 | Creates a `.venv/` virtual environment |
| 2 | Installs dependencies from `requirements.txt` (or Flask if there's no requirements file) |
| 3 | Creates a `.env` file (copies `.env.example` if it exists, otherwise writes sensible defaults) |
| 4 | Initialises the database via `db.create_all()` |
| 5 | Runs migrations if a `migrations/` directory exists |
| 6 | Starts the dev server at `http://127.0.0.1:5000` |

Steps are idempotent — running `flaskit up` a second time skips anything that already exists.

### Skip flags

| Flag             | Effect                                       |
|------------------|----------------------------------------------|
| `--skip-venv`    | Don't create the virtual environment         |
| `--skip-deps`    | Don't install dependencies                   |
| `--skip-db`      | Don't initialise the database                |
| `--skip-migrate` | Don't run migrations                         |
| `--no-server`    | Bootstrap without starting the dev server    |

## Shell Completion

Install tab-completion for your shell:

```bash
flaskit --install-completion
```

After restarting your shell, `Tab` will complete commands (`create`, `demo`, `up`), option names, and values (`--template` suggests `mvp`/`saas`, `--db` suggests `sqlite`/`postgresql`).
