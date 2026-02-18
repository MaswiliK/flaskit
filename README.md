<p align="center">
  <img src="docs/assets/logo.png" alt="FlaskIt" width="480">
</p>

<p align="center">
  Scaffold a production-ready Flask backend in seconds.<br>
  <b>MVP or SaaS — you choose.</b>
</p>

<p align="center">
  <i>Stop configuring. Start building.</i>
</p>

---
![CI](https://github.com/MaswiliK/flaskit/actions/workflows/ci.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/flaskit)
![Python](https://img.shields.io/pypi/pyversions/flaskit)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

## ✨ What is FlaskIt?

**FlaskIt** is a CLI that instantly generates a clean, organized Flask project structure — so you can skip boilerplate and go straight to writing features.

Instead of spending 2–6 hours setting up:

* folders
* blueprints
* configs
* environment files
* database wiring

You run **one command**.

```
flaskit create myapp
```

Done.

FlaskIt creates a ready-to-run backend with sensible defaults and a scalable architecture.

You can choose:

* ⚡ **MVP** → quick prototype / hackathon / learning
* 🏗️ **SaaS** → modular, scalable production structure

---

## 📦 Installation

### From PyPI

```bash
pip install flaskit
```

### From source

```bash
git clone https://github.com/MaswiliK/flaskit.git
cd flaskit
pip install -e .
```

---

## 🚀 2-Second Demo

See FlaskIt generate and run a backend automatically:

```bash
flaskit demo
```

This will:

1. Create `hello-flaskit/`
2. Install Flask (if missing)
3. Start the dev server

Then open:

```
http://127.0.0.1:5000
```

You now have a working backend.

---

## 🧠 Commands

### Create a project

```
flaskit create <project_name> [OPTIONS]
```

| Option         | Default  | Description                  |
| -------------- | -------- | ---------------------------- |
| `--template`   | `mvp`    | `mvp` or `saas`              |
| `--db`         | `sqlite` | `sqlite` or `postgresql`     |
| `--gitignore`  |          | Include `.gitignore`         |
| `--readme`     |          | Include project README       |
| `--dockerfile` |          | Include Dockerfile           |
| `--env-file`   |          | Include `.env` configuration |
| `--vscode`     |          | Open project in VS Code      |

---

### Bootstrap a project

```
flaskit up [OPTIONS]
```

Run this from inside a generated project directory. It handles everything in one shot:

1. Create `.venv/` virtual environment
2. Install dependencies from `requirements.txt`
3. Create `.env` (copies `.env.example` if present, otherwise writes defaults)
4. Initialise the database
5. Run migrations (if `migrations/` exists)
6. Start the dev server

| Option           | Description                               |
| ---------------- | ----------------------------------------- |
| `--skip-venv`    | Skip virtual environment creation         |
| `--skip-deps`    | Skip dependency installation              |
| `--skip-db`      | Skip database initialisation              |
| `--skip-migrate` | Skip migrations                           |
| `--no-server`    | Bootstrap without starting the dev server |

---

### Demo project

```
flaskit demo
```

Creates and runs a working Flask project.
Press **Ctrl + C** to stop the server.

---

## 🧪 Examples

Create a minimal prototype:

```bash
flaskit create myapp
```

Create a scalable SaaS backend:

```bash
flaskit create myapp --template saas --db postgresql --gitignore --readme --dockerfile --env-file --vscode
```

---

## ⌨️ Shell Autocomplete

Enable tab completion:

```bash
flaskit --install-completion
```

Then `Tab` will autocomplete:

* commands (`create`, `demo`, `up`)
* template types (`mvp`, `saas`)
* database options

---

## 🧱 Templates

### ⚡ MVP Template

A simple Flask app ideal for learning and rapid prototypes.

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

---

### 🏗️ SaaS Template

Blueprint-based modular architecture with app factory & SQLAlchemy.

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
    ├── Feature3/
    ├── templates/
    │   └── base.html
    ├── static/
    └── tests/
        └── test_app.py
```

---

## 🤝 Contributing

Pull requests are welcome.
Ideas, feature requests, and improvements are encouraged.

If FlaskIt helped you — consider ⭐ starring the repo.

---

## 📄 License

MIT
