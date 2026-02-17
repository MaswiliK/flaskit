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

## Quick Start

### Create an MVP project

```bash
flaskit myapp
```

This generates a minimal Flask app with a single module. Start it with:

```bash
cd myapp
pip install Flask
python main.py
```

Visit `http://127.0.0.1:5000` in your browser.

### Create a SaaS project

```bash
flaskit myapp --template saas --db postgresql
```

This generates a modular blueprint-based app with SQLAlchemy. Start it with:

```bash
cd myapp
pip install -r requirements.txt
python run.py
```

### Include optional files

Add common project files in a single command:

```bash
flaskit myapp --template saas --gitignore --readme --dockerfile --env-file
```

| Flag           | Generates                                      |
|----------------|-------------------------------------------------|
| `--gitignore`  | `.gitignore` with Python defaults               |
| `--readme`     | `README.md` with project name                   |
| `--dockerfile` | `Dockerfile` using `python:3.10-slim`            |
| `--env-file`   | `.env` with `FLASK_APP`, `FLASK_ENV`, and `DB_URL` |

### Open in VS Code

Pass `--vscode` to launch VS Code automatically after generation:

```bash
flaskit myapp --vscode
```

FlaskIt detects `code`, `code-oss`, and `codium` commands across Windows, macOS, and Linux.

## Shell Completion

Install tab-completion for your shell:

```bash
flaskit --install-completion
```

After restarting your shell, `Tab` will complete option names and values (`--template` suggests `mvp`/`saas`, `--db` suggests `sqlite`/`postgresql`).
