# FlaskIt

Flask Project Generator CLI — Just flask it.

Scaffold production-ready Flask projects from your terminal in seconds. Choose between a lightweight **MVP** template or a modular **SaaS** template with blueprints, SQLAlchemy, and an app factory.

## Installation

```bash
pip install flaskit
```

Or install from source:

```bash
git clone https://github.com/MaswiliK/flaskit.git
cd flaskit
pip install -e .
```

## Usage

```bash
flaskit <project_name> [OPTIONS]
```

### Options

| Option         | Default    | Description                          |
|----------------|------------|--------------------------------------|
| `--template`   | `mvp`      | Template to use: `mvp` or `saas`     |
| `--db`         | `sqlite`   | Database: `sqlite` or `postgresql`   |
| `--gitignore`  |            | Include a `.gitignore` file          |
| `--readme`     |            | Include a `README.md` file           |
| `--dockerfile` |            | Include a `Dockerfile`               |
| `--env-file`   |            | Include a `.env` file                |
| `--vscode`     |            | Open project in VS Code after creation |

### Examples

Create a minimal MVP project:

```bash
flaskit myapp
```

Create a SaaS project with all extras and open in VS Code:

```bash
flaskit myapp --template saas --db postgresql --gitignore --readme --dockerfile --env-file --vscode
```

### Shell Completion

Install tab-completion for your shell:

```bash
flaskit --install-completion
```

Once installed, pressing `Tab` will autocomplete option names, `--template` values (`mvp`, `saas`), and `--db` values (`sqlite`, `postgresql`).

## Templates

### MVP

A single-module Flask app for quick prototyping.

```
myapp/
├── main.py
└── app/
    ├── __init__.py
    ├── views.py
    ├── auth.py
    ├── models.py
    ├── forms.py
    ├── templates/
    │   └── layout.html
    └── static/
        ├── css/
        ├── js/
        └── images/
```

### SaaS

A blueprint-based modular structure with an app factory, SQLAlchemy, and feature modules.

```
myapp/
├── run.py
├── config.py
├── requirements.txt
└── app/
    ├── __init__.py
    ├── extensions.py
    ├── auth/
    │   ├── routes.py
    │   ├── models.py
    │   └── forms.py
    ├── Feature1/
    │   ├── routes.py
    │   ├── models.py
    │   └── services.py
    ├── Feature2/
    │   └── ...
    ├── Feature3/
    │   └── ...
    ├── templates/
    │   └── base.html
    ├── static/
    └── tests/
        └── test_app.py
```

## License

MIT
