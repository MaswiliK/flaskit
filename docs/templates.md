# Templates

FlaskIt ships with two project templates: **MVP** and **SaaS**.

## MVP Template

A single-module Flask app for quick prototyping and small projects.

```bash
flaskit create myapp --template mvp
```

### Structure

```
myapp/
├── main.py                 # Entry point — runs the dev server
└── app/
    ├── __init__.py         # App instance, config, and view import
    ├── views.py            # Route definitions (imports render_template)
    ├── auth.py             # Auth placeholder with register_routes()
    ├── models.py           # SQLAlchemy model placeholder
    ├── forms.py            # WTForms placeholder
    ├── templates/
    │   └── layout.html     # Base Jinja2 template with {% block content %}
    └── static/
        ├── css/
        ├── js/
        └── images/
```

### How it works

- `main.py` imports the `app` instance from `app/__init__.py` and calls `app.run(debug=True)`.
- `app/__init__.py` creates a plain `Flask(__name__)` instance, sets `SECRET_KEY`, and imports `views`.
- `views.py` defines a single `/` route. It imports `render_template` so you can start using Jinja2 templates immediately.
- `auth.py` provides a `register_routes(app)` stub — fill in login/register logic when ready.
- `templates/layout.html` is a minimal Jinja2 base template with `{% block content %}`.

### When to use

- Prototyping and learning
- Small single-purpose apps
- Scripts with a web interface

---

## SaaS Template

A modular blueprint-based app with an app factory, SQLAlchemy, and feature modules.

```bash
flaskit create myapp --template saas --db postgresql
```

### Structure

```
myapp/
├── run.py                      # Entry point — creates and runs the app
├── config.py                   # BaseConfig with SECRET_KEY, DB URI, etc.
├── requirements.txt            # Flask + Flask_SQLAlchemy
└── app/
    ├── __init__.py             # App factory with blueprint registration
    ├── extensions.py           # SQLAlchemy db instance
    ├── auth/
    │   ├── routes.py           # Auth blueprint with /auth/login route
    │   ├── models.py           # User/Role models (imports db)
    │   └── forms.py            # WTForms for auth
    ├── Feature1/
    │   ├── routes.py           # Feature1 blueprint
    │   ├── models.py           # Feature1 models (imports db)
    │   └── services.py         # Business logic
    ├── Feature2/
    │   └── ...                 # Same structure as Feature1
    ├── Feature3/
    │   └── ...                 # Same structure as Feature1
    ├── templates/
    │   └── base.html           # Base Jinja2 template with {% block body %}
    ├── static/
    └── tests/
        └── test_app.py         # Pytest placeholder
```

### How it works

- `run.py` calls `create_app()` from the app factory and runs the server on `0.0.0.0`.
- `app/__init__.py` contains the `create_app()` factory that:
  1. Loads config from `config.BaseConfig`
  2. Initializes SQLAlchemy via `db.init_app(app)`
  3. Registers the `auth` blueprint directly
  4. Registers `Feature1`, `Feature2`, `Feature3` blueprints inside `try/except` blocks so missing features don't crash the app
- `config.py` reads `SECRET_KEY` and `DB_URL` from environment variables with sensible defaults.
- `extensions.py` holds the shared `db = SQLAlchemy()` instance imported by all model files.
- Each feature module (`auth`, `Feature1`, etc.) is a self-contained blueprint with its own routes, models, and services.

### When to use

- Multi-feature web applications
- Projects that will grow over time
- Team projects where features can be developed in parallel
- Apps that need a database from the start

---

## Database Options

Both templates support the `--db` flag:

| Value          | Effect                                                      |
|----------------|-------------------------------------------------------------|
| `sqlite`       | Default. Sets `DB_URL=sqlite:///app.db` in `.env` and config. |
| `postgresql`   | Sets `DB_URL=postgresql://username:password@localhost:5432/dbname`. |

The SaaS template always includes `Flask_SQLAlchemy` in `requirements.txt`. The MVP template does not generate a `requirements.txt` — install Flask manually.
